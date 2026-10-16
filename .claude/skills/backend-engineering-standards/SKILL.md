---
name: backend-engineering-standards
description: Implement maintainable and secure backend behavior.
---

# Implement maintainable and secure backend behavior

## When to use
Use this skill when the task involves implement maintainable and secure backend behavior.

## Procedure
Keep business rules testable, validate at trust boundaries, authorize every sensitive operation server-side, handle errors consistently, avoid leaking secrets, and test normal and failure paths. Do not assume a framework.

## Quality checks
- Confirm scope, assumptions, and relevant constraints.
- Follow the shared instructions in `.claude/CLAUDE.md` and applicable files under `standards/`.
- Prefer small, reversible changes and preserve traceability to requirements.
- Run appropriate checks when available and report exact observed results; never claim unrun checks passed.
- Identify risks, open questions, and next actions explicitly.
