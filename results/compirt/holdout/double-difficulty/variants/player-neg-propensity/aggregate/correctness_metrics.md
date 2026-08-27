# dd-bernstein-332-simplex-locations-terminal-player-neg-propensity correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.798956 | 0.779498 | 0.019459 |
| auc | 0.815818 | 0.715746 | 0.100072 |
| log loss | 0.432859 | 0.487742 | 0.054883 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.798956 | 0.779485 |
| Neg F1 | 0.314159 | 0.239176 |
| Lift over all-correct | 0.031620 | 0.012495 |
| Joint event LL | 6.379021 | 6.582795 |
| Correctness LL | 0.432863 | 0.487771 |
| AUC | 0.815790 | 0.715776 |
| ECE | 0.053595 | 0.012841 |
| Position MAE | 0.145785 | 0.151078 |
| First-buzzer top-1 | 0.400051 | 0.360863 |
| No-buzz error | 0.000038 | 0.000690 |
| Predicted final-decile mass | 0.189111 | 0.186633 |

Training folds included: 5. Held-out folds included: 5.
