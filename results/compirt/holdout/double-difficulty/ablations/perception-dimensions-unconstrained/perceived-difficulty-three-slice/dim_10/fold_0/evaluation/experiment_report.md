# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.655194 |
| log_loss | 0.518254 |
| ece | 0.0119288 |
| brier | 0.169326 |
| accuracy | 0.767617 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00236686 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.105061 |
| probability_p10 | 0.631683 |
| probability_p50 | 0.793136 |
| probability_p90 | 0.897656 |
| mean_predictive_variance | 0.162476 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.109179 |
| joint_tossup_event_log_loss | 7.14501 |
| buzz_position_mae | 0.170487 |
| buzz_position_median_absolute_error | 0.154048 |
| buzz_position_bias | -0.0766227 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34653 |
| first_buzzer_mean_reciprocal_rank | 0.561689 |
| first_buzzer_log_loss | 1.73985 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637224 |
| tossup_scorer_player_top1_accuracy | 0.31741 |
| tossup_scorer_team_top1_accuracy | 0.492251 |
| tossup_game_winner_accuracy | 0.781938 |
| tossup_game_margin_mae | 36.4605 |
| tournament_player_ppg_spearman | 0.66371 |
| tournament_player_ppg_mae | 9.79475 |
| tournament_player_ppg_top10_overlap | 0.644828 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.655194 |
| neg_average_precision | 0.373039 |
| neg_precision | 0.58209 |
| neg_recall | 0.035747 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.053925 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0914735 |
| no_buzz_calibration_error | 0.0782038 |
| no_buzz_brier | 0.0259445 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9295 | -0.0766227 | -0.0911049 |
| Q1 (0-.2) | 197 | 0.358452 | 0.362411 |
| Q2 (.2-.4) | 985 | 0.196364 | 0.197358 |
| Q3 (.4-.6) | 2251 | 0.0412461 | 0.0498729 |
| Q4 (.6-.8) | 2866 | -0.102694 | -0.0940557 |
| Q5 (.8-1) | 2996 | -0.2586 | -0.254961 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0119288 | 0.169326 | 0.655194 | 0.518254 |
| tossup_correctness | tier | fall | 2933 | 0.0187 | 0.155844 | 0.651703 | 0.487202 |
| tossup_correctness | tier | nationals | 1584 | 0.0228743 | 0.187134 | 0.656375 | 0.557682 |
| tossup_correctness | tier | regionals | 1886 | 0.0162705 | 0.180749 | 0.636724 | 0.544071 |
| tossup_correctness | tier | winter | 2892 | 0.0426346 | 0.165797 | 0.66547 | 0.511315 |
| tossup_correctness | category | Current Events | 124 | 0.0945184 | 0.1709 | 0.674991 | 0.522544 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0407531 | 0.17771 | 0.619291 | 0.543133 |
| tossup_correctness | category | Geography | 197 | 0.0829825 | 0.194819 | 0.745804 | 0.567827 |
| tossup_correctness | category | History | 1491 | 0.0223466 | 0.156201 | 0.677769 | 0.485367 |
| tossup_correctness | category | Literature | 1472 | 0.0293497 | 0.151623 | 0.634314 | 0.481369 |
| tossup_correctness | category | Mythology | 332 | 0.0425362 | 0.142852 | 0.68871 | 0.452318 |
| tossup_correctness | category | Other Academic | 69 | 0.100736 | 0.20044 | 0.447964 | 0.596073 |
| tossup_correctness | category | Philosophy | 324 | 0.0313606 | 0.148687 | 0.673834 | 0.468345 |
| tossup_correctness | category | Popular Culture | 102 | 0.124003 | 0.159787 | 0.419377 | 0.504313 |
| tossup_correctness | category | Religion | 372 | 0.0580166 | 0.19457 | 0.674032 | 0.573148 |
| tossup_correctness | category | Science | 1487 | 0.00928877 | 0.172568 | 0.666645 | 0.524194 |
| tossup_correctness | category | Social Science | 336 | 0.0586796 | 0.198235 | 0.662458 | 0.583019 |
| tossup_correctness | category | Unknown | 1886 | 0.0162705 | 0.180749 | 0.636724 | 0.544071 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.057029 | 0.193322 | 0.60809 | 0.577548 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0237133 | 0.184844 | 0.636036 | 0.555226 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0112481 | 0.16642 | 0.664196 | 0.51006 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0179403 | 0.159548 | 0.660992 | 0.494084 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0411067 | 0.174185 | 0.658287 | 0.531478 |
