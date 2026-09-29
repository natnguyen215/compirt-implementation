# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.662266 |
| log_loss | 0.513303 |
| ece | 0.0367643 |
| brier | 0.166435 |
| accuracy | 0.775771 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00572687 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.140157 |
| probability_p10 | 0.550049 |
| probability_p50 | 0.77293 |
| probability_p90 | 0.907223 |
| mean_predictive_variance | 0.168488 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101875 |
| joint_tossup_event_log_loss | 6.8543 |
| buzz_position_mae | 0.161087 |
| buzz_position_median_absolute_error | 0.14592 |
| buzz_position_bias | -0.0702069 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.355396 |
| first_buzzer_mean_reciprocal_rank | 0.564975 |
| first_buzzer_log_loss | 1.68178 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.655617 |
| tossup_scorer_player_top1_accuracy | 0.319957 |
| tossup_scorer_team_top1_accuracy | 0.504881 |
| tossup_game_winner_accuracy | 0.780973 |
| tossup_game_margin_mae | 36.4745 |
| tournament_player_ppg_spearman | 0.692163 |
| tournament_player_ppg_mae | 9.12891 |
| tournament_player_ppg_top10_overlap | 0.648276 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.662266 |
| neg_average_precision | 0.391128 |
| neg_precision | 0.546099 |
| neg_recall | 0.14751 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0546649 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.085762 |
| no_buzz_calibration_error | 0.0705776 |
| no_buzz_brier | 0.0243551 |
| full_pmf_max_mass_error | 1.55431e-15 |
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
| overall | 9080 | -0.0702069 | -0.0876849 |
| Q1 (0-.2) | 192 | 0.370867 | 0.370827 |
| Q2 (.2-.4) | 889 | 0.199313 | 0.201007 |
| Q3 (.4-.6) | 2210 | 0.044959 | 0.0477389 |
| Q4 (.6-.8) | 2869 | -0.0950411 | -0.0923139 |
| Q5 (.8-1) | 2920 | -0.244028 | -0.24522 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0367643 | 0.166435 | 0.662266 | 0.513303 |
| tossup_correctness | tier | fall | 2817 | 0.0348133 | 0.160214 | 0.658431 | 0.497977 |
| tossup_correctness | tier | nationals | 1542 | 0.0636362 | 0.183678 | 0.678228 | 0.54867 |
| tossup_correctness | tier | regionals | 1934 | 0.0234937 | 0.173428 | 0.658275 | 0.528364 |
| tossup_correctness | tier | winter | 2787 | 0.0466456 | 0.15833 | 0.649627 | 0.498775 |
| tossup_correctness | category | Current Events | 125 | 0.0641256 | 0.187874 | 0.708231 | 0.556381 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0368887 | 0.166178 | 0.664482 | 0.508533 |
| tossup_correctness | category | Geography | 185 | 0.0870157 | 0.17289 | 0.770769 | 0.522505 |
| tossup_correctness | category | History | 1443 | 0.0590844 | 0.163035 | 0.715705 | 0.500966 |
| tossup_correctness | category | Literature | 1411 | 0.0589442 | 0.155354 | 0.57589 | 0.502134 |
| tossup_correctness | category | Mythology | 320 | 0.106552 | 0.168172 | 0.588881 | 0.521231 |
| tossup_correctness | category | Other Academic | 64 | 0.0966012 | 0.188049 | 0.604167 | 0.561807 |
| tossup_correctness | category | Philosophy | 312 | 0.0710957 | 0.159864 | 0.591871 | 0.501066 |
| tossup_correctness | category | Popular Culture | 104 | 0.160666 | 0.152862 | 0.488636 | 0.489789 |
| tossup_correctness | category | Religion | 358 | 0.0426374 | 0.18289 | 0.691601 | 0.544838 |
| tossup_correctness | category | Science | 1431 | 0.0234277 | 0.162911 | 0.681194 | 0.50176 |
| tossup_correctness | category | Social Science | 321 | 0.0590052 | 0.179183 | 0.668793 | 0.539198 |
| tossup_correctness | category | Unknown | 1934 | 0.0234937 | 0.173428 | 0.658275 | 0.528364 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.071276 | 0.190632 | 0.714359 | 0.565112 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0492336 | 0.178361 | 0.69254 | 0.536778 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0435562 | 0.174628 | 0.645299 | 0.534168 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0407953 | 0.158264 | 0.656412 | 0.493518 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0330334 | 0.163041 | 0.661969 | 0.506398 |
