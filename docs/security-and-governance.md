# Repository security and governance checklist

This starter kit defines instructions and configuration; it is not a security sandbox. Tool allowlists reduce exposure but do not make a broad tool such as `Bash` safe by themselves. Verify the effective permissions in the installed Claude Code version and keep human review for privileged changes.

## Required repository settings

Configure these settings in GitHub **Settings → Rules → Rulesets** (or branch protection, where rulesets are unavailable) for `main`:

- Require a pull request before merging.
- Require at least one approval if the repository has another eligible reviewer; otherwise document the solo-maintainer exception and keep CI required.
- Require the `Static configuration checks (Python 3.10)`, `Static configuration checks (Python 3.11)`, `Static configuration checks (Python 3.12)`, and secret-scan workflow checks. Use the exact check names shown on a real pull request.
- Require branches to be up to date before merging when practical.
- Block force pushes and branch deletion.
- Do not allow routine direct pushes to `main`; tightly limit any bypass list.
- Review ruleset bypass actors and GitHub Actions permissions periodically.

A workflow file cannot enable branch protection by itself. Verify the active ruleset in repository settings after configuring it; do not infer enforcement from this document or a green CI run.

## Agent and command permissions

- Give each agent only the tools it needs; keep security review read-only.
- Treat `Bash` as a high-impact capability. Use command restrictions/permission prompts supported by the deployed Claude Code version, and inspect the effective settings.
- Do not place credentials in prompts, tracked files, issue bodies, logs, or test fixtures.
- Treat hooks and text-based secret scanners as defense in depth, not a substitute for secret management or provider-side secret scanning.
- Require human review before merging and before running deployment, destructive, or credential-sensitive commands.

## Secret scanning

Use GitHub secret scanning / push protection when available for the repository plan. This repository includes `.github/workflows/secret-scan.yml`, which runs Gitleaks on pushes to `main`, pull requests, and manual dispatch. The workflow pins third-party actions to full commit SHAs and checks out full history. Inspect its actual CI result after each change; a workflow file alone is not evidence that a scan passed. Any custom regex scanner is heuristic and must fail closed when it cannot inspect the repository.

## License

No license is added by this change because choosing a license changes the legal permissions granted to users. The repository owner should explicitly choose one (for example, MIT, Apache-2.0, or another suitable license) before publishing reusable code under a declared license.

## Verification boundaries

CI covers static repository validation and regression tests only. It does not prove Claude Code runtime discovery/delegation, operating-system sandboxing, GitHub ruleset enforcement, or application behavior. Record actual smoke-test evidence separately in `docs/verification-report.md`.
