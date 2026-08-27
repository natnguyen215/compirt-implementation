# Double-difficulty holdout results

These runs fit separate position curves for correctness and buzz hazard. They
use frozen five-fold matrix infill on whole games: train on four folds, freeze
the fitted parameters, replay the held-out fold, and evaluate. Held-out data do
not update player or question parameters.

Unless a folder says otherwise, runs share `base_split=year_2024`, split seed
42, optimization seed 42, 3,000 SVI steps, lr 0.005, and 5/5 complete folds.

## Index

| Contents | Location |
| --- | --- |
| Reference configuration | [`ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/`](ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/) |
| Double- versus single-difficulty comparison | [`model-comparisons/double-vs-single-difficulty/aggregate/comparison.md`](model-comparisons/double-vs-single-difficulty/aggregate/comparison.md) |
| Curve-family comparison | [`model-comparisons/curve-family/`](model-comparisons/curve-family/) |
| Degree, dimension, and prior grid | [`ablations/hyperparameter-grid/aggregate/summary.md`](ablations/hyperparameter-grid/aggregate/summary.md) |
| Per-run metrics | `<run>/aggregate/pooled.csv` and `<run>/aggregate/fold_mean_std.csv` |
| Interpretation | [`RESEARCH_LOG.md`](../../../../RESEARCH_LOG.md), Sections 3.1–3.11 |

## Layout

```
ablations/                  configuration changes to one fixed model form
  relevance-locations-terminal/  relevance parameterization x learned locations
                                 x terminal intercepts -- read together, so
                                 grouped. Seven runs, each named for its own
                                 settings; the reference configuration is
                                 dd-bernstein-332-simplex-locations-terminal/.
  optimization-steps/            steps-6000/ and steps-20000/ (reference is 3,000)
  incorrect-loss-weight/         weight-1.5 | weight-2 | weight-3 (reference is 1x)
  hyperparameter-grid/           100-point sweep: degree 3-6 x dim 1-5 x
                                 drop-concentration 0.67-2.0. Ignored by git;
                                 its 3/3/2 cell is tracked in the group above.
model-comparisons/          model families evaluated side by side
  double-vs-single-difficulty/   double vs single curve (4 arms + comparison.md)
  curve-family/                  sigmoid | linear-spline |
                                 monotone-linear-spline (its Bernstein arm is
                                 ablations/.../dd-bernstein-332-unconstrained-terminal/)
  compact-parameterization/      scalar-projection compact model vs full 3/3/2
variants/                   structural model changes
  perceived-difficulty/          6 arms
  perceived-logit/               2 arms
  player-neg-propensity/         hierarchical per-player neg propensity
2023-2025-season/           same model, different data
  season-2023-25/                2023-25 data; not comparable with 2024 runs
```

### Reading a single run

```
<run>/
  configuration.json    every setting used
  aggregate/
    pooled.csv          metrics pooled across folds
    fold_mean_std.csv   per-metric mean and sd across folds
    per_fold.csv        one row per fold
    correctness_metrics.md
  fold_{0..4}/
    train/pyramidal/    the fitted model for that fold
    holdout/pyramidal/  frozen replay on the held-out fold (predictions, no refit)
    evaluation/         experiment_report.md, csvs/, graphs/
```

Some runners add a `seed_42/` or `degree_3/curves_3/dirichlet_2/` directory
above the folds. Resume markers depend on this layout.

## Results at a glance

Values are pooled over the five held-out folds. Lower is better for log loss,
ECE, and MAE; higher is better for accuracy. The always-correct accuracy
baseline is 0.7670.

