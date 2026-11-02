# EngineeringOS — Foundation v0.1 (MERGED / UNRELEASED)

**Status · 2026-11-02:** Foundation v0.1 is merged into main through [PR #1](https://github.com/fatihemres/EngineeringOS/pull/1) at commit [f1860b21fc580afc080ba1583635ee514fbd989c](https://github.com/fatihemres/EngineeringOS/commit/f1860b21fc580afc080ba1583635ee514fbd989c). The [main-push validation](https://github.com/fatihemres/EngineeringOS/actions/runs/41498102378) succeeded on Windows and Ubuntu. Foundation supplies architecture, core scaffolding and a minimal standard-library bootstrap prototype; it remains **unreleased**, with no tag or release authorized.
**Date:** 2026-11-02 · **Owner choices:** Public Core + Private Workspace; Apache License 2.0 for original EngineeringOS Public Core materials. Publication follows the scoped owner authorizations recorded in docs/DECISIONS.md. Foundation integration received separate approval; future integrations and releases require their own scoped authorization.

## Mission

A portable, evolving engineering operating system for frontend/UX, backend, APIs, data modelling, databases, architecture, testing, security, operations and product delivery. Multiple expert viewpoints can propose, criticize and converge; execution evidence and failures feed a reusable experience ledger. The platform can onboard existing or new projects and create a ChatGPT Project instructions/source kit. Project-specific authority and real verification always outrank generic recommendations.

## What works in Foundation

- `python tools/engineeringos.py doctor --profile profiles/examples/desktop.profile.json`: **read-only** PATH discovery, no installations, network, git or version execution.
- `python tools/engineeringos.py export-chatgpt --profile profiles/examples/desktop.profile.json --output <empty-dir>`: **dry-run** listing of files to be generated.
- Add `--write` to create four local, reviewable kit files only inside the selected destination. Existing differing files are never overwritten.
- `python tools/engineeringos.py validate-experience --public examples/synthetic-ui-review.json`: publication, schema-subset and provenance checks; **not** a complete security/privacy audit.
- `python -m unittest discover -s tests -v`: local unit checks for the bootstrap prototype.

## What is designed but NOT implemented

Runtime multi-agent orchestration, remote provisioning, semantic/graph memory, CLI installers, GitHub issue/PR mutation, ChatGPT Project uploads/sync, skill/MCP provisioning, cross-project auto-sync, full JSON-Schema or license scanning, external contributors, native desktop QA. All require separate implementation and verification.

**Historical PR evidence:** Hosted GitHub Actions validation passed on Windows and Ubuntu for Foundation Draft PR #1 at revision `07d57e411d8980dc8ba292483996bb6ded788c72`. The [historical run](https://github.com/fatihemres/EngineeringOS/actions/runs/41480277276) verifies that revision; each subsequent revision needs its own CI verification. Hosted CI does not authorize Foundation integration or release.

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

Governance Stages A and B are complete: main-governance (#26365625) requires PRs and strict Windows/Ubuntu checks from GitHub Actions App ID 15368, with zero required approvals and no bypass actors. Deletion and non-fast-forward restrictions remain active; Private Vulnerability Reporting is enabled. Independent agent review, CI and explicit PO authorization preceded the Foundation merge. Agent review is not a GitHub human approval. Contributor onboarding, additional governance and release decisions remain separately gated. See [current status](PROJECT_STATUS.md), [verification](VALIDATION_REPORT.md) and [remaining decisions](docs/NEXT_DECISIONS.md).

**Historical source checkpoint (before PR CI, review and integration):** The PO had authorized feature-branch publication and a Draft PR; hosted CI, subsequent independent review and PO integration approval were still pending. That earlier pending state is superseded by the dated integration record above.
