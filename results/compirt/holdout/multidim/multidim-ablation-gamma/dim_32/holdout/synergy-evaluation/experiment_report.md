# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Tossup Metrics

| auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | integrated_brier_score | survival_events | survival_events_skipped | first_buzzer_top1_accuracy | first_buzzer_mean_reciprocal_rank | first_buzzer_log_loss | first_buzzer_events | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.710622 | 0.57305 | 0.118471 | 0.180717 | 0.745381 | 0.770352 | -0.0249715 | 0.27352 | 0.240983 | 0.773107 | 0.973498 | 0.13989 | 0.0882605 | 65443 | 0 | 0.575285 | 0.738675 | 1.16916 | 64834 | 0.132925 | 0.111563 |

## Bonus Metrics

| auc | log_loss | ece | brier | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | part_accuracy | part_all_correct_accuracy | part_accuracy_lift_over_all_correct | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ranked_probability_score | ranked_probability_score_responses | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.935939 | 0.337481 | 0.0139975 | 0.098055 | 0.387591 | 0.0304203 | 0.590756 | 0.994572 | 0.0980497 | 0.865501 | 0.532399 | 0.333102 | 0.87106 | 0.865957 | 0.863829 | 0.646541 | 0.0936065 | 60454 | 1.79353 |

## Match Simulation Metrics

| match_winner_accuracy | match_winner_brier | match_games | match_simulations_per_game |
| --- | --- | --- | --- |
| 0.790123 | 0.147595 | 3240 | 500 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
