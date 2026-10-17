# GitHub `main` Branch Protection Checklist

Repository files cannot enforce branch protection by themselves. A repository owner must configure these controls in GitHub Settings and verify the resulting behavior.

1. Open **Settings → Rules → Rulesets** (or the branch protection rules page, depending on the GitHub UI).
2. Create a ruleset targeting the default branch `main` and enable it.
3. Require a pull request before merging. Require at least one human approval if collaborators are available; otherwise document the owner-only review policy and understand the limitation.
4. Require the status checks from both workflows: `Static configuration checks (Python 3.10)`, `Static configuration checks (Python 3.11)`, `Static configuration checks (Python 3.12)`, and the Gitleaks job check name as displayed by GitHub.
5. Block force pushes and branch deletion.
6. Restrict bypass actors to the smallest possible set. Do not grant AI tokens bypass privileges.
7. Consider requiring conversation resolution and signed commits if they fit the project workflow.
8. Save the ruleset and verify it is active. Open a test PR, confirm required checks are enforced, and confirm direct pushes to `main` are rejected for ordinary actors.
9. Enable Secret Scanning and Push Protection under **Settings → Security** if available.

GitHub UI labels and check-run names may vary. Use the exact names displayed by the checks on a real PR. Do not mark this checklist complete until enforcement has been tested.
