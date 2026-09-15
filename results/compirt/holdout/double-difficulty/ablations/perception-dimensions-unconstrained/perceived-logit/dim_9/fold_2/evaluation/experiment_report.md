# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.563617 |
| log_loss | 0.560959 |
| ece | 0.0737919 |
| brier | 0.183515 |
| accuracy | 0.762666 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00151237 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.118838 |
| probability_p10 | 0.601663 |
| probability_p50 | 0.807218 |
| probability_p90 | 0.909219 |
| mean_predictive_variance | 0.158168 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172735 |
| joint_tossup_event_log_loss | 7.66924 |
| buzz_position_mae | 0.318856 |
| buzz_position_median_absolute_error | 0.314222 |
| buzz_position_bias | -0.30143 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.30269 |
| first_buzzer_mean_reciprocal_rank | 0.519073 |
| first_buzzer_log_loss | 1.76284 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.618775 |
| tossup_scorer_player_top1_accuracy | 0.257249 |
| tossup_scorer_team_top1_accuracy | 0.377292 |
| tossup_game_winner_accuracy | 0.673913 |
| tossup_game_margin_mae | 48.3607 |
| tournament_player_ppg_spearman | 0.527605 |
| tournament_player_ppg_mae | 11.039 |
| tournament_player_ppg_top10_overlap | 0.510345 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.563617 |
| neg_average_precision | 0.299616 |
| neg_precision | 0.461957 |
| neg_recall | 0.0389372 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.037675 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.199854 |
| no_buzz_calibration_error | 0.186741 |
| no_buzz_brier | 0.0547667 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9257 | -0.30143 | -0.313701 |
| Q1 (0-.2) | 183 | 0.205014 | 0.199005 |
| Q2 (.2-.4) | 955 | 0.0267017 | 0.0229323 |
| Q3 (.4-.6) | 2239 | -0.154771 | -0.158053 |
| Q4 (.6-.8) | 2875 | -0.326564 | -0.326229 |
| Q5 (.8-1) | 3005 | -0.521781 | -0.521645 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0737919 | 0.183515 | 0.563617 | 0.560959 |
| tossup_correctness | tier | fall | 2798 | 0.0571577 | 0.171033 | 0.559642 | 0.533146 |
| tossup_correctness | tier | nationals | 1545 | 0.0755369 | 0.202506 | 0.595627 | 0.594947 |
| tossup_correctness | tier | regionals | 2039 | 0.0942543 | 0.186957 | 0.54248 | 0.569514 |
| tossup_correctness | tier | winter | 2875 | 0.0747116 | 0.183015 | 0.550826 | 0.563694 |
| tossup_correctness | category | Current Events | 129 | 0.169283 | 0.233287 | 0.552461 | 0.672345 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0696213 | 0.178798 | 0.562105 | 0.549991 |
| tossup_correctness | category | Geography | 180 | 0.166022 | 0.262324 | 0.58428 | 0.740411 |
| tossup_correctness | category | History | 1454 | 0.0778967 | 0.187782 | 0.557282 | 0.57088 |
| tossup_correctness | category | Literature | 1435 | 0.0793693 | 0.158154 | 0.543441 | 0.507384 |
| tossup_correctness | category | Mythology | 324 | 0.0707573 | 0.166977 | 0.562518 | 0.521745 |
| tossup_correctness | category | Other Academic | 71 | 0.25581 | 0.234625 | 0.285403 | 0.697315 |
| tossup_correctness | category | Philosophy | 310 | 0.0790258 | 0.187549 | 0.562128 | 0.571749 |
| tossup_correctness | category | Popular Culture | 108 | 0.103004 | 0.106415 | 0.633681 | 0.369773 |
| tossup_correctness | category | Religion | 361 | 0.0712965 | 0.192105 | 0.580525 | 0.579764 |
| tossup_correctness | category | Science | 1445 | 0.0505583 | 0.18837 | 0.601631 | 0.567327 |
| tossup_correctness | category | Social Science | 327 | 0.0828757 | 0.202828 | 0.58247 | 0.605164 |
| tossup_correctness | category | Unknown | 2039 | 0.0942543 | 0.186957 | 0.54248 | 0.569514 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.102334 | 0.202482 | 0.497966 | 0.601212 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0745066 | 0.203669 | 0.543409 | 0.602612 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0699011 | 0.18913 | 0.554116 | 0.572004 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0804733 | 0.171228 | 0.564349 | 0.531336 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0760279 | 0.183525 | 0.571928 | 0.565382 |
