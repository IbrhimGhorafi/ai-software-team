---
name: code-review-refactoring
description: Review diffs and refactor safely.
---

# Review diffs and refactor safely

## When to use
Use this skill when the task involves review diffs and refactor safely.

## Procedure
Review actual changes for correctness, readability, coupling, duplication, testability, and regressions. Report evidence-based findings with severity and file/line. Refactor in small steps and rerun relevant checks.

## Quality checks
- Confirm scope, assumptions, and relevant constraints.
- Follow the shared instructions in `.claude/CLAUDE.md` and applicable files under `standards/`.
- Prefer small, reversible changes and preserve traceability to requirements.
- Run appropriate checks when available and report exact observed results; never claim unrun checks passed.
- Identify risks, open questions, and next actions explicitly.
