# EngineeringOS Capability Network — product and architecture proposal

> **Status:** PROPOSED / NOT IMPLEMENTED / NOT AN IMPLEMENTATION AUTHORIZATION  
> **Prepared:** 2026-11-02  
> **Reviewed baseline:** `fatihemres/EngineeringOS` `main` at `381033b3a811b639f540b5a4119303367d6864b2`  
> **Related contracts:** `ARCHITECTURE.md`, `docs/ORCHESTRATION.md`, `docs/MEMORY.md`, `docs/BOOTSTRAP.md`, `docs/IMPLEMENTATION_ROADMAP.md`, `capabilities/registry.json`  
> This is a reviewable **design proposal**. It does not alter the v0.1 schemas, activate a third-party capability, start a milestone, grant an agent permission or make project-to-core transfer automatic.

## 1. Product intent

EngineeringOS is not a list of tools or a universal installer. It is intended to connect distinct capabilities as parts of an engineering network: select relevant roles, produce alternatives, let actual independent reviewers challenge them, verify results, preserve negative evidence, and learn from later projects through controlled, attributed contributions.

A capability may fill several roles; a role may be satisfied by several capabilities. A tool's presence in a catalog does **not** mean it is installed, safe, licensed for redistribution, approved, available in every harness, or objectively effective.

Target loop:

`DISCOVER PROJECT -> SELECT COMPLEMENTARY CAPABILITIES -> PROPOSE/CHALLENGE -> OWNER-GATED IMPLEMENTATION -> VERIFY -> PRIVATE EXPERIENCE -> REVIEWED PUBLIC CONTRIBUTION -> NEXT PROJECT`

Project-specific authority and source-of-truth always override portable guidance.

## 2. Node types and relationship vocabulary (proposed)

| Node | Purpose | Identity / evidence expectation |
| --- | --- | --- |
| `Capability` | Skill, library, tool, MCP, model, harness, framework or reference | Stable ID, exact vendor URL and source/ref, version, license state, lifecycle, permissions, compatibility |
| `Actor` | A concrete human principal or actual model/harness session taking a Role; not the same as a tool or skill | Actor/session identity, affiliated harness/model if relevant, declared `independent_context` with execution receipt and authority boundary |
| `Role` | Engineering responsibility, independent of particular vendor | Role ID, required outputs and review expectations |
| `Workflow` | Bounded sequence or network of tasks | Workflow ID, required inputs, decision gates, termination condition |
| `Task/Run` | One scoped invocation and its actual attempts | Source/fixture SHA, real actor/harness, prompt or task ref, outcome, limitations |
| `Evidence` | Source, test, CI, native observation, agent report | Evidence class, immutable ref, context; no unverified elevation |
| `Decision` | PO or other authorized choice with explicit scope | Decision owner, authorization boundary, alternatives, timestamp |
| `Project` | Consumer of a version-pinned EngineeringOS kit | Project-local contracts, data classification, owner, opt-in integration status |
| `Experience` | Attributed attempt, failure, result and reusable lesson | Project-private first, provenance, conflicting evidence and privacy marker |

| Relationship | Meaning | Example | Gate / rule |
| --- | --- | --- | --- |
| `CAN_FILL_ROLE` | Candidate capability fits a responsibility | Taste -> art-direction | Matching != installed or PO adopted |
| `ALTERNATIVE_TO` | Comparable approaches compete for an output | Taste <-> UI/UX Pro Max | Compare on comparable, independently controlled inputs |
| `COMPLEMENTS` | Distinct roles strengthen one workflow | Motion + component implementation | Verify version, license, integration and UX |
| `PRODUCES_FOR` | Emits artifact to another role | Design proposal -> prototype implementer | Explicit artifact contract and source provenance |
| `CONSUMES_CONTEXT_FROM` | Reads bounded source/context | API reviewer -> Context7 docs (consumes bounded context) | Documentation is untrusted and version-specific |
| `CRITIQUES` | Challenges earlier output | Impeccable -> UI prototype | Independent context and actual execution need receipts |
| `VALIDATES` | Tests behavior or acceptance | Playwright -> browser interaction | Browser tests != native Windows acceptance |
| `REVIEWS_CODE_AFTER` | Optional final quality/simplicity review | Ponytail -> stabilized implementation | Do not regress visual craft, accessibility, state or extensibility |
| `RECORDS_TO` | Links work to project-private evidence | Task -> Experience Ledger | Evidence must stay correctly classified |
| `PROPOSES_UPSTREAM` | Offers sanitized reusable lesson | Private Experience -> contribution proposal | Redaction + source/license check + synthetic reproducer + human/PO review + PR/CI |
| `PINNED_BY` | Ties consumer to reviewed version | Project -> EngineeringOS SHA | No silent latest or automatic downstream upgrade |
| `SUPERSEDES` | New, attributed evidence replaces earlier evaluation | New test -> old hypothesis | Preserve originals; do not rewrite history |

