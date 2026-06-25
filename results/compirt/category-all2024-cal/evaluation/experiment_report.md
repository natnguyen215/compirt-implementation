# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|      auc |   log_loss |        ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|---------:|-----------:|-----------:|--------------------:|--------------------------------------:|
| 0.611751 |    0.52806 | 0.00571128 |            0.142135 |                              0.126368 |

## Bonus Metrics

|      auc |   log_loss |        ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|-----------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.908746 |   0.381682 | 0.00602173 |        0.825485 |               0.558006 |                5.23662 |   2.47031 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
