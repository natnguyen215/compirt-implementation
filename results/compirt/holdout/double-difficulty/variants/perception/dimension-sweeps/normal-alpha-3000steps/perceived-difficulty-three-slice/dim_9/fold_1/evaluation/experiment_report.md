# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.652255 |
| log_loss | 0.522315 |
| ece | 0.0147762 |
| brier | 0.170536 |
| accuracy | 0.767403 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00527879 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.114127 |
| probability_p10 | 0.613506 |
| probability_p50 | 0.795071 |
| probability_p90 | 0.902381 |
| mean_predictive_variance | 0.161681 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101086 |
| joint_tossup_event_log_loss | 6.88881 |
| buzz_position_mae | 0.162552 |
| buzz_position_median_absolute_error | 0.148957 |
| buzz_position_bias | -0.0731469 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34774 |
| first_buzzer_mean_reciprocal_rank | 0.560064 |
| first_buzzer_log_loss | 1.68696 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637963 |
| tossup_scorer_player_top1_accuracy | 0.321645 |
| tossup_scorer_team_top1_accuracy | 0.493074 |
| tossup_game_winner_accuracy | 0.777027 |
| tossup_game_margin_mae | 34.1799 |
| tournament_player_ppg_spearman | 0.664431 |
| tournament_player_ppg_mae | 9.03912 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.652255 |
| neg_average_precision | 0.387079 |
| neg_precision | 0.611111 |
| neg_recall | 0.0610264 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0551064 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0938899 |
| no_buzz_calibration_error | 0.0779808 |
| no_buzz_brier | 0.0279834 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0731469 | -0.0933149 |
| Q1 (0-.2) | 167 | 0.359094 | 0.368979 |
| Q2 (.2-.4) | 912 | 0.202673 | 0.201556 |
| Q3 (.4-.6) | 2115 | 0.0477911 | 0.050635 |
| Q4 (.6-.8) | 2844 | -0.0913383 | -0.0903666 |
| Q5 (.8-1) | 3055 | -0.245906 | -0.24448 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0147762 | 0.170536 | 0.652255 | 0.522315 |
| tossup_correctness | tier | fall | 2842 | 0.0145481 | 0.154648 | 0.692096 | 0.480366 |
| tossup_correctness | tier | nationals | 1564 | 0.0393514 | 0.191501 | 0.650533 | 0.569854 |
| tossup_correctness | tier | regionals | 1937 | 0.027327 | 0.177391 | 0.617015 | 0.540744 |
| tossup_correctness | tier | winter | 2750 | 0.0398904 | 0.170204 | 0.643782 | 0.525648 |
| tossup_correctness | category | Current Events | 126 | 0.0693334 | 0.170163 | 0.67508 | 0.519354 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0257453 | 0.165973 | 0.669028 | 0.509932 |
| tossup_correctness | category | Geography | 185 | 0.0420556 | 0.179376 | 0.725498 | 0.5395 |
| tossup_correctness | category | History | 1440 | 0.017415 | 0.171095 | 0.677282 | 0.520387 |
| tossup_correctness | category | Literature | 1422 | 0.0392728 | 0.150496 | 0.598223 | 0.480361 |
| tossup_correctness | category | Mythology | 318 | 0.0489223 | 0.153675 | 0.689778 | 0.481393 |
| tossup_correctness | category | Other Academic | 66 | 0.102477 | 0.201591 | 0.590146 | 0.595493 |
| tossup_correctness | category | Philosophy | 311 | 0.0500784 | 0.177806 | 0.675524 | 0.535865 |
| tossup_correctness | category | Popular Culture | 102 | 0.10869 | 0.116783 | 0.630556 | 0.395625 |
| tossup_correctness | category | Religion | 358 | 0.048486 | 0.192349 | 0.664496 | 0.569765 |
| tossup_correctness | category | Science | 1433 | 0.0342338 | 0.179027 | 0.673064 | 0.540996 |
| tossup_correctness | category | Social Science | 324 | 0.0585299 | 0.183725 | 0.645812 | 0.55418 |
| tossup_correctness | category | Unknown | 1937 | 0.027327 | 0.177391 | 0.617015 | 0.540744 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0648223 | 0.201589 | 0.589286 | 0.594046 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.029886 | 0.182735 | 0.664942 | 0.550128 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0206808 | 0.172373 | 0.659076 | 0.524911 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0155644 | 0.16318 | 0.64479 | 0.504518 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0296834 | 0.170773 | 0.652873 | 0.52486 |
