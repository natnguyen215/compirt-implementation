# dd-bernstein-332-simplex-locations-terminal-incorrect3 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.764143 | 0.690662 | 0.073481 |
| auc | 0.839954 | 0.710526 | 0.129428 |
| log loss | 0.504612 | 0.587991 | 0.083379 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.690642 |
| Neg F1 | 0.467785 |
| Lift over all-correct | -0.076349 |
| Joint event LL | 6.706901 |
| Correctness LL | 0.588011 |
| AUC | 0.710522 |
| ECE | 0.187186 |
| Position MAE | 0.151703 |
| First-buzzer top-1 | 0.351711 |
| No-buzz error | 0.000763 |
| Predicted final-decile mass | 0.187542 |

Folds included: 5.
