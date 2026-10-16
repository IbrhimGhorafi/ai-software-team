# AI Software Team

A reusable, project-independent starter kit for coordinating AI-assisted software delivery with Claude Code. It contains agent definitions, skills, engineering standards, templates, and workflows—not an application.

## What is included

| Area | Contents |
|---|---|
| Agents | 12 focused roles under `.claude/agents/` |
| Skills | 18 reusable procedures under `.claude/skills/<skill-name>/SKILL.md` |
| Shared instructions | `.claude/CLAUDE.md` |
| Standards | Engineering, security, Git workflow, and definition of done |
| Templates | Requirements, stories, sprint plans, architecture decisions, test plans, code reviews, and handovers |
| Workflow and docs | Future-project workflow, two-week Agile agent delivery, GitHub Projects setup, capabilities, and verification notes |
| Validation | A dependency-free Python static validator and GitHub Actions workflow |

## Prerequisites

- Python 3.10+ to run the static validator (standard library only).
- Claude Code installed and authenticated to verify actual agent/skill discovery. Follow the current official [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview).
- GitHub is optional for local use; GitHub Actions runs the static checks when changes are pushed or a pull request is opened.

## Quick start

1. Clone or download this repository.
2. From the repository root, run:

   ```bash
   python scripts/validate_team.py
   ```

3. Start Claude Code from this directory.
4. Ask Claude Code to inspect the team configuration only, report which agents and skills it discovers, and identify version-specific issues. Do not authorize application creation unless you are ready to start a separate project.

## Agile workflow for future projects

For implementation projects, use [the Agile agent delivery workflow](workflows/agile-agent-delivery.md) and [GitHub Projects setup guide](docs/github-projects-setup.md). The default sprint is two weeks. Track backlog and sprint work in GitHub Issues/Projects, execute Claude Code agents locally on isolated branches/worktrees, and require an AI Tech Lead review before the repository owner performs the final merge. Use the [technical proposal template](templates/technical-proposal-template.md) for framework/architecture ideas and the [pull request template](templates/pull-request-template.md) to report validation evidence. GitHub Projects does not coordinate local agents by itself; parallel task claiming requires a local coordinator or an explicit claim protocol.

## Important distinction: static checks vs runtime verification

The validator checks expected file counts, required files, and basic agent/skill frontmatter. GitHub Actions automates that static check. Neither proves that Claude Code has loaded or can delegate to every agent or skill.

Runtime verification must be performed in an installed Claude Code environment. Record the Claude Code version, observed discovery results, permissions, and any limitations in `docs/verification-report.md`. Never report runtime verification as complete based only on a passing static check.

## Working safely

- Keep this repository focused on reusable team configuration. Start an application in a separate repository after requirements and constraints are agreed.
- Use small, reviewable branches and pull requests.
- Keep credentials and secrets out of prompts, files, logs, and commits.
- Require human approval for production deployment, destructive or irreversible operations, permission changes, and spending.
- Use bounded tasks and concise handovers to manage context and token usage.
- A Claude Pro subscription does not automatically include Anthropic API credits; check the current plan and usage terms.

## Repository layout

```text
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
```

## Contributing

Before proposing a change, run the validator locally and review the diff. Pull requests should explain the motivation, summarize changes, state checks actually run, and disclose any runtime checks not performed.
