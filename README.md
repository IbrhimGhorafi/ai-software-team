# AI Software Team

A reusable, project-independent starter kit for coordinating AI-assisted software delivery with Claude Code. It contains agent definitions, skills, engineering standards, templates, and workflows—not an application.

## What is included

| Area | Contents |
|---|---|
| Agents | 12 focused roles under .claude/agents/ |
| Skills | 18 reusable procedures under .claude/skills/<skill-name>/SKILL.md |
| Shared instructions | .claude/CLAUDE.md and local permission guardrails in .claude/settings.json |
| Standards | Engineering, security, Git workflow, and definition of done |
| Templates | Requirements, stories, sprint plans, architecture decisions, test plans, code reviews, handovers, sprint reviews, retrospectives, release readiness, and daily reports |
| Workflow and docs | Project bootstrap, Agile delivery, orchestration contract, agent traceability, GitHub Projects setup, capabilities, and verification notes |
| Validation | Dependency-free Python static checks and regression tests |
| Security automation | Gitleaks secret scanning and weekly GitHub Actions dependency update PRs |

## Prerequisites

- Python 3.10+ for the static validator (standard library only).
- Claude Code installed and authenticated to verify actual agent/skill discovery. Follow the current official [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview).
- GitHub is optional for local use; GitHub Actions runs static checks on pushes and pull requests.

## Quick start

1. Clone or download this repository.
2. From the repository root, run `python scripts/validate_team.py`.
3. Start Claude Code from this directory.
4. Ask Claude Code to inspect the team configuration only, report which agents and skills it discovers, and identify version-specific issues. Do not authorize application creation unless you are ready to start a separate project.

## Agile commands

The available prompts include `/kickoff`, `/plan-sprint`, `/next-story`, `/review-pr`, `/status`, `/daily-report`, `/handover`, `/approve-gate`, `/sprint-review`, `/retro`, and `/release-check`. See [the command reference](docs/agile-command-reference.md). Commands run only when invoked in Claude Code; they are not background jobs.

## Give the team an idea

When ready to start an application, describe it in plain language, for example: "Build an e-commerce website where customers can browse products, purchase items, and track orders."

The team should perform discovery, requirements, architecture options, backlog preparation, test strategy and delivery planning, then implement incrementally through bounded tasks, isolated branches and PRs. The user supervises progress and makes material sponsor decisions; the team owns routine planning and coordination. The human owner alone merges PRs.

For the exact phases, recovery rules, evidence requirements and safety boundaries, read `workflows/orchestration-contract.md`, then `workflows/project-bootstrap.md` and `workflows/agile-agent-delivery.md`.

## Important security limits

- `.claude/settings.json` defines client-side permission deny rules for selected dangerous commands and sensitive file paths. These are defense-in-depth, not a substitute for GitHub permissions, branch protection, or careful review. Test behavior in the installed Claude Code version.
- `.gitignore` reduces accidental tracking of common local secret files but cannot remove secrets already committed.
- Gitleaks runs in GitHub Actions; separately enable GitHub Secret Scanning and Push Protection where available.
- Configure and verify GitHub rulesets/branch protection and permissions separately. Do not treat the human-merge rule in documentation as technical enforcement.
- The validation workflow uses read-only repository permissions and disables persisted checkout credentials.

## Important limits

- This repository does not itself run a background agent team when Claude Code is closed.
- Markdown task records and GitHub labels are not atomic distributed locks. The documented protocol is single-coordinator/single-writer unless separate isolated worktrees and a real coordination mechanism are configured.
- The validator checks repository structure, required content and selected security/workflow invariants. It does not prove agent discovery, delegation, application correctness, tests, deployment, or branch protection.
- Choose a project license before presenting the repository as licensed open-source software.

## Verification

Run `python scripts/validate_team.py` and `python -m unittest discover -s tests -v` locally, then inspect the actual CI result on the pull request. Use `docs/verification-report.md` to record a real Claude Code smoke test; do not mark runtime verification complete without evidence.
