# EngineeringOS — P0 Handoff Wire Contract Proposal v0.3

> **DESIGN CANDIDATE — NOT APPROVED AS A MACHINE CONTRACT / NOT IMPLEMENTED**  
> Prepared: 2026-11-04 (Europe/Istanbul)  
> Review baseline: protected `main` `f7f693650b205e6d3f19ac01f51169354e3fd40b`; tree `cbfd52021c208ef80214a4f2634ab356f6de5e86`  
> Origin: canonical P0 contract; design-only wire v0.1/v0.2; Gemini Flash v0.1 (`AGENT_REPORTED`, 3 MEDIUM + 2 LOW); Claude Opus High v0.2 (`AGENT_REPORTED`, 2 HIGH + 10 MEDIUM + 7 LOW).  
> **Exact-SHA Draft PR #10 provenance (dated checkpoints, not live-status promises):** Initial documentation HEAD `6d3aa54b4ecb510aee50e59390e2942f26e4262d` received a user-supplied Claude Opus High `AGENT_REPORTED PASS WITH FINDINGS` review. The subsequent docs correction HEAD `eb0fc5d5218a7d653af696caf0a430971f6df0d5` received a Google Antigravity Argon High `AGENT_REPORTED BLOCKED` review (primary prior-review packet inaccessible; independent live-source assessment found 3 MEDIUM + 5 LOW). Both commits were on **Draft PR #10**, not integrated into protected `main` at those checkpoints. Neither is an approved wire schema or executed validator; review conclusions apply only to their exact source bytes. Verify the latest branch/head, review and CI through live GitHub rather than treating this header as a current-head certificate.

## 1. Authority, purpose, and non-goals

This proposal defines evidence-honest, manually coordinated handoff **messages**, not an execution engine. It preserves distinctions among Capability, Role, actual Actor, source, artifact, scoped authorization, task execution, verification scope/oracle, handoff lifecycle, and PO decision. It does not install a harness, schedule agents, provision capabilities, create a graph store, access private content, run a pilot, modify GitHub, or authorize external actions.

PO-approved *directions* already recorded in `docs/DECISIONS.md` (`EGO-P0-ARCH-DIRECTION-001`, P0-D1–D7) and `docs/NEXT_DECISIONS.md` (P0-D8 five-scenario study) are distinct from **unapproved exact encoding**. The PO additionally accepted minimum P0-D3/D4/D5/D6 technical approaches in the EngineeringOS project conversation on 2026-11-04. That conversational approval is not yet recorded in public Git; it does **not** accept the fields, enums, cryptographic mechanisms, serialization, schema/CLI changes, Gate B, pilot, or GitHub mutation in this proposal. No retrospective decision ID is invented.

Source hierarchy and privacy boundaries remain governed by canonical repository documents and the project's current PO decisions. Historic draft checkpoints are not live status. Proposed schema and status names below are *candidates*, never additions to shipped Foundation v0.1.

## 2. Versioning, record families, and immutable snapshots

`contract_version` is a required explicit contract discriminator. The documentary value `0.3-proposal` indicates a **candidate**, not a released schema; no automatic compatibility or fallback from `0.1-proposal`/`0.2-proposal` is presumed. Future validators must reject unsupported versions, while separately designed migration/tests may support earlier proposals. Foundation v0.1 registry and experience schemas remain byte-identical.

Conceptual record families: `HANDOFF`, `ACTOR_EXECUTION_RECEIPT`, `INDEPENDENCE_ASSESSMENT`, `ARTIFACT_DESCRIPTOR`, `PERMISSION_RECEIPT`, `PERMISSION_REVOCATION`, `VERIFICATION_RECEIPT`. These are **not** seven mandatory persisted files, graph node kinds, implemented APIs or adopted registry enums.

**Snapshot rule (C-02):** One `HANDOFF` is an immutable point-in-time **assertion**, including its displayed lifecycle and execution state. A later observation/transition creates a **different `handoff_id`** and a `supersedes_ref` pointing to the prior record of the same kind; it does not edit the earlier record. A new execution attempt, when separately authorized, may use `retry_of` to reference the former attempted handoff. Do not infer from the mere presence of `retry_of` that a retry is safe; reconcile unknown outcomes first. New records must carry their own attribution, timestamps and provenance; the exact state-transition graph is still open. Duplicate IDs with conflicting bytes are invalid.

**Fork and authority boundary (proposed):** If multiple records supersede one predecessor, preserve every fork, dissent reference and attributable provenance. No branch silently becomes the canonical current state. Who may authorize supersession and how a canonical current record is reconciled are open Gate B choices; a new record never retroactively rewrites evidence or creates a new permission grant.

The four canonical optional handoff envelope fields remain available: `failure_details`, `retry_of`, `supersedes_ref`, `review_notes`. **`failure_details` and `review_notes`** may contain untrusted free text (including tool stderr or model-generated content); **`retry_of` and `supersedes_ref`** are untrusted reference assertions until independently resolved and validated. No field content is executable instruction or permission. Supersession preserves original dissent and evidence references.

## 3. Envelope shape and field ownership

A candidate `HANDOFF` requires the following **top-level** fields, matching canonical `docs/P0_HANDOFF_CONTRACT_PROPOSAL.md` §4:

