# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.601724 |
| log_loss | 0.5724 |
| ece | 0.10975 |
| brier | 0.187651 |
| accuracy | 0.739914 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0334412 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.167456 |
| probability_p10 | 0.467913 |
| probability_p50 | 0.708582 |
| probability_p90 | 0.913327 |
| mean_predictive_variance | 0.183401 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.114812 |
| joint_tossup_event_log_loss | 6.90413 |
| buzz_position_mae | 0.188362 |
| buzz_position_median_absolute_error | 0.165352 |
| buzz_position_bias | -0.122933 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.38986 |
| first_buzzer_mean_reciprocal_rank | 0.59325 |
| first_buzzer_log_loss | 1.61829 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.647033 |
| tossup_scorer_player_top1_accuracy | 0.296908 |
| tossup_scorer_team_top1_accuracy | 0.451919 |
| tossup_game_winner_accuracy | 0.778993 |
| tossup_game_margin_mae | 39.0175 |
| tournament_player_ppg_spearman | 0.596783 |
| tournament_player_ppg_mae | 11.0756 |
| tournament_player_ppg_top10_overlap | 0.641379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.601724 |
| neg_average_precision | 0.312435 |
| neg_precision | 0.374798 |
| neg_recall | 0.220847 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0985463 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0931208 |
| no_buzz_calibration_error | 0.0813937 |
| no_buzz_brier | 0.0270519 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.122933 | -0.128897 |
| Q1 (0-.2) | 179 | 0.299542 | 0.29177 |
| Q2 (.2-.4) | 957 | 0.146928 | 0.140158 |
| Q3 (.4-.6) | 2203 | -0.0098747 | -0.0186871 |
| Q4 (.6-.8) | 2978 | -0.146879 | -0.151617 |
| Q5 (.8-1) | 2953 | -0.296192 | -0.288001 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.10975 | 0.187651 | 0.601724 | 0.5724 |
| tossup_correctness | tier | fall | 2876 | 0.0970881 | 0.172972 | 0.579056 | 0.551898 |
| tossup_correctness | tier | nationals | 1579 | 0.105806 | 0.209462 | 0.617289 | 0.605315 |
| tossup_correctness | tier | regionals | 1990 | 0.117981 | 0.193293 | 0.615245 | 0.577004 |
| tossup_correctness | tier | winter | 2825 | 0.125648 | 0.186429 | 0.580978 | 0.57163 |
| tossup_correctness | category | Current Events | 123 | 0.12296 | 0.198346 | 0.590242 | 0.584238 |
| tossup_correctness | category | Fine Arts | 1093 | 0.122506 | 0.188699 | 0.602759 | 0.581093 |
| tossup_correctness | category | Geography | 191 | 0.0663994 | 0.200377 | 0.666025 | 0.595117 |
| tossup_correctness | category | History | 1469 | 0.0798511 | 0.18405 | 0.629484 | 0.562104 |
| tossup_correctness | category | Literature | 1436 | 0.142213 | 0.180076 | 0.533236 | 0.566353 |
| tossup_correctness | category | Mythology | 325 | 0.170959 | 0.176669 | 0.527694 | 0.543587 |
| tossup_correctness | category | Other Academic | 67 | 0.198585 | 0.212721 | 0.619946 | 0.607988 |
| tossup_correctness | category | Philosophy | 322 | 0.143352 | 0.186757 | 0.560635 | 0.590082 |
| tossup_correctness | category | Popular Culture | 100 | 0.183535 | 0.153288 | 0.53524 | 0.480912 |
| tossup_correctness | category | Religion | 365 | 0.0797565 | 0.19491 | 0.642327 | 0.592295 |
| tossup_correctness | category | Science | 1456 | 0.101007 | 0.18778 | 0.591972 | 0.571907 |
| tossup_correctness | category | Social Science | 333 | 0.0939158 | 0.196133 | 0.644947 | 0.582123 |
| tossup_correctness | category | Unknown | 1990 | 0.117981 | 0.193293 | 0.615245 | 0.577004 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.25712 | 0.254804 | 0.515755 | 0.714924 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.193918 | 0.22468 | 0.566464 | 0.649506 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.151427 | 0.201677 | 0.598106 | 0.600037 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.115532 | 0.173545 | 0.637524 | 0.535311 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0512329 | 0.175341 | 0.611108 | 0.555557 |
