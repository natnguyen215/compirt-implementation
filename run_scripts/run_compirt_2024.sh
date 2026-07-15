#!/usr/bin/env bash
set -euo pipefail

# Thin wrapper around run_compirt_2024.py, kept as the documented shell entry
# point for the full-2024 reproducibility run. All configuration environment
# variables (ROOT, SPLIT, TOURNAMENT, GPU, ...) are read by the Python runner.
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

exec "${PYTHON:-.venv/bin/python}" run_scripts/run_compirt_2024.py "$@"
