#!/usr/bin/env bash
set -euo pipefail

# Isolated topic-weighted CompIRT runner.
# Results go to results/compirt/in_sample/topic_compirt by default.

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/lib/result_root.sh"
TOPIC_FIXED_DIR="topic/fixed"

PYTHON="${PYTHON:-.venv/bin/python}"

# Set TOURNAMENT="" to include every tournament in the selected split.
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-2024-acf-regionals}"
OUTPUT_ROOT="$(resolve_result_root "${ROOT:-results/compirt/in_sample/topic_compirt}" in_sample)"
DEVICE="${DEVICE:-cuda}"
GPU="${GPU:-0}"
DIMENSIONS="${DIMENSIONS:-10}"
LR="${LR:-0.01}"

# Regenerate PLDA vectors by default because topic-weighted training needs
# CompIRT-compatible document IDs in document_latent_vectors.csv.
RUN_PLDA="${RUN_PLDA:-1}"
PLDA_OUTPUT_DIR="${PLDA_OUTPUT_DIR:-$TOPIC_FIXED_DIR/outputs/plda}"
TOPIC_VECTORS="${TOPIC_VECTORS:-$PLDA_OUTPUT_DIR/document_latent_vectors.csv}"
# Optional dimension,column,category CSV used to relabel topic-coordinate legends
# (e.g. topic/fixed/outputs/category/category_index.csv for one-hot categories).
TOPIC_NAMES="${TOPIC_NAMES:-}"
PLDA_ITERATIONS="${PLDA_ITERATIONS:-500}"
PLDA_TRAIN_INTERVAL="${PLDA_TRAIN_INTERVAL:-50}"
PLDA_WORKERS="${PLDA_WORKERS:-1}"

PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"

RUN_SYNERGY="${RUN_SYNERGY:-0}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-1}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
CALIBRATE_CORRECTNESS="${CALIBRATE_CORRECTNESS:-0}"
EVALUATE="${EVALUATE:-1}"

export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE="${PYTHONDONTWRITEBYTECODE:-1}"
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-topic-compirt}"

mkdir -p "$OUTPUT_ROOT"
LOG_PATH="$OUTPUT_ROOT/run.log"
exec > >(tee "$LOG_PATH") 2>&1

echo "# CompIRT Run Log"
echo
echo "Generated: $(date -Is)"
echo "Placeholder: no"
echo "Captured stdout/stderr: yes"
echo
echo "## Run Variables"
echo
echo "- RUNNER: topic/fixed/run_topic_compirt.sh"
echo "- ROOT: $OUTPUT_ROOT"
echo "- MODEL: topic-weighted"
echo "- SPLIT: $SPLIT"
echo "- TOURNAMENT: ${TOURNAMENT:-<all>}"
echo "- DEVICE: $DEVICE"
echo "- GPU: $GPU"
echo "- DIMENSIONS: $DIMENSIONS"
echo "- PYRAMIDAL_STEPS: $PYRAMIDAL_STEPS"
echo "- BONUS_STEPS: $BONUS_STEPS"
echo "- LR: $LR"
echo "- RUN_PLDA: $RUN_PLDA"
echo "- PLDA_OUTPUT_DIR: $PLDA_OUTPUT_DIR"
echo "- TOPIC_VECTORS: $TOPIC_VECTORS"
echo "- TOPIC_NAMES: ${TOPIC_NAMES:-unknown}"
echo "- RUN_SYNERGY: $RUN_SYNERGY"
echo "- SYNERGY_DIMENSIONS: $SYNERGY_DIMENSIONS"
echo "- SAVE_SYNERGY_DETAILS: $SAVE_SYNERGY_DETAILS"
echo "- CALIBRATE_CORRECTNESS: $CALIBRATE_CORRECTNESS"
echo "- PREDICT_BUZZ_POSITIONS: $PREDICT_BUZZ_POSITIONS"
echo "- EVALUATE: $EVALUATE"
echo "- MPLCONFIGDIR: $MPLCONFIGDIR"
echo "- PYRAMIDAL_OUTPUT: $OUTPUT_ROOT/pyramidal"
echo "- COMPOSITIONAL_OUTPUT: $OUTPUT_ROOT/compositional"
if [[ "$RUN_SYNERGY" == "1" ]]; then
  echo "- SYNERGY_OUTPUT: $OUTPUT_ROOT/synergy"
  echo "- SYNERGY_EVALUATION_OUTPUT: $OUTPUT_ROOT/synergy-evaluation"
