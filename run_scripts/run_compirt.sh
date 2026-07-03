#!/usr/bin/env bash
set -euo pipefail

# This script lives in run_scripts/, so the repo root is one directory up.
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Configuration. Set TOURNAMENT="" to include every tournament in the split.
GPU="${GPU:-0}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-2024-acf-regionals}"
OUTPUT_ROOT="${ROOT:-results/compirt/in_sample/cuda-regionals-2024}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
DIMENSIONS="${DIMENSIONS:-3}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
LR="${LR:-0.01}"
PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"
RUN_SYNERGY="${RUN_SYNERGY:-0}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
CALIBRATE_CORRECTNESS="${CALIBRATE_CORRECTNESS:-0}"

export CUDA_VISIBLE_DEVICES="$GPU"
export PYTHONUNBUFFERED=1
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-compirt}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

PYTHON=".venv/bin/python"

mkdir -p "$OUTPUT_ROOT"
LOG_PATH="$OUTPUT_ROOT/run.log"
if [[ "${COMPIRT_LOG_ACTIVE:-0}" != "1" ]]; then
  export COMPIRT_LOG_ACTIVE=1
  exec > >(tee "$LOG_PATH") 2>&1
fi

echo "# CompIRT Run Log"
echo
echo "Generated: $(date -Is)"
echo "Placeholder: no"
echo "Captured stdout/stderr: yes"
echo
echo "## Run Variables"
echo
echo "- RUNNER: run_scripts/run_compirt.sh"
echo "- ROOT: $OUTPUT_ROOT"
echo "- MODEL: baseline"
echo "- SPLIT: $SPLIT"
echo "- TOURNAMENT: ${TOURNAMENT:-<all>}"
echo "- DEVICE: cuda"
echo "- GPU: $GPU"
echo "- DIMENSIONS: $DIMENSIONS"
echo "- PYRAMIDAL_STEPS: $PYRAMIDAL_STEPS"
echo "- BONUS_STEPS: $BONUS_STEPS"
echo "- LR: $LR"
echo "- RUN_SYNERGY: $RUN_SYNERGY"
echo "- SYNERGY_DIMENSIONS: $SYNERGY_DIMENSIONS"
echo "- SAVE_SYNERGY_DETAILS: $SAVE_SYNERGY_DETAILS"
echo "- CALIBRATE_CORRECTNESS: $CALIBRATE_CORRECTNESS"
echo "- PREDICT_BUZZ_POSITIONS: $PREDICT_BUZZ_POSITIONS"
echo "- MPLCONFIGDIR: $MPLCONFIGDIR"
echo "- PYRAMIDAL_OUTPUT: $OUTPUT_ROOT/pyramidal"
echo "- COMPOSITIONAL_OUTPUT: $OUTPUT_ROOT/compositional"
if [[ "$RUN_SYNERGY" == "1" ]]; then
  echo "- SYNERGY_OUTPUT: $OUTPUT_ROOT/synergy"
  echo "- SYNERGY_EVALUATION_OUTPUT: $OUTPUT_ROOT/synergy-evaluation"
  echo "- COMPARISON_OUTPUT: $OUTPUT_ROOT/comparison"
fi
echo "- EVALUATION_OUTPUT: $OUTPUT_ROOT/evaluation"
echo

tournament_args=()
if [[ -n "$TOURNAMENT" ]]; then
  tournament_args=(--tournament "$TOURNAMENT")
fi

run_compositional() {
  local model_name="$1"
  shift
  "$PYTHON" train_compositional.py \
    --split "$SPLIT" \
    "${tournament_args[@]}" \
    --player-skills "$OUTPUT_ROOT/pyramidal/players.csv" \
    --steps "$BONUS_STEPS" \
    --lr "$LR" \
    --device cuda \
    --output-dir "$OUTPUT_ROOT/$model_name" \
    "$@"
}

evaluate() {
  local model_name="$1"
  local output_name="$2"
  "$PYTHON" evaluate_compirt.py \
    --pyramidal-results "$OUTPUT_ROOT/pyramidal" \
    --compositional-results "$OUTPUT_ROOT/$model_name" \
    --output-dir "$OUTPUT_ROOT/$output_name"
}

cuda_check="import torch; "
cuda_check+="assert torch.cuda.is_available(), 'CUDA is unavailable'; "
cuda_check+="print(torch.cuda.get_device_name(0))"
"$PYTHON" -c "$cuda_check"

pyramidal_args=(
  --split "$SPLIT"
  "${tournament_args[@]}"
  --dimensions "$DIMENSIONS"
  --steps "$PYRAMIDAL_STEPS"
  --lr "$LR"
  --device cuda
  --output-dir "$OUTPUT_ROOT/pyramidal"
)
if [[ "$PREDICT_BUZZ_POSITIONS" == "1" ]]; then
  pyramidal_args+=(--predict-buzz-positions)
fi
if [[ "$CALIBRATE_CORRECTNESS" == "1" ]]; then
  pyramidal_args+=(--calibrate-correctness)
fi
"$PYTHON" train_pyramidal.py "${pyramidal_args[@]}"

calibrate_args=()
if [[ "$CALIBRATE_CORRECTNESS" == "1" ]]; then
  calibrate_args=(--calibrate-correctness)
fi

run_compositional compositional "${calibrate_args[@]}"

if [[ "$RUN_SYNERGY" == "1" ]]; then
  synergy_args=(--use-synergy --synergy-dimensions "$SYNERGY_DIMENSIONS")
  if [[ "$SAVE_SYNERGY_DETAILS" == "1" ]]; then
    synergy_args+=(--save-synergy-details)
  fi
  synergy_args+=("${calibrate_args[@]}")
  run_compositional synergy "${synergy_args[@]}"
fi

evaluate compositional evaluation

if [[ "$RUN_SYNERGY" == "1" ]]; then
  evaluate synergy synergy-evaluation
  "$PYTHON" compare_compirt.py \
    --compositional-metrics "$OUTPUT_ROOT/evaluation/csvs/bonus_metrics.csv" \
    --synergy-metrics "$OUTPUT_ROOT/synergy-evaluation/csvs/bonus_metrics.csv" \
    --output-dir "$OUTPUT_ROOT/comparison"
fi

echo "Finished. Inspect $OUTPUT_ROOT/evaluation/experiment_report.md"
if [[ "$RUN_SYNERGY" == "1" ]]; then
  echo "Compare it with $OUTPUT_ROOT/synergy-evaluation/experiment_report.md"
  echo "Direct comparison: $OUTPUT_ROOT/comparison/bonus_model_comparison.md"
fi
