# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.553942 |
| log_loss | 0.599362 |
| ece | 0.105356 |
| brier | 0.186551 |
| accuracy | 0.773031 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.000323625 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0877394 |
| probability_p10 | 0.762258 |
| probability_p50 | 0.897293 |
| probability_p90 | 0.955917 |
| mean_predictive_variance | 0.102986 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173209 |
| joint_tossup_event_log_loss | 7.79412 |
| buzz_position_mae | 0.33942 |
| buzz_position_median_absolute_error | 0.342914 |
| buzz_position_bias | -0.327296 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.339374 |
| first_buzzer_mean_reciprocal_rank | 0.554933 |
| first_buzzer_log_loss | 1.69072 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.62438 |
| tossup_scorer_player_top1_accuracy | 0.256397 |
| tossup_scorer_team_top1_accuracy | 0.423774 |
| tossup_game_winner_accuracy | 0.719912 |
| tossup_game_margin_mae | 43.9089 |
| tournament_player_ppg_spearman | 0.628428 |
| tournament_player_ppg_mae | 10.3888 |
| tournament_player_ppg_top10_overlap | 0.62069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.553942 |
| neg_average_precision | 0.269618 |
| neg_precision | 0.454545 |
| neg_recall | 0.00713946 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0285527 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.234717 |
| no_buzz_calibration_error | 0.22299 |
| no_buzz_brier | 0.0717722 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9270 | -0.327296 | -0.342914 |
| Q1 (0-.2) | 179 | 0.166682 | 0.168598 |
| Q2 (.2-.4) | 957 | 0.00441434 | 0.00183537 |
| Q3 (.4-.6) | 2203 | -0.174598 | -0.176826 |
| Q4 (.6-.8) | 2978 | -0.35475 | -0.354072 |
| Q5 (.8-1) | 2953 | -0.550969 | -0.5534 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.105356 | 0.186551 | 0.553942 | 0.599362 |
| tossup_correctness | tier | fall | 2876 | 0.0864977 | 0.171846 | 0.543458 | 0.554935 |
| tossup_correctness | tier | nationals | 1579 | 0.13463 | 0.21504 | 0.571756 | 0.679678 |
| tossup_correctness | tier | regionals | 1990 | 0.119326 | 0.194223 | 0.531623 | 0.624687 |
| tossup_correctness | tier | winter | 2825 | 0.108955 | 0.180193 | 0.567378 | 0.581861 |
| tossup_correctness | category | Current Events | 123 | 0.115959 | 0.185683 | 0.591709 | 0.583709 |
| tossup_correctness | category | Fine Arts | 1093 | 0.126917 | 0.19128 | 0.564256 | 0.616689 |
| tossup_correctness | category | Geography | 191 | 0.184435 | 0.228609 | 0.6849 | 0.687185 |
| tossup_correctness | category | History | 1469 | 0.113576 | 0.194921 | 0.567929 | 0.612692 |
| tossup_correctness | category | Literature | 1436 | 0.0825913 | 0.158119 | 0.537512 | 0.531003 |
| tossup_correctness | category | Mythology | 325 | 0.0617121 | 0.135526 | 0.574639 | 0.451515 |
| tossup_correctness | category | Other Academic | 67 | 0.0962241 | 0.173651 | 0.528302 | 0.567452 |
| tossup_correctness | category | Philosophy | 322 | 0.115806 | 0.184911 | 0.502205 | 0.608596 |
| tossup_correctness | category | Popular Culture | 100 | 0.0337301 | 0.1062 | 0.537283 | 0.374195 |
| tossup_correctness | category | Religion | 365 | 0.161048 | 0.223192 | 0.571595 | 0.699396 |
| tossup_correctness | category | Science | 1456 | 0.0933445 | 0.187737 | 0.552259 | 0.59638 |
| tossup_correctness | category | Social Science | 333 | 0.145373 | 0.219816 | 0.513992 | 0.695348 |
| tossup_correctness | category | Unknown | 1990 | 0.119326 | 0.194223 | 0.531623 | 0.624687 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.110935 | 0.19521 | 0.514096 | 0.624807 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.103295 | 0.200855 | 0.49517 | 0.63153 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.107271 | 0.190488 | 0.548768 | 0.600613 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0939097 | 0.174432 | 0.571601 | 0.563727 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.124625 | 0.190674 | 0.560521 | 0.622399 |
