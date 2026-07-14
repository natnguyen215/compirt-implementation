#!/usr/bin/env bash
# Held-out multidim dimension ablation out to m = 40, with the Gamma(2, 2)
# bonus-part alpha prior that matches the multidim pyramidal relevance vector.
# Detaches under nohup on GPU 0 and prints the pid.
#
# Writes to its own root: the existing multidim-ablation/ runs were fit with the
# Normal alpha prior, and the runner resumes off marker files, so reusing that
# root would mix priors within one sweep.
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON="${PYTHON:-.venv/bin/python}"
ROOT="${ROOT:-results/compirt/holdout/multidim-ablation-gamma}"
GPU="${GPU:-0}"
DEVICE="${DEVICE:-cuda}"
DIMENSIONS="${DIMENSIONS:-1 2 3 4 5 6 7 8 9 10 12 14 16 20 24 28 32 36 40}"

mkdir -p "${ROOT}"

# The runner already tees its own run.log inside ROOT; this only catches anything
# written before that tee is installed (e.g. an early crash).
GPU="${GPU}" CUDA_VISIBLE_DEVICES="${GPU}" nohup "${PYTHON}" -m run_scripts.run_multidim_ablation \
  --root "${ROOT}" \
  --dimensions ${DIMENSIONS} \
  --plot-dimensions ${DIMENSIONS} \
  --pyramidal-module multidim \
  --alpha-prior gamma \
  --synergy-dimensions 1 \
  --device "${DEVICE}" \
  "$@" \
  > "${ROOT}/nohup.log" 2>&1 &

echo "multidim ablation (gamma alpha) started on GPU ${GPU}: pid $!"
echo "  root: ${ROOT}"
echo "  tail -f ${ROOT}/run.log"
