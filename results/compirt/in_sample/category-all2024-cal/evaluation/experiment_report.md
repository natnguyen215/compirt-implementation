# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.61389 | 0.527521 | 0.00542506 | 0.767458 | 0.141649 | 0.125685 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.909656 | 0.379766 | 0.00556298 | 0.827036 | 0.827036 | 0.552903 | 5.20465 | 2.43173 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
