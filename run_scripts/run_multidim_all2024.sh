#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/lib/result_root.sh"

PYTHON="${PYTHON:-.venv/bin/python}"
GPU="${GPU:-0}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-}"
DIMENSIONS="${DIMENSIONS:-5}"
DIFFICULTY_LINK="${DIFFICULTY_LINK:-sigmoid}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
LR="${LR:-0.01}"
DEVICE="${DEVICE:-cuda}"
PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
NO_CAL_ROOT="$(resolve_result_root "${NO_CAL_ROOT:-results/compirt/in_sample/multidim-all2024}" in_sample)"
CAL_ROOT="$(resolve_result_root "${CAL_ROOT:-results/compirt/in_sample/multidim-all2024-cal}" in_sample)"

run_one () {
  local root="$1"
  local calibrate="$2"
  GPU="$GPU" \
  SPLIT="$SPLIT" \
  TOURNAMENT="$TOURNAMENT" \
  ROOT="$root" \
  DIMENSIONS="$DIMENSIONS" \
  DIFFICULTY_LINK="$DIFFICULTY_LINK" \
  SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
  PYRAMIDAL_STEPS="$PYRAMIDAL_STEPS" \
  BONUS_STEPS="$BONUS_STEPS" \
  LR="$LR" \
  DEVICE="$DEVICE" \
  PREDICT_BUZZ_POSITIONS="$PREDICT_BUZZ_POSITIONS" \
  SAVE_SYNERGY_DETAILS="$SAVE_SYNERGY_DETAILS" \
  CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/run_multidim_compirt.py
}

run_one "$NO_CAL_ROOT" 0
run_one "$CAL_ROOT" 1

echo "Finished multidim all-2024 runs:"
echo "  no calibration: $NO_CAL_ROOT/synergy-evaluation/experiment_report.md"
echo "  calibration:    $CAL_ROOT/synergy-evaluation/experiment_report.md"
