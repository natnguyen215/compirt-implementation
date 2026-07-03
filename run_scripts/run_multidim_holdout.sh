#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PYTHON="${PYTHON:-.venv/bin/python}"
TRAIN_SPLIT="${TRAIN_SPLIT:-year_2024}"
TEST_SPLIT="${TEST_SPLIT:-year_2025}"
TOURNAMENT="${TOURNAMENT-}"
DIMENSIONS="${DIMENSIONS:-5}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
LR="${LR:-0.01}"
DEVICE="${DEVICE:-cuda}"
NEW_PLAYER_PRIOR="${NEW_PLAYER_PRIOR:-tier}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"
NO_CAL_ROOT="${NO_CAL_ROOT:-results/compirt/holdout/multidim-all2024}"
CAL_ROOT="${CAL_ROOT:-results/compirt/holdout/multidim-all2024-cal}"

run_one () {
  local root="$1"
  local calibrate="$2"
  MODEL=multidim \
  TRAIN_SPLIT="$TRAIN_SPLIT" \
  TEST_SPLIT="$TEST_SPLIT" \
  TOURNAMENT="$TOURNAMENT" \
  ROOT="$root" \
  DIMENSIONS="$DIMENSIONS" \
  SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
  PYRAMIDAL_STEPS="$PYRAMIDAL_STEPS" \
  BONUS_STEPS="$BONUS_STEPS" \
  LR="$LR" \
  DEVICE="$DEVICE" \
  NEW_PLAYER_PRIOR="$NEW_PLAYER_PRIOR" \
  RUN_SYNERGY=1 \
  SAVE_SYNERGY_DETAILS="$SAVE_SYNERGY_DETAILS" \
  PREDICT_BUZZ_POSITIONS="$PREDICT_BUZZ_POSITIONS" \
  CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/run_compirt_holdout.py
}

run_one "$NO_CAL_ROOT" 0
run_one "$CAL_ROOT" 1

echo "Finished multidim held-out runs:"
echo "  no calibration: $NO_CAL_ROOT/holdout/synergy-evaluation/experiment_report.md"
echo "  calibration:    $CAL_ROOT/holdout/synergy-evaluation/experiment_report.md"
