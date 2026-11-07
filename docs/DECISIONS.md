# EngineeringOS Decision Register

## Accepted Product Owner decisions and observed milestones

| ID | Date | Decision / event | Authority and scope |
| --- | --- | --- | --- |
| **EGO-001** | 2026-11-02 | **Public Core + Private Workspace**: a reusable public platform and separately controlled private raw logs, experience and project data. | **PO APPROVED**, architecture direction. |
| **EGO-002** | 2026-11-02 | Continue EngineeringOS work in the existing project conversation instead of re-teaching context in a new conversation. | **PO APPROVED**, working preference. |
| **EGO-003** | 2026-11-02 | **Apache License, Version 2.0** selected for **original EngineeringOS Public Core materials**. Preserve license notices and third-party rights; do not relicense external tools or private projects. | **PO APPROVED**, public-core licensing. |
| **EGO-004** | 2026-11-02 | Prepare initial pre-commit documentation and source corrections; request a **separate owner authorization before any commit or push**. | **PO APPROVED**, preparatory work only. |

## Observed milestone (not a separate product/merge decision)

- The public repository exists. The v0.2.1 transfer was applied locally and independently reviewed with findings. Detailed dated source evidence is preserved privately.

## R1 owner decisions (2026-11-02)

Public examples must be synthetic and reviewed for publication. Historical evidence and transfer checksums stay private. The owner selected a six-file governance seed on main followed by a Foundation draft PR. Both publication steps require separate authorization.

## Previous proposals resolved by decisions

- `EGO-P01` — the repository name/creation candidate is resolved by the PO-authorized repository creation. This does **not** authorize source publication.
- The **license choice only** within `EGO-P06` is resolved by EGO-003; contributor rights processes, branch rules, and release policy remain open.

## Proposed, NOT approved implementation choices

| ID | Proposal | Approval gate |
| --- | --- | --- |
| EGO-P02 | stdlib Python initial bootstrap with explicit `--write`; portable adapters for future harnesses | Technical review + implementation authorization |
| EGO-P03 | Git-tracked evidence ledger as source of truth; optional derived search/graph index | Data architecture review |
| EGO-P04 | Multi-agent independent proposal → critique → synthesis → verification loop | Pilot and governance review |
| EGO-P05 | Public experience promotion via redaction, review, Issue/PR/CI | Privacy/license/maintainer approval |
| EGO-P06R | Branch rules, version policy, contributor requirements, CODEOWNERS and CI/Actions | Separate repo-governance decisions |

A proposal, generated draft, GitHub repo existence or locally passing test is not authorization to publish or integrate. New decisions receive dated entries, without silently changing or backdating older evidence.


## Subsequent owner authorizations and verified milestones · 2026-11-02

- EGO-SEED-PUBLICATION-001 authorized the exact six-file seed commit and main push. The published root commit is `2b18708c30da03e59578cc4f7f4ebe8f269aec4d`.
- EGO-GOVERNANCE-STAGE-A-001 and its PVR-only continuation authorized main-governance and Private Vulnerability Reporting. Stage A completed. Required approvals are zero. The PO accepted GitHub's returned empty required-reviewer list and additional unattributed-change approval default for that zero-approval configuration.
- EGO-FOUNDATION-PR-001 authorizes the R1-NEW-01 documentation correction, regression tests, current security/status wording, an isolated feature branch, scoped Foundation commits, feature-branch push and draft PR publication. Integration, release and further settings changes remain separate gates.

The PO reports independent Antigravity R1 re-review as PASS WITH FINDINGS. This is attributed review evidence. Hosted Foundation CI and review of the updated PR remain pending at this source checkpoint.

## Foundation integration authorizations and observed completion · 2026-11-02

The entries above retain their historical scope and pending states. The following separately scoped PO decisions supersede only the specific governance/publication gates they resolved; broader proposals, contributor policy, roadmap and release choices are not thereby approved.

