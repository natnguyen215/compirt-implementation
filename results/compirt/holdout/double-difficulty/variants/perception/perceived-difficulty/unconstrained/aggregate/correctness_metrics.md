# perceived-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.784115 | 0.768323 | 0.015792 |
| auc | 0.741359 | 0.660356 | 0.081003 |
| log loss | 0.479097 | 0.516621 | 0.037524 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.784115 | 0.768330 |
| Neg F1 | 0.270023 | 0.217730 |
| Lift over all-correct | 0.016780 | 0.001339 |
| Joint event LL | 7.430461 | 7.617837 |
| Correctness LL | 0.479097 | 0.516634 |
| AUC | 0.741427 | 0.660483 |
| ECE | 0.037165 | 0.035030 |
| Position MAE | 0.324755 | 0.327728 |
| First-buzzer top-1 | 0.396005 | 0.350968 |
| No-buzz error | 0.208716 | 0.208150 |
| Predicted final-decile mass | 0.033066 | 0.032263 |

Training folds included: 5. Held-out folds included: 5.
