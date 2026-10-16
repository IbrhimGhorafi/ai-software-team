# Project Bootstrap Workflow

## Purpose and scope

Use this workflow when the human owner presents a new software idea and asks the team to prepare it for delivery. It prepares a proposal and, after explicit approval, initializes the agreed project repositories. It does not authorize application implementation by itself.

This workflow applies to future application projects, not changes to this reusable AI team starter kit.

## Non-negotiable gates

- **Gate 0 — Activation:** Confirm the user wants to start a real project. If they are only brainstorming or improving this starter kit, do not create application repositories or code.
- **Gate 1 — Discovery:** Clarify the problem, users, outcomes, in-scope and out-of-scope features, constraints, budget, hosting, security/privacy needs, integrations, and acceptance criteria. Mark assumptions and open questions clearly.
- **Gate 2 — Technical options:** The Software Architect leads a comparison of viable system shapes: monorepo vs multi-repo, modular monolith vs microservices, and relevant technology options. Do not assume microservices or a framework by default.
- **Gate 3 — Proposal:** Prepare a project brief, architecture proposal, repository topology plan, initial delivery slices, risks, and estimated operating/tooling costs. Include a reasonable simpler alternative and explain trade-offs.
- **Gate 4 — Human approval:** Stop and ask the human owner to approve the project scope, architecture direction, repository plan, initial stack, budget/costs, and whether remote repositories may be created. Silence is not approval.
- **Gate 5 — Repository setup:** Only after approval, the DevOps/Repository Setup responsibility may create the approved repositories and scaffolding, provided the available GitHub credentials and permissions support the action. Otherwise provide exact manual steps and continue only within authorized local scope.
- **Gate 6 — Bootstrap verification:** Verify repository names, default branch, initial structure, README/setup instructions, license choice if requested, security settings requested by the owner, CI baseline, and links between repositories. Report checks actually performed and any settings that could not be verified.
- **Gate 7 — Sprint planning:** The Project Manager turns approved requirements into prioritized issues, dependencies, acceptance checks, and a proposed two-week sprint. The human owner approves the sprint goal and scope before implementation begins.
- **Gate 8 — Implementation authorization:** Developer agents start only on approved, Ready issues. Follow `workflows/agile-agent-delivery.md`; use isolated branches/worktrees and PRs. The human owner performs every final merge.

## Role ownership

- **Product Owner / Business Analyst:** clarify user value, requirements, boundaries, acceptance criteria, and unresolved product decisions.
- **Software Architect:** compare architecture and repository options; define service boundaries, API contracts, key quality attributes, and proposed ADRs.
- **Project Manager:** sequence work, identify dependencies/risks, and prepare a sprint proposal; do not silently commit the owner to scope.
- **DevOps / Repository Setup:** translate the approved repository plan into repository scaffolding, CI, developer setup, and operational baseline. Do not create unapproved remote resources or incur costs.
- **Backend / Frontend / Database agents:** advise on feasibility during planning when requested; do not start product implementation before the implementation gate.
- **QA Automation:** prepare risk-based test strategy and acceptance verification early; do not report tests as run until evidence exists.
- **Code Review / Security:** assess design and changes against quality and security requirements.
- **Human owner:** approves material decisions, remote repository creation, scope, costs, sprint commitment, security/permission changes, production deployment, and final merges.

The repository setup responsibility may remain part of the existing DevOps agent; a separate agent is not required unless actual workload or orchestration complexity justifies it.

## Repository topology decision checklist

Before recommending one or multiple repositories, evaluate:

- independent release/deployment needs;
- service ownership and team boundaries;
- shared code and versioning strategy;
- local development and integration-test complexity;
- CI/CD duplication and maintenance;
- permissions, secrets, and access boundaries;
- deployment/runtime costs and observability;
- expected scale and operational maturity.

Default to the simplest architecture that meets confirmed requirements. Microservices require a concrete justification and an explicit description of service boundaries, communication, data ownership, observability, failure handling, local development, and testing.

## Required deliverables before approval

1. Project brief and requirements summary.
2. Confirmed facts, assumptions, open questions, and out-of-scope items.
3. Architecture options comparison with recommendation and trade-offs.
4. Proposed repository plan using `templates/repository-plan-template.md`.
5. Proposed technology stack with alternatives and source-backed rationale where research is needed.
6. Security/privacy risks, operational requirements, cost assumptions, and major dependencies.
7. Initial delivery slices and proposed first sprint goal.
8. Explicit list of decisions requiring human approval.

Do not create a remote repository plan that assumes the user has approved a GitHub organization, visibility, licensing, paid services, cloud resources, or access permissions.

## Repository setup execution checklist

After approval, the setup owner must:

1. Reconfirm the approved plan and target owner/organization.
2. Check whether each repository already exists to avoid accidental duplicates.
3. Create only the approved repositories and use the approved visibility.
4. Use the agreed default branch and baseline files.
5. Add only approved collaborators, permissions, integrations, and secrets references; never print or commit secret values.
6. Add baseline CI/static checks and setup documentation appropriate to the selected stack.
7. Keep implementation work on feature branches and open PRs for code/configuration changes where supported.
8. Record exact repository URLs, initial commit/branch, setup steps, checks run, limitations, and manual actions needed.
9. Stop if permissions, visibility, costs, or an irreversible choice differs from the approved plan.

## Failure and pause rules

Pause and ask the human owner if requirements materially conflict, an architecture choice changes cost or risk, a repository is unexpectedly present, required permissions are unavailable, credentials are missing, or the proposed setup exceeds approved scope. Never work around missing permissions by weakening security.

## Completion definition

Bootstrap is complete only when the approved repository structure exists (or the remaining manual steps are clearly documented), setup instructions are available, the agreed baseline checks have actual recorded results, and the owner has received the repository links, risks, and next decision. It does not mean the application itself is implemented.
