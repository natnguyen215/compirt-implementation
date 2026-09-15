# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.628927 |
| log_loss | 0.535009 |
| ece | 0.0375559 |
| brier | 0.17515 |
| accuracy | 0.761795 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000329924 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.130255 |
| probability_p10 | 0.577445 |
| probability_p50 | 0.786784 |
| probability_p90 | 0.908607 |
| mean_predictive_variance | 0.164723 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101552 |
| joint_tossup_event_log_loss | 6.91214 |
| buzz_position_mae | 0.161291 |
| buzz_position_median_absolute_error | 0.14676 |
| buzz_position_bias | -0.0702973 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34675 |
| first_buzzer_mean_reciprocal_rank | 0.560433 |
| first_buzzer_log_loss | 1.68144 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.638403 |
| tossup_scorer_player_top1_accuracy | 0.314502 |
| tossup_scorer_team_top1_accuracy | 0.480736 |
| tossup_game_winner_accuracy | 0.765766 |
| tossup_game_margin_mae | 34.8841 |
| tournament_player_ppg_spearman | 0.680577 |
| tournament_player_ppg_mae | 8.85001 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.628927 |
| neg_average_precision | 0.358577 |
| neg_precision | 0.496144 |
| neg_recall | 0.0892279 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0571086 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0935857 |
| no_buzz_calibration_error | 0.0776766 |
| no_buzz_brier | 0.027158 |
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
| overall | 9093 | -0.0702973 | -0.0880908 |
| Q1 (0-.2) | 167 | 0.36089 | 0.369529 |
| Q2 (.2-.4) | 912 | 0.204455 | 0.206655 |
| Q3 (.4-.6) | 2115 | 0.051633 | 0.0525346 |
| Q4 (.6-.8) | 2844 | -0.0880801 | -0.0853328 |
| Q5 (.8-1) | 3055 | -0.243748 | -0.241244 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0375559 | 0.17515 | 0.628927 | 0.535009 |
| tossup_correctness | tier | fall | 2842 | 0.0326472 | 0.165444 | 0.615281 | 0.51274 |
| tossup_correctness | tier | nationals | 1564 | 0.0550385 | 0.193029 | 0.652195 | 0.574015 |
| tossup_correctness | tier | regionals | 1937 | 0.0392192 | 0.17842 | 0.616467 | 0.542323 |
| tossup_correctness | tier | winter | 2750 | 0.0364721 | 0.172711 | 0.629688 | 0.530688 |
| tossup_correctness | category | Current Events | 126 | 0.0633589 | 0.182917 | 0.564522 | 0.550128 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0452657 | 0.172507 | 0.629544 | 0.527445 |
| tossup_correctness | category | Geography | 185 | 0.052568 | 0.191875 | 0.683278 | 0.564679 |
| tossup_correctness | category | History | 1440 | 0.0270466 | 0.17442 | 0.656031 | 0.529443 |
| tossup_correctness | category | Literature | 1422 | 0.0654651 | 0.156197 | 0.564054 | 0.498996 |
| tossup_correctness | category | Mythology | 318 | 0.0792059 | 0.160318 | 0.669025 | 0.499054 |
| tossup_correctness | category | Other Academic | 66 | 0.101694 | 0.188074 | 0.678611 | 0.558408 |
| tossup_correctness | category | Philosophy | 311 | 0.0481809 | 0.181341 | 0.64426 | 0.546324 |
| tossup_correctness | category | Popular Culture | 102 | 0.182944 | 0.146124 | 0.614815 | 0.46246 |
| tossup_correctness | category | Religion | 358 | 0.0506627 | 0.195317 | 0.65098 | 0.577552 |
| tossup_correctness | category | Science | 1433 | 0.0536367 | 0.185896 | 0.645953 | 0.561633 |
| tossup_correctness | category | Social Science | 324 | 0.0829217 | 0.183515 | 0.636549 | 0.553999 |
| tossup_correctness | category | Unknown | 1937 | 0.0392192 | 0.17842 | 0.616467 | 0.542323 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0482817 | 0.206027 | 0.588761 | 0.602424 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0461867 | 0.192245 | 0.620566 | 0.573114 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0298766 | 0.177354 | 0.63146 | 0.537929 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0440936 | 0.168007 | 0.616659 | 0.517865 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0377297 | 0.173483 | 0.638453 | 0.533887 |
