#!/usr/bin/env bash
set -euo pipefail

# Run the cumulative TF-IDF pyramidal model as an in-sample 2024 run.
# Defaults mirror the other full-2024 in-sample result scripts:
#   pyramidal 5000 steps, bonus 3000 steps, 5 dimensions, 3 synergy dimensions.

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/lib/result_root.sh"

GPU="${GPU:-0}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-}"
CALIBRATE_CORRECTNESS="${CALIBRATE_CORRECTNESS:-0}"

PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-5000}"
BONUS_STEPS="${BONUS_STEPS:-3000}"
DIMENSIONS="${DIMENSIONS:-5}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
LR="${LR:-0.005}"
PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"
RUN_SYNERGY="${RUN_SYNERGY:-1}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-1}"
TFIDF_EFFECT_PRIOR_SCALE="${TFIDF_EFFECT_PRIOR_SCALE:-1.0}"
NO_NORMALIZE_TFIDF="${NO_NORMALIZE_TFIDF:-0}"
TFIDF_PLOT_COUNT="${TFIDF_PLOT_COUNT:-6}"
MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-compirt}"

PYTHON="${PYTHON:-.venv/bin/python}"
VARIANT="cumulative-difficulty"

cal_suffix=""
if [[ "$CALIBRATE_CORRECTNESS" == "1" ]]; then
  cal_suffix="-cal"
fi

tournament_args=()
if [[ -n "$TOURNAMENT" ]]; then
  tournament_args=(--tournament "$TOURNAMENT")
fi

echo "Validating data once before the cumulative TF-IDF run..."
"$PYTHON" -m data_pipeline.validate
"$PYTHON" compirt_data.py --split "$SPLIT" "${tournament_args[@]}"

root="$(resolve_result_root "${ROOT_PREFIX:-results/compirt/in_sample}/tfidf-${VARIANT}-all2024${cal_suffix}" in_sample)"
echo
echo "## $VARIANT -> $root"
GPU="$GPU" \
SPLIT="$SPLIT" \
TOURNAMENT="$TOURNAMENT" \
CALIBRATE_CORRECTNESS="$CALIBRATE_CORRECTNESS" \
TFIDF_VARIANT="$VARIANT" \
ROOT="$root" \
PYRAMIDAL_STEPS="$PYRAMIDAL_STEPS" \
BONUS_STEPS="$BONUS_STEPS" \
DIMENSIONS="$DIMENSIONS" \
SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
LR="$LR" \
PREDICT_BUZZ_POSITIONS="$PREDICT_BUZZ_POSITIONS" \
RUN_SYNERGY="$RUN_SYNERGY" \
SAVE_SYNERGY_DETAILS="$SAVE_SYNERGY_DETAILS" \
RUN_VALIDATION=0 \
TFIDF_EFFECT_PRIOR_SCALE="$TFIDF_EFFECT_PRIOR_SCALE" \
NO_NORMALIZE_TFIDF="$NO_NORMALIZE_TFIDF" \
TFIDF_PLOT_COUNT="$TFIDF_PLOT_COUNT" \
MPLCONFIGDIR="$MPLCONFIGDIR" \
PYTHON="$PYTHON" \
  bash run_scripts/run_tfidf_compirt_2024.sh

echo
echo "Finished cumulative TF-IDF in-sample run:"
echo "  $VARIANT: $root/evaluation/experiment_report.md"
if [[ "$RUN_SYNERGY" == "1" ]]; then
  echo "    synergy: $root/synergy-evaluation/experiment_report.md"
fi
