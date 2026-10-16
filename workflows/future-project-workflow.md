# Future Project Workflow

## Gate 0 — Explicit activation
This repository configures the reusable team only. Do not start an application, create product code, or select a technology stack until the user explicitly approves a real project brief.

For a new application idea, follow `workflows/project-bootstrap.md` before repository creation or implementation. That workflow owns the detailed gates for discovery, architecture/repository planning, explicit human approval, repository setup, and first sprint authorization.

## Gate 1 — Discovery
Business Analyst and Product Owner clarify users, problem, goals, scope, constraints, risks, acceptance outcomes, and open questions. Record assumptions separately from confirmed facts.

## Gate 2 — Plan
Project Manager proposes small sprint-sized increments, dependencies, ownership, and verification criteria. Human owner approves priorities and scope.

## Gate 3 — Architecture and implementation
Architect compares viable options against confirmed requirements. Record material decisions as ADRs. Backend, frontend, database, and DevOps work only within approved slices; avoid framework assumptions. Do not assume microservices or multiple repositories without a documented need and approved repository plan.

## Gate 4 — Verification
QA defines risk-based test strategy and traceability. Developers run relevant checks. Code Reviewer independently reviews diffs and security risks. Never report checks as passed unless actually run.

## Gate 5 — Review and handover
Summarize completed work, evidence, risks, deviations, and next steps. Human approval is required for production deployment, irreversible actions, permission changes, and spending. The human owner performs final PR merges.

## Token and context management
- Work in bounded increments and prioritize high-risk unknowns.
- Reuse skills/templates instead of repeating long instructions.
- Delegate only independent tasks with explicit outputs and file ownership.
- Keep durable decisions in files and use concise handovers.
- Stop at a gate when required information or approval is missing.
