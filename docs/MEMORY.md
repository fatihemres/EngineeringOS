# Engineering Experience Ledger

## Four layers
1. **Run evidence** (project-private by default): exact commands, logs, agents, contexts, source SHA, time, failures and test artifacts. Immutable dated original.
2. **Project memory**: canonical product decisions, architecture, status, accepted tests, scoped guidance. Does not inherit EngineeringOS rules over owner policy.
3. **Cross-project lessons**: carefully generalized and sanitized patterns/anti-patterns with evidence and applicability boundaries. Reviewed before promotion to public core.
4. **Derived indexes**: search, full text, local embeddings or temporal graphs. Rebuildable; not authority. Graphiti/Graphify are optional candidates, not prerequisites.

## Proposed experience feedback

[Capability Network](CAPABILITY_NETWORK.md), [candidate intake](CAPABILITY_INTAKE_PROTOCOL_PROPOSAL.md) and [continuity](PROJECT_CONTINUITY_PROTOCOL_PROPOSAL.md) describe a future chain from private task evidence to a reviewed, redacted, license-checked and synthetic public contribution candidate. The shipped `schemas/experience.schema.json` remains the authoritative v0.1 schema. No new private store, automatic sync or graph index is implied.


## Evidence, decision and status semantics
`HYPOTHESIS`, `AGENT_REPORTED`, `USER_REPORTED`, `SOURCE_REVIEWED`, `LOCAL_TEST_VERIFIED`, `CI_VERIFIED`, `HUMAN_NATIVE_ACCEPTED`, `PO_DECISION`. These are distinct, not a single numeric confidence. Record exactly what was tested and by whom. Conflicting information gets new dated correction/rebuttal and links; history is not rewritten.

## Required experience fields
The current v0.1 required fields are `schema_version`, `id`, `date`, `project`, `task`, `status`, `provenance`, `actors`, `tools`, `evidence`, `lessons`, `privacy`. The [shipped schema](../schemas/experience.schema.json) is the authoritative machine-readable contract; see the [valid synthetic example](../examples/synthetic-ui-review.json). Conceptual or future ledger dimensions such as scope, problem and attempts are not independently accepted top-level v0.1 fields. The schema rejects unknown properties.

## Agent capability memory
Track task category, outcome and tool versions, context limits, number of retries, independent reviewer, expected vs actual result, incident frequency and reproducibility. No model leaderboard based on unequal tasks; do not attribute joint-agent outcomes to one component without control.

## Promotion criteria
Repeatable or carefully scoped insight, non-proprietary source, sanitized example, no security escalation, linked evidence, applicable domain/platform, reviewer and maintainer approval. `AGENT_REPORTED` can be published as an attributed report but must not be recast as verified test data.


SYNTHETIC_FIXTURE identifies invented examples. Verified statuses require corresponding evidence types and a receipt reference. Validation checks declarations and cannot authenticate an external receipt or grant owner approval.
