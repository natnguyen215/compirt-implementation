# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.665476 |
| log_loss | 0.515624 |
| ece | 0.0226483 |
| brier | 0.168011 |
| accuracy | 0.769769 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00451856 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.131818 |
| probability_p10 | 0.568857 |
| probability_p50 | 0.778818 |
| probability_p90 | 0.903608 |
| mean_predictive_variance | 0.167879 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10277 |
| joint_tossup_event_log_loss | 6.95409 |
| buzz_position_mae | 0.161718 |
| buzz_position_median_absolute_error | 0.148127 |
| buzz_position_bias | -0.065302 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.350296 |
| first_buzzer_mean_reciprocal_rank | 0.563246 |
| first_buzzer_log_loss | 1.69001 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.643249 |
| tossup_scorer_player_top1_accuracy | 0.322399 |
| tossup_scorer_team_top1_accuracy | 0.489915 |
| tossup_game_winner_accuracy | 0.786344 |
| tossup_game_margin_mae | 35.0561 |
| tournament_player_ppg_spearman | 0.677706 |
| tournament_player_ppg_mae | 9.32214 |
| tournament_player_ppg_top10_overlap | 0.631034 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.665476 |
| neg_average_precision | 0.389791 |
| neg_precision | 0.545064 |
| neg_recall | 0.116407 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.056148 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0922817 |
| no_buzz_calibration_error | 0.0790121 |
| no_buzz_brier | 0.0258079 |
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
| overall | 9295 | -0.065302 | -0.0820878 |
| Q1 (0-.2) | 197 | 0.356663 | 0.365213 |
| Q2 (.2-.4) | 985 | 0.201344 | 0.198419 |
| Q3 (.4-.6) | 2251 | 0.0505741 | 0.0506114 |
| Q4 (.6-.8) | 2866 | -0.0912013 | -0.0860184 |
| Q5 (.8-1) | 2996 | -0.243 | -0.2396 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0226483 | 0.168011 | 0.665476 | 0.515624 |
| tossup_correctness | tier | fall | 2933 | 0.0322961 | 0.156711 | 0.65791 | 0.487919 |
| tossup_correctness | tier | nationals | 1584 | 0.049977 | 0.183743 | 0.686631 | 0.549712 |
| tossup_correctness | tier | regionals | 1886 | 0.0299287 | 0.18151 | 0.639788 | 0.547234 |
| tossup_correctness | tier | winter | 2892 | 0.0200778 | 0.162049 | 0.67419 | 0.504438 |
| tossup_correctness | category | Current Events | 124 | 0.0877062 | 0.174234 | 0.681582 | 0.529371 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0321516 | 0.174766 | 0.637704 | 0.533539 |
| tossup_correctness | category | Geography | 197 | 0.0527233 | 0.18995 | 0.729953 | 0.559292 |
| tossup_correctness | category | History | 1491 | 0.0504178 | 0.154177 | 0.703215 | 0.480999 |
| tossup_correctness | category | Literature | 1472 | 0.036041 | 0.151081 | 0.63234 | 0.484583 |
| tossup_correctness | category | Mythology | 332 | 0.0706561 | 0.151307 | 0.6592 | 0.473642 |
| tossup_correctness | category | Other Academic | 69 | 0.108352 | 0.18761 | 0.579186 | 0.564621 |
| tossup_correctness | category | Philosophy | 324 | 0.0374897 | 0.150909 | 0.673418 | 0.472341 |
| tossup_correctness | category | Popular Culture | 102 | 0.135421 | 0.16397 | 0.478201 | 0.510299 |
| tossup_correctness | category | Religion | 372 | 0.0590283 | 0.191135 | 0.678521 | 0.562637 |
| tossup_correctness | category | Science | 1487 | 0.0187142 | 0.169315 | 0.690943 | 0.515273 |
| tossup_correctness | category | Social Science | 336 | 0.0552905 | 0.18928 | 0.688136 | 0.562629 |
| tossup_correctness | category | Unknown | 1886 | 0.0299287 | 0.18151 | 0.639788 | 0.547234 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0753421 | 0.19408 | 0.614854 | 0.577427 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0317635 | 0.182303 | 0.662931 | 0.54745 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0307783 | 0.164491 | 0.675707 | 0.506178 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0270226 | 0.159465 | 0.664869 | 0.494146 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0225442 | 0.172417 | 0.66423 | 0.528739 |