| run | joint event LL | correctness LL | ECE | accuracy | position MAE |
| --- | ---: | ---: | ---: | ---: | ---: |
| [`dd-bernstein-332-simplex-locations-terminal`](ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/) (Bernstein 3/3/2, simplex, locations, terminal) | 6.6124 | 0.4878 | 0.0098 | 0.7795 | 0.1519 |
| [`steps-6000`](ablations/optimization-steps/steps-6000/) | 6.5032 | 0.4885 | 0.0079 | 0.7789 | 0.1440 |
| [`steps-20000`](ablations/optimization-steps/steps-20000/) | 6.4463 | 0.4888 | 0.0063 | 0.7793 | 0.1392 |
| [`dd-bernstein-332-gamma-locations-terminal`](ablations/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/) | 6.4065 | 0.4977 | 0.0424 | 0.7770 | 0.1356 |
| [`dd-bernstein-330p67-simplex-locations-terminal`](ablations/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/) | 6.6091 | 0.4873 | 0.0070 | 0.7794 | 0.1494 |
| [`incorrect-weight-1.5`](ablations/incorrect-loss-weight/weight-1.5/) | 6.6191 | 0.4991 | 0.0604 | 0.7720 | 0.1518 |
| [`incorrect-weight-2`](ablations/incorrect-loss-weight/weight-2/) | 6.6441 | 0.5256 | 0.1128 | 0.7489 | 0.1517 |
| [`incorrect-weight-3`](ablations/incorrect-loss-weight/weight-3/) | 6.7070 | 0.5880 | 0.1870 | 0.6907 | 0.1517 |
| [`dd-bernstein-332-simplex-terminal`](ablations/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/) (no learned locations) | 6.7217 | 0.5021 | 0.0702 | 0.7731 | 0.1667 |
| [`dd-bernstein-332-simplex`](ablations/relevance-locations-terminal/dd-bernstein-332-simplex/) (no learned locations) | 6.7445 | 0.5025 | 0.0669 | 0.7716 | 0.1783 |
| [`curve-family/sigmoid`](model-comparisons/curve-family/sigmoid/) | 6.6769 | 0.5470 | 0.1091 | 0.7243 | 0.1566 |
| [`player-neg-propensity`](variants/player-neg-propensity/) | 6.5831 | 0.4877 | 0.0112 | 0.7795 | 0.1511 |
| [`perceived-difficulty/unconstrained`](variants/perceived-difficulty/unconstrained/) | 7.6181 | 0.5166 | 0.0332 | 0.7683 | 0.3277 |
| [`perceived-difficulty/positive-alpha`](variants/perceived-difficulty/positive-alpha/) | 6.6375 | 0.6360 | 0.2022 | 0.6487 | 0.1363 |
| [`perceived-difficulty/three-slice`](variants/perceived-difficulty/three-slice/) | 6.8076 | 0.7050 | 0.2584 | 0.5858 | 0.1383 |
| [`perceived-difficulty/three-slice-10000`](variants/perceived-difficulty/three-slice-10000-steps/) | 6.7307 | 0.6389 | 0.2000 | 0.6548 | 0.1389 |
| [`perceived-difficulty/three-slice-alternating`](variants/perceived-difficulty/three-slice-alternating/) | 6.8625 | 0.7337 | 0.2823 | 0.5504 | 0.1392 |
| [`perceived-difficulty/three-slice-alternating-10000`](variants/perceived-difficulty/three-slice-alternating-10000-steps/) | 6.7658 | 0.6612 | 0.2206 | 0.6286 | 0.1389 |
| [`perceived-logit/unconstrained`](variants/perceived-logit/unconstrained/) | 7.7777 | 0.6080 | 0.1049 | 0.7665 | 0.3418 |
| [`perceived-logit/positive-alpha`](variants/perceived-logit/positive-alpha/) | 6.7591 | 0.7876 | 0.3458 | 0.3758 | 0.1376 |
| [`season-2023-25`](2023-2025-season/season-2023-25/) (different population) | 5.5353 | 0.4934 | 0.0143 | 0.7741 | 0.1588 |

The two `dd-bernstein-332-unconstrained*` runs are absent from this table: no
pooled aggregate was computed for them, only fold-level metrics. Their
unweighted fold means are the `DD-Bernstein 3/3/2` rows of the
[`RESEARCH_LOG.md`](../../../../RESEARCH_LOG.md) main table, which uses that
basis throughout and so is the place to compare all nine on equal footing.

Other model-comparison runs use grid- or seed-nested layouts. Their aggregate
reports, along with the compact and linear-spline comparisons, are in
[`results/compirt/holdout/aggregate_correctness_metrics.md`](../aggregate_correctness_metrics.md)
and [`docs/dd-linear-spline-vs-bernstein-3-3-2.md`](../../../../docs/dd-linear-spline-vs-bernstein-3-3-2.md).

## Limitations

- Every run uses optimization seed 42. Small differences may reflect
  initialization noise.
- Joint event log loss continues to improve beyond 3,000 steps. Comparisons at
  3,000 steps control the budget but do not represent converged fits.
- The 2023–25 split has a different event population and is not comparable with
  the 2024 runs.
- The hyperparameter grid predates the simplex relevance prior, so its points
  use the older unconstrained relevance and are not directly comparable with
  the simplex runs. Only its `degree_3/curves_3/dirichlet_2` point is tracked
  in git, as `ablations/relevance-locations-terminal/dd-bernstein-332-unconstrained/`;
  the other 99 are ignored as regenerable.
- The seven runs in `ablations/relevance-locations-terminal/` add one setting
  at a time, so only adjacent rows of that group's table are one-factor
  comparisons. In particular the two `-simplex` runs have no learned curve
  locations, so neither is one factor away from
  `dd-bernstein-332-simplex-locations-terminal/`.
- These are held-out estimates. The in-sample counterparts live under
  [`results/compirt/in_sample/double-difficulty/`](../../in_sample/double-difficulty/)
  and are diagnostic only.
