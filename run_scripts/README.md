# Experiment runners

Run commands from the repository root. Keep reusable orchestration here; select
seeds, dimensions, datasets, calibration, and output directories through a
runner's settings instead of adding a script per experiment.

## Choose a runner

| Task | Entry point |
| --- | --- |
| Baseline in-sample training and evaluation | `common/run_compirt.py` |
| Temporal holdout (`MODEL=baseline` or `multidim`) | `common/run_compirt_holdout.py` |
| Whole-game frozen cross-validation | `common/run_compirt_game_holdout.py` |
| DD-Bernstein + multidim five folds on shared GPUs | `common/run_parallel_game_holdout.py` |
| Bonus models from saved Stage-1 folds | `common/run_compositional_from_folds.py` |
| No-synergy vs synergy metric deltas | `common/run_synergy_comparison.py` |
| DD-Bernstein 3/3/2 frozen folds | `double_difficulty/run_dd_bernstein_332.py` |
| DD-Bernstein hyperparameter grid | `double_difficulty/run_dd_bernstein_ablation.py` |
| Perceived-difficulty and perceived-logit 3/3/2 folds | `double_difficulty/run_perceived_*_332.py` |
| Perception dimension sweeps | `double_difficulty/run_perception_dimension_ablation{,_parallel}.py` |
| Repository checks | `common/check_repo.py` |

`run_dd_bernstein_ablation.py` also holds the fold configuration, command, and
pooling helpers the other double-difficulty runners import.
`double_difficulty/evaluate_fold.py` scores one frozen fold for all of them, and
`common/lib/gpu_queue.py` is the shared GPU scheduler.

`run_compirt.py`, `run_compirt_holdout.py`, and `run_compirt_game_holdout.py`
read environment variables documented in their source and have no `--help`.
The other runners take CLI arguments; use `--help`.

## Common commands

```bash
# Baseline in-sample fit and evaluation; RUN_SYNERGY=1 adds the synergy branch.
TOURNAMENT= ROOT=results/compirt/in_sample/baseline/<run> \
  .venv/bin/python run_scripts/common/run_compirt.py

# Temporal holdout with synergy.
MODEL=multidim RUN_SYNERGY=1 \
  .venv/bin/python -m run_scripts.common.run_compirt_holdout
```

Use `ROOT` to give each experiment its own output directory.

## Bonus stage from saved folds

To add compositional bonuses to the saved DD-Bernstein model with learned curve
locations, terminal intercepts, and simplex relevance:

```bash
.venv/bin/python -m run_scripts.common.run_compositional_from_folds \
  --stage1-root results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal \
  --root results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal
```

This reuses the source folds' player skills and split definitions, then fits
both the base bonus model and rank-one synergy with the shared
`compositional_model.py`. Positive Gamma bonus discrimination matches this
Stage-1 skill basis; the Stage-1 simplex is a tossup relevance constraint.
Defaults are 2,000 bonus steps, learning rate 0.01, seed 42, and CUDA. Use
`--alpha-prior normal` for a signed Stage-1 basis, `--arms compositional` for
the base model alone, or `--collect-only` to rebuild the aggregate reports.
Source hashes and configuration are checked on resume. Each fold's split comes
from its saved Stage-1 summary, and the runner checks that bonus test games occur
in neither the Stage-1 nor the bonus training predictions. Results and fold
variation are written to `aggregate/`; each fold retains predictions, training
logs, posterior quantiles, calibration figures, and train/test coverage checks.

Refresh completed bonus folds without fitting or replaying predictions:

```bash
.venv/bin/python -m run_scripts.common.run_compositional_from_folds \
  --root results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350 \
  --evaluate-only
```

Evaluation-only and collect-only use the saved configuration and verify the
source artifact hashes; they allow updated evaluation code. Each fold gets
`experiment_report.md`, parameter distributions in `graphs/parameters/`, and
evaluated aggregate ability and synergy distributions in `graphs/bonus/`.
The root bonus trainer always saves synergy profiles when synergy is enabled;
`--save-synergy-details` additionally exports observed pairs and roster summaries.

## Shared GPU queue for DD and multidimensional folds

The parallel runner preserves DD-Bernstein simplex relevance, learned locations,
terminal intercepts, rank-one Gamma-prior DD bonuses, and the historical
five-dimensional sigmoid comparator with rank-three synergy. All five folds
use frozen prediction. Settings such as steps, learning rates, seeds, dimensions,
and GPU concurrency are CLI options; inspect `--help` for the full list.

```bash
TAG="normalized-v1-$(date +%Y%m%d-%H%M%S)"
QUEUE_ROOT="results/compirt/holdout/common/parallel-$TAG"
mkdir -p "$QUEUE_ROOT"
nohup .venv/bin/python -B -u -m run_scripts.common.run_parallel_game_holdout \
  --root "$QUEUE_ROOT" \
  --dd-root "results/compirt/holdout/double-difficulty/dd-332-$TAG" \
  --bonus-root "results/compirt/holdout/double-difficulty/bonuses-$TAG" \
  --multidim-root "results/compirt/holdout/multidim/multidim-$TAG" \
  --gpus 0 1 --jobs-per-gpu 2 --cpu-jobs 2 \
  > "$QUEUE_ROOT/nohup.log" 2>&1 < /dev/null &
echo $! > "$QUEUE_ROOT/scheduler.pid"
```

Training and GPU replay take the next available slot on the least occupied GPU.
Reports use separate CPU workers. Two jobs per GPU can overlap CPU work in SVI;
use `--jobs-per-gpu 1` if individual fits consume most of a GPU's memory. The
runner sets single-thread BLAS/OpenMP and `COMPIRT_SURVIVAL_CHUNK=2048` by
default. GPU IDs are physical CUDA indexes; each worker sees its assigned GPU
as `cuda:0`.

`queue.json` records commands, dependencies, environment, and source hashes;
`status.json` records running PIDs, GPU assignments, failures, and completions.
`logs/` contains one append-only log per task. Resume with the **same command
and all four roots**; keep the original `TAG`. Completed tasks are skipped only
after successful exits and output checks. Configuration or source changes
require fresh roots. A run lock prevents two schedulers from sharing a queue.
`kill -TERM "$(cat "$QUEUE_ROOT/scheduler.pid")"` stops the scheduler and its
workers; unfinished fits restart on resume. Failed tasks block their dependents
while independent work continues.

The bonus runner's `--prepare-only`, `--worker-fold`, `--worker-arm`, and
`--worker-stage` options support this scheduler; a worker requires the prepared
manifest and never aggregates shared outputs.

## Retired runners

Runners for finished experiments are deleted rather than kept; recover one
from git history if it is needed again. Code for completed evaluation studies
sits in a `code/` folder beside its results (listed in
[`../results/README.md`](../results/README.md)). Runners for archived model
families are under `../archive/run_scripts/`.
