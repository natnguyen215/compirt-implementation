#!/usr/bin/env bash
# Run all three TF-IDF variants (replace-position, cumulative-difficulty,
# hazard-spike) for both the single-dimension and multidimensional pyramidal
# families, on all-2024, end-to-end (Stage 1 -> Stage 2 -> synergy -> evaluate).
#
# Each inner runner derives its own tiered output ROOT from TFIDF_VARIANT:
#   single: results/compirt/in_sample/tfidf-<variant>-all2024
#   multi:  results/compirt/in_sample/tfidf-multidim-<variant>-all2024
#
# Usage:
#   bash run_scripts/run_all_tfidf_2024.sh
#   GPU=1 bash run_scripts/run_all_tfidf_2024.sh          # pick a device
#   VARIANTS="cumulative-difficulty" bash run_scripts/run_all_tfidf_2024.sh
#   DIMS="single" bash run_scripts/run_all_tfidf_2024.sh  # single|multi|both
#
# Common overrides (forwarded to the inner runners via the environment):
#   GPU, PYRAMIDAL_STEPS, BONUS_STEPS, DIMENSIONS, LR, RUN_SYNERGY,
#   TFIDF_EFFECT_PRIOR_SCALE, CALIBRATE_CORRECTNESS, ...
set -euo pipefail

cd "$(dirname "$0")/.."

VARIANTS="${VARIANTS:-replace-position cumulative-difficulty hazard-spike}"
DIMS="${DIMS:-both}"   # single | multi | both

single_runner="run_scripts/run_tfidf_compirt_2024.sh"
multi_runner="run_scripts/run_tfidf_multidim_compirt_2024.sh"

run_one() {
  local runner="$1" variant="$2" label="$3"
  echo
  echo "=================================================================="
  echo ">>> ${label}: TFIDF_VARIANT=${variant}"
  echo "=================================================================="
  TFIDF_VARIANT="$variant" bash "$runner"
}

for variant in $VARIANTS; do
  if [[ "$DIMS" == "single" || "$DIMS" == "both" ]]; then
    run_one "$single_runner" "$variant" "single-dim"
  fi
  if [[ "$DIMS" == "multi" || "$DIMS" == "both" ]]; then
    run_one "$multi_runner" "$variant" "multidim"
  fi
done

echo
echo "All requested TF-IDF runs complete. Outputs under results/compirt/in_sample/."
