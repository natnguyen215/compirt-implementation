# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.656427 |
| log_loss | 0.518209 |
| ece | 0.0134786 |
| brier | 0.169154 |
| accuracy | 0.767617 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00236686 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.114356 |
| probability_p10 | 0.614547 |
| probability_p50 | 0.794102 |
| probability_p90 | 0.904487 |
| mean_predictive_variance | 0.16178 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.106486 |
| joint_tossup_event_log_loss | 7.10917 |
| buzz_position_mae | 0.165016 |
| buzz_position_median_absolute_error | 0.148892 |
| buzz_position_bias | -0.0696995 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.350619 |
| first_buzzer_mean_reciprocal_rank | 0.563895 |
| first_buzzer_log_loss | 1.71938 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.640882 |
| tossup_scorer_player_top1_accuracy | 0.322399 |
| tossup_scorer_team_top1_accuracy | 0.487261 |
| tossup_game_winner_accuracy | 0.801762 |
| tossup_game_margin_mae | 35.1918 |
| tournament_player_ppg_spearman | 0.688943 |
| tournament_player_ppg_mae | 9.40553 |
| tournament_player_ppg_top10_overlap | 0.648276 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.656427 |
| neg_average_precision | 0.37444 |
| neg_precision | 0.552885 |
| neg_recall | 0.0527039 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0560063 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0994924 |
| no_buzz_calibration_error | 0.0862227 |
| no_buzz_brier | 0.0290299 |
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
| overall | 9295 | -0.0696995 | -0.0836246 |
| Q1 (0-.2) | 197 | 0.34973 | 0.348644 |
| Q2 (.2-.4) | 985 | 0.192715 | 0.19436 |
| Q3 (.4-.6) | 2251 | 0.0423924 | 0.0506687 |
| Q4 (.6-.8) | 2866 | -0.0954555 | -0.0837498 |
| Q5 (.8-1) | 2996 | -0.243133 | -0.237308 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0134786 | 0.169154 | 0.656427 | 0.518209 |
| tossup_correctness | tier | fall | 2933 | 0.0217764 | 0.156526 | 0.645567 | 0.489609 |
| tossup_correctness | tier | nationals | 1584 | 0.0445809 | 0.190304 | 0.646807 | 0.565076 |
| tossup_correctness | tier | regionals | 1886 | 0.0235067 | 0.180491 | 0.63897 | 0.54434 |
| tossup_correctness | tier | winter | 2892 | 0.0371764 | 0.162982 | 0.675759 | 0.504506 |
| tossup_correctness | category | Current Events | 124 | 0.0665313 | 0.17363 | 0.676726 | 0.527782 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0376304 | 0.177306 | 0.621052 | 0.541912 |
| tossup_correctness | category | Geography | 197 | 0.0612405 | 0.19431 | 0.728788 | 0.568194 |
| tossup_correctness | category | History | 1491 | 0.0413766 | 0.157698 | 0.67416 | 0.489968 |
| tossup_correctness | category | Literature | 1472 | 0.0256762 | 0.151603 | 0.634314 | 0.48186 |
| tossup_correctness | category | Mythology | 332 | 0.0520591 | 0.145263 | 0.682557 | 0.45846 |
| tossup_correctness | category | Other Academic | 69 | 0.118737 | 0.194974 | 0.507919 | 0.581939 |
| tossup_correctness | category | Philosophy | 324 | 0.0388421 | 0.149222 | 0.672884 | 0.47152 |
| tossup_correctness | category | Popular Culture | 102 | 0.100969 | 0.161112 | 0.440138 | 0.507655 |
| tossup_correctness | category | Religion | 372 | 0.0586435 | 0.192847 | 0.676978 | 0.567553 |
| tossup_correctness | category | Science | 1487 | 0.0363037 | 0.171748 | 0.680807 | 0.522399 |
| tossup_correctness | category | Social Science | 336 | 0.0523797 | 0.192327 | 0.687669 | 0.566462 |
| tossup_correctness | category | Unknown | 1886 | 0.0235067 | 0.180491 | 0.63897 | 0.54434 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0722488 | 0.190483 | 0.607427 | 0.572338 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0133376 | 0.184115 | 0.641175 | 0.553685 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0116519 | 0.166283 | 0.664062 | 0.510332 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0188684 | 0.159941 | 0.656329 | 0.495852 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0335404 | 0.173802 | 0.661607 | 0.530293 |
