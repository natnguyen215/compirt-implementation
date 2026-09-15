# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.649895 |
| log_loss | 0.523926 |
| ece | 0.0207402 |
| brier | 0.171035 |
| accuracy | 0.767513 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00538876 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.120583 |
| probability_p10 | 0.601576 |
| probability_p50 | 0.792496 |
| probability_p90 | 0.907259 |
| mean_predictive_variance | 0.162421 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100087 |
| joint_tossup_event_log_loss | 6.86462 |
| buzz_position_mae | 0.160045 |
| buzz_position_median_absolute_error | 0.145933 |
| buzz_position_bias | -0.068749 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.361157 |
| first_buzzer_mean_reciprocal_rank | 0.571563 |
| first_buzzer_log_loss | 1.65395 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.641372 |
| tossup_scorer_player_top1_accuracy | 0.329221 |
| tossup_scorer_team_top1_accuracy | 0.495779 |
| tossup_game_winner_accuracy | 0.759009 |
| tossup_game_margin_mae | 34.0762 |
| tournament_player_ppg_spearman | 0.679536 |
| tournament_player_ppg_mae | 8.81131 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.649895 |
| neg_average_precision | 0.383428 |
| neg_precision | 0.589744 |
| neg_recall | 0.0744337 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.056742 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0964695 |
| no_buzz_calibration_error | 0.0805604 |
| no_buzz_brier | 0.0284135 |
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
| overall | 9093 | -0.068749 | -0.0880424 |
| Q1 (0-.2) | 167 | 0.360467 | 0.370944 |
| Q2 (.2-.4) | 912 | 0.202802 | 0.205447 |
| Q3 (.4-.6) | 2115 | 0.052115 | 0.0527492 |
| Q4 (.6-.8) | 2844 | -0.0860826 | -0.0842809 |
| Q5 (.8-1) | 3055 | -0.240816 | -0.239637 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0207402 | 0.171035 | 0.649895 | 0.523926 |
| tossup_correctness | tier | fall | 2842 | 0.0226634 | 0.157365 | 0.670373 | 0.489516 |
| tossup_correctness | tier | nationals | 1564 | 0.0491084 | 0.190862 | 0.661049 | 0.568081 |
| tossup_correctness | tier | regionals | 1937 | 0.0217693 | 0.176407 | 0.619418 | 0.536489 |
| tossup_correctness | tier | winter | 2750 | 0.0341866 | 0.170103 | 0.64554 | 0.525525 |
| tossup_correctness | category | Current Events | 126 | 0.0649617 | 0.172394 | 0.65695 | 0.523458 |
| tossup_correctness | category | Fine Arts | 1071 | 0.042347 | 0.167693 | 0.655596 | 0.515192 |
| tossup_correctness | category | Geography | 185 | 0.0411896 | 0.182993 | 0.711656 | 0.547217 |
| tossup_correctness | category | History | 1440 | 0.0141723 | 0.170903 | 0.67587 | 0.520393 |
| tossup_correctness | category | Literature | 1422 | 0.0559433 | 0.151507 | 0.594193 | 0.484408 |
| tossup_correctness | category | Mythology | 318 | 0.0561031 | 0.155554 | 0.694952 | 0.48697 |
| tossup_correctness | category | Other Academic | 66 | 0.041056 | 0.201432 | 0.590146 | 0.593076 |
| tossup_correctness | category | Philosophy | 311 | 0.0521488 | 0.176873 | 0.682344 | 0.53306 |
| tossup_correctness | category | Popular Culture | 102 | 0.117296 | 0.114283 | 0.627778 | 0.390307 |
| tossup_correctness | category | Religion | 358 | 0.0434803 | 0.191541 | 0.672911 | 0.567323 |
| tossup_correctness | category | Science | 1433 | 0.0549451 | 0.181144 | 0.670047 | 0.548688 |
| tossup_correctness | category | Social Science | 324 | 0.0627961 | 0.182804 | 0.646006 | 0.551727 |
| tossup_correctness | category | Unknown | 1937 | 0.0217693 | 0.176407 | 0.619418 | 0.536489 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0487704 | 0.193557 | 0.647234 | 0.575981 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0263851 | 0.182921 | 0.669203 | 0.549595 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0107547 | 0.172911 | 0.657814 | 0.526037 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0236236 | 0.164561 | 0.633687 | 0.508897 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0305752 | 0.170984 | 0.650505 | 0.525947 |
