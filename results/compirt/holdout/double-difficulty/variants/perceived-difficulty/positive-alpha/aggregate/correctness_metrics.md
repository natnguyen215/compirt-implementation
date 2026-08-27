# perceived-difficulty-positive-alpha-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.696433 | 0.648744 | 0.047688 |
| auc | 0.656500 | 0.601642 | 0.054859 |
| log loss | 0.595512 | 0.635952 | 0.040440 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.696431 | 0.648728 |
| Neg F1 | 0.391013 | 0.355947 |
| Lift over all-correct | -0.070905 | -0.118263 |
| Joint event LL | 6.214868 | 6.637349 |
| Correctness LL | 0.595514 | 0.635948 |
| AUC | 0.656492 | 0.601681 |
| ECE | 0.184266 | 0.202172 |
| Position MAE | 0.126521 | 0.136340 |
| First-buzzer top-1 | 0.455233 | 0.391843 |
| No-buzz error | 0.034885 | 0.034329 |
| Predicted final-decile mass | 0.140651 | 0.138518 |

Training folds included: 5. Held-out folds included: 5.
