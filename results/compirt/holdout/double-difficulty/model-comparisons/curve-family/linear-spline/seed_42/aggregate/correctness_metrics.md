# seed_42 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.855813 | 0.734493 | 0.121320 |
| auc | 0.898074 | 0.722838 | 0.175235 |
| log loss | 0.337989 | 0.565116 | 0.227127 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.855812 | 0.734504 |
| Neg F1 | 0.674079 | 0.462773 |
| Lift over all-correct | 0.088477 | -0.032486 |
| Joint event LL | 5.730020 | 6.459592 |
| Correctness LL | 0.337989 | 0.565126 |
| AUC | 0.898072 | 0.722822 |
| ECE | 0.059008 | 0.118483 |
| Position MAE | 0.125385 | 0.135931 |
| First-buzzer top-1 | 0.477136 | 0.397445 |
| No-buzz error | 0.033617 | 0.033684 |
| Predicted final-decile mass | 0.179825 | 0.177649 |

Training folds included: 5. Held-out folds included: 5.
