# Public/Private Boundary & Redaction Policy (Proposal)

## Public Core
Generic workflow contracts, reusable open-source code/templates, registry metadata, publication-reviewed synthetic examples, reproducible benchmark fixtures, release notes and reviewed contribution summaries.

## Private Workspace (outside public Git)
Raw agent conversations, private engineering notes, non-public repository summaries, credentials (in secret manager, never plain text), detailed local paths, personal data, customer/provider information, logs with embedded user content, private code and real data fixtures. Private workspace uses separate access control and backup policy; public core never automatically syncs it.

## Evidence classification
`PUBLIC_REUSABLE`, `PROJECT_INTERNAL`, `SENSITIVE`, `SECRET`. Unknown defaults to internal. A contributor-facing proposal must be explicitly marked public, source-licensed and sanitized. Project owner retains final disclosure authority.

## Promotion pipeline
Private experience → local classifier/author proposal → redact (people, path, URLs, identifiers, tokens, proprietary snippets) → synthetic reproducer → license/source check → human review → PR with evidence → CI + independent review → maintainer merge. On rejection, private entry remains intact. No automated export of raw transcripts.

## No silent ingestion
Do not enable always-on session capture, remote vector indexing, cloud model uploads, third-party error reporting, or auto-install of agent memory services merely because EngineeringOS is connected. Each connector declares network/data-access effects and opt-in permissions.


## Public examples

Use newly authored fictional fixtures. An experience in the public examples directory requires SYNTHETIC_FIXTURE, PUBLIC_REUSABLE, a matching fixture provenance reference and an affirmative publication review. Private historical records may retain their original privacy and review state. Review all free text before disclosure.
