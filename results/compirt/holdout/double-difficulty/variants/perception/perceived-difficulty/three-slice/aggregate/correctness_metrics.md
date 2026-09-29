# perceived-difficulty-three-slice-positive-alpha-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.637262 | 0.585759 | 0.051503 |
| auc | 0.650029 | 0.600781 | 0.049248 |
| log loss | 0.655324 | 0.704988 | 0.049664 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.637266 | 0.585725 |
| Neg F1 | 0.411483 | 0.379898 |
| Lift over all-correct | -0.130069 | -0.181266 |
| Joint event LL | 6.246709 | 6.807457 |
| Correctness LL | 0.655321 | 0.704994 |
| AUC | 0.650030 | 0.600866 |
| ECE | 0.237859 | 0.258387 |
| Position MAE | 0.128748 | 0.138301 |
| First-buzzer top-1 | 0.436307 | 0.375047 |
| No-buzz error | 0.037643 | 0.037590 |
| Predicted final-decile mass | 0.139734 | 0.136705 |

Training folds included: 5. Held-out folds included: 5.
