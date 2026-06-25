# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|    auc |   log_loss |      ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|-------:|-----------:|---------:|--------------------:|--------------------------------------:|
| 0.6644 |   0.612555 | 0.182414 |            0.161416 |                              0.146306 |

## Bonus Metrics

|      auc |   log_loss |       ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|----------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.904051 |   0.417792 | 0.0819663 |        0.812627 |               0.522602 |                5.53691 |   2.89148 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
