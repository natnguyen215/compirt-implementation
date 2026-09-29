# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.565615 |
| log_loss | 0.557447 |
| ece | 0.0673271 |
| brier | 0.182959 |
| accuracy | 0.76353 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000648158 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.117835 |
| probability_p10 | 0.594277 |
| probability_p50 | 0.79271 |
| probability_p90 | 0.900685 |
| mean_predictive_variance | 0.164349 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.171638 |
| joint_tossup_event_log_loss | 7.64678 |
| buzz_position_mae | 0.315012 |
| buzz_position_median_absolute_error | 0.309148 |
| buzz_position_bias | -0.296661 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.300745 |
| first_buzzer_mean_reciprocal_rank | 0.518061 |
| first_buzzer_log_loss | 1.76606 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.618235 |
| tossup_scorer_player_top1_accuracy | 0.256397 |
| tossup_scorer_team_top1_accuracy | 0.370789 |
| tossup_game_winner_accuracy | 0.66087 |
| tossup_game_margin_mae | 48.5849 |
| tournament_player_ppg_spearman | 0.530053 |
| tournament_player_ppg_mae | 11.1353 |
| tournament_player_ppg_top10_overlap | 0.52069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.565615 |
| neg_average_precision | 0.301046 |
| neg_precision | 0.483871 |
| neg_recall | 0.0412277 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0390051 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.19674 |
| no_buzz_calibration_error | 0.183627 |
| no_buzz_brier | 0.0535356 |
| full_pmf_max_mass_error | 1.77636e-15 |
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
| overall | 9257 | -0.296661 | -0.308544 |
| Q1 (0-.2) | 183 | 0.209464 | 0.20508 |
| Q2 (.2-.4) | 955 | 0.0310002 | 0.0285054 |
| Q3 (.4-.6) | 2239 | -0.150743 | -0.155076 |
| Q4 (.6-.8) | 2875 | -0.321643 | -0.320279 |
| Q5 (.8-1) | 3005 | -0.516437 | -0.51761 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0673271 | 0.182959 | 0.565615 | 0.557447 |
| tossup_correctness | tier | fall | 2798 | 0.0487931 | 0.170108 | 0.562449 | 0.528916 |
| tossup_correctness | tier | nationals | 1545 | 0.0778238 | 0.203201 | 0.598175 | 0.596034 |
| tossup_correctness | tier | regionals | 2039 | 0.0905914 | 0.187063 | 0.544053 | 0.567429 |
| tossup_correctness | tier | winter | 2875 | 0.064689 | 0.181677 | 0.552745 | 0.557399 |
| tossup_correctness | category | Current Events | 129 | 0.15612 | 0.232286 | 0.543267 | 0.667762 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0646818 | 0.178001 | 0.565777 | 0.545406 |
| tossup_correctness | category | Geography | 180 | 0.152022 | 0.256204 | 0.592506 | 0.720472 |
| tossup_correctness | category | History | 1454 | 0.0681394 | 0.186735 | 0.560105 | 0.566287 |
| tossup_correctness | category | Literature | 1435 | 0.0710446 | 0.158294 | 0.545964 | 0.505018 |
| tossup_correctness | category | Mythology | 324 | 0.06271 | 0.166565 | 0.564899 | 0.519178 |
| tossup_correctness | category | Other Academic | 71 | 0.241374 | 0.233658 | 0.288671 | 0.689626 |
| tossup_correctness | category | Philosophy | 310 | 0.0738638 | 0.186144 | 0.566823 | 0.565429 |
| tossup_correctness | category | Popular Culture | 108 | 0.105362 | 0.108672 | 0.632812 | 0.376782 |
| tossup_correctness | category | Religion | 361 | 0.0608664 | 0.191386 | 0.580043 | 0.575857 |
| tossup_correctness | category | Science | 1445 | 0.047744 | 0.187735 | 0.600706 | 0.564856 |
| tossup_correctness | category | Social Science | 327 | 0.078121 | 0.201667 | 0.581869 | 0.600533 |
| tossup_correctness | category | Unknown | 2039 | 0.0905914 | 0.187063 | 0.544053 | 0.567429 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0920347 | 0.202633 | 0.500469 | 0.600057 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0624379 | 0.20308 | 0.542543 | 0.59985 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0666213 | 0.188079 | 0.560285 | 0.567187 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.074531 | 0.171181 | 0.565587 | 0.529446 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0676105 | 0.18282 | 0.572616 | 0.56091 |
