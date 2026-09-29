# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710937 |
| log_loss | 0.485657 |
| ece | 0.0089787 |
| brier | 0.156996 |
| accuracy | 0.784471 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0144273 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147977 |
| probability_p10 | 0.566561 |
| probability_p50 | 0.808526 |
| probability_p90 | 0.919973 |
| mean_predictive_variance | 0.15392 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0948729 |
| joint_tossup_event_log_loss | 6.428 |
| buzz_position_mae | 0.141754 |
| buzz_position_median_absolute_error | 0.121967 |
| buzz_position_bias | -0.0208054 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.364427 |
| first_buzzer_mean_reciprocal_rank | 0.577503 |
| first_buzzer_log_loss | 1.63571 |
| first_buzzer_events | 9080 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.223348 |
| first_buzzer_team_replay_accuracy | 0.485242 |
| tossup_scorer_player_replay_accuracy | 0.241106 |
| tossup_scorer_team_replay_accuracy | 0.445553 |
| tossup_game_winner_accuracy | 0.695556 |
| tossup_model_official_winner_accuracy | 0.706783 |
| tossup_game_margin_mae | 46.6377 |
| tossup_game_zero_margin_mae | 59.1757 |
| tournament_player_ppg_spearman | 0.608659 |
| tournament_player_ppg_mae | 12.1543 |
| tournament_player_ppg_top10_overlap | 0.631034 |
| tournament_player_ppg_top10_random_overlap | 0.291734 |
| tournament_player_ppg_top10_adjusted_overlap | 0.458453 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710937 |
| neg_average_precision | 0.448633 |
| neg_precision | 0.619308 |
| neg_recall | 0.162835 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.168905 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0224393 |
| no_buzz_calibration_error | 0.00725495 |
| no_buzz_brier | 0.0143229 |
| full_pmf_max_mass_error | 5.55112e-16 |
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
| overall | 9080 | -0.0208054 | -0.0431333 |
| Q1 (0-.2) | 192 | 0.405738 | 0.411216 |
| Q2 (.2-.4) | 889 | 0.226709 | 0.22372 |
| Q3 (.4-.6) | 2210 | 0.0771788 | 0.0731626 |
| Q4 (.6-.8) | 2869 | -0.0492005 | -0.0478042 |
| Q5 (.8-1) | 2920 | -0.170468 | -0.163254 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0089787 | 0.156996 | 0.710937 | 0.485657 |
| tossup_correctness | tier | fall | 2817 | 0.0172695 | 0.152931 | 0.7034 | 0.477215 |
| tossup_correctness | tier | nationals | 1542 | 0.0319207 | 0.169876 | 0.727061 | 0.5136 |
| tossup_correctness | tier | regionals | 1934 | 0.0218232 | 0.161923 | 0.717308 | 0.496927 |
| tossup_correctness | tier | winter | 2787 | 0.0231808 | 0.150561 | 0.700192 | 0.470909 |
| tossup_correctness | category | Current Events | 125 | 0.064233 | 0.177115 | 0.762592 | 0.523422 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0205947 | 0.152253 | 0.728597 | 0.473509 |
| tossup_correctness | category | Geography | 185 | 0.0462772 | 0.158397 | 0.787692 | 0.485741 |
| tossup_correctness | category | History | 1443 | 0.026132 | 0.159799 | 0.725413 | 0.487472 |
| tossup_correctness | category | Literature | 1411 | 0.0255694 | 0.144601 | 0.662521 | 0.459461 |
| tossup_correctness | category | Mythology | 320 | 0.0493256 | 0.152132 | 0.661298 | 0.482937 |
| tossup_correctness | category | Other Academic | 64 | 0.128758 | 0.18697 | 0.654948 | 0.555226 |
| tossup_correctness | category | Philosophy | 312 | 0.0406996 | 0.148134 | 0.660129 | 0.466875 |
| tossup_correctness | category | Popular Culture | 104 | 0.0453902 | 0.123861 | 0.634233 | 0.413949 |
| tossup_correctness | category | Religion | 358 | 0.0403296 | 0.180904 | 0.700432 | 0.540525 |
| tossup_correctness | category | Science | 1431 | 0.0261239 | 0.158527 | 0.702014 | 0.490493 |
| tossup_correctness | category | Social Science | 321 | 0.0330257 | 0.161136 | 0.727472 | 0.498144 |
| tossup_correctness | category | Unknown | 1934 | 0.0218232 | 0.161923 | 0.717308 | 0.496927 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0443267 | 0.184605 | 0.738291 | 0.544536 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0228658 | 0.16322 | 0.751171 | 0.497466 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0265316 | 0.167982 | 0.685172 | 0.515121 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0186004 | 0.14991 | 0.698529 | 0.468734 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0158089 | 0.151935 | 0.725232 | 0.472519 |
