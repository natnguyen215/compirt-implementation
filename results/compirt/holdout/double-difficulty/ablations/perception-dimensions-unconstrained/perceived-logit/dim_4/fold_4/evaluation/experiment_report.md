# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.54316 |
| log_loss | 0.586609 |
| ece | 0.0914102 |
| brier | 0.184478 |
| accuracy | 0.774002 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.000647249 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0992816 |
| probability_p10 | 0.710682 |
| probability_p50 | 0.881654 |
| probability_p90 | 0.947451 |
| mean_predictive_variance | 0.115846 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173594 |
| joint_tossup_event_log_loss | 7.74645 |
| buzz_position_mae | 0.338566 |
| buzz_position_median_absolute_error | 0.341214 |
| buzz_position_bias | -0.32602 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.362567 |
| first_buzzer_mean_reciprocal_rank | 0.572675 |
| first_buzzer_log_loss | 1.65518 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.622977 |
| tossup_scorer_player_top1_accuracy | 0.262473 |
| tossup_scorer_team_top1_accuracy | 0.410874 |
| tossup_game_winner_accuracy | 0.715536 |
| tossup_game_margin_mae | 45.1475 |
| tournament_player_ppg_spearman | 0.606689 |
| tournament_player_ppg_mae | 10.6016 |
| tournament_player_ppg_top10_overlap | 0.606897 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.54316 |
| neg_average_precision | 0.270853 |
| neg_precision | 0.548387 |
| neg_recall | 0.0161828 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0292503 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.235993 |
| no_buzz_calibration_error | 0.224266 |
| no_buzz_brier | 0.0723853 |
| full_pmf_max_mass_error | 1.44329e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.32602 | -0.341214 |
| Q1 (0-.2) | 179 | 0.167783 | 0.164045 |
| Q2 (.2-.4) | 957 | 0.0075808 | 0.00509776 |
| Q3 (.4-.6) | 2203 | -0.173408 | -0.176217 |
| Q4 (.6-.8) | 2978 | -0.353104 | -0.353458 |
| Q5 (.8-1) | 2953 | -0.550605 | -0.55228 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0914102 | 0.184478 | 0.54316 | 0.586609 |
| tossup_correctness | tier | fall | 2876 | 0.0844034 | 0.171828 | 0.528287 | 0.552649 |
| tossup_correctness | tier | nationals | 1579 | 0.0931723 | 0.205427 | 0.570129 | 0.630534 |
| tossup_correctness | tier | regionals | 1990 | 0.106647 | 0.191548 | 0.525037 | 0.607291 |
| tossup_correctness | tier | winter | 2825 | 0.102698 | 0.180668 | 0.540118 | 0.582063 |
| tossup_correctness | category | Current Events | 123 | 0.100529 | 0.183661 | 0.608951 | 0.56519 |
| tossup_correctness | category | Fine Arts | 1093 | 0.110755 | 0.189553 | 0.539923 | 0.607532 |
| tossup_correctness | category | Geography | 191 | 0.159817 | 0.222372 | 0.674756 | 0.657304 |
| tossup_correctness | category | History | 1469 | 0.0985008 | 0.192511 | 0.547221 | 0.601896 |
| tossup_correctness | category | Literature | 1436 | 0.0856073 | 0.158817 | 0.514345 | 0.527574 |
| tossup_correctness | category | Mythology | 325 | 0.0571496 | 0.13406 | 0.569987 | 0.446301 |
| tossup_correctness | category | Other Academic | 67 | 0.107933 | 0.168791 | 0.551213 | 0.538916 |
| tossup_correctness | category | Philosophy | 322 | 0.121775 | 0.186106 | 0.496935 | 0.606809 |
| tossup_correctness | category | Popular Culture | 100 | 0.0329827 | 0.105231 | 0.544433 | 0.369765 |
| tossup_correctness | category | Religion | 365 | 0.14865 | 0.219803 | 0.562406 | 0.684616 |
| tossup_correctness | category | Science | 1456 | 0.0813924 | 0.184132 | 0.559239 | 0.576862 |
| tossup_correctness | category | Social Science | 333 | 0.144365 | 0.216748 | 0.517375 | 0.676154 |
| tossup_correctness | category | Unknown | 1990 | 0.106647 | 0.191548 | 0.525037 | 0.607291 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0833317 | 0.187963 | 0.543118 | 0.586358 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0990478 | 0.200291 | 0.480044 | 0.6252 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0914385 | 0.188592 | 0.532876 | 0.589292 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0795907 | 0.172639 | 0.561708 | 0.551667 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.1084 | 0.188013 | 0.547771 | 0.607355 |
