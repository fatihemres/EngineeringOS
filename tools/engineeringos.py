#!/usr/bin/env python3
"""EngineeringOS v0.1 safe prototype: read-only doctor + deliberate local kit export.

This does NOT install dependencies, call APIs, mutate Git, provision agents,
or upload project sources to ChatGPT.
"""
from __future__ import annotations
import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "0.1"
DENIED_KEY_PARTS = ("password", "token", "secret", "api_key", "private_key", "credential")


class ValidationError(ValueError):
    pass


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def read_json(path: Path) -> dict:
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValidationError("Duplicate JSON object key")
            result[key] = value
        return result

    def invalid_number(value):
        raise ValidationError("Non-finite JSON number")

    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys,
                      parse_constant=invalid_number)
    if not isinstance(data, dict):
        raise ValidationError(f"Expected JSON object: {path}")
    return data


def reject_secret_field_names(obj, path="root"):
    """Heuristic guard only; NOT a comprehensive content/PII or licensing audit."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            key_l = str(key).lower()
            if any(part in key_l for part in DENIED_KEY_PARTS):
                raise ValidationError(f"Potential secret-bearing field at {path}.{key}")
            reject_secret_field_names(value, path + "." + str(key))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            reject_secret_field_names(value, f"{path}[{i}]")


def check_shape(value, rule, path="root"):
    """Offline subset used by the bundled schemas. Unknown keywords fail closed."""
    known = {"$schema", "title", "type", "const", "enum", "required", "properties",
             "additionalProperties", "items", "minItems", "uniqueItems", "contains",
             "minLength", "pattern", "format", "allOf", "if", "then"}
    if rule.keys() - known:
        raise ValidationError("Unsupported bundled schema keyword")
    types = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}
    kinds = rule.get("type", [])
    if isinstance(kinds, str):
        kinds = [kinds]
    if kinds and type(value) not in [types[k] for k in kinds]:
        raise ValidationError(f"{path}: incorrect type")
    if "const" in rule and (type(value) is not type(rule["const"]) or value != rule["const"]):
        raise ValidationError(f"{path}: incorrect constant")
    if "enum" in rule and value not in rule["enum"]:
        raise ValidationError(f"{path}: unsupported value")
    if isinstance(value, dict):
        if set(rule.get("required", [])) - value.keys():
            raise ValidationError(f"{path}: missing required field")
        fields = rule.get("properties", {})
        for key, child in value.items():
            constraint = fields.get(key, rule.get("additionalProperties", True))
            if constraint is False:
                raise ValidationError(f"{path}: unexpected field")
            if isinstance(constraint, dict):
                check_shape(child, constraint, f"{path}.{key}")
    if isinstance(value, list):
        if len(value) < rule.get("minItems", 0):
            raise ValidationError(f"{path}: too few entries")
        if rule.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            raise ValidationError(f"{path}: duplicate entry")
        if "items" in rule:
            for i, child in enumerate(value):
                check_shape(child, rule["items"], f"{path}[{i}]")
        if "contains" in rule and not any(matches_shape(x, rule["contains"]) for x in value):
            raise ValidationError(f"{path}: missing supporting evidence")
    if isinstance(value, str):
        if len(value) < rule.get("minLength", 0) or ("pattern" in rule and not re.search(rule["pattern"], value)):
            raise ValidationError(f"{path}: invalid text")
        if rule.get("format") == "date":
            try:
                if date.fromisoformat(value).isoformat() != value:
                    raise ValueError
            except ValueError:
                raise ValidationError(f"{path}: invalid ISO date") from None
    for part in rule.get("allOf", []):
        check_shape(value, part, path)
    if "if" in rule and matches_shape(value, rule["if"]):
        check_shape(value, rule["then"], path)


def matches_shape(value, rule):
    try:
        check_shape(value, rule)
        return True
    except ValidationError:
        return False


def validate_record(record, schema):
    reject_secret_field_names(record)
    path = ROOT / "schemas" / (schema + ".schema.json")
    check_plain_path(path)
    check_shape(record, read_json(path))


def validate_profile(profile):
    validate_record(profile, "project-profile")
    docs = profile["source_docs"]
    if len({p.casefold() for p in docs}) != len(docs):
        raise ValidationError("Duplicate source document on case-insensitive filesystems")


def validate_experience(item, public=False):
    validate_record(item, "experience")
    if item["status"] == "SYNTHETIC_FIXTURE" and item["provenance"]["source_ref"] != "fixture:" + item["id"]:
        raise ValidationError("Synthetic provenance must reference its own fixture ID")
    if public and (item["privacy"] != "PUBLIC_REUSABLE" or
                   item.get("reviewed_for_publication") is not True or item["status"] != "SYNTHETIC_FIXTURE"):
        raise ValidationError("Public examples require reviewed, public synthetic fixtures")


def validate_registry(record):
    validate_record(record, "registry")
    ids = [row["id"] for row in record["capabilities"]]
    if len(ids) != len(set(ids)):
        raise ValidationError("Duplicate capability ID")


def validate_core(record):
    validate_record(record, "core")


def render_kit(profile: dict) -> dict[str, bytes]:
    validate_profile(profile)
    proj = profile["project"]
    privacy = profile.get("privacy") or {}
    template = (ROOT / "templates/chatgpt/PROJECT_INSTRUCTIONS.template.md").read_text(encoding="utf-8")
    # Free-form metadata stays in PROJECT_PROFILE.json. Only constrained values enter instructions.
    fields = {
        "PROJECT_REPOSITORY": proj["repository"],
        "NETWORK_DEFAULT": privacy.get("external_network_default", "off"),
        "PRODUCTION_TESTING": privacy.get("production_data_testing", "prohibited"),
    }

    def substitute(match):
        if match[1] not in fields:
            raise ValidationError("Unknown instructions template field")
        return fields[match[1]]

    template = re.sub(r"\{\{([^{}]+)\}\}", substitute, template)
    source_lines = [
        "# Project Source Map (generated draft)", "",
        "Actual files and live refs MUST be verified within the current project. These are desired repo paths, not downloaded content:", "",
    ]
    source_lines.extend(f"- `{path}` — project-owned source, presence/version not yet verified." for path in profile["source_docs"])
    source_lines.extend(["", "Priority: current owner decisions and real repo/test evidence > project documents > pinned EngineeringOS defaults > external skill guidance.", "The generated kit is NOT synced to ChatGPT Project Sources."])
    result = {
        "PROJECT_INSTRUCTIONS.md": template.rstrip().encode("utf-8") + b"\n",
        "PROJECT_SOURCE_MAP.md": ("\n".join(source_lines) + "\n").encode("utf-8"),
        "PROJECT_PROFILE.json": (json.dumps(profile, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8"),
    }
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "engineeringos_package": "local-v0.1-draft-not-released",
        "project_repository": proj["repository"],
        "chatgpt_sources_sync_status": "NOT_SYNCED",
        "repo_sources_verification_status": "NOT_FETCHED",
        "source_docs": profile["source_docs"],
        "generated_files_sha256": {path: sha256(data) for path, data in result.items()},
    }
    result["SOURCE_MANIFEST.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return result


def check_plain_path(path):
    for entry in (*reversed(path.parents), path):
        try:
            info = entry.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
            raise ValidationError("Refusing linked or redirected path")


def reserved_name(part):
    # os.path.isreserved is available from Python 3.13 onward.
    if hasattr(os.path, "isreserved"):
        return os.path.isreserved(part)
    return Path(part).is_reserved()


def ensure_safe_target(output):
    path = output.expanduser().absolute()
    if os.name == "nt":
        if path.drive.startswith("\\\\") or any(
            part.endswith((".", " ")) or ":" in part or reserved_name(part)
            for part in path.parts[1:]
        ):
            raise ValidationError("Unsafe Windows output path")
    if ".." in path.parts:
        raise ValidationError("Output path must not contain parent traversal")
    check_plain_path(path)
    path = path.resolve()
    if path.is_relative_to(ROOT) or (path.exists() and not path.is_dir()):
        raise ValidationError("Choose an output directory outside the public source tree")
    return path


def write_kit(output, files):
    output = ensure_safe_target(output)
    pending = []
    for name, data in files.items():
        path = output / name
        check_plain_path(path)
        if path.exists():
            if not path.is_file() or path.read_bytes() != data:
                raise ValidationError("Existing file differs or is not a regular file")
        else:
            pending.append((path, data))
    output.mkdir(parents=True, exist_ok=True)
    for path, data in pending:
        check_plain_path(path)
        # Publish only complete bytes. Hard-link creation cannot replace a competing file.
        temp = tempfile.NamedTemporaryFile(dir=output, delete=False)
        scratch = Path(temp.name)
        try:
            with temp:
                temp.write(data)
            check_plain_path(path)
            try:
                os.link(scratch, path)
            except FileExistsError:
                check_plain_path(path)
                if not path.is_file() or path.read_bytes() != data:
                    raise ValidationError("A competing writer created a different file")
        finally:
            scratch.unlink()


def doctor(args) -> int:
    profile = read_json(args.profile)
    validate_profile(profile)
    commands = ("git", "gh", "python", "node", "npm", "rustc", "cargo", "dotnet", "swift", "codex", "claude")
    report = {
        "status": "DISCOVERY_ONLY_NOT_VERSION_VERIFIED",
        "project": profile["project"]["name"],
        "network_used": False,
        "installations_performed": False,
        "commands_executed": False,
        "tools": {cmd: {"path_found": bool(shutil.which(cmd)), "version_verified": False} for cmd in commands},
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def export_chatgpt(args) -> int:
    profile = read_json(args.profile)
    result = render_kit(profile)
    output = ensure_safe_target(args.output)
    print(f"Mode: {'WRITE LOCAL FILES' if args.write else 'DRY RUN'} | output: {output}")
    for path, data in result.items():
        print(f"  {path}: sha256={sha256(data)}")
    if not args.write:
        print("No files written. No network, git, installations or ChatGPT Project sync.")
        return 0
    write_kit(output, result)
    print("Local kit created/confirmed. ChatGPT Project sync status: NOT_SYNCED")
    return 0


def check_json(args) -> int:
    jobs = [(ROOT / "engineeringos.json", validate_core),
            (ROOT / "capabilities/registry.json", validate_registry)]
    for folder, validator in [("schemas", None), ("profiles/examples", validate_profile),
                              ("examples", lambda item: validate_experience(item, public=True))]:
        directory = ROOT / folder
        check_plain_path(directory)
        paths = sorted(directory.glob("*.json"))
        if not paths:
            raise ValidationError(f"No public JSON files in {folder}")
        jobs.extend((path, validator) for path in paths)
    for path, validator in jobs:
        check_plain_path(path)
        record = read_json(path)
        if validator:
            validator(record)
    print(f"Public JSON files parsed: {len(jobs)}. Bundled schema and semantic checks passed.")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    d = subs.add_parser("doctor", help="read-only command PATH discovery")
    d.add_argument("--profile", type=Path, required=True)
    e = subs.add_parser("export-chatgpt", help="dry-run or create a local Project Kit")
    e.add_argument("--profile", type=Path, required=True)
    e.add_argument("--output", type=Path, required=True)
    e.add_argument("--write", action="store_true", help="explicitly create local kit files; never overwrite differences")
    v = subs.add_parser("validate-experience", help="basic fields and provenance validator")
    v.add_argument("path", type=Path)
    v.add_argument("--public", action="store_true", help="require a publication-reviewed synthetic fixture")
    subs.add_parser("check-json", help="parse bundled JSON documents")
    args = parser.parse_args(argv)
    try:
        if args.command == "doctor": return doctor(args)
        if args.command == "export-chatgpt": return export_chatgpt(args)
        if args.command == "validate-experience":
            examples = ROOT / "examples"
            public = args.public or args.path.absolute().is_relative_to(examples) or args.path.resolve().is_relative_to(examples)
            if public:
                check_plain_path(args.path.absolute())
            validate_experience(read_json(args.path), public=public)
            context = "Public fixture" if public else "Experience record"
            print(f"{context} validation passed: {args.path}")
            return 0
        if args.command == "check-json": return check_json(args)
    except (OSError, ValueError, RecursionError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
