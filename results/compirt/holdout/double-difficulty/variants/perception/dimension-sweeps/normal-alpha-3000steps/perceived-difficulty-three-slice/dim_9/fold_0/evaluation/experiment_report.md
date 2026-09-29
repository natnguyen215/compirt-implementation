# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.655081 |
| log_loss | 0.518465 |
| ece | 0.0135007 |
| brier | 0.169422 |
| accuracy | 0.767617 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00236686 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.108062 |
| probability_p10 | 0.624101 |
| probability_p50 | 0.792668 |
| probability_p90 | 0.897485 |
| mean_predictive_variance | 0.16315 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.107531 |
| joint_tossup_event_log_loss | 7.07953 |
| buzz_position_mae | 0.168614 |
| buzz_position_median_absolute_error | 0.153892 |
| buzz_position_bias | -0.0765872 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.343303 |
| first_buzzer_mean_reciprocal_rank | 0.560361 |
| first_buzzer_log_loss | 1.71416 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.63475 |
| tossup_scorer_player_top1_accuracy | 0.315711 |
| tossup_scorer_team_top1_accuracy | 0.487367 |
| tossup_game_winner_accuracy | 0.781938 |
| tossup_game_margin_mae | 36.4518 |
| tournament_player_ppg_spearman | 0.660382 |
| tournament_player_ppg_mae | 9.51574 |
| tournament_player_ppg_top10_overlap | 0.641379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.655081 |
| neg_average_precision | 0.371071 |
| neg_precision | 0.571429 |
| neg_recall | 0.04033 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0535644 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0910824 |
| no_buzz_calibration_error | 0.0778127 |
| no_buzz_brier | 0.0261121 |
| full_pmf_max_mass_error | 1.55431e-15 |
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
| overall | 9295 | -0.0765872 | -0.0919366 |
| Q1 (0-.2) | 197 | 0.351714 | 0.361861 |
| Q2 (.2-.4) | 985 | 0.192914 | 0.191821 |
| Q3 (.4-.6) | 2251 | 0.0385356 | 0.0459692 |
| Q4 (.6-.8) | 2866 | -0.10353 | -0.0941869 |
| Q5 (.8-1) | 2996 | -0.254076 | -0.250172 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0135007 | 0.169422 | 0.655081 | 0.518465 |
| tossup_correctness | tier | fall | 2933 | 0.0148063 | 0.15592 | 0.654674 | 0.48634 |
| tossup_correctness | tier | nationals | 1584 | 0.0349062 | 0.189602 | 0.644032 | 0.563171 |
| tossup_correctness | tier | regionals | 1886 | 0.0363435 | 0.181746 | 0.633823 | 0.54755 |
| tossup_correctness | tier | winter | 2892 | 0.036091 | 0.164026 | 0.670954 | 0.50759 |
| tossup_correctness | category | Current Events | 124 | 0.0776783 | 0.169692 | 0.694069 | 0.519759 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0354539 | 0.176783 | 0.626266 | 0.539382 |
| tossup_correctness | category | Geography | 197 | 0.0606348 | 0.194618 | 0.729021 | 0.569038 |
| tossup_correctness | category | History | 1491 | 0.0297543 | 0.156098 | 0.682565 | 0.485169 |
| tossup_correctness | category | Literature | 1472 | 0.0238136 | 0.152298 | 0.6281 | 0.483175 |
| tossup_correctness | category | Mythology | 332 | 0.0494423 | 0.14499 | 0.692593 | 0.457191 |
| tossup_correctness | category | Other Academic | 69 | 0.108361 | 0.201589 | 0.440045 | 0.59808 |
| tossup_correctness | category | Philosophy | 324 | 0.0312531 | 0.149226 | 0.666647 | 0.471858 |
| tossup_correctness | category | Popular Culture | 102 | 0.090928 | 0.160596 | 0.416609 | 0.510389 |
| tossup_correctness | category | Religion | 372 | 0.0442332 | 0.193116 | 0.667438 | 0.568582 |
| tossup_correctness | category | Science | 1487 | 0.0185906 | 0.172712 | 0.669304 | 0.523922 |
| tossup_correctness | category | Social Science | 336 | 0.0591077 | 0.19425 | 0.687627 | 0.570708 |
| tossup_correctness | category | Unknown | 1886 | 0.0363435 | 0.181746 | 0.633823 | 0.54755 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0748583 | 0.191842 | 0.607427 | 0.574401 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0169861 | 0.184218 | 0.640529 | 0.553236 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0224514 | 0.166175 | 0.662223 | 0.510335 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.00570391 | 0.160078 | 0.659527 | 0.49549 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.037317 | 0.174462 | 0.659163 | 0.53144 |
