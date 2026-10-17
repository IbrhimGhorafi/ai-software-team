---
description: Save a resumable project handover with evidence and next actions
---

# Handover

Update the project's durable state/handover file with UTC timestamp, current phase, goal/scope, last known commit and branch, approved decisions/ADRs, assumptions, task IDs/status/owners/dependencies, delegation IDs, PRs, test/CI evidence, blockers, sponsor decisions, and next actions.

Separate verified repository/CI evidence from agent-reported progress. Include exact commands and results for checks actually run. Never include secrets, tokens, private chain-of-thought, or credentials. If remote state could not be updated, record that limitation explicitly.