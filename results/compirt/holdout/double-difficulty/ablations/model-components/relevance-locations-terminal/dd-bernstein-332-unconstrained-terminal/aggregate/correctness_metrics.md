# seed_42 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.810905 | 0.765453 | 0.045453 |
| auc | 0.818841 | 0.716590 | 0.102250 |
| log loss | 0.425028 | 0.505831 | 0.080803 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.765455 |
| Neg F1 | 0.411095 |
| Lift over all-correct | -0.001536 |
| Joint event LL | 6.437505 |
| Correctness LL | 0.505854 |
| AUC | 0.716635 |
| ECE | 0.070584 |
| Position MAE | 0.136436 |
| First-buzzer top-1 | 0.379875 |
| No-buzz error | -0.004869 |
| Predicted final-decile mass | 0.189412 |

Folds included: 5.
