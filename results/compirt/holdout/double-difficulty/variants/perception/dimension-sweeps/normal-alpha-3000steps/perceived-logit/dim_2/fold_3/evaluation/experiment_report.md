# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.54923 |
| log_loss | 0.611278 |
| ece | 0.11219 |
| brier | 0.190244 |
| accuracy | 0.768612 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00143172 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0892334 |
| probability_p10 | 0.758203 |
| probability_p50 | 0.898993 |
| probability_p90 | 0.95549 |
| mean_predictive_variance | 0.102056 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174767 |
| joint_tossup_event_log_loss | 7.78696 |
| buzz_position_mae | 0.342725 |
| buzz_position_median_absolute_error | 0.346285 |
| buzz_position_bias | -0.330231 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.339868 |
| first_buzzer_mean_reciprocal_rank | 0.555336 |
| first_buzzer_log_loss | 1.69024 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637445 |
| tossup_scorer_player_top1_accuracy | 0.261171 |
| tossup_scorer_team_top1_accuracy | 0.429176 |
| tossup_game_winner_accuracy | 0.734513 |
| tossup_game_margin_mae | 45.1292 |
| tournament_player_ppg_spearman | 0.625199 |
| tournament_player_ppg_mae | 10.2573 |
| tournament_player_ppg_top10_overlap | 0.6 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.54923 |
| neg_average_precision | 0.26542 |
| neg_precision | 0.372549 |
| neg_recall | 0.00909962 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0282279 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.231074 |
| no_buzz_calibration_error | 0.215889 |
| no_buzz_brier | 0.0701174 |
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
| overall | 9080 | -0.330231 | -0.346285 |
| Q1 (0-.2) | 192 | 0.170901 | 0.167307 |
| Q2 (.2-.4) | 889 | 0.0010975 | -0.00310035 |
| Q3 (.4-.6) | 2210 | -0.177813 | -0.17886 |
| Q4 (.6-.8) | 2869 | -0.358425 | -0.357533 |
| Q5 (.8-1) | 2920 | -0.551713 | -0.557382 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.11219 | 0.190244 | 0.54923 | 0.611278 |
| tossup_correctness | tier | fall | 2817 | 0.0983673 | 0.181141 | 0.551123 | 0.574273 |
| tossup_correctness | tier | nationals | 1542 | 0.138915 | 0.211099 | 0.593679 | 0.659952 |
| tossup_correctness | tier | regionals | 1934 | 0.12388 | 0.200066 | 0.537398 | 0.648873 |
| tossup_correctness | tier | winter | 2787 | 0.109694 | 0.181089 | 0.52132 | 0.595662 |
| tossup_correctness | category | Current Events | 125 | 0.161798 | 0.223514 | 0.639435 | 0.664046 |
| tossup_correctness | category | Fine Arts | 1072 | 0.123597 | 0.191002 | 0.566977 | 0.611168 |
| tossup_correctness | category | Geography | 185 | 0.174858 | 0.225298 | 0.630769 | 0.687633 |
| tossup_correctness | category | History | 1443 | 0.113725 | 0.191946 | 0.568958 | 0.605399 |
| tossup_correctness | category | Literature | 1411 | 0.0923014 | 0.163664 | 0.513991 | 0.546733 |
| tossup_correctness | category | Mythology | 320 | 0.0883021 | 0.171371 | 0.537461 | 0.564175 |
| tossup_correctness | category | Other Academic | 64 | 0.15626 | 0.208578 | 0.546875 | 0.658862 |
| tossup_correctness | category | Philosophy | 312 | 0.112999 | 0.169367 | 0.490516 | 0.566592 |
| tossup_correctness | category | Popular Culture | 104 | 0.0775037 | 0.136956 | 0.541193 | 0.463703 |
| tossup_correctness | category | Religion | 358 | 0.162339 | 0.225687 | 0.551138 | 0.71287 |
| tossup_correctness | category | Science | 1431 | 0.104386 | 0.190527 | 0.561503 | 0.602454 |
| tossup_correctness | category | Social Science | 321 | 0.157991 | 0.216485 | 0.500153 | 0.685472 |
| tossup_correctness | category | Unknown | 1934 | 0.12388 | 0.200066 | 0.537398 | 0.648873 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.156524 | 0.238533 | 0.499743 | 0.727421 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.120977 | 0.21012 | 0.553095 | 0.648067 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.116235 | 0.200247 | 0.5037 | 0.636643 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0970577 | 0.175577 | 0.558863 | 0.567688 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.121838 | 0.187857 | 0.564844 | 0.616072 |
