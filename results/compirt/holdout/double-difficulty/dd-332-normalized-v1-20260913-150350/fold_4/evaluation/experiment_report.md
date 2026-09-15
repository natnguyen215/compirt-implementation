# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.726677 |
| log_loss | 0.474419 |
| ece | 0.0120256 |
| brier | 0.153183 |
| accuracy | 0.789105 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0157497 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.139147 |
| probability_p10 | 0.581331 |
| probability_p50 | 0.810531 |
| probability_p90 | 0.917042 |
| mean_predictive_variance | 0.154702 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101581 |
| joint_tossup_event_log_loss | 6.60374 |
| buzz_position_mae | 0.15319 |
| buzz_position_median_absolute_error | 0.136227 |
| buzz_position_bias | -0.0482858 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.35329 |
| first_buzzer_mean_reciprocal_rank | 0.564422 |
| first_buzzer_log_loss | 1.68275 |
| first_buzzer_events | 9270 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.178317 |
| first_buzzer_team_replay_accuracy | 0.412513 |
| tossup_scorer_player_replay_accuracy | 0.208742 |
| tossup_scorer_team_replay_accuracy | 0.403625 |
| tossup_game_winner_accuracy | 0.641921 |
| tossup_model_official_winner_accuracy | 0.663793 |
| tossup_game_margin_mae | 49.2004 |
| tossup_game_zero_margin_mae | 58.0704 |
| tournament_player_ppg_spearman | 0.573974 |
| tournament_player_ppg_mae | 13.2307 |
| tournament_player_ppg_top10_overlap | 0.631034 |
| tournament_player_ppg_top10_random_overlap | 0.291672 |
| tournament_player_ppg_top10_adjusted_overlap | 0.475374 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.726677 |
| neg_average_precision | 0.458391 |
| neg_precision | 0.647177 |
| neg_recall | 0.152784 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.174227 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0295295 |
| no_buzz_calibration_error | 0.0178024 |
| no_buzz_brier | 0.0129018 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9380 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 464 |
| first_buzzer_player_replay_accuracy_events | 9270 |
| first_buzzer_team_replay_accuracy_events | 9270 |
| tossup_scorer_player_replay_accuracy_events | 9380 |
| tossup_scorer_team_replay_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 458 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0482858 | -0.0670925 |
| Q1 (0-.2) | 179 | 0.375143 | 0.385465 |
| Q2 (.2-.4) | 957 | 0.216516 | 0.210053 |
| Q3 (.4-.6) | 2203 | 0.0629345 | 0.0585358 |
| Q4 (.6-.8) | 2978 | -0.0754551 | -0.0755888 |
| Q5 (.8-1) | 2953 | -0.215342 | -0.21068 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0120256 | 0.153183 | 0.726677 | 0.474419 |
| tossup_correctness | tier | fall | 2876 | 0.010879 | 0.14384 | 0.730617 | 0.450847 |
| tossup_correctness | tier | nationals | 1579 | 0.0358224 | 0.173189 | 0.721088 | 0.523273 |
| tossup_correctness | tier | regionals | 1990 | 0.0281615 | 0.155886 | 0.732119 | 0.480181 |
| tossup_correctness | tier | winter | 2825 | 0.0152224 | 0.149607 | 0.719282 | 0.467052 |
| tossup_correctness | category | Current Events | 123 | 0.0696589 | 0.150132 | 0.77036 | 0.462197 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0218323 | 0.150413 | 0.738459 | 0.468822 |
| tossup_correctness | category | Geography | 191 | 0.0786346 | 0.159167 | 0.796867 | 0.489506 |
| tossup_correctness | category | History | 1469 | 0.0291676 | 0.163564 | 0.721127 | 0.497571 |
| tossup_correctness | category | Literature | 1436 | 0.0175438 | 0.13566 | 0.71499 | 0.432509 |
| tossup_correctness | category | Mythology | 325 | 0.0667925 | 0.127499 | 0.686346 | 0.412705 |
| tossup_correctness | category | Other Academic | 67 | 0.0726172 | 0.15679 | 0.684636 | 0.485357 |
| tossup_correctness | category | Philosophy | 322 | 0.0446295 | 0.158978 | 0.683966 | 0.487037 |
| tossup_correctness | category | Popular Culture | 100 | 0.0648263 | 0.104833 | 0.541369 | 0.363707 |
| tossup_correctness | category | Religion | 365 | 0.0380991 | 0.185885 | 0.669142 | 0.556043 |
| tossup_correctness | category | Science | 1456 | 0.0142599 | 0.155581 | 0.726464 | 0.480831 |
| tossup_correctness | category | Social Science | 333 | 0.0502615 | 0.160504 | 0.749931 | 0.494389 |
| tossup_correctness | category | Unknown | 1990 | 0.0281615 | 0.155886 | 0.732119 | 0.480181 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0615673 | 0.15792 | 0.766833 | 0.483047 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0138991 | 0.163588 | 0.703348 | 0.501603 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.024482 | 0.157068 | 0.725624 | 0.483237 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0140075 | 0.147882 | 0.716068 | 0.462353 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.017988 | 0.15197 | 0.740184 | 0.470677 |
