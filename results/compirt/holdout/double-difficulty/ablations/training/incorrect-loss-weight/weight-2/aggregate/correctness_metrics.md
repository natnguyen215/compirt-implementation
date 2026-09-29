# dd-bernstein-332-simplex-locations-terminal-incorrect2 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.803451 | 0.748929 | 0.054522 |
| auc | 0.829653 | 0.713034 | 0.116620 |
| log loss | 0.455556 | 0.525638 | 0.070081 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.748922 |
| Neg F1 | 0.436067 |
| Lift over all-correct | -0.018069 |
| Joint event LL | 6.644014 |
| Correctness LL | 0.525662 |
| AUC | 0.713071 |
| ECE | 0.113056 |
| Position MAE | 0.151742 |
| First-buzzer top-1 | 0.352809 |
| No-buzz error | 0.000816 |
| Predicted final-decile mass | 0.187462 |

Folds included: 5.
