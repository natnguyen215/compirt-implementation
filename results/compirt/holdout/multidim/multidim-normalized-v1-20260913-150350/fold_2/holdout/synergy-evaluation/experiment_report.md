# CompIRT Experiment Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.625497 |
| log_loss | 0.816903 |
| ece | 0.219935 |
| brier | 0.261412 |
| accuracy | 0.619099 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.145079 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.290538 |
| probability_p10 | 0.103815 |
| probability_p50 | 0.616161 |
| probability_p90 | 0.907097 |
| mean_predictive_variance | 0.162195 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0957555 |
| joint_tossup_event_log_loss | 6.79486 |
| buzz_position_mae | 0.14565 |
| buzz_position_median_absolute_error | 0.125779 |
| buzz_position_bias | -0.0381238 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.396565 |
| first_buzzer_mean_reciprocal_rank | 0.604003 |
| first_buzzer_log_loss | 1.59599 |
| first_buzzer_events | 9257 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.00822689 |
| first_buzzer_team_replay_accuracy | 0.00985062 |
| tossup_scorer_player_replay_accuracy | 0.0904915 |
| tossup_scorer_team_replay_accuracy | 0.092094 |
| tossup_game_winner_accuracy | 0.138462 |
| tossup_model_official_winner_accuracy | 0.138528 |
| tossup_game_margin_mae | 57.265 |
| tossup_game_zero_margin_mae | 58.4615 |
| tournament_player_ppg_spearman | 0.225162 |
| tournament_player_ppg_mae | 23.4047 |
| tournament_player_ppg_top10_overlap | 0.331034 |
| tournament_player_ppg_top10_random_overlap | 0.280534 |
| tournament_player_ppg_top10_adjusted_overlap | 0.0587342 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.625497 |
| neg_average_precision | 0.325025 |
| neg_precision | 0.314452 |
| neg_recall | 0.521301 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.093734 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.062718 |
| no_buzz_calibration_error | 0.049605 |
| no_buzz_brier | 0.0216847 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9360 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 462 |
| first_buzzer_player_replay_accuracy_events | 9238 |
| first_buzzer_team_replay_accuracy_events | 9238 |
| tossup_scorer_player_replay_accuracy_events | 9360 |
| tossup_scorer_team_replay_accuracy_events | 9360 |
| tossup_game_winner_accuracy_games | 455 |
| tossup_game_margin_mae_games | 468 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 1 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0381238 | -0.0537252 |
| Q1 (0-.2) | 183 | 0.35894 | 0.364321 |
| Q2 (.2-.4) | 955 | 0.1952 | 0.190024 |
| Q3 (.4-.6) | 2239 | 0.060963 | 0.0586064 |
| Q4 (.6-.8) | 2875 | -0.0590179 | -0.0582726 |
| Q5 (.8-1) | 3005 | -0.190294 | -0.181745 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.893986 |
| log_loss | 0.414747 |
| ece | 0.0331832 |
| brier | 0.132227 |
| part_accuracy | 0.812144 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.292777 |
| part_accuracy_macro_team | 0.81594 |
| part_accuracy_macro_bonus | 0.808567 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.340539 |
| probability_p10 | 0.060908 |
| probability_p50 | 0.452959 |
| probability_p90 | 0.945891 |
| mean_predictive_variance | 0.133843 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.523904 |
| ranked_probability_score | 0.112309 |
| bonus_total_score_log_loss | 0.993031 |
| ppb_mae | 1.88191 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.138462 |
| tossup_game_margin_mae | 57.265 |
| tossup_game_zero_margin_mae | 58.4615 |
| tossup_game_margin_mae_games | 468 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 455 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.219935 | 0.261412 | 0.625497 | 0.816903 |
| tossup_correctness | tier | fall | 2798 | 0.242273 | 0.261876 | 0.641885 | 0.82931 |
| tossup_correctness | tier | nationals | 1545 | 0.190727 | 0.257506 | 0.611894 | 0.767793 |
| tossup_correctness | tier | regionals | 2039 | 0.219762 | 0.262299 | 0.621669 | 0.837953 |
| tossup_correctness | tier | winter | 2875 | 0.224146 | 0.26243 | 0.627343 | 0.816291 |
| tossup_correctness | category | Current Events | 129 | 0.266282 | 0.294886 | 0.583018 | 0.885802 |
| tossup_correctness | category | Fine Arts | 1074 | 0.262273 | 0.285303 | 0.605346 | 0.884314 |
| tossup_correctness | category | Geography | 180 | 0.183502 | 0.277558 | 0.600862 | 0.809501 |
| tossup_correctness | category | History | 1454 | 0.207609 | 0.250326 | 0.639519 | 0.777272 |
| tossup_correctness | category | Literature | 1435 | 0.232712 | 0.25395 | 0.597975 | 0.80519 |
| tossup_correctness | category | Mythology | 324 | 0.261127 | 0.271638 | 0.627388 | 0.895737 |
| tossup_correctness | category | Other Academic | 71 | 0.242795 | 0.265854 | 0.592593 | 0.778608 |
| tossup_correctness | category | Philosophy | 310 | 0.228899 | 0.249912 | 0.689132 | 0.749782 |
| tossup_correctness | category | Popular Culture | 108 | 0.423073 | 0.33206 | 0.545139 | 1.00622 |
| tossup_correctness | category | Religion | 361 | 0.242395 | 0.26777 | 0.644559 | 0.800607 |
| tossup_correctness | category | Science | 1445 | 0.192138 | 0.253003 | 0.636346 | 0.792905 |
| tossup_correctness | category | Social Science | 327 | 0.174964 | 0.243966 | 0.665772 | 0.724105 |
| tossup_correctness | category | Unknown | 2039 | 0.219762 | 0.262299 | 0.621669 | 0.837953 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.499462 | 0.430719 | 0.70729 | 1.38374 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.378491 | 0.355191 | 0.658384 | 1.10872 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.267666 | 0.280311 | 0.657289 | 0.877331 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.200656 | 0.240975 | 0.629505 | 0.748607 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.150583 | 0.226769 | 0.598522 | 0.709959 |
| bonus_part_correctness | aggregate | all | 25791 | 0.0331832 | 0.132227 | 0.893986 | 0.414747 |
| bonus_part_correctness | tier | fall | 7995 | 0.0263749 | 0.126894 | 0.898346 | 0.398722 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0599056 | 0.139877 | 0.885081 | 0.435641 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0417539 | 0.136177 | 0.887837 | 0.427154 |
| bonus_part_correctness | tier | winter | 8121 | 0.0221693 | 0.130906 | 0.894549 | 0.411463 |
| bonus_part_correctness | category | Current Events | 216 | 0.0628831 | 0.128089 | 0.893672 | 0.407933 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.040564 | 0.142906 | 0.879642 | 0.440496 |
| bonus_part_correctness | category | Geography | 501 | 0.0266036 | 0.13047 | 0.892996 | 0.408442 |
| bonus_part_correctness | category | History | 4068 | 0.0368009 | 0.130651 | 0.896858 | 0.409206 |
| bonus_part_correctness | category | Literature | 4065 | 0.0252943 | 0.123697 | 0.904493 | 0.393082 |
| bonus_part_correctness | category | Mythology | 945 | 0.0363361 | 0.148807 | 0.861519 | 0.454611 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0685676 | 0.155609 | 0.865782 | 0.47252 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0370086 | 0.129916 | 0.898196 | 0.407571 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0553763 | 0.159704 | 0.840278 | 0.485363 |
| bonus_part_correctness | category | Religion | 1008 | 0.0423564 | 0.129409 | 0.900949 | 0.404136 |
| bonus_part_correctness | category | Science | 4059 | 0.0369864 | 0.129026 | 0.898446 | 0.407823 |
| bonus_part_correctness | category | Social Science | 909 | 0.0316941 | 0.10853 | 0.922087 | 0.353792 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0417539 | 0.136177 | 0.887837 | 0.427154 |
