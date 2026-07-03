#!/usr/bin/env bash
set -euo pipefail

cd /teapot/students/natnguyen/CompIRT-Implementation

export TRAIN_SPLIT="${TRAIN_SPLIT:-year_2024}"
export TEST_SPLIT="${TEST_SPLIT:-year_2025}"
export NEW_PLAYER_PRIOR="${NEW_PLAYER_PRIOR:-tier}"

export DEVICE="${DEVICE:-cuda}"
export GPU="${GPU:-0}"
export CUDA_VISIBLE_DEVICES="$GPU"
export PYTHONUNBUFFERED=1
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-compirt}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

export PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-5000}"
export BONUS_STEPS="${BONUS_STEPS:-3000}"
export DIMENSIONS="${DIMENSIONS:-5}"
export SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
export LR="${LR:-0.005}"
export CATEGORY_PYRAMIDAL_DEVICE="${CATEGORY_PYRAMIDAL_DEVICE:-cpu}"

PY=.venv/bin/python

run_if_missing () {
  local marker="$1"
  shift
  if [[ -f "$marker" ]]; then
    echo "skip: $marker"
    return
  fi
  echo "run: $*"
  "$@"
}

run_topic_holdout () {
  local root="$1"
  local vectors="$2"
  local dims="$3"
  local topic_names="${4:-}"
  local cal="${5:-0}"
  local pyramidal_device="${6:-$DEVICE}"
  local cal_args=()
  local names_args=()

  if [[ "$cal" == "1" ]]; then
    cal_args=(--calibrate-correctness)
  fi
  if [[ -n "$topic_names" ]]; then
    names_args=(--topic-names "$topic_names")
  fi

  run_if_missing "$root/train/pyramidal/summary.json" \
    "$PY" -m topic.fixed.train_topic_pyramidal \
      --split "$TRAIN_SPLIT" \
      --topic-vectors "$vectors" \
      --dimensions "$dims" \
      --steps "$PYRAMIDAL_STEPS" \
      --lr "$LR" \
      --device "$pyramidal_device" \
      --predict-buzz-positions \
      "${cal_args[@]}" \
      --output-dir "$root/train/pyramidal"

  run_if_missing "$root/holdout/pyramidal/summary.json" \
    "$PY" -m topic.fixed.train_topic_pyramidal \
      --split "$TEST_SPLIT" \
      --topic-vectors "$vectors" \
      --dimensions "$dims" \
      --steps "$PYRAMIDAL_STEPS" \
      --lr "$LR" \
      --device "$pyramidal_device" \
      --train-posterior "$root/train/pyramidal/player_posterior.csv" \
      --new-player-prior "$NEW_PLAYER_PRIOR" \
      --predict-buzz-positions \
      "${cal_args[@]}" \
      --output-dir "$root/holdout/pyramidal"

  run_if_missing "$root/holdout/compositional/summary.json" \
    "$PY" -m topic.fixed.train_topic_compositional \
      --split "$TEST_SPLIT" \
      --topic-vectors "$vectors" \
      --player-skills "$root/holdout/pyramidal/players.csv" \
      --steps "$BONUS_STEPS" \
      --lr "$LR" \
      --device "$DEVICE" \
      "${cal_args[@]}" \
      --output-dir "$root/holdout/compositional"

  run_if_missing "$root/holdout/synergy/summary.json" \
    "$PY" -m topic.fixed.train_topic_compositional \
      --split "$TEST_SPLIT" \
      --topic-vectors "$vectors" \
      --player-skills "$root/holdout/pyramidal/players.csv" \
      --use-synergy \
      --synergy-dimensions "$SYNERGY_DIMENSIONS" \
      --save-synergy-details \
      --steps "$BONUS_STEPS" \
      --lr "$LR" \
      --device "$DEVICE" \
      "${cal_args[@]}" \
      --output-dir "$root/holdout/synergy"

  run_if_missing "$root/holdout/evaluation/experiment_report.md" \
    "$PY" -m topic.fixed.evaluate_topic_compirt \
      --pyramidal-results "$root/holdout/pyramidal" \
      --compositional-results "$root/holdout/compositional" \
      "${names_args[@]}" \
      --output-dir "$root/holdout/evaluation"

  run_if_missing "$root/holdout/synergy-evaluation/experiment_report.md" \
    "$PY" -m topic.fixed.evaluate_topic_compirt \
      --pyramidal-results "$root/holdout/pyramidal" \
      --compositional-results "$root/holdout/synergy" \
      "${names_args[@]}" \
      --output-dir "$root/holdout/synergy-evaluation"
}

