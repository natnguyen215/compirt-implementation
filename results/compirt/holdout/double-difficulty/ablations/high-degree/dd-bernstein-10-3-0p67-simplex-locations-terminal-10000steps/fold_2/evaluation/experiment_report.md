# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710255 |
| log_loss | 0.493786 |
| ece | 0.0162908 |
| brier | 0.160367 |
| accuracy | 0.775413 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0112347 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.152395 |
| probability_p10 | 0.537682 |
| probability_p50 | 0.785752 |
| probability_p90 | 0.909188 |
| mean_predictive_variance | 0.164363 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100277 |
| joint_tossup_event_log_loss | 6.52085 |
| buzz_position_mae | 0.139417 |
| buzz_position_median_absolute_error | 0.112019 |
| buzz_position_bias | 0.0313609 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.368478 |
| first_buzzer_mean_reciprocal_rank | 0.579119 |
| first_buzzer_log_loss | 1.63032 |
| first_buzzer_events | 9257 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.219203 |
| first_buzzer_team_replay_accuracy | 0.483005 |
| tossup_scorer_player_replay_accuracy | 0.23547 |
| tossup_scorer_team_replay_accuracy | 0.44156 |
| tossup_game_winner_accuracy | 0.703297 |
| tossup_game_margin_mae | 48.1197 |
| tossup_game_zero_margin_mae | 58.4615 |
| tournament_player_ppg_spearman | 0.596369 |
| tournament_player_ppg_mae | 12.4119 |
| tournament_player_ppg_top10_overlap | 0.617241 |
| tournament_player_ppg_top10_random_overlap | 0.280534 |
| tournament_player_ppg_top10_adjusted_overlap | 0.460927 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710255 |
| neg_average_precision | 0.450101 |
| neg_precision | 0.572423 |
| neg_recall | 0.188273 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.254632 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0237445 |
| no_buzz_calibration_error | 0.0106315 |
| no_buzz_brier | 0.0143212 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9360 |
| tossup_replay_seed | 42 |
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
| overall | 9257 | 0.0313609 | 0.00859512 |
| Q1 (0-.2) | 183 | 0.447771 | 0.468809 |
| Q2 (.2-.4) | 955 | 0.279735 | 0.280293 |
| Q3 (.4-.6) | 2239 | 0.132104 | 0.128981 |
| Q4 (.6-.8) | 2875 | 0.00591809 | 0.00642918 |
| Q5 (.8-1) | 3005 | -0.123653 | -0.116825 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0162908 | 0.160367 | 0.710255 | 0.493786 |
| tossup_correctness | tier | fall | 2798 | 0.0328077 | 0.146838 | 0.736183 | 0.460484 |
| tossup_correctness | tier | nationals | 1545 | 0.0232577 | 0.178386 | 0.705511 | 0.536756 |
| tossup_correctness | tier | regionals | 2039 | 0.0210005 | 0.163649 | 0.697388 | 0.502451 |
| tossup_correctness | tier | winter | 2875 | 0.0164988 | 0.161524 | 0.695977 | 0.496959 |
| tossup_correctness | category | Current Events | 129 | 0.0948064 | 0.204758 | 0.683613 | 0.601668 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0388113 | 0.154729 | 0.709068 | 0.481439 |
| tossup_correctness | category | Geography | 180 | 0.0770938 | 0.18652 | 0.764199 | 0.553072 |
| tossup_correctness | category | History | 1454 | 0.01758 | 0.167855 | 0.689642 | 0.512291 |
| tossup_correctness | category | Literature | 1435 | 0.0236839 | 0.136341 | 0.723534 | 0.436562 |
| tossup_correctness | category | Mythology | 324 | 0.0408158 | 0.15056 | 0.70126 | 0.47067 |
| tossup_correctness | category | Other Academic | 71 | 0.090395 | 0.178152 | 0.62854 | 0.54001 |
| tossup_correctness | category | Philosophy | 310 | 0.0288363 | 0.163296 | 0.703275 | 0.498724 |
| tossup_correctness | category | Popular Culture | 108 | 0.107362 | 0.110088 | 0.502604 | 0.382861 |
| tossup_correctness | category | Religion | 361 | 0.0591716 | 0.173949 | 0.701131 | 0.52665 |
| tossup_correctness | category | Science | 1445 | 0.0154691 | 0.167419 | 0.714465 | 0.50859 |
| tossup_correctness | category | Social Science | 327 | 0.0513774 | 0.172194 | 0.752821 | 0.517078 |
| tossup_correctness | category | Unknown | 2039 | 0.0210005 | 0.163649 | 0.697388 | 0.502451 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0453401 | 0.179003 | 0.685232 | 0.534064 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0256024 | 0.170804 | 0.727744 | 0.518458 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0103666 | 0.162197 | 0.721581 | 0.496805 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0236778 | 0.153116 | 0.698284 | 0.4763 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0312975 | 0.161491 | 0.704497 | 0.497973 |
