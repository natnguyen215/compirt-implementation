# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|      auc |   log_loss |      ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|---------:|-----------:|---------:|--------------------:|--------------------------------------:|
| 0.664963 |   0.613202 | 0.180173 |            0.157885 |                              0.142185 |

## Bonus Metrics

|      auc |   log_loss |       ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|----------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.915335 |   0.386587 | 0.0585045 |        0.835075 |               0.574954 |                5.00016 |   1.89343 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
