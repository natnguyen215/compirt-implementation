# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.611127 |
| log_loss | 0.571608 |
| ece | 0.0958603 |
| brier | 0.188624 |
| accuracy | 0.734081 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0280435 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.165628 |
| probability_p10 | 0.470596 |
| probability_p50 | 0.711647 |
| probability_p90 | 0.908938 |
| mean_predictive_variance | 0.1831 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.114893 |
| joint_tossup_event_log_loss | 6.85066 |
| buzz_position_mae | 0.188496 |
| buzz_position_median_absolute_error | 0.164881 |
| buzz_position_bias | -0.124673 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.387221 |
| first_buzzer_mean_reciprocal_rank | 0.590396 |
| first_buzzer_log_loss | 1.61434 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.648411 |
| tossup_scorer_player_top1_accuracy | 0.306169 |
| tossup_scorer_team_top1_accuracy | 0.458442 |
| tossup_game_winner_accuracy | 0.774775 |
| tossup_game_margin_mae | 38.8038 |
| tournament_player_ppg_spearman | 0.586736 |
| tournament_player_ppg_mae | 10.5945 |
| tournament_player_ppg_top10_overlap | 0.627586 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.611127 |
| neg_average_precision | 0.332861 |
| neg_precision | 0.394366 |
| neg_recall | 0.220065 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.10131 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0906411 |
| no_buzz_calibration_error | 0.074732 |
| no_buzz_brier | 0.0287985 |
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
| overall | 9093 | -0.124673 | -0.130613 |
| Q1 (0-.2) | 167 | 0.295056 | 0.302398 |
| Q2 (.2-.4) | 912 | 0.145641 | 0.135737 |
| Q3 (.4-.6) | 2115 | -0.0089021 | -0.0181656 |
| Q4 (.6-.8) | 2844 | -0.143287 | -0.149593 |
| Q5 (.8-1) | 3055 | -0.291133 | -0.28622 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0958603 | 0.188624 | 0.611127 | 0.571608 |
| tossup_correctness | tier | fall | 2842 | 0.0845823 | 0.172129 | 0.612487 | 0.536619 |
| tossup_correctness | tier | nationals | 1564 | 0.0864089 | 0.210161 | 0.62142 | 0.609009 |
| tossup_correctness | tier | regionals | 1937 | 0.0975441 | 0.193598 | 0.608144 | 0.575314 |
| tossup_correctness | tier | winter | 2750 | 0.111906 | 0.189917 | 0.58854 | 0.583887 |
| tossup_correctness | category | Current Events | 126 | 0.0997382 | 0.186119 | 0.653039 | 0.548641 |
| tossup_correctness | category | Fine Arts | 1071 | 0.117801 | 0.186059 | 0.624346 | 0.572764 |
| tossup_correctness | category | Geography | 185 | 0.0827466 | 0.207833 | 0.648948 | 0.599603 |
| tossup_correctness | category | History | 1440 | 0.0906192 | 0.188067 | 0.611324 | 0.570294 |
| tossup_correctness | category | Literature | 1422 | 0.127632 | 0.173964 | 0.565359 | 0.551739 |
| tossup_correctness | category | Mythology | 318 | 0.140997 | 0.180712 | 0.608908 | 0.546571 |
| tossup_correctness | category | Other Academic | 66 | 0.117754 | 0.2171 | 0.600224 | 0.632674 |
| tossup_correctness | category | Philosophy | 311 | 0.0812415 | 0.182378 | 0.678907 | 0.551981 |
| tossup_correctness | category | Popular Culture | 102 | 0.17281 | 0.153054 | 0.526852 | 0.475215 |
| tossup_correctness | category | Religion | 358 | 0.0717508 | 0.204935 | 0.616029 | 0.616648 |
| tossup_correctness | category | Science | 1433 | 0.0778158 | 0.194917 | 0.605679 | 0.584395 |
| tossup_correctness | category | Social Science | 324 | 0.0923379 | 0.197486 | 0.624909 | 0.586623 |
| tossup_correctness | category | Unknown | 1937 | 0.0975441 | 0.193598 | 0.608144 | 0.575314 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.190332 | 0.220616 | 0.644783 | 0.635051 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.155674 | 0.226288 | 0.57952 | 0.648443 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.136393 | 0.203107 | 0.599354 | 0.601512 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.108539 | 0.179469 | 0.611756 | 0.548273 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0398383 | 0.174126 | 0.641892 | 0.546224 |
