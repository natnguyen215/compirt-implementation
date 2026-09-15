# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.571399 |
| log_loss | 0.564869 |
| ece | 0.0691127 |
| brier | 0.184653 |
| accuracy | 0.759815 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00230947 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.118711 |
| probability_p10 | 0.611395 |
| probability_p50 | 0.827306 |
| probability_p90 | 0.917062 |
| mean_predictive_variance | 0.150249 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173053 |
| joint_tossup_event_log_loss | 7.67913 |
| buzz_position_mae | 0.327164 |
| buzz_position_median_absolute_error | 0.329406 |
| buzz_position_bias | -0.311425 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.296162 |
| first_buzzer_mean_reciprocal_rank | 0.517736 |
| first_buzzer_log_loss | 1.76077 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.613769 |
| tossup_scorer_player_top1_accuracy | 0.26158 |
| tossup_scorer_team_top1_accuracy | 0.372294 |
| tossup_game_winner_accuracy | 0.718468 |
| tossup_game_margin_mae | 44.3766 |
| tournament_player_ppg_spearman | 0.52682 |
| tournament_player_ppg_mae | 10.9859 |
| tournament_player_ppg_top10_overlap | 0.551724 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.571399 |
| neg_average_precision | 0.301125 |
| neg_precision | 0.433962 |
| neg_recall | 0.0319001 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0362029 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.207401 |
| no_buzz_calibration_error | 0.191492 |
| no_buzz_brier | 0.0590569 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9093 | -0.311425 | -0.329031 |
| Q1 (0-.2) | 167 | 0.187708 | 0.176421 |
| Q2 (.2-.4) | 912 | 0.0257559 | 0.0217527 |
| Q3 (.4-.6) | 2115 | -0.154205 | -0.15672 |
| Q4 (.6-.8) | 2844 | -0.333237 | -0.333941 |
| Q5 (.8-1) | 3055 | -0.527907 | -0.528336 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0691127 | 0.184653 | 0.571399 | 0.564869 |
| tossup_correctness | tier | fall | 2842 | 0.0608338 | 0.170537 | 0.579209 | 0.529997 |
| tossup_correctness | tier | nationals | 1564 | 0.0823505 | 0.207374 | 0.569411 | 0.6075 |
| tossup_correctness | tier | regionals | 1937 | 0.0717331 | 0.186495 | 0.555095 | 0.570322 |
| tossup_correctness | tier | winter | 2750 | 0.0808701 | 0.18502 | 0.560298 | 0.572822 |
| tossup_correctness | category | Current Events | 126 | 0.11915 | 0.191815 | 0.516886 | 0.577451 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0729269 | 0.181822 | 0.588599 | 0.55813 |
| tossup_correctness | category | Geography | 185 | 0.150461 | 0.231087 | 0.543743 | 0.677683 |
| tossup_correctness | category | History | 1440 | 0.0719309 | 0.188761 | 0.569615 | 0.573509 |
| tossup_correctness | category | Literature | 1422 | 0.0667974 | 0.156575 | 0.557149 | 0.501466 |
| tossup_correctness | category | Mythology | 318 | 0.0615656 | 0.168123 | 0.583814 | 0.522768 |
| tossup_correctness | category | Other Academic | 66 | 0.187183 | 0.228677 | 0.509518 | 0.665169 |
| tossup_correctness | category | Philosophy | 311 | 0.0762621 | 0.191296 | 0.59019 | 0.584196 |
| tossup_correctness | category | Popular Culture | 102 | 0.0651586 | 0.116915 | 0.548148 | 0.393933 |
| tossup_correctness | category | Religion | 358 | 0.112534 | 0.217029 | 0.562269 | 0.64441 |
| tossup_correctness | category | Science | 1433 | 0.0786749 | 0.195124 | 0.583325 | 0.586213 |
| tossup_correctness | category | Social Science | 324 | 0.0913497 | 0.198787 | 0.580824 | 0.598977 |
| tossup_correctness | category | Unknown | 1937 | 0.0717331 | 0.186495 | 0.555095 | 0.570322 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0744968 | 0.205182 | 0.581583 | 0.606119 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0655695 | 0.19773 | 0.587434 | 0.587581 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0816969 | 0.192257 | 0.540632 | 0.581287 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0650234 | 0.173438 | 0.576183 | 0.53578 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0754837 | 0.184802 | 0.575832 | 0.571549 |
