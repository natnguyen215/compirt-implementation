# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.647454 |
| log_loss | 0.530671 |
| ece | 0.0384622 |
| brier | 0.173589 |
| accuracy | 0.760585 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00153965 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.143003 |
| probability_p10 | 0.545896 |
| probability_p50 | 0.776664 |
| probability_p90 | 0.912838 |
| mean_predictive_variance | 0.167287 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101795 |
| joint_tossup_event_log_loss | 6.91662 |
| buzz_position_mae | 0.161818 |
| buzz_position_median_absolute_error | 0.14754 |
| buzz_position_bias | -0.0687676 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.338722 |
| first_buzzer_mean_reciprocal_rank | 0.552018 |
| first_buzzer_log_loss | 1.70686 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.634114 |
| tossup_scorer_player_top1_accuracy | 0.318506 |
| tossup_scorer_team_top1_accuracy | 0.483766 |
| tossup_game_winner_accuracy | 0.745495 |
| tossup_game_margin_mae | 35.3394 |
| tournament_player_ppg_spearman | 0.673321 |
| tournament_player_ppg_mae | 9.00354 |
| tournament_player_ppg_top10_overlap | 0.655172 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.647454 |
| neg_average_precision | 0.37259 |
| neg_precision | 0.488255 |
| neg_recall | 0.134535 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0572329 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0903992 |
| no_buzz_calibration_error | 0.0744901 |
| no_buzz_brier | 0.0264023 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0687676 | -0.0868491 |
| Q1 (0-.2) | 167 | 0.367298 | 0.378553 |
| Q2 (.2-.4) | 912 | 0.208951 | 0.211623 |
| Q3 (.4-.6) | 2115 | 0.0540572 | 0.0566807 |
| Q4 (.6-.8) | 2844 | -0.0870578 | -0.0843432 |
| Q5 (.8-1) | 3055 | -0.243517 | -0.241484 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0384622 | 0.173589 | 0.647454 | 0.530671 |
| tossup_correctness | tier | fall | 2842 | 0.0155722 | 0.15717 | 0.674084 | 0.488583 |
| tossup_correctness | tier | nationals | 1564 | 0.0644484 | 0.197689 | 0.634811 | 0.583864 |
| tossup_correctness | tier | regionals | 1937 | 0.054896 | 0.178894 | 0.623968 | 0.544487 |
| tossup_correctness | tier | winter | 2750 | 0.0399609 | 0.173114 | 0.636108 | 0.534183 |
| tossup_correctness | category | Current Events | 126 | 0.0901605 | 0.174662 | 0.675791 | 0.530048 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0333018 | 0.171152 | 0.647893 | 0.523206 |
| tossup_correctness | category | Geography | 185 | 0.0652251 | 0.194579 | 0.693798 | 0.571608 |
| tossup_correctness | category | History | 1440 | 0.0332028 | 0.175876 | 0.659594 | 0.531829 |
| tossup_correctness | category | Literature | 1422 | 0.057524 | 0.154201 | 0.586487 | 0.495042 |
| tossup_correctness | category | Mythology | 318 | 0.0650445 | 0.160209 | 0.669144 | 0.498099 |
| tossup_correctness | category | Other Academic | 66 | 0.0602851 | 0.18051 | 0.714446 | 0.5388 |
| tossup_correctness | category | Philosophy | 311 | 0.0675049 | 0.177087 | 0.676179 | 0.535885 |
| tossup_correctness | category | Popular Culture | 102 | 0.181156 | 0.132546 | 0.644444 | 0.435616 |
| tossup_correctness | category | Religion | 358 | 0.0440536 | 0.192869 | 0.65277 | 0.574587 |
| tossup_correctness | category | Science | 1433 | 0.0321565 | 0.181161 | 0.668827 | 0.54587 |
| tossup_correctness | category | Social Science | 324 | 0.0371572 | 0.178937 | 0.668364 | 0.540322 |
| tossup_correctness | category | Unknown | 1937 | 0.054896 | 0.178894 | 0.623968 | 0.544487 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0660272 | 0.205951 | 0.606443 | 0.605177 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0481843 | 0.185505 | 0.66541 | 0.5568 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0285849 | 0.1741 | 0.660478 | 0.529132 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0400009 | 0.165935 | 0.641717 | 0.51092 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0415759 | 0.175033 | 0.639413 | 0.53825 |
