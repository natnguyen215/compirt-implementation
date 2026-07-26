# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | integrated_brier_score | survival_events | survival_events_skipped | first_buzzer_top1_accuracy | first_buzzer_mean_reciprocal_rank | first_buzzer_log_loss | first_buzzer_events | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.695695 | 0.605553 | 0.122991 | 0.183923 | 0.745257 | 0.770352 | -0.0250949 | 0.280014 | 0.238765 | 0.800336 | 0.985385 | 0.130148 | 0.0896713 | 65443 | 0 | 0.58093 | 0.742059 | 1.17245 | 64834 | 0.133858 | 0.111313 |

## Bonus Metrics

| auc | log_loss | ece | brier | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | part_accuracy | part_all_correct_accuracy | part_accuracy_lift_over_all_correct | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ranked_probability_score | ranked_probability_score_responses | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.933903 | 0.355803 | 0.0183029 | 0.0987788 | 0.396012 | 0.0238173 | 0.626401 | 0.997755 | 0.090606 | 0.866527 | 0.532399 | 0.334127 | 0.872397 | 0.866849 | 0.862756 | 0.650346 | 0.0951482 | 60454 | 1.9408 |

## Match Simulation Metrics

| match_winner_accuracy | match_winner_brier | match_games | match_simulations_per_game |
| --- | --- | --- | --- |
| 0.78179 | 0.158834 | 3240 | 500 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
