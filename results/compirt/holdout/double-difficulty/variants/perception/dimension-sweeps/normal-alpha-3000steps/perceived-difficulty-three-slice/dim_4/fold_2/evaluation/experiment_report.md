# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.648628 |
| log_loss | 0.522535 |
| ece | 0.0228948 |
| brier | 0.171373 |
| accuracy | 0.764395 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.000216053 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.122716 |
| probability_p10 | 0.587448 |
| probability_p50 | 0.780694 |
| probability_p90 | 0.899213 |
| mean_predictive_variance | 0.16764 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10427 |
| joint_tossup_event_log_loss | 6.93702 |
| buzz_position_mae | 0.163462 |
| buzz_position_median_absolute_error | 0.146862 |
| buzz_position_bias | -0.0689742 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349897 |
| first_buzzer_mean_reciprocal_rank | 0.563893 |
| first_buzzer_log_loss | 1.67662 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.652479 |
| tossup_scorer_player_top1_accuracy | 0.319296 |
| tossup_scorer_team_top1_accuracy | 0.488273 |
| tossup_game_winner_accuracy | 0.773913 |
| tossup_game_margin_mae | 36.8467 |
| tournament_player_ppg_spearman | 0.699103 |
| tournament_player_ppg_mae | 8.77498 |
| tournament_player_ppg_top10_overlap | 0.641379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.648628 |
| neg_average_precision | 0.363004 |
| neg_precision | 0.503106 |
| neg_recall | 0.0742098 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0562417 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0911262 |
| no_buzz_calibration_error | 0.0780132 |
| no_buzz_brier | 0.0246182 |
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
| overall | 9257 | -0.0689742 | -0.0826449 |
| Q1 (0-.2) | 183 | 0.378923 | 0.377388 |
| Q2 (.2-.4) | 955 | 0.206513 | 0.209128 |
| Q3 (.4-.6) | 2239 | 0.0517045 | 0.054057 |
| Q4 (.6-.8) | 2875 | -0.0904548 | -0.0858698 |
| Q5 (.8-1) | 3005 | -0.253167 | -0.251066 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0228948 | 0.171373 | 0.648628 | 0.522535 |
| tossup_correctness | tier | fall | 2798 | 0.0234163 | 0.159339 | 0.655103 | 0.494613 |
| tossup_correctness | tier | nationals | 1545 | 0.0314355 | 0.19178 | 0.64599 | 0.566423 |
| tossup_correctness | tier | regionals | 2039 | 0.0304439 | 0.176656 | 0.617268 | 0.535315 |
| tossup_correctness | tier | winter | 2875 | 0.0251901 | 0.16837 | 0.651608 | 0.517062 |
| tossup_correctness | category | Current Events | 129 | 0.0622376 | 0.215434 | 0.626825 | 0.620781 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0291093 | 0.166587 | 0.639164 | 0.512069 |
| tossup_correctness | category | Geography | 180 | 0.100902 | 0.214916 | 0.706489 | 0.624587 |
| tossup_correctness | category | History | 1454 | 0.0307457 | 0.173818 | 0.655353 | 0.52628 |
| tossup_correctness | category | Literature | 1435 | 0.0251687 | 0.146707 | 0.642143 | 0.46852 |
| tossup_correctness | category | Mythology | 324 | 0.0583919 | 0.16186 | 0.638132 | 0.499866 |
| tossup_correctness | category | Other Academic | 71 | 0.167247 | 0.208837 | 0.368192 | 0.612282 |
| tossup_correctness | category | Philosophy | 310 | 0.0454271 | 0.174045 | 0.647962 | 0.527357 |
| tossup_correctness | category | Popular Culture | 108 | 0.127673 | 0.121072 | 0.601562 | 0.405212 |
| tossup_correctness | category | Religion | 361 | 0.060282 | 0.1865 | 0.62819 | 0.558314 |
| tossup_correctness | category | Science | 1445 | 0.0338912 | 0.17768 | 0.664661 | 0.535819 |
| tossup_correctness | category | Social Science | 327 | 0.0384431 | 0.180958 | 0.705134 | 0.541638 |
| tossup_correctness | category | Unknown | 2039 | 0.0304439 | 0.176656 | 0.617268 | 0.535315 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0904518 | 0.20078 | 0.591364 | 0.592417 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0357252 | 0.188697 | 0.634042 | 0.563794 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0248386 | 0.175534 | 0.655341 | 0.530837 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0232256 | 0.158944 | 0.658391 | 0.491958 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0284561 | 0.172867 | 0.641804 | 0.528237 |
