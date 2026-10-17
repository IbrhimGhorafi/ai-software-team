---
description: Check release readiness, evidence, risks, and required human approvals
---

# Release readiness check

Evaluate whether the requested release is ready for human approval. This command does not deploy or release software.

## Procedure
1. Identify the release scope, target environment, and required approvals.
2. Verify linked pull requests, required CI checks, test results, and known defects.
3. Review configuration, migrations, secrets handling, observability, backup/rollback plan, and release notes where applicable.
4. Record each check as PASS, FAIL, BLOCKED, or NOT APPLICABLE with evidence.
5. List blockers and decisions required from the owner.
6. Use templates/release-readiness-template.md for the report.

Never infer a green CI run from configuration alone. Do not deploy, tag, publish, or merge as part of this check.
