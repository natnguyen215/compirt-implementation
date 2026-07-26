#!/usr/bin/env bash
set -euo pipefail

# Final-round-fraction entry point. The Python wrapper defaults to holding out
# the final 20% of rounds from every tournament in BASE_SPLIT=all.
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

exec "${PYTHON:-.venv/bin/python}" run_scripts/common/run_compirt_round_holdout.py "$@"
