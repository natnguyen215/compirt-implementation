# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.560969 |
| log_loss | 0.562318 |
| ece | 0.0777519 |
| brier | 0.180273 |
| accuracy | 0.771521 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00183387 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.115447 |
| probability_p10 | 0.642867 |
| probability_p50 | 0.852781 |
| probability_p90 | 0.934532 |
| mean_predictive_variance | 0.136521 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.171184 |
| joint_tossup_event_log_loss | 7.69551 |
| buzz_position_mae | 0.32845 |
| buzz_position_median_absolute_error | 0.327257 |
| buzz_position_bias | -0.313898 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.339051 |
| first_buzzer_mean_reciprocal_rank | 0.550723 |
| first_buzzer_log_loss | 1.70857 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.620928 |
| tossup_scorer_player_top1_accuracy | 0.254478 |
| tossup_scorer_team_top1_accuracy | 0.39435 |
| tossup_game_winner_accuracy | 0.693654 |
| tossup_game_margin_mae | 46.1425 |
| tournament_player_ppg_spearman | 0.56467 |
| tournament_player_ppg_mae | 11.0227 |
| tournament_player_ppg_top10_overlap | 0.603448 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.560969 |
| neg_average_precision | 0.285242 |
| neg_precision | 0.42735 |
| neg_recall | 0.0237982 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.033282 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.218854 |
| no_buzz_calibration_error | 0.207127 |
| no_buzz_brier | 0.0635808 |
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
| overall | 9270 | -0.313898 | -0.327257 |
| Q1 (0-.2) | 179 | 0.177364 | 0.171503 |
| Q2 (.2-.4) | 957 | 0.0187445 | 0.0159761 |
| Q3 (.4-.6) | 2203 | -0.163515 | -0.165651 |
| Q4 (.6-.8) | 2978 | -0.341 | -0.340683 |
| Q5 (.8-1) | 2953 | -0.536336 | -0.53576 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0777519 | 0.180273 | 0.560969 | 0.562318 |
| tossup_correctness | tier | fall | 2876 | 0.0708041 | 0.169561 | 0.541561 | 0.538819 |
| tossup_correctness | tier | nationals | 1579 | 0.0728735 | 0.197757 | 0.591697 | 0.590599 |
| tossup_correctness | tier | regionals | 1990 | 0.0910499 | 0.187172 | 0.539179 | 0.579782 |
| tossup_correctness | tier | winter | 2825 | 0.0808022 | 0.176545 | 0.558089 | 0.558133 |
| tossup_correctness | category | Current Events | 123 | 0.0795697 | 0.172766 | 0.635363 | 0.529004 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0857638 | 0.183559 | 0.569862 | 0.573465 |
| tossup_correctness | category | Geography | 191 | 0.125985 | 0.212452 | 0.675783 | 0.622871 |
| tossup_correctness | category | History | 1469 | 0.0738078 | 0.1869 | 0.567515 | 0.574562 |
| tossup_correctness | category | Literature | 1436 | 0.084817 | 0.157892 | 0.53222 | 0.515348 |
| tossup_correctness | category | Mythology | 325 | 0.0432933 | 0.132096 | 0.620366 | 0.430598 |
| tossup_correctness | category | Other Academic | 67 | 0.100319 | 0.162992 | 0.606469 | 0.513621 |
| tossup_correctness | category | Philosophy | 322 | 0.123963 | 0.184948 | 0.489431 | 0.589653 |
| tossup_correctness | category | Popular Culture | 100 | 0.0606607 | 0.109209 | 0.615935 | 0.371688 |
| tossup_correctness | category | Religion | 365 | 0.125495 | 0.210748 | 0.584421 | 0.643133 |
| tossup_correctness | category | Science | 1456 | 0.0561805 | 0.180264 | 0.57299 | 0.557443 |
| tossup_correctness | category | Social Science | 333 | 0.121055 | 0.2138 | 0.509145 | 0.649381 |
| tossup_correctness | category | Unknown | 1990 | 0.0910499 | 0.187172 | 0.539179 | 0.579782 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0951182 | 0.189573 | 0.529353 | 0.580922 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.104286 | 0.197679 | 0.491495 | 0.603631 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0731065 | 0.185037 | 0.546409 | 0.569661 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0667979 | 0.168577 | 0.581701 | 0.529748 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0839042 | 0.182309 | 0.568017 | 0.57517 |