| Required field | Proposed meaning / boundary |
| --- | --- |
| `contract_version`, `record_kind`, `handoff_id` | Version, record type and immutable snapshot ID. |
| `workflow_id`, `workflow_run_id`, `task_id`, `created_at` | Workflow definition, invocation context, task and UTC timestamp; a reserved synthetic run ID is never proof of a real invocation. |
| `project_context` | `profile_ref`, `source_ref`, `source_sha`, `policy_ref`, `data_classification`; `source_sha=null` only for correctly designated pre-execution or synthetic planning. |
| `relation` | One directed typed edge: `relation_id`, `type`, `from`, `to`, `provenance_ref`, `scope_ref`, `assertion_state`, `evidence_refs[]`, `input_artifact_refs[]`, `output_artifact_refs[]`, `symmetric`. |
| `actor` | Intended/real Actor identity, role/harness/context, `independent_context`, execution/upstream/disclosure references, `self_review` and candidate assessment reference. |
| `counterparty`, `acceptance_receipt_ref` | May be null for `DRAFT`; `ACCEPTED` requires an actual identified recipient and authentic acceptance receipt. |
| `capability_bindings[]` | Availability, registry/license/vetting **observations**, not granted adoption/install/execute rights. |
| `inputs[]` | Array of **input descriptor objects**, never mixed with bare strings. |
| `expected_outputs[]` | Array of **planned output descriptors** (proposal: `{ "description": string }`); not produced evidence. |
| `outputs[]` | Array of **actual output descriptor objects**, never predictions. |
| `authorization` | `owner`, `policy_ref`, `permission_state`, `allowed_side_effects[]`, `permission_receipt_ref` are caller assertions until checked externally. |
| `execution` | `state`, `attempted`, `failure_code`, `run_receipt_ref`; distinguishes actual task attempt from side effects. |
| `verification` | `state`, `scope_ref`, `scopes[]`, `evidence[]`; evidence class is separate from requirement oracle. |
| `handoff_state` | Protocol state, independent of execution. |
| `next_gate` | `owner`, `state`, `decision_ref`; a fictional decision owner is not an approval. |
| `dissent_refs[]` | Preserve contrary evidence/objections. |

Candidate **optional** fields: `failure_details`, `retry_of`, `supersedes_ref`, `review_notes`. Every semantic rule for `relation` endpoint types, permitted symmetry and input/output references remains inherited from canonical P0 §3–4. For a Role-origin relation that describes the enclosing Actor's own act, `relation.from.id` should match `actor.role_id`; do not impose this rule on unrelated relationships or producer-target edges without identifying the actual acting Role.

The precise `expected_outputs[]` shape is an explicit **v0.3 proposal**, not an assertion that old design examples used the same shape. `0.1-proposal` and `0.2-proposal` are not wire-compatibility promises.

## 4. Artifact references, conceptual fixtures, and SHA-256 (C-01/C-08/C-13/C-16)

A **conceptual** synthetic planning reference uses a clearly fictional and non-resolvable `fixture:` label (e.g. `fixture:SYNTHETIC-U1-BRIEF-PLAN`). It does not claim materialized bytes, authentic provenance, digest verification or owner authorization. Do not place a plausible 64-character placeholder hash in a conceptual fixture.

A **materialized** synthetic fixture may be used in a future authorized run, but only after actual byte creation, permitted storage, a computed digest, source/classification controls and a real resolver/receipt. Therefore **synthetic does not mean NOT_RUN forever**. The validator must distinguish a conceptual planning fixture from a pinned, materialized synthetic artifact. No change from `fixture:` to an actual artifact reference occurs by mere string substitution.

Candidate typed external identity for actual artifacts: `egos-ref:v1:<kind>:<opaque-id>` (illustrative; **grammar unapproved**). For private data, reference-to-path mappings remain only in access-controlled Private Workspace. Never interpret a reference as an arbitrary filesystem path or URL, allow implicit network resolution, permit traversal/symlink escapes, or let it cross project namespaces. Exact resolver containment and normalization grammar remain gated Gate B choices.

**Input descriptor** candidate:

| Field | Proposed type | Check |
| --- | --- | --- |
| `artifact_ref` | opaque typed string | Must resolve within authorized project/scope if used. |
| `content_sha256` | lowercase 64-hex string **or null** | Hash present when byte-addressable materialized content integrity is claimed; null for conceptual/non-byte/unavailable bytes with an explicit reason/limit. |
| `classification` | canonical classification enum | Classification is not a publication right. |
| `trust` | canonical input trust enum | Caller trust label is never its own evidence. |
| `purpose` | nonempty purpose | Untrusted descriptive content. |

**Output descriptor** candidate: `{ artifact_ref, content_sha256, classification, produced_by_run_ref }` with the same conditional digest semantics. An actually produced byte artifact must have a computed, checked digest before claiming byte-level integrity; a PR, CI run or external DB state reference is not necessarily a byte artifact and may have `content_sha256:null` with an accountable evidence receipt. A null digest does **not** mean integrity was verified. `NOT_RUN` always requires `outputs:[]`.

**Consumed/produced artifact evidence boundary (proposed):** `content_sha256:null` is an absence of byte-integrity evidence, not a passing hash check. For actual materialized byte content consumed or produced by an attempted run, an attributable source/producer receipt and a computed, verifiable digest are prerequisites to claiming verified **byte** integrity. If the bytes or digest are unavailable, the associated verification/evidence record must disclose that limitation; a consumer whose safety or correctness depends on byte integrity must fail closed. A non-byte reference can legitimately lack a byte digest, but must not claim byte-level proof. Whether a future optional `digest_limit` descriptor field or an external limitation/evidence reference expresses this is still an **unapproved Gate B wire-shape choice**.

When a digest is present, its proposed normalization is `^[0-9a-f]{64}$`; the exact byte/canonical-content hashing policy remains open. No synthetic placeholder digest is acceptable as evidence. `relation.input_artifact_refs[]` / `relation.output_artifact_refs[]` must match the envelope input/output refs; missing outputs cannot be invented in a relation.

## 5. Role, Actor, identity and review provenance (C-11/C-19)

Capability is a catalogued candidate, Role is an abstract responsibility, and Actor is the actual human principal or executed model/harness session. Use project-scoped pseudonymous identities. Keep raw transcripts, account identifiers, credentials, private paths and cross-project mapping tables outside public handoffs.

Keep canonical `actor.identity`, `role_id`, `harness_ref`, `context_ref`, `independent_context`, `execution_receipt_ref`, `upstream_actor_ref`, `independence_disclosure_ref`, `self_review`. A candidate `actor.independence_assessment_ref` (nullable) can point to a separately verified conclusion; it is **not adopted as a required field** until an exact wire decision. For a synthetic `NOT_RUN` record, `context_ref`, receipts and assessment may be null and `self_review=null`, `independent_context=false`.

A claim of `independent_context=true` requires distinct real producer/reviewer contexts, source-target pin, controlled-common-input disclosure, authentic execution/context receipts, and a verifier that **does not accept the attested Actor's self-authored identity assertions as proof**. A different model name alone is insufficient; a genuinely distinct context need not use a different model. This establishes *context separation*, not statistically independent judgement.

