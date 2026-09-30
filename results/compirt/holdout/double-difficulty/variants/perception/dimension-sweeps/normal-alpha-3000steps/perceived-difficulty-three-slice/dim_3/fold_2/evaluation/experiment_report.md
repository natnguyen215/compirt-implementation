# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.642424 |
| log_loss | 0.526071 |
| ece | 0.0348814 |
| brier | 0.172193 |
| accuracy | 0.76299 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00118829 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.130481 |
| probability_p10 | 0.577156 |
| probability_p50 | 0.786604 |
| probability_p90 | 0.905972 |
| mean_predictive_variance | 0.165049 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102429 |
| joint_tossup_event_log_loss | 6.89836 |
| buzz_position_mae | 0.159907 |
| buzz_position_median_absolute_error | 0.143293 |
| buzz_position_bias | -0.0655287 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.356163 |
| first_buzzer_mean_reciprocal_rank | 0.567239 |
| first_buzzer_log_loss | 1.66271 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.660257 |
| tossup_scorer_player_top1_accuracy | 0.317484 |
| tossup_scorer_team_top1_accuracy | 0.488486 |
| tossup_game_winner_accuracy | 0.78913 |
| tossup_game_margin_mae | 36.5438 |
| tournament_player_ppg_spearman | 0.697696 |
| tournament_player_ppg_mae | 8.74165 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.642424 |
| neg_average_precision | 0.364892 |
| neg_precision | 0.487059 |
| neg_recall | 0.0948236 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0568121 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0919313 |
| no_buzz_calibration_error | 0.0788183 |
| no_buzz_brier | 0.0249724 |
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
| overall | 9257 | -0.0655287 | -0.0801031 |
| Q1 (0-.2) | 183 | 0.37511 | 0.379633 |
| Q2 (.2-.4) | 955 | 0.204518 | 0.207286 |
| Q3 (.4-.6) | 2239 | 0.0508273 | 0.0506659 |
| Q4 (.6-.8) | 2875 | -0.0872022 | -0.0826772 |
| Q5 (.8-1) | 3005 | -0.244145 | -0.243935 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0348814 | 0.172193 | 0.642424 | 0.526071 |
| tossup_correctness | tier | fall | 2798 | 0.0368295 | 0.163418 | 0.624331 | 0.508263 |
| tossup_correctness | tier | nationals | 1545 | 0.0499096 | 0.187687 | 0.679859 | 0.556465 |
| tossup_correctness | tier | regionals | 2039 | 0.0503153 | 0.17827 | 0.607828 | 0.543434 |
| tossup_correctness | tier | winter | 2875 | 0.0255259 | 0.168097 | 0.654104 | 0.514753 |
| tossup_correctness | category | Current Events | 129 | 0.0691786 | 0.211003 | 0.630882 | 0.610904 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0585005 | 0.172588 | 0.61303 | 0.527541 |
| tossup_correctness | category | Geography | 180 | 0.0802482 | 0.21013 | 0.708317 | 0.611357 |
| tossup_correctness | category | History | 1454 | 0.0376303 | 0.173688 | 0.658542 | 0.526553 |
| tossup_correctness | category | Literature | 1435 | 0.034272 | 0.148272 | 0.628808 | 0.474803 |
| tossup_correctness | category | Mythology | 324 | 0.050314 | 0.161408 | 0.639584 | 0.498116 |
| tossup_correctness | category | Other Academic | 71 | 0.1241 | 0.206601 | 0.41939 | 0.606082 |
| tossup_correctness | category | Philosophy | 310 | 0.0335233 | 0.17015 | 0.677451 | 0.515188 |
| tossup_correctness | category | Popular Culture | 108 | 0.16194 | 0.132386 | 0.577257 | 0.434209 |
| tossup_correctness | category | Religion | 361 | 0.0468376 | 0.186306 | 0.622452 | 0.559104 |
| tossup_correctness | category | Science | 1445 | 0.0265644 | 0.176091 | 0.666698 | 0.532118 |
| tossup_correctness | category | Social Science | 327 | 0.0519825 | 0.180636 | 0.695513 | 0.543192 |
| tossup_correctness | category | Unknown | 2039 | 0.0503153 | 0.17827 | 0.607828 | 0.543434 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0951091 | 0.192825 | 0.608886 | 0.574724 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0453452 | 0.191203 | 0.625444 | 0.569699 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0255068 | 0.175775 | 0.654558 | 0.531196 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0362039 | 0.160217 | 0.646159 | 0.49682 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0375402 | 0.173685 | 0.63387 | 0.533409 |
