# Agent Activity Event Template

Use one compact record per meaningful state change. Store in the linked issue, project-local activity log, or session handover.

```yaml
event_id: "<project-task-delegation-sequence>"
observed_at: "<timestamp only if actually observed>"
task_id: "<issue or local task id>"
delegation_id: "<stable delegation id, if applicable>"
actor_role: "<coordinator or agent role>"
event: "<delegation_started | delegation_returned | output_accepted | changes_requested | blocked | unblocked | pr_opened | review_completed | check_completed | human_decision_requested | human_decision_received | merge_observed | deployment_observed>"
status_before: "<known prior state or unknown>"
status_after: "<new observed state>"
summary: "<short factual description>"
evidence:
  - "<commit, PR, issue, CI run, test output, or artifact URL/path>"
next_action: "<action or none>"
owner: "<role or person responsible>"
```

## Rules

- Log meaningful transitions, not every tool call or internal thought.
- Use a timestamp only when it is actually available; never invent one.
- Link evidence where possible. If evidence is absent, say so.
- Do not put credentials, secrets, full transcripts, or private chain-of-thought in the log.
- Mark an event unknown or unverified if the coordinator did not observe it.
