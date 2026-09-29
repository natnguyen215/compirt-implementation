# dd-bernstein-330p67-simplex-locations-terminal correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.798585 | 0.779433 | 0.019152 |
| auc | 0.814545 | 0.716000 | 0.098545 |
| log loss | 0.434528 | 0.487302 | 0.052774 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.779423 |
| Neg F1 | 0.238846 |
| Lift over all-correct | 0.012433 |
| Joint event LL | 6.609021 |
| Correctness LL | 0.487331 |
| AUC | 0.716029 |
| ECE | 0.011035 |
| Position MAE | 0.149447 |
| First-buzzer top-1 | 0.351107 |
| No-buzz error | 0.001280 |
| Predicted final-decile mass | 0.196173 |

Folds included: 5.
