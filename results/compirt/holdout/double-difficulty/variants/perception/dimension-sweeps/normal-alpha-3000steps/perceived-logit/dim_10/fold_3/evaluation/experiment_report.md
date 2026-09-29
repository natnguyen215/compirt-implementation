# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.568021 |
| log_loss | 0.548833 |
| ece | 0.0681481 |
| brier | 0.179589 |
| accuracy | 0.768172 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00187225 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.116548 |
| probability_p10 | 0.598483 |
| probability_p50 | 0.79481 |
| probability_p90 | 0.900198 |
| mean_predictive_variance | 0.163897 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172746 |
| joint_tossup_event_log_loss | 7.63746 |
| buzz_position_mae | 0.31803 |
| buzz_position_median_absolute_error | 0.314361 |
| buzz_position_bias | -0.299542 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.291189 |
| first_buzzer_mean_reciprocal_rank | 0.513458 |
| first_buzzer_log_loss | 1.77797 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.619714 |
| tossup_scorer_player_top1_accuracy | 0.249566 |
| tossup_scorer_team_top1_accuracy | 0.387093 |
| tossup_game_winner_accuracy | 0.710177 |
| tossup_game_margin_mae | 48.3597 |
| tournament_player_ppg_spearman | 0.502297 |
| tournament_player_ppg_mae | 11.4584 |
| tournament_player_ppg_top10_overlap | 0.517241 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.568021 |
| neg_average_precision | 0.295879 |
| neg_precision | 0.449102 |
| neg_recall | 0.0359195 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0380434 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.19302 |
| no_buzz_calibration_error | 0.177836 |
| no_buzz_brier | 0.0528133 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.299542 | -0.314107 |
| Q1 (0-.2) | 192 | 0.206164 | 0.199846 |
| Q2 (.2-.4) | 889 | 0.0313915 | 0.0253334 |
| Q3 (.4-.6) | 2210 | -0.149593 | -0.151147 |
| Q4 (.6-.8) | 2869 | -0.326012 | -0.326434 |
| Q5 (.8-1) | 2920 | -0.521027 | -0.518534 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0681481 | 0.179589 | 0.568021 | 0.548833 |
| tossup_correctness | tier | fall | 2817 | 0.0577762 | 0.173287 | 0.563257 | 0.534967 |
| tossup_correctness | tier | nationals | 1542 | 0.0931076 | 0.196779 | 0.626935 | 0.581444 |
| tossup_correctness | tier | regionals | 1934 | 0.080966 | 0.189391 | 0.537438 | 0.57199 |
| tossup_correctness | tier | winter | 2787 | 0.0571524 | 0.169646 | 0.551966 | 0.528736 |
| tossup_correctness | category | Current Events | 125 | 0.0946705 | 0.203157 | 0.618243 | 0.593093 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0843921 | 0.183438 | 0.546172 | 0.559446 |
| tossup_correctness | category | Geography | 185 | 0.0689306 | 0.198246 | 0.653287 | 0.585978 |
| tossup_correctness | category | History | 1443 | 0.0473267 | 0.175671 | 0.605233 | 0.537583 |
| tossup_correctness | category | Literature | 1411 | 0.0827877 | 0.160228 | 0.534973 | 0.509025 |
| tossup_correctness | category | Mythology | 320 | 0.0561944 | 0.170065 | 0.541935 | 0.52923 |
| tossup_correctness | category | Other Academic | 64 | 0.0706678 | 0.179652 | 0.645833 | 0.54307 |
| tossup_correctness | category | Philosophy | 312 | 0.128748 | 0.173737 | 0.483484 | 0.542711 |
| tossup_correctness | category | Popular Culture | 104 | 0.0776729 | 0.14548 | 0.49929 | 0.466231 |
| tossup_correctness | category | Religion | 358 | 0.0855841 | 0.200851 | 0.594859 | 0.597226 |
| tossup_correctness | category | Science | 1431 | 0.0500169 | 0.177356 | 0.608929 | 0.538367 |
| tossup_correctness | category | Social Science | 321 | 0.0997094 | 0.202923 | 0.517757 | 0.606876 |
| tossup_correctness | category | Unknown | 1934 | 0.080966 | 0.189391 | 0.537438 | 0.57199 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0662711 | 0.215905 | 0.540787 | 0.625849 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.061236 | 0.196953 | 0.572901 | 0.584106 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.066658 | 0.189224 | 0.537553 | 0.571543 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0721149 | 0.168885 | 0.567041 | 0.523986 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0730218 | 0.175139 | 0.584087 | 0.540256 |
