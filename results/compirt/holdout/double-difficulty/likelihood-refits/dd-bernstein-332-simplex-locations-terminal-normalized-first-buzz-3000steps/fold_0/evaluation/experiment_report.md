# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.715926 |
| log_loss | 0.489687 |
| ece | 0.0130247 |
| brier | 0.15918 |
| accuracy | 0.776762 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0115116 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.139542 |
| probability_p10 | 0.582291 |
| probability_p50 | 0.815234 |
| probability_p90 | 0.916691 |
| mean_predictive_variance | 0.153756 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102274 |
| joint_tossup_event_log_loss | 6.61322 |
| buzz_position_mae | 0.15537 |
| buzz_position_median_absolute_error | 0.13828 |
| buzz_position_bias | -0.0475459 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.357181 |
| first_buzzer_mean_reciprocal_rank | 0.569737 |
| first_buzzer_log_loss | 1.6655 |
| first_buzzer_events | 9295 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.177192 |
| first_buzzer_team_replay_accuracy | 0.402044 |
| tossup_scorer_player_replay_accuracy | 0.211465 |
| tossup_scorer_team_replay_accuracy | 0.392887 |
| tossup_game_winner_accuracy | 0.654102 |
| tossup_model_official_winner_accuracy | 0.67735 |
| tossup_game_margin_mae | 49.4904 |
| tossup_game_zero_margin_mae | 54.8195 |
| tournament_player_ppg_spearman | 0.54796 |
| tournament_player_ppg_mae | 12.8284 |
| tournament_player_ppg_top10_overlap | 0.596552 |
| tournament_player_ppg_top10_random_overlap | 0.282327 |
| tournament_player_ppg_top10_adjusted_overlap | 0.444004 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.715926 |
| neg_average_precision | 0.44876 |
| neg_precision | 0.606362 |
| neg_recall | 0.13978 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.175218 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0331827 |
| no_buzz_calibration_error | 0.0199131 |
| no_buzz_brier | 0.0156462 |
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
| overall | 9295 | -0.0475459 | -0.0685619 |
| Q1 (0-.2) | 197 | 0.367151 | 0.370149 |
| Q2 (.2-.4) | 985 | 0.212735 | 0.205808 |
| Q3 (.4-.6) | 2251 | 0.0618052 | 0.0597199 |
| Q4 (.6-.8) | 2866 | -0.0755553 | -0.0778365 |
| Q5 (.8-1) | 2996 | -0.215752 | -0.212694 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0130247 | 0.15918 | 0.715926 | 0.489687 |
| tossup_correctness | tier | fall | 2933 | 0.0110293 | 0.147861 | 0.712451 | 0.462283 |
| tossup_correctness | tier | nationals | 1584 | 0.040146 | 0.175886 | 0.711155 | 0.531931 |
| tossup_correctness | tier | regionals | 1886 | 0.0285129 | 0.170519 | 0.711561 | 0.515392 |
| tossup_correctness | tier | winter | 2892 | 0.0121186 | 0.154115 | 0.720996 | 0.477578 |
| tossup_correctness | category | Current Events | 124 | 0.106583 | 0.169482 | 0.675338 | 0.524325 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0214265 | 0.161472 | 0.709934 | 0.497256 |
| tossup_correctness | category | Geography | 197 | 0.0752701 | 0.171035 | 0.78683 | 0.517775 |
| tossup_correctness | category | History | 1491 | 0.0171648 | 0.14824 | 0.726576 | 0.4617 |
| tossup_correctness | category | Literature | 1472 | 0.0276985 | 0.137701 | 0.730035 | 0.437528 |
| tossup_correctness | category | Mythology | 332 | 0.0198716 | 0.140986 | 0.692712 | 0.447868 |
| tossup_correctness | category | Other Academic | 69 | 0.0775224 | 0.166984 | 0.702489 | 0.507186 |
| tossup_correctness | category | Philosophy | 324 | 0.0293421 | 0.147915 | 0.691773 | 0.463294 |
| tossup_correctness | category | Popular Culture | 102 | 0.0531024 | 0.1483 | 0.431142 | 0.484542 |
| tossup_correctness | category | Religion | 372 | 0.0475316 | 0.182823 | 0.718996 | 0.54149 |
| tossup_correctness | category | Science | 1487 | 0.0275766 | 0.169498 | 0.688741 | 0.515548 |
| tossup_correctness | category | Social Science | 336 | 0.0410663 | 0.178594 | 0.730593 | 0.536937 |
| tossup_correctness | category | Unknown | 1886 | 0.0285129 | 0.170519 | 0.711561 | 0.515392 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0685664 | 0.16736 | 0.694562 | 0.522705 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0269102 | 0.172544 | 0.716782 | 0.520173 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0191933 | 0.161137 | 0.700183 | 0.495223 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0158393 | 0.152679 | 0.703434 | 0.475131 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0242566 | 0.158997 | 0.737085 | 0.487258 |
