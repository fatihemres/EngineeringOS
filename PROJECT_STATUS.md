# Foundation status · 2026-11-02

The governance seed is published on main at `2b18708c30da03e59578cc4f7f4ebe8f269aec4d`. Repository ruleset `main-governance` (#26365625) is active. Updates to main require a PR, with zero required approving reviews, restricted deletion and non-fast-forward updates, and no bypass actors. GitHub Private Vulnerability Reporting is enabled.

R1 local remediation completed. Its Windows suite recorded 23 PASS, 0 FAIL and 1 SKIP. The PO reports that independent Antigravity R1 re-review completed with PASS WITH FINDINGS. The R1-NEW-01 bootstrap example is corrected in this Foundation candidate, with regression coverage for the documented external destination and continued traversal rejection.

Foundation v0.1 is prepared on an isolated feature branch for a draft PR. Hosted Windows and Ubuntu CI and subsequent independent PR review remain pending at this source checkpoint. Foundation is unmerged and unreleased. Integration requires separate explicit PO authorization.

Agent orchestration, remote provisioning and ChatGPT source synchronization remain unimplemented. The CLI provides local discovery, validation and explicit kit export. See [remaining gates](docs/NEXT_DECISIONS.md).
