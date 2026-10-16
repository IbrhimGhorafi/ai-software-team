---
name: database-modelling-migrations
description: Model data and evolve schemas safely.
---

# Model data and evolve schemas safely

## When to use
Use this skill when the task involves model data and evolve schemas safely.

## Procedure
Define entities, relationships, constraints, indexes, and retention needs from requirements. Make migrations repeatable and safe; consider locks, data volume, backfills, rollback, and compatibility with deployed code.

## Quality checks
- Confirm scope, assumptions, and relevant constraints.
- Follow the shared instructions in `.claude/CLAUDE.md` and applicable files under `standards/`.
- Prefer small, reversible changes and preserve traceability to requirements.
- Run appropriate checks when available and report exact observed results; never claim unrun checks passed.
- Identify risks, open questions, and next actions explicitly.
