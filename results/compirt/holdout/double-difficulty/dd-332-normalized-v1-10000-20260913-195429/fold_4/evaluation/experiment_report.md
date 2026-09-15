# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.724378 |
| log_loss | 0.476309 |
| ece | 0.0112732 |
| brier | 0.153939 |
| accuracy | 0.785868 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0125135 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147834 |
| probability_p10 | 0.564707 |
| probability_p50 | 0.807051 |
| probability_p90 | 0.919385 |
| mean_predictive_variance | 0.155359 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0951315 |
| joint_tossup_event_log_loss | 6.45976 |
| buzz_position_mae | 0.14112 |
| buzz_position_median_absolute_error | 0.120138 |
| buzz_position_bias | -0.0154183 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.36343 |
| first_buzzer_mean_reciprocal_rank | 0.573736 |
| first_buzzer_log_loss | 1.65097 |
| first_buzzer_events | 9270 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.219957 |
| first_buzzer_team_replay_accuracy | 0.48425 |
| tossup_scorer_player_replay_accuracy | 0.240725 |
| tossup_scorer_team_replay_accuracy | 0.459595 |
| tossup_game_winner_accuracy | 0.676856 |
| tossup_model_official_winner_accuracy | 0.696121 |
| tossup_game_margin_mae | 50.3412 |
| tossup_game_zero_margin_mae | 58.0704 |
| tournament_player_ppg_spearman | 0.619928 |
| tournament_player_ppg_mae | 12.5652 |
| tournament_player_ppg_top10_overlap | 0.641379 |
| tournament_player_ppg_top10_random_overlap | 0.291672 |
| tournament_player_ppg_top10_adjusted_overlap | 0.482657 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.724378 |
| neg_average_precision | 0.45018 |
| neg_precision | 0.596346 |
| neg_recall | 0.170871 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.171806 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0217473 |
| no_buzz_calibration_error | 0.0100202 |
| no_buzz_brier | 0.0122691 |
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
| overall | 9270 | -0.0154183 | -0.0390866 |
| Q1 (0-.2) | 179 | 0.391628 | 0.397742 |
| Q2 (.2-.4) | 957 | 0.235635 | 0.225178 |
| Q3 (.4-.6) | 2203 | 0.0859062 | 0.0828453 |
| Q4 (.6-.8) | 2978 | -0.0419895 | -0.0412986 |
| Q5 (.8-1) | 2953 | -0.170246 | -0.163268 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0112732 | 0.153939 | 0.724378 | 0.476309 |
| tossup_correctness | tier | fall | 2876 | 0.0130737 | 0.144025 | 0.731299 | 0.451411 |
| tossup_correctness | tier | nationals | 1579 | 0.0347603 | 0.174824 | 0.713251 | 0.528277 |
| tossup_correctness | tier | regionals | 1990 | 0.0183567 | 0.15541 | 0.737353 | 0.478478 |
| tossup_correctness | tier | winter | 2825 | 0.020319 | 0.151323 | 0.713108 | 0.471082 |
| tossup_correctness | category | Current Events | 123 | 0.0847238 | 0.143171 | 0.804842 | 0.446304 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0122396 | 0.149547 | 0.739336 | 0.466898 |
| tossup_correctness | category | Geography | 191 | 0.078432 | 0.15863 | 0.785953 | 0.490103 |
| tossup_correctness | category | History | 1469 | 0.0267759 | 0.166035 | 0.710567 | 0.504059 |
| tossup_correctness | category | Literature | 1436 | 0.0181056 | 0.136748 | 0.708251 | 0.436107 |
| tossup_correctness | category | Mythology | 325 | 0.0509297 | 0.131383 | 0.663804 | 0.422841 |
| tossup_correctness | category | Other Academic | 67 | 0.0705016 | 0.162156 | 0.67655 | 0.498 |
| tossup_correctness | category | Philosophy | 322 | 0.0267415 | 0.1593 | 0.68643 | 0.487496 |
| tossup_correctness | category | Popular Culture | 100 | 0.0475015 | 0.105381 | 0.565884 | 0.362452 |
| tossup_correctness | category | Religion | 365 | 0.0756889 | 0.187734 | 0.664191 | 0.56033 |
| tossup_correctness | category | Science | 1456 | 0.0114327 | 0.156453 | 0.721354 | 0.482966 |
| tossup_correctness | category | Social Science | 333 | 0.0246734 | 0.163348 | 0.752812 | 0.498354 |
| tossup_correctness | category | Unknown | 1990 | 0.0183567 | 0.15541 | 0.737353 | 0.478478 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0607521 | 0.160617 | 0.760033 | 0.489579 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0219718 | 0.163389 | 0.70699 | 0.500276 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0160469 | 0.156596 | 0.727335 | 0.482218 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0152227 | 0.148162 | 0.714212 | 0.46353 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0150447 | 0.154316 | 0.73287 | 0.476218 |
