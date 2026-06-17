#!/usr/bin/env bash
set -euo pipefail

# This script lives in run_scripts/, so the repo root is one directory up.
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Full 2024 experiment: validate the dataset, then train and evaluate the
# no-synergy and synergy variants. By default, it includes every 2024 tournament.
export SPLIT="${SPLIT:-year_2024}"
export TOURNAMENT="${TOURNAMENT-}"
export ROOT="${ROOT:-results/compirt/cuda-all-2024}"
export PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-5000}"
export BONUS_STEPS="${BONUS_STEPS:-3000}"
export DIMENSIONS="${DIMENSIONS:-5}"
export SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
export LR="${LR:-0.005}"
export PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"
export RUN_SYNERGY=1
export SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-1}"
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-compirt}"

PYTHON=".venv/bin/python"

tournament_args=()
if [[ -n "$TOURNAMENT" ]]; then
  tournament_args=(--tournament "$TOURNAMENT")
fi

"$PYTHON" -m data_pipeline.validate
"$PYTHON" compirt_data.py --split "$SPLIT" "${tournament_args[@]}"

./run_scripts/run_compirt.sh
