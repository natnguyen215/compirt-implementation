# dirichlet_2 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.809335 | 0.773128 | 0.036207 |
| auc | 0.809040 | 0.714041 | 0.094999 |
| log loss | 0.447260 | 0.502120 | 0.054860 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.809337 | 0.773134 |
| Neg F1 | 0.465761 | 0.373405 |
| Lift over all-correct | 0.042002 | 0.006144 |
| Joint event LL | 6.511866 | 6.721603 |
| Correctness LL | 0.447260 | 0.502132 |
| AUC | 0.809035 | 0.714030 |
| ECE | 0.077319 | 0.070702 |
| Position MAE | 0.160666 | 0.166723 |
| First-buzzer top-1 | 0.381206 | 0.336722 |
| No-buzz error | -0.002308 | -0.001945 |
| Predicted final-decile mass | 0.178179 | 0.175156 |

Training folds included: 5. Held-out folds included: 5.
