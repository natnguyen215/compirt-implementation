# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.656053 |
| log_loss | 0.52294 |
| ece | 0.0268204 |
| brier | 0.170601 |
| accuracy | 0.764654 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00252942 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.130847 |
| probability_p10 | 0.575987 |
| probability_p50 | 0.784894 |
| probability_p90 | 0.910285 |
| mean_predictive_variance | 0.164265 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100138 |
| joint_tossup_event_log_loss | 6.88489 |
| buzz_position_mae | 0.160255 |
| buzz_position_median_absolute_error | 0.145667 |
| buzz_position_bias | -0.0679996 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.344661 |
| first_buzzer_mean_reciprocal_rank | 0.557887 |
| first_buzzer_log_loss | 1.68853 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.640273 |
| tossup_scorer_player_top1_accuracy | 0.318615 |
| tossup_scorer_team_top1_accuracy | 0.491017 |
| tossup_game_winner_accuracy | 0.772523 |
| tossup_game_margin_mae | 33.9018 |
| tournament_player_ppg_spearman | 0.677856 |
| tournament_player_ppg_mae | 8.79414 |
| tournament_player_ppg_top10_overlap | 0.651724 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.656053 |
| neg_average_precision | 0.387387 |
| neg_precision | 0.528536 |
| neg_recall | 0.0984743 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0567792 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0942014 |
| no_buzz_calibration_error | 0.0782923 |
| no_buzz_brier | 0.0276599 |
| full_pmf_max_mass_error | 1.55431e-15 |
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
| overall | 9093 | -0.0679996 | -0.0859795 |
| Q1 (0-.2) | 167 | 0.362147 | 0.378324 |
| Q2 (.2-.4) | 912 | 0.206272 | 0.20889 |
| Q3 (.4-.6) | 2115 | 0.0524411 | 0.0533225 |
| Q4 (.6-.8) | 2844 | -0.0854106 | -0.0823265 |
| Q5 (.8-1) | 3055 | -0.240564 | -0.239972 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0268204 | 0.170601 | 0.656053 | 0.52294 |
| tossup_correctness | tier | fall | 2842 | 0.0103145 | 0.155109 | 0.685566 | 0.482249 |
| tossup_correctness | tier | nationals | 1564 | 0.0496961 | 0.190636 | 0.659365 | 0.568324 |
| tossup_correctness | tier | regionals | 1937 | 0.0384398 | 0.176235 | 0.627524 | 0.536116 |
| tossup_correctness | tier | winter | 2750 | 0.0305719 | 0.171248 | 0.642013 | 0.529901 |
| tossup_correctness | category | Current Events | 126 | 0.0919123 | 0.171305 | 0.69321 | 0.522257 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0325038 | 0.167735 | 0.659245 | 0.515138 |
| tossup_correctness | category | Geography | 185 | 0.0575746 | 0.188057 | 0.694491 | 0.558628 |
| tossup_correctness | category | History | 1440 | 0.0153759 | 0.171602 | 0.675167 | 0.521376 |
| tossup_correctness | category | Literature | 1422 | 0.0491949 | 0.150076 | 0.606509 | 0.48382 |
| tossup_correctness | category | Mythology | 318 | 0.0713262 | 0.156663 | 0.689005 | 0.487991 |
| tossup_correctness | category | Other Academic | 66 | 0.0754756 | 0.195953 | 0.617021 | 0.581111 |
| tossup_correctness | category | Philosophy | 311 | 0.0594128 | 0.177487 | 0.675087 | 0.537156 |
| tossup_correctness | category | Popular Culture | 102 | 0.12791 | 0.118186 | 0.637037 | 0.400236 |
| tossup_correctness | category | Religion | 358 | 0.0359913 | 0.19229 | 0.662364 | 0.569778 |
| tossup_correctness | category | Science | 1433 | 0.0358001 | 0.178997 | 0.670374 | 0.541623 |
| tossup_correctness | category | Social Science | 324 | 0.0460108 | 0.179096 | 0.668801 | 0.541551 |
| tossup_correctness | category | Unknown | 1937 | 0.0384398 | 0.176235 | 0.627524 | 0.536116 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0684255 | 0.199675 | 0.615021 | 0.59222 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0317983 | 0.182355 | 0.673222 | 0.548845 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0135448 | 0.172373 | 0.663214 | 0.52436 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0316662 | 0.163083 | 0.649647 | 0.503857 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0352521 | 0.171274 | 0.651464 | 0.528202 |
