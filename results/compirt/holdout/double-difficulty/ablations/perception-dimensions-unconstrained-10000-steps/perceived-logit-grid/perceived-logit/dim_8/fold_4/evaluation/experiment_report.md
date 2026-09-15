# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.624857 |
| log_loss | 0.574434 |
| ece | 0.138263 |
| brier | 0.193201 |
| accuracy | 0.718986 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0543689 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.159541 |
| probability_p10 | 0.425049 |
| probability_p50 | 0.654604 |
| probability_p90 | 0.844408 |
| mean_predictive_variance | 0.203934 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.103023 |
| joint_tossup_event_log_loss | 6.7006 |
| buzz_position_mae | 0.166259 |
| buzz_position_median_absolute_error | 0.149227 |
| buzz_position_bias | -0.0845352 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.396656 |
| first_buzzer_mean_reciprocal_rank | 0.598137 |
| first_buzzer_log_loss | 1.60693 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.656419 |
| tossup_scorer_player_top1_accuracy | 0.284009 |
| tossup_scorer_team_top1_accuracy | 0.416738 |
| tossup_game_winner_accuracy | 0.792123 |
| tossup_game_margin_mae | 38.81 |
| tournament_player_ppg_spearman | 0.632649 |
| tournament_player_ppg_mae | 11.6468 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.624857 |
| neg_average_precision | 0.320949 |
| neg_precision | 0.359218 |
| neg_recall | 0.306045 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.100554 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0755111 |
| no_buzz_calibration_error | 0.0637841 |
| no_buzz_brier | 0.0231184 |
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
| overall | 9270 | -0.0845352 | -0.0951709 |
| Q1 (0-.2) | 179 | 0.330462 | 0.330405 |
| Q2 (.2-.4) | 957 | 0.178559 | 0.174925 |
| Q3 (.4-.6) | 2203 | 0.0258873 | 0.0184863 |
| Q4 (.6-.8) | 2978 | -0.106555 | -0.107398 |
| Q5 (.8-1) | 2953 | -0.255125 | -0.246603 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.138263 | 0.193201 | 0.624857 | 0.574434 |
| tossup_correctness | tier | fall | 2876 | 0.120758 | 0.176693 | 0.615821 | 0.542667 |
| tossup_correctness | tier | nationals | 1579 | 0.13829 | 0.212339 | 0.632679 | 0.611576 |
| tossup_correctness | tier | regionals | 1990 | 0.147748 | 0.200269 | 0.619049 | 0.589193 |
| tossup_correctness | tier | winter | 2825 | 0.149832 | 0.194332 | 0.613808 | 0.575619 |
| tossup_correctness | category | Current Events | 123 | 0.127512 | 0.192103 | 0.644167 | 0.564242 |
| tossup_correctness | category | Fine Arts | 1093 | 0.143604 | 0.194606 | 0.639295 | 0.576423 |
| tossup_correctness | category | Geography | 191 | 0.114663 | 0.217944 | 0.616718 | 0.632032 |
| tossup_correctness | category | History | 1469 | 0.102579 | 0.186162 | 0.6561 | 0.556187 |
| tossup_correctness | category | Literature | 1436 | 0.159411 | 0.188371 | 0.569657 | 0.564907 |
| tossup_correctness | category | Mythology | 325 | 0.23785 | 0.198319 | 0.501217 | 0.588204 |
| tossup_correctness | category | Other Academic | 67 | 0.241333 | 0.218121 | 0.668464 | 0.624023 |
| tossup_correctness | category | Philosophy | 322 | 0.151882 | 0.190532 | 0.617632 | 0.570437 |
| tossup_correctness | category | Popular Culture | 100 | 0.252162 | 0.169507 | 0.547497 | 0.528985 |
| tossup_correctness | category | Religion | 365 | 0.0978101 | 0.182815 | 0.726935 | 0.551239 |
| tossup_correctness | category | Science | 1456 | 0.125485 | 0.192024 | 0.618138 | 0.575328 |
| tossup_correctness | category | Social Science | 333 | 0.121763 | 0.20067 | 0.67069 | 0.587629 |
| tossup_correctness | category | Unknown | 1990 | 0.147748 | 0.200269 | 0.619049 | 0.589193 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.33972 | 0.291057 | 0.547098 | 0.791223 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.237883 | 0.240936 | 0.615412 | 0.676941 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.187058 | 0.209877 | 0.635472 | 0.610337 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.140483 | 0.179614 | 0.654045 | 0.542972 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0595821 | 0.173062 | 0.635952 | 0.533018 |
