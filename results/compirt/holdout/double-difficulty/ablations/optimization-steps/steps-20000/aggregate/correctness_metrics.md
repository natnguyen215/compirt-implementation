# simplex-locations-terminal-20000 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.802557 | 0.779259 | 0.023299 |
| auc | 0.824544 | 0.713202 | 0.111343 |
| log loss | 0.426397 | 0.488751 | 0.062354 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.779258 |
| Neg F1 | 0.258169 |
| Lift over all-correct | 0.012267 |
| Joint event LL | 6.446222 |
| Correctness LL | 0.488773 |
| AUC | 0.713298 |
| ECE | 0.010813 |
| Position MAE | 0.139200 |
| First-buzzer top-1 | 0.365979 |
| No-buzz error | -0.004089 |
| Predicted final-decile mass | 0.181098 |

Folds included: 5.
