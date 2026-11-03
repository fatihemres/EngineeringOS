# Bootstrap Contract v0.1

Goal: make a new/existing project *ready to work* while preserving its local authority and avoiding false installation claims.

## States

`DISCOVERED` → `PROFILED` → `DOCTOR_CHECKED` → `PLAN_REVIEWED` → `AUTHORIZED` → `PROVISIONED` → `VERIFIED` → `READY`.

`BLOCKED` may interrupt any state. A dry-run cannot reach `PROVISIONED`, and exporting text cannot mean ChatGPT Project files were actually uploaded.

## Policy and idempotence
- Read live project repo and its native contracts first. Project-specific restrictions win.
- Project profile pins EngineeringOS and capability versions; no `latest` auto-upgrade.
- `doctor` never executes discovered binaries or sends network requests; a PATH hit proves only discoverability, **not** version, safety, compatibility or successful installation.
- Prepare explicit proposed installs, permission scopes, file targets, dependencies, rollback and verification. No implicit install, account authorization, hook, global settings or repo mutations.
- `export-chatgpt` dry-runs by default; `--write` writes a local output package only, refuses different existing files and does not upload to ChatGPT.
- Actual host environment checks, git status/CI, desktop interactions and connector availability must be verified independently.

## Capability-aware readiness (proposed)

A future bootstrap can select *only* project-relevant, source-pinned candidates by role and the [Capability Network](CAPABILITY_NETWORK.md). See [intake protocol](CAPABILITY_INTAKE_PROTOCOL_PROPOSAL.md). PATH discovery is not a verified installation, and kit export is not real ChatGPT Project Sources import. Installation, network, secrets, hooks and project settings remain independently gated.


## Local prototype commands

```bash
python tools/engineeringos.py doctor --profile profiles/examples/desktop.profile.json
python tools/engineeringos.py export-chatgpt --profile profiles/examples/desktop.profile.json --output ~/example-kit
python tools/engineeringos.py export-chatgpt --profile profiles/examples/desktop.profile.json --output ~/example-kit --write
python tools/engineeringos.py validate-experience --public examples/synthetic-ui-review.json
python -m unittest discover -s tests -v
```

The `~/example-kit` destination expands to an external directory under the current user home. The default command previews it without creating files. Choose a different trusted external path if needed.

The sample project profile is a **source-scope example**, not a live Windows environment report. `--write` to your own chosen path is a separate deliberate user action.

## Outputs for future full bootstrap
Project diagnosis, authority map, source manifest, proposed selected capabilities, least-privilege installation plan, approval receipts, actual setup/test logs, ChatGPT Source Kit, Project Readiness Report, update/rollback manifest and contribution policy. Each item records `PROPOSED` vs `VERIFIED`.

## ChatGPT Project limit
ChatGPT Projects support project instructions and added sources but local source kit generation is **not** equivalent to adding/updating those sources within the ChatGPT UI. Export outputs must be manually imported or updated through a separately verified supported connector/host flow; record last imported version/hash.


## Validation and export limits

The CLI reads the bundled schemas offline with a standard-library subset for object fields, exact types, arrays, constants, enums, patterns, dates and conditional evidence requirements. It also checks case-insensitive source paths, unique capability IDs and publication context. It is not a general Draft 2020-12 implementation. Registry lifecycle values are CANDIDATE, RESEARCHED and ON_HOLD. Registration does not authorize installation or establish a license.

R1 retains schema_version 0.1 for compatible records but deliberately rejects previously accepted unsafe input. Export profiles require true governance flags, portable relative document names and prohibited production-data testing. Real-world authorizations belong in the private project policy. Published fixtures require synthetic provenance. Private experience records use the general validation context. Verified states require a matching receipt. Earlier registry type aliases and project-specific state labels were migrated.

Choose a trusted external output directory on a filesystem supporting hard links. The exporter preflights all destinations, publishes complete files without overwriting competing writers, and permits retry after partial completion. Keep the directory and its ancestors under the same trusted user's control throughout export.
