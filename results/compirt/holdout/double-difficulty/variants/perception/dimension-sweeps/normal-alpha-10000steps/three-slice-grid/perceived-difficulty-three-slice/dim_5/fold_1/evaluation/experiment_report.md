# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.660993 |
| log_loss | 0.521095 |
| ece | 0.0243588 |
| brier | 0.169868 |
| accuracy | 0.769493 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00736831 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.131215 |
| probability_p10 | 0.568785 |
| probability_p50 | 0.777911 |
| probability_p90 | 0.905257 |
| mean_predictive_variance | 0.167145 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100994 |
| joint_tossup_event_log_loss | 6.88409 |
| buzz_position_mae | 0.161706 |
| buzz_position_median_absolute_error | 0.148941 |
| buzz_position_bias | -0.0706284 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.336083 |
| first_buzzer_mean_reciprocal_rank | 0.552232 |
| first_buzzer_log_loss | 1.69588 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.639283 |
| tossup_scorer_player_top1_accuracy | 0.320563 |
| tossup_scorer_team_top1_accuracy | 0.49632 |
| tossup_game_winner_accuracy | 0.772523 |
| tossup_game_margin_mae | 34.6393 |
| tournament_player_ppg_spearman | 0.665417 |
| tournament_player_ppg_mae | 9.06091 |
| tournament_player_ppg_top10_overlap | 0.658621 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.660993 |
| neg_average_precision | 0.393437 |
| neg_precision | 0.578824 |
| neg_recall | 0.113731 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0559355 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0908255 |
| no_buzz_calibration_error | 0.0749164 |
| no_buzz_brier | 0.0265576 |
| full_pmf_max_mass_error | 1.55431e-15 |
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
| overall | 9093 | -0.0706284 | -0.0889598 |
| Q1 (0-.2) | 167 | 0.36303 | 0.378785 |
| Q2 (.2-.4) | 912 | 0.206457 | 0.210211 |
| Q3 (.4-.6) | 2115 | 0.0509722 | 0.0526024 |
| Q4 (.6-.8) | 2844 | -0.0876698 | -0.0856937 |
| Q5 (.8-1) | 3055 | -0.245372 | -0.245586 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0243588 | 0.169868 | 0.660993 | 0.521095 |
| tossup_correctness | tier | fall | 2842 | 0.0145304 | 0.154781 | 0.686361 | 0.48099 |
| tossup_correctness | tier | nationals | 1564 | 0.0312644 | 0.188201 | 0.665391 | 0.564173 |
| tossup_correctness | tier | regionals | 1937 | 0.0353697 | 0.177142 | 0.629314 | 0.536966 |
| tossup_correctness | tier | winter | 2750 | 0.0286635 | 0.169911 | 0.649232 | 0.526863 |
| tossup_correctness | category | Current Events | 126 | 0.102551 | 0.166859 | 0.713473 | 0.516056 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0262634 | 0.16656 | 0.670899 | 0.511094 |
| tossup_correctness | category | Geography | 185 | 0.0563856 | 0.177775 | 0.742248 | 0.533673 |
| tossup_correctness | category | History | 1440 | 0.0139521 | 0.170707 | 0.677532 | 0.519079 |
| tossup_correctness | category | Literature | 1422 | 0.0485498 | 0.1507 | 0.59927 | 0.490748 |
| tossup_correctness | category | Mythology | 318 | 0.0496259 | 0.152815 | 0.711839 | 0.476484 |
| tossup_correctness | category | Other Academic | 66 | 0.0760738 | 0.185981 | 0.675252 | 0.555038 |
| tossup_correctness | category | Philosophy | 311 | 0.0534098 | 0.175717 | 0.684199 | 0.530293 |
| tossup_correctness | category | Popular Culture | 102 | 0.137096 | 0.124358 | 0.622222 | 0.415623 |
| tossup_correctness | category | Religion | 358 | 0.0480872 | 0.189418 | 0.678508 | 0.563945 |
| tossup_correctness | category | Science | 1433 | 0.0204995 | 0.178615 | 0.672348 | 0.538432 |
| tossup_correctness | category | Social Science | 324 | 0.0298179 | 0.176256 | 0.68951 | 0.533422 |
| tossup_correctness | category | Unknown | 1937 | 0.0353697 | 0.177142 | 0.629314 | 0.536966 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0699811 | 0.199953 | 0.605917 | 0.59049 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0408008 | 0.180743 | 0.677788 | 0.545774 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0206309 | 0.171603 | 0.669699 | 0.521935 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0264095 | 0.163003 | 0.654552 | 0.50314 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0263288 | 0.170167 | 0.657385 | 0.526068 |
