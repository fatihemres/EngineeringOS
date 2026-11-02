# Security & Data Handling (DRAFT)

Do not submit credentials, auth tokens, private dumps, internal transcripts, end-user library databases, or production backups to this repository. Prefer an out-of-repository private workspace and a dedicated secrets manager. Avoid hidden telemetry or remote calls.

Threats: malicious third-party skill instructions, MCP tool impersonation, install-script supply chain, untrusted PR code, prompt injection via retrieved docs, accidental publication of workspace data, dependency compromise, symlink/path traversal in bootstrap and secrets in traces.

Never run untrusted fork code with elevated GitHub Action permissions or write-scoped repository tokens; public PR CI must use least privilege and avoid `pull_request_target` execution of contributor code. Pin external dependencies/Actions by reviewed immutable refs at production hardening; the draft workflow is a starting example only.

GitHub Private Vulnerability Reporting is enabled. Use the repository's [private security reporting interface](https://github.com/fatihemres/EngineeringOS/security/advisories/new). Keep sensitive vulnerability details out of public Issues. Repository owner `fatihemres` handles initial private security-report intake.
