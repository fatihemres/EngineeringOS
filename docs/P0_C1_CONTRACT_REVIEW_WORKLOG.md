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

## 11. Dated checkpoint — 2026-11-12 / C1-R9: Normative vs Candidate Decision Matrix

> **ASSISTANT_PROPOSED / SOURCE_REVIEWED (pinned public sources) / NOT_RUN / REVIEW_PENDING**
>
> **Read-only baseline verified before this proposed update:** `main` `2f31e248bf82f64870bb9591aafdfc53261add19`; prior Draft PR #16 HEAD `428310150df057b833f00766f7b4654d787f8a45`; pre-update worklog blob `d06fd1e5a913fa71694e7a4d2b39b20f6590c6c5`.
>
> **Source set:** P0 handoff blob `3d8548643956636a5283c0e6bd126b9b0e22b6e3`; P0 wire proposal blob `9b0e861fd5655f25d5adbd3e7706e78a6731c481`; public journal blob `101cdb9442089bf3307ee9afcbae119d5732c249`; `AGENTS.md` blob `c7951764e6d209d81dad3fc5baf8c2d0b5b2a992`; `docs/PRIVACY.md` blob `99741f0889afaec1039da4b4fe96c61fbfa40e99`.
>
> **Meaning of "normative" here:** a requirement or candidate invariant **described in published P0 proposals or accepted K1–K6 architectural directions**, **not** an already adopted machine-wire standard. The separately governed internal G2 candidate is **not** reproduced, quoted, or declared byte-verified by this public checkpoint.

### 11.1 Decision sheet — six narrow R8 candidates against published P0

| R9 decision | Public source requirement / published candidate | Minimal C1 choice (not approved) | Acceptable alternative | False interpretation to reject | Current gate |
| --- | --- | --- | --- | --- | --- |
| **R9-D01** — Dispatch/invocation/outcome observations | P0 wire §6 distinguishes actual attempt, pre-start block, unknown outcome and unattributed completion; K2 direction distinguishes invocation uncertainty | Separate **dispatch**, **invocation** and **target-outcome/attribution** observations in a companion execution record; preserve local-versus-target observation point | Another lossless, versioned observation model proving the same distinctions | Lost ACK = proven no dispatch; remote target effect inferred from local exit status | Exact encoding **OPEN**; E attribution **NOT_VERIFIED** |
| **R9-D02** — Unknown `attempted` | P0 canonical invariant 1 requires `NOT_RUN → attempted=false`; wire §6 explicitly leaves unknown-invocation tri-state open | New-version `execution.attempted: boolean \| null`; `null` means start genuinely unknown and needs limitations/provenance | Explicit enum or separate authenticated start-observation record preserving unknown | Guessing `false` from timeout; assigning `true` to a merely planned synthetic run | Canonical version/nullability **OPEN** |
| **R9-D03** — Reviewer independence | P0 invariant 3 requires real distinct actor/context receipts for `independent_context=true`; invariant 4 currently requires executed reviewers to classify self-review | Conditional nullable `self_review` for unverified executed review plus independently assessed reviewer/producer/context scope | Existing Boolean retained **only if** an independently verifiable unknown state can be represented without a false claim | Different model name, new persona or self-authored receipt proves independence; unknown = proven self-review | **Invariant 4 conflict OPEN**; independent E proof missing |
| **R9-D04** — Blind-round preservation | Public `AGENTS.md` requires same pinned source, separate actual sessions, no same-round peer findings until every first report is complete | Versioned review-round input manifest plus separately attributable immutable initial report/seal evidence; later reconciliation additive | Equivalent independently verifiable immutable report and exposure chronology without extra HANDOFF top-level field | Later report edits original independent verdict; timestamp alone proves no earlier contamination | Exact phase/receipt semantics **OPEN**; E isolation **NOT_VERIFIED** |
| **R9-D05** — Trusted gate evaluation | P0 invariant 7 and wire §8: `verification.state` applies to one scope; missing/failed required scopes prevent blanket acceptance; required scopes cannot be Actor-selected (K3 direction) | External, authenticated required-scope manifest and evaluator result pinned to subject, manifest, evidence frontier and applicable gate | Additional scope-item oracle field or distinct evaluated result, if required-scope authority and complete coverage remain external | `SUCCEEDED` probe = requirement PASS; self-reported scopes define all mandatory checks; mock evidence supplies real E | Manifest/result interface **OPEN**; exact oracle dispute preserved |
| **R9-D06** — Companion evidence joins | Public K6 direction separates S/M/E and receipt responsibilities; P0 receipt refs do not prove themselves | Claim-specific relational checks across subject/source, actor, action/attempt, recipient, scope, time, environmental assumptions and applicable restrictions | Any independently verifiable equivalent join semantics without compulsory identical fields on unrelated receipt types | Two individually authentic but incompatible receipts yield a single genuine authorization/gate PASS | Join serialization **OPEN**; genuine E **NOT_VERIFIED** |

