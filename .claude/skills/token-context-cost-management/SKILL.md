---
name: token-context-cost-management
description: Use when bounding agent delegation, context usage, or execution cost.
---

# Manage context and usage efficiently

## When to use
Use this skill before multi-agent tasks, long sessions, large research jobs, or work with token/time/cost constraints.


## Procedure
Break work into bounded tasks, load only relevant files, reuse existing skills and templates, summarize durable decisions, and hand off concise context. Avoid redundant agent calls and stop to ask when missing information changes the result.

## Expected outputs
- Bounded task plan with expected deliverables and stopping condition
- Minimal context/file loading plan and checkpoint/handover strategy
- Observed token/cost/duration data if exposed; otherwise mark unavailable

## Quality checks
- Set explicit delegation/WIP limits and avoid duplicate agent calls.
- Do not invent token counts, model prices, or usage telemetry.
- Stop starting new work when budget pressure threatens verification or handover.
