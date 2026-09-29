# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.614225 |
| log_loss | 0.544188 |
| ece | 0.051396 |
| brier | 0.178763 |
| accuracy | 0.756185 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00799395 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.138264 |
| probability_p10 | 0.56204 |
| probability_p50 | 0.786623 |
| probability_p90 | 0.913303 |
| mean_predictive_variance | 0.163792 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.104294 |
| joint_tossup_event_log_loss | 6.95396 |
| buzz_position_mae | 0.161831 |
| buzz_position_median_absolute_error | 0.145258 |
| buzz_position_bias | -0.0654451 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.331857 |
| first_buzzer_mean_reciprocal_rank | 0.548524 |
| first_buzzer_log_loss | 1.69314 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.651183 |
| tossup_scorer_player_top1_accuracy | 0.303198 |
| tossup_scorer_team_top1_accuracy | 0.472495 |
| tossup_game_winner_accuracy | 0.771739 |
| tossup_game_margin_mae | 36.7052 |
| tournament_player_ppg_spearman | 0.693987 |
| tournament_player_ppg_mae | 8.67886 |
| tournament_player_ppg_top10_overlap | 0.648276 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.614225 |
| neg_average_precision | 0.324826 |
| neg_precision | 0.426 |
| neg_recall | 0.0975721 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0575287 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0895 |
| no_buzz_calibration_error | 0.076387 |
| no_buzz_brier | 0.023951 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0654451 | -0.079843 |
| Q1 (0-.2) | 183 | 0.382914 | 0.389109 |
| Q2 (.2-.4) | 955 | 0.210952 | 0.2135 |
| Q3 (.4-.6) | 2239 | 0.0532107 | 0.0522161 |
| Q4 (.6-.8) | 2875 | -0.0880449 | -0.0835515 |
| Q5 (.8-1) | 3005 | -0.247377 | -0.245527 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.051396 | 0.178763 | 0.614225 | 0.544188 |
| tossup_correctness | tier | fall | 2798 | 0.0625802 | 0.174254 | 0.578003 | 0.539096 |
| tossup_correctness | tier | nationals | 1545 | 0.0483098 | 0.192632 | 0.653461 | 0.567479 |
| tossup_correctness | tier | regionals | 2039 | 0.0618604 | 0.182552 | 0.586501 | 0.556164 |
| tossup_correctness | tier | winter | 2875 | 0.0413516 | 0.17301 | 0.632515 | 0.528132 |
| tossup_correctness | category | Current Events | 129 | 0.0760744 | 0.224289 | 0.570038 | 0.641523 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0640846 | 0.177156 | 0.584512 | 0.545284 |
| tossup_correctness | category | Geography | 180 | 0.0996178 | 0.218336 | 0.691996 | 0.632563 |
| tossup_correctness | category | History | 1454 | 0.0587718 | 0.185047 | 0.610094 | 0.553205 |
| tossup_correctness | category | Literature | 1435 | 0.0400446 | 0.15187 | 0.614037 | 0.487528 |
| tossup_correctness | category | Mythology | 324 | 0.0792907 | 0.17 | 0.602764 | 0.518498 |
| tossup_correctness | category | Other Academic | 71 | 0.169615 | 0.208502 | 0.368192 | 0.614261 |
| tossup_correctness | category | Philosophy | 310 | 0.058408 | 0.170968 | 0.662277 | 0.522993 |
| tossup_correctness | category | Popular Culture | 108 | 0.191103 | 0.160385 | 0.527778 | 0.493831 |
| tossup_correctness | category | Religion | 361 | 0.0729518 | 0.19192 | 0.596654 | 0.577142 |
| tossup_correctness | category | Science | 1445 | 0.0441639 | 0.185454 | 0.626119 | 0.556042 |
| tossup_correctness | category | Social Science | 327 | 0.0186838 | 0.182326 | 0.692322 | 0.545616 |
| tossup_correctness | category | Unknown | 2039 | 0.0618604 | 0.182552 | 0.586501 | 0.556164 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.103255 | 0.208243 | 0.545839 | 0.610387 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0766283 | 0.20449 | 0.576088 | 0.600663 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0507349 | 0.184416 | 0.613456 | 0.553557 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0390459 | 0.163757 | 0.630339 | 0.50651 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0544884 | 0.178935 | 0.611184 | 0.551275 |
