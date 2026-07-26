#!/usr/bin/env bash
# Held-out multidim dimension ablation out to m = 40 using the biased-tanh
# difficulty curve
#
#     d_jk(t) = tanh(gamma_jk * (mu_jk - t / T_j) + bias_jk) * scale
#
# (learned per-dim shift bias_jk ~ Normal(0, 1), fixed amplitude scale), with the
# Gamma(2, 2) bonus-part alpha prior that matches the multidim pyramidal relevance
# vector. Detaches under nohup on GPU 0 and prints the pid.
#
# Uses the biased-tanh Stage-1 trainer (--pyramidal-module multidim-tanhbias)
# and a dedicated result root so its checkpoints stay separate from the
# sigmoid and tanh sweeps.
set -euo pipefail

cd "$(dirname "$0")/../../.."

PYTHON="${PYTHON:-.venv/bin/python}"
ROOT="${ROOT:-results/compirt/holdout/multidim/multidim-tanhbias-ablation-gamma}"
GPU="${GPU:-0}"
DEVICE="${DEVICE:-cuda}"
DIMENSIONS="${DIMENSIONS:-1 2 3 4 5 6 7 8 9 10 12 14 16 20 24 28 32 36 40}"
DIFFICULTY_SCALE="${DIFFICULTY_SCALE:-5.0}"

mkdir -p "${ROOT}"

# The runner already tees its own run.log inside ROOT; this only catches anything
# written before that tee is installed (e.g. an early crash).
GPU="${GPU}" CUDA_VISIBLE_DEVICES="${GPU}" nohup "${PYTHON}" -m run_scripts.multidimensional.multidim.run_multidim_ablation \
  --root "${ROOT}" \
  --dimensions ${DIMENSIONS} \
  --plot-dimensions ${DIMENSIONS} \
  --pyramidal-module multidim-tanhbias \
  --difficulty-scale "${DIFFICULTY_SCALE}" \
  --alpha-prior gamma \
  --synergy-dimensions 1 \
  --device "${DEVICE}" \
  "$@" \
  > "${ROOT}/nohup.log" 2>&1 &

echo "multidim tanhbias ablation (gamma alpha) started on GPU ${GPU}: pid $!"
echo "  root: ${ROOT}"
echo "  scale: ${DIFFICULTY_SCALE}"
echo "  tail -f ${ROOT}/run.log"
