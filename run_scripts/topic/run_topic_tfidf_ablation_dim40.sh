#!/usr/bin/env bash
# Held-out learned-topic + TF-IDF topic-count ablation over the same points as
# the multidim sweeps. Stage 1 is topic/tfidf's joint sLDA (Dirichlet r learned
# from words + outcomes, per-topic TF-IDF lambda). Stage 2 uses
# topic.learned.train_joint_compositional, and the evaluator replays the saved
# TF-IDF adjustment curves. Detaches under nohup on GPU 0 and prints the pid.
#
# --dimensions sweeps the topic count K, which this family ties to the IRT skill
# dimensionality.
set -euo pipefail

cd "$(dirname "$0")/../.."

PYTHON="${PYTHON:-.venv/bin/python}"
ROOT="${ROOT:-results/compirt/holdout/topic/topic-tfidf-ablation}"
GPU="${GPU:-0}"
DEVICE="${DEVICE:-cuda}"
BOW_WEIGHT="${BOW_WEIGHT:-0.1}"
DIMENSIONS="${DIMENSIONS:-1 2 3 4 5 6 7 8 9 10 12 14 16 20 24 28 32 36 40}"

mkdir -p "${ROOT}"

GPU="${GPU}" CUDA_VISIBLE_DEVICES="${GPU}" nohup "${PYTHON}" -m run_scripts.topic.run_learned_topic_ablation \
  --root "${ROOT}" \
  --dimensions ${DIMENSIONS} \
  --plot-dimensions ${DIMENSIONS} \
  --pyramidal-module learned-tfidf \
  --bow-weight "${BOW_WEIGHT}" \
  --synergy-dimensions 1 \
  --device "${DEVICE}" \
  "$@" \
  > "${ROOT}/nohup.log" 2>&1 &

echo "topic-tfidf (learned) ablation started on GPU ${GPU}: pid $!"
echo "  bow-weight: ${BOW_WEIGHT}"
echo "  root: ${ROOT}"
echo "  tail -f ${ROOT}/run.log"
