# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.665471 |
| log_loss | 0.510063 |
| ece | 0.0272607 |
| brier | 0.164963 |
| accuracy | 0.77533 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00528634 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.13254 |
| probability_p10 | 0.570421 |
| probability_p50 | 0.777698 |
| probability_p90 | 0.906246 |
| mean_predictive_variance | 0.167325 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100632 |
| joint_tossup_event_log_loss | 6.85329 |
| buzz_position_mae | 0.159808 |
| buzz_position_median_absolute_error | 0.145282 |
| buzz_position_bias | -0.0670675 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349449 |
| first_buzzer_mean_reciprocal_rank | 0.561493 |
| first_buzzer_log_loss | 1.68732 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.656057 |
| tossup_scorer_player_top1_accuracy | 0.315184 |
| tossup_scorer_team_top1_accuracy | 0.508568 |
| tossup_game_winner_accuracy | 0.825221 |
| tossup_game_margin_mae | 35.4755 |
| tournament_player_ppg_spearman | 0.711959 |
| tournament_player_ppg_mae | 8.87736 |
| tournament_player_ppg_top10_overlap | 0.668966 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.665471 |
| neg_average_precision | 0.401484 |
| neg_precision | 0.554795 |
| neg_recall | 0.116379 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0554361 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.090475 |
| no_buzz_calibration_error | 0.0752906 |
| no_buzz_brier | 0.0255715 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9080 | -0.0670675 | -0.0838073 |
| Q1 (0-.2) | 192 | 0.372468 | 0.381463 |
| Q2 (.2-.4) | 889 | 0.20285 | 0.204761 |
| Q3 (.4-.6) | 2210 | 0.0481469 | 0.0501444 |
| Q4 (.6-.8) | 2869 | -0.0916028 | -0.0856028 |
| Q5 (.8-1) | 2920 | -0.241239 | -0.24258 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0272607 | 0.164963 | 0.665471 | 0.510063 |
| tossup_correctness | tier | fall | 2817 | 0.0261952 | 0.159791 | 0.655273 | 0.49734 |
| tossup_correctness | tier | nationals | 1542 | 0.0643725 | 0.178751 | 0.706983 | 0.537379 |
| tossup_correctness | tier | regionals | 1934 | 0.0197921 | 0.17066 | 0.666834 | 0.520075 |
| tossup_correctness | tier | winter | 2787 | 0.0344001 | 0.15861 | 0.644152 | 0.500862 |
| tossup_correctness | category | Current Events | 125 | 0.11437 | 0.181583 | 0.734337 | 0.54269 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0418652 | 0.166588 | 0.654496 | 0.511095 |
| tossup_correctness | category | Geography | 185 | 0.0694513 | 0.170125 | 0.773706 | 0.515379 |
| tossup_correctness | category | History | 1443 | 0.0359617 | 0.159945 | 0.716419 | 0.493516 |
| tossup_correctness | category | Literature | 1411 | 0.051327 | 0.153291 | 0.583236 | 0.499498 |
| tossup_correctness | category | Mythology | 320 | 0.0752732 | 0.162848 | 0.600453 | 0.508735 |
| tossup_correctness | category | Other Academic | 64 | 0.0908399 | 0.181971 | 0.589844 | 0.551561 |
| tossup_correctness | category | Philosophy | 312 | 0.0482218 | 0.159699 | 0.592 | 0.501478 |
| tossup_correctness | category | Popular Culture | 104 | 0.113008 | 0.147114 | 0.512784 | 0.474964 |
| tossup_correctness | category | Religion | 358 | 0.0264494 | 0.181906 | 0.688108 | 0.543816 |
| tossup_correctness | category | Science | 1431 | 0.0363871 | 0.165907 | 0.673448 | 0.508836 |
| tossup_correctness | category | Social Science | 321 | 0.0326188 | 0.176154 | 0.678947 | 0.53194 |
| tossup_correctness | category | Unknown | 1934 | 0.0197921 | 0.17066 | 0.666834 | 0.520075 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0511495 | 0.188215 | 0.718219 | 0.559058 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0374363 | 0.177939 | 0.692844 | 0.535214 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0342472 | 0.174021 | 0.642098 | 0.533651 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0333729 | 0.15719 | 0.656327 | 0.491004 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0307017 | 0.160266 | 0.672224 | 0.500058 |
