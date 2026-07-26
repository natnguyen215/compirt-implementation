# Topic-Weighted CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.654603 | 0.562973 | 0.106359 | 0.72152 | 0.145536 | 0.127336 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.920729 | 0.377097 | 0.0651602 | 0.843777 | 0.845136 | 0.844277 | 0.836445 | 0.587405 | 0.463094 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 2.96514 |
| 2 | latent_topic_01 | 3.45954 |
| 3 | latent_topic_02 | 2.7473 |
| 4 | latent_topic_03 | 2.42005 |
| 5 | latent_topic_04 | 1.97868 |
| 6 | latent_topic_05 | 1.1236 |
| 7 | latent_topic_06 | 1.10358 |
