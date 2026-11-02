# API & Database Feature Workflow (proposed)

1. Clarify domain entities, identity and invariants; distinguish user-owned data from derived/cache data.
2. Independent API (contract/errors/version compatibility), database (transactions/migrations/rollback/indexes) and security (auth/privacy/input) proposals.
3. Explicit cross-review: compare pagination, consistency, concurrency, failure semantics, integrity, migration/backup compatibility, and performance evidence.
4. Owner-approved implementation with synthetic isolated data; unit, integration, migration, rollback and adversarial tests.
5. Independent review and on-SHA CI; if user data or desktop involved, separate human native acceptance.
6. Preserve reasoned alternatives, actual failures, verified solutions and reusable lessons for local/private ledger and reviewed public contribution.
