# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.65295 |
| log_loss | 0.52189 |
| ece | 0.0222048 |
| brier | 0.170308 |
| accuracy | 0.769383 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00725833 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.120875 |
| probability_p10 | 0.597695 |
| probability_p50 | 0.789959 |
| probability_p90 | 0.901726 |
| mean_predictive_variance | 0.164292 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0998406 |
| joint_tossup_event_log_loss | 6.87099 |
| buzz_position_mae | 0.16018 |
| buzz_position_median_absolute_error | 0.146339 |
| buzz_position_bias | -0.0692885 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.354448 |
| first_buzzer_mean_reciprocal_rank | 0.565071 |
| first_buzzer_log_loss | 1.67374 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.644452 |
| tossup_scorer_player_top1_accuracy | 0.325974 |
| tossup_scorer_team_top1_accuracy | 0.49329 |
| tossup_game_winner_accuracy | 0.788288 |
| tossup_game_margin_mae | 33.7837 |
| tournament_player_ppg_spearman | 0.677534 |
| tournament_player_ppg_mae | 8.83747 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.65295 |
| neg_average_precision | 0.390778 |
| neg_precision | 0.611486 |
| neg_recall | 0.0836801 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0562744 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0971194 |
| no_buzz_calibration_error | 0.0812103 |
| no_buzz_brier | 0.0285926 |
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
| overall | 9093 | -0.0692885 | -0.0883224 |
| Q1 (0-.2) | 167 | 0.360964 | 0.372352 |
| Q2 (.2-.4) | 912 | 0.204377 | 0.209563 |
| Q3 (.4-.6) | 2115 | 0.0507342 | 0.0522484 |
| Q4 (.6-.8) | 2844 | -0.0866088 | -0.0852255 |
| Q5 (.8-1) | 3055 | -0.241473 | -0.240802 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0222048 | 0.170308 | 0.65295 | 0.52189 |
| tossup_correctness | tier | fall | 2842 | 0.0196601 | 0.153973 | 0.692475 | 0.478815 |
| tossup_correctness | tier | nationals | 1564 | 0.0542471 | 0.191282 | 0.657873 | 0.569289 |
| tossup_correctness | tier | regionals | 1937 | 0.0373688 | 0.177578 | 0.61103 | 0.540386 |
| tossup_correctness | tier | winter | 2750 | 0.0435018 | 0.17014 | 0.645851 | 0.526422 |
| tossup_correctness | category | Current Events | 126 | 0.0932697 | 0.170386 | 0.702808 | 0.521559 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0270233 | 0.164653 | 0.674792 | 0.506999 |
| tossup_correctness | category | Geography | 185 | 0.0528238 | 0.173576 | 0.7482 | 0.525159 |
| tossup_correctness | category | History | 1440 | 0.0207225 | 0.171894 | 0.670829 | 0.522489 |
| tossup_correctness | category | Literature | 1422 | 0.0447553 | 0.150126 | 0.606276 | 0.479931 |
| tossup_correctness | category | Mythology | 318 | 0.0544125 | 0.152364 | 0.69739 | 0.478353 |
| tossup_correctness | category | Other Academic | 66 | 0.150919 | 0.205052 | 0.572228 | 0.602846 |
| tossup_correctness | category | Philosophy | 311 | 0.0669947 | 0.176255 | 0.684144 | 0.530268 |
| tossup_correctness | category | Popular Culture | 102 | 0.112328 | 0.115527 | 0.634259 | 0.393161 |
| tossup_correctness | category | Religion | 358 | 0.0601328 | 0.195381 | 0.650181 | 0.576853 |
| tossup_correctness | category | Science | 1433 | 0.0429732 | 0.179036 | 0.673573 | 0.542537 |
| tossup_correctness | category | Social Science | 324 | 0.0790668 | 0.18093 | 0.657597 | 0.546978 |
| tossup_correctness | category | Unknown | 1937 | 0.0373688 | 0.177578 | 0.61103 | 0.540386 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0567127 | 0.199648 | 0.594888 | 0.589427 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0327491 | 0.181299 | 0.67587 | 0.546448 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.025145 | 0.171566 | 0.663425 | 0.522691 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0234926 | 0.163554 | 0.63853 | 0.506677 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0273543 | 0.170839 | 0.652613 | 0.524476 |
