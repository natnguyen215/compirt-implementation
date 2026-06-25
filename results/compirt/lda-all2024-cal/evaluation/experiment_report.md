# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|    auc |   log_loss |        ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|-------:|-----------:|-----------:|--------------------:|--------------------------------------:|
| 0.6287 |   0.523608 | 0.00888419 |            0.152675 |                              0.137911 |

## Bonus Metrics

|      auc |   log_loss |       ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|----------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.910076 |   0.379328 | 0.0104577 |        0.826594 |               0.558995 |                5.19426 |    2.3795 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
