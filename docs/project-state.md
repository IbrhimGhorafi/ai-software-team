# IA Team Project State and Handover

> Durable session-resume record for the reusable AI Software Team repository. Update this file at session start/end and reconcile every claim against GitHub evidence. Never store secrets or private chain-of-thought here.

## Project identity

- **Project:** IA Team Agile — reusable AI software development team kit
- **Repository:** https://github.com/ibrahim-ai-team/ai-software-team
- **Purpose:** Build and verify a practical, incremental AI software team using Claude Code, repository instructions, agents, skills, commands, GitHub workflows and evidence-based orchestration.
- **Current phase:** SECURITY VERIFICATION → RUNTIME SMOKE TEST → SPRINT/TOKEN CONTROLS
- **Last reconciled:** 2026-10-17 (UTC; timestamp date based on current session; exact clock time not captured)
- **Source-of-truth rule:** Repository/commit/CI evidence for code facts; GitHub Issues for task state; this file for cross-session handover. Chat history is context, not proof.

## Current objective

Finish the security review, then test Claude Code's real runtime discovery and permission behavior in an isolated environment. Only after recording the installed Claude Code version should we define story sizing, task budgets, and model-routing rules.

## Canonical task backlog

| ID | Task | Status | Dependency / next action |
|---|---|---|---|
| IA-00 | [Establish durable project state and session handover](https://github.com/ibrahim-ai-team/ai-software-team/issues/23) | IN_PROGRESS | This state file is being introduced through a feature branch/PR; reconcile after merge. |
| IA-SEC-01 | [Finish security guardrail review and verify GitHub branch protection](https://github.com/ibrahim-ai-team/ai-software-team/issues/24) | READY | Review PR #22; inspect branch settings manually; owner decides merge. |
| IA-RUN-02 | [Run isolated Claude Code discovery, delegation, and permission smoke tests](https://github.com/ibrahim-ai-team/ai-software-team/issues/25) | BLOCKED_ON_INPUT | Need installed runtime version from `claude --version`; use fake data, throwaway clone, local-only remote. |
| IA-BUD-03 | [Define sprint sizing, per-task budgets, and model routing](https://github.com/ibrahim-ai-team/ai-software-team/issues/26) | BLOCKED_BY_IA-RUN-02 | First establish actual supported options for the installed Claude Code version. |

## Security status — evidence and limits

### Confirmed
- PR #21 was merged into `main`; the current `main` commit observed during this work is `3978b87e321a23b5cd7b55a0a3a07e7f88ea7f2a`.
- PR #22: https://github.com/ibrahim-ai-team/ai-software-team/pull/22
- PR #22 is a draft PR adding confirmation rules for both `Edit` and `Write` on sensitive Claude configuration, GitHub workflows, CODEOWNERS, and Dependabot configuration, plus test/validator/documentation updates.
- At observed PR #22 head `adbafd3b8ec2d053e0f4977dac98ae701d42153a`, GitHub Actions reported success for Python 3.10, 3.11, Python 3.12 and the repository secret scan:
  - Workflow checks: https://github.com/ibrahim-ai-team/ai-software-team/actions/runs/39044489711
  - Secret scan: https://github.com/ibrahim-ai-team/ai-software-team/actions/runs/39044489730
- **Recheck CI if PR #22 head SHA changes.** These results are tied to the observed head above, not automatically to future commits.

### Not verified
- Actual Claude Code runtime permission behavior; current tests simulate rule matching.
- Actual discovery of team instructions, agents, skills and commands inside the installed Claude Code runtime.
- A real harmless delegation in the installed runtime.
- Full GitHub branch protection/ruleset configuration. The branch summary reported `main` as protected, but required status-check contexts were not listed in the accessible summary and the full protection endpoint could not be read through the current integration.
- Do not say security is fully complete until the above are either verified or explicitly documented as unavailable.

## Required safe runtime test

1. Ask the user to run `claude --version` in their own environment and provide only the version output. Never request a token or credential.
2. Use an isolated throwaway clone/worktree, fake files only, and a local-only Git remote.
3. Verify that `.claude/CLAUDE.md` is loaded and identify supported ways to inspect agents, skills and commands for that version.
4. Ask Claude Code to perform one harmless delegation, e.g. summarize a fixture file; record observed evidence.
5. Test representative permission cases in isolation: fake-secret reads, protected config edits/writes, a destructive operation limited to a disposable scratch directory, a force-push to a local-only remote, and a safe read-only operation.
6. Record each as PASS / FAIL / NOT RUN, whether denied/prompted/allowed, exact evidence, runtime version, and limitations in `docs/verification-report.md`.
7. Never use real secrets, production systems, real destructive operations or remote pushes for testing.

## Sprint and token controls — do not implement prematurely

After IA-RUN-02:
- Inspect version-specific supported model selection, subagent configuration, permission settings, and available usage/context telemetry.
- Separate hard runtime capabilities from team policy defaults and estimates.
- Define story sizing from scope, uncertainty, dependencies, verification burden and risk.
- Give each task a bounded output, stopping condition, verification budget and checkpoint/handover rule.
- Record actual token/cost/duration only when runtime exposes reliable measurements; otherwise mark them unavailable.
- Use only model IDs/options confirmed for the installed version.
- Keep default WIP low and file ownership non-overlapping; human repository owner alone merges PRs.

## Repository and workflow constraints

- Work through feature branches and pull requests; do not commit directly to `main`.
- Human repository owner performs all merges.
- Never claim a task ran, check passed, PR merged, or runtime feature discovered without observable evidence.
- Static validation is not runtime proof.
- On every new coordinator/chat session: read this file, the orchestration contract, relevant task issues, open PRs, current CI and the verification report; reconcile before resuming.
- Before ending a session, update task statuses, evidence, blockers and the next 1–3 actions.

## Copy/paste prompt for a new ChatGPT conversation

Continue the IA Team Agile project in https://github.com/ibrahim-ai-team/ai-software-team. First read and reconcile `docs/project-state.md`, `workflows/orchestration-contract.md`, Issues #23–#26, PR #22 and current CI. Do not rely on prior chat memory. Do not repeat completed work without evidence. Current order: (1) review security PR #22 and verify GitHub branch protection separately; (2) run isolated Claude Code runtime discovery/delegation/permission smoke tests after asking me for the output of `claude --version`; (3) define sprint sizing, task budgets and model routing only after checking the options supported by my installed version. Use feature branches and PRs; never merge for me. Keep status claims evidence-based and update this file and the issues before handover.
