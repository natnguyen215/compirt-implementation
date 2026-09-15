# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.666696 |
| log_loss | 0.507506 |
| ece | 0.0214079 |
| brier | 0.164469 |
| accuracy | 0.773899 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00385463 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.122317 |
| probability_p10 | 0.593332 |
| probability_p50 | 0.78304 |
| probability_p90 | 0.902615 |
| mean_predictive_variance | 0.16579 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100379 |
| joint_tossup_event_log_loss | 6.83639 |
| buzz_position_mae | 0.159723 |
| buzz_position_median_absolute_error | 0.145222 |
| buzz_position_bias | -0.0677459 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.361784 |
| first_buzzer_mean_reciprocal_rank | 0.572549 |
| first_buzzer_log_loss | 1.66273 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.662115 |
| tossup_scorer_player_top1_accuracy | 0.321367 |
| tossup_scorer_team_top1_accuracy | 0.510954 |
| tossup_game_winner_accuracy | 0.803097 |
| tossup_game_margin_mae | 35.6575 |
| tournament_player_ppg_spearman | 0.71231 |
| tournament_player_ppg_mae | 8.90446 |
| tournament_player_ppg_top10_overlap | 0.672414 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.666696 |
| neg_average_precision | 0.398354 |
| neg_precision | 0.55287 |
| neg_recall | 0.0876437 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0554334 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0929333 |
| no_buzz_calibration_error | 0.0777489 |
| no_buzz_brier | 0.0263363 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0677459 | -0.0844382 |
| Q1 (0-.2) | 192 | 0.369935 | 0.377151 |
| Q2 (.2-.4) | 889 | 0.201352 | 0.198947 |
| Q3 (.4-.6) | 2210 | 0.0471856 | 0.048948 |
| Q4 (.6-.8) | 2869 | -0.0917174 | -0.0860389 |
| Q5 (.8-1) | 2920 | -0.241885 | -0.243295 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0214079 | 0.164469 | 0.666696 | 0.507506 |
| tossup_correctness | tier | fall | 2817 | 0.0209203 | 0.159274 | 0.657738 | 0.495321 |
| tossup_correctness | tier | nationals | 1542 | 0.0689639 | 0.178377 | 0.715572 | 0.537493 |
| tossup_correctness | tier | regionals | 1934 | 0.0153094 | 0.172557 | 0.658768 | 0.525235 |
| tossup_correctness | tier | winter | 2787 | 0.0220196 | 0.156412 | 0.659223 | 0.490929 |
| tossup_correctness | category | Current Events | 125 | 0.103176 | 0.18365 | 0.719595 | 0.547998 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0316099 | 0.162971 | 0.674103 | 0.502164 |
| tossup_correctness | category | Geography | 185 | 0.0505324 | 0.171484 | 0.761678 | 0.519383 |
| tossup_correctness | category | History | 1443 | 0.0423397 | 0.162267 | 0.705579 | 0.499661 |
| tossup_correctness | category | Literature | 1411 | 0.0454002 | 0.151107 | 0.59891 | 0.484209 |
| tossup_correctness | category | Mythology | 320 | 0.0855916 | 0.161567 | 0.59592 | 0.507255 |
| tossup_correctness | category | Other Academic | 64 | 0.0736771 | 0.183884 | 0.601562 | 0.553627 |
| tossup_correctness | category | Philosophy | 312 | 0.0535207 | 0.158848 | 0.585161 | 0.498647 |
| tossup_correctness | category | Popular Culture | 104 | 0.0866787 | 0.138343 | 0.549716 | 0.451375 |
| tossup_correctness | category | Religion | 358 | 0.0400657 | 0.183925 | 0.681201 | 0.549217 |
| tossup_correctness | category | Science | 1431 | 0.0229144 | 0.163231 | 0.686032 | 0.50267 |
| tossup_correctness | category | Social Science | 321 | 0.0404089 | 0.174638 | 0.690019 | 0.526484 |
| tossup_correctness | category | Unknown | 1934 | 0.0153094 | 0.172557 | 0.658768 | 0.525235 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0482668 | 0.192939 | 0.694416 | 0.56909 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0319893 | 0.175981 | 0.700008 | 0.530144 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0208584 | 0.172861 | 0.646942 | 0.528691 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0290444 | 0.156847 | 0.652955 | 0.490217 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0277422 | 0.160229 | 0.673837 | 0.497518 |
