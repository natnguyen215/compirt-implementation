# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Tossup Metrics

| auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | joint_tossup_event_log_loss | joint_tossup_event_log_loss_events | integrated_brier_score | survival_events | survival_events_skipped | first_buzzer_top1_accuracy | first_buzzer_mean_reciprocal_rank | first_buzzer_log_loss | first_buzzer_events | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.655844 | 0.514258 | 0.0098768 | 0.167994 | 0.770234 | 0.767271 | 0.00296364 | 0.0903405 | 0.648164 | 0.786729 | 0.870591 | 0.168544 | 5.99378 | 48612 | 0.0836097 | 48612 | 0 | 0.49138 | 0.678047 | 1.32475 | 47914 | 0.129225 | 0.109887 |

## Bonus Metrics

| auc | log_loss | ece | brier | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance | part_accuracy | part_all_correct_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ranked_probability_score | ranked_probability_score_responses | bonus_total_score_log_loss | bonus_total_score_log_loss_responses | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.936507 | 0.330569 | 0.0390519 | 0.10326 | 0.33385 | 0.359403 | 0.0447387 | 0.455291 | 0.971026 | 0.120775 | 0.854339 | 0.520489 | 0.85652 | 0.854685 | 0.861601 | 0.617012 | 0.0938353 | 44487 | 0.836281 | 44487 | 1.55185 |

## Match Simulation Metrics

| match_winner_accuracy | match_winner_brier | match_games | match_simulations_per_game |
| --- | --- | --- | --- |
| 0.802823 | 0.133324 | 2409 | 500 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
