# EngineeringOS — Foundation v0.1 (DRAFT / PRE-COMMIT)

**Status:** The public repository at https://github.com/fatihemres/EngineeringOS contains the governance seed on main. Foundation v0.1 supplies draft architecture and a minimal standard-library bootstrap prototype, prepared for draft PR review. Foundation remains unmerged and unreleased.
**Date:** 2026-11-02 · **Owner choices:** Public Core + Private Workspace; Apache License 2.0 for original EngineeringOS Public Core materials. Publication follows the scoped owner authorizations recorded in docs/DECISIONS.md. Integration and release require separate approval.

## Mission

A portable, evolving engineering operating system for frontend/UX, backend, APIs, data modelling, databases, architecture, testing, security, operations and product delivery. Multiple expert viewpoints can propose, criticize and converge; execution evidence and failures feed a reusable experience ledger. The platform can onboard existing or new projects and create a ChatGPT Project instructions/source kit. Project-specific authority and real verification always outrank generic recommendations.

## What works in this draft

- `python tools/engineeringos.py doctor --profile profiles/examples/desktop.profile.json`: **read-only** PATH discovery, no installations, network, git or version execution.
- `python tools/engineeringos.py export-chatgpt --profile profiles/examples/desktop.profile.json --output <empty-dir>`: **dry-run** listing of files to be generated.
- Add `--write` to create four local, reviewable kit files only inside the selected destination. Existing differing files are never overwritten.
- `python tools/engineeringos.py validate-experience --public examples/synthetic-ui-review.json`: publication, schema-subset and provenance checks; **not** a complete security/privacy audit.
- `python -m unittest discover -s tests -v`: local unit checks for the bootstrap prototype.

## What is designed but NOT implemented

Runtime multi-agent orchestration, semantic/graph memory, CLI installers, GitHub issue/PR mutation, ChatGPT Project uploads/sync, skill/MCP provisioning, cross-project auto-sync, full JSON-Schema or license scanning, external contributors, **GitHub Actions executed for EngineeringOS**, native desktop QA. All require separate implementation and verification.

## Recommended reading order

1. `VISION.md` → `ARCHITECTURE.md` → `AGENTS.md`
2. `docs/DECISIONS.md` → `docs/BOOTSTRAP.md` → `docs/MEMORY.md`
3. `docs/ORCHESTRATION.md` → `docs/CONTRIBUTION_PIPELINE.md` → `docs/PRIVACY.md`
4. `templates/chatgpt/MASTER_BOOTSTRAP_PROMPT.md`, sample profile, examples and schemas
5. `docs/IMPLEMENTATION_ROADMAP.md` for proposed increments.

## Public vs private

The public repo is intended to contain original public templates, schemas, publication-reviewed synthetic examples, generic evaluations and **approved** reusable lessons. Project source, credentials, private raw traces, personally identifying data and internal logs reside in a distinct **private workspace**, never mirrored automatically into public Git. Only reviewed sanitized contribution proposals may go upstream.

## Project connections

The desktop profile and UI review record are fictional fixtures. Real project profiles, execution evidence and disclosure decisions stay in the project-controlled private workspace.

## License and contribution gate

The PO approved **Apache License, Version 2.0** for **original EngineeringOS Public Core materials** on 2026-11-02. Read [LICENSE](LICENSE), [NOTICE](NOTICE), [LICENSES_THIRD_PARTY.md](LICENSES_THIRD_PARTY.md) and [the decision register](docs/DECISIONS.md). This license does **not** automatically relicense third-party projects referenced in capability metadata or any proprietary/private project material. Original license decision history is preserved in `docs/DECISIONS.md`.

The six-file governance seed is published. The main-governance ruleset is active and Private Vulnerability Reporting is enabled. The PO authorized Foundation feature-branch publication and a draft PR. Hosted Foundation CI, subsequent independent PR review and PO integration approval remain pending at this source checkpoint. Contributor onboarding, additional required checks and release authorization require separate decisions.
