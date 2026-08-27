# seed_42 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.810063 | 0.746625 | 0.063439 |
| auc | 0.831231 | 0.709430 | 0.121801 |
| log loss | 0.418023 | 0.528036 | 0.110013 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.746669 |
| Neg F1 | 0.426975 |
| Lift over all-correct | -0.020322 |
| Joint event LL | 6.513694 |
| Correctness LL | 0.528027 |
| AUC | 0.709471 |
| ECE | 0.092545 |
| Position MAE | 0.137626 |
| First-buzzer top-1 | 0.395131 |
| No-buzz error | 0.054984 |
| Predicted final-decile mass | 0.154292 |

Folds included: 5.
