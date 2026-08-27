# dd-sigmoid-simplex-terminal correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.775513 | 0.724296 | 0.051217 |
| auc | 0.754762 | 0.667615 | 0.087146 |
| log loss | 0.490505 | 0.546976 | 0.056471 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.724295 |
| Neg F1 | 0.364586 |
| Lift over all-correct | -0.042696 |
| Joint event LL | 6.676725 |
| Correctness LL | 0.546982 |
| AUC | 0.667611 |
| ECE | 0.109259 |
| Position MAE | 0.156610 |
| First-buzzer top-1 | 0.327571 |
| No-buzz error | -0.007583 |
| Predicted final-decile mass | 0.157326 |

Folds included: 5.
