# AI Software Team

A reusable, project-independent starter kit for coordinating AI-assisted software delivery with Claude Code. It contains agent definitions, skills, engineering standards, templates, and workflows—not an application.

## What is included

| Area | Contents |
|---|---|
| Agents | 12 focused roles under .claude/agents/ |
| Skills | 18 reusable procedures under .claude/skills/<skill-name>/SKILL.md |
| Shared instructions | .claude/CLAUDE.md |
| Standards | Engineering, security, Git workflow, and definition of done |
| Templates | Requirements, stories, sprint plans, architecture decisions, test plans, code reviews, handovers, delegation, and daily reports |
| Workflow and docs | Project bootstrap, Agile delivery, orchestration contract, agent traceability, GitHub Projects setup, capabilities, and verification notes |
| Validation | Dependency-free Python static checks and GitHub Actions |

## Prerequisites

- Python 3.10+ for the static validator (standard library only).
- Claude Code installed and authenticated to verify actual agent/skill discovery. Follow the current official [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview).
- GitHub is optional for local use; GitHub Actions runs static checks and a Gitleaks secret scan on pull requests and pushes to `main`.

## Quick start

1. Clone or download this repository.
2. Run `./install.sh` on macOS/Linux, or `./install.ps1` in PowerShell on Windows; these helpers only check Python and run static validation. Alternatively, run `python scripts/validate_team.py` directly.
3. Start Claude Code from this directory.
4. Ask Claude Code to inspect the team configuration only, report which agents and skills it discovers, and identify version-specific issues. Do not authorize application creation unless you are ready to start a separate project.

## Give the team an idea

When ready to start an application, describe it in plain language, for example: "Build an e-commerce website where customers can browse products, purchase items, and track orders."

The team should perform discovery, requirements, architecture options, backlog preparation, test strategy and delivery planning, then implement incrementally through bounded tasks, isolated branches and PRs. The user supervises progress and makes material sponsor decisions; the team owns routine planning and coordination. The human owner alone merges PRs.

For the exact phases, recovery rules, evidence requirements and safety boundaries, read `workflows/orchestration-contract.md`, then `workflows/project-bootstrap.md` and `workflows/agile-agent-delivery.md`.

## Important limits

- This repository does not itself run a background agent team when Claude Code is closed.
- Markdown task records and GitHub labels are not atomic distributed locks. The documented protocol is single-coordinator/single-writer unless separate isolated worktrees and a real coordination mechanism are configured.
- The validator checks repository structure and selected workflow invariants only. It does not prove agent discovery, delegation, application correctness, tests, deployment, or branch protection.
- Configure and verify GitHub rulesets/branch protection and permissions separately. Do not treat the human-merge rule in documentation as technical enforcement.

## Verification

Run `./install.sh` (POSIX) or `./install.ps1` (Windows PowerShell), or run `python scripts/validate_team.py` locally, and inspect the actual CI and secret-scan results on the pull request. Use `docs/verification-report.md` to record a real Claude Code smoke test; do not mark runtime verification complete without evidence.
