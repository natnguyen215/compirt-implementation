# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.562686 |
| log_loss | 0.565191 |
| ece | 0.0757514 |
| brier | 0.184264 |
| accuracy | 0.762234 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00194447 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.12039 |
| probability_p10 | 0.608208 |
| probability_p50 | 0.822877 |
| probability_p90 | 0.917726 |
| mean_predictive_variance | 0.15168 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172918 |
| joint_tossup_event_log_loss | 7.67856 |
| buzz_position_mae | 0.322421 |
| buzz_position_median_absolute_error | 0.319016 |
| buzz_position_bias | -0.30588 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.316193 |
| first_buzzer_mean_reciprocal_rank | 0.530385 |
| first_buzzer_log_loss | 1.74292 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.623744 |
| tossup_scorer_player_top1_accuracy | 0.259808 |
| tossup_scorer_team_top1_accuracy | 0.382196 |
| tossup_game_winner_accuracy | 0.686957 |
| tossup_game_margin_mae | 48.28 |
| tournament_player_ppg_spearman | 0.525162 |
| tournament_player_ppg_mae | 10.9595 |
| tournament_player_ppg_top10_overlap | 0.524138 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.562686 |
| neg_average_precision | 0.297845 |
| neg_precision | 0.454082 |
| neg_recall | 0.0407696 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0363412 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.205804 |
| no_buzz_calibration_error | 0.192691 |
| no_buzz_brier | 0.0573284 |
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
| overall | 9257 | -0.30588 | -0.318393 |
| Q1 (0-.2) | 183 | 0.200177 | 0.196182 |
| Q2 (.2-.4) | 955 | 0.0224132 | 0.0191679 |
| Q3 (.4-.6) | 2239 | -0.158723 | -0.163903 |
| Q4 (.6-.8) | 2875 | -0.330839 | -0.331116 |
| Q5 (.8-1) | 3005 | -0.526797 | -0.527029 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0757514 | 0.184264 | 0.562686 | 0.565191 |
| tossup_correctness | tier | fall | 2798 | 0.0578935 | 0.171563 | 0.561068 | 0.536264 |
| tossup_correctness | tier | nationals | 1545 | 0.0736471 | 0.203049 | 0.590448 | 0.597503 |
| tossup_correctness | tier | regionals | 2039 | 0.0973942 | 0.187654 | 0.540463 | 0.574086 |
| tossup_correctness | tier | winter | 2875 | 0.0801774 | 0.184126 | 0.551114 | 0.569672 |
| tossup_correctness | category | Current Events | 129 | 0.138927 | 0.237847 | 0.536777 | 0.687879 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0779141 | 0.179047 | 0.567406 | 0.552543 |
| tossup_correctness | category | Geography | 180 | 0.187338 | 0.266551 | 0.598642 | 0.753346 |
| tossup_correctness | category | History | 1454 | 0.0881864 | 0.18913 | 0.555449 | 0.576512 |
| tossup_correctness | category | Literature | 1435 | 0.0739341 | 0.157869 | 0.544633 | 0.508672 |
| tossup_correctness | category | Mythology | 324 | 0.0839789 | 0.168869 | 0.5516 | 0.530195 |
| tossup_correctness | category | Other Academic | 71 | 0.242453 | 0.2382 | 0.27451 | 0.713465 |
| tossup_correctness | category | Philosophy | 310 | 0.0889981 | 0.18953 | 0.552565 | 0.581598 |
| tossup_correctness | category | Popular Culture | 108 | 0.0963758 | 0.103018 | 0.65191 | 0.359026 |
| tossup_correctness | category | Religion | 361 | 0.0830841 | 0.194471 | 0.577155 | 0.589321 |
| tossup_correctness | category | Science | 1445 | 0.0561067 | 0.188351 | 0.603052 | 0.568577 |
| tossup_correctness | category | Social Science | 327 | 0.0795988 | 0.204072 | 0.588668 | 0.610411 |
| tossup_correctness | category | Unknown | 2039 | 0.0973942 | 0.187654 | 0.540463 | 0.574086 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0909806 | 0.204643 | 0.481383 | 0.609998 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0722531 | 0.203943 | 0.545544 | 0.604952 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0688829 | 0.189741 | 0.553746 | 0.575518 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0812346 | 0.171436 | 0.563951 | 0.533755 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0764838 | 0.184961 | 0.569493 | 0.572209 |
