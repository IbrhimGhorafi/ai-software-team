#!/usr/bin/env python3
"""Static validator for the reusable Claude Code AI team starter kit.

Checks expected agent and skill counts, required files, and basic frontmatter.
Does not start Claude Code, create an application, or execute application tests.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_AGENTS = 12
EXPECTED_SKILLS = 18
errors = []
agents = sorted((ROOT / ".claude" / "agents").glob("*.md"))
skills = sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md"))
if len(agents) != EXPECTED_AGENTS:
    errors.append(f"Expected {EXPECTED_AGENTS} agent files, found {len(agents)}")
if len(skills) != EXPECTED_SKILLS:
    errors.append(f"Expected {EXPECTED_SKILLS} skill files, found {len(skills)}")
for p in agents + skills:
    text = p.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"Missing or malformed frontmatter: {p.relative_to(ROOT)}")
    elif "name:" not in text.split("\n---\n", 1)[0]:
        errors.append(f"Missing name in frontmatter: {p.relative_to(ROOT)}")
required = [
    "README.md", ".claude/CLAUDE.md", "workflows/future-project-workflow.md",
    "standards/engineering-principles.md", "standards/security-principles.md",
    "standards/git-workflow.md", "standards/definition-of-done.md",
    "templates/requirements-template.md", "templates/user-story-template.md",
    "templates/architecture-decision-template.md", "templates/sprint-plan-template.md",
    "templates/test-plan-template.md", "templates/code-review-template.md",
    "templates/session-handover-template.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")
print(f"Agents: {len(agents)}/{EXPECTED_AGENTS}")
print(f"Skills: {len(skills)}/{EXPECTED_SKILLS}")
print("Required templates and standards: checked")
print("Static-only validation: no Claude runtime, application, or tests invoked")
if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("PASS")
