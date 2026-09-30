# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.571495 |
| log_loss | 0.608163 |
| ece | 0.118313 |
| brier | 0.18968 |
| accuracy | 0.768282 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00176211 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0827163 |
| probability_p10 | 0.785957 |
| probability_p50 | 0.903852 |
| probability_p90 | 0.959173 |
| mean_predictive_variance | 0.0968376 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173837 |
| joint_tossup_event_log_loss | 7.81712 |
| buzz_position_mae | 0.340234 |
| buzz_position_median_absolute_error | 0.34349 |
| buzz_position_bias | -0.327481 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.309141 |
| first_buzzer_mean_reciprocal_rank | 0.530768 |
| first_buzzer_log_loss | 1.75074 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.629185 |
| tossup_scorer_player_top1_accuracy | 0.253145 |
| tossup_scorer_team_top1_accuracy | 0.438395 |
| tossup_game_winner_accuracy | 0.74115 |
| tossup_game_margin_mae | 43.9429 |
| tournament_player_ppg_spearman | 0.647056 |
| tournament_player_ppg_mae | 10.1204 |
| tournament_player_ppg_top10_overlap | 0.613793 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.571495 |
| neg_average_precision | 0.277999 |
| neg_precision | 0.3 |
| neg_recall | 0.00574713 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0288705 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.224385 |
| no_buzz_calibration_error | 0.209201 |
| no_buzz_brier | 0.0664356 |
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
| overall | 9080 | -0.327481 | -0.34349 |
| Q1 (0-.2) | 192 | 0.172988 | 0.172885 |
| Q2 (.2-.4) | 889 | 0.00322687 | -0.000366528 |
| Q3 (.4-.6) | 2210 | -0.175646 | -0.177126 |
| Q4 (.6-.8) | 2869 | -0.355702 | -0.354281 |
| Q5 (.8-1) | 2920 | -0.548263 | -0.552993 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.118313 | 0.18968 | 0.571495 | 0.608163 |
| tossup_correctness | tier | fall | 2817 | 0.09869 | 0.179504 | 0.574489 | 0.57067 |
| tossup_correctness | tier | nationals | 1542 | 0.151006 | 0.212328 | 0.619152 | 0.660817 |
| tossup_correctness | tier | regionals | 1934 | 0.129257 | 0.200629 | 0.557102 | 0.647393 |
| tossup_correctness | tier | winter | 2787 | 0.112463 | 0.179836 | 0.547349 | 0.589703 |
| tossup_correctness | category | Current Events | 125 | 0.160454 | 0.225912 | 0.625614 | 0.679129 |
| tossup_correctness | category | Fine Arts | 1072 | 0.127457 | 0.191179 | 0.575405 | 0.613564 |
| tossup_correctness | category | Geography | 185 | 0.169473 | 0.225709 | 0.627972 | 0.692877 |
| tossup_correctness | category | History | 1443 | 0.114797 | 0.191079 | 0.582497 | 0.601678 |
| tossup_correctness | category | Literature | 1411 | 0.0953594 | 0.161262 | 0.563779 | 0.538393 |
| tossup_correctness | category | Mythology | 320 | 0.0945843 | 0.17229 | 0.53257 | 0.566352 |
| tossup_correctness | category | Other Academic | 64 | 0.177195 | 0.208583 | 0.567708 | 0.64785 |
| tossup_correctness | category | Philosophy | 312 | 0.104933 | 0.169628 | 0.493742 | 0.570172 |
| tossup_correctness | category | Popular Culture | 104 | 0.07747 | 0.132175 | 0.606534 | 0.438298 |
| tossup_correctness | category | Religion | 358 | 0.170785 | 0.225739 | 0.557732 | 0.715002 |
| tossup_correctness | category | Science | 1431 | 0.114709 | 0.189807 | 0.587427 | 0.596889 |
| tossup_correctness | category | Social Science | 321 | 0.150113 | 0.213366 | 0.530207 | 0.669972 |
| tossup_correctness | category | Unknown | 1934 | 0.129257 | 0.200629 | 0.557102 | 0.647393 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.181635 | 0.240546 | 0.518013 | 0.736882 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.133272 | 0.209846 | 0.576907 | 0.648006 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.121777 | 0.199181 | 0.534552 | 0.634273 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.104535 | 0.175603 | 0.577152 | 0.567631 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.122434 | 0.186837 | 0.588682 | 0.607631 |
