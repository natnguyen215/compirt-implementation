# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.707467 |
| log_loss | 0.499036 |
| ece | 0.014965 |
| brier | 0.162382 |
| accuracy | 0.770593 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00846805 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.15141 |
| probability_p10 | 0.556347 |
| probability_p50 | 0.809623 |
| probability_p90 | 0.923805 |
| mean_predictive_variance | 0.154291 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0946409 |
| joint_tossup_event_log_loss | 6.45775 |
| buzz_position_mae | 0.141477 |
| buzz_position_median_absolute_error | 0.121228 |
| buzz_position_bias | -0.0192668 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.362477 |
| first_buzzer_mean_reciprocal_rank | 0.575306 |
| first_buzzer_log_loss | 1.64623 |
| first_buzzer_events | 9093 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.208182 |
| first_buzzer_team_replay_accuracy | 0.468052 |
| tossup_scorer_player_replay_accuracy | 0.232576 |
| tossup_scorer_team_replay_accuracy | 0.433983 |
| tossup_game_winner_accuracy | 0.689579 |
| tossup_model_official_winner_accuracy | 0.707424 |
| tossup_game_margin_mae | 46.5584 |
| tossup_game_zero_margin_mae | 55.2922 |
| tournament_player_ppg_spearman | 0.610701 |
| tournament_player_ppg_mae | 12.2554 |
| tournament_player_ppg_top10_overlap | 0.589655 |
| tournament_player_ppg_top10_random_overlap | 0.269705 |
| tournament_player_ppg_top10_adjusted_overlap | 0.442768 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.707467 |
| neg_average_precision | 0.44106 |
| neg_precision | 0.561997 |
| neg_recall | 0.16135 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.176868 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0230869 |
| no_buzz_calibration_error | 0.00717783 |
| no_buzz_brier | 0.0165859 |
| full_pmf_max_mass_error | 5.55112e-16 |
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
| overall | 9093 | -0.0192668 | -0.040668 |
| Q1 (0-.2) | 167 | 0.390536 | 0.404338 |
| Q2 (.2-.4) | 912 | 0.232691 | 0.232039 |
| Q3 (.4-.6) | 2115 | 0.0850793 | 0.083801 |
| Q4 (.6-.8) | 2844 | -0.039909 | -0.0409024 |
| Q5 (.8-1) | 3055 | -0.169908 | -0.164835 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.014965 | 0.162382 | 0.707467 | 0.499036 |
| tossup_correctness | tier | fall | 2842 | 0.0150357 | 0.14967 | 0.724867 | 0.465847 |
| tossup_correctness | tier | nationals | 1564 | 0.0445876 | 0.179493 | 0.715885 | 0.539591 |
| tossup_correctness | tier | regionals | 1937 | 0.025895 | 0.168057 | 0.688399 | 0.513406 |
| tossup_correctness | tier | winter | 2750 | 0.0163364 | 0.161792 | 0.695532 | 0.500149 |
| tossup_correctness | category | Current Events | 126 | 0.0756196 | 0.159235 | 0.721294 | 0.488962 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0237628 | 0.152312 | 0.745505 | 0.471338 |
| tossup_correctness | category | Geography | 185 | 0.0690699 | 0.163836 | 0.791944 | 0.496605 |
| tossup_correctness | category | History | 1440 | 0.0310072 | 0.169098 | 0.700915 | 0.515078 |
| tossup_correctness | category | Literature | 1422 | 0.0208319 | 0.143679 | 0.67542 | 0.455484 |
| tossup_correctness | category | Mythology | 318 | 0.0477206 | 0.154158 | 0.652257 | 0.488344 |
| tossup_correctness | category | Other Academic | 66 | 0.0943518 | 0.174648 | 0.790594 | 0.518103 |
| tossup_correctness | category | Philosophy | 311 | 0.0858781 | 0.171992 | 0.714644 | 0.515497 |
| tossup_correctness | category | Popular Culture | 102 | 0.0628418 | 0.108654 | 0.524074 | 0.381969 |
| tossup_correctness | category | Religion | 358 | 0.0452999 | 0.180051 | 0.711936 | 0.541289 |
| tossup_correctness | category | Science | 1433 | 0.0274966 | 0.173886 | 0.696552 | 0.527904 |
| tossup_correctness | category | Social Science | 324 | 0.0583696 | 0.157236 | 0.781415 | 0.483134 |
| tossup_correctness | category | Unknown | 1937 | 0.025895 | 0.168057 | 0.688399 | 0.513406 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0767328 | 0.208777 | 0.594013 | 0.621263 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0266258 | 0.173607 | 0.718602 | 0.524649 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0274764 | 0.164982 | 0.710986 | 0.504762 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0121398 | 0.156079 | 0.690209 | 0.486085 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0188182 | 0.160563 | 0.719613 | 0.4928 |