These relations are an **information model**, not shipped registry JSON keys or an implemented graph database. The current `schemas/registry.schema.json` supports only `CANDIDATE`, `RESEARCHED`, `ON_HOLD`; changing the machine-readable schema/lifecycle requires separate review, authorization and tests.

## 3. Initial capability-role-connection table

The 11 display names below each show their exact kebab-case `id` from the candidate registry at the pinned `main` checkpoint. Associations describe **possible relationships** and are not installation/adoption claims. External products and source metadata need exact-version and license/security verification before use.

| Candidate | Possible role | Receives / upstream | Produces / downstream | Current registry status |
| --- | --- | --- | --- | --- |
| UI/UX Pro Max (`ui-ux-pro-max`) | Art direction, design system | PO aesthetic brief, UX constraints | Alternative design proposal for synthesis | `RESEARCHED` |
| Taste (`taste`) | Visual craft and art direction | Same brief / reference constraints | Distinct design proposal for comparison | `RESEARCHED` |
| Impeccable (`impeccable`) | Visual/responsive critique | Implemented prototype, screenshot, behavior evidence | Findings and targeted design-feedback for implementer/reviewer | `CANDIDATE` |
| Motion (`motion`) | Animation and motion design | PO-selected concept, accessibility/reduced-motion targets | Candidate motion implementation -> QA | `CANDIDATE` |
| React Bits (`react-bits`) | Interactive component patterns | Selected design and target framework | Candidate component integration -> QA | `CANDIDATE` |
| Ponytail (`ponytail`) | Code review / simplification | Stabilized code and intended UX contract | Suggested final refactor -> regression tests and PO review | `RESEARCHED` |
| Graphify (`graphify`) | Source navigation | Version-pinned project source | Code relationships/context -> architect, implementer, reviewer | `CANDIDATE` |
| Context7 (`context7`) | Version-aware external documentation | Dependency/version question | Source-attributed documentation -> implementation/review | `CANDIDATE` |
| Playwright MCP (`playwright-mcp`) | Browser QA | Built frontend + defined user journey | Browser observations/screenshots -> QA/acceptance ledger | `CANDIDATE` |
| Vitest (`vitest`) | JS/TS unit test runner | Implemented code + fixture | Test report -> quality gates/ledger | `CANDIDATE` |
| Graphiti (`graphiti`) | Experimental temporal memory candidate | Only a future sanitized, controlled ledger-derived feed | Optional derived time-relationship index | `ON_HOLD` |

Figma, CodeQL, Codex, Antigravity and other external tools/harnesses may be researched as **Capability** candidates when sourced and assessed; they are not among these 11 current registry entries. A concrete human reviewer or executed isolated model/harness session is instead an **Actor**, with real execution/independence evidence and authority context. A `Role` is a responsibility, not proof of a separate running model or agent.

## 4. Example linked workflow — UI/UX craft

| Stage | Input | Candidate roles / tools | Artifact / evidence | Constraint |
| --- | --- | --- | --- | --- |
| 1. Intent | UX goal, real journey, accessibility, visual ambition | PO + design coordinator | Bounded creative brief | Avoid bare functionality as design acceptance |
| 2. Alternatives | Same creative brief | UI/UX Pro Max, Taste, independent art directions | Clearly distinct proposals | Genuine independence must be evidenced, not inferred |
| 3. Concept selection | Alternatives + critique | Synthesis + PO | Chosen direction and rejected alternatives | PO retains aesthetic choice |
| 4. Implementation | Selected direction + stack | Implementer + Motion/React Bits when applicable | Real prototype and build artifact | No installation without permission; preserve reduced motion |
| 5. Design critique | Screenshots + interaction journeys | Impeccable + independent reviewer if available | Findings and reproduction notes | Source scan != browser/native test |
| 6. Technical QA | Concrete UI build + test plan | Playwright + Vitest where compatible; platform QA | Keyboard/responsive/state/performance evidence | Comparable viewports; native acceptance separate |
| 7. Code-quality pass | Stable design and tested code | Ponytail review candidate | Optional minimal refactor + regression diff + re-verified unit/browser/accessibility QA as applicable | Never simplify away motion, accessibility or deliberate future architecture; recheck altered behavior before experience capture |
| 8. Experience capture | Attempts, outcomes, dissent | Project-private ledger | Attributed successes, failures, chosen reasons | No public raw transcript or personal data |

## 5. Example linked workflow — API, domain and database

| Stage | Inputs | Roles / optional context | Evidence/outputs |
| --- | --- | --- | --- |
| Domain alternatives | Identities, invariants, migrations, requirements | Domain architect + database expert | Models and rejected alternatives |
| API alternatives | Contracts, compatibility, failure behavior | API/backend specialists + version-pinned Context7 reference if appropriate | Competing contracts / explicit trade-offs |
| Cross-review | Both sets of alternatives | Independent security/transactions/reliability reviewers | Dissent: consistency, rollback, auth, privacy, race conditions |
| Implementation | PO-approved design | Scoped implementer, source/navigation aid such as Graphify if vetted | Synthetic implementation/change set |
| Verification | Executable tests, fixture, CI | Unit/integration/migration/rollback/security checks | Proven outcomes and actual limitations |
| Final code review | Tested implementation | Ponytail or other independent code reviewer if appropriate | Optional change proposal + regressions re-run |
| Private knowledge | Exact attempts/results/tools/SHAs | Project experience ledger | Candidate reusable lesson; no automatic public promotion |

