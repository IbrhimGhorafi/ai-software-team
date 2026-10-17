"""Regression tests for the public static validator contract.

These tests deliberately make no claim about Claude Code runtime behavior.
"""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / ".claude" / "agents"


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


class ValidatorRegressionTests(unittest.TestCase):
    def test_static_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_team.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_every_agent_has_an_explicit_tools_allowlist(self):
        agents = sorted(AGENTS.glob("*.md"))
        self.assertTrue(agents, "No agent definitions found")
        for path in agents:
            with self.subTest(agent=path.name):
                tools = read_frontmatter(path).get("tools", "").strip()
                self.assertTrue(tools, f"{path.relative_to(ROOT)} has no tools allowlist")
                self.assertEqual(
                    len([tool.strip() for tool in tools.split(",") if tool.strip()]),
                    len(set(tool.strip() for tool in tools.split(",") if tool.strip())),
                    f"{path.relative_to(ROOT)} has duplicate tools",
                )

    def test_security_reviewer_is_read_only(self):
        path = AGENTS / "code-review-security.md"
        self.assertTrue(path.is_file(), "Security reviewer agent is missing")
        tools = {
            tool.strip()
            for tool in read_frontmatter(path).get("tools", "").split(",")
            if tool.strip()
        }
        forbidden = {"Edit", "Write", "Bash"} & tools
        self.assertFalse(
            forbidden,
            f"Security reviewer must remain read-only; forbidden tools: {sorted(forbidden)}",
        )


if __name__ == "__main__":
    unittest.main()
