# P0 — Capability Network contract discovery checkpoint

> **Status:** `SOURCE_REVIEWED` / `READ_ONLY_ANALYSIS` / `NOT_IMPLEMENTED`  
> **Date:** 2026-11-02; repository `main` `381033b3a811b639f540b5a4119303367d6864b2`  
> No source edit, local test, schema upgrade, installation, GitHub mutation, UI pilot, project connection or PO milestone closure was performed by this analysis.

## Source observations

| Inspected source | Direct observation | Delta to target product |
| --- | --- | --- |
| `capabilities/registry.json` | 11 candidate capabilities; `auto_install: false`; no bundled external code; license flags unverified | No capability-to-capability relations, direct source refs/versions, install receipts, project-specific adoption or benchmark records |
| `schemas/registry.schema.json` | Capability IDs/type/role/url/status and boolean license metadata; statuses only `CANDIDATE`, `RESEARCHED`, `ON_HOLD` | No typed edges, lifecycle/compatibility/authority/evaluation schema; extending requires a versioned migration |
| `docs/ORCHESTRATION.md` | Human/agent identity split; independent proposals -> critique -> synthesis -> authorized execution -> evidence | Describes protocol but provides no runtime adapter, inter-agent transport or structured handoff record |
| `workflows/ui-ux-craft.md` | Visual alternatives, QA, Impeccable critique and optional Ponytail quality check documented | No proven integrated toolchain; no visual/native acceptance for EngineeringOS itself |
| `workflows/api-database-feature.md` | API/DB/security cross-review and rollback/test expectations documented | No runnable cross-skill orchestration or measured multi-role benefit |
| `schemas/experience.schema.json` + `docs/MEMORY.md` | Evidence categories, actors, tools, privacy and linked IDs; synthetic validation exists | No persistent project-private execution ledger, event graph, provenance-aware retrieval or approved upstream loop |
| `docs/BOOTSTRAP.md` + `tools/engineeringos.py` | Read-only doctor; dry-run and explicit local four-file ChatGPT kit; no direct upload | Project suitability planning, approved provisioning/readiness and cross-project deployment incomplete |
| `docs/CONTRIBUTION_PIPELINE.md` | Privacy, source/license, review/CI and maintainer workflow described | No automatic Issue/PR flow, private inbox, sanitized promotion or adopter acceptance |
| `.github/workflows/validate.yml` | Hosted Windows+Ubuntu validation exists; latest main-push SUCCESS on exact SHA | Existing CI does not establish third-party tool safety, complete JSON Schema compliance or end-to-end collaboration |

## First two scenario contracts to define (research only)

**Scenario U — ambitious UI/UX:** same brief -> two genuinely distinct direction proposals -> PO choice -> approved motion/component implementation -> independent visual critique -> browser + applicable native QA -> optional Ponytail code review -> regressions -> private evidence -> synthetic reusable pattern candidate. Failure-path example: visual quality increases but keyboard/reduced-motion behavior regresses; preserve rejection and test receipts.

**Scenario D — API/database:** shared domain constraints -> independent API/data/security proposals -> cross-review for transactions, schema evolution, auth and rollback -> PO choice -> synthetic implementation -> true unit/integration/security tests -> private evidence -> generalized lesson proposal. Failure-path example: contract passes unit tests but migration rollback violates an invariant; preserve negative evidence.

## Candidate handoff envelope (conceptual; not shipped JSON Schema)

`{task_id, project_profile_ref, base_sha, actor_identity, actual_harness, role_id, capability_refs_and_versions, input_artifact_refs, output_artifact_refs, evidence_class, claims_and_limits, dissent_refs, allowed_side_effects, next_gate_owner, privacy}`

The envelope must carry *truthful* `NOT_RUN`/`NOT_AVAILABLE` markers, preserve versioned refs, and distinguish agent claims from CI or human observations. Avoid storing secrets, raw personally identifying text, or private local paths in public records.

## P0 acceptance checklist (proposed)

- [x] Source read-only inspection of existing registry, workflow, memory, bootstrap and CI contracts.
- [x] Initial 11-candidate role/connection matrix drafted in `CAPABILITY_NETWORK.md` (proposal only).
- [x] Two contrasting scenario descriptions drafted (not executed).
- [ ] Define minimal relation and handoff schema with negative/missing permissions states.
- [ ] Assess identity/version/source pinning, independent reviewers and conflicting results.
- [ ] Develop a threat/authority matrix for project/private/public boundaries.
- [ ] PO review of the conceptual contract; authorize any repository or schema edits separately.

**Current conclusion:** Foundation is a stable starting point. The next dependency is a reviewable contract, **not** a large installer or orchestration engine. This analysis does not close E0 or begin an approved E1–E7 milestone.

## Dated tracking update · 2026-11-03

[Issue #4](https://github.com/fatihemres/EngineeringOS/issues/4) tracks P0 contract research; [Issue #5](https://github.com/fatihemres/EngineeringOS/issues/5) tracks new candidate intake. These Issues do not authorize a schema upgrade, an orchestration runtime, tool installation or milestone commencement.