**No recommendation in this table is a new `PO_DECISION`.** D01–D09 from section 5 and original K1–K6 direction decisions retain their prior identities; R9-D01–D06 identify a narrower review checklist, not new adopted requirements.

### 11.2 Conditional field/null rules — candidate, not released schema

| Case | Candidate structural/semantic disposition | Evidence boundary |
| --- | --- | --- |
| `execution.state=NOT_RUN` | `attempted=false`, `run_receipt_ref=null`, `outputs=[]`, `verification.state=NOT_VERIFIED` | Planning only; no fabricated run |
| Pre-invocation `execution.state=BLOCKED` | `attempted=false`, no produced outputs; authentic denial and its scope separately evidenced | A blocked task is not an attempted task; `handoff_state=BLOCKED` is a different axis |
| Actual observed start with unresolved target result | `attempted=true`, outcome can remain `OUTCOME_UNKNOWN` | Preserve start evidence without inventing target completion |
| Start itself unresolved | `attempted=null` only under a **new, explicitly versioned candidate**; capture uncertainty provenance | Do not silently normalize an old Boolean record |
| `execution.state=CANCELLED` | Pre/post-start facts must be preserved; proposed nullable edge is **not yet selected** | Cancellation request does not prove target termination |
| Executed evaluative review, self-review status unverified | Do not claim `self_review=false` or `independent_context=true`; proposed nullable representation conflicts with canonical invariant 4 | Report can be preserved without mandatory independent credit |
| `handoff_state=ACCEPTED` | Identified recipient and non-null acceptance ref required | Authentic receiving-party E still needed; never execution grant |
| `verification.scopes[]` | Scoped observations and evidence, with independently sourced complete required scope set | Genuine oracle/gate evaluation required; synthetic fixtures do not establish real E |

The canonical HANDOFF **22 required / four optional top-level field** boundary remains unchanged. Candidate `actor.independence_assessment_ref` and scope-level `oracle_result` are **nested** candidates, not approved new required top-level fields. Do not write this into Foundation's limited shipped v0.1 subset or accept proposal-version aliases automatically.

### 11.3 Companion-to-claim obligations and blockers

| Claim | Minimum accountable companion or authority | When credit must be withheld |
| --- | --- | --- |
| Real invocation/outcome | Attributable `ACTOR_EXECUTION_RECEIPT` or equivalent real observation | Missing start/outcome attribution; unknown result guessed as success |
| Mandatory independent review | `INDEPENDENCE_ASSESSMENT` plus real Actor/session/source evidence | Producer/self-review or unverified separation; unseen shared inputs treated as proven isolated |
| Byte artifact integrity | `ARTIFACT_DESCRIPTOR` and actual consumed/produced byte/digest continuity | Hash exists but refers to a different object or only a label |
| Effective protected action | Genuine `PERMISSION_RECEIPT`, current revocation state and external trusted PEP | Self-issued grant, wrong scope, stale revocation or no real enforcement |
| Authorization cutoff | `PERMISSION_REVOCATION` / authoritative policy state; real target cutoff if applicable | Grant record present but current effectiveness unknown |
| Requirement evidence and gate | `VERIFICATION_RECEIPT`, independently authoritative scope manifest and qualified evaluation | Missing mandatory scope, evidence, accepted exception or accountable dissent resolution |
| Handoff acceptance | Genuine counterparty acceptance receipt | Non-null, untrusted string asserted as real acceptance |
| Combined evidence | Independent compatible binding of each constituent proposition | Different subject, recipient, operation, effective interval or relevant environment, despite individually valid receipts |

The six companion families remain **conceptual responsibility boundaries**. The exact number of persisted files, transport frames, cryptographic primitives, validator technology and real authority providers are **not selected**.

