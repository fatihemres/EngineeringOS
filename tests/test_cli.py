import json
import os
import shlex
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch
import unittest

from tools import engineeringos as cli

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "engineeringos.py"
PROFILE_PATH = ROOT / "profiles" / "examples" / "desktop.profile.json"


def call(*args):
    return subprocess.run([sys.executable, str(CLI), *map(str, args)], capture_output=True, text=True, check=False)


class BootstrapTests(unittest.TestCase):
    def test_doctor_is_discovery_only(self):
        res = call("doctor", "--profile", PROFILE_PATH)
        self.assertEqual(res.returncode, 0, res.stderr)
        payload = json.loads(res.stdout)
        self.assertFalse(payload["network_used"])
        self.assertFalse(payload["installations_performed"])
        self.assertFalse(payload["commands_executed"])
        self.assertTrue(all(not d["version_verified"] for d in payload["tools"].values()))

    def test_export_default_is_dry_run(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "kit"
            res = call("export-chatgpt", "--profile", PROFILE_PATH, "--output", target)
            self.assertEqual(res.returncode, 0, res.stderr)
            self.assertFalse(target.exists())

    def test_explicit_write_and_idempotence(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "kit"
            args = ("export-chatgpt", "--profile", PROFILE_PATH, "--output", target, "--write")
            first = call(*args)
            self.assertEqual(first.returncode, 0, first.stderr)
            files = {p.name: p.read_bytes() for p in target.iterdir()}
            self.assertEqual(set(files), {"PROJECT_INSTRUCTIONS.md", "PROJECT_PROFILE.json", "PROJECT_SOURCE_MAP.md", "SOURCE_MANIFEST.json"})
            manifest = json.loads((target / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["chatgpt_sources_sync_status"], "NOT_SYNCED")
            second = call(*args)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual({p.name: p.read_bytes() for p in target.iterdir()}, files)
            (target / "PROJECT_INSTRUCTIONS.md").write_text("changed", encoding="utf-8")
            third = call(*args)
            self.assertEqual(third.returncode, 2)
            self.assertEqual((target / "PROJECT_INSTRUCTIONS.md").read_text(), "changed")

    def test_profile_rejects_secret_named_field(self):
        with tempfile.TemporaryDirectory() as temp:
            item = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
            item["api_token"] = "example"
            bad = Path(temp) / "bad.json"
            bad.write_text(json.dumps(item), encoding="utf-8")
            res = call("doctor", "--profile", bad)
            self.assertEqual(res.returncode, 2)
            self.assertIn("secret-bearing", res.stderr)

    def test_example_experience_basic_validation(self):
        res = call("validate-experience", "--public", ROOT / "examples" / "synthetic-ui-review.json")
        self.assertEqual(res.returncode, 0, res.stderr)

    def test_json_syntax(self):
        self.assertEqual(call("check-json").returncode, 0)

    def test_malformed_profile_returns_controlled_error(self):
        profile = cli.read_json(PROFILE_PATH)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "profile.json"
            for value in ["strict", ["off"], None]:
                profile["privacy"] = value
                path.write_text(json.dumps(profile), encoding="utf-8")
                for args in [("doctor",), ("export-chatgpt", "--output", Path(temp) / "kit")]:
                    with self.subTest(privacy=value, command=args[0]):
                        result = call(*args, "--profile", path)
                        self.assertEqual(result.returncode, 2)
                        self.assertNotIn("Traceback", result.stderr)

    def test_export_preserves_all_free_text_only_as_profile_data(self):
        profile = cli.read_json(PROFILE_PATH)
        collision = "{{NETWORK_DEFAULT}}"
        profile["governance"]["notes"] = collision
        profile["project"]["name"] = "{{PROJECT_REPOSITORY}}"
        kit = cli.render_kit(profile)
        self.assertEqual(json.loads(kit["PROJECT_PROFILE.json"]), profile)
        self.assertNotIn(collision.encode(), kit["PROJECT_INSTRUCTIONS.md"])
        self.assertNotIn(b"{{PROJECT_REPOSITORY}}", kit["PROJECT_SOURCE_MAP.md"])
        self.assertIn(profile["project"]["repository"].encode(), kit["PROJECT_INSTRUCTIONS.md"])

    def test_json_scope_ignores_unrelated_directories(self):
        import shutil
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for folder in ["capabilities", "schemas", "profiles", "examples"]:
                shutil.copytree(ROOT / folder, root / folder)
            shutil.copyfile(ROOT / "engineeringos.json", root / "engineeringos.json")
            for folder in [".git", "node_modules", "out/kit", ".engineeringos/private", "__pycache__"]:
                directory = root / folder
                directory.mkdir(parents=True)
                (directory / "bad.json").write_text("invalid", encoding="utf-8")
            with patch.object(cli, "ROOT", root):
                self.assertEqual(cli.check_json(None), 0)
                published = root / "examples" / "unreviewed.json"
                sample = cli.read_json(root / "examples" / "synthetic-ui-review.json")
                sample["reviewed_for_publication"] = False
                published.write_text(json.dumps(sample), encoding="utf-8")
                with self.assertRaises(cli.ValidationError):
                    cli.check_json(None)
                self.assertEqual(cli.main(["validate-experience", str(published)]), 2)

    def test_extra_evidence_and_receipt_rules(self):
        sample = cli.read_json(ROOT / "examples" / "synthetic-ui-review.json")
        sample["evidence"][0]["reference"] = "unverified-ci-run"
        with self.assertRaises(cli.ValidationError):
            cli.validate_experience(sample, public=True)
        sample.update(id="TEST-CI", status="CI_VERIFIED", privacy="PROJECT_INTERNAL",
                      reviewed_for_publication=False)
        sample["provenance"] = {"origin": "test", "source_ref": "run-001"}
        sample["evidence"] = [{"type": "ci_run", "description": "Test receipt"}]
        with self.assertRaises(cli.ValidationError):
            cli.validate_experience(sample)
        sample["evidence"][0]["reference"] = "receipt-001"
        cli.validate_experience(sample)
        sample["unrecognized"] = False
        with self.assertRaises(cli.ValidationError):
            cli.validate_experience(sample)

    def test_all_destinations_preflight_before_writes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "last").write_bytes(b"existing")
            with self.assertRaises(cli.ValidationError):
                cli.write_kit(root, {"first": b"x", "last": b"y"})
            self.assertEqual(list(root.iterdir()), [root / "last"])
            self.assertEqual((root / "last").read_bytes(), b"existing")

    def test_dry_run_and_export_never_execute_tools_or_connect(self):
        with (
            tempfile.TemporaryDirectory() as temp,
            patch("socket.socket", side_effect=AssertionError),
            patch("subprocess.Popen", side_effect=AssertionError),
        ):
            output = Path(temp) / "kit"
            args = ["export-chatgpt", "--profile", str(PROFILE_PATH), "--output", str(output)]
            self.assertEqual(cli.main(args), 0)
            self.assertFalse(output.exists())
            self.assertEqual(cli.main([*args, "--write"]), 0)
            stamps = {f.name: f.stat().st_mtime_ns for f in output.iterdir()}
            self.assertEqual(cli.main([*args, "--write"]), 0)
            self.assertEqual(stamps, {f.name: f.stat().st_mtime_ns for f in output.iterdir()})

    def test_documented_export_destination_is_safe_in_dry_run(self):
        lines = (ROOT / "docs" / "BOOTSTRAP.md").read_text(encoding="utf-8").splitlines()
        commands = [shlex.split(line) for line in lines
                    if line.startswith("python tools/engineeringos.py export-chatgpt ")]
        self.assertEqual(len(commands), 2)
        self.assertEqual(sum("--write" in command for command in commands), 1)
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            env = {**os.environ, "HOME": temp, "USERPROFILE": temp}
            for command in commands:
                with self.subTest(command=command):
                    output = command[command.index("--output") + 1]
                    self.assertEqual(output, "~/example-kit")
                    with patch.dict(os.environ, env):
                        target = cli.ensure_safe_target(Path(output))
                    self.assertEqual(target, home.resolve() / "example-kit")
                    self.assertFalse(target.is_relative_to(ROOT))
                    args = [part for part in command[2:] if part != "--write"]
                    result = subprocess.run(
                        [sys.executable, "-B", str(CLI), *args],
                        capture_output=True, text=True, env=env,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn("DRY RUN", result.stdout)
                    self.assertFalse(target.exists())
            self.assertEqual(list(home.iterdir()), [])

    def test_documented_parent_traversal_form_stays_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            parent = Path(temp)
            cwd = parent / "working"
            cwd.mkdir()
            sentinel = parent / "sentinel"
            sentinel.write_bytes(b"preserve")
            result = subprocess.run(
                [sys.executable, "-B", str(CLI), "export-chatgpt", "--profile",
                 str(PROFILE_PATH), "--output", "../example-kit"],
                cwd=cwd, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn(result.stderr.strip(), (
                "ERROR: Unsafe Windows output path",
                "ERROR: Output path must not contain parent traversal",
            ))
            self.assertNotIn("Traceback", result.stderr)
            self.assertFalse((parent / "example-kit").exists())
            self.assertEqual(sentinel.read_bytes(), b"preserve")
            self.assertEqual(set(parent.iterdir()), {cwd, sentinel})
            self.assertEqual(list(cwd.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
