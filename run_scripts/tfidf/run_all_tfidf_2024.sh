#!/usr/bin/env bash
# Run the cumulative TF-IDF variant for both the single-dimension and
# multidimensional pyramidal families, on all-2024, end-to-end (Stage 1 ->
# Stage 2 -> synergy -> evaluate).
#
# Each inner runner derives its own tiered output ROOT for cumulative-difficulty.
#
# Usage:
#   bash run_scripts/tfidf/run_all_tfidf_2024.sh
#   GPU=1 bash run_scripts/tfidf/run_all_tfidf_2024.sh          # pick a device
#   DIMS="single" bash run_scripts/tfidf/run_all_tfidf_2024.sh  # single|multi|both
#
# Common overrides (forwarded to the inner runners via the environment):
#   GPU, PYRAMIDAL_STEPS, BONUS_STEPS, DIMENSIONS, LR, RUN_SYNERGY,
#   TFIDF_EFFECT_PRIOR_SCALE, CALIBRATE_CORRECTNESS, ...
set -euo pipefail

cd "$(dirname "$0")/../.."

DIMS="${DIMS:-both}"   # single | multi | both

single_runner="run_scripts/tfidf/run_tfidf_compirt_2024.sh"
multi_runner="run_scripts/tfidf/run_tfidf_multidim_compirt_2024.sh"

run_one() {
  local runner="$1" label="$2"
  echo
  echo "=================================================================="
  echo ">>> ${label}: cumulative TF-IDF"
  echo "=================================================================="
  bash "$runner"
}

if [[ "$DIMS" == "single" || "$DIMS" == "both" ]]; then
  run_one "$single_runner" "single-dim"
fi
if [[ "$DIMS" == "multi" || "$DIMS" == "both" ]]; then
  run_one "$multi_runner" "multidim"
fi

echo
echo "All requested TF-IDF runs complete. Outputs under results/compirt/in_sample/."
