# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.714647 |
| log_loss | 0.491587 |
| ece | 0.0126121 |
| brier | 0.15997 |
| accuracy | 0.774225 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0100465 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.139642 |
| probability_p10 | 0.583622 |
| probability_p50 | 0.810937 |
| probability_p90 | 0.917207 |
| mean_predictive_variance | 0.154779 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102866 |
| joint_tossup_event_log_loss | 6.62213 |
| buzz_position_mae | 0.155044 |
| buzz_position_median_absolute_error | 0.136308 |
| buzz_position_bias | -0.0483728 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.353138 |
| first_buzzer_mean_reciprocal_rank | 0.566676 |
| first_buzzer_log_loss | 1.66501 |
| first_buzzer_events | 9257 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.17612 |
| first_buzzer_team_replay_accuracy | 0.408855 |
| tossup_scorer_player_replay_accuracy | 0.201709 |
| tossup_scorer_team_replay_accuracy | 0.382692 |
| tossup_game_winner_accuracy | 0.646154 |
| tossup_model_official_winner_accuracy | 0.660173 |
| tossup_game_margin_mae | 50.3846 |
| tossup_game_zero_margin_mae | 58.4615 |
| tournament_player_ppg_spearman | 0.569195 |
| tournament_player_ppg_mae | 12.7879 |
| tournament_player_ppg_top10_overlap | 0.558621 |
| tournament_player_ppg_top10_random_overlap | 0.280534 |
| tournament_player_ppg_top10_adjusted_overlap | 0.380153 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.714647 |
| neg_average_precision | 0.448392 |
| neg_precision | 0.596674 |
| neg_recall | 0.13147 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.177697 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.030367 |
| no_buzz_calibration_error | 0.017254 |
| no_buzz_brier | 0.0148778 |
| full_pmf_max_mass_error | 6.66134e-16 |
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
| overall | 9257 | -0.0483728 | -0.067283 |
| Q1 (0-.2) | 183 | 0.38565 | 0.397994 |
| Q2 (.2-.4) | 955 | 0.214922 | 0.215979 |
| Q3 (.4-.6) | 2239 | 0.0615357 | 0.0575984 |
| Q4 (.6-.8) | 2875 | -0.0733144 | -0.0758385 |
| Q5 (.8-1) | 3005 | -0.21651 | -0.21537 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0126121 | 0.15997 | 0.714647 | 0.491587 |
| tossup_correctness | tier | fall | 2798 | 0.0228095 | 0.146372 | 0.740494 | 0.456732 |
| tossup_correctness | tier | nationals | 1545 | 0.0478646 | 0.178501 | 0.713678 | 0.536344 |
| tossup_correctness | tier | regionals | 2039 | 0.013081 | 0.162081 | 0.708046 | 0.497038 |
| tossup_correctness | tier | winter | 2875 | 0.0199458 | 0.161748 | 0.692105 | 0.497589 |
| tossup_correctness | category | Current Events | 129 | 0.0891103 | 0.20838 | 0.690644 | 0.606427 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0268016 | 0.152679 | 0.710197 | 0.475545 |
| tossup_correctness | category | Geography | 180 | 0.0748987 | 0.191196 | 0.752187 | 0.565794 |
| tossup_correctness | category | History | 1454 | 0.0235653 | 0.166661 | 0.696087 | 0.508894 |
| tossup_correctness | category | Literature | 1435 | 0.0238061 | 0.135291 | 0.728852 | 0.432223 |
| tossup_correctness | category | Mythology | 324 | 0.0328964 | 0.152428 | 0.683199 | 0.476315 |
| tossup_correctness | category | Other Academic | 71 | 0.0986813 | 0.177462 | 0.592593 | 0.547913 |
| tossup_correctness | category | Philosophy | 310 | 0.0315422 | 0.160863 | 0.726809 | 0.49037 |
| tossup_correctness | category | Popular Culture | 108 | 0.111058 | 0.106287 | 0.492187 | 0.372597 |
| tossup_correctness | category | Religion | 361 | 0.0178478 | 0.177621 | 0.679907 | 0.533372 |
| tossup_correctness | category | Science | 1445 | 0.0295246 | 0.168373 | 0.721414 | 0.508933 |
| tossup_correctness | category | Social Science | 327 | 0.0470794 | 0.176957 | 0.737327 | 0.528258 |
| tossup_correctness | category | Unknown | 2039 | 0.013081 | 0.162081 | 0.708046 | 0.497038 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0711975 | 0.181551 | 0.659418 | 0.539909 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0277523 | 0.173376 | 0.72274 | 0.522842 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0251348 | 0.161636 | 0.730302 | 0.494845 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0177861 | 0.15182 | 0.709365 | 0.471291 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0221886 | 0.160952 | 0.705399 | 0.495701 |
