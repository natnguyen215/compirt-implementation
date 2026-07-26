#!/usr/bin/env bash
set -euo pipefail

# Shell entry point for the full-2024 reproducibility run. run_compirt_2024.py
# reads all configuration environment variables (ROOT, SPLIT, TOURNAMENT,
# GPU, ...).
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

exec "${PYTHON:-.venv/bin/python}" run_scripts/common/run_compirt_2024.py "$@"
