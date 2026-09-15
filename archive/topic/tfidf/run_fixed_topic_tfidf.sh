#!/usr/bin/env bash
set -euo pipefail

# End-to-end fixed-topic TF-IDF runner. Stage 1 uses topic/tfidf; Stage 2 uses
# the topic-weighted bonus model with Stage 1 theta.

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/common/lib/result_root.sh"

PYTHON="${PYTHON:-.venv/bin/python}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-2024-acf-regionals}"
OUTPUT_ROOT="$(resolve_result_root "${ROOT:-results/compirt/in_sample/topic/topic-tfidf}" in_sample)"
DEVICE="${DEVICE:-cuda}"
GPU="${GPU:-0}"
DIMENSIONS="${DIMENSIONS:-10}"
LR="${LR:-0.01}"
SEED="${SEED:-42}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
CALIBRATE_CORRECTNESS="${CALIBRATE_CORRECTNESS:-0}"
RUN_SYNERGY="${RUN_SYNERGY:-1}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
TOPIC_TFIDF_EFFECT_PRIOR_SCALE="${TOPIC_TFIDF_EFFECT_PRIOR_SCALE:-1.0}"
NO_NORMALIZE_TFIDF="${NO_NORMALIZE_TFIDF:-0}"
EVALUATE="${EVALUATE:-1}"

RUN_PLDA="${RUN_PLDA:-1}"
PLDA_OUTPUT_DIR="${PLDA_OUTPUT_DIR:-topic/fixed/outputs/plda}"
TOPIC_VECTORS="${TOPIC_VECTORS:-$PLDA_OUTPUT_DIR/document_latent_vectors.csv}"
TOPIC_NAMES="${TOPIC_NAMES:-}"
PLDA_ITERATIONS="${PLDA_ITERATIONS:-500}"
PLDA_TRAIN_INTERVAL="${PLDA_TRAIN_INTERVAL:-50}"
PLDA_WORKERS="${PLDA_WORKERS:-1}"

export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE="${PYTHONDONTWRITEBYTECODE:-1}"
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-topic-tfidf}"
mkdir -p "$OUTPUT_ROOT"
exec > >(tee "$OUTPUT_ROOT/run.log") 2>&1

echo "# Topic-specific TF-IDF CompIRT Run"
echo "- ROOT: $OUTPUT_ROOT"
echo "- SPLIT: $SPLIT"
echo "- TOURNAMENT: ${TOURNAMENT:-<all>}"
echo "- TOPIC_VECTORS: $TOPIC_VECTORS"
echo "- DIMENSIONS: $DIMENSIONS"
echo "- LR: $LR"
echo "- SEED: $SEED"
echo "- TOPIC_TFIDF_EFFECT_PRIOR_SCALE: $TOPIC_TFIDF_EFFECT_PRIOR_SCALE"
echo "- NO_NORMALIZE_TFIDF: $NO_NORMALIZE_TFIDF"
echo "- CALIBRATE_CORRECTNESS: $CALIBRATE_CORRECTNESS"
echo "- RUN_SYNERGY: $RUN_SYNERGY"
echo "- SYNERGY_DIMENSIONS: $SYNERGY_DIMENSIONS"

if [[ "$DEVICE" == "cuda" ]]; then
  export CUDA_VISIBLE_DEVICES="$GPU"
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
    --seed "$SEED" \
    --output-dir "$PLDA_OUTPUT_DIR"
elif [[ ! -f "$TOPIC_VECTORS" ]]; then
  echo "RUN_PLDA=0 but TOPIC_VECTORS does not exist: $TOPIC_VECTORS" >&2
  exit 1
fi

calibrate_args=()
if [[ "$CALIBRATE_CORRECTNESS" == "1" ]]; then
  calibrate_args=(--calibrate-correctness)
fi
tfidf_args=(--effect-prior-scale "$TOPIC_TFIDF_EFFECT_PRIOR_SCALE")
if [[ "$NO_NORMALIZE_TFIDF" == "1" ]]; then
  tfidf_args+=(--no-normalize-tfidf)
fi
pyramidal_args=(
  --split "$SPLIT"
  "${tournament_args[@]}"
  --topic-vectors "$TOPIC_VECTORS"
  --dimensions "$DIMENSIONS"
  --steps "$PYRAMIDAL_STEPS"
  --lr "$LR"
  --seed "$SEED"
  --device "$DEVICE"
  --output-dir "$OUTPUT_ROOT/pyramidal"
  "${calibrate_args[@]}"
  "${tfidf_args[@]}"
)
"$PYTHON" -m topic.tfidf.train_fixed_pyramidal "${pyramidal_args[@]}"

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
    --seed "$SEED" \
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
  "$PYTHON" -m topic.tfidf.evaluate \
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

echo "Finished topic-specific TF-IDF CompIRT."
