# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.655846 | 0.621151 | 0.182357 | 0.673242 | 0.153987 | 0.13584 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | rounded_score_accuracy | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.91787 | 0.376906 | 0.0526634 | 0.838494 | 0.838494 | 0.576157 | 0.581301 | 4.93906 | 1.78333 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
