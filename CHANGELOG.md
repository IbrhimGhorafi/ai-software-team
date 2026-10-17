# Changelog

Notable changes to this starter kit are recorded here.

## Unreleased

- Add local Claude Code permission deny rules for selected dangerous commands and sensitive paths.
- Add a Gitleaks GitHub Actions workflow and common local-secret ignore patterns.
- Harden repository validation for required command/template inventories, non-empty content, and selected security configuration.
- Add negative validator regression tests for manifest containment, hard inventory floors, workflow permissions, action SHA pins, and command metadata.
- Compare manifest requirements with the pull-request base in CI to detect silent reductions.
- Extend Claude Code deny rules for destructive Git operations and repository deletion.
- Rename the mock discovery check to an offline inventory check and remove its duplicate frontmatter parser.
- Disable persisted checkout credentials in the validation workflow.
- Remove direct file-write capability from the technical research agent.
- Add sprint review, retrospective, and release-readiness commands and templates.
- Add weekly Dependabot updates for GitHub Actions.
- Add GitHub pull request template, CODEOWNERS, security policy, and contribution guidance.
