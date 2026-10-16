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
| Workflow and docs | Project bootstrap, Agile delivery, agent traceability, GitHub Projects setup, capabilities, and verification notes |
| Validation | A dependency-free Python static validator and GitHub Actions workflow |

## Prerequisites

- Python 3.10+ to run the static validator (standard library only).
- Claude Code installed and authenticated to verify actual agent/skill discovery. Follow the current official [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview).
- GitHub is optional for local use; GitHub Actions runs the static check when changes are pushed or a pull request is opened.

## Quick start

1. Clone or download this repository.
2. From the repository root, run the static validator:

   python scripts/validate_team.py

3. Start Claude Code from this directory.
4. Ask Claude Code to inspect the team configuration only, report which agents and skills it discovers, and identify version-specific issues. Do not authorize application creation unless you are ready to start a separate project.

## Give the team an idea

When ready to start an application, give Claude Code the idea in plain language—for example, "Build an e-commerce website where customers can browse products, purchase items, and track orders."

The team should then:
1. Have the Product Owner and Business Analyst create the product brief, requirements, user journeys, assumptions, and acceptance criteria.
2. Have the Architect compare suitable technical options and document the recommendation.
3. Have the Project Manager create the prioritized backlog, dependencies, delivery slices, and daily task plan.
4. Have QA prepare test strategy and acceptance coverage while DevOps plans CI/CD and environments.
5. Implement incrementally through bounded agent tasks, isolated branches, PRs, and evidence-backed reviews.
6. Maintain project status and a daily report so you can see what is done, in progress, blocked, awaiting review, and planned next.

You supervise progress and make material decisions when escalated; you do not need to write specifications or assign routine tasks. You retain final PR merge authority. The team does not automatically work while Claude Code is closed unless separate background/scheduling infrastructure is configured.

## Agile delivery and traceability

Use [the project bootstrap workflow](workflows/project-bootstrap.md), [the Agile delivery workflow](workflows/agile-agent-delivery.md), and [the agent traceability guide](docs/agent-traceability.md). Use [GitHub Projects setup](docs/github-projects-setup.md) for the board and [the daily report template](templates/daily-project-report-template.md) for reporting.

GitHub Issues and Projects are the durable tracking layer, but they do not automatically coordinate local Claude Code sessions. The main session and Project Manager must explicitly record delegation outcomes, update statuses, link evidence, and reconcile the daily report.

## Static checks vs runtime verification

The validator checks expected file counts, required files, and basic agent/skill frontmatter. GitHub Actions automates that static check. Neither proves that Claude Code has loaded or can delegate to every agent or skill.

Runtime verification must be performed in an installed Claude Code environment. Record the Claude Code version, observed discovery results, permissions, and limitations in docs/verification-report.md. Never report runtime verification as complete based only on a passing static check.

## Working safely

- Keep this repository focused on reusable team configuration. Start an application in a separate repository after the team establishes the project plan and target.
- Use small, reviewable branches and pull requests.
- Keep credentials and secrets out of prompts, files, logs, and commits.
- Require human approval for production deployment, destructive/irreversible operations, permission changes, and spending.
- Use bounded tasks and concise handovers to manage context and token usage.
- A Claude Pro subscription does not automatically include Anthropic API credits; check current plan and usage terms.

## Repository layout

.claude/
  CLAUDE.md
  agents/
  skills/
docs/
standards/
templates/
workflows/
scripts/validate_team.py
.github/workflows/validate-team.yml

## Contributing

Before proposing a change, run the validator locally and review the diff. Pull requests should explain the motivation, summarize changes, state checks actually run, and disclose any runtime checks not performed.
