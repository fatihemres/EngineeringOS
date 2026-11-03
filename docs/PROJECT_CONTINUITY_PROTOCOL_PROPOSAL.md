# EngineeringOS — Project Continuity, Evidence and Issue Protocol (PROPOSAL)

> **2026-11-03 · PROPOSED / NOT IMPLEMENTED / NOT A PO IMPLEMENTATION APPROVAL**  
> Baseline for the original review: `main` `381033b3a811b639f540b5a4119303367d6864b2`. Re-verify current refs before any action.

## Purpose

EngineeringOS must survive full ChatGPT conversations, changing agents and harnesses, newly discovered libraries and different consumer projects without losing actual authorizations, decisions, negative evidence or unresolved objections. A chat message, GitHub Issue, source document and CI result have distinct roles and evidence authority.

## Source of truth by location

| Location | What it owns |
| --- | --- |
| `docs/DECISIONS.md` | Dated scoped PO decisions; historical entries are immutable and never silently backdated or edited |
| `PROJECT_STATUS.md`, `VALIDATION_REPORT.md`, `docs/NEXT_DECISIONS.md` | Current verified repo checkpoint, tests and remaining gates with older historical stages preserved |
| `ARCHITECTURE.md`, `docs/IMPLEMENTATION_ROADMAP.md` and proposed `docs/CAPABILITY_NETWORK.md` | Architecture and future contracts — not authorization or proof that components run |
| GitHub Issues | Purpose, scope, acceptance criteria, evidence links, blockers and task history; an Issue is not a PO merge decision |
| `capabilities/registry.json` and shipped schemas | Actual v0.1 machine contract and candidate status; proposed edge types are not shipped |
| Separate Private Workspace | Raw transcripts, private code, local paths and environments, customer data, credentials (in external vault), logs and unredacted evidence |
| Public EngineeringOS | Reviewed generic documentation, original source, synthetic tests, redacted and approved reusable contributions |
| ChatGPT Project Instructions and Sources | Version-stamped snapshot/cache — GitHub commits do not automatically import updates to ChatGPT; ChatGPT uploads do not create Git commits |

Project-specific owner authority outranks general EngineeringOS recommendations.

## Issue management

One umbrella Issue per independently bounded initiative, focused linked children only where a discrete reviewable deliverable is justified. Every issue should record purpose, out-of-scope actions, exact source and baseline SHA, who can authorize what, privacy/license risk, verifiable acceptance targets, decisions, tests and the next PO gate. Avoid one Issue for every GitHub star. Category tags are *proposed* and not assumed to be installed GitHub labels.

[Issue #3](https://github.com/fatihemres/EngineeringOS/issues/3) tracks documentation and branch-hygiene proposals; [Issue #4](https://github.com/fatihemres/EngineeringOS/issues/4) P0 capability handoff contracts; [Issue #5](https://github.com/fatihemres/EngineeringOS/issues/5) candidate intake.

## Dated checkpoint and chat rollover

After a real milestone, meaningful owner decision, incident or integration — and before a long chat rollover when useful — verify live GitHub main SHA/tree, PRs/Issues, ruleset, required CI and actual sources. Record dates and evidence classes, including HYPOTHESIS, AGENT_REPORTED, USER_REPORTED, SOURCE_REVIEWED, LOCAL_TEST_VERIFIED, CI_VERIFIED, HUMAN_NATIVE_ACCEPTED and PO_DECISION. Do not turn an agent PASS into a GitHub review or hosted tests into native user acceptance.

A handoff should give:
- generated date, repo/branch, verified main and tree SHA, active Issue/PR and required CI references;
- implemented vs proposed functions, exact refs and limits, unresolved objections and risks;
- PO decisions, **currently scoped permission** and excluded mutations;
- sanitized source map and restricted pointers (not copied raw logs) to private evidence;
- outstanding tests, next owner decision and safe next read-only step;
- ChatGPT Source state `NOT_SYNCED` / `SYNC_PENDING` / `SYNC_VERIFIED` with actual version/hash if known.

In a new chat, read the Project Instructions + latest handoff, then live source and actual code/CI. Earlier planning chat transcripts are historical context, not execution authority.

## Post-merge remote source-branch disposition — PO direction; deletion separately gated

The PO directed that **completed future EngineeringOS work should not leave remote PR source branches accumulating**. The proposed default: after a separately authorized PR merge, independently verify its merged state, exact integration commit/parents/tree and successful strict required **main-push post-merge CI**. Then inspect the source branch's expected tip and ownership, and seek/execute **separate branch-specific deletion authorization** if eligible.

Never delete `main`, a protected, unmerged, diverged, shared, reused or unknown-ownership branch, a branch with unique unpreserved content/evidence, or a branch supporting another open PR. Preserve dated original source-tip SHA, PR and merge receipts, CI run and exact permission. On missing evidence, CI failure or ambiguous deletion result, **stop**; no force delete, bypass, blind retry or silent rollback.

Proposed final task receipt:

`REMOTE_BRANCH_DISPOSITION = DELETED_VERIFIED | PRESERVED_WITH_REASON | CLEANUP_PENDING`

with remote source branch, tip SHA, integrated PR, integration SHA, post-merge CI, eligibility and authorized deletion details. This is a **proposed checklist convention**, not an implemented schema.

**Separate concerns:** local branch and worktree cleanup, temporary build outputs, historical logs and private evidence are deferred until later separately scoped PO permission. Existing remote branches `feat/foundation-v0.1` and `docs/foundation-checkpoint-20261102` are not retroactively approved for deletion. Do **not** silently enable GitHub's `delete_branch_on_merge` setting: its timing is not the same as evidence-gated post-merge cleanup. Other projects retain their own governance.

## Security and publication limits

The project must never silently ingest raw agent transcripts or synchronize another repository's private files. Generalized lessons may reach public core only after redaction, original license/provenance checks, synthetic reproduction as appropriate, human/PO review and separately authorized PR/CI integration. No always-on collection, cloud telemetry, auto-installation, model self-upgrade, background syncing or global settings mutation is implied.

**Acceptance proposal:** a new reader with no prior chat can identify the current verifiable checkpoint, active work, source ownership, withheld evidence, unresolved gates and next PO-controlled action without re-explaining the project.
