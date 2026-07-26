# Topic-Weighted CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.651874 | 0.562218 | 0.104329 | 0.722291 | 0.146221 | 0.128089 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.919307 | 0.381643 | 0.0692594 | 0.843435 | 0.845047 | 0.843912 | 0.834515 | 0.586677 | 0.46892 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 2.13648 |
| 2 | latent_topic_01 | 2.967 |
| 3 | latent_topic_02 | 3.32053 |
| 4 | latent_topic_03 | 3.01077 |
| 5 | latent_topic_04 | 2.12145 |
| 6 | latent_topic_05 | 2.67639 |
| 7 | latent_topic_06 | 0.0553724 |
| 8 | latent_topic_07 | 0.0534748 |
