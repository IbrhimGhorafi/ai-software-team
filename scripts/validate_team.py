#!/usr/bin/env python3
"""Static validation for the reusable Claude Code AI team starter kit.

Checks inventories, non-empty content, frontmatter, permission guardrails,
CI security settings, and critical orchestration contract markers. Static
validation cannot prove Claude Code runtime behavior or GitHub owner settings.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TOOLS = {"Read", "Grep", "Glob", "Edit", "Write", "Bash", "WebSearch", "WebFetch"}
MANIFEST_PATH = ROOT / ".claude" / "manifest.json"
errors: list[str] = []


def load_manifest() -> dict:
    """Load and validate the declarative inventory manifest."""
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot load .claude/manifest.json: {exc}")
        return {}
    if manifest.get("schema_version") != 1:
        errors.append("Unsupported or missing manifest schema_version (expected 1)")
    inventory = manifest.get("inventory")
    if not isinstance(inventory, dict):
        errors.append("Manifest inventory must be an object")
        return {}
    for kind in ("agents", "skills", "commands", "templates"):
        spec = inventory.get(kind)
        if not isinstance(spec, dict):
            errors.append(f"Manifest inventory.{kind} must be an object")
            continue
        if not isinstance(spec.get("directory"), str) or not isinstance(spec.get("pattern"), str):
            errors.append(f"Manifest inventory.{kind} must define string directory and pattern")
        if kind in ("agents", "skills"):
            count = spec.get("minimum_count")
            if not isinstance(count, int) or isinstance(count, bool) or count < 1:
                errors.append(f"Manifest inventory.{kind}.minimum_count must be a positive integer")
        else:
            required = spec.get("required")
            if not isinstance(required, list) or not all(isinstance(item, str) and item.strip() for item in required):
                errors.append(f"Manifest inventory.{kind}.required must be a list of non-empty filenames")
            elif len(required) != len(set(required)):
                errors.append(f"Manifest inventory.{kind}.required contains duplicate filenames")
    return inventory


def read_text(path: Path) -> str:
    """Read UTF-8 text, recording failures rather than hiding them."""
    relative = path.relative_to(ROOT)
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read {relative}: {exc}")
        return ""


def require_nonempty(path: Path, label: str | None = None) -> str:
    text = read_text(path) if path.is_file() else ""
    if not path.is_file():
        errors.append(f"Missing required {label or 'file'}: {path.relative_to(ROOT)}")
    elif not text.strip():
        errors.append(f"Empty required {label or 'file'}: {path.relative_to(ROOT)}")
    return text


manifest_inventory = load_manifest()


def inventory_paths(kind: str) -> list[Path]:
    spec = manifest_inventory.get(kind, {})
    directory = spec.get("directory")
    pattern = spec.get("pattern")
    if not isinstance(directory, str) or not isinstance(pattern, str):
        return []
    folder = ROOT / directory
    return sorted(folder.glob(pattern)) if folder.is_dir() else []


agents = inventory_paths("agents")
skills = inventory_paths("skills")
commands = inventory_paths("commands")
templates = inventory_paths("templates")

for kind, paths in (("agents", agents), ("skills", skills)):
    spec = manifest_inventory.get(kind, {})
    minimum = spec.get("minimum_count")
    if isinstance(minimum, int) and not isinstance(minimum, bool) and len(paths) < minimum:
        errors.append(f"Manifest requires at least {minimum} {kind} files, found {len(paths)}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = require_nonempty(path)
    if not text:
        return {}
    if not text.startswith("---\n"):
        errors.append(f"Frontmatter must start with ---: {path.relative_to(ROOT)}")
        return {}
    match = re.search(r"\n---\s*(?:\n|$)", text[4:])
    if not match:
        errors.append(f"Frontmatter closing delimiter missing: {path.relative_to(ROOT)}")
        return {}
    block = text[4:4 + match.start()]
    fields: dict[str, str] = {}
    for line_number, line in enumerate(block.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"Invalid frontmatter line {line_number} in {path.relative_to(ROOT)}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            errors.append(f"Empty frontmatter key at line {line_number} in {path.relative_to(ROOT)}")
            continue
        if key in fields:
            errors.append(f"Duplicate frontmatter key '{key}' in {path.relative_to(ROOT)}")
        fields[key] = value
    for required in ("name", "description"):
        if not fields.get(required, "").strip():
            errors.append(f"Missing or empty '{required}' in {path.relative_to(ROOT)}")
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
        raw = parse_frontmatter(path).get("tools", "").strip()
        if not raw:
            errors.append(f"Agent must declare an explicit 'tools' allowlist: {path.relative_to(ROOT)}")
            continue
        names = [tool.strip() for tool in raw.split(",") if tool.strip()]
        unknown = [tool for tool in names if tool not in ALLOWED_TOOLS]
        if unknown:
            errors.append(f"Unknown tools {unknown} in {path.relative_to(ROOT)}")
        if len(set(names)) != len(names):
            errors.append(f"Duplicate tools in {path.relative_to(ROOT)}")
        if path.stem == "code-review-security" and {"Edit", "Write", "Bash"} & set(names):
            errors.append("code-review-security must remain read-only (no Edit/Write/Bash)")


check_agent_tools(agents)
check_unique_names(agents, "agent")
check_unique_names(skills, "skill")

for path in agents:
    body = read_text(path).split("---", 2)
    if len(body) < 3 or len(body[2].strip()) < 80:
        errors.append(f"Agent body is missing or suspiciously short: {path.relative_to(ROOT)}")

for path in skills:
    text = require_nonempty(path, "skill")
    if len(text.splitlines()) < 8:
        errors.append(f"Skill content is suspiciously short: {path.relative_to(ROOT)}")

def check_required_files(kind: str, paths: list[Path]) -> None:
    spec = manifest_inventory.get(kind, {})
    required = spec.get("required", [])
    actual = {path.name for path in paths}
    for name in sorted(set(required) - actual):
        errors.append(f"Missing required {kind[:-1] if kind.endswith('s') else kind}: {spec.get('directory', kind)}/{name}")


check_required_files("commands", commands)
for path in commands:
    text = require_nonempty(path, "command")
    if len(text.splitlines()) < 5:
        errors.append(f"Command content is suspiciously short: {path.relative_to(ROOT)}")

check_required_files("templates", templates)
for path in templates:
    require_nonempty(path, "template")

required_files = [
    "README.md", ".claude/CLAUDE.md",
    "workflows/future-project-workflow.md", "workflows/project-bootstrap.md",
    "workflows/agile-agent-delivery.md", "workflows/orchestration-contract.md",
    "docs/orchestration-design.md", "docs/agent-traceability.md",
    "docs/verification-report.md", "docs/agile-command-reference.md",
    "standards/engineering-principles.md", "standards/security-principles.md",
    "standards/git-workflow.md", "standards/definition-of-done.md",
]
for relative in required_files:
    require_nonempty(ROOT / relative)

contract_path = ROOT / "workflows" / "orchestration-contract.md"
if contract_path.is_file():
    contract = read_text(contract_path)
    for marker in (
        "Session-start / resume protocol", "Task ownership and concurrency",
        "Retry, failure and recovery", "Quality and merge gate",
        "Daily report evidence rules", "human repository owner merges PRs",
        "atomic exclusivity",
    ):
        if marker.casefold() not in contract.casefold():
            errors.append(f"Orchestration contract missing required marker: {marker}")

design_path = ROOT / "docs" / "orchestration-design.md"
if design_path.is_file():
    design = read_text(design_path)
    if "only after the user approves a real project" in design.casefold():
        errors.append("Contradictory activation rule in docs/orchestration-design.md")

settings_path = ROOT / ".claude" / "settings.json"
settings_text = require_nonempty(settings_path, "Claude Code permission settings")
if settings_text:
    try:
        settings = json.loads(settings_text)
        deny = settings.get("permissions", {}).get("deny", [])
        required_denies = (
            "Bash(git push --force*)", "Bash(gh pr merge*)",
            "Bash(rm -rf*)", "Read(./.env)",
        )
        for rule in required_denies:
            if rule not in deny:
                errors.append(f"Claude Code permission deny rule missing: {rule}")
    except (json.JSONDecodeError, AttributeError) as exc:
        errors.append(f"Invalid .claude/settings.json: {exc}")

ignore_path = ROOT / ".gitignore"
ignore_text = require_nonempty(ignore_path, ".gitignore")
for pattern in (".env", "*.pem", "*.key"):
    if pattern not in ignore_text:
        errors.append(f".gitignore missing sensitive-file pattern: {pattern}")

workflow_path = ROOT / ".github" / "workflows" / "validate-team.yml"
workflow_text = require_nonempty(workflow_path, "validation workflow")
if workflow_text:
    if not re.search(r"(?m)^\s*contents:\s*read\s*$", workflow_text):
        errors.append("Validation workflow must keep contents permission read-only")
    if "persist-credentials: false" not in workflow_text:
        errors.append("Validation workflow checkout must set persist-credentials: false")

secret_workflow = ROOT / ".github" / "workflows" / "secret-scan.yml"
secret_text = require_nonempty(secret_workflow, "secret scanning workflow")
if secret_text and ("gitleaks" not in secret_text.casefold() or "pull_request:" not in secret_text):
    errors.append("Secret scanning workflow must run Gitleaks on pull requests")

dependabot_path = ROOT / ".github" / "dependabot.yml"
dependabot_text = require_nonempty(dependabot_path, "Dependabot configuration")
if dependabot_text and ("package-ecosystem: github-actions" not in dependabot_text or "interval: weekly" not in dependabot_text):
    errors.append("Dependabot must schedule weekly GitHub Actions updates")

print(f"Agents: {len(agents)} discovered; manifest minimum {manifest_inventory.get('agents', {}).get('minimum_count', 'invalid')}")
print(f"Skills: {len(skills)} discovered; manifest minimum {manifest_inventory.get('skills', {}).get('minimum_count', 'invalid')}")
print(f"Commands: {len(commands)} discovered; {len(manifest_inventory.get('commands', {}).get('required', []))} required by manifest")
print(f"Templates: {len(templates)} discovered; {len(manifest_inventory.get('templates', {}).get('required', []))} required by manifest")
print(f"Required documentation files checked: {len(required_files)}")
print("Security checks: Claude deny rules, .gitignore, read-only CI, checkout credentials, Gitleaks and Dependabot")
print("Static-only validation: does not prove Claude Code runtime behavior or GitHub owner settings")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PASS")
