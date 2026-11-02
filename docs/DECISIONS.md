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
