# dd-bernstein-332-simplex-locations-terminal-acf-2023-25 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.796280 | 0.774070 | 0.022210 |
| auc | 0.812519 | 0.711402 | 0.101117 |
| log loss | 0.436170 | 0.493381 | 0.057211 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 518775 |
| held-out | 125875 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.774078 |
| Neg F1 | 0.237409 |
| Lift over all-correct | 0.009215 |
| Joint event LL | 5.535359 |
| Correctness LL | 0.493369 |
| AUC | 0.711443 |
| ECE | 0.014295 |
| Position MAE | 0.158783 |
| First-buzzer top-1 | 0.334670 |
| No-buzz error | 0.010081 |
| Predicted final-decile mass | 0.141861 |

Folds included: 5.
