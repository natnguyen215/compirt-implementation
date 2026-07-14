# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.663814 | 0.628697 | 0.152239 | 0.664736 | 0.151691 | 0.142988 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.92288 | 0.388372 | 0.0885815 | 0.846421 | 0.846421 | 0.597121 | 4.76326 | 1.72631 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
