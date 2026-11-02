# Contributing — policy draft (not yet activated)

The public GitHub repository exists and the PO has chosen **Apache-2.0** for original EngineeringOS Public Core materials. **The governance seed is published. Foundation CI and integration remain pending at this source checkpoint.** This document describes a proposed contributor process, not an active promise that contributions can already be merged.

Before contributing, review [LICENSE](LICENSE), [NOTICE](NOTICE), [SECURITY.md](SECURITY.md), the [public/private policy](docs/PRIVACY.md) and [third-party rights](LICENSES_THIRD_PARTY.md). Do not assume rights to copy, adapt or redistribute third-party skill/tool code simply because a GitHub URL appears in the registry.

Propose a focused Issue, check for existing work, and submit a scoped PR with source attribution, exact versions and reproducible evidence **under the approved repository governance**. Never include automatic tool installation, secrets, private data, uncontrolled network or execution of contributor-supplied skills in privileged CI.

For reusable engineering experience, submit **sanitized** evidence: what happened, reproduction on synthetic data, tool/harness version and tested outcome. Do not submit raw private chats, proprietary code, account IDs or filesystem usernames. Mark `AGENT_REPORTED`, `SOURCE_REVIEWED`, `LOCAL_TEST_VERIFIED`, `CI_VERIFIED` appropriately.

A PR requires independent review, least-privilege automated checks and authorized maintainer action. An author cannot independently approve their own work. Rejected proposals should retain an explained reason rather than silently rewriting historical findings. Release and version publication are separate gates. The main-governance ruleset and private reporting channel are enabled. DCO/CLA, CODEOWNERS and additional required CI or human-review rules remain pending owner decisions.
