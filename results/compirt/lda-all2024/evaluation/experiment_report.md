# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|      auc |   log_loss |      ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|---------:|-----------:|---------:|--------------------:|--------------------------------------:|
| 0.664963 |   0.613202 | 0.180173 |            0.157885 |                              0.142185 |

## Bonus Metrics

|      auc |   log_loss |       ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|----------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.907132 |   0.407712 | 0.0737959 |        0.817737 |                 0.5331 |                5.44114 |   2.79912 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
