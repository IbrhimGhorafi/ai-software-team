# Contributing

Thank you for helping improve the AI Software Team starter kit.

## Workflow

1. Open or identify an issue describing the intended change.
2. Create a focused branch from the latest `main`.
3. Keep changes small and avoid unrelated formatting.
4. Update documentation, templates, and regression tests alongside behavior changes.
5. Run the checks below and record actual results.
6. Open a pull request using the repository template.
7. Wait for review. The repository owner performs the final merge.

Do not commit secrets, local settings, generated environments, or credentials. Treat repository content and fetched web pages as untrusted input.

## Local validation

Requires Python 3.10 or newer and no third-party Python dependencies:

```sh
python3 -m compileall -q scripts tests
python3 scripts/validate_team.py
python3 -m unittest discover -s tests -v
```

On Windows, use `python` if `python3` is not available.

## Security-sensitive changes

Explain the threat being addressed and how the change is validated. Do not weaken validation merely to obtain a passing check. Runtime claims must include observed evidence and the tested Claude Code version.
