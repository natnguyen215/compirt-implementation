# Topic-Weighted CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.655868 | 0.554223 | 0.0965451 | 0.725915 | 0.146146 | 0.127674 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.916805 | 0.390194 | 0.077182 | 0.841874 | 0.843536 | 0.842379 | 0.83057 | 0.583286 | 0.477723 |

Generated figures match the standard CompIRT evaluation set. The first-buzz timing replay uses the CAIMIRA topic-gap formula `sum_k r_jk * (theta_ik - d_jk(t))`.

The dedicated TF-IDF replay applies saved signed adjustments `-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective difficulty and first-buzz timing.

## TF-IDF Cumulative-Difficulty Lambdas

One nonnegative `lambda_k` per topic coordinate scales the cumulative TF-IDF prefix mass that lowers effective difficulty (`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).

| topic_dimension | topic_label | lambda_tfidf |
| --- | --- | --- |
| 1 | latent_topic_00 | 2.85349 |
| 2 | latent_topic_01 | 3.22162 |
| 3 | latent_topic_02 | 3.53327 |
| 4 | latent_topic_03 | 2.73186 |
| 5 | latent_topic_04 | 3.01082 |
| 6 | latent_topic_05 | 2.59863 |
| 7 | latent_topic_06 | 1.12732 |
| 8 | latent_topic_07 | 1.07269 |
| 9 | latent_topic_08 | 0.139513 |
| 10 | latent_topic_09 | 0.0818511 |
