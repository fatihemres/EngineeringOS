# EngineeringOS — C1 Contract Decision & Review Worklog

> **PUBLIC-SAFE WORKING DRAFT — NOT AN ADOPTED CONTRACT**
>
> **Started:** 2026-11-12  
> **Classification:** ASSISTANT_PROPOSED / PUBLIC-SOURCE-DERIVED / PRIVATE-SOURCE-FIDELITY-PENDING  
> **Scope:** EngineeringOS P0 Gate B wire-contract design and C1 review preparation.  
> **Baseline public main:** `2f31e248bf82f64870bb9591aafdfc53261add19`  
> **Repository:** `fatihemres/EngineeringOS`  
> **Publishing boundary:** This Draft PR branch is **public immediately**. This document does **not** reproduce private source documents, raw transcripts, agent scratch files, local paths, private metadata, credentials, or third-party content. Internal-only source fidelity, rights, and exact-content admission remain separate reviews.
>
> **Authority:** The Product Owner requested a persistent GitHub Draft PR for the C1 workstream. This document records **candidates**, not PO approval of exact wire choices, Gate B.1, tests, side effects, Ready transition, merge, release, or publication of withheld private material.

## 1. Scope and source precedence

This is a **new append-only working ledger**, not a rewrite of `docs/P0_WIRE_CONTRACT_DESIGN_JOURNAL.md`. It is intentionally limited to a public-safe C1 index and proposals derived from the repository's published contracts. Do **not** substitute this text for the fuller separately governed private design/evidence record.

Public sources at the pinned baseline:

| Source | Pinned Git blob | Role |
| --- | --- | --- |
| [P0 handoff contract](P0_HANDOFF_CONTRACT_PROPOSAL.md) | `3d8548643956636a5283c0e6bd126b9b0e22b6e3` | Draft envelope and cross-field invariants |
| [P0 wire contract](P0_HANDOFF_WIRE_CONTRACT_PROPOSAL.md) | `9b0e861fd5655f25d5adbd3e7706e78a6731c481` | Draft wire semantics and W01–W36 plans |
| [P0 design journal](P0_WIRE_CONTRACT_DESIGN_JOURNAL.md) | `101cdb9442089bf3307ee9afcbae119d5732c249` | Dated directions, dissent and open risks |
| [Privacy policy](PRIVACY.md) | `99741f0889afaec1039da4b4fe96c61fbfa40e99` | Public/private segregation and promotion |
| [Agent contract](../AGENTS.md) | `c7951764e6d209d81dad3fc5baf8c2d0b5b2a992` | Scoped permissions and independent-review discipline |

**Source precedence:** Specific PO authority and protective rules > verified exact source/test/CI > published canonical contracts > dated handoffs > agent assertions > editorial proposals. Raw private candidate bytes, any private finding register and private reviewer reports are **not** contained or certified in this public file.

## 2. Preserved baseline — not changed by C1

- Foundation v0.1 is **MERGED / CI_VERIFIED / UNRELEASED**, with a limited schema subset. It is **not** a Gate B validator, trusted PEP, resolver, orchestration runner or native acceptance.
- Gate B.0 is **CLOSED — ARCHITECTURE_DIRECTION_REVIEWED** in a bounded, conditional sense. K1–K6 directions are accepted; detailed mechanisms and exact machine wire are **OPEN**.
- Historical technical findings: **28 OPEN**. Risk clusters: **C01–C13 OPEN**. Do not fabricate resolution or convert a source-review explanation into test evidence.
- Original 36 wire scenarios + 22 P0 test scenarios + 10 Gate A domain negatives = **68 NOT_RUN**. New C1 case identifiers in this ledger are design-only, also NOT_RUN.
- Historical Codex **BLOCKED** exact-wire assessment is preserved; Flash/Argon PASS_WITH_FINDINGS does not overrule it.
- Gate B.1 **NOT_STARTED / NOT_AUTHORIZED**. No implementation, real E-level authority enforcement, external reviewer invocation, or merge authorization follows from this worklog.
- Open, unrelated PRs and changes to project settings remain outside the scope of this C1 record.

## 3. HANDOFF envelope boundary

The public P0 contract proposes **22 required top-level HANDOFF fields** and **four optional**: `failure_details`, `retry_of`, `supersedes_ref`, `review_notes`. Their shapes are *draft*, not a released JSON Schema.

Existing key areas include `actor`, `authorization`, `execution`, `verification`, `inputs[]`, `expected_outputs[]`, `outputs[]`, `handoff_state`, `next_gate`, and `dissent_refs[]`. Each snapshot is immutable; future observations require new attributed records. **No new mandatory top-level HANDOFF field is proposed by C1.**

