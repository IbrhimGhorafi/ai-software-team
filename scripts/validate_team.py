#!/usr/bin/env python3
"""Static validation for the reusable Claude Code AI team starter kit.

Checks inventory, required files, basic frontmatter, and critical orchestration
contract markers. This is static validation only; it does not prove Claude Code
runtime discovery, delegation, atomic locking, application execution, or tests.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_AGENTS = 12
EXPECTED_SKILLS = 18
ALLOWED_TOOLS = {"Read", "Grep", "Glob", "Edit", "Write", "Bash", "WebSearch", "WebFetch"}
errors: list[str] = []

agents = sorted((ROOT / ".claude" / "agents").glob("*.md"))
skills = sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md"))

if len(agents) != EXPECTED_AGENTS:
    errors.append(f"Expected {EXPECTED_AGENTS} agent files, found {len(agents)}")
if len(skills) != EXPECTED_SKILLS:
    errors.append(f"Expected {EXPECTED_SKILLS} skill files, found {len(skills)}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    relative = path.relative_to(ROOT)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read {relative}: {exc}")
        return {}
    if not text.startswith("---\n"):
        errors.append(f"Frontmatter must start with ---: {relative}")
        return {}
    match = re.search(r"\n---\s*(?:\n|$)", text[4:])
    if not match:
        errors.append(f"Frontmatter closing delimiter missing: {relative}")
        return {}
    block = text[4:4 + match.start()]
    fields: dict[str, str] = {}
    for line_number, line in enumerate(block.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"Invalid frontmatter line {line_number} in {relative}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            errors.append(f"Empty frontmatter key at line {line_number} in {relative}")
            continue
        if key in fields:
            errors.append(f"Duplicate frontmatter key '{key}' in {relative}")
        fields[key] = value
    for required in ("name", "description"):
        if not fields.get(required, "").strip():
            errors.append(f"Missing or empty '{required}' in {relative}")
    return fields


def check_unique_names(paths: list[Path], kind: str) -> None:
    seen: dict[str, Path] = {}
    for path in paths:
        name = parse_frontmatter(path).get("name", "").strip()
        if not name:
            continue
        if name in seen:
            errors.append(
                f"Duplicate {kind} name '{name}': "
                f"{seen[name].relative_to(ROOT)} and {path.relative_to(ROOT)}"
            )
        else:
            seen[name] = path


def check_agent_tools(paths: list[Path]) -> None:
    for path in paths:
        relative = path.relative_to(ROOT)
        raw = parse_frontmatter(path).get("tools", "").strip()
        if not raw:
            errors.append(f"Agent must declare an explicit 'tools' allowlist: {relative}")
            continue
        names = [tool.strip() for tool in raw.split(",") if tool.strip()]
        unknown = [tool for tool in names if tool not in ALLOWED_TOOLS]
        if unknown:
            errors.append(f"Unknown tools {unknown} in {relative}")
        if len(set(names)) != len(names):
            errors.append(f"Duplicate tools in {relative}")
        if path.stem == "code-review-security" and {"Edit", "Write", "Bash"} & set(names):
            errors.append("code-review-security must remain read-only (no Edit/Write/Bash)")


check_agent_tools(agents)
check_unique_names(agents, "agent")
check_unique_names(skills, "skill")

required_files = [
    "README.md",
    ".claude/CLAUDE.md",
    "workflows/future-project-workflow.md",
    "workflows/project-bootstrap.md",
    "workflows/agile-agent-delivery.md",
    "workflows/orchestration-contract.md",
    "docs/orchestration-design.md",
    "docs/agent-traceability.md",
    "docs/verification-report.md",
    "standards/engineering-principles.md",
    "standards/security-principles.md",
    "standards/git-workflow.md",
    "standards/definition-of-done.md",
    "templates/requirements-template.md",
    "templates/user-story-template.md",
    "templates/architecture-decision-template.md",
    "templates/sprint-plan-template.md",
    "templates/test-plan-template.md",
    "templates/code-review-template.md",
    "templates/session-handover-template.md",
]

for relative in required_files:
    target = ROOT / relative
    if not target.is_file():
        errors.append(f"Missing required file: {relative}")
    elif not target.read_text(encoding="utf-8").strip():
        errors.append(f"Required file is empty: {relative}")

required_commands = [
    ".claude/commands/kickoff.md",
    ".claude/commands/plan-sprint.md",
    ".claude/commands/next-story.md",
    ".claude/commands/approve-gate.md",
    ".claude/commands/review-pr.md",
    ".claude/commands/status.md",
    ".claude/commands/handover.md",
    ".claude/commands/daily-report.md",
    "templates/project-state-template.md",
    "docs/agile-command-reference.md",
    "workflows/sprint-execution-checklist.md",
]
for relative in required_commands:
    target = ROOT / relative
    if not target.is_file():
        errors.append(f"Missing Agile command/template file: {relative}")
    elif not target.read_text(encoding="utf-8").strip():
        errors.append(f"Agile command/template file is empty: {relative}")

contract_path = ROOT / "workflows" / "orchestration-contract.md"
if contract_path.is_file():
    contract = contract_path.read_text(encoding="utf-8")
    for marker in (
        "Session-start / resume protocol",
        "Task ownership and concurrency",
        "Retry, failure and recovery",
        "Quality and merge gate",
        "Daily report evidence rules",
        "human repository owner merges PRs",
        "atomic exclusivity",
    ):
        if marker.casefold() not in contract.casefold():
            errors.append(f"Orchestration contract missing required marker: {marker}")

design_path = ROOT / "docs" / "orchestration-design.md"
if design_path.is_file():
    design = design_path.read_text(encoding="utf-8")
    if "only after the user approves a real project" in design.casefold():
        errors.append(
            "Contradictory activation rule in docs/orchestration-design.md; "
            "a clear build request must activate discovery immediately"
        )

print(f"Agents: {len(agents)}/{EXPECTED_AGENTS}")
print(f"Skills: {len(skills)}/{EXPECTED_SKILLS}")
print(f"Required files checked: {len(required_files)}")
print(f"Agile command/template files checked: {len(required_commands)}")
print("Frontmatter checks: name, description, agent tools allowlist, delimiter, duplicate keys and duplicate names")
print("Orchestration checks: required contract sections and selected activation contradiction")
print("Static-only validation: no Claude runtime, lock service, application, or tests invoked")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PASS")
