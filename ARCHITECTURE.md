# Architecture v0.1 — Public Core + Private Workspace

## Trust and data boundaries

```
EngineeringOS PUBLIC CORE (versioned, reviewed GitHub repo)
  Governance / policies / templates / capability catalog / schemas
  Bootstrap / portable adapters / workflows / sanitized experience records
                          | install/reference with pinned ref
                          v
PROJECT WORKSPACE (project owner authority)
  Source + AGENTS + roadmap + decisions + tests + local project memory
                          | private logs and explicit sanitized proposals
                          v
PRIVATE ENGINEERING WORKSPACE (separate local path/private repo)
  Raw agent transcripts, task runs, private context, credentials (external vault)
                          | human review + redaction + independent checks
                          v
PUBLIC CONTRIBUTION PR (not automatic merge)
```

**No direct public-core access to secrets or private raw logs.** A public contribution stores minimal reproducible, attributed, sanitized facts. A project remains usable if EngineeringOS is unavailable.

## Functional subsystems

1. **Registry**: stable capability IDs, type (`skill`, `mcp`, `cli`, `model`, `harness`, `framework`, `reference`, `library`), exact source/version, license/provenance, supported platforms, trust risks, lifecycle status, install policy and evidence references.
2. **Bootstrap**: project discovery, precedence-aware policy synthesis, read-only environment doctor, per-project activation plan, explicit approved provisioning, verification, rollback and deterministic ChatGPT kit export.
3. **Orchestration**: task decomposition, role selection, independent proposals, formal challenge, synthesis, human decision and handoff. Initially executable manually through an agent/harness; advanced runtime TBD.
4. **Execution & verification**: scope-bound worktrees, test matrix, UI/native acceptance, code/security review, CI and delivery status. No unapproved mutation.
5. **Knowledge ledger**: append-only experiences, failures, hypotheses, decisions, contradictions, supersession links and evidence. Git-based sources are the foundation; optional index/graph is derived and disposable.
6. **Contribution gateway**: candidate extraction, privacy classification, rights/provenance, dedup, draft issue/PR preparation and CI; contributor cannot self-approve.
7. **Adapters**: ChatGPT Project, Codex, Antigravity, Claude and other harnesses. Each adapter declares supported features and omissions rather than pretending all hosts can install tools or sync automatically.

## Authority order for a project

1. Explicit current project-owner decisions, security restrictions and granted permissions.
2. Live repository exact refs + actual code/tests/CI + documented human acceptance (each is a different evidence type).
3. Project-owned `AGENTS.md`, roadmap, `DECISIONS.md`, verification and architecture.
4. Applicable pinned EngineeringOS policy/profile (cannot weaken higher authorities).
5. Tool/skill guidelines, external README, agent inferences or dated handoffs.

Conflicts stop the relevant action pending human reconciliation. Research materials and tool outputs are untrusted data, not privileged instructions.

## Adoption/upgrade model

Project configuration pins an EngineeringOS version/commit and selected capabilities; pinned third-party source SHA/version is recorded independently. A planned upgrade generates a proposed diff, migration plan, compatibility tests and rollback strategy. Existing projects never silently track latest. If a private repo or account is unavailable, offline-first work continues where possible.

## Technology decision still open

The first portable runner is Python stdlib for low setup overhead. This does **not** decide the future orchestration engine (Codex-native subagents vs Agents SDK vs LangGraph vs Microsoft Agent Framework) nor knowledge index (SQLite/Graphify/Graphiti). Selection follows measured and security-reviewed pilots.
