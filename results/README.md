# Experiment results

Saved runs are kept in the repository as the record of the paper's experiments.

## Layout

```
results/
  compirt/
    in_sample/<family>/<run>/     fitted and evaluated on the same split
    holdout/<family>/<run>/       trained on one split, evaluated on another
    comparisons/                  cross-run reports that span many runs
  ranking_comparison/<run>/       fitted player rankings vs observed scoring
```

- `compirt/in_sample/` — fit diagnostics, not generalization estimates.
- `compirt/holdout/` — temporal, game-infill, and fold workflows. Read each
  run's summary: the temporal holdout fits test-period parameters under
  transferred player priors, while the fold runners are frozen matrix infill.
- `compirt/comparisons/` — `parameter_comparison.md` and
  `synergy_bonus_model_comparison.md`, which span both tiers.
- `ranking_comparison/` — fitted player rankings against observed tournament
  scoring; not a CompIRT run root.

Runners resolve output roots through `utils.run_logging.resolve_result_root`,
which redirects a bare `results/compirt/<name>` into the runner's tier.

## Families

Within each tier, runs are grouped by model family: `baseline/`, `multidim/`,
`double-difficulty/`, and results from families whose code is now under
`archive/` (`topic/`, `tfidf/`, `embedding/`, `frozen-skills/`). Two kinds of
directory are not families:

- `common/` — studies that span families or ask about the data.
  `in_sample/common/` holds the drop-robustness study and the 2024 Nationals
  comparison fits; [`holdout/common/`](compirt/holdout/common/README.md) has its
  own index.
- `in_sample/polynomial/` and `in_sample/test_additions/` — scratch tracks,
  ignored by git along with their source under `archive/`.

A two-stage run root contains `pyramidal/`, `compositional/`, optional
`synergy/`, their evaluation directories, and an optional `comparison/`. Fold
and sweep runners nest further (`<arm>/seed_N/fold_K/`, or
`degree_D/curves_C/dirichlet_A/fold_K/`).

[`holdout/double-difficulty/`](compirt/holdout/double-difficulty/README.md) is
grouped one level deeper, by the question each run answers (`ablations/`,
`model-comparisons/`, `variants/`, `2023-2025-season/`), and has its own index.

i## Naming

Leaf names mix historical styles (`all-2024`, `all2024`) and are not renamed,
because a leaf name is part of the run's provenance. The directories above the
leaves have been reorganized, so `Result root:` lines in older
`evaluation/docs/summary.md` files may name a previous location.

`holdout/double-difficulty/` is the exception: its runs were renamed, and their
recorded paths (`configuration.json`, `command.json`, `.complete.json` resume
markers, and `Result root:` lines) were rewritten to match, so resume still
works there. New runs should use the names emitted by the current runners.

## Code kept beside results

Completed studies keep the code that produced them beside their results:

- `in_sample/common/drop-robustness/code/`
- `in_sample/multidim/multidim-all2024/code/` (posterior predictive checks and
  match simulation)
- `in_sample/multidim/multidim-all2024/compirt_eval/parameter-recovery/code/`
- `in_sample/multidim/multidim-all2024-cal/imaginary-tournament/code/`
- `holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/code/`
- `holdout/common/token-threshold-replay/2026-09-13/replay_research_log_outcomes.py`
- `ranking_comparison/code/`

This code is a record. It is not imported or checked, its imports and READMEs
name its original locations (for example `compirt_eval.drop_robustness` and
`run_scripts/common/`), and some helpers it used have been deleted. Copy it back
and restore those helpers from git history before rerunning it.

Prediction CSVs, posterior draws, and plots from new runs may be ignored by git
even where older artifacts are tracked.
