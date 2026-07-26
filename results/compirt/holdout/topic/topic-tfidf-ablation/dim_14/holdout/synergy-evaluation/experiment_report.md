# Topic-Weighted CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.649714 | 0.548904 | 0.0881738 | 0.731468 | 0.148695 | 0.13073 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.910848 | 0.40828 | 0.0898075 | 0.837022 | 0.839336 | 0.837601 | 0.815902 | 0.572601 | 0.495847 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 3.48752 |
| 2 | latent_topic_01 | 2.19537 |
| 3 | latent_topic_02 | 3.93783 |
| 4 | latent_topic_03 | 3.23393 |
| 5 | latent_topic_04 | 3.47608 |
| 6 | latent_topic_05 | 3.09575 |
| 7 | latent_topic_06 | 2.32571 |
| 8 | latent_topic_07 | 0.201066 |
| 9 | latent_topic_08 | 1.09446 |
| 10 | latent_topic_09 | 0.556013 |
| 11 | latent_topic_10 | 0.387981 |
| 12 | latent_topic_11 | 0.379554 |
| 13 | latent_topic_12 | 0.372394 |
| 14 | latent_topic_13 | 0.346831 |
