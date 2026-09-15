# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.568205 |
| log_loss | 0.554027 |
| ece | 0.0656381 |
| brier | 0.18155 |
| accuracy | 0.764605 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000645508 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.114662 |
| probability_p10 | 0.602518 |
| probability_p50 | 0.795664 |
| probability_p90 | 0.899935 |
| mean_predictive_variance | 0.163548 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.1687 |
| joint_tossup_event_log_loss | 7.63834 |
| buzz_position_mae | 0.313113 |
| buzz_position_median_absolute_error | 0.308967 |
| buzz_position_bias | -0.294549 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.292738 |
| first_buzzer_mean_reciprocal_rank | 0.516006 |
| first_buzzer_log_loss | 1.766 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.609252 |
| tossup_scorer_player_top1_accuracy | 0.25828 |
| tossup_scorer_team_top1_accuracy | 0.361783 |
| tossup_game_winner_accuracy | 0.707048 |
| tossup_game_margin_mae | 44.0409 |
| tournament_player_ppg_spearman | 0.529234 |
| tournament_player_ppg_mae | 11.1095 |
| tournament_player_ppg_top10_overlap | 0.548276 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.568205 |
| neg_average_precision | 0.304063 |
| neg_precision | 0.48125 |
| neg_recall | 0.0352887 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0387824 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.200363 |
| no_buzz_calibration_error | 0.187093 |
| no_buzz_brier | 0.05524 |
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
| overall | 9295 | -0.294549 | -0.30779 |
| Q1 (0-.2) | 197 | 0.200667 | 0.189913 |
| Q2 (.2-.4) | 985 | 0.0293009 | 0.0227665 |
| Q3 (.4-.6) | 2251 | -0.148129 | -0.150341 |
| Q4 (.6-.8) | 2866 | -0.323702 | -0.323205 |
| Q5 (.8-1) | 2996 | -0.515706 | -0.514553 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0656381 | 0.18155 | 0.568205 | 0.554027 |
| tossup_correctness | tier | fall | 2933 | 0.0553099 | 0.165469 | 0.568998 | 0.516154 |
| tossup_correctness | tier | nationals | 1584 | 0.088496 | 0.201292 | 0.601333 | 0.593479 |
| tossup_correctness | tier | regionals | 1886 | 0.0746256 | 0.196295 | 0.529156 | 0.589211 |
| tossup_correctness | tier | winter | 2892 | 0.0601457 | 0.177431 | 0.557382 | 0.547884 |
| tossup_correctness | category | Current Events | 124 | 0.0960108 | 0.189304 | 0.566771 | 0.567476 |
| tossup_correctness | category | Fine Arts | 1103 | 0.103443 | 0.191039 | 0.518953 | 0.584623 |
| tossup_correctness | category | Geography | 197 | 0.111151 | 0.224685 | 0.624359 | 0.645611 |
| tossup_correctness | category | History | 1491 | 0.0627591 | 0.170685 | 0.569879 | 0.525289 |
| tossup_correctness | category | Literature | 1472 | 0.0639855 | 0.15963 | 0.567937 | 0.505434 |
| tossup_correctness | category | Mythology | 332 | 0.0621518 | 0.15669 | 0.562784 | 0.49078 |
| tossup_correctness | category | Other Academic | 69 | 0.142531 | 0.20068 | 0.487557 | 0.594176 |
| tossup_correctness | category | Philosophy | 324 | 0.0594248 | 0.15534 | 0.629878 | 0.4868 |
| tossup_correctness | category | Popular Culture | 102 | 0.122383 | 0.165385 | 0.4 | 0.517879 |
| tossup_correctness | category | Religion | 372 | 0.0866051 | 0.204436 | 0.610831 | 0.606157 |
| tossup_correctness | category | Science | 1487 | 0.0512769 | 0.179448 | 0.617773 | 0.54592 |
| tossup_correctness | category | Social Science | 336 | 0.101534 | 0.218513 | 0.541992 | 0.646072 |
| tossup_correctness | category | Unknown | 1886 | 0.0746256 | 0.196295 | 0.529156 | 0.589211 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0892197 | 0.207734 | 0.507294 | 0.608965 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0677192 | 0.195032 | 0.569812 | 0.581779 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0510448 | 0.176014 | 0.588065 | 0.536638 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0691667 | 0.171354 | 0.570452 | 0.528415 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0822893 | 0.18931 | 0.557312 | 0.578857 |
