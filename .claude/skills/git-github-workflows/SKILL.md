---
name: git-github-workflows
description: Make safe and reviewable Git changes.
---

# Make safe and reviewable Git changes

## When to use
Use this skill when the task involves make safe and reviewable git changes.

## Procedure
Inspect status and diffs before changes. Use focused branches and descriptive commits, avoid committing secrets, never rewrite shared history without approval, and report checks skipped. Push only when explicitly authorized.

## Quality checks
- Confirm scope, assumptions, and relevant constraints.
- Follow the shared instructions in `.claude/CLAUDE.md` and applicable files under `standards/`.
- Prefer small, reversible changes and preserve traceability to requirements.
- Run appropriate checks when available and report exact observed results; never claim unrun checks passed.
- Identify risks, open questions, and next actions explicitly.
