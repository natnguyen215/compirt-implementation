# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.617915 | 0.570207 | 0.0209683 | 0.728086 | 0.164806 | 0.16027 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.924768 | 0.349892 | 0.0276531 | 0.849176 | 0.849176 | 0.598974 | 4.67515 | 1.6494 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
