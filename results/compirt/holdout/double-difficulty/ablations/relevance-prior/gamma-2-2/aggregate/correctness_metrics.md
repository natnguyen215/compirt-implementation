# dd-bernstein-332-gamma22-locations-terminal correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.812620 | 0.776976 | 0.035645 |
| auc | 0.816060 | 0.715768 | 0.100292 |
| log loss | 0.421316 | 0.497701 | 0.076385 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.812619 | 0.776970 |
| Neg F1 | 0.457057 | 0.360844 |
| Lift over all-correct | 0.045283 | 0.009980 |
| Joint event LL | 6.049835 | 6.406475 |
| Correctness LL | 0.421318 | 0.497741 |
| AUC | 0.816054 | 0.715841 |
| ECE | 0.037553 | 0.042568 |
| Position MAE | 0.126971 | 0.135594 |
| First-buzzer top-1 | 0.442689 | 0.390291 |
| No-buzz error | -0.004822 | -0.004630 |
| Predicted final-decile mass | 0.193859 | 0.191220 |

Training folds included: 5. Held-out folds included: 5.
