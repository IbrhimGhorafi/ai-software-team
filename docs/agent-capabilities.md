# Agent Capabilities and Runtime Caveats

This kit defines 12 Claude Code subagent profiles. Their presence as Markdown files does not prove runtime discovery or guarantee that all agents can be spawned in parallel. Actual capabilities depend on installed Claude Code version, settings, permissions, and available tools.

The `description` frontmatter is intended to help routing. Agent definitions intentionally do not hard-code a project stack. Skills are shared procedural references and do not grant permissions by themselves.

Use the fewest agents needed for each task. The coordinator should not delegate merely to simulate activity.

## Tool allowlists (least privilege)

Each agent declares an explicit `tools:` allowlist in its frontmatter; the static validator requires it. Allowlists are a starting point and should be tightened per project.

| Agent | Tools | Rationale |
|---|---|---|
| backend-developer, frontend-developer, database-engineer, devops-platform, qa-automation | Read, Grep, Glob, Edit, Write, Bash | Implement and run checks |
| project-manager | Read, Grep, Glob, Edit, Write, Bash | Plans/reports; Bash for `gh` issue/PR queries |
| product-owner, business-analyst, software-architect, documentation-manager | Read, Grep, Glob, Edit, Write | Documents only; no shell |
| code-review-security | Read, Grep, Glob | Read-only review; no shell or file-writing tools |
| technical-research | Read, Grep, Glob, Write, WebSearch, WebFetch | Web research, writes notes only |

Unverified at runtime: tool names and enforcement depend on the installed Claude Code version. Confirm in a real session and record results in `docs/verification-report.md`.
