# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.563649 |
| log_loss | 0.566761 |
| ece | 0.0754535 |
| brier | 0.18377 |
| accuracy | 0.764605 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000645508 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.114626 |
| probability_p10 | 0.636601 |
| probability_p50 | 0.840302 |
| probability_p90 | 0.923838 |
| mean_predictive_variance | 0.14292 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.170505 |
| joint_tossup_event_log_loss | 7.67993 |
| buzz_position_mae | 0.324116 |
| buzz_position_median_absolute_error | 0.32248 |
| buzz_position_bias | -0.308305 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.316192 |
| first_buzzer_mean_reciprocal_rank | 0.5361 |
| first_buzzer_log_loss | 1.72411 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.611296 |
| tossup_scorer_player_top1_accuracy | 0.262527 |
| tossup_scorer_team_top1_accuracy | 0.379193 |
| tossup_game_winner_accuracy | 0.698238 |
| tossup_game_margin_mae | 44.2336 |
| tournament_player_ppg_spearman | 0.544139 |
| tournament_player_ppg_mae | 10.7085 |
| tournament_player_ppg_top10_overlap | 0.562069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.563649 |
| neg_average_precision | 0.297223 |
| neg_precision | 0.479167 |
| neg_recall | 0.0316224 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0347025 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.214136 |
| no_buzz_calibration_error | 0.200867 |
| no_buzz_brier | 0.0608053 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9295 | -0.308305 | -0.322237 |
| Q1 (0-.2) | 197 | 0.186495 | 0.178027 |
| Q2 (.2-.4) | 985 | 0.0169489 | 0.00887761 |
| Q3 (.4-.6) | 2251 | -0.159806 | -0.160094 |
| Q4 (.6-.8) | 2866 | -0.337222 | -0.33542 |
| Q5 (.8-1) | 2996 | -0.531684 | -0.53192 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0754535 | 0.18377 | 0.563649 | 0.566761 |
| tossup_correctness | tier | fall | 2933 | 0.057014 | 0.166374 | 0.572865 | 0.52177 |
| tossup_correctness | tier | nationals | 1584 | 0.0696944 | 0.199475 | 0.592103 | 0.59271 |
| tossup_correctness | tier | regionals | 1886 | 0.0973354 | 0.199123 | 0.526859 | 0.6055 |
| tossup_correctness | tier | winter | 2892 | 0.0840512 | 0.182798 | 0.547393 | 0.572913 |
| tossup_correctness | category | Current Events | 124 | 0.100883 | 0.190329 | 0.563302 | 0.57093 |
| tossup_correctness | category | Fine Arts | 1103 | 0.107435 | 0.194057 | 0.522092 | 0.602699 |
| tossup_correctness | category | Geography | 197 | 0.153047 | 0.234178 | 0.642424 | 0.677297 |
| tossup_correctness | category | History | 1491 | 0.0634956 | 0.171433 | 0.569304 | 0.531334 |
| tossup_correctness | category | Literature | 1472 | 0.0632713 | 0.159901 | 0.565327 | 0.512516 |
| tossup_correctness | category | Mythology | 332 | 0.0919388 | 0.158065 | 0.560394 | 0.498831 |
| tossup_correctness | category | Other Academic | 69 | 0.129226 | 0.200538 | 0.484163 | 0.609628 |
| tossup_correctness | category | Philosophy | 324 | 0.0631579 | 0.156554 | 0.607128 | 0.495395 |
| tossup_correctness | category | Popular Culture | 102 | 0.110985 | 0.159592 | 0.36609 | 0.512745 |
| tossup_correctness | category | Religion | 372 | 0.10363 | 0.20981 | 0.611777 | 0.628397 |
| tossup_correctness | category | Science | 1487 | 0.046182 | 0.181966 | 0.606413 | 0.557352 |
| tossup_correctness | category | Social Science | 336 | 0.12639 | 0.225855 | 0.540042 | 0.676766 |
| tossup_correctness | category | Unknown | 1886 | 0.0973354 | 0.199123 | 0.526859 | 0.6055 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0813165 | 0.205416 | 0.518302 | 0.607414 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0793474 | 0.199271 | 0.552772 | 0.598764 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0621291 | 0.177413 | 0.58453 | 0.544213 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0699156 | 0.172367 | 0.569469 | 0.536407 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0971555 | 0.192934 | 0.552946 | 0.599543 |
