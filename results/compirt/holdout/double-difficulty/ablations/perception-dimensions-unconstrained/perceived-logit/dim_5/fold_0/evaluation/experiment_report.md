# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.551374 |
| log_loss | 0.58911 |
| ece | 0.088897 |
| brier | 0.18811 |
| accuracy | 0.764282 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000968263 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.105564 |
| probability_p10 | 0.684468 |
| probability_p50 | 0.872429 |
| probability_p90 | 0.94094 |
| mean_predictive_variance | 0.123416 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.171899 |
| joint_tossup_event_log_loss | 7.7189 |
| buzz_position_mae | 0.333371 |
| buzz_position_median_absolute_error | 0.333432 |
| buzz_position_bias | -0.319719 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.35277 |
| first_buzzer_mean_reciprocal_rank | 0.565925 |
| first_buzzer_log_loss | 1.66771 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.625605 |
| tossup_scorer_player_top1_accuracy | 0.265287 |
| tossup_scorer_team_top1_accuracy | 0.396815 |
| tossup_game_winner_accuracy | 0.69163 |
| tossup_game_margin_mae | 43.5098 |
| tournament_player_ppg_spearman | 0.576682 |
| tournament_player_ppg_mae | 10.3509 |
| tournament_player_ppg_top10_overlap | 0.603448 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.551374 |
| neg_average_precision | 0.283229 |
| neg_precision | 0.449438 |
| neg_recall | 0.0183318 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0310022 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.230991 |
| no_buzz_calibration_error | 0.217721 |
| no_buzz_brier | 0.0690733 |
| full_pmf_max_mass_error | 1.22125e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.319719 | -0.333432 |
| Q1 (0-.2) | 197 | 0.173256 | 0.161365 |
| Q2 (.2-.4) | 985 | 0.00646079 | -0.00134792 |
| Q3 (.4-.6) | 2251 | -0.168342 | -0.168276 |
| Q4 (.6-.8) | 2866 | -0.348556 | -0.347796 |
| Q5 (.8-1) | 2996 | -0.545521 | -0.549052 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.088897 | 0.18811 | 0.551374 | 0.58911 |
| tossup_correctness | tier | fall | 2933 | 0.0709779 | 0.169428 | 0.561712 | 0.535334 |
| tossup_correctness | tier | nationals | 1584 | 0.0816682 | 0.20564 | 0.569961 | 0.620173 |
| tossup_correctness | tier | regionals | 1886 | 0.105851 | 0.20326 | 0.522964 | 0.630647 |
| tossup_correctness | tier | winter | 2892 | 0.109353 | 0.187575 | 0.536473 | 0.599546 |
| tossup_correctness | category | Current Events | 124 | 0.0971771 | 0.195696 | 0.522373 | 0.593683 |
| tossup_correctness | category | Fine Arts | 1103 | 0.122432 | 0.198787 | 0.522407 | 0.629187 |
| tossup_correctness | category | Geography | 197 | 0.178391 | 0.241778 | 0.654429 | 0.713739 |
| tossup_correctness | category | History | 1491 | 0.0793779 | 0.174015 | 0.558639 | 0.546071 |
| tossup_correctness | category | Literature | 1472 | 0.0783901 | 0.16299 | 0.552547 | 0.528352 |
| tossup_correctness | category | Mythology | 332 | 0.0835639 | 0.154952 | 0.601732 | 0.494822 |
| tossup_correctness | category | Other Academic | 69 | 0.0846116 | 0.192102 | 0.514706 | 0.604344 |
| tossup_correctness | category | Philosophy | 324 | 0.0793664 | 0.160162 | 0.584675 | 0.51559 |
| tossup_correctness | category | Popular Culture | 102 | 0.121018 | 0.155433 | 0.357785 | 0.516933 |
| tossup_correctness | category | Religion | 372 | 0.138452 | 0.217004 | 0.619774 | 0.657903 |
| tossup_correctness | category | Science | 1487 | 0.0761893 | 0.189796 | 0.568753 | 0.587789 |
| tossup_correctness | category | Social Science | 336 | 0.162638 | 0.235716 | 0.534407 | 0.719318 |
| tossup_correctness | category | Unknown | 1886 | 0.105851 | 0.20326 | 0.522964 | 0.630647 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.109702 | 0.205376 | 0.53939 | 0.610329 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0950645 | 0.205406 | 0.525116 | 0.627577 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0757792 | 0.181965 | 0.571374 | 0.563728 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0789075 | 0.175149 | 0.555875 | 0.553194 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.111929 | 0.198304 | 0.545097 | 0.628495 |
