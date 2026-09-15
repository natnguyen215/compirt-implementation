# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.556231 |
| log_loss | 0.605389 |
| ece | 0.10073 |
| brier | 0.191975 |
| accuracy | 0.760585 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00153965 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.100519 |
| probability_p10 | 0.706637 |
| probability_p50 | 0.885456 |
| probability_p90 | 0.948361 |
| mean_predictive_variance | 0.114501 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.17535 |
| joint_tossup_event_log_loss | 7.75042 |
| buzz_position_mae | 0.343933 |
| buzz_position_median_absolute_error | 0.350895 |
| buzz_position_bias | -0.331951 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.358188 |
| first_buzzer_mean_reciprocal_rank | 0.569498 |
| first_buzzer_log_loss | 1.65903 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.624546 |
| tossup_scorer_player_top1_accuracy | 0.272944 |
| tossup_scorer_team_top1_accuracy | 0.394481 |
| tossup_game_winner_accuracy | 0.711712 |
| tossup_game_margin_mae | 43.0516 |
| tournament_player_ppg_spearman | 0.585007 |
| tournament_player_ppg_mae | 10.3058 |
| tournament_player_ppg_top10_overlap | 0.596552 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.556231 |
| neg_average_precision | 0.282643 |
| neg_precision | 0.36 |
| neg_recall | 0.00832178 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.029436 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.236224 |
| no_buzz_calibration_error | 0.220315 |
| no_buzz_brier | 0.0727984 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.331951 | -0.350895 |
| Q1 (0-.2) | 167 | 0.168788 | 0.164849 |
| Q2 (.2-.4) | 912 | 0.00696811 | 0.00340699 |
| Q3 (.4-.6) | 2115 | -0.171021 | -0.174326 |
| Q4 (.6-.8) | 2844 | -0.352448 | -0.355872 |
| Q5 (.8-1) | 3055 | -0.552832 | -0.555224 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.10073 | 0.191975 | 0.556231 | 0.605389 |
| tossup_correctness | tier | fall | 2842 | 0.0827507 | 0.175318 | 0.55759 | 0.554165 |
| tossup_correctness | tier | nationals | 1564 | 0.10346 | 0.214608 | 0.562724 | 0.648769 |
| tossup_correctness | tier | regionals | 1937 | 0.104109 | 0.195709 | 0.541004 | 0.621406 |
| tossup_correctness | tier | winter | 2750 | 0.117653 | 0.193686 | 0.544885 | 0.622374 |
| tossup_correctness | category | Current Events | 126 | 0.109264 | 0.191578 | 0.507999 | 0.598138 |
| tossup_correctness | category | Fine Arts | 1071 | 0.111959 | 0.190604 | 0.572146 | 0.600683 |
| tossup_correctness | category | Geography | 185 | 0.175277 | 0.243569 | 0.522702 | 0.751685 |
| tossup_correctness | category | History | 1440 | 0.103967 | 0.197893 | 0.545351 | 0.616686 |
| tossup_correctness | category | Literature | 1422 | 0.064423 | 0.156975 | 0.533203 | 0.518516 |
| tossup_correctness | category | Mythology | 318 | 0.0937044 | 0.170654 | 0.600642 | 0.541768 |
| tossup_correctness | category | Other Academic | 66 | 0.21743 | 0.245524 | 0.455767 | 0.76328 |
| tossup_correctness | category | Philosophy | 311 | 0.137486 | 0.201252 | 0.600338 | 0.639271 |
| tossup_correctness | category | Popular Culture | 102 | 0.0295907 | 0.107015 | 0.609259 | 0.368986 |
| tossup_correctness | category | Religion | 358 | 0.160067 | 0.229025 | 0.582105 | 0.701546 |
| tossup_correctness | category | Science | 1433 | 0.105342 | 0.202883 | 0.563624 | 0.626631 |
| tossup_correctness | category | Social Science | 324 | 0.140955 | 0.210853 | 0.588341 | 0.64754 |
| tossup_correctness | category | Unknown | 1937 | 0.104109 | 0.195709 | 0.541004 | 0.621406 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.138018 | 0.223465 | 0.52451 | 0.672553 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.10613 | 0.210435 | 0.545079 | 0.64027 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0994035 | 0.196364 | 0.540691 | 0.609578 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0907109 | 0.178907 | 0.560804 | 0.567792 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.113078 | 0.193868 | 0.559189 | 0.623406 |
