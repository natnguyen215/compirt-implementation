# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | integrated_brier_score | survival_events | survival_events_skipped | first_buzzer_top1_accuracy | first_buzzer_mean_reciprocal_rank | first_buzzer_log_loss | first_buzzer_events | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.709326 | 0.563933 | 0.113179 | 0.178825 | 0.74774 | 0.770352 | -0.0226116 | 0.270755 | 0.251667 | 0.782362 | 0.97346 | 0.138519 | 0.0861841 | 65443 | 0 | 0.598945 | 0.755914 | 1.09789 | 64834 | 0.131324 | 0.110435 |

## Bonus Metrics

| auc | log_loss | ece | brier | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | part_accuracy | part_all_correct_accuracy | part_accuracy_lift_over_all_correct | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ranked_probability_score | ranked_probability_score_responses | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.934512 | 0.334326 | 0.0133318 | 0.0998836 | 0.381861 | 0.0344004 | 0.579854 | 0.990817 | 0.102764 | 0.862353 | 0.532399 | 0.329953 | 0.868941 | 0.86276 | 0.85624 | 0.638337 | 0.0953257 | 60454 | 1.87597 |

## Match Simulation Metrics

| match_winner_accuracy | match_winner_brier | match_games | match_simulations_per_game |
| --- | --- | --- | --- |
| 0.785185 | 0.148685 | 3240 | 500 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