Executed non-review generation: `self_review=null` (not applicable). An executed, evidenced same-context review: `self_review=true`. An executed review with **verified** distinct producer/reviewer context and no self-review: `self_review=false`. For executed evaluative work with **unverified** separation, do not invent `true` or `false`; treat the independence assertion as unverified, prevent independent-review certification, and record the uncertainty in attributable review provenance/evidence. A final `null`/dedicated assessment encoding and verifier are **open PO design choices**. Canonical `MULTI-PERSPECTIVE_SINGLE_AGENT` terminology is retained for same-context role simulation.

## 6. Independent statuses and snapshot semantics (C-02/C-06/C-07)

Preserve existing **candidate** axes (do not patch shipped registry/experience enums):

| Axis | Draft values |
| --- | --- |
| Registry observation | `CANDIDATE`, `RESEARCHED`, `ON_HOLD`, `UNREGISTERED` (last is *handoff-only*, not shipped registry) |
| Availability | `UNVERIFIED`, `AVAILABLE_VERIFIED`, `NOT_AVAILABLE`, `INCOMPATIBLE` |
| License posture | `UNKNOWN`, `SOURCE_REVIEWED`, `USAGE_APPROVED`, `REDISTRIBUTION_APPROVED`, `RESTRICTED` |
| Permission | `NOT_REQUESTED`, `DENIED`, `SCOPED_GRANTED`, `EXPIRED` (`REVOKED` not silently adopted) |
| Execution | `NOT_RUN`, `RUNNING`, `SUCCEEDED`, `FAILED`, `PARTIAL`, `BLOCKED`, `CANCELLED`, `OUTCOME_UNKNOWN` |
| Handoff | `DRAFT`, `OFFERED`, `ACCEPTED`, `REJECTED`, `BLOCKED` |
| Scope verification state | `NOT_VERIFIED`, `AGENT_REPORTED`, `SOURCE_REVIEWED`, `LOCAL_TEST_VERIFIED`, `CI_VERIFIED`, `HUMAN_NATIVE_ACCEPTED` |
| `verification.evidence[].class` (separate canonical evidence enum) | `HYPOTHESIS`, `AGENT_REPORTED`, `USER_REPORTED`, `SOURCE_REVIEWED`, `LOCAL_TEST_VERIFIED`, `CI_VERIFIED`, `HUMAN_NATIVE_ACCEPTED`, `PO_DECISION`, `SYNTHETIC_FIXTURE` (`SYNTHETIC_FIXTURE` proves an illustration, not execution) |
| PO decision | `NOT_REQUESTED`, `PENDING`, `APPROVED`, `REJECTED`, `EXPIRED` |
| Relation assertion | `PROPOSED`, `OBSERVED_WITH_EVIDENCE`, `REJECTED`, `SUPERSEDED` |
| Data classification | `PUBLIC_REUSABLE`, `PROJECT_INTERNAL`, `SENSITIVE`, `SECRET` |
| Input trust | `UNTRUSTED`, `PINNED_SOURCE_VERIFIED`, `OWNER_POLICY` |

`execution.attempted` means a **real task invocation has actually begun**, including read-only analysis/tests; it does **not** mean a side effect occurred. **Every task requires independently verified permission before invocation or access to protected input, even when `allowed_side_effects:[]`; recheck again before each side effect.** A proposal, planned synthetic invocation ID, permission check, or prevented pre-start operation does not imply `attempted=true`.

**Read-only authorization boundary (proposed; canonical invariant 5 preserved):** Counting a real read-only invocation as `attempted=true` records what happened, not permission to start it. Neither `allowed_side_effects:[]` nor `permission_state=NOT_REQUESTED` constitutes a grant. This proposal authorizes no new read-only execution: the applicable project must have an authenticated, scope-specific owner grant or an independently verifiable PO-approved standing read-only policy covering the particular source, actor and data/network boundary. A record may truthfully describe a historically unauthorized attempt **only as an attributable quarantined incident/failure record**, not as an accepted handoff, permitted workflow continuation, trusted evidence promotion, or retrospective grant. Capture only safe, access-controlled incident metadata; do not copy restricted inputs into public evidence. The incident/quarantine representation, standing read-only grants and any modification to canonical P0 execution invariant 5 remain **open Gate B decisions**, not implicit permissions.

**Proposed execution state table** (semantics, **not implemented validation**):

| State | `attempted` | Receipt / outputs | Interpretation |
| --- | --- | --- | --- |
| `NOT_RUN` | false | `run_receipt_ref=null`, `outputs=[]`, `verification.state=NOT_VERIFIED` | Only planned. |
| `BLOCKED` | false | `outputs=[]`; `failure_code` describes pre-start prevention | Policy/prerequisite stopped task before invocation; an optional denial-evidence ref is separate from a run receipt. |
| `RUNNING` | true | Run receipt **if obtainable**; no fabricated outputs | Actual task started; this is a snapshot, not proof of completion. |
| `SUCCEEDED` | true | Attribution/evidence required for claimed actual output | Task/probe completed; **not** product requirement PASS. |
| `FAILED` | true | Preserve failure evidence where available | Task/harness failed, possibly before output evidence was captured. |
| `PARTIAL` | true | Only real attributable partial outputs | Some intended steps completed; limitations explicit. |
| `CANCELLED` | true/false | Record whether task started | Before or after invocation; do not fabricate side effects. |
| `OUTCOME_UNKNOWN` | true when invocation was observed; false/unknown must be explained rather than guessed | `run_receipt_ref` **may be null** when disconnected; no guessed outputs | External outcome not reliably established; reconcile before any retry. |

A future schema may need a tri-state or detailed evidence field for `attempted` if even invocation is unknowable; this is deliberately **open**, not silently resolved by a Boolean. Do not conflate command exit status with task outcome. `failure_code` is expected for blocked/failed/partial cases when a genuine classification exists; absent evidence must not be filled with a fictional code.

