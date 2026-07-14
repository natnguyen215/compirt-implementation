# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.597349 | 0.527683 | 0.00240029 | 0.770367 | 0.146981 | 0.129307 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.91557 | 0.367116 | 0.00873569 | 0.832727 | 0.832727 | 0.562494 | 5.07253 | 2.3563 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
