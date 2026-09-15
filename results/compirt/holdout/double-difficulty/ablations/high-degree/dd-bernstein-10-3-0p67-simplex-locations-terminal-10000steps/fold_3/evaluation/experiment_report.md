# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711526 |
| log_loss | 0.486383 |
| ece | 0.0167554 |
| brier | 0.157417 |
| accuracy | 0.782159 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0121145 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.151858 |
| probability_p10 | 0.539961 |
| probability_p50 | 0.78905 |
| probability_p90 | 0.910386 |
| mean_predictive_variance | 0.162558 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0982968 |
| joint_tossup_event_log_loss | 6.46826 |
| buzz_position_mae | 0.137812 |
| buzz_position_median_absolute_error | 0.110849 |
| buzz_position_bias | 0.0239641 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.363326 |
| first_buzzer_mean_reciprocal_rank | 0.577042 |
| first_buzzer_log_loss | 1.63788 |
| first_buzzer_events | 9080 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.215749 |
| first_buzzer_team_replay_accuracy | 0.483811 |
| tossup_scorer_player_replay_accuracy | 0.235575 |
| tossup_scorer_team_replay_accuracy | 0.442082 |
| tossup_game_winner_accuracy | 0.682222 |
| tossup_game_margin_mae | 47.7874 |
| tossup_game_zero_margin_mae | 59.1757 |
| tournament_player_ppg_spearman | 0.592519 |
| tournament_player_ppg_mae | 12.4404 |
| tournament_player_ppg_top10_overlap | 0.613793 |
| tournament_player_ppg_top10_random_overlap | 0.291734 |
| tournament_player_ppg_top10_adjusted_overlap | 0.433451 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711526 |
| neg_average_precision | 0.447729 |
| neg_precision | 0.58209 |
| neg_recall | 0.186782 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.244524 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0260721 |
| no_buzz_calibration_error | 0.0108877 |
| no_buzz_brier | 0.014996 |
| full_pmf_max_mass_error | 4.44089e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9220 |
| tossup_replay_seed | 42 |
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
| overall | 9080 | 0.0239641 | -0.000885743 |
| Q1 (0-.2) | 192 | 0.446703 | 0.454936 |
| Q2 (.2-.4) | 889 | 0.271255 | 0.273092 |
| Q3 (.4-.6) | 2210 | 0.122529 | 0.118791 |
| Q4 (.6-.8) | 2869 | -0.00369481 | -0.00228385 |
| Q5 (.8-1) | 2920 | -0.126543 | -0.119368 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0167554 | 0.157417 | 0.711526 | 0.486383 |
| tossup_correctness | tier | fall | 2817 | 0.0219342 | 0.152978 | 0.708856 | 0.476556 |
| tossup_correctness | tier | nationals | 1542 | 0.0252718 | 0.169927 | 0.723656 | 0.51385 |
| tossup_correctness | tier | regionals | 1934 | 0.0205775 | 0.16222 | 0.71496 | 0.497746 |
| tossup_correctness | tier | winter | 2787 | 0.033375 | 0.151648 | 0.701269 | 0.473234 |
| tossup_correctness | category | Current Events | 125 | 0.0657509 | 0.172645 | 0.770577 | 0.513448 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0223464 | 0.1532 | 0.72777 | 0.475545 |
| tossup_correctness | category | Geography | 185 | 0.0797563 | 0.156229 | 0.794406 | 0.48148 |
| tossup_correctness | category | History | 1443 | 0.0368696 | 0.160644 | 0.724269 | 0.489842 |
| tossup_correctness | category | Literature | 1411 | 0.0414228 | 0.145221 | 0.665817 | 0.459777 |
| tossup_correctness | category | Mythology | 320 | 0.0318279 | 0.154068 | 0.654736 | 0.488437 |
| tossup_correctness | category | Other Academic | 64 | 0.138689 | 0.184769 | 0.660156 | 0.548914 |
| tossup_correctness | category | Philosophy | 312 | 0.0440807 | 0.149441 | 0.663226 | 0.469451 |
| tossup_correctness | category | Popular Culture | 104 | 0.0358855 | 0.123489 | 0.642756 | 0.411309 |
| tossup_correctness | category | Religion | 358 | 0.0202623 | 0.181126 | 0.699922 | 0.541413 |
| tossup_correctness | category | Science | 1431 | 0.0318324 | 0.158048 | 0.708083 | 0.488277 |
| tossup_correctness | category | Social Science | 321 | 0.0427668 | 0.163783 | 0.725584 | 0.504251 |
| tossup_correctness | category | Unknown | 1934 | 0.0205775 | 0.16222 | 0.71496 | 0.497746 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0654574 | 0.187022 | 0.730957 | 0.550491 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0233527 | 0.162093 | 0.752317 | 0.494962 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0177881 | 0.167977 | 0.686441 | 0.514343 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0248438 | 0.15078 | 0.698354 | 0.470499 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0254655 | 0.152575 | 0.724291 | 0.474002 |
