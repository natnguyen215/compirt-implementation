# perceived-difficulty-three-slice-10000-positive-alpha-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.704177 | 0.654789 | 0.049388 |
| auc | 0.677495 | 0.621327 | 0.056168 |
| log loss | 0.589471 | 0.638892 | 0.049421 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.704177 | 0.654759 |
| Neg F1 | 0.418079 | 0.374756 |
| Lift over all-correct | -0.063158 | -0.112231 |
| Joint event LL | 6.297173 | 6.730268 |
| Correctness LL | 0.589471 | 0.638904 |
| AUC | 0.677497 | 0.621520 |
| ECE | 0.180102 | 0.200011 |
| Position MAE | 0.130348 | 0.138856 |
| First-buzzer top-1 | 0.415157 | 0.370622 |
| No-buzz error | 0.035186 | 0.034923 |
| Predicted final-decile mass | 0.145786 | 0.143966 |

Training folds included: 5. Held-out folds included: 5.
