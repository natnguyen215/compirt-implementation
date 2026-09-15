# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.655053 |
| log_loss | 0.522655 |
| ece | 0.0360398 |
| brier | 0.170718 |
| accuracy | 0.764286 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.000108026 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.14105 |
| probability_p10 | 0.550532 |
| probability_p50 | 0.776373 |
| probability_p90 | 0.911368 |
| mean_predictive_variance | 0.167348 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.103608 |
| joint_tossup_event_log_loss | 6.94209 |
| buzz_position_mae | 0.160791 |
| buzz_position_median_absolute_error | 0.142527 |
| buzz_position_bias | -0.0644277 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.346981 |
| first_buzzer_mean_reciprocal_rank | 0.560167 |
| first_buzzer_log_loss | 1.69262 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.659069 |
| tossup_scorer_player_top1_accuracy | 0.316951 |
| tossup_scorer_team_top1_accuracy | 0.489872 |
| tossup_game_winner_accuracy | 0.780435 |
| tossup_game_margin_mae | 36.7763 |
| tournament_player_ppg_spearman | 0.70622 |
| tournament_player_ppg_mae | 8.8492 |
| tournament_player_ppg_top10_overlap | 0.651724 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.655053 |
| neg_average_precision | 0.383168 |
| neg_precision | 0.500882 |
| neg_recall | 0.130096 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0573642 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0899574 |
| no_buzz_calibration_error | 0.0768444 |
| no_buzz_brier | 0.0243601 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9257 | -0.0644277 | -0.0781224 |
| Q1 (0-.2) | 183 | 0.381027 | 0.389165 |
| Q2 (.2-.4) | 955 | 0.208281 | 0.212007 |
| Q3 (.4-.6) | 2239 | 0.0533519 | 0.0541427 |
| Q4 (.6-.8) | 2875 | -0.0861119 | -0.0810172 |
| Q5 (.8-1) | 3005 | -0.245234 | -0.241733 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0360398 | 0.170718 | 0.655053 | 0.522655 |
| tossup_correctness | tier | fall | 2798 | 0.0385458 | 0.160511 | 0.646165 | 0.500206 |
| tossup_correctness | tier | nationals | 1545 | 0.0479344 | 0.18684 | 0.685102 | 0.553502 |
| tossup_correctness | tier | regionals | 2039 | 0.0533426 | 0.177 | 0.621624 | 0.540921 |
| tossup_correctness | tier | winter | 2875 | 0.027578 | 0.167532 | 0.657667 | 0.51497 |
| tossup_correctness | category | Current Events | 129 | 0.0626562 | 0.207925 | 0.650352 | 0.603202 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0476424 | 0.171267 | 0.622552 | 0.524748 |
| tossup_correctness | category | Geography | 180 | 0.0696175 | 0.203106 | 0.721635 | 0.594067 |
| tossup_correctness | category | History | 1454 | 0.0359838 | 0.172144 | 0.673177 | 0.521205 |
| tossup_correctness | category | Literature | 1435 | 0.035341 | 0.144813 | 0.646831 | 0.467772 |
| tossup_correctness | category | Mythology | 324 | 0.052736 | 0.158937 | 0.647366 | 0.493157 |
| tossup_correctness | category | Other Academic | 71 | 0.127163 | 0.205684 | 0.417211 | 0.606415 |
| tossup_correctness | category | Philosophy | 310 | 0.0316482 | 0.172668 | 0.659929 | 0.521921 |
| tossup_correctness | category | Popular Culture | 108 | 0.184968 | 0.141375 | 0.576389 | 0.454192 |
| tossup_correctness | category | Religion | 361 | 0.0701392 | 0.181881 | 0.650457 | 0.54713 |
| tossup_correctness | category | Science | 1445 | 0.0224548 | 0.175934 | 0.672628 | 0.53164 |
| tossup_correctness | category | Social Science | 327 | 0.031355 | 0.181124 | 0.695328 | 0.54571 |
| tossup_correctness | category | Unknown | 2039 | 0.0533426 | 0.177 | 0.621624 | 0.540921 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.112481 | 0.195563 | 0.61311 | 0.581226 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0388526 | 0.187649 | 0.647301 | 0.560044 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0251552 | 0.172887 | 0.670105 | 0.524749 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0385545 | 0.158349 | 0.66387 | 0.491591 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0379774 | 0.174042 | 0.638307 | 0.535365 |
