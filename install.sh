#!/usr/bin/env sh
set -eu

# Non-destructive local setup helper. Run from a clone of this repository.
ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$ROOT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  printf '%s\n' 'ERROR: Python 3.10+ is required. Install Python, then rerun ./install.sh.' >&2
  exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')
python3 - <<'PY'
import sys
if sys.version_info < (3, 10):
    raise SystemExit("ERROR: Python 3.10+ is required.")
PY

printf 'Python %s detected. Running static validation...\n' "$PYTHON_VERSION"
python3 scripts/validate_team.py
printf '\n%s\n' 'Setup checks passed.' 'Next: install and authenticate Claude Code using its official documentation, then launch it from this repository root.' 'This script does not install Claude Code, create credentials, change permissions, or launch an application project.'
