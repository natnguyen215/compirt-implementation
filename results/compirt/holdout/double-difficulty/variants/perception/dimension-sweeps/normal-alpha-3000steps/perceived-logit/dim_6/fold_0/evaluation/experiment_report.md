# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.554777 |
| log_loss | 0.577715 |
| ece | 0.0823619 |
| brier | 0.185956 |
| accuracy | 0.765465 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.000215169 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.112354 |
| probability_p10 | 0.655483 |
| probability_p50 | 0.854881 |
| probability_p90 | 0.933144 |
| mean_predictive_variance | 0.134532 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.170339 |
| joint_tossup_event_log_loss | 7.68296 |
| buzz_position_mae | 0.328052 |
| buzz_position_median_absolute_error | 0.326762 |
| buzz_position_bias | -0.313279 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.340075 |
| first_buzzer_mean_reciprocal_rank | 0.557232 |
| first_buzzer_log_loss | 1.68468 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.621087 |
| tossup_scorer_player_top1_accuracy | 0.266561 |
| tossup_scorer_team_top1_accuracy | 0.386943 |
| tossup_game_winner_accuracy | 0.711454 |
| tossup_game_margin_mae | 43.6788 |
| tournament_player_ppg_spearman | 0.568674 |
| tournament_player_ppg_mae | 10.4629 |
| tournament_player_ppg_top10_overlap | 0.610345 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.554777 |
| neg_average_precision | 0.288943 |
| neg_precision | 0.508475 |
| neg_recall | 0.0274977 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0330132 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.223426 |
| no_buzz_calibration_error | 0.210156 |
| no_buzz_brier | 0.0654855 |
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
| overall | 9295 | -0.313279 | -0.326651 |
| Q1 (0-.2) | 197 | 0.179465 | 0.169067 |
| Q2 (.2-.4) | 985 | 0.0119446 | 0.00704018 |
| Q3 (.4-.6) | 2251 | -0.163987 | -0.16506 |
| Q4 (.6-.8) | 2866 | -0.341886 | -0.340744 |
| Q5 (.8-1) | 2996 | -0.537405 | -0.538767 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0823619 | 0.185956 | 0.554777 | 0.577715 |
| tossup_correctness | tier | fall | 2933 | 0.0675787 | 0.168963 | 0.558541 | 0.532676 |
| tossup_correctness | tier | nationals | 1584 | 0.0714159 | 0.200776 | 0.58354 | 0.599335 |
| tossup_correctness | tier | regionals | 1886 | 0.109288 | 0.201452 | 0.521602 | 0.617556 |
| tossup_correctness | tier | winter | 2892 | 0.0926479 | 0.184966 | 0.538278 | 0.585569 |
| tossup_correctness | category | Current Events | 124 | 0.115262 | 0.19457 | 0.551162 | 0.583692 |
| tossup_correctness | category | Fine Arts | 1103 | 0.117519 | 0.197388 | 0.513703 | 0.619094 |
| tossup_correctness | category | Geography | 197 | 0.157461 | 0.238152 | 0.64662 | 0.691365 |
| tossup_correctness | category | History | 1491 | 0.0618907 | 0.172023 | 0.558889 | 0.537882 |
| tossup_correctness | category | Literature | 1472 | 0.0791304 | 0.161622 | 0.557798 | 0.520478 |
| tossup_correctness | category | Mythology | 332 | 0.0901832 | 0.157543 | 0.557646 | 0.501933 |
| tossup_correctness | category | Other Academic | 69 | 0.149169 | 0.196591 | 0.489819 | 0.612382 |
| tossup_correctness | category | Philosophy | 324 | 0.0719318 | 0.157603 | 0.596495 | 0.503446 |
| tossup_correctness | category | Popular Culture | 102 | 0.107673 | 0.157171 | 0.33564 | 0.518969 |
| tossup_correctness | category | Religion | 372 | 0.116067 | 0.212599 | 0.61318 | 0.640997 |
| tossup_correctness | category | Science | 1487 | 0.0576233 | 0.185633 | 0.591374 | 0.570506 |
| tossup_correctness | category | Social Science | 336 | 0.136949 | 0.229991 | 0.539153 | 0.69597 |
| tossup_correctness | category | Unknown | 1886 | 0.109288 | 0.201452 | 0.521602 | 0.617556 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0978635 | 0.205404 | 0.524801 | 0.61175 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0888966 | 0.202896 | 0.536007 | 0.614326 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0634442 | 0.179464 | 0.574383 | 0.553041 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.076899 | 0.173985 | 0.559786 | 0.545105 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.104207 | 0.195437 | 0.546599 | 0.613173 |