The six *companion* responsibility families are `ACTOR_EXECUTION_RECEIPT`, `INDEPENDENCE_ASSESSMENT`, `ARTIFACT_DESCRIPTOR`, `PERMISSION_RECEIPT`, `PERMISSION_REVOCATION`, `VERIFICATION_RECEIPT`. Along with `HANDOFF`, these are seven conceptual record families, **not** seven mandatory storage files or implemented APIs.

## 4. C1 chronology — editorial index, not independent proof

| Work item | Topic | Publication interpretation |
| --- | --- | --- |
| C1-R1 | Contract delta: execution uncertainty, evidence classes, expected outputs, version/migration boundaries | ASSISTANT_PROPOSED |
| C1-R2 | D01–D09 exact decision candidates and valid/unverified/denied separation | ASSISTANT_PROPOSED |
| C1-R3 | Contract closure matrix: HANDOFF assertion versus trusted external evidence and gate | ASSISTANT_PROPOSED |
| C1-R4 | Minimum companion claim-to-evidence responsibility boundaries | ASSISTANT_PROPOSED |
| C1-R5 | Adversarial walkthroughs: unknown/revoked retry, reviewer provenance, probe-versus-requirement result | ASSISTANT_PROPOSED / NOT_RUN |
| C1-R6 | Internal source-reconciliation checkpoint | **Details withheld** pending independent rights, provenance and exact-text review |
| C1-R7 | Source-to-contract traceability checkpoint | **Private-origin coverage not reproduced**; do not infer verified source fidelity |
| C1-R8 | Interface/nullability, scoped assessment and receipt-join proposals | Public P0-compatible subset summarized below; full internal draft withheld |
| C1-R9 | Normative-versus-candidate decision shortlist | ASSISTANT_PROPOSED; no actual PO exact-wire adoption |

**No raw conversation transcript is copied here.** These are deliberately bounded summaries, not claims that every earlier internal sentence is publicly preserved. A separate rights-reviewed private worklog is needed for any private-origin detail which must not be disclosed in Public Core.

## 5. Decision register — C1-D01 through D09 (all OPEN)

| ID | Draft choice | Acceptance boundary / unresolved conflict |
| --- | --- | --- |
| D01 | `execution.attempted: boolean \| null` when real invocation cannot be established | `NOT_RUN=false`; preserve unknown dispatch/invocation/outcome instead of inventing `false`; exact encoding open |
| D02 | Nullable `actor.self_review` with independent, scoped assessment | Canonical executed-review Boolean invariant requires explicit versioned reconciliation |
| D03 | New-version `expected_outputs[]` uses planned `{description:string}` objects | Legacy strings are not silently declared compatible |
| D04 | Scope-level oracle outcomes with a separately authenticated required-scope manifest | Actor's own scopes cannot define mandatory coverage |
| D05 | Authentic counterparty receipt required for genuine `ACCEPTED` credit | Acceptance never grants execution authority |
| D06 | Explicit production contract version; proposal versions are not automatic aliases | Literal, compatibility matrix and validator OPEN |
| D07 | Conditional companion evidence responsibilities, not one universal fake receipt | Exact schema, bindings and authenticity checks OPEN |
| D08 | Explicit, evidence-preserving migration; no unknown-to-PASS or detached-restriction loss | Legacy/current restriction interpretation and enforcement OPEN |
| D09 | Trusted external gate evaluation, with immutable subject/manifest/evidence bindings | Aggregate result/exception/adjudication serialization OPEN |

**Status of every row:** `ASSISTANT_PROPOSED`. The PO's K1–K6 architectural-direction decisions do not auto-approve these field encodings. Do not write them into Foundation v0.1 schemas.

## 6. Reviewable invariants — C1 public subset

1. **Structure is not authority.** A syntactically valid permission, CI or completion receipt may still fail independent authenticity or claim-scope verification.
2. **Planning is not execution.** `NOT_RUN` requires no fabricated run receipt or produced outputs; a `fixture:` planning ref cannot be asserted to be a materialized artifact.
3. **Handoff acceptance is not execution authorization.** A genuine receiving-party acceptance may coexist with a subsequent denied invocation.
4. **Execution success is not requirement PASS.** A completed defect-detection probe may have `execution.state=SUCCEEDED` and a genuine failing requirement oracle.
5. **Review output is not independence.** Different model labels, roles or reports cannot replace verified actor/session/context and material contribution provenance.
6. **No scope-by-omission.** Required scopes must come from a trusted, independently authorized manifest; missing/unverifiable mandatory evidence cannot yield aggregate PASS.
7. **Unknown side-effect outcome is not retry permission.** A retry identifier, new grant, timeout or apparent target state does not independently prove replay safety.
8. **Byte refs are not byte proof.** Check any digest against the actual consumed/produced byte boundary, distinguishing genuinely non-byte references from missing integrity evidence.
9. **Old or derived data does not shed restrictions.** Preserve original and current applicable negative restrictions, privacy and rights; a conversion receipt is not authority.
10. **Evidence composition is scoped.** Individually authentic receipts must jointly support the *same* authorized claim, subject, operation, environment and observation boundary.
11. **Forks and dissent are not silently erased.** A new immutable successor does not rewrite earlier assertions or automatically choose an authoritative winner.
12. **Privacy promotion is separate.** Public release needs exact proposed content and metadata, contributing-source/rights examination, applicable notice fulfillment, and distinct PO approval.

