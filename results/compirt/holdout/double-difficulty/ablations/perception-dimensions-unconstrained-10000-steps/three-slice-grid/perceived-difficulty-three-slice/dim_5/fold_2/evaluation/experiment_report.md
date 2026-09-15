# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.669172 |
| log_loss | 0.514849 |
| ece | 0.0216361 |
| brier | 0.167851 |
| accuracy | 0.768067 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00388895 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.134102 |
| probability_p10 | 0.564757 |
| probability_p50 | 0.777581 |
| probability_p90 | 0.903704 |
| mean_predictive_variance | 0.168079 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10161 |
| joint_tossup_event_log_loss | 6.88173 |
| buzz_position_mae | 0.159646 |
| buzz_position_median_absolute_error | 0.1438 |
| buzz_position_bias | -0.0644362 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349465 |
| first_buzzer_mean_reciprocal_rank | 0.561376 |
| first_buzzer_log_loss | 1.67771 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.653776 |
| tossup_scorer_player_top1_accuracy | 0.321855 |
| tossup_scorer_team_top1_accuracy | 0.501812 |
| tossup_game_winner_accuracy | 0.773913 |
| tossup_game_margin_mae | 36.7571 |
| tournament_player_ppg_spearman | 0.699729 |
| tournament_player_ppg_mae | 8.94786 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.669172 |
| neg_average_precision | 0.396782 |
| neg_precision | 0.536145 |
| neg_recall | 0.122309 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.056255 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0905395 |
| no_buzz_calibration_error | 0.0774265 |
| no_buzz_brier | 0.025101 |
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
| overall | 9257 | -0.0644362 | -0.0794138 |
| Q1 (0-.2) | 183 | 0.380751 | 0.39379 |
| Q2 (.2-.4) | 955 | 0.207608 | 0.211257 |
| Q3 (.4-.6) | 2239 | 0.0525116 | 0.0542561 |
| Q4 (.6-.8) | 2875 | -0.086937 | -0.0822056 |
| Q5 (.8-1) | 3005 | -0.243614 | -0.244389 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0216361 | 0.167851 | 0.669172 | 0.514849 |
| tossup_correctness | tier | fall | 2798 | 0.0271852 | 0.156409 | 0.679337 | 0.486919 |
| tossup_correctness | tier | nationals | 1545 | 0.050293 | 0.18463 | 0.690919 | 0.54964 |
| tossup_correctness | tier | regionals | 2039 | 0.0433312 | 0.17422 | 0.635066 | 0.533563 |
| tossup_correctness | tier | winter | 2875 | 0.0215639 | 0.165453 | 0.665799 | 0.510062 |
| tossup_correctness | category | Current Events | 129 | 0.0493459 | 0.20744 | 0.667117 | 0.601676 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0374485 | 0.167301 | 0.646838 | 0.512787 |
| tossup_correctness | category | Geography | 180 | 0.0733428 | 0.201285 | 0.729991 | 0.590431 |
| tossup_correctness | category | History | 1454 | 0.0143624 | 0.169961 | 0.673476 | 0.517436 |
| tossup_correctness | category | Literature | 1435 | 0.0303799 | 0.144849 | 0.650672 | 0.465869 |
| tossup_correctness | category | Mythology | 324 | 0.0474602 | 0.15795 | 0.654451 | 0.488934 |
| tossup_correctness | category | Other Academic | 71 | 0.128638 | 0.202069 | 0.375817 | 0.60166 |
| tossup_correctness | category | Philosophy | 310 | 0.0209232 | 0.172152 | 0.658326 | 0.520167 |
| tossup_correctness | category | Popular Culture | 108 | 0.161612 | 0.132934 | 0.557292 | 0.437054 |
| tossup_correctness | category | Religion | 361 | 0.0557068 | 0.175127 | 0.680709 | 0.529995 |
| tossup_correctness | category | Science | 1445 | 0.0253062 | 0.170193 | 0.707405 | 0.515779 |
| tossup_correctness | category | Social Science | 327 | 0.0462474 | 0.178932 | 0.712026 | 0.539157 |
| tossup_correctness | category | Unknown | 2039 | 0.0433312 | 0.17422 | 0.635066 | 0.533563 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.107344 | 0.195506 | 0.603098 | 0.57974 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0277173 | 0.181689 | 0.680546 | 0.545285 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.020057 | 0.170113 | 0.683885 | 0.517921 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0217843 | 0.156529 | 0.673778 | 0.487088 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0277104 | 0.170916 | 0.65179 | 0.525495 |
