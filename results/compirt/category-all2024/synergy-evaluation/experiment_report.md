# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|      auc |   log_loss |      ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|---------:|-----------:|---------:|--------------------:|--------------------------------------:|
| 0.675014 |   0.625936 | 0.193517 |            0.148221 |                              0.131333 |

## Bonus Metrics

|      auc |   log_loss |    ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|-------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.917836 |   0.371552 | 0.0367 |        0.836544 |               0.580462 |                4.96779 |   1.85828 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
