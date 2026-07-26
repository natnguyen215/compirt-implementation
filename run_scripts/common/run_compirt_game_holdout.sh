#!/usr/bin/env bash
set -euo pipefail

# Stratified whole-game k-fold matrix-infill entry point. The Python wrapper
# holds out whole games spread across every tournament and round, then scores
# them with train-frozen parameters (no test refitting) and aggregates the
# per-fold metrics. Defaults: BASE_SPLIT=year_2024, N_FOLDS=5, SPLIT_SEED=42.
# MODEL must be multidim.
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

exec "${PYTHON:-.venv/bin/python}" run_scripts/common/run_compirt_game_holdout.py "$@"
