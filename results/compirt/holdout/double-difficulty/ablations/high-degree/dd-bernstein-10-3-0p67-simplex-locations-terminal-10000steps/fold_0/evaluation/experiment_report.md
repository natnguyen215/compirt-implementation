# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710459 |
| log_loss | 0.492433 |
| ece | 0.012942 |
| brier | 0.160172 |
| accuracy | 0.776116 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0108661 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.153655 |
| probability_p10 | 0.533348 |
| probability_p50 | 0.79085 |
| probability_p90 | 0.911859 |
| mean_predictive_variance | 0.162437 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0997374 |
| joint_tossup_event_log_loss | 6.48931 |
| buzz_position_mae | 0.139678 |
| buzz_position_median_absolute_error | 0.113228 |
| buzz_position_bias | 0.0295403 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.381711 |
| first_buzzer_mean_reciprocal_rank | 0.588892 |
| first_buzzer_log_loss | 1.61284 |
| first_buzzer_events | 9295 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.220334 |
| first_buzzer_team_replay_accuracy | 0.475847 |
| tossup_scorer_player_replay_accuracy | 0.240552 |
| tossup_scorer_team_replay_accuracy | 0.447028 |
| tossup_game_winner_accuracy | 0.667406 |
| tossup_game_margin_mae | 50.5626 |
| tossup_game_zero_margin_mae | 54.8195 |
| tournament_player_ppg_spearman | 0.579014 |
| tournament_player_ppg_mae | 12.6166 |
| tournament_player_ppg_top10_overlap | 0.596552 |
| tournament_player_ppg_top10_random_overlap | 0.282327 |
| tournament_player_ppg_top10_adjusted_overlap | 0.43569 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710459 |
| neg_average_precision | 0.444813 |
| neg_precision | 0.569083 |
| neg_recall | 0.190651 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.248265 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0259634 |
| no_buzz_calibration_error | 0.0126937 |
| no_buzz_brier | 0.0151146 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9420 |
| tossup_replay_seed | 42 |
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
| overall | 9295 | 0.0295403 | 0.00418849 |
| Q1 (0-.2) | 197 | 0.423985 | 0.427974 |
| Q2 (.2-.4) | 985 | 0.273336 | 0.26829 |
| Q3 (.4-.6) | 2251 | 0.128575 | 0.127243 |
| Q4 (.6-.8) | 2866 | 0.00158958 | 0.00139365 |
| Q5 (.8-1) | 2996 | -0.124219 | -0.117257 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.012942 | 0.160172 | 0.710459 | 0.492433 |
| tossup_correctness | tier | fall | 2933 | 0.0352562 | 0.149554 | 0.711649 | 0.466344 |
| tossup_correctness | tier | nationals | 1584 | 0.0292542 | 0.178947 | 0.694053 | 0.54055 |
| tossup_correctness | tier | regionals | 1886 | 0.0166932 | 0.169852 | 0.708208 | 0.514096 |
| tossup_correctness | tier | winter | 2892 | 0.0173004 | 0.154343 | 0.719059 | 0.47841 |
| tossup_correctness | category | Current Events | 124 | 0.0917766 | 0.169252 | 0.689213 | 0.520087 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0388703 | 0.160896 | 0.706908 | 0.496369 |
| tossup_correctness | category | Geography | 197 | 0.0644668 | 0.168756 | 0.791958 | 0.510477 |
| tossup_correctness | category | History | 1491 | 0.0367876 | 0.151249 | 0.713318 | 0.469696 |
| tossup_correctness | category | Literature | 1472 | 0.0289545 | 0.137542 | 0.727058 | 0.438408 |
| tossup_correctness | category | Mythology | 332 | 0.0459778 | 0.144178 | 0.694086 | 0.454936 |
| tossup_correctness | category | Other Academic | 69 | 0.106928 | 0.166045 | 0.733032 | 0.498645 |
| tossup_correctness | category | Philosophy | 324 | 0.0398308 | 0.151387 | 0.671518 | 0.472958 |
| tossup_correctness | category | Popular Culture | 102 | 0.0791365 | 0.149587 | 0.445675 | 0.485214 |
| tossup_correctness | category | Religion | 372 | 0.0378011 | 0.183766 | 0.71135 | 0.54511 |
| tossup_correctness | category | Science | 1487 | 0.0300873 | 0.172762 | 0.679095 | 0.523265 |
| tossup_correctness | category | Social Science | 336 | 0.040369 | 0.178237 | 0.724068 | 0.536678 |
| tossup_correctness | category | Unknown | 1886 | 0.0166932 | 0.169852 | 0.708208 | 0.514096 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0545515 | 0.168915 | 0.698408 | 0.519311 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0229547 | 0.171747 | 0.718211 | 0.517921 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0292302 | 0.162364 | 0.694252 | 0.499356 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0227578 | 0.155159 | 0.696294 | 0.480778 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0161233 | 0.158939 | 0.731004 | 0.488233 |