These are public-safe **candidate interpretations** of the public P0/journal commitments. Exact implementation and genuine E proof remain open.

## 7. Three adversarial design walkthroughs — NOT_RUN

| ID | Case | Expected negative | Required legitimate positive |
| --- | --- | --- | --- |
| WT01 | Unknown attempt/outcome + revoked permission + attempted unsafe retry | Deny overlapping protected effects while prior effect/cutoff/replay safety unresolved | Independently authorized operation with genuine target-enforced safety, preserving historical uncertainty |
| WT02 | Executed reviewer with unverified session or authorship separation | Do not grant mandatory independent-review credit by model/role label | Genuine non-author reviewer, independently evidenced context and scoped review |
| WT03 | Successfully completed defect probe, failing requirement, possibly outdated manifest | Never convert probe success or old scoped evidence to blanket product/gate PASS | Preserve attributable defect evidence; re-evaluate against authorized required manifest and complete evidence |

The table states **expected controls**, not actual test execution, security verification or release acceptance.

## 8. Evidence provenance and unresolved technical gates

| Evidence label | Valid scope in this worklog |
| --- | --- |
| `SOURCE_REVIEWED` | Public GitHub docs and exact refs listed in section 1 |
| `PO_DECISION` | Earlier bounded architectural directions only; PR/worklog persistence request is not a wire-approval decision |
| `ASSISTANT_PROPOSED` | C1 exact choices, cross-record constraints and design cases |
| `AGENT_REPORTED` | Historical reviewer verdicts, never automatically independent or externally proven |
| `CI_VERIFIED` | Foundation workflows on separately verified exact SHAs, **not** Gate B tests |
| `NOT_RUN` | All 68 original scenarios and newly designed C1 cases |
| `BLOCKED` | Exact wire freeze, unresolved authority/receipt/validator concerns |

The outstanding technical clusters **C01–C13**, original reviewer IDs and minority dissent remain in the dated public journal; this summary does not revise their status.

## 9. Working protocol for this Draft PR

- **Single workstream:** only this docs-only C1 worklog and expressly approved in-scope follow-up files. Do not edit canonical `docs/DECISIONS.md`, the append-only main journal, schema, code, GitHub settings or unrelated PRs without separately scoped permission.
- **Append-only checkpoints:** add a dated section for each approved new C1 delta. Do not erase/rewrite history or silently mark OPEN as resolved. Correct old claims with a new attributed note.
- **Source lock:** every checkpoint should state public HEAD, relevant blob/digest, private source access/fidelity limits, provenance labels and whether actual tests/reviews occurred.
- **Publication guard:** public PR visibility begins on the branch, **not** after merge. Never place private candidate text, raw agent transcripts, local paths, customer/personal data or third-party proprietary source in this file. Any private-to-public derivative requires prior exact-content human review, rights/privacy assessment and specific transfer permission.
- **Future updates:** proposed as edits to **this same Draft PR after an explicit, in-scope user request and fresh source checks**; no asynchronous or automatic writes. Preserve reviewed revisions and repeat CI/review as applicable.
- **Integration gate:** Draft → Ready, independent technical/privacy review, final exact-content PO approval, merge, post-merge verification and cleanup are **separate future decisions**. No auto-merge.

## 10. Dated checkpoint — 2026-11-12 / INIT

**ASSISTANT_PROPOSED / SOURCE_REVIEWED (public only):** Initial public-safe C1 ledger. The requested GitHub persistence scope is limited to a new documentation branch, one-file commit and Draft PR. The present document is **not** a comprehensive export of private material, not an exact source-fidelity certificate, and not an adopted wire.

**Still OPEN:** source-byte verification for withheld internal inputs; complete historical C1/private-origin content admission; exact D01–D09 decisions; valid companion schema; trusted oracle, PEP, replay/revocation/secure resolver; independent review; the historical 28 findings, 13 clusters, 68 NOT_RUN tests and Gate B.1 authorization.

**Next checkpoint candidate:** P0-compatible exact structural/semantic control table and source-to-claim tracing after the applicable content/privacy review, with earlier INIT text preserved.
