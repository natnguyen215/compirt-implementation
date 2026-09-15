# CompIRT Experiment Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.635681 |
| log_loss | 0.808871 |
| ece | 0.220271 |
| brier | 0.258067 |
| accuracy | 0.629801 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.135449 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.29347 |
| probability_p10 | 0.103289 |
| probability_p50 | 0.619857 |
| probability_p90 | 0.912607 |
| mean_predictive_variance | 0.160332 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0948929 |
| joint_tossup_event_log_loss | 6.79924 |
| buzz_position_mae | 0.144941 |
| buzz_position_median_absolute_error | 0.12523 |
| buzz_position_bias | -0.0389374 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.402797 |
| first_buzzer_mean_reciprocal_rank | 0.605685 |
| first_buzzer_log_loss | 1.60382 |
| first_buzzer_events | 9295 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.00860678 |
| first_buzzer_team_replay_accuracy | 0.0104357 |
| tossup_scorer_player_replay_accuracy | 0.0932059 |
| tossup_scorer_team_replay_accuracy | 0.0949045 |
| tossup_game_winner_accuracy | 0.137472 |
| tossup_model_official_winner_accuracy | 0.143162 |
| tossup_game_margin_mae | 53.8217 |
| tossup_game_zero_margin_mae | 54.8195 |
| tournament_player_ppg_spearman | 0.214224 |
| tournament_player_ppg_mae | 23.1421 |
| tournament_player_ppg_top10_overlap | 0.286207 |
| tournament_player_ppg_top10_random_overlap | 0.282327 |
| tournament_player_ppg_top10_adjusted_overlap | -0.0157208 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.635681 |
| neg_average_precision | 0.333078 |
| neg_precision | 0.326632 |
| neg_recall | 0.543538 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0907123 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0633615 |
| no_buzz_calibration_error | 0.0500918 |
| no_buzz_brier | 0.0226461 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9420 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 468 |
| first_buzzer_player_replay_accuracy_events | 9295 |
| first_buzzer_team_replay_accuracy_events | 9295 |
| tossup_scorer_player_replay_accuracy_events | 9420 |
| tossup_scorer_team_replay_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0389374 | -0.0530772 |
| Q1 (0-.2) | 197 | 0.337501 | 0.339786 |
| Q2 (.2-.4) | 985 | 0.193106 | 0.187103 |
| Q3 (.4-.6) | 2251 | 0.0592124 | 0.0544448 |
| Q4 (.6-.8) | 2866 | -0.062483 | -0.0573119 |
| Q5 (.8-1) | 2996 | -0.191199 | -0.183343 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.887122 |
| log_loss | 0.42405 |
| ece | 0.0166041 |
| brier | 0.134864 |
| part_accuracy | 0.809861 |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.291425 |
| part_accuracy_macro_team | 0.811903 |
| part_accuracy_macro_bonus | 0.805403 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.326718 |
| probability_p10 | 0.0859546 |
| probability_p50 | 0.478096 |
| probability_p90 | 0.932025 |
| mean_predictive_variance | 0.143243 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.51313 |
| ranked_probability_score | 0.117189 |
| bonus_total_score_log_loss | 1.02505 |
| ppb_mae | 2.36785 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.137472 |
| tossup_game_margin_mae | 53.8217 |
| tossup_game_zero_margin_mae | 54.8195 |
| tossup_game_margin_mae_games | 471 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.220271 | 0.258067 | 0.635681 | 0.808871 |
| tossup_correctness | tier | fall | 2933 | 0.249203 | 0.254557 | 0.650265 | 0.81313 |
| tossup_correctness | tier | nationals | 1584 | 0.168285 | 0.252947 | 0.616787 | 0.769935 |
| tossup_correctness | tier | regionals | 1886 | 0.217961 | 0.263941 | 0.63736 | 0.829775 |
| tossup_correctness | tier | winter | 2892 | 0.230142 | 0.260599 | 0.642171 | 0.812244 |
| tossup_correctness | category | Current Events | 124 | 0.262217 | 0.275882 | 0.586889 | 0.856001 |
| tossup_correctness | category | Fine Arts | 1103 | 0.220756 | 0.247077 | 0.660076 | 0.771412 |
| tossup_correctness | category | Geography | 197 | 0.245 | 0.300376 | 0.619814 | 0.937449 |
| tossup_correctness | category | History | 1491 | 0.219877 | 0.241518 | 0.665021 | 0.772663 |
| tossup_correctness | category | Literature | 1472 | 0.223381 | 0.252407 | 0.606354 | 0.796917 |
| tossup_correctness | category | Mythology | 332 | 0.294876 | 0.274812 | 0.617981 | 0.858599 |
| tossup_correctness | category | Other Academic | 69 | 0.27445 | 0.280618 | 0.569005 | 0.819017 |
| tossup_correctness | category | Philosophy | 324 | 0.220374 | 0.256582 | 0.581467 | 0.758783 |
| tossup_correctness | category | Popular Culture | 102 | 0.398492 | 0.382151 | 0.444983 | 1.2149 |
| tossup_correctness | category | Religion | 372 | 0.188925 | 0.273854 | 0.617284 | 0.84513 |
| tossup_correctness | category | Science | 1487 | 0.212861 | 0.254079 | 0.638517 | 0.791738 |
| tossup_correctness | category | Social Science | 336 | 0.221723 | 0.270775 | 0.64089 | 0.844266 |
| tossup_correctness | category | Unknown | 1886 | 0.217961 | 0.263941 | 0.63736 | 0.829775 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.485614 | 0.421197 | 0.678249 | 1.3236 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.388184 | 0.356168 | 0.663306 | 1.12967 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.274953 | 0.283812 | 0.643806 | 0.875379 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.193286 | 0.234051 | 0.643783 | 0.725883 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.138294 | 0.218718 | 0.6316 | 0.698974 |
| bonus_part_correctness | aggregate | all | 25818 | 0.0166041 | 0.134864 | 0.887122 | 0.42405 |
| bonus_part_correctness | tier | fall | 8415 | 0.0263991 | 0.136379 | 0.882054 | 0.425145 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0179744 | 0.139363 | 0.87302 | 0.44003 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0238859 | 0.132481 | 0.887987 | 0.419741 |
| bonus_part_correctness | tier | winter | 8154 | 0.0216623 | 0.132475 | 0.890701 | 0.417408 |
| bonus_part_correctness | category | Current Events | 258 | 0.0556625 | 0.106461 | 0.926502 | 0.356229 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.022781 | 0.14429 | 0.872915 | 0.447988 |
| bonus_part_correctness | category | Geography | 453 | 0.0339919 | 0.140057 | 0.870166 | 0.440815 |
| bonus_part_correctness | category | History | 4176 | 0.0231263 | 0.138166 | 0.882152 | 0.431576 |
| bonus_part_correctness | category | Literature | 4197 | 0.0294431 | 0.123643 | 0.903382 | 0.395151 |
| bonus_part_correctness | category | Mythology | 951 | 0.0402188 | 0.148188 | 0.863618 | 0.450399 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0735019 | 0.114207 | 0.922576 | 0.368502 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0338867 | 0.143201 | 0.873593 | 0.445868 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0643032 | 0.15302 | 0.855088 | 0.459266 |
| bonus_part_correctness | category | Religion | 1041 | 0.0284359 | 0.136803 | 0.88257 | 0.431282 |
| bonus_part_correctness | category | Science | 4152 | 0.0189606 | 0.134853 | 0.886693 | 0.424014 |
| bonus_part_correctness | category | Social Science | 915 | 0.0368472 | 0.133201 | 0.887024 | 0.421952 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0238859 | 0.132481 | 0.887987 | 0.419741 |
