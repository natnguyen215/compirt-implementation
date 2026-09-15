#!/bin/bash
set -euo pipefail
cd /teapot/students/natnguyen/CompIRT-Implementation
exec /teapot/students/natnguyen/CompIRT-Implementation/.venv/bin/python -B -u -m run_scripts.common.run_parallel_game_holdout --root /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/parallel-normalized-v1-20260913-150350 --dd-root /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350 --bonus-root /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350 --multidim-root /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/multidim-normalized-v1-20260913-150350 --gpus 0 1 --jobs-per-gpu 2 --cpu-jobs 2
