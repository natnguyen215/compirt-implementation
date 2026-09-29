# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.563571 |
| log_loss | 0.591767 |
| ece | 0.090725 |
| brier | 0.189595 |
| accuracy | 0.760915 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00120972 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.108686 |
| probability_p10 | 0.671533 |
| probability_p50 | 0.875619 |
| probability_p90 | 0.942404 |
| mean_predictive_variance | 0.123435 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174931 |
| joint_tossup_event_log_loss | 7.7351 |
| buzz_position_mae | 0.340234 |
| buzz_position_median_absolute_error | 0.345077 |
| buzz_position_bias | -0.327523 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.339822 |
| first_buzzer_mean_reciprocal_rank | 0.554384 |
| first_buzzer_log_loss | 1.69205 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.620587 |
| tossup_scorer_player_top1_accuracy | 0.267316 |
| tossup_scorer_team_top1_accuracy | 0.39026 |
| tossup_game_winner_accuracy | 0.718468 |
| tossup_game_margin_mae | 42.8859 |
| tournament_player_ppg_spearman | 0.573756 |
| tournament_player_ppg_mae | 10.4568 |
| tournament_player_ppg_top10_overlap | 0.586207 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.563571 |
| neg_average_precision | 0.290313 |
| neg_precision | 0.438202 |
| neg_recall | 0.0180305 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.031128 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.227189 |
| no_buzz_calibration_error | 0.21128 |
| no_buzz_brier | 0.0679926 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| overall | 9093 | -0.327523 | -0.34506 |
| Q1 (0-.2) | 167 | 0.171836 | 0.166483 |
| Q2 (.2-.4) | 912 | 0.0106342 | 0.00716322 |
| Q3 (.4-.6) | 2115 | -0.167665 | -0.171251 |
| Q4 (.6-.8) | 2844 | -0.348233 | -0.349408 |
| Q5 (.8-1) | 3055 | -0.54716 | -0.549892 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.090725 | 0.189595 | 0.563571 | 0.591767 |
| tossup_correctness | tier | fall | 2842 | 0.0767081 | 0.173304 | 0.571401 | 0.544857 |
| tossup_correctness | tier | nationals | 1564 | 0.0877415 | 0.211367 | 0.554996 | 0.628064 |
| tossup_correctness | tier | regionals | 1937 | 0.0869307 | 0.192485 | 0.541264 | 0.604513 |
| tossup_correctness | tier | winter | 2750 | 0.111989 | 0.192014 | 0.554359 | 0.610626 |
| tossup_correctness | category | Current Events | 126 | 0.110031 | 0.195446 | 0.483825 | 0.600001 |
| tossup_correctness | category | Fine Arts | 1071 | 0.100582 | 0.186661 | 0.589554 | 0.583723 |
| tossup_correctness | category | Geography | 185 | 0.165707 | 0.238356 | 0.543189 | 0.722729 |
| tossup_correctness | category | History | 1440 | 0.103243 | 0.196162 | 0.554944 | 0.605363 |
| tossup_correctness | category | Literature | 1422 | 0.066752 | 0.156215 | 0.552163 | 0.510144 |
| tossup_correctness | category | Mythology | 318 | 0.1018 | 0.171274 | 0.590593 | 0.541541 |
| tossup_correctness | category | Other Academic | 66 | 0.214046 | 0.246386 | 0.453527 | 0.741365 |
| tossup_correctness | category | Philosophy | 311 | 0.117139 | 0.198782 | 0.593682 | 0.62136 |
| tossup_correctness | category | Popular Culture | 102 | 0.0489728 | 0.110523 | 0.584259 | 0.37579 |
| tossup_correctness | category | Religion | 358 | 0.150011 | 0.226154 | 0.581611 | 0.683053 |
| tossup_correctness | category | Science | 1433 | 0.0876095 | 0.199897 | 0.565704 | 0.612282 |
| tossup_correctness | category | Social Science | 324 | 0.11558 | 0.205751 | 0.593773 | 0.628797 |
| tossup_correctness | category | Unknown | 1937 | 0.0869307 | 0.192485 | 0.541264 | 0.604513 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.108557 | 0.218105 | 0.531688 | 0.654917 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0921679 | 0.206528 | 0.559922 | 0.622889 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0975971 | 0.195473 | 0.535367 | 0.602754 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.08093 | 0.176741 | 0.573617 | 0.555343 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0973015 | 0.190879 | 0.567615 | 0.605326 |
