# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.645403 |
| log_loss | 0.524217 |
| ece | 0.0305484 |
| brier | 0.171254 |
| accuracy | 0.765573 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.000322754 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.129949 |
| probability_p10 | 0.578939 |
| probability_p50 | 0.784193 |
| probability_p90 | 0.907571 |
| mean_predictive_variance | 0.165348 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101902 |
| joint_tossup_event_log_loss | 6.91346 |
| buzz_position_mae | 0.160675 |
| buzz_position_median_absolute_error | 0.148198 |
| buzz_position_bias | -0.0649778 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.343948 |
| first_buzzer_mean_reciprocal_rank | 0.559674 |
| first_buzzer_log_loss | 1.68403 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.639376 |
| tossup_scorer_player_top1_accuracy | 0.312527 |
| tossup_scorer_team_top1_accuracy | 0.478238 |
| tossup_game_winner_accuracy | 0.799559 |
| tossup_game_margin_mae | 34.281 |
| tournament_player_ppg_spearman | 0.67555 |
| tournament_player_ppg_mae | 8.9986 |
| tournament_player_ppg_top10_overlap | 0.651724 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.645403 |
| neg_average_precision | 0.366429 |
| neg_precision | 0.50348 |
| neg_recall | 0.09945 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0563015 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0917439 |
| no_buzz_calibration_error | 0.0784743 |
| no_buzz_brier | 0.025582 |
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
| overall | 9295 | -0.0649778 | -0.0811895 |
| Q1 (0-.2) | 197 | 0.353842 | 0.358798 |
| Q2 (.2-.4) | 985 | 0.2015 | 0.200767 |
| Q3 (.4-.6) | 2251 | 0.0505327 | 0.0518557 |
| Q4 (.6-.8) | 2866 | -0.0910091 | -0.0850102 |
| Q5 (.8-1) | 2996 | -0.242013 | -0.239373 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0305484 | 0.171254 | 0.645403 | 0.524217 |
| tossup_correctness | tier | fall | 2933 | 0.0345359 | 0.161458 | 0.615337 | 0.505796 |
| tossup_correctness | tier | nationals | 1584 | 0.0603829 | 0.190276 | 0.656485 | 0.564487 |
| tossup_correctness | tier | regionals | 1886 | 0.0262221 | 0.18241 | 0.634117 | 0.548372 |
| tossup_correctness | tier | winter | 2892 | 0.02139 | 0.163494 | 0.663456 | 0.505091 |
| tossup_correctness | category | Current Events | 124 | 0.077617 | 0.174593 | 0.691988 | 0.526674 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0530057 | 0.178917 | 0.60983 | 0.545747 |
| tossup_correctness | category | Geography | 197 | 0.0560393 | 0.193823 | 0.723077 | 0.567659 |
| tossup_correctness | category | History | 1491 | 0.0779664 | 0.160771 | 0.677712 | 0.498628 |
| tossup_correctness | category | Literature | 1472 | 0.0392865 | 0.153538 | 0.616497 | 0.489357 |
| tossup_correctness | category | Mythology | 332 | 0.0778614 | 0.152588 | 0.653345 | 0.47633 |
| tossup_correctness | category | Other Academic | 69 | 0.143483 | 0.194201 | 0.520362 | 0.577732 |
| tossup_correctness | category | Philosophy | 324 | 0.0355905 | 0.14985 | 0.678586 | 0.470207 |
| tossup_correctness | category | Popular Culture | 102 | 0.145205 | 0.179398 | 0.492042 | 0.542654 |
| tossup_correctness | category | Religion | 372 | 0.0408484 | 0.194 | 0.666316 | 0.572844 |
| tossup_correctness | category | Science | 1487 | 0.0339646 | 0.172329 | 0.671681 | 0.527104 |
| tossup_correctness | category | Social Science | 336 | 0.0340306 | 0.195098 | 0.662542 | 0.57405 |
| tossup_correctness | category | Unknown | 1886 | 0.0262221 | 0.18241 | 0.634117 | 0.548372 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0822155 | 0.190642 | 0.634218 | 0.572612 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0528334 | 0.191348 | 0.611741 | 0.571995 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0272197 | 0.169317 | 0.645937 | 0.518694 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0282587 | 0.160403 | 0.653584 | 0.497141 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0301613 | 0.175208 | 0.652058 | 0.535377 |