**Unattested outcome boundary (proposed):** `execution.state=SUCCEEDED` is an asserted task outcome, not by itself evidence of run provenance or requirement acceptance. If `run_receipt_ref` and equivalent independently attributable completion evidence are missing, that **execution claim** must not be promoted merely by assertion to `SOURCE_REVIEWED`, `LOCAL_TEST_VERIFIED`, `CI_VERIFIED`, `HUMAN_NATIVE_ACCEPTED`, `relation.assertion_state=OBSERVED_WITH_EVIDENCE`, certified independent review, or product/PO acceptance. Independently source-reviewed *documents* may still be marked `SOURCE_REVIEWED` for their own narrowly stated scope, never as a substitute for missing execution evidence. Genuine interruptions may remain `OUTCOME_UNKNOWN` and lack a receipt without inventing one. Future minimum-receipt criteria and an unknown-invocation/tri-state `attempted` representation remain Gate B choices.

**Handoff versus execution `BLOCKED`:** `handoff_state=BLOCKED` is a transfer/acceptance/protocol blocker; `execution.state=BLOCKED` is a pre-invocation execution prerequisite/policy blocker. They may differ. `ACCEPTED` requires a real identified receiving party, authentic acceptance receipt, policy-accessible/trusted inputs **at acceptance time**, and no *handoff-protocol* blocker. A later or separate execution denial does not retroactively erase a genuine handoff acceptance. `ACCEPTED` never grants permission to execute.

## 7. Owner permission, trusted verifier and revocation (C-03/C-04/C-17)

An agent-generated `authorization.owner`, `policy_ref`, `permission_state`, or claimed receipt **is not a grant**. The trusted owner identities, allowed authority scopes and grant/revocation record roots must be established through an **independently controlled, project-approved verifier policy outside the untrusted handoff under evaluation**. The exact protected channel (authenticated repository action, local owner-authorized store, or another mechanism) and evidence/authentication process are not chosen here.

Candidate owner grant information includes `receipt_id`, `issuer_ref`, `grantee_ref`, `project_ref`, `target_ref`, applicable `source_sha`, `allowed_actions[]`, `resource_scopes[]`, egress destinations/classification constraints, `issued_at`, `not_before`, `expires_at`, `decision_ref`, `issuer_attestation_ref`; task/run binding, repeat-use limits and consumption records are **proposed refinements**, not silently adopted crypto or runtime systems. No universal `max_uses=1` applies to all grants. Side-effect and repeat-use policy depends on the owner's exact scoped authorization and task risk.

**Replay and first-use default (proposed):** For a side-effecting or non-idempotent action, if neither an **independently enforceable unique task/run/state precondition or idempotency binding** nor authoritative consumption/use tracking exists, the verifier cannot distinguish first presentation from replay and **must fail closed before even the first execution**. A caller-authored task ID, an unbound receipt, unverified `source_sha`, or silence about repeat use does not establish uniqueness; simply saying “one-time” without an enforceable check is insufficient. Separately approved bounded repeat-use, demonstrably idempotent operations, or standing read-only access may follow explicitly different policies without imposing universal `max_uses=1`. Exact binding, state and ledger mechanisms remain Gate B choices.

At **task-invocation start, before read-only analysis, external access or protected input ingestion**, the trusted verifier must independently check: authentic issuer/owner authority, actual Actor/grantee, exact project/task/source/target, authorized **read/input classification and resource scope**, network/egress boundary, permitted capabilities and license/vetting state, validity/time window, revocation freshness, applicable task/run/replay policy, and target-project rules. **An empty `allowed_side_effects[]` is not a read authorization** (the empty-set subset check is otherwise vacuously true). Before **each separate side effect**, recheck the same applicable authority/freshness constraints and require `allowed_side_effects[]` to be a genuine subset of permitted actions for that specific operation. A grant or standing policy must be independently verifiable and scope-specific; absent evidence fails closed. Pre-invocation denied attempts are `BLOCKED`/not attempted; if an unauthorized invocation already occurred, quarantine its truthful incident record per §6 rather than promoting it to normal workflow evidence.

**Direct-human-owner exception and W18 boundary (proposed):** A directly authenticated **human PO principal** may act as both issuer and grantee **for that human's own direct action** only if an external trusted owner policy explicitly permits it. An AI model, agent, delegated automation, tool/harness session, or agent using the PO's ambient OS/browser/GitHub credentials is **not** the direct human principal and requires its own explicit, verified actor/grantee authorization. Neither `actor.harness_ref=null` nor host-login identity alone proves a direct human action; distinguish the initiating principal and delegation chain externally. The verifier applies the same source, target, action, expiry, revocation, read and egress limits at invocation and at each side effect.

Time invariants: applicable timestamps must parse as real UTC instants, with issuance/activation before expiry (precise skew and maximum lifetime remain open). `source_sha` must be pinned for repo side effects; SHA alone is not a protection against repeated operations within the permission window, and non-repository actions may need different immutable target IDs.

Grant and revocation events are immutable; revocation is a new attributable record referencing the grant. An effective revoked grant cannot authorize execution. Whether `REVOKED` becomes a wire enum or maps to `DENIED` plus a revocation ref remains an **open PO decision**. A receipt is never trusted merely because its fields use familiar names. Cryptographic signing/PKI and use-count ledgers are **options**, not current adopted infrastructure.

## 8. Verification: probe execution, oracle result, and evidence strength (C-10)

Keep **three axes** separate:

1. `execution.state` = status of the handoff's own actual task. For a `VALIDATES` relation, the task is the **test probe**; `SUCCEEDED` means the probe completed its defined observation, not that the product passed.
2. **Requirement oracle** = observed result against a named requirement (`PASS`, `FAIL`, `INCONCLUSIVE`, `NOT_EVALUATED` are **candidate** scope-level values). A repro that intentionally detects a defect yields requirement `FAIL`, even when the detection probe executed successfully.
3. `verification.state` = evidence classification for **only** `verification.scope_ref`, not a global outcome or aggregate product acceptance. `verification.scopes[]` preserves each required scope, oracle and evidence refs. `LOCAL_TEST_VERIFIED` + requirement `FAIL` can be valid evidence of a defect.

A nonzero process exit is not automatically task `FAILED`: test frameworks may use nonzero to indicate an **observed failing assertion**, while the instrumented probe completed and captured a credible result. Conversely, a harness crash/timeout before obtaining a trustworthy observation is `FAILED`/`OUTCOME_UNKNOWN` with oracle `INCONCLUSIVE` (not a fabricated `PASS`/`FAIL`). The exact run-exit policy belongs to a later validator/harness contract.