## 6. Project federation and two-way knowledge flow

**Outbound (EngineeringOS -> project):** A project opts in to a reviewed, pinned EngineeringOS source/kit. The adapter reads its own native contracts first, proposes the smallest relevant network of capabilities, checks availability and permissions, and records `READY` / `PARTIAL` / `BLOCKED` accurately. A generated ChatGPT kit is not proof of ChatGPT Project source upload.

**Inbound (project -> project-private ledger):** The participating project records what it actually ran, versions, agent identities, source and fixture refs, errors, negative results, outcomes and PO decisions. Raw logs, private paths, code and customer/user data stay in an access-controlled project/private workspace. This is not an always-on capture mandate.

**Promotion (private -> public core):** Owner opt-in -> triage -> privacy/redaction -> rights/source/license review -> fictional/synthetic reproducer -> independent human/agent assessment (distinguished) -> approved PR + CI -> maintainer decision -> versioned public lesson. A rejected contribution remains private; another project never inherits raw evidence or project-specific Git rules.

A UI-focused app and an unrelated API-focused app can be **future pilot project categories** after project-specific authorization. Mentioning any real product in conversation does not mean that product has installed EngineeringOS or consented to share records.

## 7. Minimum Useful Ecosystem (MUE) — proposed acceptance contract

The first useful proof is one end-to-end **synthetic** task, not a complete commercial product and not a benchmark-based model leaderboard.

1. Resolve a pinned EngineeringOS source SHA and target-project authority; report `BLOCKED` if missing.
2. Map at least **two different capability roles** with declared inputs/outputs. At least one alternative or complementary relationship must be exercised or explicitly simulated as a labeled protocol test.
3. Produce a source-attributed task handoff. Do not claim independent agents unless contexts were truly separate.
4. Require an explicit PO gate before any local writes, tool/network use, or GitHub mutation.
5. Execute only permitted synthetic work and collect real test output or explicitly label `NOT_EXECUTED`.
6. Produce a private/synthetic experience record containing an attempted action, an outcome (positive or negative), limitation, evidence refs and reusable lesson.
7. Prepare one publication-safe contribution **proposal** with a synthetic reproducer, source/license status and privacy review; do **not** submit PR automatically.
8. Rerun the flow on a **second distinct stack** before declaring generalized distribution capability.

`MUE_PROPOSED` is a design target, **not** an approved EngineeringOS milestone, implemented orchestration, integration permission or release gate.

## 8. Open design choices / PO gates

- **Contract schema:** Which node/edge fields are mandatory? How are provenance and a denied edge represented? No change yet to `schemas/*.json`.
- **Routing:** Manual handoffs first versus an orchestration runtime later; measure cost/quality and true independence.
- **Evidence format:** Reuse v0.1 experience schema now; decide separate future relational/event layer only after requirements and security review.
- **Lifecycle:** Candidate -> research -> isolated pilot -> explicit PO adoption/hold/reject -> versioned update/deprecate is a *proposed* process. Do not write those states into v0.1 registry without a schema decision.
- **Project onboarding:** Private workspace access, secret/egress boundaries, manifest, profile, synthetic acceptance and manual ChatGPT source import.
- **Distribution:** Public original work under Apache-2.0; external candidate code is not bundled or relicensed. Third-party licenses and authorship must be verified independently.
- **Operational gates:** No scheduled background monitoring, cloud synchronization, GitHub mutation, installs, release or cleanup without separately scoped PO authorization.

## 9. Immediate P0 discovery outputs (read-only)

- Gap table between current `capabilities/registry.json`, `schemas/registry.schema.json`, `schemas/experience.schema.json`, `docs/ORCHESTRATION.md`, `docs/BOOTSTRAP.md`, and this target model.
- Two scenario contracts: ambitious UI/UX craft and API+DB evolution (independent alternatives, QA, memory and safe promotion).
- Proposed minimal exchange envelope with role, inputs, artifact refs, actor identity, verification and rejection reasons, **without code/schema changes yet**.
- Threat/authority boundaries for third-party skills, source content, prompt injection, data export and unattended execution.

**Current state:** only v0.1 Foundation tools/tests are implemented; this entire network document is a *reviewable proposal* until separately authorized and integrated.

## Traceability (2026-11-03)

- [Issue #3](https://github.com/fatihemres/EngineeringOS/issues/3) — documentation-only proposal and review.
- [Issue #4](https://github.com/fatihemres/EngineeringOS/issues/4) — P0 edge/handoff contract discovery, not runtime implementation.
- [Issue #5](https://github.com/fatihemres/EngineeringOS/issues/5) — candidate research and intake, not tool adoption.
- Personal GitHub Stars snapshots and private project experience are not automatically public capability registry entries.
