# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710472 |
| log_loss | 0.486021 |
| ece | 0.00761757 |
| brier | 0.157115 |
| accuracy | 0.784141 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0140969 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.140645 |
| probability_p10 | 0.584307 |
| probability_p50 | 0.813094 |
| probability_p90 | 0.918295 |
| mean_predictive_variance | 0.153136 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101597 |
| joint_tossup_event_log_loss | 6.58321 |
| buzz_position_mae | 0.154889 |
| buzz_position_median_absolute_error | 0.138491 |
| buzz_position_bias | -0.0539685 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.351211 |
| first_buzzer_mean_reciprocal_rank | 0.567336 |
| first_buzzer_log_loss | 1.67206 |
| first_buzzer_events | 9080 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.179075 |
| first_buzzer_team_replay_accuracy | 0.418392 |
| tossup_scorer_player_replay_accuracy | 0.207267 |
| tossup_scorer_team_replay_accuracy | 0.386226 |
| tossup_game_winner_accuracy | 0.671111 |
| tossup_model_official_winner_accuracy | 0.676149 |
| tossup_game_margin_mae | 46.1605 |
| tossup_game_zero_margin_mae | 59.1757 |
| tournament_player_ppg_spearman | 0.545067 |
| tournament_player_ppg_mae | 13.345 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| tournament_player_ppg_top10_random_overlap | 0.291734 |
| tournament_player_ppg_top10_adjusted_overlap | 0.426799 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710472 |
| neg_average_precision | 0.448519 |
| neg_precision | 0.635021 |
| neg_recall | 0.144157 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.171209 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0314012 |
| no_buzz_calibration_error | 0.0162169 |
| no_buzz_brier | 0.0153711 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9220 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 457 |
| first_buzzer_player_replay_accuracy_events | 9080 |
| first_buzzer_team_replay_accuracy_events | 9080 |
| tossup_scorer_player_replay_accuracy_events | 9220 |
| tossup_scorer_team_replay_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 450 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0539685 | -0.0744456 |
| Q1 (0-.2) | 192 | 0.386245 | 0.393765 |
| Q2 (.2-.4) | 889 | 0.207351 | 0.208436 |
| Q3 (.4-.6) | 2210 | 0.0537661 | 0.0521259 |
| Q4 (.6-.8) | 2869 | -0.0835238 | -0.0824219 |
| Q5 (.8-1) | 2920 | -0.214973 | -0.212842 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.00761757 | 0.157115 | 0.710472 | 0.486021 |
| tossup_correctness | tier | fall | 2817 | 0.0130392 | 0.15318 | 0.702848 | 0.477789 |
| tossup_correctness | tier | nationals | 1542 | 0.0357701 | 0.170807 | 0.725283 | 0.51584 |
| tossup_correctness | tier | regionals | 1934 | 0.022122 | 0.162291 | 0.717768 | 0.497579 |
| tossup_correctness | tier | winter | 2787 | 0.0185441 | 0.149924 | 0.699363 | 0.469822 |
| tossup_correctness | category | Current Events | 125 | 0.0701688 | 0.180521 | 0.742629 | 0.533273 |
| tossup_correctness | category | Fine Arts | 1072 | 0.019369 | 0.152306 | 0.726658 | 0.473997 |
| tossup_correctness | category | Geography | 185 | 0.0558479 | 0.160747 | 0.778462 | 0.491078 |
| tossup_correctness | category | History | 1443 | 0.025348 | 0.158975 | 0.727502 | 0.485827 |
| tossup_correctness | category | Literature | 1411 | 0.0285484 | 0.14447 | 0.658481 | 0.459499 |
| tossup_correctness | category | Mythology | 320 | 0.0323705 | 0.151683 | 0.665116 | 0.482442 |
| tossup_correctness | category | Other Academic | 64 | 0.182584 | 0.19091 | 0.643229 | 0.567038 |
| tossup_correctness | category | Philosophy | 312 | 0.0391661 | 0.149019 | 0.658774 | 0.468594 |
| tossup_correctness | category | Popular Culture | 104 | 0.031032 | 0.125479 | 0.606534 | 0.421524 |
| tossup_correctness | category | Religion | 358 | 0.0350283 | 0.178752 | 0.715463 | 0.532928 |
| tossup_correctness | category | Science | 1431 | 0.0183252 | 0.15952 | 0.699299 | 0.493102 |
| tossup_correctness | category | Social Science | 321 | 0.0286651 | 0.159935 | 0.733493 | 0.494041 |
| tossup_correctness | category | Unknown | 1934 | 0.022122 | 0.162291 | 0.717768 | 0.497579 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0859163 | 0.184742 | 0.746912 | 0.544822 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0307657 | 0.163451 | 0.751967 | 0.498019 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0246879 | 0.167318 | 0.685761 | 0.513045 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.015441 | 0.151409 | 0.692969 | 0.472773 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0145416 | 0.151252 | 0.727594 | 0.471065 |