No aggregate acceptance claim is permitted while applicable required verification scopes are absent, failed or unverifiable. A passing CI test is scoped to the actual job/ref/platform; it does not prove native UI, migration rollback or PO acceptance.

A candidate scope descriptor should include `scope_ref`, `state`, `oracle_result`, `requirement_ref`, `evidence_refs[]` and limitations. The final exact nesting, required fields and allowed enum values are **not yet PO-approved**. For `NOT_RUN` fixtures, `scope_ref` must have an explicit `NOT_VERIFIED`/`NOT_EVALUATED` entry, not an empty required-scope set falsely interpreted as success.

## 9. Private/Public boundary, classification and trust (C-09)

Default unknown data to `PROJECT_INTERNAL`. A typed ref, byte digest, trust label or `PUBLIC_REUSABLE` classification **never constitutes publication permission**. No raw transcripts, private source, credentials, account inventories, local paths, personal/customer data, third-party copyrighted material or sensitive evidence enter public Git by default.

No output may be silently downgraded to a less restrictive/public classification merely because its reference string or label changed. A deliberate **redacted, synthetic or declassified derivative** may acquire a different classification **only after** an attributable authorized transformation/promotion decision: source/license review, redaction, rights determination, synthetic reproducer when appropriate, human/PO review, and separately authorized PR/CI. The original stays private with unchanged provenance. Data classifications are policy categories, not necessarily a simple ordered integer scale; final promotion rule needs a classification/rights-aware policy and independently checked proof.

**W10/W24 minimum rejection rule (proposed):** An unauthorised assertion that `PROJECT_INTERNAL`, `SENSITIVE` or `SECRET` became `PUBLIC_REUSABLE` solely by changing a string or label must be rejected. Other transfers and reclassifications require project-specific exposure and rights analysis, not an invented total order of enum values. A reviewed redacted/synthetic derivative receives its own identity and promotion receipt; the original retains its classification and evidence.

**Public-record versus fictional private-classification fixture (proposed):** The P1 JSON in §13 intentionally includes the literal value `PROJECT_INTERNAL` as a **fictional design vector**, not a claim that a real internal record or its bytes may enter Public Core. Publishing this reviewed synthetic *description* in Markdown does not turn an actual `PROJECT_INTERNAL` handoff record into `PUBLIC_REUSABLE`. A future `validate-handoff --public` positive control must be a **separate, reviewed synthetic record** classified `PUBLIC_REUSABLE` and passing provenance/rights/secret checks; P1 must not be treated as that public-admission positive control. `W31` requires both rejecting ineligible private-classified records and accepting a genuinely eligible public synthetic control. This mode distinction is itself proposed design; no CLI or validator exists.

`UNTRUSTED`, `PINNED_SOURCE_VERIFIED`, `OWNER_POLICY` are inputs to a review, not values a requester can assert to gain trust. Free text in external artifacts/README/agent outputs is untrusted and cannot alter permission or higher-priority policy.

## 10. Design-level validation layers and invariants

Use distinct future layers: **S** = structural shape/version/type checks; **M** = within-record or ledger semantic consistency; **E** = external evidence/authority validation. JSON parsing **cannot** authenticate grants, sessions, digests, CI, branch history or actual product outcomes. The shipped `check_shape()` supports only a subset of JSON Schema and is not a complete Draft 2020-12 validator.

| Invariant | Layer | Proposed failure condition |
| --- | --- | --- |
| Explicit supported contract version; distinct record kind; types, required fields | S | Unknown version or malformed field. |
| `NOT_RUN` empty outputs, false attempted, null run receipt, `NOT_VERIFIED` | S/M | Planned work misrepresented as execution. |
| Actual nonempty output tied to observed execution and producer receipt | M/E | Output without traceable provenance. |
| Immutable new IDs with `supersedes_ref`, retry provenance and no unsafe auto-retry | M/E | Rewritten snapshot, duplicate ID conflict, or unreconciled unknown outcome. |
| Matching relation artifacts, allowed endpoint pairs, symmetry | M | Orphan/mismatched ref or illegal symmetric edge. |
| Context independence/real reviewer provenance and assessment | M/E | Self-asserted independent review or invented `self_review`. |
| Valid accepted handoff recipient/receipt and input policy conditions | M/E | `ACCEPTED` invented or inputs inaccessible at acceptance time. |
| Effective permission owner, grantee/actor, target/action/source, time, revocation | M/E | Untrusted self-issued grant, replay or stale/revoked scope. |
| Pre-invocation permission for read-only/input access; unauthorized event quarantine | M/E | Empty side-effect list accepted as read permission, or unauthorized incident promoted as valid progression. |
| Independently enforceable first-use/replay condition for side-effecting tasks | E | Stateless/unbound grant accepted for first operation when identical replay cannot be distinguished. |
| Distinct scope verification and evidence class | S/M | `SYNTHETIC_FIXTURE` treated as verified execution or excluded from canonical evidence enum. |
| Typed reference resolver containment; digest match only if bytes exist | M/E | Traversal/cross-project leak or made-up digest. |
| Classification/egress/public promotion with external receipt | M/E | Relabel-only private-to-public transfer. |
| Probe status ≠ requirement oracle ≠ scope evidence; positive/negative validity | M/E | False system success from a completed detector. |
| v0.1 registry/experience fixtures unchanged; isolated handoff fixtures | Regression checks | Existing CLI interpreting handoff JSON as experience. |

## 11. Design tests W01–W15 (IDs preserved; wording refined) and proposed extensions

**W01–W15 remain design cases, NOT executed tests or fifteen JSON fixtures.** All future checks need *positive* and *negative* controls; reject-all behavior is not success. W01 should include explicit valid syntax/record parsing in addition to unsupported-version rejection.

