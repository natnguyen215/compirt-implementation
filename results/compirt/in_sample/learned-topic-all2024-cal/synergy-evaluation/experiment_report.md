# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.630615 | 0.522923 | 0.0103939 | 0.768001 | 0.144669 | 0.128838 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.921769 | 0.355762 | 0.0133989 | 0.840965 | 0.840965 | 0.582799 | 4.80533 | 1.71382 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.
