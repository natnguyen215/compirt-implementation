# Double-difficulty holdout results

Every run here fits the **double-difficulty** tossup model: correctness and buzz
hazard get their own position curve, instead of sharing one difficulty curve
`b_j(t)`. All runs use the same protocol — **frozen five-fold matrix infill** on
whole games: train on four folds, freeze every fitted parameter, replay the
held-out fold, evaluate. No held-out outcome ever refits a player or a question.

Unless a folder says otherwise, runs share `base_split=year_2024`, split seed
42, optimization seed 42, 3,000 SVI steps, lr 0.005, and 5/5 complete folds.

## Where to start

| I want… | Go to |
| --- | --- |
| the current best model | [`reference-model/`](reference-model/) |
| does splitting the curve help at all? | [`model-comparisons/double-vs-single-difficulty/aggregate/comparison.md`](model-comparisons/double-vs-single-difficulty/aggregate/comparison.md) |
| which curve shape to use | [`model-comparisons/curve-family/`](model-comparisons/curve-family/) |
| the full degree × dimension × prior sweep | [`ablations/hyperparameter-grid/aggregate/summary.md`](ablations/hyperparameter-grid/aggregate/summary.md) |
| one experiment's numbers | that run's `aggregate/pooled.csv` and `aggregate/fold_mean_std.csv` |
| the narrative and verdicts | [`RESEARCH_LOG.md`](../../../../RESEARCH_LOG.md) §3.1–3.11 |

## Layout

```
reference-model/            the configuration everything else is measured against
model-comparisons/          "which model?" — arms meant to be read side by side
  double-vs-single-difficulty/   double vs single curve (4 arms + comparison.md)
  curve-family/                  bernstein-332 | sigmoid | linear-spline |
                                 monotone-linear-spline
  compact-parameterization/      scalar-projection compact model vs full 3/3/2
ablations/                  "does this knob matter?" — one factor changed at a time
  hyperparameter-grid/           100-point sweep: degree 3-6 x dim 1-5 x
                                 concentration 0.67-2.0 (no terminal intercepts)
  terminal-cell-intercepts/      off/ vs on/
  relevance-prior/               gamma-2-2/ and dirichlet-concentration-0.67/
                                 (Dirichlet 2.0 is the reference model)
  optimization-steps/            steps-6000/ and steps-20000/ (reference is 3,000)
  incorrect-loss-weight/         weight-1.5 | weight-2 | weight-3 (reference is 1x)
variants/                   structural changes to the model, not just a setting
  perceived-difficulty/          6 arms
  perceived-logit/               2 arms
  player-neg-propensity/         hierarchical per-player neg propensity
data-splits/                same model, different data
  season-2023-25/                2023-25 instead of 2024 — NOT comparable above
```

### Reading a single run

```
<run>/
  configuration.json    every setting used
  aggregate/
    pooled.csv          headline metrics, all folds pooled  <- start here
    fold_mean_std.csv   per-metric mean and sd across folds
    per_fold.csv        one row per fold
    correctness_metrics.md
  fold_{0..4}/
    train/pyramidal/    the fitted model for that fold
    holdout/pyramidal/  frozen replay on the held-out fold (predictions, no refit)
    evaluation/         experiment_report.md, csvs/, graphs/
```

Some runs keep an extra `seed_42/` or `degree_3/curves_3/dirichlet_2/` layer
above the folds. That is the grid path its runner writes, and the runners' resume
markers depend on it, so it is left in place.

## Results at a glance

Pooled over all five held-out folds, read directly from each run's
`aggregate/pooled.csv`. Lower is better for LL, ECE and MAE; higher for accuracy.
The all-correct accuracy baseline on this population is **0.7670**, so accuracy
below that is worse than always predicting "correct".

