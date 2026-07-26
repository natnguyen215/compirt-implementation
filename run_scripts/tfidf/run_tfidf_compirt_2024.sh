#!/usr/bin/env bash
set -euo pipefail

# Full-2024 TF-IDF CompIRT pipeline: TF-IDF-adjusted pyramidal Stage 1,
# standard compositional Stage 2, and evaluation.

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/common/lib/result_root.sh"

# Set TOURNAMENT="" to include every tournament in the split.
GPU="${GPU:-0}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-}"
CALIBRATE_CORRECTNESS="${CALIBRATE_CORRECTNESS:-0}"

if [[ "$CALIBRATE_CORRECTNESS" == "1" ]]; then
  DEFAULT_ROOT="results/compirt/in_sample/tfidf/tfidf-cumulative-difficulty-all2024-cal"
else
  DEFAULT_ROOT="results/compirt/in_sample/tfidf/tfidf-cumulative-difficulty-all2024"
fi
OUTPUT_ROOT="$(resolve_result_root "${ROOT:-$DEFAULT_ROOT}" in_sample)"

PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-5000}"
BONUS_STEPS="${BONUS_STEPS:-3000}"
DIMENSIONS="${DIMENSIONS:-5}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
LR="${LR:-0.005}"
SEED="${SEED:-42}"
RUN_SYNERGY="${RUN_SYNERGY:-1}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-1}"
RUN_VALIDATION="${RUN_VALIDATION:-1}"
TFIDF_PLOT_COUNT="${TFIDF_PLOT_COUNT:-6}"

TFIDF_EFFECT_PRIOR_SCALE="${TFIDF_EFFECT_PRIOR_SCALE:-1.0}"
NO_NORMALIZE_TFIDF="${NO_NORMALIZE_TFIDF:-0}"

export CUDA_VISIBLE_DEVICES="$GPU"
export PYTHONUNBUFFERED=1
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-compirt}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

PYTHON="${PYTHON:-.venv/bin/python}"

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
echo "- RUNNER: run_scripts/tfidf/run_tfidf_compirt_2024.sh"
echo "- ROOT: $OUTPUT_ROOT"
echo "- MODEL: tfidf-cumulative-difficulty-pyramidal"
echo "- SPLIT: $SPLIT"
echo "- TOURNAMENT: ${TOURNAMENT:-<all>}"
echo "- DEVICE: cuda"
echo "- GPU: $GPU"
echo "- DIMENSIONS: $DIMENSIONS"
echo "- PYRAMIDAL_STEPS: $PYRAMIDAL_STEPS"
echo "- BONUS_STEPS: $BONUS_STEPS"
echo "- LR: $LR"
echo "- SEED: $SEED"
echo "- RUN_SYNERGY: $RUN_SYNERGY"
echo "- SYNERGY_DIMENSIONS: $SYNERGY_DIMENSIONS"
echo "- SAVE_SYNERGY_DETAILS: $SAVE_SYNERGY_DETAILS"
echo "- CALIBRATE_CORRECTNESS: $CALIBRATE_CORRECTNESS"
echo "- RUN_VALIDATION: $RUN_VALIDATION"
echo "- TFIDF_EFFECT_PRIOR_SCALE: $TFIDF_EFFECT_PRIOR_SCALE"
echo "- NO_NORMALIZE_TFIDF: $NO_NORMALIZE_TFIDF"
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

calibrate_args=()
if [[ "$CALIBRATE_CORRECTNESS" == "1" ]]; then
  calibrate_args=(--calibrate-correctness)
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
    --seed "$SEED" \
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

if [[ "$RUN_VALIDATION" == "1" ]]; then
  "$PYTHON" -m data_pipeline.validate
  "$PYTHON" compirt_data.py --split "$SPLIT" "${tournament_args[@]}"
fi

pyramidal_args=(
  --split "$SPLIT"
  "${tournament_args[@]}"
  --dimensions "$DIMENSIONS"
  --steps "$PYRAMIDAL_STEPS"
  --lr "$LR"
  --seed "$SEED"
  --device cuda
  --tfidf-effect-prior-scale "$TFIDF_EFFECT_PRIOR_SCALE"
  --output-dir "$OUTPUT_ROOT/pyramidal"
)
if [[ "$NO_NORMALIZE_TFIDF" == "1" ]]; then
  pyramidal_args+=(--no-normalize-tfidf)
fi
pyramidal_args+=("${calibrate_args[@]}")

"$PYTHON" -m tfidf.train_tfidf_pyramidal "${pyramidal_args[@]}"

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

"$PYTHON" -m tfidf.plot_tfidf_difficulty_curves \
  --results-dir "$OUTPUT_ROOT/pyramidal" \
  --output-dir "$OUTPUT_ROOT/evaluation/graphs" \
  --count "$TFIDF_PLOT_COUNT"

if [[ "$RUN_SYNERGY" == "1" ]]; then
  evaluate synergy synergy-evaluation
  "$PYTHON" run_scripts/common/run_synergy_comparison.py \
    --compositional-metrics "$OUTPUT_ROOT/evaluation/csvs/bonus_metrics.csv" \
    --synergy-metrics "$OUTPUT_ROOT/synergy-evaluation/csvs/bonus_metrics.csv" \
    --output-dir "$OUTPUT_ROOT/comparison"
fi

echo "Finished. Inspect $OUTPUT_ROOT/evaluation/experiment_report.md"
if [[ "$RUN_SYNERGY" == "1" ]]; then
  echo "Compare it with $OUTPUT_ROOT/synergy-evaluation/experiment_report.md"
  echo "Direct comparison: $OUTPUT_ROOT/comparison/bonus_model_comparison.md"
fi
