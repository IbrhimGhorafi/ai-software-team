# Agile delivery workflow for Claude Code agents

## Operating model

- GitHub Issues are the durable record for backlog items, acceptance criteria, decisions, blockers, and links to code.
- GitHub Projects is the planning board for the two-week sprint. Keep status, priority, sprint iteration, estimate, and owner visible.
- Claude Code runs specialist agents locally against a checked-out repository. Agents do not have a shared filesystem merely because they share a GitHub project.
- Every implementation task uses an isolated branch. Use a separate Git worktree per concurrently running coding agent where practical.
- The AI Tech Lead reviews the actual diff and may submit an APPROVE or REQUEST_CHANGES review only after evaluating evidence.
- The repository owner/user is the only person who performs the final merge. Agents must never merge PRs or configure automation to merge on the user's behalf.

## Issue lifecycle

Use these statuses (adapt GitHub Projects options if necessary):

1. **Backlog** — captured, not committed to a sprint.
2. **Ready** — clear acceptance criteria, test expectations, and dependencies identified.
3. **In Progress** — one developer agent has claimed the task and is working in its own branch/worktree.
4. **In Review** — a PR is open, linked to the issue, and the developer has supplied test evidence.
5. **Changes Requested** — the Tech Lead found specific issues that need fixing.
6. **Approved — Awaiting Human Merge** — Tech Lead approved the current PR revision and required checks pass.
7. **Done** — the user merged the PR and the issue was verified/closed.
8. **Blocked** — record the blocker, impact, attempted resolution, and decision/dependency needed.

Never mark an issue Done merely because a local implementation or approval exists. Never leave a blocked task silently In Progress.

## Two-week sprint cadence

### Before sprint start
- Business Analyst clarifies the outcome, users, constraints, and acceptance criteria.
- Project Manager splits work into reviewable issues and identifies dependencies and risks.
- Tech Lead checks feasibility, boundaries, sequencing, and task size.
- The human owner approves the sprint goal and scope. Do not silently start a new sprint or add major scope.
- Split oversized stories into tasks that can be reviewed independently.

### During the sprint
- Agents claim only Ready tasks and check for existing ownership before starting.
- Limit work in progress; finish/review existing work before claiming more when practical.
- Each task has one primary implementation owner. Specialist agents can advise, but avoid multiple agents editing the same files.
- If criteria are ambiguous, dependencies are missing, or scope must change, stop and ask rather than inventing product decisions.
- Post concise progress and blockers to the GitHub issue. Update status when work moves stages.
- New ideas go to the backlog as proposals; they do not automatically enter the active sprint.

### Sprint end
- Review merged and unmerged work against the sprint goal.
- Keep incomplete work open and return it to the backlog or plan it explicitly for the next sprint.
- Record outcomes, blockers, follow-up issues, and a short retrospective.
- Never call work complete when checks were not run or the user has not merged the PR.

## Task claiming and local execution

Before coding, the developer agent must:
1. Read the issue, acceptance criteria, linked decisions, repo instructions, and relevant implementation.
2. Confirm the issue is Ready, dependencies are met, and no other agent owns the implementation.
3. State a short plan and expected files/checks.
4. Create a branch named feat/<issue-number>-<short-name>, fix/<issue-number>-<short-name>, or chore/<issue-number>-<short-name>.
5. If another agent is using the same checkout, use a separate worktree or wait. Never concurrently edit the same working tree.
6. Make the smallest coherent change; do not refactor unrelated code.
7. Run relevant tests, lint, type checks, and static validation available locally. Report exact commands and results; never fabricate checks.
8. Commit and push the branch, then open a PR linked to the issue. If a required check cannot run, disclose why and mark it as not run.

Example worktree pattern (adapt paths and branch to the actual issue):
    git fetch origin
    git worktree add ../work-issue-123 -b feat/123-short-name origin/main
    cd ../work-issue-123

A GitHub issue is not automatically assigned to an AI agent by GitHub itself. Task claiming is a coordination protocol implemented by the orchestrator and issue/status updates; use a lock/claim mechanism if parallel orchestration is added.

## Pull request readiness checklist

The developer may move a task to In Review only when:
- [ ] PR title is clear and issue is linked.
- [ ] Scope matches the approved issue; unrelated changes are excluded.
- [ ] Acceptance criteria are mapped to implementation and evidence.
- [ ] Relevant tests were added/updated and actual test commands/results are reported.
- [ ] Relevant lint/build/type checks were run or explicitly marked not run with reason.
- [ ] Security, secrets, permissions, data handling, and error handling were considered.
- [ ] Documentation/configuration/migration changes are included when needed.
- [ ] Known limitations, risks, and follow-up work are stated.
- [ ] No secrets, credentials, or generated clutter are included.
- [ ] PR has not been merged.

## AI Tech Lead review protocol

The Tech Lead must review the current PR diff, not merely the developer summary. Verify correctness, acceptance criteria, architecture, test quality, security/privacy, dependency changes, maintainability, CI status, evidence, and unresolved review threads.

If changes are needed, submit REQUEST_CHANGES with actionable findings, severity, affected file/line when available, and expected resolution. Do not approve a PR with unresolved blocking defects or failing required checks.

If the current revision is acceptable, submit APPROVE with a concise evidence-based review. Then set the project status to **Approved — Awaiting Human Merge** if the integration supports it. Approval is not a merge command or authorization to merge. The user reviews the PR and performs the merge manually.

If the GitHub account/token used by an agent cannot create formal reviews, post a clearly labelled review report/comment and do not claim GitHub recorded a formal approval. Never impersonate the human repository owner.

## Framework and architecture improvement proposals

Any agent may propose a framework, tool, architecture, or workflow improvement. Proposals are backlog items, not permission to change shared standards.

A proposal must explain:
- current problem and concrete evidence;
- expected benefit and how it will be measured;
- proposed change and a reasonable alternative, including doing nothing;
- compatibility, security, maintenance, migration, cost/token, and rollback risks;
- affected agents, skills, templates, standards, applications, and CI;
- proof-of-concept scope and success/failure criteria.

The Tech Lead evaluates the proposal and recommends accept, reject, or request-more-evidence. Record accepted consequential decisions as an Architecture Decision Record (ADR). The human owner approves major architecture changes, new paid services/spending, security/permission changes, and irreversible actions. Only then may implementation tickets be added to a sprint.

## Automation boundaries

Safe candidates for automation: linting and static validation, status/label updates based on explicit events, sprint summaries, and notifications that a PR is ready for review.

Human-controlled actions: final merge, production deployment, destructive or irreversible operations, granting permissions or exposing secrets, spending money/enabling paid services, and high-impact architectural changes.

A green CI check is evidence for review, not a substitute for review. A Tech Lead approval is a recommendation to the human owner, not a merge trigger.
