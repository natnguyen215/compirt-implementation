# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.555738 |
| log_loss | 0.614696 |
| ece | 0.108909 |
| brier | 0.193351 |
| accuracy | 0.761795 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000329924 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0921284 |
| probability_p10 | 0.738315 |
| probability_p50 | 0.892556 |
| probability_p90 | 0.952563 |
| mean_predictive_variance | 0.107422 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.176047 |
| joint_tossup_event_log_loss | 7.76951 |
| buzz_position_mae | 0.346246 |
| buzz_position_median_absolute_error | 0.352239 |
| buzz_position_bias | -0.334432 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.352689 |
| first_buzzer_mean_reciprocal_rank | 0.568866 |
| first_buzzer_log_loss | 1.6551 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.614979 |
| tossup_scorer_player_top1_accuracy | 0.274892 |
| tossup_scorer_team_top1_accuracy | 0.397727 |
| tossup_game_winner_accuracy | 0.718468 |
| tossup_game_margin_mae | 42.1881 |
| tournament_player_ppg_spearman | 0.589903 |
| tournament_player_ppg_mae | 10.2679 |
| tournament_player_ppg_top10_overlap | 0.589655 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.555738 |
| neg_average_precision | 0.283191 |
| neg_precision | 0.451613 |
| neg_recall | 0.00647249 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0285263 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.238169 |
| no_buzz_calibration_error | 0.22226 |
| no_buzz_brier | 0.0741156 |
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
| overall | 9093 | -0.334432 | -0.352239 |
| Q1 (0-.2) | 167 | 0.168691 | 0.167131 |
| Q2 (.2-.4) | 912 | 0.00495417 | 0.00176549 |
| Q3 (.4-.6) | 2115 | -0.173667 | -0.177778 |
| Q4 (.6-.8) | 2844 | -0.355479 | -0.356346 |
| Q5 (.8-1) | 3055 | -0.554955 | -0.557506 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.108909 | 0.193351 | 0.555738 | 0.614696 |
| tossup_correctness | tier | fall | 2842 | 0.0885179 | 0.175266 | 0.57055 | 0.55491 |
| tossup_correctness | tier | nationals | 1564 | 0.125659 | 0.217996 | 0.571007 | 0.673158 |
| tossup_correctness | tier | regionals | 1937 | 0.117961 | 0.198542 | 0.529545 | 0.637408 |
| tossup_correctness | tier | winter | 2750 | 0.120773 | 0.194367 | 0.544686 | 0.627235 |
| tossup_correctness | category | Current Events | 126 | 0.114749 | 0.190245 | 0.532172 | 0.596932 |
| tossup_correctness | category | Fine Arts | 1071 | 0.120687 | 0.191807 | 0.572404 | 0.608844 |
| tossup_correctness | category | Geography | 185 | 0.171777 | 0.235064 | 0.565476 | 0.719182 |
| tossup_correctness | category | History | 1440 | 0.110732 | 0.199108 | 0.542956 | 0.626566 |
| tossup_correctness | category | Literature | 1422 | 0.0683067 | 0.156665 | 0.540659 | 0.519397 |
| tossup_correctness | category | Mythology | 318 | 0.0960777 | 0.170498 | 0.597491 | 0.54751 |
| tossup_correctness | category | Other Academic | 66 | 0.194743 | 0.241759 | 0.473684 | 0.770763 |
| tossup_correctness | category | Philosophy | 311 | 0.141778 | 0.202509 | 0.607213 | 0.642213 |
| tossup_correctness | category | Popular Culture | 102 | 0.056291 | 0.109784 | 0.57963 | 0.375764 |
| tossup_correctness | category | Religion | 358 | 0.170668 | 0.231156 | 0.590939 | 0.71145 |
| tossup_correctness | category | Science | 1433 | 0.119842 | 0.20625 | 0.567289 | 0.644234 |
| tossup_correctness | category | Social Science | 324 | 0.142776 | 0.211489 | 0.592415 | 0.656415 |
| tossup_correctness | category | Unknown | 1937 | 0.117961 | 0.198542 | 0.529545 | 0.637408 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.130484 | 0.224162 | 0.511029 | 0.689438 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.117887 | 0.211363 | 0.557371 | 0.645023 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.109963 | 0.198066 | 0.539056 | 0.618984 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0959977 | 0.180038 | 0.559899 | 0.574571 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.124934 | 0.195418 | 0.55582 | 0.635941 |
