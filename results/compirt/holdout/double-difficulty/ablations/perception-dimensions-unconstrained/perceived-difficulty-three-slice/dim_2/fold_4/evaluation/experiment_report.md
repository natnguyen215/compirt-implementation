# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.612851 |
| log_loss | 0.534115 |
| ece | 0.0554665 |
| brier | 0.174412 |
| accuracy | 0.763862 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00949299 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.138368 |
| probability_p10 | 0.565978 |
| probability_p50 | 0.78475 |
| probability_p90 | 0.917156 |
| mean_predictive_variance | 0.163373 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10304 |
| joint_tossup_event_log_loss | 6.96327 |
| buzz_position_mae | 0.16132 |
| buzz_position_median_absolute_error | 0.147566 |
| buzz_position_bias | -0.064217 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.338188 |
| first_buzzer_mean_reciprocal_rank | 0.550208 |
| first_buzzer_log_loss | 1.71256 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637864 |
| tossup_scorer_player_top1_accuracy | 0.299041 |
| tossup_scorer_team_top1_accuracy | 0.472814 |
| tossup_game_winner_accuracy | 0.785558 |
| tossup_game_margin_mae | 34.7412 |
| tournament_player_ppg_spearman | 0.674601 |
| tournament_player_ppg_mae | 9.30955 |
| tournament_player_ppg_top10_overlap | 0.668966 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.612851 |
| neg_average_precision | 0.317902 |
| neg_precision | 0.411647 |
| neg_recall | 0.0975726 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0564033 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0882772 |
| no_buzz_calibration_error | 0.0765501 |
| no_buzz_brier | 0.0237849 |
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
| overall | 9270 | -0.064217 | -0.0818342 |
| Q1 (0-.2) | 179 | 0.366383 | 0.363372 |
| Q2 (.2-.4) | 957 | 0.211235 | 0.210161 |
| Q3 (.4-.6) | 2203 | 0.0575234 | 0.0599658 |
| Q4 (.6-.8) | 2978 | -0.0884191 | -0.0867918 |
| Q5 (.8-1) | 2953 | -0.246 | -0.243775 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0554665 | 0.174412 | 0.612851 | 0.534115 |
| tossup_correctness | tier | fall | 2876 | 0.0751238 | 0.169388 | 0.574598 | 0.527963 |
| tossup_correctness | tier | nationals | 1579 | 0.0568244 | 0.192208 | 0.63647 | 0.569336 |
| tossup_correctness | tier | regionals | 1990 | 0.0438356 | 0.177288 | 0.617088 | 0.540263 |
| tossup_correctness | tier | winter | 2825 | 0.0431809 | 0.167554 | 0.621999 | 0.516362 |
| tossup_correctness | category | Current Events | 123 | 0.115977 | 0.18725 | 0.601981 | 0.563963 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0598636 | 0.176685 | 0.601188 | 0.541878 |
| tossup_correctness | category | Geography | 191 | 0.0705236 | 0.187825 | 0.724448 | 0.555663 |
| tossup_correctness | category | History | 1469 | 0.0490337 | 0.180328 | 0.636903 | 0.541117 |
| tossup_correctness | category | Literature | 1436 | 0.062124 | 0.154972 | 0.567246 | 0.500779 |
| tossup_correctness | category | Mythology | 325 | 0.1249 | 0.156477 | 0.580077 | 0.485658 |
| tossup_correctness | category | Other Academic | 67 | 0.160832 | 0.18927 | 0.580863 | 0.571129 |
| tossup_correctness | category | Philosophy | 322 | 0.0355823 | 0.163753 | 0.636822 | 0.505583 |
| tossup_correctness | category | Popular Culture | 100 | 0.237315 | 0.16093 | 0.59142 | 0.500421 |
| tossup_correctness | category | Religion | 365 | 0.0784629 | 0.203245 | 0.611724 | 0.59877 |
| tossup_correctness | category | Science | 1456 | 0.067182 | 0.174194 | 0.616414 | 0.53266 |
| tossup_correctness | category | Social Science | 333 | 0.057323 | 0.193283 | 0.608596 | 0.574432 |
| tossup_correctness | category | Unknown | 1990 | 0.0438356 | 0.177288 | 0.617088 | 0.540263 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.135854 | 0.19572 | 0.585904 | 0.582902 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0977456 | 0.202499 | 0.545706 | 0.597188 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.060905 | 0.179595 | 0.605608 | 0.544413 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0468307 | 0.164207 | 0.621712 | 0.508607 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0460514 | 0.170443 | 0.633064 | 0.528759 |