### 11.4 Reviewer challenges and expected controls — designed, NOT_RUN

| ID | Negative control (must not earn promoted claim) | Legitimate positive control |
| --- | --- | --- |
| R9-V01 | ACK timeout converted to `NOT_DISPATCHED` with no evidence | Authenticated no-dispatch or safely reconciled observation |
| R9-V02 | `NOT_RUN` populated with outputs and fabricated receipt | Proper empty unexecuted design record |
| R9-V03 | Same underlying producer reported as independent reviewer by different model/persona | Real separate non-producer context with independently attributable assessment |
| R9-V04 | Unverified executed reviewer silently forced to `self_review=false` | Unknown preserved without independent credit until evidence arrives |
| R9-V05 | Original blind report overwritten after reviewer cross-exposure | Immutable initial reports followed by additive, scoped reconciliation |
| R9-V06 | Successful defect-detection probe asserted as product requirement PASS | `SUCCEEDED` probe + verified requirement `FAIL` without aggregate PASS |
| R9-V07 | Actor omits required verification scope; evaluator returns PASS | Authorized manifest detects missing required scope |
| R9-V08 | Synthetic/mock external receipt promoted to live PEP authorization proof | Actual independently controlled enforcement proof for its exact claim |
| R9-V09 | Authentic receipt for a different revision/recipient used as matching authority | Truly compatible receipt set for the intended subject/action/recipient |
| R9-V10 | Unknown-outcome side effect retried on caller-created new operation ID | Independently authorized and target-enforced bounded retry |
| R9-V11 | `ACCEPTED` handoff treated as permission to run after scope denial | Genuine acceptance preserved while execution separately denied |
| R9-V12 | Non-byte artifact with justified null digest rejected as fabricated hash | Non-byte ref remains representable, without byte-integrity credit |

**Statuses:** All `R9-V01–R9-V12` are newly authored **NOT_RUN** design cases; they **do not** alter, renumber or execute the original `W01–W36`, `P0-TEST-T01–T22` and ten Gate A negatives (**68 NOT_RUN**). Historical Codex `BLOCKED` for exact wire remains open.

### 11.5 Decision-versus-implementation split, and what would block a future review

- **Representation decisions still required:** versioned nullability and unknown-state encoding; conditional receipt fields; reviewer assessment reference/scope; immutable first-round report relationship; trusted manifest/evaluation result; receipt relational-join representation; conversion/loss semantics.
- **Actual E-level evidence still required:** authentic owner/recipient identity and rights, actor/session provenance, read/model-egress enforcement, target-side replay/revocation safety, secure resolver/consumed-byte continuity, authentic required-scope authority, real receipt join and applicable publication obligations. A schema cannot prove these.
- **Future exact-wire reviewer should remain BLOCKED for adoption** if a supported version allows unrepresentable start uncertainty, silently changes canonical executed-review semantics, promotes a claimed receipt to E without authentic source checks, treats missing required scopes as PASS, permits unsafe replay, loses critical restrictions or does not define testable migration/compatibility semantics. This is a **proposed acceptance screen**, not a replacement for the historical independent reviewer verdict.
- **Blind review discipline:** The producer's C1 analysis and this R9 disposition must not be supplied as initial peer/producer rebuttal material in a future independently blind first pass. Separate review instructions, source pins, disclosure and per-recipient PO permission must be established then.

### 11.6 Publication and source-fidelity limitation

This public PR checkpoint cites only **already-public EngineeringOS contracts, journal and operating rules** and adds newly authored bounded editorial candidates. It contains no raw transcript, internal candidate excerpt, private file/recipient metadata, private agent report or secret. The fuller separately controlled private architecture candidate and any private finding-register version are **not** uploaded, independently byte-verified or admitted for public publication by this checkpoint. Comparison against all private-source-specific constraints is therefore **NOT_VERIFIED** here.

**Result:** C1-R9 is **ASSISTANT_PROPOSED / REVIEW_PENDING**. No new P0 decision, exact-wire freeze, reviewer resolution, Gate B.1, new CI test coverage, private-data sync, release or merge occurs by appending this section. Prior sections 1–10 remain historical and unchanged.

## 12. Dated checkpoint — 2026-11-12 / C1-R10: Decision-Ready Exact-Wire Alternatives

