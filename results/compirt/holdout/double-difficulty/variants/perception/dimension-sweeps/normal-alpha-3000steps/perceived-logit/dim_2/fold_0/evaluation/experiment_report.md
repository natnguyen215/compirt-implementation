# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.553929 |
| log_loss | 0.620572 |
| ece | 0.116765 |
| brier | 0.193381 |
| accuracy | 0.764174 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00107585 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.083096 |
| probability_p10 | 0.772515 |
| probability_p50 | 0.901224 |
| probability_p90 | 0.955759 |
| mean_predictive_variance | 0.0994755 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172352 |
| joint_tossup_event_log_loss | 7.80613 |
| buzz_position_mae | 0.338135 |
| buzz_position_median_absolute_error | 0.341464 |
| buzz_position_bias | -0.325195 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.329424 |
| first_buzzer_mean_reciprocal_rank | 0.550561 |
| first_buzzer_log_loss | 1.691 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.615492 |
| tossup_scorer_player_top1_accuracy | 0.264119 |
| tossup_scorer_team_top1_accuracy | 0.401486 |
| tossup_game_winner_accuracy | 0.742291 |
| tossup_game_margin_mae | 42.2208 |
| tournament_player_ppg_spearman | 0.615632 |
| tournament_player_ppg_mae | 9.84308 |
| tournament_player_ppg_top10_overlap | 0.610345 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.553929 |
| neg_average_precision | 0.276963 |
| neg_precision | 0.291667 |
| neg_recall | 0.00320807 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0286675 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.238267 |
| no_buzz_calibration_error | 0.224998 |
| no_buzz_brier | 0.0733907 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9295 | -0.325195 | -0.341421 |
| Q1 (0-.2) | 197 | 0.170469 | 0.168022 |
| Q2 (.2-.4) | 985 | 0.00304376 | -0.00173712 |
| Q3 (.4-.6) | 2251 | -0.17264 | -0.174898 |
| Q4 (.6-.8) | 2866 | -0.354615 | -0.353513 |
| Q5 (.8-1) | 2996 | -0.552181 | -0.555853 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.116765 | 0.193381 | 0.553929 | 0.620572 |
| tossup_correctness | tier | fall | 2933 | 0.0833377 | 0.169923 | 0.578978 | 0.542473 |
| tossup_correctness | tier | nationals | 1584 | 0.147933 | 0.220415 | 0.566973 | 0.700887 |
| tossup_correctness | tier | regionals | 1886 | 0.140827 | 0.211772 | 0.517986 | 0.677855 |
| tossup_correctness | tier | winter | 2892 | 0.124584 | 0.19037 | 0.554276 | 0.618432 |
| tossup_correctness | category | Current Events | 124 | 0.111454 | 0.200563 | 0.502948 | 0.638153 |
| tossup_correctness | category | Fine Arts | 1103 | 0.136321 | 0.202847 | 0.519242 | 0.664884 |
| tossup_correctness | category | Geography | 197 | 0.218228 | 0.256142 | 0.667949 | 0.765693 |
| tossup_correctness | category | History | 1491 | 0.09284 | 0.175223 | 0.569555 | 0.560819 |
| tossup_correctness | category | Literature | 1472 | 0.0916778 | 0.166867 | 0.528517 | 0.555438 |
| tossup_correctness | category | Mythology | 332 | 0.100277 | 0.15661 | 0.625448 | 0.504336 |
| tossup_correctness | category | Other Academic | 69 | 0.193822 | 0.202916 | 0.419683 | 0.673244 |
| tossup_correctness | category | Philosophy | 324 | 0.0936339 | 0.16469 | 0.590971 | 0.534127 |
| tossup_correctness | category | Popular Culture | 102 | 0.108747 | 0.15321 | 0.393772 | 0.52365 |
| tossup_correctness | category | Religion | 372 | 0.169955 | 0.22545 | 0.643764 | 0.691221 |
| tossup_correctness | category | Science | 1487 | 0.121599 | 0.19612 | 0.588768 | 0.618205 |
| tossup_correctness | category | Social Science | 336 | 0.188528 | 0.242963 | 0.546102 | 0.761577 |
| tossup_correctness | category | Unknown | 1886 | 0.140827 | 0.211772 | 0.517986 | 0.677855 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.117009 | 0.20804 | 0.536605 | 0.637532 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.124757 | 0.211056 | 0.522047 | 0.662447 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.105244 | 0.18615 | 0.585664 | 0.586352 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.106321 | 0.180135 | 0.558909 | 0.580356 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.140353 | 0.20471 | 0.541669 | 0.669872 |
