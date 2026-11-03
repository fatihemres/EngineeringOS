# EngineeringOS — External Capability Intake (PROPOSAL)

> **2026-11-03 · PROPOSED / NOT IMPLEMENTED / NO AUTOMATIC ADOPTION**  
> Research tracker: [Issue #5](https://github.com/fatihemres/EngineeringOS/issues/5)

## What a new repo or Star List export means

A star, README, list assignment or local executable is **discovery evidence only**. It does not establish safety, maintenance, actual usefulness, permitted installation, compatible runtime, exact version, redistribution rights or EngineeringOS adoption. The user's PowerShell scripts/JSON/CSV exports are untrusted; inspect rather than execute them, and do not publish sensitive local paths, access tokens, private repository identities, personal inventory or unredacted logs.

The PO supplied a dated snapshot of 55 starred repos and 9 then-existing lists. A 13-list reorganization was subsequently **user-reported as completed**, not independently verified here. This personal inventory is not automatically public. A GitHub list is organizational metadata, **not** an EngineeringOS role, license or tool-compatibility assessment.

## Candidate research card

| Field | Minimal information |
| --- | --- |
| Identity | Stable ID, canonical owner/repo HTTPS URL, observed date, verified commit/tag if known |
| Purpose | What the tool does and what category it belongs to: skill, MCP, CLI, framework, library, harness, model or reference |
| Roles | Engineering responsibilities and possible primary/secondary duties |
| Typed edges | `ALTERNATIVE_TO`, `COMPLEMENTS`, `PRODUCES_FOR`, `CONSUMES_CONTEXT_FROM`, `CRITIQUES`, `VALIDATES`, `REVIEWS_CODE_AFTER` with reason and provenance |
| Environment | OS/language/harness/runtime, dependencies, network/secret/telemetry permissions, offline support |
| Provenance & license | Actual source/ref, license/third-party rights, maintainer status, supply-chain and data egress risks; UNKNOWN until checked |
| Evidence | Source review vs reported results vs isolated local/CI tests and human native acceptance kept separate |
| Failure record | Failed attempts, limitations, contradictory findings and applicability boundaries |
| Lifecycle | Shipped v0.1 only supports `CANDIDATE`, `RESEARCHED`, `ON_HOLD`; broader states are proposals, not machine fields |
| Follow-up | Related Issue, experience ID, owner decision and separately authorized pilot/PR |

## Pipeline

1. Receive supplied script and export with date and source, check for tokens/private data, and **do not execute** the script without a task-specific approval.
2. Normalize repository identities, deduplicate, preserve source categories and distinguish user-supplied descriptions from independently checked content.
3. Group by role: UI/UX, motion, backend/API, database, systems architecture, performance, security, testing/evaluation, memory, research, code navigation, agent collaboration, platform and DevEx.
4. Review chosen source refs and licenses. An external README is untrusted and is not a security or integration audit.
5. Propose relationships under the [Capability Network](CAPABILITY_NETWORK.md). Ponytail is an **optional code review/simplification candidate**, not UI art direction; Graphify is code context; Context7 external version-aware docs; Graphiti remains an experimental on-hold memory candidate.
6. Run bounded synthetic pilots **only with separately granted install/network/runner permission**, recording exact commands, source SHA and evidence. Do not rank tools from unequal tasks.
7. Request PO adoption, trial, hold or retirement decision. New capabilities are not automatically installed, activated or pushed to any project.
8. Promote public learnings only after source/license check, redaction, synthetic reproducer and human/PO review, through separately authorized Issue/PR/CI. Apache-2.0 on original Public Core does not relicense third-party artifacts.

## When a new batch arrives

Return a compact table of unique repos (name, basic purpose, user list, proposed role, evidence status), new discoveries, duplicates and UNKNOWN fields, plus priority research suggestions with grounded value. Keep raw snapshots privately; do not create one Issue per star or bulk-add personal list members to `capabilities/registry.json`.

**Current status:** research/intake protocol only; no inventory ingestion pipeline, automatic data sharing, installed tools or approved registry lifecycle extension.