run_learned_holdout () {
  local root="$1"
  local cal="${2:-0}"
  local cal_args=()

  if [[ "$cal" == "1" ]]; then
    cal_args=(--calibrate-correctness)
  fi

  run_if_missing "$root/train/pyramidal/summary.json" \
    "$PY" -m topic.learned.train_joint_pyramidal \
      --split "$TRAIN_SPLIT" \
      --dimensions "$DIMENSIONS" \
      --steps "$PYRAMIDAL_STEPS" \
      --lr "$LR" \
      --device "$DEVICE" \
      --predict-buzz-positions \
      "${cal_args[@]}" \
      --output-dir "$root/train/pyramidal"

  run_if_missing "$root/holdout/pyramidal/summary.json" \
    "$PY" -m topic.learned.train_joint_pyramidal \
      --split "$TEST_SPLIT" \
      --dimensions "$DIMENSIONS" \
      --steps "$PYRAMIDAL_STEPS" \
      --lr "$LR" \
      --device "$DEVICE" \
      --train-posterior "$root/train/pyramidal/player_posterior.csv" \
      --train-topic-model "$root/train/pyramidal" \
      --new-player-prior "$NEW_PLAYER_PRIOR" \
      --predict-buzz-positions \
      "${cal_args[@]}" \
      --output-dir "$root/holdout/pyramidal"

  run_if_missing "$root/holdout/compositional/summary.json" \
    "$PY" -m topic.learned.train_joint_compositional \
      --split "$TEST_SPLIT" \
      --player-skills "$root/holdout/pyramidal/players.csv" \
      --topic-model-dir "$root/train/pyramidal" \
      --steps "$BONUS_STEPS" \
      --lr "$LR" \
      --device "$DEVICE" \
      "${cal_args[@]}" \
      --output-dir "$root/holdout/compositional"

  run_if_missing "$root/holdout/synergy/summary.json" \
    "$PY" -m topic.learned.train_joint_compositional \
      --split "$TEST_SPLIT" \
      --player-skills "$root/holdout/pyramidal/players.csv" \
      --topic-model-dir "$root/train/pyramidal" \
      --use-synergy \
      --synergy-dimensions "$SYNERGY_DIMENSIONS" \
      --save-synergy-details \
      --steps "$BONUS_STEPS" \
      --lr "$LR" \
      --device "$DEVICE" \
      "${cal_args[@]}" \
      --output-dir "$root/holdout/synergy"

  run_if_missing "$root/holdout/evaluation/experiment_report.md" \
    "$PY" -m topic.fixed.evaluate_topic_compirt \
      --pyramidal-results "$root/holdout/pyramidal" \
      --compositional-results "$root/holdout/compositional" \
      --output-dir "$root/holdout/evaluation"

  run_if_missing "$root/holdout/synergy-evaluation/experiment_report.md" \
    "$PY" -m topic.fixed.evaluate_topic_compirt \
      --pyramidal-results "$root/holdout/pyramidal" \
      --compositional-results "$root/holdout/synergy" \
      --output-dir "$root/holdout/synergy-evaluation"
}

category_vectors=topic/fixed/outputs/category/document_latent_vectors.csv
category_names=topic/fixed/outputs/category/category_index.csv

run_topic_holdout \
  results/compirt/holdout/category-all2024 \
  "$category_vectors" \
  13 \
  "$category_names" \
  0 \
  "$CATEGORY_PYRAMIDAL_DEVICE"

run_topic_holdout \
  results/compirt/holdout/category-all2024-cal \
  "$category_vectors" \
  13 \
  "$category_names" \
  1 \
  "$CATEGORY_PYRAMIDAL_DEVICE"

run_learned_holdout results/compirt/holdout/learned-topic-all2024 0
run_learned_holdout results/compirt/holdout/learned-topic-all2024-cal 1
