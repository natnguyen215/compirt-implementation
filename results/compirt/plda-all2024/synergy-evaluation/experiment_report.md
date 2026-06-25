# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|    auc |   log_loss |      ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|-------:|-----------:|---------:|--------------------:|--------------------------------------:|
| 0.6644 |   0.612555 | 0.182414 |            0.161416 |                              0.146306 |

## Bonus Metrics

|      auc |   log_loss |       ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|----------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.912923 |   0.394996 | 0.0658297 |        0.833562 |               0.571718 |                5.05165 |   1.90773 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
