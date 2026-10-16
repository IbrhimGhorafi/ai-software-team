# AI Software Team Audit

- Audit date: 2026-10-16
- Scope: repository files on `main` after the Agile workflow PR was merged, based on remotely readable GitHub contents.
- Important limitation: this is a repository/configuration audit. It is not proof of Claude Code runtime discovery, local delegation, or actual task execution.

## Executive summary

The starter kit has a useful foundation: 12 agent profile files, 18 skill files, shared instructions, reusable templates, a future-project workflow, an Agile delivery workflow, a static validator, and a GitHub Actions workflow.

The main gap identified for the requested use case was that project discovery and architecture planning were described, but the handoff from an approved idea to an explicit repository topology plan and gated repository creation was not sufficiently operationalized. The existing DevOps role can own repository setup without introducing a new agent immediately.

## Findings

| Area | Evidence in repository | Assessment |
|---|---|---|
| Agent/skill inventory | `.claude/agents/` and `.claude/skills/`; README and capability note report 12 agents and 18 skills | Present as files; runtime discovery still unverified |
| Project activation gate | `workflows/future-project-workflow.md`, `.claude/CLAUDE.md` | Present; keep separate from team-kit maintenance |
| Requirements and architecture | Business Analyst, Product Owner, Software Architect profiles; ADR and requirements templates | Present; proposal-to-repository setup handoff needed more detail |
| Agile execution | `workflows/agile-agent-delivery.md`, GitHub Projects setup guide | Documented; no evidence in these files that a real board or local orchestrator has been configured |
| Task claiming and parallelism | Agile workflow documents claim protocol and worktree isolation | Protocol is documented; no local coordinator/lock implementation is evidenced by documentation alone |
| Repository creation responsibility | DevOps profile covers CI/CD, containers, infrastructure and operational workflows | Repository scaffolding responsibility was not explicit enough; clarified in this change |
| Bootstrap approval | Existing workflow requires human scope approval and approval for costs/irreversible actions | Added explicit gates for topology, remote repo creation, visibility, baseline setup and sprint start |
| Static validation | `scripts/validate_team.py`, `.github/workflows/validate-team.yml` | Static checks are available; they do not validate runtime behavior |
| Runtime verification | `docs/verification-report.md` is a blank template | Not yet verified; requires running Claude Code in an installed local environment |
| Merge safety | Shared instructions and Agile workflow reserve final merge for the human owner | Policy documented; repository rulesets/branch protection and permissions were not verified in this audit |

## Changes in this audit PR

- Added `workflows/project-bootstrap.md` to define explicit gates from idea discovery through repository setup and sprint authorization.
- Added `templates/repository-plan-template.md` for architecture options, repository topology, stack trade-offs, security/costs and approval recording.
- Clarified the DevOps agent's repository setup responsibilities and its approval/permission boundaries.
- Linked the bootstrap workflow from the future-project workflow and README.
- Added a report separating file-level evidence from unverified runtime and repository settings.

## Verification status

- Remote GitHub file contents and repository tree were inspected.
- GitHub Actions history was inspected for visible workflow-run evidence; results must be interpreted against the relevant commit/PR rather than treated as proof of Claude runtime behavior.
- The Python validator was **not run in a local checkout as part of this audit**.
- Claude Code agent/skill discovery and real delegation were **not run or verified**.
- GitHub Project board configuration, branch protection/rulesets, and actual permissions preventing direct pushes or merges were **not verified**.
- Repository creation against a future project was **not attempted**; no application repositories were created by this audit.

## Recommended next manual verification

1. Clone the merged repository and run `python scripts/validate_team.py`.
2. Open Claude Code at the repository root and ask it to list the agents and skills it actually discovers, with version and any warnings recorded in `docs/verification-report.md`.
3. Ask Claude Code to perform a harmless, bounded test delegation that reads files only; record observable evidence and permission constraints.
4. Confirm GitHub Project fields/views are configured if you intend to use them for a real project.
5. Review branch protection/rulesets and repository permissions manually; do not infer them from written policy.
6. Exercise the project bootstrap workflow on a sample idea in planning-only mode first. Do not create remote repositories until the plan is explicitly approved.
