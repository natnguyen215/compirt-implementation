# Experiment Results

Result directories are retained in this repository because they record the
paper's experiment history.

## Layout

```
results/
  compirt/
    in_sample/<family>/<run>/     fitted and evaluated on the same split
    holdout/<family>/<run>/       trained on one split, evaluated on another
    comparisons/                  cross-run reports that span many runs
  ranking_comparison/<run>/       fitted player rankings vs observed scoring
```

- `compirt/in_sample/` — the model is fitted and evaluated on the selected
  split. These are fit diagnostics, not generalization estimates.
- `compirt/holdout/` — temporal, game-infill, and fold workflows that train on
  one set of rows and evaluate another. Read each run's summary: the temporal
  holdout is player-prior transfer with test-period parameter fitting, not a
  strict unseen-question holdout, while the fold runners are frozen matrix
  infill.
- `compirt/comparisons/` — reports that compare many runs at once
  (`parameter_comparison.md`, `synergy_bonus_model_comparison.md`). They span
  both tiers, so they sit beside them rather than inside one.
- `ranking_comparison/` — comparisons between fitted player rankings and
  observed tournament scoring. Not a CompIRT run root, so it stays outside
  `compirt/`.

Every runner resolves its output root through `resolve_result_root`
(`utils.run_logging` for Python, `run_scripts/common/lib/result_root.sh` for
shell), which forces outputs into a tier and redirects a bare
`results/compirt/<name>`.

## The family level

Inside each tier, runs are grouped by model family: `baseline/`, `multidim/`,
`topic/`, `tfidf/`, `embedding/`, `double-difficulty/`. Two directories are not
families:

- `common/` — studies that span families rather than belonging to one
  (`in_sample/common/drop-robustness`, `holdout/common/neg-test`).
- `polynomial/` and `test_additions/` under `in_sample/` — scratch tracks,
  ignored by git along with their source packages.

A normal two-stage run root contains `pyramidal/`, `compositional/`, optional
`synergy/`, their evaluation directories, and an optional `comparison/`. Fold
and sweep runners nest further (`<arm>/seed_N/fold_K/`, or the ablation grid's
`degree_D/curves_C/dirichlet_A/fold_K/`).

`holdout/double-difficulty/` is the one family grouped a level deeper, by the
*question* each run answers rather than as a flat list of runs:
`ablations/`, `model-comparisons/`, `variants/`, `2023-2025-season/`. It has
enough runs that a flat listing stopped being navigable. The reference
configuration is not a top-level folder: it lives in
`ablations/simplex-locations-terminal/reference/`, alongside the runs that vary
the relevance prior, the learned curve locations, and the terminal intercepts,
because those three settings are interrelated and are read together. See
[`holdout/double-difficulty/README.md`](compirt/holdout/double-difficulty/README.md)
for the index.

## Naming

Run leaf names use several historical styles (`all-2024` and `all2024`, for
example). They are intentionally not renamed: a leaf name is part of the
recorded experiment provenance, and the `Result root:` lines inside each run's
`evaluation/docs/summary.md` record the path the run was written to. Only the
directory *structure* above them has been normalized, so those recorded paths
may name an older location for the same run.

`holdout/double-difficulty/` is the exception: its run leaves *were* renamed
from encoded settings (`dd-bernstein-332-simplex-locations-terminal`,
`matrix-infill`) to what each run answers
(`ablations/simplex-locations-terminal/reference`,
`model-comparisons/double-vs-single-difficulty`). Every recorded path inside
those runs — `configuration.json`, `command.json`, the `.complete.json` resume
markers, and the `Result root:` lines — was rewritten to match, so the runners'
resume logic still works and the reports stay self-consistent. The settings
those old names encoded are in each run's `configuration.json`.

New work should follow the names emitted by the current runners.

Generated prediction CSVs, posterior draws, and plots may be ignored for new
runs even when older paper artifacts remain tracked.
