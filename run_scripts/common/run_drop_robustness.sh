#!/usr/bin/env bash
# Thin env-knob wrapper around run_drop_robustness.py (Tier-1 random drops).
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/common/lib/result_root.sh"

PYTHON="${PYTHON:-.venv/bin/python}"
GPU="${GPU:-0}"
ROOT="$(resolve_result_root "${ROOT:-results/compirt/in_sample/common/drop-robustness}" in_sample)"
MODELS="${MODELS:-plain baseline multidim}"
FRACTIONS="${FRACTIONS:-0.001 0.005 0.01 0.05}"
REPLICATES="${REPLICATES:-3}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-}"
DIFFICULTY_LINK="${DIFFICULTY_LINK:-sigmoid}"
SEED="${SEED:-42}"
DROP_SEED="${DROP_SEED:-2025}"
DEVICE="${DEVICE:-cuda}"

extra_args=()
if [[ -n "$TOURNAMENT" ]]; then
  extra_args+=(--tournament "$TOURNAMENT")
fi

CUDA_VISIBLE_DEVICES="$GPU" "$PYTHON" run_scripts/common/run_drop_robustness.py \
  --root "$ROOT" \
  --models $MODELS \
  --fractions $FRACTIONS \
  --replicates "$REPLICATES" \
  --split "$SPLIT" \
  --difficulty-link "$DIFFICULTY_LINK" \
  --seed "$SEED" \
  --drop-seed "$DROP_SEED" \
  --device "$DEVICE" \
  "${extra_args[@]}" \
  "$@"

echo "Finished drop-robustness run: $ROOT/csvs/drop_robustness_metrics.csv"
