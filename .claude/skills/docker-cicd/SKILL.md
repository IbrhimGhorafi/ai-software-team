---
name: docker-cicd
description: Build repeatable container and CI workflows.
---

# Build repeatable container and CI workflows

## When to use
Use this skill when the task involves build repeatable container and ci workflows.

## Procedure
Use reproducible builds, minimal base images, non-root execution, pinned or controlled dependencies, health checks, caching where safe, and least-privilege CI permissions. Never expose secrets in logs or images.

## Quality checks
- Confirm scope, assumptions, and relevant constraints.
- Follow the shared instructions in `.claude/CLAUDE.md` and applicable files under `standards/`.
- Prefer small, reversible changes and preserve traceability to requirements.
- Run appropriate checks when available and report exact observed results; never claim unrun checks passed.
- Identify risks, open questions, and next actions explicitly.
