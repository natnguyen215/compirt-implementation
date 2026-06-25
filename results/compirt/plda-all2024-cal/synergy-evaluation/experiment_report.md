# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

|      auc |   log_loss |        ece |   buzz_position_mae |   buzz_position_median_absolute_error |
|---------:|-----------:|-----------:|--------------------:|--------------------------------------:|
| 0.632976 |   0.522314 | 0.00977668 |            0.156444 |                              0.142587 |

## Bonus Metrics

|      auc |   log_loss |       ece |   part_accuracy |   exact_score_accuracy |   per_bonus_points_mae |   ppb_mae |
|---------:|-----------:|----------:|----------------:|-----------------------:|-----------------------:|----------:|
| 0.917174 |   0.367331 | 0.0206971 |        0.836716 |                0.58516 |                4.94059 |   1.79766 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
