# Agent Capabilities and Runtime Caveats

This kit defines 12 Claude Code subagent profiles. Their presence as Markdown files does not prove runtime discovery or guarantee that all agents can be spawned in parallel. Actual capabilities depend on installed Claude Code version, settings, permissions, and available tools.

The `description` frontmatter is intended to help routing. Agent definitions intentionally do not hard-code a project stack. Skills are shared procedural references and do not grant permissions by themselves.

Use the fewest agents needed for each task. The coordinator should not delegate merely to simulate activity.