> **ASSISTANT_PROPOSED / PUBLIC SOURCE_REVIEWED / DESIGN-ONLY / NOT_RUN**  
> **Pinned public main:** `2f31e248bf82f64870bb9591aafdfc53261add19`.  
> **Prior PR #16 source head:** `15321a22e13be6627c312b0048b5408b5be9121c`.  
> **Source claims:** canonical P0 handoff contract blob `3d8548643956636a5283c0e6bd126b9b0e22b6e3`; P0 wire proposal blob `9b0e861fd5655f25d5adbd3e7706e78a6731c481`; public journal blob `101cdb9442089bf3307ee9afcbae119d5732c249`; public `AGENTS.md` blob `c7951764e6d209d81dad3fc5baf8c2d0b5b2a992`.  
> **Disclosure:** Public-source-derived candidate specifications only. No private G2 text, internal registers, hidden source mapping, agent session material, raw transcript, or private rights evidence is included. This checkpoint **does not independently verify private-source fidelity**.
>
> This checkpoint **extends, never rewrites**, C1-R9 in section 11. The alternatives are **not** adopted schema definitions, validated JSON examples, actual receipt formats, PO decisions, or implementation authorization.

### 12.1 Six bounded decisions; one preferred candidate each

| ID and R9 mapping | Candidate A — preferred for later PO consideration | Candidate B — acceptable if the same invariant is proven | Reason / non-negotiable blocker |
| --- | --- | --- | --- |
| **R10-D01** (R9-D01) Dispatch/invocation/outcome | **A:** distinct versioned observation axes in the `ACTOR_EXECUTION_RECEIPT` responsibility: local dispatch, remote invocation, target outcome, attribution and observation point | **B:** one structured event/history model that is demonstrably lossless for all four facts, including uncertain transport | A single `execution.state`, ACK or local runner exit cannot establish actual remote start/commit. Unknown must survive crashes and reconciliation. |
| **R10-D02** (R9-D02) `attempted` unknown | **A:** newly versioned `boolean \| null` for `execution.attempted`, plus separate attributable uncertainty evidence | **B:** a new explicit attempted-status enum with authenticated mapping back to HANDOFF | Legacy Boolean meaning must not change silently. `NOT_RUN=false` remains strict. Unknown invocation is not `false`; `CANCELLED` pre-/post-start status still needs rules. |
| **R10-D03** (R9-D03) Executed self-review classification | **A:** newly versioned conditional `actor.self_review: boolean \| null` + independently resolved assessment for credit scope | **B:** preserve a Boolean only with a separate explicit, unforgeable unknown classification and no forced false/true value | Canonical P0 invariant 4 **currently requires true/false for executed evaluative reviews**. This conflict is **BLOCKED pending explicit versioned PO resolution**; independence unknown is neither proven self-review nor independent credit. |
| **R10-D04** (R9-D04) Independent review round preservation | **A:** immutable, attributable report and input-manifest refs for each blind initial reviewer pass, with separate subsequent additive reports and chronology evidence | **B:** a different sealed artifact/event ledger that proves identical input exposure ordering and immutable first reports | A new model name, reported session, or report timestamp cannot certify actual isolation. Later reports cannot overwrite first-pass findings. |
| **R10-D05** (R9-D05) Requirement oracle and gate result | **A:** scope-level oracle in candidate `verification.scopes[]` plus **external** authorized required-scope manifest and separate trusted aggregate evaluator result | **B:** an explicit top-level oracle field only if it cannot masquerade as global product PASS, while all required-scope authority and aggregation remain externally enforced | Historical disagreement over mandatory top-level `oracle_result` remains intact. Probe `SUCCEEDED` is not requirement PASS; missing mandatory scopes and unqualified objections cannot yield aggregate PASS. |
| **R10-D06** (R9-D06) Companion receipt composition | **A:** claim-specific relational compatibility checked by a trusted verifier over each receipt's applicable subject, source, operation/attempt, recipient, scope, time, restriction and environment facts | **B:** a normalized evidence-join manifest with the same enforceable relation checks, not a naive all-fields-equal rule | Each receipt being authentic is insufficient. Different supported propositions, mutable refs, inconsistent environment or mismatched recipients must not be silently composed into verified credit. |

**PO decision state:** `NOT_REQUESTED / ASSISTANT_PROPOSED` for all R10-D01–D06. No preferred A option is self-executing permission or a vote against the documented reviewer dissent. Alternatives are technically admissible only after detailed S/M/E proof and scope review.