| ID | Planned check | Canonical linkage |
| --- | --- | --- |
| W01 | Supported version/valid record accepted; unknown version rejected | T01; P0-D1 |
| W02 | `NOT_RUN` with fabricated outputs rejected | T03 |
| W03 | Unverified independent context claim rejected | T02, T16 |
| W04 | Invalid typed ref, edge endpoint or symmetry rejected | T17 |
| W05 | Actual digest mismatch blocks artifact use | T09 |
| W06 | `ACCEPTED` without authentic recipient receipt rejected | T15 |
| W07 | Missing/expired/revoked/wrong-scope grant denies side effects | T10; P0-D6 |
| W08 | Stale source SHA denies side effects | T19 |
| W09 | Partial CI cannot imply missing acceptance scopes | T06, T22 |
| W10 | Private-to-public relabel without promotion evidence rejected | T05 |
| W11 | Untrusted text cannot change authorization | T21 |
| W12 | Legacy experience/registry retained; handoff examples isolated | T12, T20 |
| W13 | Duplicate immutable ID / invalid supersession rejected | T11 |
| W14 | Unknown outcome cannot trigger unsafe retry | Execution/retry design |
| W15 | Three distinct design-only positives: P1 unexecuted, P2 accepted handoff without execution permission, P3 completed probe with failing requirement oracle | Defined in §13; not executed |

**Additional proposed cases, not renumbering W01–W15:**

| ID | Candidate positive/negative assertion | Layer |
| --- | --- | --- |
| W16 | Snapshot transition new ID plus valid supersession succeeds; conflicting in-place rewrite rejected | M/E |
| W17 | Grant replay beyond approved task/use scope rejected; legitimate bounded repeat-use not falsely rejected | M/E |
| W18 | Agent self-issued permission, actor/grantee mismatch or ambient-PO-credential delegation denied; only independently authenticated direct *human* PO actions may use the narrowly approved owner exception | E |
| W19 | Timestamp-order error, expired grant, or unverifiable revocation freshness denies action | M/E |
| W20 | Conceptual `fixture:` never accepted as materialized digest-backed evidence; real separately materialized synthetic input remains permissible when authorized | M/E |
| W21 | Byte-addressable artifact with absent/fabricated hash cannot claim byte integrity; non-byte output with null digest not falsely rejected | M/E |
| W22 | Pre-invocation `BLOCKED` has no task attempt/outputs; unauthorized observed read-only attempts remain truthful **quarantined incidents**, never accepted evidence/workflow progress | M/E |
| W23 | Evaluative review with unverified separation cannot claim independent status; genuine self-review remains representable | M/E |
| W24 | Classification relabel without approved transformation/promotion receipt denied | M/E |
| W25 | Requirement-FAIL successfully observed by probe is not converted to product PASS; nonzero exit and crash are distinguished | M/E |
| W26 | Two dissent refs preserved without auto-resolution | M/E; T08 |
| W27 | `ON_HOLD`/`UNREGISTERED` invocation denied; `CANDIDATE`/`RESEARCHED` with absent source/version, unverified availability, or unknown/restricted license also denied until separate authorized clearance | E; T04, T18 |
| W28 | Traversal, encoded traversal and cross-project resolver access rejected | M/E |
| W29 | `ACCEPTED` + later denied execution may be valid with original acceptance conditions satisfied | M/E |
| W30 | Proper required `NOT_VERIFIED` scope in a `NOT_RUN` design fixture | S/M |
| W31 | Public-record negatives (private classification, secrets, paths, personal/customer data, raw private transcripts) rejected; **separate `PUBLIC_REUSABLE`, rights-reviewed synthetic** public-mode positive accepted; fictional P1 `PROJECT_INTERNAL` is not that positive | S/M/E; privacy policy |

**Additional proposed design cases (not executed; W01–W31 IDs unchanged):**

| ID | Proposed positive/negative assertion | Layer |
| --- | --- | --- |
| W32 | Genuine read-only grant/PO-approved standing policy permits exact scoped input access; `allowed_side_effects:[]` without such permission blocks invocation; observed unauthorized `attempted=true` evidence is quarantined, not accepted | M/E; T10 |
| W33 | First side-effecting use with no externally enforceable operation/precondition/idempotency binding **and** no consumption tracking fails closed; legitimate approved repeatable/idempotent operation remains possible | E; T10 |
| W34 | `SUCCEEDED` without independent completion attribution cannot promote its execution claim to verified evidence or `OBSERVED_WITH_EVIDENCE`; legitimately verified completion is accepted for its narrow scope | M/E |
| W35 | `CANDIDATE`/`RESEARCHED` without pinned source/version, verified availability and allowed license/vetting cannot invoke; permitted, fully verified capability is not falsely rejected | M/E; T04 |
| W36 | Two supersession forks preserved without silent winner; self/cyclic/cross-kind `supersedes_ref` rejected; valid same-kind new-ID snapshot accepted | M/E; T11 |

**Additional structural negatives to specify at Gate B:** missing required field, extra top-level key, unknown enum, malformed/uppercase/short digest and invalid types; those cases are not yet executed or assigned additional W IDs.

**Not wire-validator-complete:** T07/T14 actual GitHub integration and squash branch disposition need live GitHub evidence; T13 distinct harness replay is Gate C/D; real U1–U4/D1 evaluations need permissioned device/API/database test evidence. No new benchmark, agent quality score, completion threshold or capability adoption is claimed.

## 12. Exact canonical Gate A domain-negative descriptions

These **design hypotheses** are copied from `docs/P0_SYNTHETIC_PILOT_SPEC_PROPOSAL.md` §5 at the pinned baseline, not observed failures:

| ID | Injected fictional defect | Expected future recognition / block |
| --- | --- | --- |
| `U1-N1` | Visually polished narrow-screen layout hides the primary CTA | Flag task-blocking responsive defect; do not report UX PASS |
| `U1-N2` | Two art directions differ only in colors | Reject claim of genuinely distinct design alternatives |
| `U2-N1` | Filtered task list displays an incorrect result count | Flag oracle mismatch; no aggregate dashboard success |
| `U2-N2` | Viewer role can submit an edit despite restricted policy | Block unauthorized mutation; require security verification |
| `U3-N1` | Longer Turkish label clips or hides a primary action | Mark locale-responsive requirement failed |
| `U3-N2` | Reconnection/back navigation erases completed step input | Fail persistence/recovery requirement |
| `U4-N1` | Focus escapes open modal or fails to return on closing | Flag keyboard/focus failure; block accessible acceptance |
| `U4-N2` | Decorative intense motion persists under reduced-motion setting | Flag preference violation and require retest |
| `D1-N1` | Concurrent clients both reserve last capacity slot | Fail capacity invariant; do not claim reliable transaction |
| `D1-N2` | Forward migration succeeds but rollback corrupts invariant | Fail migration/rollback acceptance even if unit tests pass |

