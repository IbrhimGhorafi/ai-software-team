---
description: Review a pull request for correctness, security, and evidence
---

# Review PR

1. Inspect the actual diff, target branch, linked story/requirements, and changed-file scope.
2. Check correctness, edge cases, security/privacy, secrets, permissions, backwards compatibility, maintainability, and test adequacy.
3. Run available relevant checks; separate checks that ran from checks not available or not run.
4. Report findings first, ordered by severity, with file/line references and concrete remediation.
5. Verify acceptance criteria and Definition of Done against observable evidence.
6. Do not merge the PR, change branch protections, or claim CI is green without observing the result.