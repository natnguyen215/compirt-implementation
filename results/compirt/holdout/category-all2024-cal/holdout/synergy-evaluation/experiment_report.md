# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.580065 | 0.531203 | 0.00841363 | 0.770352 | 0.144891 | 0.127647 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | rounded_score_accuracy | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.923776 | 0.350467 | 0.0115879 | 0.84296 | 0.84296 | 0.586297 | 0.597975 | 4.79444 | 1.67194 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
