# CompIRT Experiment Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.638571 |
| log_loss | 0.76454 |
| ece | 0.20997 |
| brier | 0.247901 |
| accuracy | 0.642511 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.127533 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.289422 |
| probability_p10 | 0.121959 |
| probability_p50 | 0.637374 |
| probability_p90 | 0.921279 |
| mean_predictive_variance | 0.16031 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0943159 |
| joint_tossup_event_log_loss | 6.71727 |
| buzz_position_mae | 0.145291 |
| buzz_position_median_absolute_error | 0.125107 |
| buzz_position_bias | -0.0472669 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.395925 |
| first_buzzer_mean_reciprocal_rank | 0.602303 |
| first_buzzer_log_loss | 1.59041 |
| first_buzzer_events | 9080 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.0139868 |
| first_buzzer_team_replay_accuracy | 0.0161894 |
| tossup_scorer_player_replay_accuracy | 0.0940347 |
| tossup_scorer_team_replay_accuracy | 0.0957701 |
| tossup_game_winner_accuracy | 0.186667 |
| tossup_model_official_winner_accuracy | 0.188184 |
| tossup_game_margin_mae | 57.6356 |
| tossup_game_zero_margin_mae | 59.1757 |
| tournament_player_ppg_spearman | 0.254011 |
| tournament_player_ppg_mae | 23.1984 |
| tournament_player_ppg_top10_overlap | 0.358621 |
| tournament_player_ppg_top10_random_overlap | 0.291734 |
| tournament_player_ppg_top10_adjusted_overlap | 0.0668237 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.638571 |
| neg_average_precision | 0.33887 |
| neg_precision | 0.326854 |
| neg_recall | 0.523467 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0873719 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0591148 |
| no_buzz_calibration_error | 0.0439305 |
| no_buzz_brier | 0.0207693 |
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
| overall | 9080 | -0.0472669 | -0.0610329 |
| Q1 (0-.2) | 192 | 0.346703 | 0.346819 |
| Q2 (.2-.4) | 889 | 0.185119 | 0.184004 |
| Q3 (.4-.6) | 2210 | 0.0496236 | 0.0464247 |
| Q4 (.6-.8) | 2869 | -0.0709008 | -0.0663369 |
| Q5 (.8-1) | 2920 | -0.194033 | -0.186263 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889469 |
| log_loss | 0.420593 |
| ece | 0.0233037 |
| brier | 0.134192 |
| part_accuracy | 0.808437 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.282752 |
| part_accuracy_macro_team | 0.811544 |
| part_accuracy_macro_bonus | 0.80738 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.327829 |
| probability_p10 | 0.0856896 |
| probability_p50 | 0.475409 |
| probability_p90 | 0.933695 |
| mean_predictive_variance | 0.142517 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509639 |
| ranked_probability_score | 0.117635 |
| bonus_total_score_log_loss | 1.02287 |
| ppb_mae | 2.34471 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.186667 |
| tossup_game_margin_mae | 57.6356 |
| tossup_game_zero_margin_mae | 59.1757 |
| tossup_game_margin_mae_games | 461 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 450 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.20997 | 0.247901 | 0.638571 | 0.76454 |
| tossup_correctness | tier | fall | 2817 | 0.21516 | 0.243844 | 0.640309 | 0.747904 |
| tossup_correctness | tier | nationals | 1542 | 0.181558 | 0.248716 | 0.624724 | 0.73607 |
| tossup_correctness | tier | regionals | 1934 | 0.20172 | 0.246752 | 0.64511 | 0.776827 |
| tossup_correctness | tier | winter | 2787 | 0.231346 | 0.252348 | 0.643908 | 0.788581 |
| tossup_correctness | category | Current Events | 125 | 0.213449 | 0.27389 | 0.59613 | 0.813449 |
| tossup_correctness | category | Fine Arts | 1072 | 0.223117 | 0.265162 | 0.604599 | 0.804234 |
| tossup_correctness | category | Geography | 185 | 0.202921 | 0.275468 | 0.618462 | 0.826723 |
| tossup_correctness | category | History | 1443 | 0.199053 | 0.240551 | 0.658707 | 0.744486 |
| tossup_correctness | category | Literature | 1411 | 0.213337 | 0.23671 | 0.632997 | 0.734497 |
| tossup_correctness | category | Mythology | 320 | 0.289443 | 0.275627 | 0.620795 | 0.80851 |
| tossup_correctness | category | Other Academic | 64 | 0.264418 | 0.250584 | 0.557292 | 0.70707 |
| tossup_correctness | category | Philosophy | 312 | 0.240093 | 0.245438 | 0.656323 | 0.729301 |
| tossup_correctness | category | Popular Culture | 104 | 0.346393 | 0.296597 | 0.587358 | 0.888945 |
| tossup_correctness | category | Religion | 358 | 0.212421 | 0.25397 | 0.665699 | 0.762569 |
| tossup_correctness | category | Science | 1431 | 0.194968 | 0.240308 | 0.637065 | 0.758828 |
| tossup_correctness | category | Social Science | 321 | 0.192313 | 0.238927 | 0.661445 | 0.714513 |
| tossup_correctness | category | Unknown | 1934 | 0.20172 | 0.246752 | 0.64511 | 0.776827 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.441191 | 0.381644 | 0.728127 | 1.20971 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.360382 | 0.333894 | 0.693239 | 1.02267 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.257883 | 0.270917 | 0.657135 | 0.828416 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.178947 | 0.225048 | 0.637416 | 0.693115 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.149179 | 0.21796 | 0.615728 | 0.678514 |
| bonus_part_correctness | aggregate | all | 25365 | 0.0233037 | 0.134192 | 0.889469 | 0.420593 |
| bonus_part_correctness | tier | fall | 8094 | 0.0254303 | 0.134587 | 0.885934 | 0.419781 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0333558 | 0.14324 | 0.873895 | 0.446031 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0234554 | 0.131198 | 0.891 | 0.415072 |
| bonus_part_correctness | tier | winter | 7899 | 0.028889 | 0.131051 | 0.894773 | 0.411809 |
| bonus_part_correctness | category | Current Events | 243 | 0.0642096 | 0.126146 | 0.898645 | 0.406498 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0242577 | 0.14357 | 0.873933 | 0.445855 |
| bonus_part_correctness | category | Geography | 456 | 0.0672414 | 0.137848 | 0.884028 | 0.427869 |
| bonus_part_correctness | category | History | 4050 | 0.0336292 | 0.134155 | 0.891061 | 0.418326 |
| bonus_part_correctness | category | Literature | 4029 | 0.0358407 | 0.131045 | 0.894912 | 0.412569 |
| bonus_part_correctness | category | Mythology | 936 | 0.0380172 | 0.139329 | 0.874254 | 0.432737 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0562281 | 0.115251 | 0.914785 | 0.373473 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0465171 | 0.152578 | 0.860438 | 0.464143 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0316669 | 0.132904 | 0.886162 | 0.417073 |
| bonus_part_correctness | category | Religion | 1014 | 0.0329647 | 0.129506 | 0.896177 | 0.408582 |
| bonus_part_correctness | category | Science | 4059 | 0.0258808 | 0.133515 | 0.890092 | 0.418902 |
| bonus_part_correctness | category | Social Science | 906 | 0.0536127 | 0.125073 | 0.903839 | 0.39389 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0234554 | 0.131198 | 0.891 | 0.415072 |
