# Topic-Weighted CompIRT Experiment Report

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.583266 | 0.530726 | 0.0102945 | 0.770352 | 0.146027 | 0.128165 |

## Bonus Metrics

| auc | log_loss | ece | accuracy | part_accuracy | exact_acc | per_bonus_points_mae | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.91558 | 0.367053 | 0.00921776 | 0.833184 | 0.833184 | 0.563767 | 5.06535 | 2.35344 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 2.01241 |
| 2 | latent_topic_01 | 0.186317 |
| 3 | latent_topic_02 | 0.947743 |
| 4 | latent_topic_03 | 0.543401 |
| 5 | latent_topic_04 | 0.951819 |
