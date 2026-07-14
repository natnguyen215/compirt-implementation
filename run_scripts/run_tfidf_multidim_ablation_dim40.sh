#!/usr/bin/env bash
# Held-out TF-IDF multidim dimension ablation over the same points as
# run_multidim_ablation_dim40.sh, with the same Gamma(2, 2) bonus-part alpha
# prior. Stage 1 is tfidf/multidim (free per-dimension Gamma r plus the TF-IDF
# clue-timing intervention); Stage 2 is the shared root compositional model.
# Detaches under nohup on GPU 1 and prints the pid.
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON="${PYTHON:-.venv/bin/python}"
ROOT="${ROOT:-results/compirt/holdout/tfidf-multidim-ablation-gamma}"
GPU="${GPU:-1}"
DEVICE="${DEVICE:-cuda}"
DIMENSIONS="${DIMENSIONS:-1 2 3 4 5 6 7 8 9 10 12 14 16 20 24 28 32 36 40}"

mkdir -p "${ROOT}"

GPU="${GPU}" CUDA_VISIBLE_DEVICES="${GPU}" nohup "${PYTHON}" -m run_scripts.run_multidim_ablation \
  --root "${ROOT}" \
  --dimensions ${DIMENSIONS} \
  --plot-dimensions ${DIMENSIONS} \
  --pyramidal-module tfidf-multidim \
  --alpha-prior gamma \
  --synergy-dimensions 1 \
  --device "${DEVICE}" \
  "$@" \
  > "${ROOT}/nohup.log" 2>&1 &

echo "tfidf-multidim ablation (gamma alpha) started on GPU ${GPU}: pid $!"
echo "  root: ${ROOT}"
echo "  tail -f ${ROOT}/run.log"
