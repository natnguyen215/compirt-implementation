# Topic-Weighted CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.649493 | 0.556055 | 0.0964269 | 0.726178 | 0.146951 | 0.128568 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.913531 | 0.400399 | 0.0842567 | 0.839062 | 0.841022 | 0.839647 | 0.820947 | 0.576819 | 0.483587 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 3.64647 |
| 2 | latent_topic_01 | 3.52168 |
| 3 | latent_topic_02 | 2.7514 |
| 4 | latent_topic_03 | 2.37235 |
| 5 | latent_topic_04 | 3.12161 |
| 6 | latent_topic_05 | 3.3177 |
| 7 | latent_topic_06 | 0.653539 |
| 8 | latent_topic_07 | 2.38117 |
| 9 | latent_topic_08 | 0.078353 |
| 10 | latent_topic_09 | 0.236812 |
| 11 | latent_topic_10 | 0.195293 |
| 12 | latent_topic_11 | 0.206612 |
