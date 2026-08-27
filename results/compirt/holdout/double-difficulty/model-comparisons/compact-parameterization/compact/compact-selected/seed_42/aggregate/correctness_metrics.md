# seed_42 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.806752 | 0.766431 | 0.040321 |
| auc | 0.793608 | 0.704428 | 0.089180 |
| log loss | 0.433724 | 0.515032 | 0.081308 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.766429 |
| Neg F1 | 0.356387 |
| Lift over all-correct | -0.000562 |
| Joint event LL | 6.415743 |
| Correctness LL | 0.515073 |
| AUC | 0.704470 |
| ECE | 0.055029 |
| Position MAE | 0.141066 |
| First-buzzer top-1 | 0.394957 |
| No-buzz error | -0.004791 |
| Predicted final-decile mass | 0.175157 |

Folds included: 5.
