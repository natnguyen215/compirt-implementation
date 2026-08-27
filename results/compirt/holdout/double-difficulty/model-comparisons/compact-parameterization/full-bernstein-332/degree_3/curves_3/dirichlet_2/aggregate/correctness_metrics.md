# dirichlet_2 correctness summary

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

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.810907 | 0.765455 |
| Neg F1 | 0.514289 | 0.411095 |
| Lift over all-correct | 0.043572 | -0.001536 |
| Joint event LL | 6.073468 | 6.437505 |
| Correctness LL | 0.425029 | 0.505854 |
| AUC | 0.818831 | 0.716635 |
| ECE | 0.056585 | 0.070584 |
| Position MAE | 0.127629 | 0.136436 |
| First-buzzer top-1 | 0.433022 | 0.379875 |
| No-buzz error | -0.005036 | -0.004869 |
| Predicted final-decile mass | 0.191641 | 0.189412 |

Training folds included: 5. Held-out folds included: 5.