fi
echo "- EVALUATION_OUTPUT: $OUTPUT_ROOT/evaluation"
echo

if [[ "$DEVICE" == "cuda" ]]; then
  export CUDA_VISIBLE_DEVICES="$GPU"
  export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
  "$PYTHON" -c "import torch; assert torch.cuda.is_available(), 'CUDA is unavailable'; print(torch.cuda.get_device_name(0))"
fi

tournament_args=()
if [[ -n "$TOURNAMENT" ]]; then
  tournament_args=(--tournament "$TOURNAMENT")
fi

if [[ "$RUN_PLDA" == "1" ]]; then
  "$PYTHON" -m topic.fixed.run_plda \
    --dimensions "$DIMENSIONS" \
    --iterations "$PLDA_ITERATIONS" \
    --train-interval "$PLDA_TRAIN_INTERVAL" \
    --workers "$PLDA_WORKERS" \
    --output-dir "$PLDA_OUTPUT_DIR"
elif [[ ! -f "$TOPIC_VECTORS" ]]; then
  echo "RUN_PLDA=0 but TOPIC_VECTORS does not exist: $TOPIC_VECTORS" >&2
  echo "Either set RUN_PLDA=1 or point TOPIC_VECTORS at an existing document_latent_vectors.csv." >&2
  exit 1
fi

calibrate_args=()
if [[ "$CALIBRATE_CORRECTNESS" == "1" ]]; then
  calibrate_args=(--calibrate-correctness)
fi

pyramidal_args=(
  --split "$SPLIT"
  "${tournament_args[@]}"
  --topic-vectors "$TOPIC_VECTORS"
  --dimensions "$DIMENSIONS"
  --steps "$PYRAMIDAL_STEPS"
  --lr "$LR"
  --device "$DEVICE"
  --output-dir "$OUTPUT_ROOT/pyramidal"
  "${calibrate_args[@]}"
)
if [[ "$PREDICT_BUZZ_POSITIONS" == "1" ]]; then
  pyramidal_args+=(--predict-buzz-positions)
fi
"$PYTHON" -m topic.fixed.train_topic_pyramidal "${pyramidal_args[@]}"

run_compositional() {
  local model_name="$1"
  shift
  "$PYTHON" -m topic.fixed.train_topic_compositional \
    --split "$SPLIT" \
    "${tournament_args[@]}" \
    --topic-vectors "$TOPIC_VECTORS" \
    --player-skills "$OUTPUT_ROOT/pyramidal/players.csv" \
    --steps "$BONUS_STEPS" \
    --lr "$LR" \
    --device "$DEVICE" \
    --output-dir "$OUTPUT_ROOT/$model_name" \
    "${calibrate_args[@]}" \
    "$@"
}

run_compositional compositional

if [[ "$RUN_SYNERGY" == "1" ]]; then
  synergy_args=(--use-synergy --synergy-dimensions "$SYNERGY_DIMENSIONS")
  if [[ "$SAVE_SYNERGY_DETAILS" == "1" ]]; then
    synergy_args+=(--save-synergy-details)
  fi
  run_compositional synergy "${synergy_args[@]}"
fi

topic_names_args=()
if [[ -n "$TOPIC_NAMES" ]]; then
  topic_names_args=(--topic-names "$TOPIC_NAMES")
fi

evaluate() {
  local model_name="$1"
  local output_name="$2"
  "$PYTHON" -m topic.fixed.evaluate_topic_compirt \
    --pyramidal-results "$OUTPUT_ROOT/pyramidal" \
    --compositional-results "$OUTPUT_ROOT/$model_name" \
    "${topic_names_args[@]}" \
    --output-dir "$OUTPUT_ROOT/$output_name"
}

if [[ "$EVALUATE" == "1" ]]; then
  evaluate compositional evaluation
  if [[ "$RUN_SYNERGY" == "1" ]]; then
    evaluate synergy synergy-evaluation
  fi
fi

echo "Finished topic-weighted CompIRT."
echo "Pyramidal results:      $OUTPUT_ROOT/pyramidal"
echo "Compositional results:  $OUTPUT_ROOT/compositional"
if [[ "$EVALUATE" == "1" ]]; then
  echo "Evaluation results:     $OUTPUT_ROOT/evaluation"
fi
if [[ "$RUN_SYNERGY" == "1" ]]; then
  echo "Synergy results:        $OUTPUT_ROOT/synergy"
  if [[ "$EVALUATE" == "1" ]]; then
    echo "Synergy evaluation:     $OUTPUT_ROOT/synergy-evaluation"
  fi
fi
