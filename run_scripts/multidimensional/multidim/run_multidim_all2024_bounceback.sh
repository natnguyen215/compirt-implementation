#!/usr/bin/env bash
# Rerun the multidimensional-difficulty CompIRT all-2024 pipeline WITH the
# neg-then-bounceback phase-1 risk set enabled (paper Section 3.1 / Appendix A).
#
# This is run_multidim_all2024.sh with INCLUDE_BOUNCEBACK=1 and its own output
# roots, so the bounceback fit lands next to the baseline all-2024 run for a
# side-by-side comparison rather than overwriting it. Every other knob
# (dimensions, steps, LR, synergy branch, calibration branch) matches the
# stock all-2024 runner and can still be overridden by exporting the same env
# vars documented in run_scripts/multidimensional/multidim/run_multidim_compirt.py.
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$REPO_ROOT"
source "$REPO_ROOT/run_scripts/common/lib/result_root.sh"

PYTHON="${PYTHON:-.venv/bin/python}"
GPU="${GPU:-0}"
SPLIT="${SPLIT:-year_2024}"
TOURNAMENT="${TOURNAMENT-}"
DIMENSIONS="${DIMENSIONS:-5}"
DIFFICULTY_LINK="${DIFFICULTY_LINK:-sigmoid}"
SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
PYRAMIDAL_STEPS="${PYRAMIDAL_STEPS:-3000}"
BONUS_STEPS="${BONUS_STEPS:-2000}"
LR="${LR:-0.01}"
DEVICE="${DEVICE:-cuda}"
SAVE_SYNERGY_DETAILS="${SAVE_SYNERGY_DETAILS:-0}"
NO_CAL_ROOT="$(resolve_result_root "${NO_CAL_ROOT:-results/compirt/in_sample/multidim/multidim-all2024-bounceback}" in_sample)"
CAL_ROOT="$(resolve_result_root "${CAL_ROOT:-results/compirt/in_sample/multidim/multidim-all2024-bounceback-cal}" in_sample)"

run_one () {
  local root="$1"
  local calibrate="$2"
  GPU="$GPU" \
  SPLIT="$SPLIT" \
  TOURNAMENT="$TOURNAMENT" \
  ROOT="$root" \
  DIMENSIONS="$DIMENSIONS" \
  DIFFICULTY_LINK="$DIFFICULTY_LINK" \
  SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
  PYRAMIDAL_STEPS="$PYRAMIDAL_STEPS" \
  BONUS_STEPS="$BONUS_STEPS" \
  LR="$LR" \
  DEVICE="$DEVICE" \
  SAVE_SYNERGY_DETAILS="$SAVE_SYNERGY_DETAILS" \
  INCLUDE_BOUNCEBACK=1 \
  CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/multidimensional/multidim/run_multidim_compirt.py
}

run_one "$NO_CAL_ROOT" 0
run_one "$CAL_ROOT" 1

echo "Finished multidim all-2024 bounceback runs:"
echo "  no calibration: $NO_CAL_ROOT/synergy-evaluation/experiment_report.md"
echo "  calibration:    $CAL_ROOT/synergy-evaluation/experiment_report.md"
