# EngineeringOS — P0-D8 Synthetic Pilot Specification (Gate A PROPOSAL)

> **Prepared:** 2026-11-03 · **Status:** Five-scenario DESIGN DIRECTION PO_APPROVED; detailed briefs, thresholds, rubrics and execution arrangements PROPOSED / NOT EXECUTED / NOT IMPLEMENTED.
> **Pinned review baseline:** protected `main` `b6819a80a9a041b301bc4164ec73f848f0efca9a` (tree `4a8defe682d5c51409c7e854d527d292a61cb96a`).
> **Starting evidence:** [PR #8](https://github.com/fatihemres/EngineeringOS/pull/8) squash-MERGED and [main-push CI #41649917173](https://github.com/fatihemres/EngineeringOS/actions/runs/41649917173) Windows/Ubuntu SUCCESS at that exact SHA. This CI did not validate this proposed pilot.
> **Authority:** [`EGO-P0-ARCH-DIRECTION-001`](DECISIONS.md) approves P0-D1–D7 as bounded architecture directions. The PO additionally accepted the **five-scenario P0-D8 design direction** (U1–U4, D1, four staged gates); no final rubric thresholds, fixture implementation, tool adoption, pilot execution, runtime, release, or roadmap milestone is authorized.

## 1. Purpose, scope and hard boundaries

Evaluate whether the **proposed** evidence-carrying capability/role/actor handoff contract represents five distinct engineering challenges faithfully, including negative evidence, disagreement, privacy, permissions and honest verification. Only a later, separately authorized experiment may assess whether independent agents improve quality over a matched single-agent baseline.

- **Gate A deliverable:** reviewable design specification, not software, fixture files or proof of a running capability network.
- **No side effects:** no installation, live agent orchestration, API/network experiments, actual GitHub PR/Issue mutations, private project ingestion, cloud indexing, telemetry or secret access. Publication of this synthetic proposal is itself a distinct, docs-only PR permission, not permission for any listed activity.
- **Source hierarchy:** [P0 handoff proposal](P0_HANDOFF_CONTRACT_PROPOSAL.md) (proposal-level contract), [approved direction register](DECISIONS.md), [UI/UX workflow](../workflows/ui-ux-craft.md), [API/DB workflow](../workflows/api-database-feature.md), [Privacy](PRIVACY.md), [Memory](MEMORY.md), and [Implementation Roadmap](IMPLEMENTATION_ROADMAP.md). The v0.1 `experience` and `registry` schemas/CLI stay unchanged.
- Every artifact, project, task, user and datum described below is **fictional**. No real screenshot, customer data, existing consumer project, installed skill or external product integration is implied.

## 2. Synthetic project families and baseline fixtures (design only)

| Family | Fictional system | Boundary | Planned fixture/oracle, not yet created |
| --- | --- | --- | --- |
| `SYNTHETIC-ALPHA` | A collaborative work-management product | U1–U4 share only an invented product brief/design tokens, not private project sources | Fictional feature list, 120-task synthetic dashboard data specification, four-stage bilingual onboarding, and accessible interaction descriptions |
| `SYNTHETIC-BETA` | An independent capacity-limited reservation API | D1 deliberately tests nonvisual domain/security invariants | Fictional users/roles, capacity-1 reservation invariant, concurrency cases and migration/rollback expectations |

Each eventual fixture requires a pinned version and reproducible digest. Neither a source SHA nor a benchmark answer is invented in this design document. Proposed `fixture:` labels are conceptual, **not validated real files**.

## 3. Scenario briefs, required handoff chains and domain evaluation

### U1 — Creative UI / Visual Direction

**Synthetic brief:** Design an original landing page for `SYNTHETIC-ALPHA` with a hero, a primary CTA, three fictional collaboration features, a simple sign-up entry point, mobile/desktop layouts, and a stated fictional brand voice. Request at least **two substantively different** art/interaction directions (layout, hierarchy and user journey, not merely palette substitutions).

**Planned role handoff:** brief owner → visual-direction proposer(s) → accessibility/interaction critic → PO design-choice gate → optional later prototype/QA. All roles are planned roles; no independent executed actor or real PO aesthetic acceptance is claimed.

**Expected planned artifacts:** alternative direction descriptions and rationale; interaction map; UI risk list; proposed responsive/accessibility checklist; dissent and next-gate summary. No actual `outputs[]` exist.

**Evaluation oracle:** an independently defined rubric distinguishes meaningful concept differences; proposed CTA remains discoverable at narrow widths; readability and accessible motion are checked only if the design is later actually implemented. Aesthetic preference is recorded separately from objective defects.

**Negative cases:** `U1-N1`, `U1-N2` (§5).

### U2 — Enterprise Dashboard

**Synthetic brief:** Show, filter and edit a fictional set of **120 task records** with statuses `OPEN / BLOCKED / DONE`, assigned owner, due date, and role-scoped controls. Viewer may inspect; editor may modify permitted tasks. Filters, pagination/empty state, loading/error state and persistence are part of the design.

**Planned role handoff:** domain/UX owner → table/state-machine designer → permission and accessibility challenger → QA-plan author → PO gate.

**Expected planned artifacts:** task-flow/state table, proposed fixture generation rules and golden-query oracle, role-action matrix, loading/empty/error behavior, screen-reader and keyboard QA plan.

**Evaluation oracle:** when a deterministic dataset is created under a later approval, displayed counts must match golden queries; denied edits must fail in underlying authorization, not just hide a button; filters and navigation should preserve intended state. **The exact seeded records and expected counts are not yet approved or executed.**

**Negative cases:** `U2-N1`, `U2-N2` (§5).

### U3 — Mobile-first Experience

**Synthetic brief:** Four-step fictional onboarding on a narrow touch screen with **English and Turkish** localized labels, back navigation, form validation, pause/resume and an offline/connection-loss state. Synthetic string-length stress is required; no real localization memory is used.

**Planned role handoff:** journey designer → state/i18n reviewer → responsive/touch critic → QA-plan author → PO gate.

**Expected planned artifacts:** state transition chart, input preservation strategy, locale length cases, error/restore flow, viewport and touch-target test plan.

**Evaluation oracle:** later implementation must preserve permitted input after navigation/reconnect, keep controls reachable under long Turkish text and retain consistent validation feedback. Device/native acceptance remains distinct from hosted tests.

**Negative cases:** `U3-N1`, `U3-N2` (§5).

### U4 — Accessibility & Motion Challenge

**Synthetic brief:** A fictional modal/dialog, expandable panel, asynchronous status notice and decorative animation. Define keyboard-only navigation, focus entry/return, reduced-motion preference and state announcements; deliberately propose an attractive but broken interaction for critique.

**Planned role handoff:** interaction designer → accessibility specialist critic → remediation proposer → regression/QA-plan author → PO gate.

**Expected planned artifacts:** keyboard/focus map, motion intent table, accessible announcement plan, proposed regression scenarios, disagreement receipts.

**Evaluation oracle:** future executed tests must check focus containment and restoration, operation without pointer input, preference-respecting reduced motion and post-fix regression. Visual polish cannot override an accessibility failure.

**Negative cases:** `U4-N1`, `U4-N2` (§5).

### D1 — API / Database Reliability

**Synthetic brief:** `SYNTHETIC-BETA` exposes a reservation operation with **capacity = 1** for one fictional resource. Two authorized clients can contend simultaneously. Designs must specify response/error behavior, idempotency, authorization, database transaction isolation and forward/rollback migration invariants.

**Planned role handoff:** domain owner → API architect → database architect → security/challenge reviewer → test-plan author → PO gate. Multiple role descriptions are not evidence of independent agent sessions.

**Expected planned artifacts:** API contract, capacity invariant, authorization policy table, transaction strategy alternatives, migration/rollback plan, unit/integration/concurrency/security test matrix.

**Evaluation oracle:** in a future isolated implementation, two simultaneous requests must not produce more than one successful reservation; failures should preserve the invariant; migrations and rollback must demonstrably preserve defined state. Passing unit tests alone is insufficient.

**Negative cases:** `D1-N1`, `D1-N2` (§5).

## 4. Shared handoff design, receipts and authority model

The intended design-level chain for every scenario is:

**Synthetic brief → proposal(s) → critique/challenge → scoped verification plan → evidence summary/dissent → explicit PO gate.**

A planned record follows [§§3–4 of the P0 handoff proposal](P0_HANDOFF_CONTRACT_PROPOSAL.md): distinct `Capability`, `Role`, `Actor`, `Workflow/TaskRun`, provenance, `project_context`, typed relation, `inputs[]`, `expected_outputs[]`, `outputs[]`, `authorization`, `execution`, `verification`, `handoff_state`, `counterparty`, acceptance receipt, `dissent_refs[]` and `next_gate`.

**For all design-only examples:** `execution.state=NOT_RUN`, `attempted=false`, `run_receipt_ref=null`, `outputs=[]`, `verification.state=NOT_VERIFIED`, `independent_context=false` unless a future separately verified real independent session exists. `self_review=null` if unexecuted; `SYNTHETIC_FIXTURE` denotes invented example evidence, not a test result. `expected_outputs[]` describes future planned outputs only. Handoff `ACCEPTED` (with a real recipient receipt) would **not** authorize execution.

| Transfer | Proposed relation / claim | Required receipt if ever executed | Who may decide next |
| --- | --- | --- | --- |
| Proposal → critic | `PRODUCES_FOR`, `CRITIQUES` | Source/digest, producer Actor, target artifact, reviewer context and independence/self-review disclosure | Receiving reviewer only acknowledges handoff |
| Critic → verification owner | `VALIDATES` plan; **not** verified execution | Exact scenario/fixture version and any actual test receipts; negative/partial checks preserved | Project QA owner for scoped verification claim |
| Reviewer → design decision | Separate recommendation and dissent | Attributed alternatives plus unsolved risks | PO selects/designs scope; reviewer cannot self-authorize |
| Run → private experience | `RECORDS_TO` proposal | Private immutable evidence/owner boundary | Project owner; no automatic public copy |
| Private lesson → public | `PROPOSES_UPSTREAM` proposal | Redaction, rights review, synthetic reproducer, human/PO review and PR/CI | PO/maintainer under separately scoped authorization |

## 5. Ten deliberate negative cases and expected *design-level* disposition

| ID | Injected fictional defect | Expected **future** recognition / block | Evidence needed if actually tested |
| --- | --- | --- | --- |
| `U1-N1` | Visually polished narrow-screen layout hides the primary CTA | Flag task-blocking responsive defect; do not report UX PASS | Exact viewport interaction/screenshot + reviewer receipt |
| `U1-N2` | Two art directions differ only in colors | Reject claim of genuinely distinct design alternatives | Criteria-based structural comparison with dissent preserved |
| `U2-N1` | Filtered task list displays an incorrect result count | Flag oracle mismatch; no aggregate dashboard success | Seed/hash, query and observed-vs-expected counts |
| `U2-N2` | Viewer role can submit an edit despite restricted policy | Block unauthorized mutation; require security verification | Actor/role, authorization check, denied-result receipt |
| `U3-N1` | Longer Turkish label clips or hides a primary action | Mark locale-responsive requirement failed | Locale, viewport, focus/touch test and screenshots |
| `U3-N2` | Reconnection/back navigation erases completed step input | Fail persistence/recovery requirement | Reproducer with transition history and observed state |
| `U4-N1` | Focus escapes open modal or fails to return on closing | Flag keyboard/focus failure; block accessible acceptance | Keyboard focus trace + relevant native/browser evidence |
| `U4-N2` | Decorative intense motion persists under reduced-motion setting | Flag preference violation and require retest | Preference setting, captured behavior and regression receipt |
| `D1-N1` | Concurrent clients both reserve last capacity slot | Fail capacity invariant; do not claim reliable transaction | Reproducible concurrent integration execution + DB state |
| `D1-N2` | Forward migration succeeds but rollback corrupts invariant | Fail migration/rollback acceptance even if unit tests pass | Before/after state digests and rollback integration receipt |

These are **deliberate scenario hypotheses**, not observed product bugs. Their desired dispositions must not be marked `LOCAL_TEST_VERIFIED` or `CI_VERIFIED` without an executed, source-pinned receipt. Record false positives and missed errors, not only successful blocks.

**Cross-cutting contract-negative plan:** Keep existing T02–T22 from [P0 §9](P0_HANDOFF_CONTRACT_PROPOSAL.md) as separate unexecuted tests (fake independent review, `NOT_RUN` outputs, `ON_HOLD` candidates, private-to-public egress, failed/partial CI, stale SHA, expired permission, conflicting reviewers, duplicate IDs and injection). These do **not** count as the ten domain defects above.

## 6. Proposed scorecard and experimental method (not accepted thresholds)

| Dimension | Suggested metric | Proposed Gate B/C target or interpretation |
| --- | --- | --- |
| Identity/provenance | % record fields, typed refs and SHA/receipt integrity checks valid | 100% of valid constructed records; missing or unverifiable values must remain unknown |
| Evidence honesty | Count of false `CI_VERIFIED`, `HUMAN_NATIVE_ACCEPTED` or independent-context claims | **0** false promotions |
| Owner permissions | Executed side effects lacking valid exact-scope active grant | **0** unauthorized side effects |
| Privacy/publication | Private contents copied to public without owner-reviewed sanitization | **0** leaks |
| Positive/negative validity | Correct accepts, correct rejects, false accepts and false rejects | Distinguish all four; critical negatives should be blocked, not by reject-all policy |
| U1 | Qualitative art-direction distinctness, legibility and later CTA task completion | Independent rubric/PO preference separate from objective failures |
| U2 | Golden-query correctness, task completion and authorization failures | Separate count accuracy, denied edits and accessibility |
| U3 | Completion, persistence, locale layout and reconnection | Separate browser/device/locale evidence |
| U4 | Keyboard/focus, reduced-motion, accessible status and regression | No accessible PASS while required checks fail |
| D1 | Capacity invariant, concurrency failures, authorization, rollback | No reliable-data PASS while critical invariant fails |
| Efficiency | Total wall time, retries, token/cost and reviewer intervention | Compare resources; do not invent cost or performance |
| Complementarity | Correctly discovered defects, missed defects, introduced regressions, dissent | Measure rather than presume multi-agent superiority |

**Experiment arms (future, permission-gated):**

- **A — Single agent baseline:** one context and ordinary task flow.
- **B — Structured multi-role perspectives, same context:** multiple role prompts, explicitly `independent_context=false`; never describe as independent agent collaboration.
- **C — Distinct verified Actor sessions:** only if different actual contexts plus execution receipts, versions, controlled common input disclosure and valid permissions are proven. Otherwise `NOT_RUN`, not faked.

Use matched briefs/seeded fixtures, same evaluation rubric and comparable execution budgets. Randomize/blind review order where feasible; record reviewer variability, repetition count, failures, confidence and trade-offs. **No sample size, benchmark score, pilot winner or quality gain is established.** Repeated trials and final acceptance thresholds require a later PO decision.

## 7. Gate A package and review checklist

| Design deliverable | Quantity | Review acceptance question |
| --- | --- | --- |
| Synthetic problem briefs | 5 | Do U1/U2/U3/U4/D1 represent distinct requirements without private source? |
| Planned handoff chains | 5 | Are producer, recipient, evidence, dissent and next authority gate clear? |
| Deliberate domain-negative cases | 10 | Does each have an expected failure oracle and future receipt type? |
| Cross-cutting handoff contract plan | 1 | Is planned status honest, and are T02–T22 kept separate/unexecuted? |
| Common scorecard and A/B/C comparison design | 1 | Are verified outcomes separated from preferences, cost and false positives? |
| Authority/independence and privacy boundary | 1 | Are actor, permissions, public/private and prohibited effects distinguishable? |
| Open decisions, limits and stage gates | 1 | Is nothing treated as execution/implementation/release approval? |

**Gate A design-review candidate may be deemed documented**, only after a separately authorized PR lifecycle, exact head CI and independent source review. This does **not** claim any of the future scores, validator tests or a real pilot have passed.

## 8. Future stages — individually gated

1. **Gate A — Design specification:** docs-only, synthetic and reviewable. The present Draft PR authorization covers only the two named documentation files; Ready, merge and cleanup need new permission.
2. **Gate B — Versioned contract/validator proof:** requires new PO approval for a separate handoff schema, path-isolated synthetic fixtures and semantic negative tests; do not silently modify v0.1 registry/experience or put handoff JSON under root `examples/*.json` while the existing CLI interprets these as experience records.
3. **Gate C — Controlled actual agent pilot:** separate PO approval for harnesses/versions, local writes, exact external tools, network/egress boundary, permission receipts and resource budget; verify real Actor sessions and actual output/test receipts.
4. **Gate D — Comparative evaluation:** separate PO-approved evaluation execution, repetitions, independent review and scope-specific human/native acceptance. Report uncertainty, trade-offs and negative outcomes; no automatic downstream merge/release.

All Gates default to **NOT_STARTED** unless separately authorized and genuinely performed.

## 9. Unresolved decisions, risks and disposition

- **P0-D3:** how pseudonymous Actor/context/session IDs, independence comparison and immutable receipts are serialized/verified. Role names alone never prove independence.
- **P0-D4:** exact typed artifact URI/ref grammar, digest handling and conditions warranting future first-class graph nodes.
- **P0-D5:** precise machine-wire enums and semantic invariants without mutating the shipped registry lifecycle.
- **P0-D6:** permission receipt fields, expiry, revocation, storage and verifier of authority.
- **P0-D8:** fixture generators/seeds, score thresholds, stage completion acceptance, agent/harness choices, budgets, allowed execution and public publication boundaries.
- **Known risk:** qualitative U1 evaluations can differ by reviewer; U2/D1 oracles require genuinely seeded fixtures and tests; U3/U4 require real interaction/device evidence before native claims; false-reject behavior needs explicit measurement.
- **Historical sources:** previous P0 document references to Issue #4 open or all D1–D8 undecided are dated snapshots, superseded for D1–D7 by `EGO-P0-ARCH-DIRECTION-001` and for Gate A design direction by the PO's later in-chat acceptance. Preserve history; this new proposal does not backdate or rewrite earlier records.
- **Current implementation state:** Foundation v0.1 MERGED / CI_VERIFIED / UNRELEASED. No handoff runtime, JSON Schema handoff validator, T02–T22 execution, pilot, third-party install, private ledger, automatic sync, release or ChatGPT Project Sources update has occurred in preparing this document.

**Review / next PO gate:** independent exact-diff review of this Gate A documentation candidate, then separate PO decision on Draft → Ready, merge method/integration, post-merge CI, source-branch disposition, and any later implementation scope.
