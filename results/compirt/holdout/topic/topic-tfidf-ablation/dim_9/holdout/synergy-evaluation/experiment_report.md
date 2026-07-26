# Topic-Weighted CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.653404 | 0.557849 | 0.100594 | 0.725823 | 0.147129 | 0.128589 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.917474 | 0.386052 | 0.0708066 | 0.8414 | 0.843311 | 0.841941 | 0.83276 | 0.581864 | 0.486232 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 3.28239 |
| 2 | latent_topic_01 | 3.28997 |
| 3 | latent_topic_02 | 1.5755 |
| 4 | latent_topic_03 | 2.11016 |
| 5 | latent_topic_04 | 2.72317 |
| 6 | latent_topic_05 | 1.15071 |
| 7 | latent_topic_06 | 0.892309 |
| 8 | latent_topic_07 | 0.276353 |
| 9 | latent_topic_08 | 2.92339 |