- **EGO-GOVERNANCE-STAGE-B-001 — PO authorization and verified configuration:** add exactly one required-status-check rule to main-governance (#26365625), preserving the original PR, deletion and non-fast-forward rules and all PR parameters. Required contexts are `validate (windows-latest)` and `validate (ubuntu-latest)`, each bound to GitHub Actions App ID 15368. Strict mode is true; `do_not_enforce_on_create` is false. Required approvals remain zero, bypass actors remain empty, and the accepted GitHub defaults (`required_reviewers: []`, `require_extra_approval_for_unattributed_changes: true`) remain unchanged.
- **EGO-FOUNDATION-PR-001-READY — PO authorization and observed completion:** PR #1 transitioned from Draft to Ready for Review without changing the source HEAD. This lifecycle transition did not authorize integration.
- **EGO-FOUNDATION-PR-001-INTEGRATION — PO method selection and explicit execution authorization:** use GitHub merge commit with exact head-SHA guard `7adf4576113d98ca73b876492f5692df120c812c`, permitting at most one synchronous merge request and read-only verification afterward.
- **Observed integration:** [PR #1](https://github.com/fatihemres/EngineeringOS/pull/1) merged at 2026-11-02 21:10:50 TRT (18:10:50 UTC). Actual main integration commit is `f1860b21fc580afc080ba1583635ee514fbd989c`, with first parent `2b18708c30da03e59578cc4f7f4ebe8f269aec4d`, second parent `7adf4576113d98ca73b876492f5692df120c812c`, and reviewed tree `c3857feb61a92c04a10e7716538c908e8a37388e`. The feature branch and governance controls were preserved.
- **Observed verification:** independent Antigravity/Gemini Argon final differential review reported PASS on the feature HEAD; this is agent evidence, not GitHub human approval. The [new main-push run 41498102378](https://github.com/fatihemres/EngineeringOS/actions/runs/41498102378) passed on the integration commit: Windows 26 PASS with no skips, Ubuntu 25 PASS with one Windows-only junction skip. JSON/schema-subset and public fixture checks passed.
- **EGO-FOUNDATION-MEMORY-SYNC-001 — PO authorization:** synchronize only README.md, PROJECT_STATUS.md, VALIDATION_REPORT.md, docs/DECISIONS.md and docs/NEXT_DECISIONS.md through a separate documentation branch and PR. Its independent review and integration require subsequent gates.

Foundation implementation/integration completion is not release approval or authorization to close a broader milestone. No release, tag, branch/worktree cleanup, expanded contributor governance or future runtime implementation is authorized by these records.

## PR #2 final integration evidence · verified 2026-11-03

- **Historical separate PO scope:** the original `EGO-FOUNDATION-MEMORY-SYNC-001` authorized a five-file documentation PR; a later specific PO merge-commit approval applied to **PR #2 only**, not all later PRs. The independent Antigravity/Argon memory-sync review was previously **AGENT_REPORTED PASS** (`EGO-FOUNDATION-MEMORY-SYNC-001-INDEPENDENT-REVIEW`), **not** a GitHub human Approve. Neither statement approves the current PR #6 merge.
- **GitHub-observed completion:** [PR #2](https://github.com/fatihemres/EngineeringOS/pull/2) merged on **2026-11-02 18:49:43 UTC** via [`381033b3a811b639f540b5a4119303367d6864b2`](https://github.com/fatihemres/EngineeringOS/commit/381033b3a811b639f540b5a4119303367d6864b2); first parent `f1860b21fc580afc080ba1583635ee514fbd989c`, second parent `42d303c17ee1901f9a297371c88f798befc9a8ba`, tree `bd998b6d610885512ddccedf993bddd1fc972168`. [PR CI #41501139925](https://github.com/fatihemres/EngineeringOS/actions/runs/41501139925) and [post-merge `main`-push CI #41504234468](https://github.com/fatihemres/EngineeringOS/actions/runs/41504234468) succeeded on Windows and Ubuntu. The historical branch `docs/foundation-checkpoint-20261102` remains preserved; no cleanup permission follows from this entry.

## Capability Network direction and scoped documentation permission · 2026-11-03

- **PO direction:** EngineeringOS should become a composable, evidence-driven network of complementary engineering skills/tools, specialist roles, shared handoffs and private-first lessons from separately governed consumer projects. New discovered GitHub repositories are research candidates, not adopted dependencies. Track this proposal in [Issue #3](https://github.com/fatihemres/EngineeringOS/issues/3), P0 contract research in [#4](https://github.com/fatihemres/EngineeringOS/issues/4) and capability intake in [#5](https://github.com/fatihemres/EngineeringOS/issues/5). E0 formal closure and E1–E7 implementation remain separate PO gates.
- **PO remote branch hygiene direction (2026-11-02):** future completed **EngineeringOS** remote PR source branches should be evaluated for deletion after verified merge and successful post-merge required CI. The [proposed closeout contract](PROJECT_CONTINUITY_PROTOCOL_PROPOSAL.md) preserves branch SHA/evidence, defers local cleanup, does not retroactively authorize historic branch deletion and requires specifically scoped deletion permission.
- **PO authorization for Issue #3 (2026-11-03):** only an isolated docs-only branch, the five proposal documents and additive links/status annotations, commit/push and **Draft PR** are authorized. Ready transition, independent review acceptance, merge, release, GitHub settings and branch cleanup are explicitly **not** authorized by this approval.

## PR #6 review findings and limited correction approval · 2026-11-03

- **AGENT_REPORTED independent review:** Antigravity/Gemini Argon High reviewed Draft [PR #6](https://github.com/fatihemres/EngineeringOS/pull/6) at `749ed6cc89c8c8da35ed7bd39cede0884982aa87`, returning `PASS WITH FINDINGS`: F-PR6-01 MEDIUM (incomplete PR #2 canonical checkpoint), F-PR6-02 LOW (missing `Actor`), F-PR6-03 LOW (private chat title in public doc), F-PR6-04 LOW (edge/registry ID/refactor QA notation). This is independent agent **review evidence**, not GitHub human approval and not a merge authorization.
- **PO_DECISION (scope-limited):** the PO explicitly authorized fixing these four findings **within the same Draft PR #6**, expanding the docs-only changed-file scope from 14 to **16 Markdown files** by adding `PROJECT_STATUS.md` and `VALIDATION_REPORT.md`; updating `docs/DECISIONS.md`, `docs/CAPABILITY_NETWORK.md`, `docs/PROJECT_CONTINUITY_PROTOCOL_PROPOSAL.md`, `docs/NEXT_DECISIONS.md` and the Draft PR description; creating one follow-up commit and pushing it on the same branch. No Ready transition, merge, remote branch deletion, local cleanup, repo settings, tags/releases, schema/runtime edits or new milestone start is approved. New PR-head CI and targeted review remain pending.

## P0 handoff architecture directions — PO decision · 2026-11-03

**Decision ID:** `EGO-P0-ARCH-DIRECTION-001` · **Authority:** explicit Product Owner approval in the EngineeringOS project conversation on 2026-11-03 · **Status:** `PO_DECISION` for seven *architecture directions only*, **not** implementation or adoption of the entire draft contract.

The PO approved the following bounded directions, derived from the [reviewed P0 handoff contract](P0_HANDOFF_CONTRACT_PROPOSAL.md) tracked by [Issue #4](https://github.com/fatihemres/EngineeringOS/issues/4). They constrain later design; they are not a shipped machine schema, executed pilot or grant to invoke third-party services.

| Decision | Approved architecture direction | Limit retained |
| --- | --- | --- |
| **P0-D1** | Establish a **separate, versioned handoff contract** rather than modifying `experience` v0.1 in place. | Concrete schema, migration/validator and version numbers remain separately gated. |
| **P0-D2** | Begin with **explicit manually coordinated artifact-reference handoffs**. | No runtime scheduler or autonomous multi-agent orchestration authorized. |
| **P0-D3** | Distinguish Role, Capability and actual Actor; require **privacy-safe pseudonymous identity and verifiable distinct session/context evidence** before claiming independent review. | Identity/receipt serialization, harness verification and failure semantics need further design. |
| **P0-D4** | Begin with **typed external references** for Artifact and ContributionProposal, not mandatory first-class graph nodes. | Typed-ref grammar and criteria for later graph/node migration remain open. |
| **P0-D5** | Keep **registry status, availability, permission, execution, handoff lifecycle and scope-specific verification** as separate axes. | Do not extend shipped v0.1 registry enums; detailed wire enums and semantic validators remain unapproved. |
| **P0-D6** | Use **owner-authorized, scope-limited, immutable permission receipts**, with validity/expiry semantics and default deny. | Receipt fields, revocation, expiry format, storage and verification implementation remain open; receiving a handoff is not permission to execute. |
| **P0-D7** | **Private-first handoffs and real experience evidence**; public promotion only after classification, redaction, source/license review, synthetic reproduction and explicit human/owner approval. | No automatic raw-data export, telemetry, ChatGPT sync or third-party rights assumption. |

**Still open:** **P0-D8** (pilot scope, scenario/test matrix, objective scorecard, resources and execution permissions); P0-D3/D4/D5/D6 design mechanics; actual schema, tests and validators; E0 formal closure, E1–E7 milestone starts, external tool adoption, release and any new GitHub mutation beyond individually scoped permissions. The PO expressed interest in broadening the future UI/UX pilot scenarios; **no pilot variant or execution has thereby been approved**.

**Evidence and completion boundary:** [PR #7](https://github.com/fatihemres/EngineeringOS/pull/7) merged only the **proposed** P0 research/documentation through squash commit [`617c0a78419ff40068b5973af2449684faaec073`](https://github.com/fatihemres/EngineeringOS/commit/617c0a78419ff40068b5973af2449684faaec073), tree `ebd40312ab7920b0c503c5282da9360516f303b1`, parent `7c3a26cf3f6b3a6e715dc9b75689bff2f109da41`. The required post-merge Windows and Ubuntu checks both passed in [main-push run #41641576872](https://github.com/fatihemres/EngineeringOS/actions/runs/41641576872). Argon High's final PR review was **AGENT_REPORTED PASS**, not a GitHub human Approve. [Issue #4](https://github.com/fatihemres/EngineeringOS/issues/4) was closed as **COMPLETED for design/research scope only**, with a [dated closeout receipt](https://github.com/fatihemres/EngineeringOS/issues/4#issuecomment-6605088527); [Issue #5](https://github.com/fatihemres/EngineeringOS/issues/5) remains OPEN. The PR #7 source branch remains **PRESERVED_WITH_REASON** after squash history; no cleanup.

**Publication scope:** This decision-register entry is a docs-only synchronization candidate. Publishing it in a Draft PR does not authorize Ready transition, merge, Issue mutation, runtime, installation, migration or release. Earlier decisions/checkpoints are preserved as originally written.

### EngineeringOS agent workflow direction — 2026-11-07 · `EGO-WORKFLOW-DIRECTION-20261107`

**PO_DECISION — WORKFLOW_DIRECTION (in conversation; publication pending):** For EngineeringOS work, the default authorized workflow *when each distinct step is separately permitted* is: PO defines scope and approvals → ChatGPT prepares tasks, English agent prompts, pinned sources, privacy/egress limits and evidence criteria → Antigravity Flash High prepares the initial code/document/design deliverable → Codex Astra and Antigravity Argon High perform separate first-round independent reviews of the same pinned deliverable → ChatGPT reconciles findings with actual evidence and preserved dissent → PO decides on corrective action → an authorized agent performs scoped corrections followed by targeted re-review.

Codex focuses on implementation soundness, schemas, regression, concurrency and tests; Argon focuses on architecture, security, adversarial semantics and positive/negative controls. Claude Opus is a separate, needs-based deep/third-opinion reviewer rather than a default participant. The producer/reviewer allocation may change **only with task-specific PO approval**, for example a critical implementation assigned directly to Codex.

**Non-authority and evidence limits:** This is a *workflow allocation decision*, not authorization for invocation, source reads protected by a separate grant, inference transfer/egress, coding, tests, branch/commit/push/PR/merge, publishing, cleanup, release or Gate B.1. Reviewer sessions must be genuinely separated and their common input pinned; different model names do not independently prove separation. First-round reviewers do not see each other's reports. Preserve `BLOCKED`, limitations and dissent; reported PASS never substitutes for PO/native/CI evidence or permission. Prompt headers must specify agent/model/reasoning, difficulty, selection rationale, quota/budget constraints, exact source, allowed/forbidden actions, disclosure boundary and deliverable/evidence requirements.

**Scope protection:** K1–K6, Gate B.0's bounded `CLOSED — ARCHITECTURE_DIRECTION_REVIEWED`, 28 first-round findings/13 open clusters, the 68 `NOT_RUN` design cases and Gate B.1 `NOT_AUTHORIZED` remain unchanged. This record does not adopt a V1 machine contract or alter Foundation v0.1.