| run | joint event LL | correctness LL | ECE | accuracy | position MAE |
| --- | ---: | ---: | ---: | ---: | ---: |
| [`reference-model`](reference-model/) — reference model (Bernstein 3/3/2, simplex, locations, terminal) | 6.6124 | 0.4878 | 0.0098 | 0.7795 | 0.1519 |
| [`ablations/optimization-steps/steps-6000`](ablations/optimization-steps/steps-6000/) — reference @ 6,000 steps | 6.5032 | 0.4885 | 0.0079 | 0.7789 | 0.1440 |
| [`ablations/optimization-steps/steps-20000`](ablations/optimization-steps/steps-20000/) — reference @ 20,000 steps | 6.4463 | 0.4888 | 0.0063 | 0.7793 | 0.1392 |
| [`ablations/relevance-prior/gamma-2-2`](ablations/relevance-prior/gamma-2-2/) — Gamma(2,2) relevance | 6.4065 | 0.4977 | 0.0424 | 0.7770 | 0.1356 |
| [`ablations/relevance-prior/dirichlet-concentration-0.67`](ablations/relevance-prior/dirichlet-concentration-0.67/) — Dirichlet concentration 0.67 | 6.6091 | 0.4873 | 0.0070 | 0.7794 | 0.1494 |
| [`ablations/incorrect-loss-weight/weight-1.5`](ablations/incorrect-loss-weight/weight-1.5/) — incorrect-loss weight 1.5x | 6.6191 | 0.4991 | 0.0604 | 0.7720 | 0.1518 |
| [`ablations/incorrect-loss-weight/weight-2`](ablations/incorrect-loss-weight/weight-2/) — incorrect-loss weight 2x | 6.6441 | 0.5256 | 0.1128 | 0.7489 | 0.1517 |
| [`ablations/incorrect-loss-weight/weight-3`](ablations/incorrect-loss-weight/weight-3/) — incorrect-loss weight 3x | 6.7070 | 0.5880 | 0.1870 | 0.6907 | 0.1517 |
| [`model-comparisons/curve-family/sigmoid`](model-comparisons/curve-family/sigmoid/) — sigmoid curves | 6.6769 | 0.5470 | 0.1091 | 0.7243 | 0.1566 |
| [`variants/player-neg-propensity`](variants/player-neg-propensity/) — + hierarchical player neg propensity | 6.5831 | 0.4877 | 0.0112 | 0.7795 | 0.1511 |
| [`variants/perceived-difficulty/unconstrained`](variants/perceived-difficulty/unconstrained/) — perceived difficulty, unconstrained | 7.6181 | 0.5166 | 0.0332 | 0.7683 | 0.3277 |
| [`variants/perceived-difficulty/positive-alpha`](variants/perceived-difficulty/positive-alpha/) — perceived difficulty, positive alpha | 6.6375 | 0.6360 | 0.2022 | 0.6487 | 0.1363 |
| [`variants/perceived-difficulty/three-slice`](variants/perceived-difficulty/three-slice/) — perceived difficulty, three-slice | 6.8076 | 0.7050 | 0.2584 | 0.5858 | 0.1383 |
| [`variants/perceived-difficulty/three-slice-10000-steps`](variants/perceived-difficulty/three-slice-10000-steps/) — perceived difficulty, three-slice @10k | 6.7307 | 0.6389 | 0.2000 | 0.6548 | 0.1389 |
| [`variants/perceived-difficulty/three-slice-alternating`](variants/perceived-difficulty/three-slice-alternating/) — perceived difficulty, three-slice alternating | 6.8625 | 0.7337 | 0.2823 | 0.5504 | 0.1392 |
| [`variants/perceived-difficulty/three-slice-alternating-10000-steps`](variants/perceived-difficulty/three-slice-alternating-10000-steps/) — perceived difficulty, alternating @10k | 6.7658 | 0.6612 | 0.2206 | 0.6286 | 0.1389 |
| [`variants/perceived-logit/unconstrained`](variants/perceived-logit/unconstrained/) — perceived logit, unconstrained | 7.7777 | 0.6080 | 0.1049 | 0.7665 | 0.3418 |
| [`variants/perceived-logit/positive-alpha`](variants/perceived-logit/positive-alpha/) — perceived logit, positive alpha | 6.7591 | 0.7876 | 0.3458 | 0.3758 | 0.1376 |
| [`data-splits/season-2023-25`](data-splits/season-2023-25/) — reference config on 2023-25 (different split - not comparable) | 5.5353 | 0.4934 | 0.0143 | 0.7741 | 0.1588 |

`model-comparisons/` runs are absent from the table because they are grid- or
seed-nested and are better read through their own `aggregate/` reports; the
compact-vs-full and linear-spline comparisons also appear in
[`results/compirt/holdout/aggregate_correctness_metrics.md`](../aggregate_correctness_metrics.md)
and [`docs/dd-linear-spline-vs-bernstein-3-3-2.md`](../../../../docs/dd-linear-spline-vs-bernstein-3-3-2.md).

## Caveats worth repeating before sharing

- **Single optimization seed.** Every run uses seed 42. Small gaps between
  neighbouring configurations are within initialization noise, not signal.
- **Not converged at 3,000 steps.** `optimization-steps/` shows joint event LL
  still improving at 6,000 and 20,000 steps, so any comparison at 3,000 steps is
  at an equal budget, not at convergence.
- **`data-splits/season-2023-25` is on a different population** and its metrics
  cannot be compared with the `year_2024` runs above.
- **The hyperparameter grid was run without terminal intercepts**, which the
  reference model has on; grid points are not drop-in comparable to it.
- These are held-out estimates. The in-sample counterparts live under
  [`results/compirt/in_sample/double-difficulty/`](../../in_sample/double-difficulty/)
  and are diagnostics, not generalization.