The authoritative canonical wording and future receipt requirements remain in the source specification; no recreated text overrides it.

## 13. Positive controls P1–P3 (design-only); complete illustrative JSON for P1

**Fictional planning-only record.** This is not a real source SHA, actor, test, receipt, grant or public release. New candidate fields such as `actor.independence_assessment_ref`, `verification.scopes[].oracle_result` and exact scope-item shape are for **review**, not approved wire encoding. All identities use fictional/project-scoped labels; `fixture:` is non-resolvable in this design example.

```json
{
  "contract_version": "0.3-proposal",
  "record_kind": "HANDOFF",
  "handoff_id": "SYNTHETIC-WIRE-U1-P1-001",
  "workflow_id": "fixture:SYNTHETIC-WORKFLOW-U1",
  "workflow_run_id": "SYNTHETIC-PLANNED-NOT-RUN-001",
  "task_id": "SYNTHETIC-U1-CRITIQUE-PLAN",
  "created_at": "2026-11-04T00:00:00Z",
  "project_context": {
    "profile_ref": "fixture:SYNTHETIC-PROFILE-U1",
    "source_ref": "fixture:SYNTHETIC-SOURCE-U1",
    "source_sha": null,
    "policy_ref": "fixture:SYNTHETIC-POLICY-U1",
    "data_classification": "PROJECT_INTERNAL"
  },
  "relation": {
    "relation_id": "SYNTHETIC-REL-CRITIQUES-001",
    "type": "CRITIQUES",
    "from": { "type": "Role", "id": "ux-reviewer" },
    "to": { "type": "TaskRun", "id": "SYNTHETIC-PROPOSAL-TASKRUN" },
    "provenance_ref": "fixture:SYNTHETIC-U1-PLAN",
    "scope_ref": "fixture:SYNTHETIC-U1-REVIEW-SCOPE",
    "assertion_state": "PROPOSED",
    "evidence_refs": [],
    "input_artifact_refs": [],
    "output_artifact_refs": [],
    "symmetric": false
  },
  "actor": {
    "identity": "SYNTHETIC-INTENDED-REVIEWER",
    "role_id": "ux-reviewer",
    "harness_ref": null,
    "context_ref": null,
    "independent_context": false,
    "execution_receipt_ref": null,
    "upstream_actor_ref": null,
    "independence_disclosure_ref": null,
    "independence_assessment_ref": null,
    "self_review": null
  },
  "counterparty": null,
  "acceptance_receipt_ref": null,
  "capability_bindings": [],
  "inputs": [],
  "expected_outputs": [
    { "description": "Planned synthetic UX critique; not produced" }
  ],
  "outputs": [],
  "authorization": {
    "owner": "SYNTHETIC-NONAUTHORIZING-OWNER",
    "policy_ref": "fixture:SYNTHETIC-POLICY-U1",
    "permission_state": "NOT_REQUESTED",
    "allowed_side_effects": [],
    "permission_receipt_ref": null
  },
  "execution": {
    "state": "NOT_RUN",
    "attempted": false,
    "failure_code": null,
    "run_receipt_ref": null
  },
  "verification": {
    "state": "NOT_VERIFIED",
    "scope_ref": "fixture:SYNTHETIC-U1-REVIEW-SCOPE",
    "scopes": [
      {
        "scope_ref": "fixture:SYNTHETIC-U1-REVIEW-SCOPE",
        "requirement_ref": "fixture:SYNTHETIC-U1-REVIEW-REQUIREMENT",
        "state": "NOT_VERIFIED",
        "oracle_result": "NOT_EVALUATED",
        "evidence_refs": [],
        "limitations": ["Synthetic design-only example; no execution, independent review, or oracle observation occurred."]
      }
    ],
    "evidence": [
      {
        "class": "SYNTHETIC_FIXTURE",
        "reference": "fixture:SYNTHETIC-WIRE-U1-P1-001",
        "claim": "Fictional design-only example, not a test or receipt"
      }
    ]
  },
  "handoff_state": "DRAFT",
  "next_gate": {
    "owner": "SYNTHETIC-NONAUTHORIZING-PO-LABEL",
    "state": "NOT_REQUESTED",
    "decision_ref": null
  },
  "dissent_refs": []
}
```

**Sanity checks expected for future validator:** `NOT_RUN`/false attempted/null run receipt/empty output; no permission or real independence; explicit unverified scope; `SYNTHETIC_FIXTURE` only indicates invented example; proposed edge with matched actor Role and no invented input/output. This document's illustrative JSON has not been validated against a real handoff schema because none exists.

### P2 — Accepted handoff, no execution grant (positive design condition)

A future controlled test may represent `handoff_state=ACCEPTED` only with an *authentic, independently verifiable* acceptance receipt from an actual identified counterparty, policy-permitted/trusted inputs accessible at acceptance time, and no handoff-protocol blocker. Execution may stay `NOT_RUN` or be separately denied: **acceptance is not permission to run**. This is a conceptual positive-control definition, not a fabricated live receipt or executed fixture. A future mock verifier must clearly mark synthetic evidence and cannot prove production issuer authentication.

### P3 — Completed defect-detection probe, failing requirement (positive design condition)

A future controlled test may accept an attributable, actually completed `VALIDATES` probe with `execution.state=SUCCEEDED` while its named requirement oracle is `FAIL`, supported by evidence of the observed defect at the applicable verification scope. A successful probe is **not** product PASS. Where completion/producer evidence is absent, it may not claim the verified classes or use P3 as an executed positive. This is only a test design; no probe ran.

**P1/P2/P3 test status:** P1 is the sole full JSON illustration; P2 and P3 are defined semantic conditions, not JSON fixtures, actual grants, tested validators, or production claims. W15 references exactly these three conditions. The `PROJECT_INTERNAL` value in P1 is a fictional private-classification test vector **not** a `--public` validator admission control; `W31` requires its own separately rights-reviewed `PUBLIC_REUSABLE` positive.

## 14. Finding disposition and version history