### 12.2 Minimum conditional information profile (logical interface, not release JSON)

| Responsibility | Minimum logical binding for any claim requesting promoted credit | Conditional/no-credit rule |
| --- | --- | --- |
| Execution / dispatch | Immutable record version+ID; project/task/source; Actor/session; logical operation and unique attempt where applicable; dispatch boundary; witnessed invocation/outcome/attribution; observation-time and limitations | A completed task with missing externally attributable completion evidence is **not verified**; absence of a run receipt is not fabricated into one. Pre-dispatch denial is a non-attempt. |
| Reviewer independence | Reviewed exact artifact/clause scope; producer and reviewer actual Actor/session; known common inputs; material contribution/disclosure; input exposure chronology; immutable first-report identity; assessor authority | Executed unknown separation does **not** count toward mandatory independent credit. Source/report content can be retained as an attributed claim. |
| Gate evaluation | Exact subject+revision; authorized/versioned mandatory-scope manifest; prospective evaluation criteria; applicable scopes/qualified exceptions; admission/evidence frontier; all relevant accounted-for gate-credit attempts; scope results, limitations and evaluator identity | Missing, failed or unverifiable mandatory evidence, unresolved in-scope dissent or unqualified waiver prevents unconditional aggregate PASS. |
| Receipt composition | Exact target proposition, each receipt's authentic issuer/source/subject, supported claim, observation point, relevant environment, validity/cutoff, current restrictions and genuine recipient/action bindings | Do not require unrelated fields to match blindly, but reject incompatible assumptions or unsupported broad conclusions. |
| Owner/grant checks | Authentic owner/grantee, approved action and protected read/egress resource scope, validity, revocation freshness, logical effect and target-side precondition where necessary | A claimed receipt ref or `allowed_side_effects=[]` never authorizes a protected read or remote model transfer by itself. |
| Artifact integrity | Trusted project-scoped resolution of real consumed/produced bytes, immutable identity, actual hash of the correct byte stream, non-byte limitations | A source Git blob SHA, `fixture:` ref or 64-hex placeholder does not prove that a downstream consumer saw the same raw bytes. |

These bindings may be represented by the existing **six conceptual companions**, external trusted control planes, or equivalent independently proven evidence. **Do not introduce a new mandatory HANDOFF top-level field or an eighth record family by implication.** The exact nested field names, enum vocabularies, receipt envelopes, issuer authentication and persistence shape remain open.

### 12.3 Invariant compatibility and adoption blockers

| Existing public rule | R10 impact | Disposition / adoption precondition |
| --- | --- | --- |
| Invariant 1: `NOT_RUN=false`, receipt null, no output | **Preserved** | Planned records stay correctly representable. An unknown *real* invocation uses an explicit new version candidate, not `NOT_RUN`. |
| Invariant 3: `independent_context=true` demands real receipt/comparison, `self_review=false` | **Preserved, not weakened** | Verified independent credit requires distinct non-producer, separately evidenced context. No self-attestation. |
| Invariant 4: executed evaluations require `self_review=true/false` | **Conflict** with R10-D03 A | PO must approve exact new-version replacement rule and migration behavior; do **not** silently reinterpret old compliant records. |
| Invariant 5: active scoped permission before invocation | **Preserved, evidence expanded** | Unknown/unauthorized observed start is quarantined truth, not retroactive permission. Read and egress require actual independent enforcement. |
| Invariant 7: scoped verification; no missing-required-scope PASS | **Preserved** | Trusted manifest, attempt frontier and gate decision scope separate from Actor self-report. |
| Invariant 8: no silent promotion of unknown/conflicting state | **Preserved** | Unknown outcome and receipt conflict cannot become success through version migration or aggregation. |
| Snapshot/receipt rules: immutable handoff and distinct responsibility families | **Preserved** | Later observations are separate attributable records; a `retry_of` or `supersedes_ref` assertion is not automatic replay/supersession authority. |

**Specific blockers for later independent review:** Ambiguous version/null mapping; executed-review unknown forced into a false statement; no truthful pre-dispatch crash case; fake acceptance/grant from bare refs; scope completeness determined by Actor; unaccounted official probe attempts; incompatible receipt joins; unbounded replay/cutoff claims; fabricated digest/consumed bytes; downgraded legacy security restrictions. The historical Codex exact-wire `BLOCKED` remains **OPEN** independent of this newly proposed list.

