#!/usr/bin/env bash
set -euo pipefail

# Shell entry point for run_compirt.py. The Python runner reads all configuration
# environment variables (ROOT, SPLIT, TOURNAMENT, GPU, ...).
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

exec "${PYTHON:-.venv/bin/python}" run_scripts/common/run_compirt.py "$@"
