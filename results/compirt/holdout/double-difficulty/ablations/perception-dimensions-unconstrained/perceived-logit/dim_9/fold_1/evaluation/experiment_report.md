# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.571339 |
| log_loss | 0.560563 |
| ece | 0.0671239 |
| brier | 0.18385 |
| accuracy | 0.760805 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0013197 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.117396 |
| probability_p10 | 0.605619 |
| probability_p50 | 0.81176 |
| probability_p90 | 0.908362 |
| mean_predictive_variance | 0.157021 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172887 |
| joint_tossup_event_log_loss | 7.66618 |
| buzz_position_mae | 0.323913 |
| buzz_position_median_absolute_error | 0.324595 |
| buzz_position_bias | -0.307305 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.289124 |
| first_buzzer_mean_reciprocal_rank | 0.511444 |
| first_buzzer_log_loss | 1.77696 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.61025 |
| tossup_scorer_player_top1_accuracy | 0.259848 |
| tossup_scorer_team_top1_accuracy | 0.36829 |
| tossup_game_winner_accuracy | 0.716216 |
| tossup_game_margin_mae | 44.6865 |
| tournament_player_ppg_spearman | 0.526374 |
| tournament_player_ppg_mae | 11.0712 |
| tournament_player_ppg_top10_overlap | 0.544828 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.571339 |
| neg_average_precision | 0.302821 |
| neg_precision | 0.460526 |
| neg_recall | 0.0323625 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0374842 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.201232 |
| no_buzz_calibration_error | 0.185323 |
| no_buzz_brier | 0.0565052 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.307305 | -0.3244 |
| Q1 (0-.2) | 167 | 0.192086 | 0.182351 |
| Q2 (.2-.4) | 912 | 0.0298977 | 0.0261205 |
| Q3 (.4-.6) | 2115 | -0.150355 | -0.152452 |
| Q4 (.6-.8) | 2844 | -0.329437 | -0.329551 |
| Q5 (.8-1) | 3055 | -0.523321 | -0.522324 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0671239 | 0.18385 | 0.571339 | 0.560563 |
| tossup_correctness | tier | fall | 2842 | 0.0582053 | 0.169802 | 0.580032 | 0.526419 |
| tossup_correctness | tier | nationals | 1564 | 0.0846354 | 0.206573 | 0.575879 | 0.604713 |
| tossup_correctness | tier | regionals | 1937 | 0.0702341 | 0.185742 | 0.556801 | 0.565834 |
| tossup_correctness | tier | winter | 2750 | 0.0713913 | 0.184114 | 0.557652 | 0.567028 |
| tossup_correctness | category | Current Events | 126 | 0.129426 | 0.189203 | 0.533594 | 0.568023 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0670289 | 0.180758 | 0.584984 | 0.553328 |
| tossup_correctness | category | Geography | 185 | 0.152596 | 0.227198 | 0.549695 | 0.663586 |
| tossup_correctness | category | History | 1440 | 0.066399 | 0.187382 | 0.5722 | 0.568096 |
| tossup_correctness | category | Literature | 1422 | 0.0661149 | 0.156449 | 0.557292 | 0.499178 |
| tossup_correctness | category | Mythology | 318 | 0.0460815 | 0.166729 | 0.588155 | 0.517022 |
| tossup_correctness | category | Other Academic | 66 | 0.189411 | 0.223548 | 0.511758 | 0.650252 |
| tossup_correctness | category | Philosophy | 311 | 0.0657088 | 0.189918 | 0.593682 | 0.57703 |
| tossup_correctness | category | Popular Culture | 102 | 0.089581 | 0.119173 | 0.55 | 0.400096 |
| tossup_correctness | category | Religion | 358 | 0.10277 | 0.214116 | 0.565125 | 0.63414 |
| tossup_correctness | category | Science | 1433 | 0.0821981 | 0.195735 | 0.582437 | 0.585743 |
| tossup_correctness | category | Social Science | 324 | 0.0863533 | 0.19775 | 0.579126 | 0.593691 |
| tossup_correctness | category | Unknown | 1937 | 0.0702341 | 0.185742 | 0.556801 | 0.565834 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0635457 | 0.202354 | 0.597339 | 0.596022 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0584045 | 0.197276 | 0.585285 | 0.585363 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0826849 | 0.191625 | 0.540743 | 0.577212 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0613889 | 0.172885 | 0.575227 | 0.53274 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0716136 | 0.183657 | 0.576574 | 0.565597 |
