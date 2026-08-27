# multidim-all2024-gameinfill-5fold correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.707540 | 0.627525 | 0.080015 |
| auc | 0.705408 | 0.631975 | 0.073433 |
| log loss | 0.587462 | 0.811040 | 0.223578 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Held-out Research Log main-table metrics

These values are unweighted means of the fold-level metrics, matching the convention used by the Research Log main table.

| metric | fold mean |
| --- | ---: |
| Accuracy | 0.627567 |
| Neg F1 |  |
| Lift over all-correct | -0.139423 |
| Joint event LL | 6.775575 |
| Correctness LL | 0.810913 |
| AUC | 0.631977 |
| ECE | 0.219323 |
| Position MAE | 0.145426 |
| First-buzzer top-1 | 0.395818 |
| No-buzz error |  |
| Predicted final-decile mass |  |

Folds included: 5.