| Claude Opus finding | Proposed v0.3 disposition and relevant section | Status |
| --- | --- | --- |
| C-01 HIGH | **MODIFY** — conceptual fixture vs materialized synthetic input, no placeholder hash (§4, §13). Do not ban real synthetic test execution. | Design addressed; independent closure pending |
| C-02 HIGH | **ACCEPT** — immutable snapshot, new ID, `supersedes_ref`, canonical optionals (§2–3). | Design addressed; independent closure pending |
| C-03 MEDIUM | **MODIFY** — risk-based grant task/use binding and replay controls, not universal `max_uses=1` (§7). | Design addressed; implementation open |
| C-04 MEDIUM | **ACCEPT** — verifier-controlled external owner trust roots and authorization cross-checks (§7). | Design addressed; implementation open |
| C-05 MEDIUM | **MODIFY** — distinguish dated conversation PO approval of directions from unpublished receipt / unapproved mechanics (§1). | Provenance clarified; GitHub recording pending permission |
| C-06 MEDIUM | **ACCEPT** — `ACCEPTED` requires recipient receipt, trusted/access-permitted inputs, no handoff protocol blocker (§6). | Design addressed; independent closure pending |
| C-07 MEDIUM | **MODIFY** — read-only tasks count as attempted; no fabricated receipts on interruption (§6). | Design addressed; exact event semantics open |
| C-08 MEDIUM | **MODIFY** — byte versus non-byte digests, null/unknown semantics and lowercase normalization (§4). | Design addressed; byte hashing algorithm details open |
| C-09 MEDIUM | **MODIFY** — no silent classification downgrade; evidence-backed authorized redaction/promotion exception (§9). | Design addressed; exact policy open |
| C-10 MEDIUM | **MODIFY** — probe completion vs requirement oracle and scope evidence; nonzero exits contextual (§8). | Design addressed; harness mappings open |
| C-11 MEDIUM | **MODIFY** — prohibit self-attested independence; do not pretend unknown means actual self-review (§5). | Design addressed; exact uncertainty encoding open |
| C-12 MEDIUM | **ACCEPT** — source-accurate canonical domain negative descriptions (§12). | Text aligned; review pending |
| C-13 LOW | **ACCEPT** — explicit `expected_outputs[]` object candidate, version handling and canonical enums (§2–3, §6). | Design clarified |
| C-14 LOW | **ACCEPT** — explicit unverified required scope and `next_gate=NOT_REQUESTED` for P1 (§8, §13). | Example addressed; no validator exists |
| C-15 LOW | **ACCEPT** — W16–W30 additional design tests, preserve W01–W15 plus positive controls (§11). | Design matrix extended; unexecuted |
| C-16 LOW | **DEFER WITH BOUNDARY** — no arbitrary path/URL resolution; exact ref grammar remains a gated choice (§4). | Security boundary stated; grammar open |
| C-17 LOW | **MODIFY** — temporal ordering and each-side-effect rechecks; exact tolerance/TTL open (§7). | Design clarified; policy open |
| C-18 LOW | **MODIFY** — Role endpoint/Actor matching only for the Actor's own edge (§3, §13). | Design clarified; case analysis open |
| C-19 LOW | **ACCEPT** — agent evidence labels, exact packet SHA attribution, canonical single-session term, version disambiguation (§1, §5, §14). | Provenance clarified |

These are **assistant-recommended dispositions**, not independent verified resolutions, final machine-contract acceptance or newly approved PO technical decisions.

Timeline of **proposal bytes and agent reports**, not releases: canonical P0 proposal → wire v0.1 (Gemini Flash `AGENT_REPORTED PASS WITH FINDINGS`) → wire v0.2 (Claude Opus High `AGENT_REPORTED PASS WITH FINDINGS`) → v0.3 initial Draft PR HEAD `6d3aa54...` (user-supplied Claude Opus High `AGENT_REPORTED PASS WITH FINDINGS`; findings N-01–N-18) → docs-corrected v0.3 HEAD `eb0fc5d...` (Argon High `AGENT_REPORTED BLOCKED` because original report attachment was unreadable; live-source review reported 3 MEDIUM + 5 LOW, R3-01–R3-08) → **proposed R3 documentation refinements awaiting new exact-byte review**. The `BLOCKED` result is not a PASS or GitHub `Approve`. The v0.2 Claude packet SHA-256 `3b70256ebe503e60113a7ceaee62d70289c2452424b87694d686e96df66eb433` covers an earlier complete *review packet*, not the standalone contract. Do not reuse an old v0.3 digest to identify edited bytes.

## 15. Open PO decisions and next gates

Still unresolved: read-only grant/standing-policy **wire representation** and exact canonical invariant-5 reconciliation; enforceable task/run/operation binding, idempotency/consumption model and repeat-use ledger choice; optional digest-limit encoding; supersession-fork authority; policy-aware reclassification; minimum completed-run receipts and verified-evidence promotion policy; public-mode synthetic fixture admission semantics and actual privacy structural tests; exact ref grammar, materialized fixture resolver/trust, exact scope/oracle/evidence-reference schema; `self_review`/independence uncertainty encoding **and reconciliation with canonical P0 invariant 4**; `attempted` tri-state/evidence under unknown invocation; trusted human-vs-agent delegation identity; **optional authorization-check audit receipt** and incident/quarantine record encoding; grant attestation/expiry/revocation freshness; `REVOKED` enum versus denial+ref, timestamp policy, content normalization, validator approach, contract migration strategy, and gate-specific acceptance criteria. The proposed **pre-invocation fail-closed rule** is a documentation recommendation, not a selected runtime mechanism or permission to begin Gate B. No decision is made by merely including a candidate in this document.

**Next recommended non-mutating step:** independent read-only delta review of the **new exact bytes** against `eb0fc5d...`, the original Claude N-01–N-18 findings, Argon R3-01–R3-08 and canonical P0. A second-model report does not replace PO acceptance or actual CI/native tests.

**Publication gate:** A separately scoped PO authorization is required for any new documentation file(s), feature branch, commit, push, Draft PR, Ready transition, merge method, integration, branch disposition and cleanup. Gate B actual schema/validator/tests and Gate C/D pilot remain separate permissions. Do not modify shipped v0.1 files or old historical records without explicit scope. `docs/DECISIONS.md` only receives accepted PO decisions with accurate scope and evidence.
