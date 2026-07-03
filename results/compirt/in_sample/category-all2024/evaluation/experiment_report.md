# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.675414 | 0.621615 | 0.190721 | 0.680594 | 0.147664 | 0.130571 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | rounded_score_accuracy | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.91227 | 0.385933 | 0.0470387 | 0.82801 | 0.82801 | 0.555488 | 0.551352 | 5.24322 | 2.44462 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
