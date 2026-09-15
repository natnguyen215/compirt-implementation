# Perceived difficulty and logit ablation: optimization-budget comparison

This report compares the saved dimension sweeps at matching K. Each detailed report includes all scores, fold variability, parameter diagnostics, coverage and source links. Scores are pooled unless explicitly labeled as fold statistics.

- [3,000 steps: perceived-logit, perceived-difficulty-three-slice](../../perception-dimensions-unconstrained/aggregate/summary.md)
- [10,000 steps: perceived-logit](../perceived-logit-grid/aggregate/summary.md)
- [10,000 steps: perceived-difficulty-three-slice](../three-slice-grid/aggregate/summary.md)

## Selected capacities

| Model | Steps | Selected K | Joint LL | Parameters (fold mean) | Accuracy | Neg F1 | Position MAE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| perceived-difficulty-three-slice | 3000 | 3 | 6.89727 | 48195 | 0.767149 | 0.165368 | 0.160739 |
| perceived-logit | 3000 | 6 | 7.69439 | 48180 | 0.765822 | 0.0485823 | 0.330719 |
| perceived-logit | 10000 | 8 | 6.66725 | 63690 | 0.717339 | 0.33359 | 0.165863 |
| perceived-difficulty-three-slice | 10000 | 3 | 6.93492 | 48195 | 0.767779 | 0.209108 | 0.161518 |

## Matched-dimension changes

Delta is longer-budget minus shorter-budget. Negative loss/MAE deltas favor longer training. Accuracy and F1 deltas are percentage points. Matched-fold joint-loss SD is descriptive, not a confidence interval. Only complete points with identical non-budget settings are compared; different K selections are not matched controls.

| Model | K | Steps | Short joint LL | Long joint LL | Δ joint LL | Δ correctness LL | Δ accuracy (pp) | Δ neg F1 (pp) | Δ position MAE | Fold Δ joint LL mean ± SD | Folds with lower joint LL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| perceived-logit | 6 | 3000 → 10000 | 7.69439 | 6.87408 | -0.820308 | -0.00214295 | -2.69377 | 23.2342 | -0.142653 | -0.820555 ± 0.0327377 | 5/5 |
| perceived-logit | 8 | 3000 → 10000 | 7.67617 | 6.66725 | -1.00892 | 0.0125074 | -4.80704 | 26.6819 | -0.157373 | -1.00905 ± 0.0207781 | 5/5 |
| perceived-logit | 10 | 3000 → 10000 | 7.644 | 6.65095 | -0.993056 | 0.0337608 | -6.7203 | 28.4835 | -0.152299 | -0.993181 ± 0.021066 | 5/5 |
| perceived-difficulty-three-slice | 3 | 3000 → 10000 | 6.89727 | 6.93492 | 0.0376504 | -0.00347896 | 0.0630503 | 4.37399 | 0.000779614 | 0.0373788 ± 0.0379614 | 0/5 |
| perceived-difficulty-three-slice | 5 | 3000 → 10000 | 6.86612 | 6.8932 | 0.0270861 | 0.00276628 | 0.0217415 | 4.44422 | -6.25189e-05 | 0.0270001 ± 0.0251966 | 1/5 |
| perceived-difficulty-three-slice | 6 | 3000 → 10000 | 6.87648 | 6.92485 | 0.0483635 | -0.000291923 | -0.0608762 | 4.66898 | -4.32377e-05 | 0.0481014 ± 0.0497452 | 0/5 |

## Interpretation limits

The 1% selection rule is applied separately within each saved grid. A sparse follow-up grid does not establish the smallest adequate K among dimensions that were not rerun. Hyperparameter selection and scoring share folds; these results require a separate test or nested selection for an unbiased final estimate. The arms also differ in prior and transform structure, so their comparison does not isolate slicing. Training loss slopes and fitted alpha/beta distributions are available in the linked reports; these fits use one optimizer seed.
