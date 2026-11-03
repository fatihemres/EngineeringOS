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
