#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PYTHON="${PYTHON:-.venv/bin/python}"
GPU="${GPU:-0}"
DEVICE="${DEVICE:-cuda}"
DIMENSIONS="${DIMENSIONS:-5}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
LR="${LR:-0.01}"
TOURNAMENT="${TOURNAMENT-}"
PREDICT_BUZZ_POSITIONS="${PREDICT_BUZZ_POSITIONS:-1}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
SPLIT="${SPLIT:-year_2024}"
TRAIN_SPLIT="${TRAIN_SPLIT:-year_2024}"
TEST_SPLIT="${TEST_SPLIT:-year_2025}"
NEW_PLAYER_PRIOR="${NEW_PLAYER_PRIOR:-tier}"

INSAMPLE_NO_CAL_ROOT="${INSAMPLE_NO_CAL_ROOT:-results/compirt/in_sample/multidim-all2024}"
INSAMPLE_CAL_ROOT="${INSAMPLE_CAL_ROOT:-results/compirt/in_sample/multidim-all2024-cal}"
HOLDOUT_NO_CAL_ROOT="${HOLDOUT_NO_CAL_ROOT:-results/compirt/holdout/multidim-all2024}"
HOLDOUT_CAL_ROOT="${HOLDOUT_CAL_ROOT:-results/compirt/holdout/multidim-all2024-cal}"

export PYTHON
export GPU
export DEVICE
export DIMENSIONS
export SYNERGY_DIMENSIONS
export PYRAMIDAL_STEPS
export BONUS_STEPS
export LR
export TOURNAMENT
export PREDICT_BUZZ_POSITIONS
export SAVE_SYNERGY_DETAILS
export SPLIT
export TRAIN_SPLIT
export TEST_SPLIT
export NEW_PLAYER_PRIOR

echo "Running multidim CompIRT in-sample jobs with synergy..."
NO_CAL_ROOT="$INSAMPLE_NO_CAL_ROOT" \
CAL_ROOT="$INSAMPLE_CAL_ROOT" \
  ./run_scripts/run_multidim_all2024.sh

echo
echo "Running multidim CompIRT held-out jobs with synergy..."
NO_CAL_ROOT="$HOLDOUT_NO_CAL_ROOT" \
CAL_ROOT="$HOLDOUT_CAL_ROOT" \
  ./run_scripts/run_multidim_holdout.sh

echo
echo "Finished all multidim CompIRT synergy runs:"
echo "  in-sample no calibration: $INSAMPLE_NO_CAL_ROOT/synergy-evaluation/experiment_report.md"
echo "  in-sample calibration:    $INSAMPLE_CAL_ROOT/synergy-evaluation/experiment_report.md"
echo "  held-out no calibration:  $HOLDOUT_NO_CAL_ROOT/holdout/synergy-evaluation/experiment_report.md"
echo "  held-out calibration:     $HOLDOUT_CAL_ROOT/holdout/synergy-evaluation/experiment_report.md"
