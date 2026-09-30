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
| auc | 0.891193 |
| log_loss | 0.418663 |
| ece | 0.02631 |
| brier | 0.133331 |
| part_accuracy | 0.810369 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.284814 |
| part_accuracy_macro_team | 0.814372 |
| part_accuracy_macro_bonus | 0.801633 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.32738 |
| probability_p10 | 0.0853362 |
| probability_p50 | 0.467311 |
| probability_p90 | 0.932822 |
| mean_predictive_variance | 0.142822 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.515658 |
| ranked_probability_score | 0.117406 |
| bonus_total_score_log_loss | 1.02344 |
| ppb_mae | 2.31844 |
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
| bonus_part_correctness | aggregate | all | 25866 | 0.02631 | 0.133331 | 0.891193 | 0.418663 |
| bonus_part_correctness | tier | fall | 8259 | 0.0319983 | 0.133351 | 0.887134 | 0.418071 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0229614 | 0.141993 | 0.87321 | 0.444168 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0260578 | 0.13286 | 0.891082 | 0.418623 |
| bonus_part_correctness | tier | winter | 7983 | 0.0246445 | 0.129109 | 0.897915 | 0.405991 |
| bonus_part_correctness | category | Current Events | 258 | 0.0655844 | 0.144904 | 0.879158 | 0.450111 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.026697 | 0.137442 | 0.884054 | 0.430551 |
| bonus_part_correctness | category | Geography | 450 | 0.0381345 | 0.130698 | 0.888948 | 0.413128 |
| bonus_part_correctness | category | History | 4116 | 0.0319897 | 0.132195 | 0.893291 | 0.413805 |
| bonus_part_correctness | category | Literature | 4092 | 0.0261602 | 0.131459 | 0.892033 | 0.414763 |
| bonus_part_correctness | category | Mythology | 951 | 0.067897 | 0.141379 | 0.875795 | 0.436314 |
| bonus_part_correctness | category | Other Academic | 276 | 0.047086 | 0.118026 | 0.915098 | 0.376525 |
| bonus_part_correctness | category | Philosophy | 957 | 0.031105 | 0.140681 | 0.88019 | 0.436211 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0495877 | 0.132094 | 0.891093 | 0.410607 |
| bonus_part_correctness | category | Religion | 1029 | 0.0520168 | 0.125271 | 0.904276 | 0.396547 |
| bonus_part_correctness | category | Science | 4089 | 0.0227182 | 0.136008 | 0.885978 | 0.426236 |
| bonus_part_correctness | category | Social Science | 891 | 0.0357529 | 0.119882 | 0.908656 | 0.381798 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0260578 | 0.13286 | 0.891082 | 0.418623 |
