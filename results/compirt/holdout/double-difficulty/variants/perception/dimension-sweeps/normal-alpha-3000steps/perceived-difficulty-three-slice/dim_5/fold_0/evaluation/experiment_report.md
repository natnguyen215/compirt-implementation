# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.668694 |
| log_loss | 0.512167 |
| ece | 0.00936119 |
| brier | 0.167292 |
| accuracy | 0.769016 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00376547 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.122659 |
| probability_p10 | 0.590897 |
| probability_p50 | 0.785591 |
| probability_p90 | 0.900958 |
| mean_predictive_variance | 0.165548 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102136 |
| joint_tossup_event_log_loss | 6.88698 |
| buzz_position_mae | 0.161865 |
| buzz_position_median_absolute_error | 0.148575 |
| buzz_position_bias | -0.0667709 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.363421 |
| first_buzzer_mean_reciprocal_rank | 0.573108 |
| first_buzzer_log_loss | 1.66011 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.649597 |
| tossup_scorer_player_top1_accuracy | 0.328344 |
| tossup_scorer_team_top1_accuracy | 0.491614 |
| tossup_game_winner_accuracy | 0.803965 |
| tossup_game_margin_mae | 34.2422 |
| tournament_player_ppg_spearman | 0.692889 |
| tournament_player_ppg_mae | 8.91262 |
| tournament_player_ppg_top10_overlap | 0.655172 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.668694 |
| neg_average_precision | 0.387987 |
| neg_precision | 0.55132 |
| neg_recall | 0.0861595 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0551915 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0924397 |
| no_buzz_calibration_error | 0.07917 |
| no_buzz_brier | 0.026009 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| overall | 9295 | -0.0667709 | -0.0848367 |
| Q1 (0-.2) | 197 | 0.355498 | 0.355747 |
| Q2 (.2-.4) | 985 | 0.200026 | 0.194507 |
| Q3 (.4-.6) | 2251 | 0.0484919 | 0.049512 |
| Q4 (.6-.8) | 2866 | -0.0928443 | -0.0873116 |
| Q5 (.8-1) | 2996 | -0.243911 | -0.240758 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.00936119 | 0.167292 | 0.668694 | 0.512167 |
| tossup_correctness | tier | fall | 2933 | 0.0191555 | 0.154578 | 0.665752 | 0.48246 |
| tossup_correctness | tier | nationals | 1584 | 0.0474742 | 0.1879 | 0.665265 | 0.559177 |
| tossup_correctness | tier | regionals | 1886 | 0.0209145 | 0.179019 | 0.652169 | 0.538715 |
| tossup_correctness | tier | winter | 2892 | 0.0263911 | 0.161252 | 0.681835 | 0.499235 |
| tossup_correctness | category | Current Events | 124 | 0.0804361 | 0.169147 | 0.70274 | 0.518656 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0273325 | 0.174544 | 0.640145 | 0.531694 |
| tossup_correctness | category | Geography | 197 | 0.0531298 | 0.189764 | 0.737646 | 0.559198 |
| tossup_correctness | category | History | 1491 | 0.0477892 | 0.154132 | 0.705491 | 0.479662 |
| tossup_correctness | category | Literature | 1472 | 0.0240663 | 0.150331 | 0.639291 | 0.476255 |
| tossup_correctness | category | Mythology | 332 | 0.0620543 | 0.147678 | 0.677121 | 0.463629 |
| tossup_correctness | category | Other Academic | 69 | 0.102173 | 0.191178 | 0.536199 | 0.571039 |
| tossup_correctness | category | Philosophy | 324 | 0.0325454 | 0.14879 | 0.684526 | 0.46874 |
| tossup_correctness | category | Popular Culture | 102 | 0.1093 | 0.160341 | 0.413149 | 0.507599 |
| tossup_correctness | category | Religion | 372 | 0.0508129 | 0.19098 | 0.679994 | 0.56191 |
| tossup_correctness | category | Science | 1487 | 0.0310768 | 0.170615 | 0.686368 | 0.51974 |
| tossup_correctness | category | Social Science | 336 | 0.0467262 | 0.190003 | 0.692373 | 0.56121 |
| tossup_correctness | category | Unknown | 1886 | 0.0209145 | 0.179019 | 0.652169 | 0.538715 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0749513 | 0.186467 | 0.640451 | 0.561526 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0254048 | 0.181695 | 0.655691 | 0.54777 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0185906 | 0.163534 | 0.679919 | 0.503346 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0145339 | 0.158707 | 0.66823 | 0.490973 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0258349 | 0.172333 | 0.670701 | 0.52412 |
