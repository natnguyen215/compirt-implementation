# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | integrated_brier_score | survival_events | survival_events_skipped | first_buzzer_top1_accuracy | first_buzzer_mean_reciprocal_rank | first_buzzer_log_loss | first_buzzer_events | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.675001 | 0.635651 | 0.122684 | 0.188716 | 0.741602 | 0.770352 | -0.0287503 | 0.276288 | 0.258685 | 0.826568 | 0.99023 | 0.123509 | 0.0962484 | 65443 | 0 | 0.551192 | 0.716006 | 1.29276 | 64834 | 0.141405 | 0.118601 |

## Bonus Metrics

| auc | log_loss | ece | brier | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | part_accuracy | part_all_correct_accuracy | part_accuracy_lift_over_all_correct | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ranked_probability_score | ranked_probability_score_responses | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.935786 | 0.396312 | 0.0446407 | 0.0968933 | 0.407774 | 0.01419 | 0.710699 | 0.999716 | 0.0783153 | 0.87263 | 0.532399 | 0.340231 | 0.876905 | 0.872865 | 0.868337 | 0.666027 | 0.0937078 | 60454 | 1.89834 |

## Match Simulation Metrics

| match_winner_accuracy | match_winner_brier | match_games | match_simulations_per_game |
| --- | --- | --- | --- |
| 0.754321 | 0.172293 | 3240 | 500 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
