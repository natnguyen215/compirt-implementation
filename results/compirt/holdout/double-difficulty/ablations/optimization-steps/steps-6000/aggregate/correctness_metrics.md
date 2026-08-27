# simplex-locations-terminal-6000 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.801700 | 0.778867 | 0.022832 |
| auc | 0.821965 | 0.714007 | 0.107957 |
| log loss | 0.428425 | 0.488453 | 0.060028 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.778869 |
| Neg F1 | 0.249433 |
| Lift over all-correct | 0.011879 |
| Joint event LL | 6.503170 |
| Correctness LL | 0.488479 |
| AUC | 0.714067 |
| ECE | 0.011683 |
| Position MAE | 0.143961 |
| First-buzzer top-1 | 0.363128 |
| No-buzz error | -0.002299 |
| Predicted final-decile mass | 0.182313 |

Folds included: 5.
