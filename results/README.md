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
`model-comparisons/`, `variants/`, `likelihood-refits/`, `compositional/`,
`2023-2025-season/`), and has its own index.

The [shared bonus comparison](compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md)
is the current results entry point: DD-Bernstein, multidimensional references,
and Team IRT 1D and 3D on identical games. The
[bonus research log](../RESEARCH_LOG_2.md) contains their joint summary.

The [2024–25 full-season bonus fits](compirt/in_sample/common/bonus-difficulty-season-2024-25/README.md)
check easy/medium/hard parameter ordering within bonuses and tournament
difficulty ordering across Fall, Winter, Regionals, and Nationals. They are
in-sample parameter diagnostics; the research log retains the original
calendar-2024 held-out classification comparison.

The [compositional bonus index](compirt/holdout/double-difficulty/compositional/README.md)
links each saved bonus configuration, fold report, and pooled comparison, and
documents the training → frozen replay → evaluation → pooling flow.

## Naming

Name runs by their model and configuration, without launch dates or timestamps.
List the modifications that distinguish the run: relevance prior, learned
locations, terminal intercepts, likelihood, synergy form/link/dimensions,
training steps when they vary between runs, and fold coverage. Shared bonus
training budgets belong in metadata. Parent directories supply
the family and evaluation regime. Dataset years such as `all2024` and
`2023-2025-season` describe the population and remain in the names.

For example, `dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps`
identifies a Stage-1 run. Here `332` means Bernstein degree 3, skill
dimensions 3, and drop concentration 2. The `normalized-first-buzz` suffix
identifies a refit using the corrected probability law for the first buzzer
and dead tossups; `3000steps` stays because sibling refits use 10,000 steps.
Bonus runs under `double-difficulty/compositional/` all use those skills,
3,000 steps, and five folds, so their names carry only the bonus
configuration: `phi-psi-multiplicative-3d` is the synergy form, link, and
dimensions. The metadata value `normalized_hazard_odds_v1` names that
likelihood.

Run dates remain in metadata and research notes. When renaming a run, update
saved paths, completion markers, dependent metadata hashes, commands, and
report links together. Give each configuration and training copy its own
directory, choosing a new name when a descriptive one is taken.

## Code kept beside results

Compositional analysis scripts live in
[`analysis/compositional/`](../analysis/README.md#saved-compositional-analyses);
their results folders contain reports and saved artifacts.

Some historical studies retain code snapshots beside their results:

- `in_sample/common/drop-robustness/code/`
- `in_sample/multidim/multidim-all2024/code/` (posterior predictive checks and
  match simulation)
- `in_sample/multidim/multidim-all2024/compirt_eval/parameter-recovery/code/`
- `in_sample/multidim/multidim-all2024-cal/imaginary-tournament/code/`
- `holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/replay_research_log_outcomes.py`
- `holdout/common/bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold/identifiability/code/`
  (Team IRT 3D identifiability refits and analysis)
- `comparisons/bonuses/dd-bernstein-and-team-irt-5fold/code/` (Team IRT rescoring)
- `ranking_comparison/code/`

This code is a record. It is not imported or checked, its imports and READMEs
name its original locations (for example `compirt_eval.drop_robustness` and
`run_scripts/common/`), and some helpers it used have been deleted. Copy it back
and restore those helpers from git history before rerunning it.

Prediction CSVs, posterior draws, and plots from new runs may be ignored by git
even where older artifacts are tracked.
