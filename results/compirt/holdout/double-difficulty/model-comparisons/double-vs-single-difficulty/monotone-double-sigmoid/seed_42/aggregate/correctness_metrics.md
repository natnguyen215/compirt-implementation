# seed_42 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.808012 | 0.741363 | 0.066649 |
| auc | 0.818636 | 0.674539 | 0.144097 |
| log loss | 0.424731 | 0.546480 | 0.121748 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.741385 |
| Neg F1 | 0.336872 |
| Lift over all-correct | -0.025606 |
| Joint event LL | 6.527798 |
| Correctness LL | 0.546469 |
| AUC | 0.674655 |
| ECE | 0.076626 |
| Position MAE | 0.139722 |
| First-buzzer top-1 | 0.393426 |
| No-buzz error | 0.046064 |
| Predicted final-decile mass | 0.106787 |

Folds included: 5.
