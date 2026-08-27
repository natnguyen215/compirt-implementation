# dd-bernstein-332-simplex-locations-terminal correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.797572 | 0.779498 | 0.018074 |
| auc | 0.813561 | 0.715439 | 0.098122 |
| log loss | 0.435494 | 0.487772 | 0.052279 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.797572 | 0.779493 |
| Neg F1 | 0.302886 | 0.232093 |
| Lift over all-correct | 0.030236 | 0.012502 |
| Joint event LL | 6.405448 | 6.612269 |
| Correctness LL | 0.435495 | 0.487803 |
| AUC | 0.813563 | 0.715466 |
| ECE | 0.054623 | 0.012510 |
| Position MAE | 0.146273 | 0.151862 |
| First-buzzer top-1 | 0.393159 | 0.351634 |
| No-buzz error | 0.000216 | 0.000930 |
| Predicted final-decile mass | 0.190831 | 0.188189 |

Training folds included: 5. Held-out folds included: 5.
