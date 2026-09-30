# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.608725 |
| log_loss | 0.54884 |
| ece | 0.0519156 |
| brier | 0.180061 |
| accuracy | 0.751787 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0103376 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.137813 |
| probability_p10 | 0.559141 |
| probability_p50 | 0.78682 |
| probability_p90 | 0.914707 |
| mean_predictive_variance | 0.16338 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.103317 |
| joint_tossup_event_log_loss | 6.95064 |
| buzz_position_mae | 0.163117 |
| buzz_position_median_absolute_error | 0.148617 |
| buzz_position_bias | -0.0709025 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.335093 |
| first_buzzer_mean_reciprocal_rank | 0.55022 |
| first_buzzer_log_loss | 1.70376 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.634554 |
| tossup_scorer_player_top1_accuracy | 0.305952 |
| tossup_scorer_team_top1_accuracy | 0.47132 |
| tossup_game_winner_accuracy | 0.761261 |
| tossup_game_margin_mae | 34.9249 |
| tournament_player_ppg_spearman | 0.668431 |
| tournament_player_ppg_mae | 8.99447 |
| tournament_player_ppg_top10_overlap | 0.648276 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.608725 |
| neg_average_precision | 0.330472 |
| neg_precision | 0.406 |
| neg_recall | 0.0938511 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0574049 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0915454 |
| no_buzz_calibration_error | 0.0756363 |
| no_buzz_brier | 0.026647 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0709025 | -0.0893407 |
| Q1 (0-.2) | 167 | 0.366804 | 0.375631 |
| Q2 (.2-.4) | 912 | 0.209343 | 0.21691 |
| Q3 (.4-.6) | 2115 | 0.0526354 | 0.0537272 |
| Q4 (.6-.8) | 2844 | -0.0897554 | -0.0877876 |
| Q5 (.8-1) | 3055 | -0.246466 | -0.244209 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0519156 | 0.180061 | 0.608725 | 0.54884 |
| tossup_correctness | tier | fall | 2842 | 0.0471414 | 0.168933 | 0.598274 | 0.524263 |
| tossup_correctness | tier | nationals | 1564 | 0.0630428 | 0.199866 | 0.624283 | 0.589343 |
| tossup_correctness | tier | regionals | 1937 | 0.0577988 | 0.18368 | 0.598406 | 0.558297 |
| tossup_correctness | tier | winter | 2750 | 0.0471688 | 0.177749 | 0.605138 | 0.544544 |
| tossup_correctness | category | Current Events | 126 | 0.115387 | 0.195536 | 0.538571 | 0.577313 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0561411 | 0.177719 | 0.601525 | 0.543474 |
| tossup_correctness | category | Geography | 185 | 0.086866 | 0.202053 | 0.661822 | 0.586561 |
| tossup_correctness | category | History | 1440 | 0.0447786 | 0.181137 | 0.635827 | 0.54405 |
| tossup_correctness | category | Literature | 1422 | 0.0696873 | 0.158479 | 0.544712 | 0.513133 |
| tossup_correctness | category | Mythology | 318 | 0.0792337 | 0.164963 | 0.655587 | 0.508493 |
| tossup_correctness | category | Other Academic | 66 | 0.06126 | 0.19423 | 0.655095 | 0.574846 |
| tossup_correctness | category | Philosophy | 311 | 0.067997 | 0.183559 | 0.632202 | 0.556034 |
| tossup_correctness | category | Popular Culture | 102 | 0.190473 | 0.150055 | 0.575926 | 0.471746 |
| tossup_correctness | category | Religion | 358 | 0.070835 | 0.203701 | 0.625433 | 0.598617 |
| tossup_correctness | category | Science | 1433 | 0.0446236 | 0.18845 | 0.618457 | 0.565827 |
| tossup_correctness | category | Social Science | 324 | 0.0701555 | 0.192331 | 0.581793 | 0.576977 |
| tossup_correctness | category | Unknown | 1937 | 0.0577988 | 0.18368 | 0.598406 | 0.558297 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0900324 | 0.209224 | 0.573354 | 0.613586 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0545184 | 0.198815 | 0.597528 | 0.589398 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0464119 | 0.182991 | 0.61384 | 0.551094 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0516935 | 0.170673 | 0.602039 | 0.525491 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0547105 | 0.179579 | 0.612787 | 0.553371 |
