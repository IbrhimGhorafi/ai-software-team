# Orchestration Design

See `workflows/future-project-workflow.md`. Use Project Manager as coordinator only after the user approves a real project. Use Product Owner for priority/value decisions; Architect for technical decisions; human owner for material business, budget, security-risk acceptance, and release decisions.

Recommended lightweight task record:
- ID, title, owner, status, priority, dependency IDs
- Input artifacts and output path
- Acceptance checks and evidence
- Risks/blockers and next action

Keep project-independent standards under `standards/` and shared agent/skill definitions under `.claude/`. Put future product artifacts in a separate project repository or a clearly separated project-specific directory.
