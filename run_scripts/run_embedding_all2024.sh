#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PYTHON="${PYTHON:-.venv/bin/python}"
GPU="${GPU:-0}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-}"
DIMENSIONS="${DIMENSIONS:-5}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-5000}"
BONUS_STEPS="${BONUS_STEPS:-3000}"
LR="${LR:-0.005}"
DEVICE="${DEVICE:-cuda}"
EMBED_DEVICE="${EMBED_DEVICE:-$DEVICE}"
PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
NO_CAL_ROOT="${NO_CAL_ROOT:-results/compirt/in_sample/embedding-all2024}"
CAL_ROOT="${CAL_ROOT:-results/compirt/in_sample/embedding-all2024-cal}"

run_one () {
  local root="$1"
  local calibrate="$2"
  GPU="$GPU" \
  SPLIT="$SPLIT" \
  TOURNAMENT="$TOURNAMENT" \
  ROOT="$root" \
  DIMENSIONS="$DIMENSIONS" \
  SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
  PYRAMIDAL_STEPS="$PYRAMIDAL_STEPS" \
  BONUS_STEPS="$BONUS_STEPS" \
  LR="$LR" \
  DEVICE="$DEVICE" \
  EMBED_DEVICE="$EMBED_DEVICE" \
  PREDICT_BUZZ_POSITIONS="$PREDICT_BUZZ_POSITIONS" \
  SAVE_SYNERGY_DETAILS="$SAVE_SYNERGY_DETAILS" \
  CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/run_embedding_compirt.py
}

run_one "$NO_CAL_ROOT" 0
run_one "$CAL_ROOT" 1

echo "Finished embedding all-2024 runs:"
echo "  no calibration: $NO_CAL_ROOT/synergy-evaluation/experiment_report.md"
echo "  calibration:    $CAL_ROOT/synergy-evaluation/experiment_report.md"
