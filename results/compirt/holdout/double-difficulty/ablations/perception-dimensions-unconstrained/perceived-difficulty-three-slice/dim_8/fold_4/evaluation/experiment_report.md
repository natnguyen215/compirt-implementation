# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.650916 |
| log_loss | 0.5093 |
| ece | 0.0157944 |
| brier | 0.165543 |
| accuracy | 0.777562 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00420712 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.110804 |
| probability_p10 | 0.624638 |
| probability_p50 | 0.797572 |
| probability_p90 | 0.902563 |
| mean_predictive_variance | 0.160474 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100673 |
| joint_tossup_event_log_loss | 6.91582 |
| buzz_position_mae | 0.159306 |
| buzz_position_median_absolute_error | 0.146579 |
| buzz_position_bias | -0.0643775 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.363862 |
| first_buzzer_mean_reciprocal_rank | 0.57372 |
| first_buzzer_log_loss | 1.66256 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.647465 |
| tossup_scorer_player_top1_accuracy | 0.32516 |
| tossup_scorer_team_top1_accuracy | 0.504478 |
| tossup_game_winner_accuracy | 0.792123 |
| tossup_game_margin_mae | 33.6691 |
| tournament_player_ppg_spearman | 0.700249 |
| tournament_player_ppg_mae | 9.00812 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.650916 |
| neg_average_precision | 0.366247 |
| neg_precision | 0.604278 |
| neg_recall | 0.0537839 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0555759 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0963187 |
| no_buzz_calibration_error | 0.0845916 |
| no_buzz_brier | 0.0268987 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9270 | -0.0643775 | -0.0826124 |
| Q1 (0-.2) | 179 | 0.358539 | 0.357904 |
| Q2 (.2-.4) | 957 | 0.203767 | 0.202842 |
| Q3 (.4-.6) | 2203 | 0.0530901 | 0.0576441 |
| Q4 (.6-.8) | 2978 | -0.0875848 | -0.0841403 |
| Q5 (.8-1) | 2953 | -0.241142 | -0.238959 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0157944 | 0.165543 | 0.650916 | 0.5093 |
| tossup_correctness | tier | fall | 2876 | 0.0246613 | 0.157669 | 0.633813 | 0.49187 |
| tossup_correctness | tier | nationals | 1579 | 0.0486903 | 0.188384 | 0.643172 | 0.561544 |
| tossup_correctness | tier | regionals | 1990 | 0.013282 | 0.166309 | 0.669262 | 0.50961 |
| tossup_correctness | tier | winter | 2825 | 0.0250576 | 0.160252 | 0.658831 | 0.497625 |
| tossup_correctness | category | Current Events | 123 | 0.071068 | 0.169573 | 0.658474 | 0.520031 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0265408 | 0.16801 | 0.65244 | 0.513352 |
| tossup_correctness | category | Geography | 191 | 0.0635309 | 0.180158 | 0.747304 | 0.539372 |
| tossup_correctness | category | History | 1469 | 0.0191972 | 0.171161 | 0.671224 | 0.52084 |
| tossup_correctness | category | Literature | 1436 | 0.0362539 | 0.150723 | 0.590945 | 0.479559 |
| tossup_correctness | category | Mythology | 325 | 0.0973332 | 0.13999 | 0.618506 | 0.451143 |
| tossup_correctness | category | Other Academic | 67 | 0.114853 | 0.173067 | 0.613208 | 0.528038 |
| tossup_correctness | category | Philosophy | 322 | 0.0520665 | 0.167061 | 0.6048 | 0.513326 |
| tossup_correctness | category | Popular Culture | 100 | 0.120151 | 0.120903 | 0.559755 | 0.406246 |
| tossup_correctness | category | Religion | 365 | 0.0519861 | 0.193784 | 0.64709 | 0.573254 |
| tossup_correctness | category | Science | 1456 | 0.0221199 | 0.167432 | 0.650024 | 0.514889 |
| tossup_correctness | category | Social Science | 333 | 0.0208676 | 0.178255 | 0.689026 | 0.53579 |
| tossup_correctness | category | Unknown | 1990 | 0.013282 | 0.166309 | 0.669262 | 0.50961 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.094457 | 0.184831 | 0.590547 | 0.557157 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.044386 | 0.180559 | 0.613072 | 0.545042 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0134224 | 0.17042 | 0.637158 | 0.520987 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0160203 | 0.156057 | 0.664344 | 0.485675 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0258838 | 0.165434 | 0.662866 | 0.509922 |
