---
name: architecture-evaluation-adr
description: Evaluate architecture choices and record decisions.
---

# Evaluate architecture choices and record decisions

## When to use
Use this skill when the task involves evaluate architecture choices and record decisions.

## Procedure
Start from requirements and quality attributes. Compare viable options against constraints, costs, security, operability, and reversibility. Record context, alternatives, decision, consequences, and evidence in an ADR.

## Quality checks
- Confirm scope, assumptions, and relevant constraints.
- Follow the shared instructions in `.claude/CLAUDE.md` and applicable files under `standards/`.
- Prefer small, reversible changes and preserve traceability to requirements.
- Run appropriate checks when available and report exact observed results; never claim unrun checks passed.
- Identify risks, open questions, and next actions explicitly.
