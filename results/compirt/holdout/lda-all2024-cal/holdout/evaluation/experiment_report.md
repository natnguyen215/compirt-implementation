# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.597036 | 0.527886 | 0.00371094 | 0.770337 | 0.15253 | 0.135587 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | rounded_score_accuracy | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.911379 | 0.37593 | 0.00933296 | 0.82874 | 0.82874 | 0.554769 | 0.565207 | 5.18295 | 2.4397 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
