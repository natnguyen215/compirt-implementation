# dd-bernstein-332-simplex-locations-terminal-incorrect1p5 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.810787 | 0.771975 | 0.038811 |
| auc | 0.822745 | 0.714439 | 0.108307 |
| log loss | 0.437085 | 0.499097 | 0.062012 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.771957 |
| Neg F1 | 0.374826 |
| Lift over all-correct | 0.004966 |
| Joint event LL | 6.618979 |
| Correctness LL | 0.499123 |
| AUC | 0.714489 |
| ECE | 0.061117 |
| Position MAE | 0.151802 |
| First-buzzer top-1 | 0.352158 |
| No-buzz error | 0.000890 |
| Predicted final-decile mass | 0.187720 |

Folds included: 5.
