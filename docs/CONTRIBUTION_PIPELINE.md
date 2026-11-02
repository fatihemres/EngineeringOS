# Contribution & GitHub Governance (Draft)

EngineeringOS should accept outside PRs without granting contributor-provided code privileged access. Each consumer retains authority over its own integration policy.

1. **Discovery/Issue:** check duplicates and registry first; state source, expected value, trust risk, maintainers and exact scope.
2. **Candidate:** feature branch/fork, pinned dependencies, changed-file manifest, impact and rollback notes.
3. **Evidence:** reproducible tests, screenshots (if UI), exact version/harness/fixture, stated failures and limitations; sanitized experience JSON if proposing knowledge.
4. **CI:** JSON syntax/schema, test suites, links, secrets/privacy lint, dependency/license and third-party provenance (some are future gates; not all implemented in v0.1).
5. **Review:** independent reviewer, code/design/security as applicable; original PR author cannot self-approve; label review provenance.
6. **Maintainer merge:** branch rules/required checks, release notes, decision/registry update. Public core version changes are explicit.
7. **Consumer update:** project pins, checked upgrade proposal and roll-back. No automatic downstream modification.

## Governance to decide before public launch
Apache-2.0 is approved for original Public Core material. Open decisions include the contributor agreement/DCO, maintainers/CODEOWNERS, merge strategy, additional branch rules and required checks, issue labels, release cadence and compatibility policy. The main-governance ruleset is active and Private Vulnerability Reporting is enabled. Do not invent a unanimous maintainer agreement.

## CI security baseline
Least privilege `contents: read`, `pull_request` event, no `pull_request_target` execution of untrusted code, no secrets in fork jobs, no write tokens and no third-party install scripts until vetted. Production CI should pin actions to reviewed commit SHAs and maintain update governance.
