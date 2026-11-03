# EngineeringOS — P0 Capability Network Handoff Contract (PROPOSAL)

> **Status:** `R2 TARGETED RE-REVIEW: AGENT_REPORTED PASS / PROPOSED / NOT IMPLEMENTED / NOT PO-APPROVED`  
> **Prepared:** 2026-11-03 · **Tracker:** [Issue #4](https://github.com/fatihemres/EngineeringOS/issues/4)  
> **Verified protected `main`:** `7c3a26cf3f6b3a6e715dc9b75689bff2f109da41`  
> **Git tree:** `4d1cd95651dcee8bde86412a20824d94b048e447`  
> **Post-merge push CI:** [#41607317625](https://github.com/fatihemres/EngineeringOS/actions/runs/41607317625), Windows/Ubuntu `SUCCESS` on that exact `main`.  
> **Review provenance:** Original 426-line candidate SHA-256 `01b0ce81bc686190c17ff9ce443f154c7bf8314df04fa3eba96d19425d94ca9b` received **Argon High AGENT_REPORTED PASS WITH FINDINGS** (F-P0-01–05; 2 MEDIUM, 3 LOW). The original 527-line R2 candidate (SHA-256 `cfa58364c99b56e10f0a6210992bd79f9f56c41e5777075ec5fa3186d5c24993`) received a **user-supplied independent Argon High targeted re-review report: AGENT_REPORTED PASS** on 2026-11-03; F-P0-01–05 reported RESOLVED, with zero new findings. The PASS is not a GitHub Approve, a PO architecture decision, an executable schema test or CI of this candidate. **This docs-only publication-preparation copy changes attribution/status text after that review and is not byte-identical to the Argon-reviewed R2.**  
> **Scope:** one review candidate drafted outside Git. No GitHub/repository/schema/CI mutations, external capability execution, third-party installs, private-data access, pilot, or orchestration runtime were authorized by preparation of this proposal.

## 1. Purpose, non-goals, source hierarchy

This document specifies a **proposed message and relationship contract** for bounded handoff between EngineeringOS capabilities and real actors. A handoff is a receipt-carrying unit of *claimed input, attempted action, produced artifacts, limitations, evidence and next authority gate*; it must not silently promote an agent claim into verified execution or a proposal into approval.

**Non-goals:** launching multi-agent orchestration; provisioning third-party tools; writing a graph database; deciding an SDK/harness; modifying current JSON schemas; writing project-private experience to public Git; completing E0 or starting E1–E7; choosing an implementation technology. All require new PO authority and independently verified evidence.

**Authority precedence:** explicit current project PO decisions/security constraints → real project repo HEAD/code/tests/CI and human acceptance as distinct evidence → project-specific canonical contracts → pinned EngineeringOS defaults → outside skill/README/agent statements. A lower-ranked source cannot expand permission. GitHub Issue text is a tracker, not an execution grant. Independent agent review is `AGENT_REPORTED`, not GitHub `Approve`.

**Sources inspected (pinned `main`):** `README.md`, `AGENTS.md` (DRAFT), `ARCHITECTURE.md`, `docs/DECISIONS.md`, `PROJECT_STATUS.md`, `VALIDATION_REPORT.md`, `docs/NEXT_DECISIONS.md`, `docs/PRIVACY.md` (Proposal), `docs/MEMORY.md`, `docs/IMPLEMENTATION_ROADMAP.md`, `docs/CAPABILITY_NETWORK.md`, `docs/P0_CAPABILITY_CONTRACT_DISCOVERY.md`, `docs/ORCHESTRATION.md`, `docs/PROJECT_CONTINUITY_PROTOCOL_PROPOSAL.md`, `workflows/{ui-ux-craft,api-database-feature,multi-agent-feature}.md`, `schemas/{registry,experience,project-profile,core}.schema.json`, `capabilities/registry.json`, `examples/synthetic-ui-review.json`, and `tools/engineeringos.py`. This is a source-backed candidate, not a shipped schema or independently reviewed acceptance.

## 2. Model boundaries and identity rules

| Object | Identity / owner | Normative distinction proposed for P0 |
| --- | --- | --- |
| **Capability** | Registry `id` + independent vendor/source ref/version; catalog administrator | A tool, MCP, skill, model, harness, library, CLI, framework or reference. Listed/`RESEARCHED` ≠ installed, licensed, usable or approved. |
| **Role** | Stable task-specific role ID; project/workflow contract | Engineering responsibility and required outputs, not a real human/session. Multiple capabilities can be candidates for the same role. |
| **Actor** | Concrete pseudonymous person or verifiable executed harness/session ID; project execution authority | Distinct from role and capability. `independent_context=true` requires a different actual context plus session receipt, not several prompts in one chat. |
| **Project context** | Project-owned profile ref + immutable source SHA + policy/owner ref | Refs only in public examples; project-specific contracts outrank portable guidance. |
| **Workflow / TaskRun** | Pinned workflow definition (`workflow_id`) + distinct workflow execution (`workflow_run_id`) + task/run IDs | Plan, definition, attempt, evidence and status are separate. `NOT_RUN` is not a failing or successful execution. |
| **Artifact** | Scoped URI/ref + optional content digest + classification and trust | Typed input/output receipt, **not yet a persisted graph-node type**. No content or secrets inside a public handoff. |
| **Evidence** | Evidence class + receipt ref + claim/limits; producer/observer | `AGENT_REPORTED`, `SOURCE_REVIEWED`, `CI_VERIFIED`, etc. are not interchangeable. A claimed test without actual test receipt is not `CI_VERIFIED`. |
| **Decision** | Decision owner + exact scope + receipt + date | PO gate controls side effects. Agent/CI result cannot silently grant it. |
| **Experience** | Project-private immutable record ID | v0.1 experience remains separate; public contribution is a reviewed proposal only. |

**Namespaces:** avoid conflating human display names with registry IDs (e.g. `UI/UX Pro Max` vs `ui-ux-pro-max`). Actor/session IDs should be privacy-safe pseudonyms where publication is contemplated. Same project/run ID must refer to the same pinned source. Source ref, tool version and artifact checksum may be `null` **only when correctly marked unknown/not run**; never guess a pin.

**Independence policy proposal:** 

- `independent_context=false`: shared context, simulated role, or unverified separation; report as `MULTI-PERSPECTIVE_SINGLE_AGENT` when applicable.
- `independent_context=true`: concrete distinct-session identifier **and** execution/context receipt, `independence_disclosure_ref` for controlled common inputs, and an upstream producer identity/context comparison; otherwise reject the independence claim. For an executed review, `self_review=false` additionally requires a verifiable identity/context mismatch. With no real execution, `self_review=null` (not evaluated), not an invented independent conclusion.
- Humans retain authority only if the project contract identifies their decision role; being an Actor never grants PO rights.

## 3. Proposed typed graph relationships (not shipped registry fields)

A proposed relation uses one **full edge contract**: `relation_id`, `type`, `from {type,id}`, `to {type,id}`, `provenance_ref`, `scope_ref`, `assertion_state`, `evidence_refs[]`, `input_artifact_refs[]`, `output_artifact_refs[]`, and `symmetric: boolean`. In the handoff envelope, run-specific `task_id` and executing Actor are inherited **only** from the enclosing `task_id` and `actor` (no duplicate nested fields). All lists may be empty when evidence/artifacts do not exist. The relation must match an allowed endpoint-pair; `input_artifact_refs[]` and `output_artifact_refs[]` must be consistent with the envelope's `inputs[]` and `outputs[]`. An unknown relation endpoint or mismatched artifact ref is rejected.

**Relation assertion state (draft enum):** `PROPOSED | OBSERVED_WITH_EVIDENCE | REJECTED | SUPERSEDED`. `OBSERVED_WITH_EVIDENCE` means **attributed, referenced observation only**, never automatic `LOCAL_TEST_VERIFIED` or PO adoption. `PROPOSED` can contain synthetic/context refs without claiming a real run. `symmetric=true` applies **only** to `ALTERNATIVE_TO` or `COMPLEMENTS` after explicit reciprocal semantics; other edges must have `symmetric=false`. Directed examples are always subject → object, and no reverse edge is invented.

| Relation | Proposed endpoints and semantics | Minimum proof / gate |
| --- | --- | --- |
| `CAN_FILL_ROLE` | Capability → Role; candidate suitability | Supported platform/version, provenance; does not prove availability/adoption. |
| `ALTERNATIVE_TO` | Capability ↔ Capability; comparable purpose | Same brief and evaluation rubric; independent trials needed before claims of relative quality. |
| `COMPLEMENTS` | Capability ↔ Capability; complementary outputs | Input/output compatibility and explicit permission; no automatic installs. |
| `PRODUCES_FOR` | Role → Role using an artifact ref and concrete TaskRun | Producer/consumer, artifact hash (when present), source and trust boundary. |
| `CONSUMES_CONTEXT_FROM` | Role → Evidence/source reference | Pinned provenance and sanitization; external text is untrusted. |
| `CRITIQUES` | Role → TaskRun proposal/artifact | Contradictions, actor/context independence and review receipt. |
| `VALIDATES` | Role → TaskRun result | Real test scope, exact source/artifact refs, tool/executor receipt and limitations. |
| `REVIEWS_CODE_AFTER` | Role → TaskRun implementation | Chronology, code revision, diff and *post-change* regression evidence. |
| `RECORDS_TO` | TaskRun → Experience | Project-private first; only supported fields in shipped experience v0.1. |
| `PROPOSES_UPSTREAM` | Experience → external sanitized contribution-proposal ref | Opt-in, source/license review, redaction, synthetic reproduction, human/PO review, PR/CI. |
| `PINNED_BY` | Project → EngineeringOS pinned core SHA **or** Capability/version ref (typed target) | Immutable source/version pin; no implicit latest. |
| `SUPERSEDES` | Same-kind immutable record: Evidence → Evidence, Handoff → Handoff, Experience → Experience, or Decision → Decision | Keep old immutable record, cited reason, date and replacement ref; never erase dissent. No cross-kind supersession. |

**Open schema choice:** the canonical node list has no first-class `Artifact` or `ContributionProposal` node. Above these remain **references**, not invented shipped nodes; determine a future typed ref grammar separately. In P0, use the published relation names, but avoid changing `capabilities/registry.json` or `schemas/registry.schema.json`.

## 4. Proposed handoff envelope — required / optional fields

This is a **draft interface**, **not** a shipped JSON Schema file, runtime or v0.1 experience object. A handoff has distinct *handoff lifecycle*, *execution outcome*, *verification scope*, *tool availability*, and *PO decision* axes. Field types, enums and cross-field semantics below are candidates for later validation **only after separate PO architecture and implementation permissions**.

| Field | Required? | Proposed constraints |
| --- | --- | --- |
| `contract_version`, `record_kind`, `handoff_id` | Yes | String e.g. `0.1-proposal`, fixed `HANDOFF`, unique immutable ID; replacement uses a new ID/supersession. |
| `workflow_id`, `workflow_run_id`, `task_id`, `created_at` | Yes | Distinguish pinned workflow definition (`workflow_id`), particular invocation, task and ISO-8601 UTC time. Synthetic `fixture:` definition refs are not live workflow pins. |
| `project_context` | Yes | `profile_ref`, `source_ref`, `source_sha` (nullable **only before execution/synthetic**), `policy_ref`, `data_classification`; compare `source_sha` against live repo HEAD before any action. |
| `relation` | Yes | Exactly §3 edge keys: `relation_id,type,from,to,provenance_ref,scope_ref,assertion_state,evidence_refs[],input_artifact_refs[],output_artifact_refs[],symmetric`; inherit task/Actor from envelope. |
| `actor` | Yes | Executing or **intended** Actor: `identity,role_id,harness_ref,context_ref,independent_context,execution_receipt_ref,upstream_actor_ref,independence_disclosure_ref,self_review`. The latter can be null for `NOT_RUN`. A role is not a session. |
| `counterparty` | Yes, nullable | For two-party transfers: receiving Actor or accountable human `{identity,role_id,context_ref}`. May be null in `DRAFT`, must be identified before `ACCEPTED`; distinct from executing `actor`. |
| `acceptance_receipt_ref` | Yes, nullable | Must be non-null, traceable and issued by the receiving party when `handoff_state=ACCEPTED`; **does not** approve execution. |
| `capability_bindings[]` | Yes (may be `[]`) | Canonical `registry_id` (nullable for unregistered research candidates), optional `research_candidate_ref`, actual `registry_status`, `source_ref`, `version`, `availability`, `license_state`, `usage_permission_ref`. Require an identity; `ON_HOLD`/unregistered/unknown blocks tool execution by default. |
| `inputs[]` | Yes (may be `[]`) | Each `{artifact_ref,content_sha256,classification,trust,purpose}`; source refs and claimed owner policy do **not** grant permissions. |
| `expected_outputs[]` | Yes | Planned artifact descriptions, not produced evidence. |
| `outputs[]` | Yes (may be `[]`) | Actual receipts: `{artifact_ref,content_sha256,classification,produced_by_run_ref}`; never populate for `NOT_RUN`, require run and digest verification when relevant to the artifact type. |
| `authorization` | Yes | `{owner,policy_ref,permission_state,allowed_side_effects[],permission_receipt_ref}`. Default deny, no implicit tool/network or GitHub consent. |
| `execution` | Yes | `{state,attempted,failure_code,run_receipt_ref}`; `NOT_RUN` requires `attempted=false`, empty outputs and null receipt. |
| `verification` | Yes | `{state,scope_ref,scopes[],evidence[]}`. `state` refers **only** to `scope_ref`, never blanket certification. `scopes[]` records each required or partial check with status, evidence refs and limits; unverified scope must remain explicit. `evidence[].class` has a distinct enum below. |
| `handoff_state` | Yes | `DRAFT | OFFERED | ACCEPTED | REJECTED | BLOCKED` (proposed). `ACCEPTED` requires counterparty + traceable acceptance receipt and no blocker, but not execution permission. |
| `next_gate` | Yes | `{owner,state,decision_ref}`; a recorded decision must have an authorized owner and scoped receipt. |
| `dissent_refs[]` | Yes (may be `[]`) | Preserve conflicting or negative claims without overwriting. |
| `failure_details`, `retry_of`, `supersedes_ref`, `review_notes` | Optional | Immutable follow-up attempt or same-kind supersession, not destructive update. Any free text remains untrusted data. |

**Proposed enum axes — DO NOT write these into shipped registry/experience schemas:**

| Axis | Draft values | Rule |
| --- | --- | --- |
| Registry status (read-only snapshot) | `CANDIDATE`, `RESEARCHED`, `ON_HOLD`, `UNREGISTERED` | First three are shipped registry states; `UNREGISTERED` is a **handoff observation**, not a registry mutation. `ON_HOLD` and `UNREGISTERED` block execution without a new explicit vetting/PO gate. |
| Capability availability | `UNVERIFIED`, `AVAILABLE_VERIFIED`, `NOT_AVAILABLE`, `INCOMPATIBLE` | Availability ≠ permission. |
| License posture | `UNKNOWN`, `SOURCE_REVIEWED`, `USAGE_APPROVED`, `REDISTRIBUTION_APPROVED`, `RESTRICTED` | Usage and redistribution rights separate; source review not license permission. |
| Permission | `NOT_REQUESTED`, `DENIED`, `SCOPED_GRANTED`, `EXPIRED` | A grant needs exact owner, scope, expiry and reference; no grant inherited from prior work. |
| Execution | `NOT_RUN`, `RUNNING`, `SUCCEEDED`, `FAILED`, `PARTIAL`, `BLOCKED`, `CANCELLED`, `OUTCOME_UNKNOWN` | A timeout is not success; `NOT_RUN` has empty outputs. |
| Verification state of a **specific scope** | `NOT_VERIFIED`, `AGENT_REPORTED`, `SOURCE_REVIEWED`, `LOCAL_TEST_VERIFIED`, `CI_VERIFIED`, `HUMAN_NATIVE_ACCEPTED` | No scalar global-confidence ordering; a valid CI receipt for tests does not verify native UI, migration rollback or other uncovered scopes. |
| `verification.evidence[].class` | `HYPOTHESIS`, `AGENT_REPORTED`, `USER_REPORTED`, `SOURCE_REVIEWED`, `LOCAL_TEST_VERIFIED`, `CI_VERIFIED`, `HUMAN_NATIVE_ACCEPTED`, `PO_DECISION`, `SYNTHETIC_FIXTURE` | Evidence class ≠ verification state. `SYNTHETIC_FIXTURE` is allowed evidence of an invented example, **not** a run/test result. |
| Relation assertion | `PROPOSED`, `OBSERVED_WITH_EVIDENCE`, `REJECTED`, `SUPERSEDED` | A proposed relation is not adopted or proven in operation. |
| Data classification | `PUBLIC_REUSABLE`, `PROJECT_INTERNAL`, `SENSITIVE`, `SECRET` | Unknown defaults to `PROJECT_INTERNAL`; redact/owner review before any public transition. |
| Input trust | `UNTRUSTED`, `PINNED_SOURCE_VERIFIED`, `OWNER_POLICY` | Default `UNTRUSTED`; trusted source/policy must have independently checked source/authority reference, never a caller-chosen magic label. |
| Decision | `NOT_REQUESTED`, `PENDING`, `APPROVED`, `REJECTED`, `EXPIRED` | PO decision is separate from CI and handoff acceptance. |
| Review characterization | `SELF_REVIEW=true/false/null` (field `actor.self_review`) | `null` for unexecuted/not assessed. An actual executed reviewer must disclose self-review and upstream identity/context comparison. |

**Cross-field invariants (candidate semantic validator rules, not currently executable):**

1. `NOT_RUN` → `attempted=false`, `run_receipt_ref=null`, `outputs=[]`, `verification.state=NOT_VERIFIED`; a synthetic fixture evidence item does not alter this.
2. `ACCEPTED` → identified `counterparty`, non-null `acceptance_receipt_ref`, accessible/trusted inputs within the project policy, and no blocking issue; acceptance is **never** permission to perform side effects.
3. `independent_context=true` on executed work → real distinct `actor.identity/context_ref`, `execution_receipt_ref`, `independence_disclosure_ref`, comparison to `upstream_actor_ref` and no shared reviewer/producer context; `self_review=false`. Missing or unverified receipt → independence claim rejected.
4. An executed `CRITIQUES`, `VALIDATES` or `REVIEWS_CODE_AFTER` must classify self-review (`true/false`) and provide target producer context where independence is claimed. A single harness reusing context is **not** independently reviewing itself.
5. No execution before an active scope-specific PO permission receipt, a pinned real project source, appropriate external candidate/license review, allowed egress and actual Actor identity. A handoff may remain `DRAFT/OFFERED/ACCEPTED` while execution remains `NOT_RUN`.
6. `relation.input_artifact_refs[]` and `relation.output_artifact_refs[]` must correspond to real `inputs[].artifact_ref` and `outputs[].artifact_ref`, including `[]` for zero inputs or zero produced outputs; all §3 relation metadata is explicit, with only enclosing task/Actor inherited.
7. `verification.state` is scoped by `scope_ref`; an unverified required check remains `NOT_VERIFIED` in `scopes[]`. Aggregate product/merge/acceptance success cannot be claimed when any applicable required scope is missing/failed. Attach every verified claim to independently observable receipts.
8. Unknown or conflicting status must not be silently promoted to execution, license approval, integration, native acceptance or release.

**Publication rule:** no private source/output contents, raw transcripts, local paths, secrets, personal account inventory or customer data in public handoff bodies. Public candidate records require owner opt-in, license/rights assessment, redaction, fictional/synthetic reproduction where appropriate, human check and separately authorized PR/CI. Source refs to private paths remain only in their access-controlled workspace.

## 5. Two fictional handoff records (syntax examples only)

**Both following records are fabricated**; they use `execution.state = NOT_RUN`, `verification.state = NOT_VERIFIED`, `independent_context = false`, no installation, no usage permission and no produced artifacts. They have never been validated by a shipped EngineeringOS handoff validator. Names and refs are fictional, and IDs prefixed `SYNTHETIC-` do not imply the data conforms to shipped experience v0.1.

### Scenario U — UI/UX critique handoff (fictional)

```json
{
  "contract_version": "0.1-proposal",
  "record_kind": "HANDOFF",
  "handoff_id": "SYNTHETIC-HANDOFF-UI-001",
  "workflow_id": "fixture:ui-workflow-contract",
  "workflow_run_id": "SYNTHETIC-WORKFLOW-UI-001",
  "task_id": "SYNTHETIC-TASK-UI-001",
  "created_at": "2026-11-03T09:00:00Z",
  "project_context": {
    "profile_ref": "fixture:ui-profile",
    "source_ref": "fixture:ui-source",
    "source_sha": null,
    "policy_ref": "fixture:ui-owner-policy",
    "data_classification": "PUBLIC_REUSABLE"
  },
  "relation": {
    "type": "CRITIQUES",
    "from": {
      "type": "Role",
      "id": "visual-critique"
    },
    "to": {
      "type": "TaskRun",
      "id": "SYNTHETIC-TASK-UI-PROPOSAL"
    },
    "provenance_ref": "fixture:ui-workflow-contract",
    "relation_id": "fixture:relation-ui-critique",
    "scope_ref": "fixture:ui-workflow-contract",
    "assertion_state": "PROPOSED",
    "evidence_refs": [],
    "input_artifact_refs": [
      "fixture:ui-proposal-a"
    ],
    "output_artifact_refs": [],
    "symmetric": false
  },
  "actor": {
    "identity": "Fictional UI Reviewer A",
    "role_id": "visual-critique",
    "harness_ref": null,
    "context_ref": null,
    "independent_context": false,
    "execution_receipt_ref": null,
    "upstream_actor_ref": null,
    "independence_disclosure_ref": null,
    "self_review": null
  },
  "counterparty": null,
  "acceptance_receipt_ref": null,
  "capability_bindings": [
    {
      "registry_id": "impeccable",
      "source_ref": null,
      "version": null,
      "availability": "UNVERIFIED",
      "license_state": "UNKNOWN",
      "usage_permission_ref": null,
      "registry_status": "CANDIDATE",
      "research_candidate_ref": null
    }
  ],
  "inputs": [
    {
      "artifact_ref": "fixture:ui-proposal-a",
      "content_sha256": null,
      "classification": "PUBLIC_REUSABLE",
      "trust": "UNTRUSTED",
      "purpose": "fictional proposal to critique"
    }
  ],
  "expected_outputs": [
    "source-attributed critique; accessibility issues; dissent if applicable"
  ],
  "outputs": [],
  "authorization": {
    "owner": "PROJECT_PO",
    "policy_ref": "fixture:ui-owner-policy",
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
    "evidence": [
      {
        "class": "SYNTHETIC_FIXTURE",
        "reference": "fixture:SYNTHETIC-HANDOFF-UI-001",
        "claim": "Illustrative record only. No capability or test executed."
      }
    ],
    "scope_ref": "fixture:ui-review-not-run",
    "scopes": [
      {
        "scope_ref": "fixture:ui-review-not-run",
        "state": "NOT_VERIFIED",
        "evidence_refs": [],
        "limitations": [
          "No actual work performed; illustrative handoff only."
        ]
      }
    ]
  },
  "handoff_state": "DRAFT",
  "next_gate": {
    "owner": "PROJECT_PO",
    "state": "NOT_REQUESTED",
    "decision_ref": null
  },
  "dissent_refs": []
}
```

**Illustrative stage walk-through:** same fictional brief → two independently *planned* alternatives, **not executed independent sessions** → PO aesthetic-choice gate → *if separately approved* prototype/motion implementation → code/artifact handoff to a visual-critique Role → browser/keyboard/reduced-motion/responsive checks → optional post-stabilization Ponytail review → **mandatory re-test after refactor** → private experience proposal. The sample envelope depicts just the **not-run critique handoff**, not the complete workflow.

**Illustrative negative path (NOT TESTED):** motion appears visually refined but keyboard focus order and reduced-motion behavior regress. The proposed reviewer records a conflict/evidence reference, `handoff_state=BLOCKED`, and an expected failure reason. Do **not** claim CI or human acceptance, and do not record the failure as a real bug without an executed reproducer.

### Scenario D — API/DB security challenge handoff (fictional)

```json
{
  "contract_version": "0.1-proposal",
  "record_kind": "HANDOFF",
  "handoff_id": "SYNTHETIC-HANDOFF-DB-001",
  "workflow_id": "fixture:db-workflow-contract",
  "workflow_run_id": "SYNTHETIC-WORKFLOW-DB-001",
  "task_id": "SYNTHETIC-TASK-DB-001",
  "created_at": "2026-11-03T09:00:00Z",
  "project_context": {
    "profile_ref": "fixture:db-profile",
    "source_ref": "fixture:db-source",
    "source_sha": null,
    "policy_ref": "fixture:db-owner-policy",
    "data_classification": "PUBLIC_REUSABLE"
  },
  "relation": {
    "type": "CRITIQUES",
    "from": {
      "type": "Role",
      "id": "security-review"
    },
    "to": {
      "type": "TaskRun",
      "id": "SYNTHETIC-TASK-DB-MIGRATION"
    },
    "provenance_ref": "fixture:db-workflow-contract",
    "relation_id": "fixture:relation-db-critique",
    "scope_ref": "fixture:db-workflow-contract",
    "assertion_state": "PROPOSED",
    "evidence_refs": [],
    "input_artifact_refs": [
      "fixture:db-migration-proposal-a",
      "fixture:db-invariants"
    ],
    "output_artifact_refs": [],
    "symmetric": false
  },
  "actor": {
    "identity": "Fictional Security Reviewer B",
    "role_id": "security-review",
    "harness_ref": null,
    "context_ref": null,
    "independent_context": false,
    "execution_receipt_ref": null,
    "upstream_actor_ref": null,
    "independence_disclosure_ref": null,
    "self_review": null
  },
  "counterparty": null,
  "acceptance_receipt_ref": null,
  "capability_bindings": [],
  "inputs": [
    {
      "artifact_ref": "fixture:db-migration-proposal-a",
      "content_sha256": null,
      "classification": "PUBLIC_REUSABLE",
      "trust": "UNTRUSTED",
      "purpose": "fictional transaction and migration proposal"
    },
    {
      "artifact_ref": "fixture:db-invariants",
      "content_sha256": null,
      "classification": "PUBLIC_REUSABLE",
      "trust": "UNTRUSTED",
      "purpose": "fictional integrity and rollback invariants"
    }
  ],
  "expected_outputs": [
    "threat and rollback objections",
    "negative-test design",
    "dissent if any"
  ],
  "outputs": [],
  "authorization": {
    "owner": "PROJECT_PO",
    "policy_ref": "fixture:db-owner-policy",
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
    "evidence": [
      {
        "class": "SYNTHETIC_FIXTURE",
        "reference": "fixture:SYNTHETIC-HANDOFF-DB-001",
        "claim": "Illustrative security review handoff only. No migration or security test executed."
      }
    ],
    "scope_ref": "fixture:db-review-not-run",
    "scopes": [
      {
        "scope_ref": "fixture:db-review-not-run",
        "state": "NOT_VERIFIED",
        "evidence_refs": [],
        "limitations": [
          "No actual work performed; illustrative handoff only."
        ]
      }
    ]
  },
  "handoff_state": "DRAFT",
  "next_gate": {
    "owner": "PROJECT_PO",
    "state": "NOT_REQUESTED",
    "decision_ref": null
  },
  "dissent_refs": []
}
```

**Illustrative stage walk-through:** invariant and source-contract briefing → separate planned domain/API/DB proposals → cross-critique for transaction boundaries, concurrent writes, auth, migrations/rollback → PO design selection → *separately authorized* synthetic implementation → unit/integration/migration/rollback/security tests → independent receipts → project-private ledger. The example is a **not-run security critique** only; no migration, database connection or security test was executed.

**Illustrative negative path (NOT TESTED):** migration forward succeeds but rollback violates a fictional invariant, while unit tests still pass. `PARTIAL` execution and a failing rollback receipt (if actually run) must block the `CI_VERIFIED` claim of complete acceptance and prevent a merge recommendation pending owner review.

### Mini-case — proposed `PRODUCES_FOR` two-party relationship (fictional; not a full handoff)

This **illustrates fields only**, not an executed transfer, produced artifact or accepted receipt. A complete envelope would inherit `task_id`, permissions, execution and evidence. Its `PRODUCES_FOR` relation is `PROPOSED`; a distinct recipient is named, but `acceptance_receipt_ref=null` and `handoff_state=OFFERED` **do not** constitute acceptance or permission:

```json
{
  "relation": {
    "relation_id": "fixture:api-db-proposed-transfer",
    "type": "PRODUCES_FOR",
    "from": {"type": "Role", "id": "domain-architect"},
    "to": {"type": "Role", "id": "api-implementer"},
    "provenance_ref": "fixture:api-db-workflow",
    "scope_ref": "fixture:api-db-workflow",
    "assertion_state": "PROPOSED",
    "evidence_refs": [],
    "input_artifact_refs": [],
    "output_artifact_refs": [],
    "symmetric": false
  },
  "actor": {
    "identity": "Fictional Domain Architect",
    "role_id": "domain-architect",
    "harness_ref": null,
    "context_ref": null,
    "independent_context": false,
    "execution_receipt_ref": null,
    "upstream_actor_ref": null,
    "independence_disclosure_ref": null,
    "self_review": null
  },
  "counterparty": {
    "identity": "Fictional API Implementer",
    "role_id": "api-implementer",
    "context_ref": null
  },
  "acceptance_receipt_ref": null,
  "handoff_state": "OFFERED"
}
```

The future receiving party could acknowledge **only after** policy and input checks, with a specific `acceptance_receipt_ref`. A simulated acknowledgment cannot authorize source edits, network calls or merging. A third-party capability binding, if proposed, must carry a registry status (including `ON_HOLD` or `UNREGISTERED`), provenance and permission state; the original two full `NOT_RUN` examples intentionally do not claim a real capability invocation.

## 6. Required negative-path decision table

| Input condition | Proposed record state and action | Mandatory evidence / owner gate |
| --- | --- | --- |
| `ON_HOLD` or unregistered capability encountered | `registry_status=ON_HOLD/UNREGISTERED`, `execution.state=BLOCKED` for that capability; no fallback install/use | Registry/source review, PO-vetted candidate/intake decision; no automatic promotion. |
| Capability not installed/found | `availability=NOT_AVAILABLE`, `execution=BLOCKED`; do not install | Discovery receipt; new install approval if proposed. |
| Capability source ref/version unknown | `UNVERIFIED`, `NOT_RUN/BLOCKED` for required execution | Pin exact source before execution; no `latest` fallback. |
| License unknown | `license_state=UNKNOWN`, block redistribution and dependent use pending context-specific legal/PO review | Source/license receipt and use/redistribution scope. |
| Network/secret/file access denied | `permission_state=DENIED`; `execution=BLOCKED`, no retry with broader privileges | Owner decision receipt; don't bypass. |
| Prompt injection in external README/tool response | Keep input `UNTRUSTED`; ignore instructions that request new authority or exfiltration | Trusted project policy and human/agent reviewer, never external text as authority. |
| Input is `PROJECT_INTERNAL/SENSITIVE/SECRET` and destination is public | `handoff_state=BLOCKED`; do not copy raw content | Classification + redaction + private-storage receipt + public opt-in review. |
| Tool result/CI only partially succeeded | `execution=PARTIAL` / `OUTCOME_UNKNOWN`; no global `CI_VERIFIED` | Actual per-check results, exact SHA, missing checks highlighted. |
| One model imitates multiple roles | `independent_context=false`; label `MULTI-PERSPECTIVE_SINGLE_AGENT` | Actual distinct context/session receipts required for independence claim. |
| Two independent reviewers disagree | Preserve both immutable reports in `dissent_refs`; `handoff_state=BLOCKED`, `next_gate.state=PENDING` if safety-relevant | Explicit unresolved item and PO/security gate; no automatic majority vote. |
| GitHub PR exists but not merged | `NOT_INTEGRATED` as **separate integration assertion**, no release/publication claim | PR current state, exact head, required CI, scoped PO merge authorization. |
| Merge performed but post-merge CI missing/failing | Do not mark integrated work `CI_VERIFIED`; branch disposition `CLEANUP_PENDING` | Actual main merge/tree/parents plus required push-CI run. |
| Source branch truly diverges (changed branch tip or non-equivalent tree) | Do not delete, do not infer integration; `PRESERVED_WITH_REASON` | Branch tip, tree, actual main/PR evidence, independent resolution/PO gate. |
| Squash-merged branch has equivalent tree but non-ancestor commits | Keep `PRESERVED_WITH_REASON` absent a separately approved squash-aware exception; no automatic deletion | Original tip SHA, PR ref, matching tree/merge receipt, post-merge CI and branch-specific PO decision. |
| Project source SHA lags live HEAD or fixture digest changes | `execution.state=BLOCKED`, refresh source/context and re-evaluate before action | Pinned expected SHA, newly observed HEAD, changed relevant rules/tests/refs; no silent rebase. |
| Duplicate/uncertain execution receipt | `OUTCOME_UNKNOWN`, stop; no blind retry | Query action result and reconcile before further mutation. |

Status values like `NOT_INTEGRATED` are **assertion labels** in this table, not official v0.1 enums.

## 7. Threat / authority matrix

| Threat / trust boundary | Principal risk | Proposed mandatory control | Cannot be authorized by |
| --- | --- | --- | --- |
| Upstream handoff claim/notes → downstream Actor | Prompt injection in `purpose`, `claim`, `expected_outputs`, `review_notes` or `failure_details` | Treat free text as untrusted data; verify receipts against policy and never expand `authorization` from content | Self-asserted authority in an artifact/handoff |
| External README/skill/MCP → Agent | Prompt injection, hidden shell/network action | Treat as untrusted source; quote/pin instructions, isolate execution, require PO grant | README claiming system/admin authority |
| Capability registry → Installer/runtime | Assuming a candidate is installed, compatible or safe | Verify source/version, license, platform, allowed egress; default no install | `CANDIDATE/RESEARCHED` label |
| Actor claim → Evidence broker | Fake independent contexts, forged tests or CI success | Verify actor/session/CI receipt from real authority; declare self-review | Agent-written assertion without receipt |
| Project → EngineeringOS Public Core | Exfiltration of private repo/code, paths, customer data, secrets | Owner opt-in, minimization, redaction, synthetic reproducer, source/license/human review | Another project's general EngineeringOS rules |
| Agent workflow → Project repo/GitHub | Unapproved edits, PR/merge, branch removal or bypass | Exact source refs, scope-specific approval, protected branch/CI checks, stop on uncertainty | Passing CI or previously granted different-task permission |
| Review output → PO decision | Mistaking reported PASS for authorization | Keep `AGENT_REPORTED`, `CI_VERIFIED`, human native acceptance, `PO_DECISION` separate | Independent agent PASS or majority vote |
| Private experience → derived memory/graph | Unauthorized retention and cross-project leakage | Private-first storage, derived disposable index, access controls; no always-on sync | Installing a memory tool |
| Third-party code → Public license | Incorrect redistribution under EngineeringOS Apache-2.0 | Attribution, source/license review, avoid bundling until separately approved | Public Core license alone |

**Deny-by-default:** secret/permission gap blocks action. `SOURCE_REVIEWED` never means security audit; GitHub-hosted tests never prove native UI or third-party tool safety. For internal/private data, preserve real source content and logs only in their owner-controlled workspace; public contract examples are fictional.

## 8. Compatibility with shipped Foundation v0.1

| Shipped baseline (verified) | Proposed P0 effect | Compatibility constraint |
| --- | --- | --- |
| `capabilities/registry.json`: 11 candidates, all `license_verified: false`, `auto_install: false`; statuses `CANDIDATE/RESEARCHED/ON_HOLD` | Define graph edges and evaluation, **separately** | Don't write edges or new lifecycle enums into v0.1 registry. |
| `schemas/registry.schema.json`: `schema_version=0.1`, `additionalProperties:false` | Versioned future relationship schema (open PO choice) | Existing records unchanged and current validator must keep accepting them. |
| `schemas/experience.schema.json`: required `schema_version,id,date,project,task,status,provenance,actors,tools,evidence,lessons,privacy`; `additionalProperties:false` | Link by existing `related_ids[]` and evidence/provenance refs *where allowed* | Handoff object **cannot** be embedded as unknown top-level field; do not relabel synthetic records as real executed tests. |
| `actors[]`: `role,identity` required; `independent_context` optional | Parallel handoff actor has stricter *proposal-level* execution receipt | Never claim shipped schema independently verifies real context separation. |
| `tools[]`: `id,version` required (version nullable); `source_ref` optional | Tool binding candidate metadata sits in separate handoff proposal | Don't invent installed version or validated license. |
| `evidence[]`: `type,description` required; `reference` optional | Proposed handoff requires receipt refs for verified claims | Experience status/evidence pairing is subject to its current `allOf` rules. |
| `SYNTHETIC_FIXTURE` validation and public fixture rules | Keep invented examples fictitious, source-attributed, review-gated | Public examples need actual publication review; this draft is not a committed fixture. |
| `schemas/project-profile.schema.json`: project technology/source_docs/governance, owner approval | Handoff uses profile ref, not full private project profile data | No new fields added to profile or real project writes. |
| `tools/engineeringos.py`: stdlib `check-json`, `validate-experience`, read-only `doctor`, explicit local kit export | Separate future `validate-handoff` MAY be proposed | CLI currently has **no** handoff validator or orchestration, and only a subset of JSON Schema is supported. `check_json` routes all root `examples/*.json` through public **experience** validation; do not put standalone handoff examples there without a separately authorized CLI/schema update. `check_shape` supports a restricted keyword/type subset (no `$ref`, `$defs`, `oneOf`, `anyOf`, number/integer validators; date-only format, not date-time); explicit Python semantic checks would be required for cross-field invariants. Secret-like key names are also rejected. |

**Proposed evolution (not approved):** first create a separate versioned `schemas/handoff.schema.json` and **path-isolated** synthetic handoff fixtures (not `examples/*.json` under the current CLI) in a future scoped PR **after** PO accepts the conceptual field choices. If relationships require independent automated checks, design a companion versioned relation contract; leave `registry` and `experience` v0.1 intact. Decide whether the initial validation is stdlib-compatible or uses a full independent JSON Schema implementation only after risk/maintenance review. Do not treat a future schema draft as approved implementation.

## 9. P0 acceptance test plan — design only (NOT EXECUTED)

| Candidate test | Expected contractual behavior |
| --- | --- |
| T01: Parse both full fictional JSON records and the mini-case fragment | JSON syntax correct; full records explicitly `NOT_RUN`, `NOT_VERIFIED`, no outputs; mini-case clearly not a complete envelope. |
| T02: Executed Actor with `independent_context=true` but missing context/session receipt | Reject independence claim. |
| T03: `NOT_RUN` with nonempty outputs or an actual CI-success claim | Reject inconsistent record. |
| T04: Unknown third-party version/permission, request external operation | Block execution; don't install or silently fall back. |
| T05: Private input ref routed to public output | Block data transfer until redaction+owner review. |
| T06: Partial/failed CI but requested `CI_VERIFIED` | Reject evidence promotion; preserve per-check status. |
| T07: Unmerged PR or no post-merge main push CI | Keep integration and release assertions unverified; defer branch disposition. |
| T08: Two conflicting reviewers | Keep both dissent refs, no automatic resolution. |
| T09: Run source/fixture digest mismatch | Block before use; preserve observed vs expected refs. |
| T10: Side-effect permission absent or expired | Default deny and require exact owner authorization. |
| T11: Repeated handoff ID with contradictory content | Require immutable append/new ID/supersession, not overwrite. |
| T12: Legacy v0.1 experience/registry fixtures | Stay valid and byte-identical under future migration tests. |
| T13: Two scenarios replayed with distinct harnesses when authorized | Assess real interoperability, latency/cost, and evidence quality separately; **not established here**. |
| T14: Squash-merge branch closeout | Distinguish true tree/tip divergence from equal-tree non-ancestor history; no deletion without separate permission. |
| T15: `ACCEPTED` without `counterparty` or receipt | Reject handoff; acceptance is not side-effect approval. |
| T16: Executed independent review with reused upstream actor/context | Reject independence claim or label as self-review; require controlled-input disclosure. |
| T17: Relation with missing/mismatched input refs or invalid symmetry | Reject mismatched `inputs[]`, wrong endpoints or `symmetric=true` for directed edge. |
| T18: `ON_HOLD` / unregistered candidate selected for a tool call | `execution.state=BLOCKED`; no implicit upgrade/install. |
| T19: Stale `project_context.source_sha` versus live repository | Deny side effects and ask for explicit updated source review/scope. |
| T20: Insert proposed handoff JSON in root `examples/` under v0.1 | Recognize that current `check-json` would attempt experience validation; avoid that path until authorized new validator. |
| T21: Untrusted free-text tries to escalate `authorization` | Ignore instruction, preserve observed injection and do not widen permissions. |
| T22: CI verified for code while native UI or rollback checks absent | Scope-limited CI receipt only; required unverified scopes remain explicit, no aggregate acceptance. |

**Evaluation design for actual quality gain:** compare matched brief/fixture, same time/tool budget, baseline single-context vs approved multi-role design, independent reviewers blinded to origin where feasible, real test/native-acceptance receipts, failure counts and negative effects. Report sample size, variance, missing data and dissent. One agent's subjective ranking is not efficacy evidence.

## 10. Open PO decisions and stage gates

| ID | Choice to make later | Proposed default (not accepted) | Evidence needed |
| --- | --- | --- | --- |
| P0-D1 | Independent handoff schema vs experience-v0.2 extension | Separate versioned handoff contract | Schema complexity, migration risks, existing fixture regressions. |
| P0-D2 | Initial transport/manual vs runtime scheduler | Manual artifact-ref handoffs first | Two controlled scenario tests, error and audit receipts. |
| P0-D3 | `Actor` identity and real independence | Private pseudonymous actor ID + verified distinct session receipt | Harness capabilities, context disclosure and failure cases. |
| P0-D4 | First-class `Artifact`/`ContributionProposal` nodes vs typed refs | Keep typed external refs in P0 | Graph query/evaluation need, privacy and schema migrations. |
| P0-D5 | Readiness/denied/lifecycle enum naming | Keep axes separate; no registry enum changes | Negative tests and cross-harness compatibility. |
| P0-D6 | Permission receipt format and expiry | Owner-authorized scoped immutable receipt | Repo governance and minimal secret-free audit records. |
| P0-D7 | Publication boundary for handoff/experience | Private by default, public only sanitized synthetic/approved | License, source, redaction and human acceptance. |
| P0-D8 | First synthetic pilot and objective scorecard | UI/UX + API/DB, same envelope with different constraints | Explicit PO permission for local writes/runs/network and resources. |

**Stage progression:** P0 read-only contract proposal → independent Argon/other review on exact draft revision → PO decision on the *contract proposal* → separately scoped docs/schema/fixture PR (if accepted) → CI and separate independent review → independently authorized merge → exact `main`-push verification → remote source-branch disposition review. **Issue #4 stays open** until its own accepted criteria/decision are satisfied; this document does not close E0 or authorize E1–E7.

**Future branch disposition:** The [Issue #3](https://github.com/fatihemres/EngineeringOS/issues/3) policy is proposed: after a separately authorized integration and successful required post-merge `main` CI, eligible **remote** source branches require an explicit disposition `DELETED_VERIFIED | PRESERVED_WITH_REASON | CLEANUP_PENDING` with scope-specific deletion permission. Local worktrees/evidence and older branches are not automatically cleaned; divergent/squash branch cases are not silently deleted.

## 11. Evidence, revision history and next review gate

- `SOURCE_REVIEWED`: this *candidate* is grounded in public exact-SHA EngineeringOS sources listed in §1. **It has not been accepted** as a machine contract or final architecture choice.
- **Original R1:** 426 LF-terminated lines; SHA-256 `01b0ce81bc686190c17ff9ce443f154c7bf8314df04fa3eba96d19425d94ca9b`. Google Antigravity/Gemini Argon High reported `AGENT_REPORTED PASS WITH FINDINGS` (F-P0-01–05: 2 MEDIUM, 3 LOW). The report confirmed original file read, JSON syntax, source contracts and zero repo mutation. It did **not** approve P0 decisions, a runtime, fixtures, tests or GitHub integration.
- **R2 corrective review candidate:** field/evidence enum and per-scope verification; explicit graph edge arity/status; two-party acceptance receipts and self-review/independence fields; workflow-definition identity, pinning and supersession; `ON_HOLD`, stale source, private/equivalent squash branch distinctions; CLI/fixture limitations; and review-prompt separation. **On 2026-11-03, the PO-provided independent Argon High R2 targeted review reported PASS** for the original R2 SHA-256 `cfa58364c99b56e10f0a6210992bd79f9f56c41e5777075ec5fa3186d5c24993`, explicitly marking **all five findings RESOLVED** (0 CRITICAL/HIGH/MEDIUM/LOW open or new). This is `AGENT_REPORTED` / `SOURCE_REVIEWED` evidence, **not** a native GitHub Approve, CI execution of this uncommitted candidate, or PO approval of P0-D1–D8. Attribution-only revisions in this publication-preparation copy require their own final delta review.
- **Finding traceability (R2 closure reported by independent agent; not executable/CI evidence):** `F-P0-01` (field/enum/relation/outputs consistency) → §§3–5; `F-P0-02` (recipient acceptance and independence/self-review) → §§2, 4–5; `F-P0-03` (node/edge identity and symmetry) → §§2–3; `F-P0-04` (ON_HOLD, equivalent-tree squash, stale HEAD, v0.1 CLI constraints, free-text injection) → §§6–9; `F-P0-05` (remove ephemeral review-dispatch prompt) → §11.
- **Publication-preparation delta · 2026-11-03:** Only the R2 banner, review-provenance sentence and §11 review attribution/traceability wording were updated in this draft. All three synthetic JSON code blocks and all technical contract fields remain unchanged relative to the reviewed R2 digest. The published-candidate SHA-256 is different from `cfa58364...`; it is pending a byte-exact final diff review and future separately authorized PR CI.
- `CI_VERIFIED`: only the existing Foundation main-push run [#41607317625](https://github.com/fatihemres/EngineeringOS/actions/runs/41607317625) on `7c3a26cf3f6b3a6e715dc9b75689bff2f109da41`, **not** R1/R2 or a handoff test.
- `NOT_EXECUTED`: no actual proposed actors, third-party skill, CI specific to this candidate, runtime, migration, browser/native QA, pilot, or public contribution promotion was executed for the fictional scenarios. JSON parsing is a local **syntax-only** check, not v0.1 schema validation.
- `NOT_SYNCED`: this R2 file has no EngineeringOS commit, Issue comment, branch/PR or ChatGPT Project Source synchronization. A future docs-only PR requires its own explicitly approved file scope, exact SHA/source review, CI, independent review, merge decision and post-merge branch disposition.

**Review-dispatch prompt is kept outside this public-core candidate** (in the surrounding private task handoff), not embedded as a repo specification. No PO contract decisions `P0-D1`–`P0-D8` are silently accepted by these candidate defaults.
