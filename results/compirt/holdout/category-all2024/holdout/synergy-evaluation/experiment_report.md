# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.653385 | 0.638614 | 0.200561 | 0.668368 | 0.150314 | 0.131289 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | rounded_score_accuracy | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.921776 | 0.362624 | 0.0384641 | 0.841196 | 0.841196 | 0.581649 | 0.588861 | 4.8817 | 1.72877 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
