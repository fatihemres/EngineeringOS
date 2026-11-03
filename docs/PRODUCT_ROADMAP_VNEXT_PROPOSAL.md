# EngineeringOS Product Roadmap vNext — proposal / overlay

> **2026-11-02. PROPOSED; not an accepted milestone plan, implementation grant, release or replacement for `docs/IMPLEMENTATION_ROADMAP.md`.**
> Baseline: `main` `381033b3a811b639f540b5a4119303367d6864b2`. Foundation v0.1 is integrated/CI-verified but unreleased. E0 milestone closure is not separately authorized.

## North star

A portable, continuously improvable engineering ecosystem: capabilities act as composable parts of a network, collaborate and critique each other where measurable, preserve evidence with its provenance, and exchange transferable lessons across independent projects through voluntary, protected contribution gates.

**Operational principle:** The best outcome comes from complementary capabilities and measured handoffs, *not* maximal tool count, auto-installation, universal model scores, or forced consensus.

## Proposed phases mapped to the existing E0-E7 structure

| Existing increment | vNext emphasis | Available today | To prove later |
| --- | --- | --- | --- |
| E0 Foundation | Security/authority/repository/source contract | Merged Python CLI + docs + two-platform CI | Formal PO E0 closure and release are still separate |
| E1 Bootstrap | Project discovery, pinned kit, opt-in environment plan/readiness | Doctor, local kit preview/explicit export | Correct new/existing project onboarding without override or misleading `READY` |
| E2 Registry | Capability + role + typed relationship network | 11 candidate entries, basic registry/schema | Real source/version/license/permissions, compatibility, edges, lifecycle gates |
| E3 Collaboration | Independent alternatives, critique, synthesis, actual actor handoffs | Proposed workflow Markdown | Evidence-backed distinct contexts, disagreement, controlled coordination |
| E4 Experience Ledger | Immutable task/attempt/failure/evidence, private first | JSON v0.1 schema and synthetic checks | Searchable private experience + feedback associations + safe promotion candidate |
| E5 Contribution Gateway | Voluntary safe project-to-core promotion | Issue/PR templates and policy | Sanitized synthetic reproducer through reviewed Issue/PR/CI gate |
| E6 Distribution | Version-pinned adapters + safe two-way project onboarding | ChatGPT kit local export only | Two distinct stack pilots; no silent cloud/updates |
| E7 Optional Observatory | Evidence-aware capability/project UI | Not implemented | Inspectable, private, non-telemetric activity visualization |

## Proposed delivery waves (not milestone authorizations)

| Wave | Design objective | Earliest proof | Boundary |
| --- | --- | --- | --- |
| 0. Contract / P0 discovery | Define roles, relationships, artifact handoffs, data/evidence and ownership | Two completely different scenarios fit one model | No file/tool/CI/GitHub mutation needed for analysis |
| 1. Connected foundations | Minimum registry/bootstrapping/experience handoff | Pinned synthetic project + role selection + proof-carrying record | Scope and schema edits separately approved |
| 2. Real collaboration | Independent design/API reviews and workflow feedback | One synthetic MUE with true actor provenance and CI/test observations | No false multi-agent or native acceptance claim |
| 3. Project federation | Opt-in two-way adapters, private feedback and reviewed public contribution | First permitted project pilot, then independent different-stack pilot | No private raw logs to public; owner policy prevails |
| 4. Sustainable ecosystem | Capability lifecycle/evaluation/updates + optional interface | A tool version can be adopted/deprecated and compared to older evidence | No unapproved install, always-on capture, or automatic release |

## Minimum Useful Ecosystem (MUE)

`PROJECT -> PINNED BOOTSTRAP -> ROLE NETWORK -> CONTROLLED COLLABORATION -> VERIFIED WORK -> PRIVATE EVIDENCE -> SANITIZED PROPOSAL -> REVIEWED CORE UPDATE -> FUTURE OPT-IN PROJECT`

First proof is synthetic and small. It must preserve exact source references, actor independence, permissions, test output, unknowns and negative outcomes. An upstream candidate is **not** an automatically published GitHub PR. Two differently scoped project pilots must precede portability claims.

## Initial research / decision backlog (not GitHub Issues)

**P0:** Core capability, role, relation and evidence-envelope vocabulary; UI/UX and API+DB scenario acceptance; preflight/effect/secret boundary; existing implementation gap matrix.

**P1:** Source-pinned registry/lifecycle proposal, proof-carrying workflow handoff and the first synthetic experience/reporting vertical slice.

**P2:** Opt-in project onboarding, private contribution inbox, reviewed public promotion and second project stack trial.

**P3:** Sustained capability monitoring/review, optional observability and future release strategy, all separately authorized.

## Explicitly open decisions

1. Product-direction acceptance is **not** E1 implementation authorization.
2. No **unapproved or unconditional** branch cleanup, Issue/PR creation, third-party setup, remote telemetry, ChatGPT Project sync, roadmap integration or release. The PO requests eligible future EngineeringOS remote source branches be cleaned up **after independently authorized merge and verified post-merge main-push CI**, using separately scoped branch-deletion permissions. Details: [continuity protocol](PROJECT_CONTINUITY_PROTOCOL_PROPOSAL.md), [Issue #3](https://github.com/fatihemres/EngineeringOS/issues/3). Existing historical branches and local worktrees are preserved; no GitHub auto-delete setting change is implied.
3. Whether a new registry schema, separate relations table or private knowledge store is appropriate remains an architectural decision.
4. Technical sequencing may evolve based on tests, licensing, security and owner priorities; waves are *not* an irreversible dependency schedule.
