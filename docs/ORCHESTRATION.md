# Multi-expert Collaboration Protocol

## Concepts
- **Role** = perspective and allowed work (UX specialist, API engineer, DB reviewer). Not necessarily an independent model.
- **Actor** = actual harness/session/model or human responsible for work; record ID and capabilities.
- **Skill** = instructions, **tool/MCP** = accessible interface, **runtime** = executes orchestration. Do not treat any as interchangeable.
- **Evidence broker** = canonical source pointers and read-only project facts; agent assertions are untrusted until checked.

## Workflow
1. Owner requirement and exact scope, baseline refs, data policy.
2. Coordinator identifies specialist tasks. For genuine independence, separate contexts or agents and avoid leaking solutions before initial proposals.
3. Specialists submit alternatives including tradeoffs, uncertainty, code/prototype and test intentions; all contributions attributed.
4. Cross-review challenges assumptions; security/data-integrity objections cannot be voted away. Preserve minority/dissenting review.
5. Coordinator synthesizes options with evidence references and unresolved disputes; PO decides product direction when required.
6. Authorized implementation in isolated branch/worktree; independent tests, performance, UI/a11y/native checks as applicable.
7. Experience report, risk register and upstream contribution candidacy; no automatic public sync.

## Debates must be bounded
Limit rounds, tool budget and roles per task. More agents is not inherently better. Refuse to claim 'collaboration' from sequential invocations sharing a single context; label as `MULTI-PERSPECTIVE_SINGLE_AGENT` instead of `INDEPENDENT_MULTI_AGENT`.

## UI/UX example
Art direction (Taste/UI-UX Pro Max), motion/components (project-appropriate implementation libs), critique (Impeccable + separate human review), code and performance review (Ponytail as optional final stage), Playwright/a11y/native acceptance. Preserve user-authored design choices, reduce-motion, keyboard, state and responsive behavior.

## API/DB example
Domain architect + API contract reviewer + database/transaction specialist propose; security specialist challenges auth/privacy/SQL injection; implementer tests rollback/migrations; independent reviewer checks API compatibility and backup semantics. Last simplifying pass must not remove intentional extensibility or safety guards.
