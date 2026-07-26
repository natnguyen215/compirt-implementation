#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/common/lib/result_root.sh"

PYTHON="${PYTHON:-.venv/bin/python}"
GPU="${GPU:-0}"
DEVICE="${DEVICE:-cuda}"
DIMENSIONS="${DIMENSIONS:-5}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
LR="${LR:-0.01}"
TOURNAMENT="${TOURNAMENT-}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
SPLIT="${SPLIT:-year_2024}"
TRAIN_SPLIT="${TRAIN_SPLIT:-year_2024}"
TEST_SPLIT="${TEST_SPLIT:-year_2025}"
NEW_PLAYER_PRIOR="${NEW_PLAYER_PRIOR:-tier}"

INSAMPLE_NO_CAL_ROOT="$(resolve_result_root "${INSAMPLE_NO_CAL_ROOT:-results/compirt/in_sample/multidim/multidim-all2024}" in_sample)"
INSAMPLE_CAL_ROOT="$(resolve_result_root "${INSAMPLE_CAL_ROOT:-results/compirt/in_sample/multidim/multidim-all2024-cal}" in_sample)"
HOLDOUT_NO_CAL_ROOT="$(resolve_result_root "${HOLDOUT_NO_CAL_ROOT:-results/compirt/holdout/multidim/multidim-all2024}" holdout)"
HOLDOUT_CAL_ROOT="$(resolve_result_root "${HOLDOUT_CAL_ROOT:-results/compirt/holdout/multidim/multidim-all2024-cal}" holdout)"

export PYTHON
export GPU
export DEVICE
export DIMENSIONS
export SYNERGY_DIMENSIONS
export PYRAMIDAL_STEPS
export BONUS_STEPS
export LR
export TOURNAMENT
export SAVE_SYNERGY_DETAILS
export SPLIT
export TRAIN_SPLIT
export TEST_SPLIT
export NEW_PLAYER_PRIOR

echo "Running multidim CompIRT in-sample jobs with synergy..."
NO_CAL_ROOT="$INSAMPLE_NO_CAL_ROOT" \
CAL_ROOT="$INSAMPLE_CAL_ROOT" \
  ./run_scripts/multidimensional/multidim/run_multidim_all2024.sh

echo
echo "Running multidim CompIRT held-out jobs with synergy..."
NO_CAL_ROOT="$HOLDOUT_NO_CAL_ROOT" \
CAL_ROOT="$HOLDOUT_CAL_ROOT" \
  ./run_scripts/multidimensional/multidim/run_multidim_holdout.sh

echo
echo "Finished all multidim CompIRT synergy runs:"
echo "  in-sample no calibration: $INSAMPLE_NO_CAL_ROOT/synergy-evaluation/experiment_report.md"
echo "  in-sample calibration:    $INSAMPLE_CAL_ROOT/synergy-evaluation/experiment_report.md"
echo "  held-out no calibration:  $HOLDOUT_NO_CAL_ROOT/holdout/synergy-evaluation/experiment_report.md"
echo "  held-out calibration:     $HOLDOUT_CAL_ROOT/holdout/synergy-evaluation/experiment_report.md"
