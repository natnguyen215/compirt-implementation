# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.543366 |
| log_loss | 0.604961 |
| ece | 0.0994544 |
| brier | 0.191262 |
| accuracy | 0.762882 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00129632 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.100338 |
| probability_p10 | 0.700611 |
| probability_p50 | 0.882068 |
| probability_p90 | 0.948353 |
| mean_predictive_variance | 0.115898 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174643 |
| joint_tossup_event_log_loss | 7.73804 |
| buzz_position_mae | 0.339815 |
| buzz_position_median_absolute_error | 0.342066 |
| buzz_position_bias | -0.326749 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.362753 |
| first_buzzer_mean_reciprocal_rank | 0.577204 |
| first_buzzer_log_loss | 1.63278 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637139 |
| tossup_scorer_player_top1_accuracy | 0.271322 |
| tossup_scorer_team_top1_accuracy | 0.401173 |
| tossup_game_winner_accuracy | 0.695652 |
| tossup_game_margin_mae | 47.0165 |
| tournament_player_ppg_spearman | 0.6169 |
| tournament_player_ppg_mae | 10.1763 |
| tournament_player_ppg_top10_overlap | 0.603448 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.543366 |
| neg_average_precision | 0.278039 |
| neg_precision | 0.384615 |
| neg_recall | 0.0091617 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0294183 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.236512 |
| no_buzz_calibration_error | 0.223399 |
| no_buzz_brier | 0.0717813 |
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
| overall | 9257 | -0.326749 | -0.342066 |
| Q1 (0-.2) | 183 | 0.181449 | 0.178514 |
| Q2 (.2-.4) | 955 | 0.00431593 | 0.000166893 |
| Q3 (.4-.6) | 2239 | -0.17585 | -0.179143 |
| Q4 (.6-.8) | 2875 | -0.352585 | -0.354711 |
| Q5 (.8-1) | 3005 | -0.550626 | -0.553842 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0994544 | 0.191262 | 0.543366 | 0.604961 |
| tossup_correctness | tier | fall | 2798 | 0.0860292 | 0.177027 | 0.529812 | 0.563482 |
| tossup_correctness | tier | nationals | 1545 | 0.10806 | 0.211568 | 0.57606 | 0.64509 |
| tossup_correctness | tier | regionals | 2039 | 0.0975102 | 0.192009 | 0.539963 | 0.609167 |
| tossup_correctness | tier | winter | 2875 | 0.119147 | 0.193673 | 0.529047 | 0.620779 |
| tossup_correctness | category | Current Events | 129 | 0.202679 | 0.252188 | 0.566793 | 0.750301 |
| tossup_correctness | category | Fine Arts | 1074 | 0.10418 | 0.185409 | 0.541492 | 0.591134 |
| tossup_correctness | category | Geography | 180 | 0.25405 | 0.299311 | 0.552161 | 0.891391 |
| tossup_correctness | category | History | 1454 | 0.095728 | 0.192413 | 0.553789 | 0.602393 |
| tossup_correctness | category | Literature | 1435 | 0.08138 | 0.161312 | 0.518038 | 0.531523 |
| tossup_correctness | category | Mythology | 324 | 0.126589 | 0.172055 | 0.564435 | 0.552239 |
| tossup_correctness | category | Other Academic | 71 | 0.20505 | 0.22911 | 0.361656 | 0.751721 |
| tossup_correctness | category | Philosophy | 310 | 0.132022 | 0.203163 | 0.502348 | 0.656124 |
| tossup_correctness | category | Popular Culture | 108 | 0.0771058 | 0.101969 | 0.529514 | 0.357325 |
| tossup_correctness | category | Religion | 361 | 0.132987 | 0.20863 | 0.536712 | 0.656076 |
| tossup_correctness | category | Science | 1445 | 0.103738 | 0.199041 | 0.557486 | 0.615314 |
| tossup_correctness | category | Social Science | 327 | 0.150101 | 0.2241 | 0.555828 | 0.6943 |
| tossup_correctness | category | Unknown | 2039 | 0.0975102 | 0.192009 | 0.539963 | 0.609167 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.138063 | 0.210539 | 0.451502 | 0.657424 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.118061 | 0.215354 | 0.514895 | 0.653605 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.100797 | 0.196455 | 0.539957 | 0.611988 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0876901 | 0.175623 | 0.542115 | 0.563476 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.113334 | 0.193524 | 0.553274 | 0.62076 |
