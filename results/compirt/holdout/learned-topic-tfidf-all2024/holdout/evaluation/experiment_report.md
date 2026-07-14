# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.644869 | 0.575621 | 0.11642 | 0.71279 | 0.146604 | 0.128708 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.915671 | 0.383908 | 0.0565121 | 0.835484 | 0.835484 | 0.568565 | 5.05806 | 2.14669 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 2.15671 |
| 2 | latent_topic_01 | 2.55944 |
| 3 | latent_topic_02 | 2.64018 |
| 4 | latent_topic_03 | 2.69816 |
| 5 | latent_topic_04 | 2.309 |
