# seed_42 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.805042 | 0.749299 | 0.055743 |
| auc | 0.796109 | 0.709085 | 0.087024 |
| log loss | 0.437272 | 0.530197 | 0.092925 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.749288 |
| Neg F1 | 0.415717 |
| Lift over all-correct | -0.017702 |
| Joint event LL | 6.477630 |
| Correctness LL | 0.530219 |
| AUC | 0.709112 |
| ECE | 0.081184 |
| Position MAE | 0.149276 |
| First-buzzer top-1 | 0.394141 |
| No-buzz error | -0.004998 |
| Predicted final-decile mass | 0.169152 |

Folds included: 5.
