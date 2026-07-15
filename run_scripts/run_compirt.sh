#!/usr/bin/env bash
set -euo pipefail

# Thin wrapper around run_compirt.py, kept as the documented shell entry point.
# All configuration environment variables (ROOT, SPLIT, TOURNAMENT, GPU, ...)
# are read by the Python runner.
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

exec "${PYTHON:-.venv/bin/python}" run_scripts/run_compirt.py "$@"
