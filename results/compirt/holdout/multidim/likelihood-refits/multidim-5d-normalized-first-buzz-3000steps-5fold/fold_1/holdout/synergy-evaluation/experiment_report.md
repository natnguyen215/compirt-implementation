# CompIRT Experiment Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.625979 |
| log_loss | 0.8228 |
| ece | 0.220128 |
| brier | 0.261728 |
| accuracy | 0.624546 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.137578 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.294482 |
| probability_p10 | 0.104613 |
| probability_p50 | 0.621022 |
| probability_p90 | 0.913919 |
| mean_predictive_variance | 0.15945 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950998 |
| joint_tossup_event_log_loss | 6.8183 |
| buzz_position_mae | 0.145866 |
| buzz_position_median_absolute_error | 0.125066 |
| buzz_position_bias | -0.044044 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.39041 |
| first_buzzer_mean_reciprocal_rank | 0.59654 |
| first_buzzer_log_loss | 1.63251 |
| first_buzzer_events | 9093 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.00857803 |
| first_buzzer_team_replay_accuracy | 0.0103376 |
| tossup_scorer_player_replay_accuracy | 0.094697 |
| tossup_scorer_team_replay_accuracy | 0.0963203 |
| tossup_game_winner_accuracy | 0.144124 |
| tossup_model_official_winner_accuracy | 0.144105 |
| tossup_game_margin_mae | 54.1017 |
| tossup_game_zero_margin_mae | 55.2922 |
| tournament_player_ppg_spearman | 0.258775 |
| tournament_player_ppg_mae | 22.7774 |
| tournament_player_ppg_top10_overlap | 0.327586 |
| tournament_player_ppg_top10_random_overlap | 0.269705 |
| tournament_player_ppg_top10_adjusted_overlap | 0.0642114 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.625979 |
| neg_average_precision | 0.323381 |
| neg_precision | 0.324544 |
| neg_recall | 0.534905 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0936372 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.062934 |
| no_buzz_calibration_error | 0.047025 |
| no_buzz_brier | 0.0237566 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9240 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 458 |
| first_buzzer_player_replay_accuracy_events | 9093 |
| first_buzzer_team_replay_accuracy_events | 9093 |
| tossup_scorer_player_replay_accuracy_events | 9240 |
| tossup_scorer_team_replay_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.044044 | -0.0575716 |
| Q1 (0-.2) | 167 | 0.347998 | 0.371253 |
| Q2 (.2-.4) | 912 | 0.19599 | 0.196089 |
| Q3 (.4-.6) | 2115 | 0.0597751 | 0.0582184 |
| Q4 (.6-.8) | 2844 | -0.0600317 | -0.0548138 |
| Q5 (.8-1) | 3055 | -0.194123 | -0.187011 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.895076 |
| log_loss | 0.412245 |
| ece | 0.0298494 |
| brier | 0.131336 |
| part_accuracy | 0.813658 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.294656 |
| part_accuracy_macro_team | 0.814874 |
| part_accuracy_macro_bonus | 0.811703 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.339638 |
| probability_p10 | 0.0634943 |
| probability_p50 | 0.457715 |
| probability_p90 | 0.94688 |
| mean_predictive_variance | 0.134528 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.526128 |
| ranked_probability_score | 0.111419 |
| bonus_total_score_log_loss | 0.98312 |
| ppb_mae | 1.96136 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.144124 |
| tossup_game_margin_mae | 54.1017 |
| tossup_game_zero_margin_mae | 55.2922 |
| tossup_game_margin_mae_games | 462 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.220128 | 0.261728 | 0.625979 | 0.8228 |
| tossup_correctness | tier | fall | 2842 | 0.224349 | 0.253586 | 0.63379 | 0.798823 |
| tossup_correctness | tier | nationals | 1564 | 0.190617 | 0.259688 | 0.609004 | 0.787131 |
| tossup_correctness | tier | regionals | 1937 | 0.209003 | 0.254543 | 0.63013 | 0.796262 |
| tossup_correctness | tier | winter | 2750 | 0.248293 | 0.276365 | 0.631563 | 0.886557 |
| tossup_correctness | category | Current Events | 126 | 0.320896 | 0.324802 | 0.564166 | 1.06312 |
| tossup_correctness | category | Fine Arts | 1071 | 0.243737 | 0.271934 | 0.631488 | 0.850555 |
| tossup_correctness | category | Geography | 185 | 0.245248 | 0.296377 | 0.624446 | 0.887632 |
| tossup_correctness | category | History | 1440 | 0.214433 | 0.257299 | 0.622351 | 0.796333 |
| tossup_correctness | category | Literature | 1422 | 0.229858 | 0.253307 | 0.609574 | 0.826545 |
| tossup_correctness | category | Mythology | 318 | 0.279061 | 0.274336 | 0.603675 | 0.824611 |
| tossup_correctness | category | Other Academic | 66 | 0.22359 | 0.239768 | 0.702128 | 0.759513 |
| tossup_correctness | category | Philosophy | 311 | 0.212881 | 0.258296 | 0.665812 | 0.827546 |
| tossup_correctness | category | Popular Culture | 102 | 0.40824 | 0.346726 | 0.469444 | 1.11893 |
| tossup_correctness | category | Religion | 358 | 0.182063 | 0.256556 | 0.650333 | 0.793658 |
| tossup_correctness | category | Science | 1433 | 0.211001 | 0.260257 | 0.62307 | 0.822699 |
| tossup_correctness | category | Social Science | 324 | 0.228235 | 0.264138 | 0.62874 | 0.806404 |
| tossup_correctness | category | Unknown | 1937 | 0.209003 | 0.254543 | 0.63013 | 0.796262 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.45141 | 0.425248 | 0.643557 | 1.3385 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.385622 | 0.364687 | 0.64107 | 1.18657 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.272011 | 0.284524 | 0.645203 | 0.879007 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.202339 | 0.239558 | 0.628397 | 0.747503 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.141503 | 0.22691 | 0.622658 | 0.717199 |
| bonus_part_correctness | aggregate | all | 25260 | 0.0298494 | 0.131336 | 0.895076 | 0.412245 |
| bonus_part_correctness | tier | fall | 8160 | 0.0354803 | 0.130793 | 0.891383 | 0.4091 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0445692 | 0.133375 | 0.889819 | 0.419444 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0293212 | 0.132793 | 0.891971 | 0.417325 |
| bonus_part_correctness | tier | winter | 7713 | 0.0212011 | 0.129827 | 0.895292 | 0.40826 |
| bonus_part_correctness | category | Current Events | 249 | 0.0533178 | 0.125669 | 0.902247 | 0.401066 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0341254 | 0.144441 | 0.875343 | 0.446177 |
| bonus_part_correctness | category | Geography | 459 | 0.0548743 | 0.133649 | 0.890282 | 0.415525 |
| bonus_part_correctness | category | History | 4017 | 0.0284378 | 0.128663 | 0.898256 | 0.404329 |
| bonus_part_correctness | category | Literature | 4047 | 0.0230629 | 0.125683 | 0.901258 | 0.399943 |
| bonus_part_correctness | category | Mythology | 924 | 0.0386834 | 0.143189 | 0.871444 | 0.438701 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0505445 | 0.112991 | 0.917487 | 0.368215 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0478535 | 0.130059 | 0.89806 | 0.408383 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0956281 | 0.139755 | 0.882155 | 0.422579 |
| bonus_part_correctness | category | Religion | 984 | 0.0416084 | 0.128913 | 0.900225 | 0.405137 |
| bonus_part_correctness | category | Science | 3990 | 0.0298779 | 0.130228 | 0.896894 | 0.408656 |
| bonus_part_correctness | category | Social Science | 897 | 0.0463201 | 0.116575 | 0.916063 | 0.372558 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0293212 | 0.132793 | 0.891971 | 0.417325 |
