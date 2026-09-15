# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.561115 |
| log_loss | 0.570362 |
| ece | 0.0778738 |
| brier | 0.184989 |
| accuracy | 0.762774 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00140434 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.118826 |
| probability_p10 | 0.620994 |
| probability_p50 | 0.838856 |
| probability_p90 | 0.92549 |
| mean_predictive_variance | 0.144013 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173125 |
| joint_tossup_event_log_loss | 7.68121 |
| buzz_position_mae | 0.326084 |
| buzz_position_median_absolute_error | 0.322581 |
| buzz_position_bias | -0.310488 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.326672 |
| first_buzzer_mean_reciprocal_rank | 0.542113 |
| first_buzzer_log_loss | 1.71378 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.629578 |
| tossup_scorer_player_top1_accuracy | 0.262793 |
| tossup_scorer_team_top1_accuracy | 0.385928 |
| tossup_game_winner_accuracy | 0.667391 |
| tossup_game_margin_mae | 48.0008 |
| tournament_player_ppg_spearman | 0.553893 |
| tournament_player_ppg_mae | 10.7211 |
| tournament_player_ppg_top10_overlap | 0.562069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.561115 |
| neg_average_precision | 0.296509 |
| neg_precision | 0.458065 |
| neg_recall | 0.032524 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0349013 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.211755 |
| no_buzz_calibration_error | 0.198642 |
| no_buzz_brier | 0.0600318 |
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
| overall | 9257 | -0.310488 | -0.322157 |
| Q1 (0-.2) | 183 | 0.196187 | 0.192194 |
| Q2 (.2-.4) | 955 | 0.0173544 | 0.0142691 |
| Q3 (.4-.6) | 2239 | -0.163087 | -0.166646 |
| Q4 (.6-.8) | 2875 | -0.335364 | -0.335908 |
| Q5 (.8-1) | 3005 | -0.531562 | -0.532948 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0778738 | 0.184989 | 0.561115 | 0.570362 |
| tossup_correctness | tier | fall | 2798 | 0.0598538 | 0.172366 | 0.558218 | 0.540097 |
| tossup_correctness | tier | nationals | 1545 | 0.0722512 | 0.202705 | 0.588713 | 0.598713 |
| tossup_correctness | tier | regionals | 2039 | 0.0932547 | 0.187713 | 0.540196 | 0.578359 |
| tossup_correctness | tier | winter | 2875 | 0.0905072 | 0.185823 | 0.550797 | 0.57891 |
| tossup_correctness | category | Current Events | 129 | 0.120299 | 0.240891 | 0.525149 | 0.699902 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0797544 | 0.17952 | 0.567736 | 0.557006 |
| tossup_correctness | category | Geography | 180 | 0.200953 | 0.270834 | 0.610654 | 0.769216 |
| tossup_correctness | category | History | 1454 | 0.0849511 | 0.189632 | 0.554405 | 0.580379 |
| tossup_correctness | category | Literature | 1435 | 0.071889 | 0.157465 | 0.541993 | 0.510085 |
| tossup_correctness | category | Mythology | 324 | 0.100353 | 0.169912 | 0.5516 | 0.534566 |
| tossup_correctness | category | Other Academic | 71 | 0.221519 | 0.237272 | 0.285403 | 0.722027 |
| tossup_correctness | category | Philosophy | 310 | 0.101735 | 0.193003 | 0.54243 | 0.597798 |
| tossup_correctness | category | Popular Culture | 108 | 0.077344 | 0.102123 | 0.632812 | 0.355988 |
| tossup_correctness | category | Religion | 361 | 0.096396 | 0.196986 | 0.572821 | 0.59968 |
| tossup_correctness | category | Science | 1445 | 0.0663247 | 0.189599 | 0.600721 | 0.574206 |
| tossup_correctness | category | Social Science | 327 | 0.104057 | 0.206553 | 0.586078 | 0.621767 |
| tossup_correctness | category | Unknown | 2039 | 0.0932547 | 0.187713 | 0.540196 | 0.578359 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.081666 | 0.20638 | 0.473717 | 0.620679 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0865155 | 0.205524 | 0.545112 | 0.61102 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0733901 | 0.190612 | 0.551336 | 0.580828 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0773726 | 0.171506 | 0.562171 | 0.536959 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0834453 | 0.185871 | 0.568967 | 0.578537 |
