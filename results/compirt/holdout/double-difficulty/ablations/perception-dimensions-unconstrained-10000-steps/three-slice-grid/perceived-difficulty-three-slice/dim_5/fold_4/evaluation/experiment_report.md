# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.668406 |
| log_loss | 0.504451 |
| ece | 0.0281993 |
| brier | 0.163332 |
| accuracy | 0.777994 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00463862 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.130272 |
| probability_p10 | 0.579438 |
| probability_p50 | 0.777938 |
| probability_p90 | 0.907635 |
| mean_predictive_variance | 0.167047 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100427 |
| joint_tossup_event_log_loss | 6.88307 |
| buzz_position_mae | 0.159432 |
| buzz_position_median_absolute_error | 0.147624 |
| buzz_position_bias | -0.0634688 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.352859 |
| first_buzzer_mean_reciprocal_rank | 0.561911 |
| first_buzzer_log_loss | 1.6887 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.638296 |
| tossup_scorer_player_top1_accuracy | 0.316205 |
| tossup_scorer_team_top1_accuracy | 0.502878 |
| tossup_game_winner_accuracy | 0.805252 |
| tossup_game_margin_mae | 34.8366 |
| tournament_player_ppg_spearman | 0.695679 |
| tournament_player_ppg_mae | 9.15292 |
| tournament_player_ppg_top10_overlap | 0.672414 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.668406 |
| neg_average_precision | 0.392671 |
| neg_precision | 0.549884 |
| neg_recall | 0.112803 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0551391 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0875559 |
| no_buzz_calibration_error | 0.0758288 |
| no_buzz_brier | 0.0235634 |
| full_pmf_max_mass_error | 1.22125e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0634688 | -0.0814993 |
| Q1 (0-.2) | 179 | 0.362476 | 0.362192 |
| Q2 (.2-.4) | 957 | 0.209077 | 0.205345 |
| Q3 (.4-.6) | 2203 | 0.0566298 | 0.0582474 |
| Q4 (.6-.8) | 2978 | -0.0868039 | -0.083434 |
| Q5 (.8-1) | 2953 | -0.243677 | -0.243048 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0281993 | 0.163332 | 0.668406 | 0.504451 |
| tossup_correctness | tier | fall | 2876 | 0.0266698 | 0.155098 | 0.656055 | 0.484395 |
| tossup_correctness | tier | nationals | 1579 | 0.0352272 | 0.181256 | 0.681117 | 0.544221 |
| tossup_correctness | tier | regionals | 1990 | 0.0444828 | 0.165103 | 0.690772 | 0.506943 |
| tossup_correctness | tier | winter | 2825 | 0.0299337 | 0.160448 | 0.654754 | 0.500886 |
| tossup_correctness | category | Current Events | 123 | 0.0982867 | 0.163971 | 0.73661 | 0.506383 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0267796 | 0.16448 | 0.667978 | 0.507362 |
| tossup_correctness | category | Geography | 191 | 0.0750472 | 0.173704 | 0.764766 | 0.525401 |
| tossup_correctness | category | History | 1469 | 0.0192277 | 0.167712 | 0.689648 | 0.511002 |
| tossup_correctness | category | Literature | 1436 | 0.0530856 | 0.150552 | 0.612423 | 0.483224 |
| tossup_correctness | category | Mythology | 325 | 0.095187 | 0.139053 | 0.643409 | 0.447746 |
| tossup_correctness | category | Other Academic | 67 | 0.120401 | 0.172178 | 0.641509 | 0.526015 |
| tossup_correctness | category | Philosophy | 322 | 0.0488153 | 0.166757 | 0.605316 | 0.513911 |
| tossup_correctness | category | Popular Culture | 100 | 0.157712 | 0.128114 | 0.526047 | 0.427427 |
| tossup_correctness | category | Religion | 365 | 0.0448649 | 0.191437 | 0.656466 | 0.565231 |
| tossup_correctness | category | Science | 1456 | 0.0273274 | 0.163258 | 0.677275 | 0.503153 |
| tossup_correctness | category | Social Science | 333 | 0.0309482 | 0.177273 | 0.693919 | 0.533967 |
| tossup_correctness | category | Unknown | 1990 | 0.0444828 | 0.165103 | 0.690772 | 0.506943 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0940347 | 0.181845 | 0.643449 | 0.548591 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0615617 | 0.181823 | 0.625308 | 0.547812 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0318452 | 0.168205 | 0.657157 | 0.515155 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0295912 | 0.152436 | 0.691304 | 0.476281 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.025165 | 0.16357 | 0.670141 | 0.508147 |
