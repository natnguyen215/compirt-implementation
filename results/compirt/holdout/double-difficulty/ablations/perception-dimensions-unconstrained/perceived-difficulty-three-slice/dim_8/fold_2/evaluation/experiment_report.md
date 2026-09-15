# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.642606 |
| log_loss | 0.524176 |
| ece | 0.0180489 |
| brier | 0.171566 |
| accuracy | 0.767311 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00313276 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.110582 |
| probability_p10 | 0.621143 |
| probability_p50 | 0.799484 |
| probability_p90 | 0.905191 |
| mean_predictive_variance | 0.159795 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10349 |
| joint_tossup_event_log_loss | 6.93293 |
| buzz_position_mae | 0.161786 |
| buzz_position_median_absolute_error | 0.144208 |
| buzz_position_bias | -0.0672043 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.36837 |
| first_buzzer_mean_reciprocal_rank | 0.576247 |
| first_buzzer_log_loss | 1.65456 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.662526 |
| tossup_scorer_player_top1_accuracy | 0.328678 |
| tossup_scorer_team_top1_accuracy | 0.501386 |
| tossup_game_winner_accuracy | 0.776087 |
| tossup_game_margin_mae | 36.1969 |
| tournament_player_ppg_spearman | 0.707945 |
| tournament_player_ppg_mae | 8.72152 |
| tournament_player_ppg_top10_overlap | 0.651724 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.642606 |
| neg_average_precision | 0.363137 |
| neg_precision | 0.585799 |
| neg_recall | 0.0453504 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0566673 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0985423 |
| no_buzz_calibration_error | 0.0854292 |
| no_buzz_brier | 0.027136 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0672043 | -0.0801095 |
| Q1 (0-.2) | 183 | 0.378012 | 0.38399 |
| Q2 (.2-.4) | 955 | 0.202546 | 0.209841 |
| Q3 (.4-.6) | 2239 | 0.0508518 | 0.0526936 |
| Q4 (.6-.8) | 2875 | -0.0881521 | -0.0807271 |
| Q5 (.8-1) | 3005 | -0.247966 | -0.244298 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0180489 | 0.171566 | 0.642606 | 0.524176 |
| tossup_correctness | tier | fall | 2798 | 0.0180836 | 0.1607 | 0.639712 | 0.499187 |
| tossup_correctness | tier | nationals | 1545 | 0.0351436 | 0.189342 | 0.663192 | 0.561574 |
| tossup_correctness | tier | regionals | 2039 | 0.0340624 | 0.175004 | 0.615565 | 0.533168 |
| tossup_correctness | tier | winter | 2875 | 0.0472732 | 0.17015 | 0.653612 | 0.522022 |
| tossup_correctness | category | Current Events | 129 | 0.0583041 | 0.212899 | 0.640346 | 0.617796 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0385488 | 0.168739 | 0.62507 | 0.518364 |
| tossup_correctness | category | Geography | 180 | 0.116973 | 0.220029 | 0.698786 | 0.632337 |
| tossup_correctness | category | History | 1454 | 0.0257585 | 0.175765 | 0.633543 | 0.532408 |
| tossup_correctness | category | Literature | 1435 | 0.0176736 | 0.145943 | 0.639731 | 0.467457 |
| tossup_correctness | category | Mythology | 324 | 0.0504292 | 0.159932 | 0.616586 | 0.498524 |
| tossup_correctness | category | Other Academic | 71 | 0.145404 | 0.209564 | 0.312636 | 0.618031 |
| tossup_correctness | category | Philosophy | 310 | 0.0546526 | 0.175776 | 0.640804 | 0.533539 |
| tossup_correctness | category | Popular Culture | 108 | 0.107629 | 0.117632 | 0.543403 | 0.39867 |
| tossup_correctness | category | Religion | 361 | 0.0369776 | 0.185148 | 0.625261 | 0.555274 |
| tossup_correctness | category | Science | 1445 | 0.0463809 | 0.177359 | 0.678497 | 0.535355 |
| tossup_correctness | category | Social Science | 327 | 0.0334231 | 0.186702 | 0.678585 | 0.556912 |
| tossup_correctness | category | Unknown | 2039 | 0.0340624 | 0.175004 | 0.615565 | 0.533168 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.103688 | 0.196901 | 0.566959 | 0.585953 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0351599 | 0.189643 | 0.626232 | 0.565074 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0180757 | 0.174676 | 0.657334 | 0.529131 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0208785 | 0.160278 | 0.64211 | 0.497198 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0348059 | 0.172761 | 0.639537 | 0.529536 |
