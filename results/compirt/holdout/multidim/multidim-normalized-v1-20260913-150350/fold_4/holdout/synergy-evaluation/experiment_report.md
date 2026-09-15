# CompIRT Experiment Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.635893 |
| log_loss | 0.830145 |
| ece | 0.227098 |
| brier | 0.261324 |
| accuracy | 0.623732 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.149622 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.29671 |
| probability_p10 | 0.0900234 |
| probability_p50 | 0.614423 |
| probability_p90 | 0.912391 |
| mean_predictive_variance | 0.158759 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0949591 |
| joint_tossup_event_log_loss | 6.84133 |
| buzz_position_mae | 0.145611 |
| buzz_position_median_absolute_error | 0.127451 |
| buzz_position_bias | -0.0399681 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.396764 |
| first_buzzer_mean_reciprocal_rank | 0.602402 |
| first_buzzer_log_loss | 1.62221 |
| first_buzzer_events | 9270 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.0111111 |
| first_buzzer_team_replay_accuracy | 0.0132686 |
| tossup_scorer_player_replay_accuracy | 0.0902985 |
| tossup_scorer_team_replay_accuracy | 0.0924307 |
| tossup_game_winner_accuracy | 0.189956 |
| tossup_model_official_winner_accuracy | 0.185345 |
| tossup_game_margin_mae | 56.3006 |
| tossup_game_zero_margin_mae | 58.0704 |
| tournament_player_ppg_spearman | 0.266308 |
| tournament_player_ppg_mae | 23.4198 |
| tournament_player_ppg_top10_overlap | 0.365517 |
| tournament_player_ppg_top10_random_overlap | 0.291672 |
| tournament_player_ppg_top10_adjusted_overlap | 0.101004 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.635893 |
| neg_average_precision | 0.323135 |
| neg_precision | 0.310156 |
| neg_recall | 0.539267 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0916629 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0601436 |
| no_buzz_calibration_error | 0.0484165 |
| no_buzz_brier | 0.0204414 |
| full_pmf_max_mass_error | 5.55112e-16 |
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
| overall | 9270 | -0.0399681 | -0.0540757 |
| Q1 (0-.2) | 179 | 0.341325 | 0.337011 |
| Q2 (.2-.4) | 957 | 0.196994 | 0.185854 |
| Q3 (.4-.6) | 2203 | 0.0605842 | 0.0560344 |
| Q4 (.6-.8) | 2978 | -0.0615475 | -0.0569522 |
| Q5 (.8-1) | 2953 | -0.193127 | -0.185532 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897276 |
| log_loss | 0.409278 |
| ece | 0.0346524 |
| brier | 0.130243 |
| part_accuracy | 0.816052 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.290497 |
| part_accuracy_macro_team | 0.82204 |
| part_accuracy_macro_bonus | 0.808883 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.339839 |
| probability_p10 | 0.0633799 |
| probability_p50 | 0.459827 |
| probability_p90 | 0.948638 |
| mean_predictive_variance | 0.134427 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.529344 |
| ranked_probability_score | 0.113508 |
| bonus_total_score_log_loss | 1.00018 |
| ppb_mae | 1.86663 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.189956 |
| tossup_game_margin_mae | 56.3006 |
| tossup_game_zero_margin_mae | 58.0704 |
| tossup_game_margin_mae_games | 469 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 458 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.227098 | 0.261324 | 0.635893 | 0.830145 |
| tossup_correctness | tier | fall | 2876 | 0.245605 | 0.259197 | 0.638322 | 0.823975 |
| tossup_correctness | tier | nationals | 1579 | 0.177722 | 0.251569 | 0.636498 | 0.771146 |
| tossup_correctness | tier | regionals | 1990 | 0.22459 | 0.262551 | 0.640723 | 0.848624 |
| tossup_correctness | tier | winter | 2825 | 0.243996 | 0.268077 | 0.63586 | 0.856387 |
| tossup_correctness | category | Current Events | 123 | 0.253499 | 0.260632 | 0.667645 | 0.776349 |
| tossup_correctness | category | Fine Arts | 1093 | 0.22937 | 0.267921 | 0.640007 | 0.857336 |
| tossup_correctness | category | Geography | 191 | 0.237757 | 0.305748 | 0.560478 | 0.91163 |
| tossup_correctness | category | History | 1469 | 0.195896 | 0.242437 | 0.659372 | 0.751064 |
| tossup_correctness | category | Literature | 1436 | 0.254943 | 0.258952 | 0.624997 | 0.845715 |
| tossup_correctness | category | Mythology | 325 | 0.333942 | 0.308036 | 0.521254 | 1.00138 |
| tossup_correctness | category | Other Academic | 67 | 0.283299 | 0.279599 | 0.641509 | 0.865913 |
| tossup_correctness | category | Philosophy | 322 | 0.238238 | 0.256194 | 0.667182 | 0.781778 |
| tossup_correctness | category | Popular Culture | 100 | 0.368248 | 0.299688 | 0.53524 | 0.937218 |
| tossup_correctness | category | Religion | 365 | 0.224732 | 0.249838 | 0.664004 | 0.769051 |
| tossup_correctness | category | Science | 1456 | 0.222223 | 0.262942 | 0.614552 | 0.837349 |
| tossup_correctness | category | Social Science | 333 | 0.215325 | 0.250346 | 0.678921 | 0.761083 |
| tossup_correctness | category | Unknown | 1990 | 0.22459 | 0.262551 | 0.640723 | 0.848624 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.502606 | 0.439818 | 0.708789 | 1.41367 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.410041 | 0.371785 | 0.65707 | 1.18375 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.290928 | 0.287622 | 0.662663 | 0.922224 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.195396 | 0.235018 | 0.648595 | 0.73023 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.148461 | 0.221616 | 0.6213 | 0.712246 |
| bonus_part_correctness | aggregate | all | 25866 | 0.0346524 | 0.130243 | 0.897276 | 0.409278 |
| bonus_part_correctness | tier | fall | 8259 | 0.030264 | 0.129325 | 0.893913 | 0.40572 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0571466 | 0.139884 | 0.882746 | 0.439549 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0472323 | 0.129445 | 0.90086 | 0.407646 |
| bonus_part_correctness | tier | winter | 7983 | 0.0190393 | 0.126705 | 0.901296 | 0.398273 |
| bonus_part_correctness | category | Current Events | 258 | 0.0692231 | 0.150046 | 0.869173 | 0.468169 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0294123 | 0.130447 | 0.895167 | 0.411686 |
| bonus_part_correctness | category | Geography | 450 | 0.0268258 | 0.125741 | 0.898266 | 0.394425 |
| bonus_part_correctness | category | History | 4116 | 0.0350731 | 0.130714 | 0.895639 | 0.410319 |
| bonus_part_correctness | category | Literature | 4092 | 0.0328087 | 0.127495 | 0.90106 | 0.400782 |
| bonus_part_correctness | category | Mythology | 951 | 0.067792 | 0.140558 | 0.87643 | 0.434871 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0523371 | 0.129173 | 0.900754 | 0.403282 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0238509 | 0.129505 | 0.896839 | 0.405637 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0618641 | 0.143212 | 0.870928 | 0.435203 |
| bonus_part_correctness | category | Religion | 1029 | 0.0328601 | 0.127308 | 0.90094 | 0.400651 |
| bonus_part_correctness | category | Science | 4089 | 0.0293005 | 0.1329 | 0.891714 | 0.417803 |
| bonus_part_correctness | category | Social Science | 891 | 0.0369966 | 0.118367 | 0.912441 | 0.376376 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0472323 | 0.129445 | 0.90086 | 0.407646 |
