# perceived-difficulty-three-slice-alternating-10000-positive-alpha-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.680677 | 0.628634 | 0.052043 |
| auc | 0.671492 | 0.616482 | 0.055010 |
| log loss | 0.608146 | 0.661165 | 0.053019 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.680686 | 0.628580 |
| Neg F1 | 0.420073 | 0.380605 |
| Lift over all-correct | -0.086650 | -0.138411 |
| Joint event LL | 6.280054 | 6.765616 |
| Correctness LL | 0.608138 | 0.661202 |
| AUC | 0.671653 | 0.616429 |
| ECE | 0.198744 | 0.220678 |
| Position MAE | 0.129757 | 0.138908 |
| First-buzzer top-1 | 0.422249 | 0.366702 |
| No-buzz error | 0.035885 | 0.036269 |
| Predicted final-decile mass | 0.144310 | 0.142022 |

Training folds included: 5. Held-out folds included: 5.