### 12.4 Minimal decision order and acceptance checks

| Order | Decision dependency | Why this order matters | Proposed evidence before PO adoption |
| --- | --- | --- | --- |
| 1 | **R10-D01 + D02** (invocation and tri-state) | Every later attempt, replay and receipt rule needs a truthful observation basis | Distinct `NOT_RUN`, pre-start blocked, started/unknown, uncertain dispatch, cancelled-before/after-start; positive and negative design examples |
| 2 | **R10-D03 + D04** (independent review/phase proof) | Source authorship and sealed review rounds constrain who may supply gate credit | Same producer, unknown separation, genuine non-author reviewer, contamination and later-report mutation negatives |
| 3 | **R10-D05** (oracle/manifest) | Required-scope completeness and genuine gate decision cannot derive from task success | Completed defect probe `FAIL`, missing scope, partial CI, qualified exception and retest-history controls |
| 4 | **R10-D06** (composition) | Gate credit and protected actions depend on compatible evidence from distinct authorities | Genuine but incompatible recipient/source/environment/validity examples; properly compatible positive |

The order is a **suggestion for separate PO consideration**, not an automatic dependency granting authority. Acceptance here means design-level reviewability; real E boundary and Gate B.1 runtime approval remain separate.

### 12.5 Focused adversarial set (new C1 design-only references, NOT_RUN)

| ID | Test thought experiment | Expected result |
| --- | --- | --- |
| R10-T01 | Task only planned; no attempt or output | Accept valid planning snapshot (S/M) |
| R10-T02 | Dispatch attempted, ACK lost; caller sets `NOT_DISPATCHED` | Reject no-dispatch claim without authoritative proof |
| R10-T03 | Invocation started, remote result unknown; no attributed completion receipt | Preserve started/unknown; withhold promoted completion |
| R10-T04 | Executed reviewer, no genuine separation; `self_review=false` inferred | Withhold independent credit; expose invariant-4 version conflict |
| R10-T05 | Real non-author reviewer in proved distinct context and valid blind pass | Eligible only within assessed clause/gate scope |
| R10-T06 | Later review phase mutates initial signed-off findings | Reject mutation; preserve original and additive later report |
| R10-T07 | Completed defect-detection probe: execution success, required oracle FAIL | Accept observed failure; deny product/gate PASS |
| R10-T08 | Actor omits mandatory scope or selectively submits last PASS only | Deny unqualified aggregate PASS |
| R10-T09 | Genuine receipts independently authentic but mismatched subject/destination/environment | Reject their combined gate/authority proof |
| R10-T10 | Genuine scoped acceptance followed by revoked execution permission | Preserve true acceptance; deny execution |
| R10-T11 | Unresolved mutating attempt retried solely with new ID/grant | Deny until authentic current authority **and** real combined-effect target safety established |
| R10-T12 | Authentic compatible receipts with matching supported proposition | Allow **only** the specifically evidenced claim, not blanket E certification |

**Test status:** R10-T01–T12 are `ASSISTANT_PROPOSED / NOT_RUN` scenarios, not executed tests, registered runtime assertions, or new canonical W IDs. The original **68 NOT_RUN** remain 68 NOT_RUN.

### 12.6 Decision briefing and next checkpoint

At this checkpoint the PO has **not selected A or B for any R10-D decision**. The preferred alternatives merely identify the next narrow review questions. Adopting a representation later would require separately approved version/enum/null tables, explicit invariant-4/5 reconciliation, authorized source/egress and actual negative/positive evidence. No claim of actual trusted PEP, target commitment enforcement, qualified reviewer attestation, receipt authenticity, migration safety or full JSON Schema coverage is made.

**Proposed next:** C1-R11 **Minimal V1 Wire Delta and Migration Preconditions**: show precisely which changed nested fields or companion shapes are truly necessary after the PO's exact selection, and which enforcement obligations must remain outside JSON. Do not draft or ship validators, migrations, tools or code without new task-specific PO authorization.

**Publication and gate limits:** This is a new public-safe append-only documentation checkpoint for the same Draft PR only. The earlier sections remain unchanged. No private-origin source bytes or raw historical reports are published. No Ready transition, merge, project sync, release, test/agent execution or milestone closure is authorized by this checkpoint.
