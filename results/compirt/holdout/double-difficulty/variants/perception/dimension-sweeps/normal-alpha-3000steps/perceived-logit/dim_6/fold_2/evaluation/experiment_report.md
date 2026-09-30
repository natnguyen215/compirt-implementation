# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.555778 |
| log_loss | 0.58019 |
| ece | 0.0869791 |
| brier | 0.186925 |
| accuracy | 0.76245 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00172842 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.116051 |
| probability_p10 | 0.638431 |
| probability_p50 | 0.854652 |
| probability_p90 | 0.934493 |
| mean_predictive_variance | 0.135235 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.17324 |
| joint_tossup_event_log_loss | 7.69638 |
| buzz_position_mae | 0.3303 |
| buzz_position_median_absolute_error | 0.329493 |
| buzz_position_bias | -0.315723 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.335638 |
| first_buzzer_mean_reciprocal_rank | 0.550548 |
| first_buzzer_log_loss | 1.68844 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.635951 |
| tossup_scorer_player_top1_accuracy | 0.267377 |
| tossup_scorer_team_top1_accuracy | 0.392537 |
| tossup_game_winner_accuracy | 0.673913 |
| tossup_game_margin_mae | 47.6668 |
| tournament_player_ppg_spearman | 0.572456 |
| tournament_player_ppg_mae | 10.5361 |
| tournament_player_ppg_top10_overlap | 0.568966 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.555778 |
| neg_average_precision | 0.289112 |
| neg_precision | 0.435484 |
| neg_recall | 0.0247366 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.033202 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.219273 |
| no_buzz_calibration_error | 0.206159 |
| no_buzz_brier | 0.0635449 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9257 | -0.315723 | -0.329492 |
| Q1 (0-.2) | 183 | 0.190537 | 0.181783 |
| Q2 (.2-.4) | 955 | 0.0122022 | 0.0109278 |
| Q3 (.4-.6) | 2239 | -0.167435 | -0.171345 |
| Q4 (.6-.8) | 2875 | -0.340628 | -0.340375 |
| Q5 (.8-1) | 3005 | -0.537431 | -0.539068 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0869791 | 0.186925 | 0.555778 | 0.58019 |
| tossup_correctness | tier | fall | 2798 | 0.0726992 | 0.174397 | 0.546668 | 0.549366 |
| tossup_correctness | tier | nationals | 1545 | 0.0746548 | 0.204582 | 0.577718 | 0.606822 |
| tossup_correctness | tier | regionals | 2039 | 0.0931348 | 0.188793 | 0.537184 | 0.586116 |
| tossup_correctness | tier | winter | 2875 | 0.104175 | 0.188303 | 0.55065 | 0.591674 |
| tossup_correctness | category | Current Events | 129 | 0.167941 | 0.245835 | 0.540562 | 0.719736 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0921135 | 0.181527 | 0.56294 | 0.567407 |
| tossup_correctness | category | Geography | 180 | 0.220201 | 0.278736 | 0.606737 | 0.79859 |
| tossup_correctness | category | History | 1454 | 0.0953668 | 0.191573 | 0.54878 | 0.589582 |
| tossup_correctness | category | Literature | 1435 | 0.0745934 | 0.157757 | 0.539433 | 0.514218 |
| tossup_correctness | category | Mythology | 324 | 0.0904623 | 0.170795 | 0.554562 | 0.54007 |
| tossup_correctness | category | Other Academic | 71 | 0.238509 | 0.237798 | 0.297386 | 0.733841 |
| tossup_correctness | category | Philosophy | 310 | 0.117509 | 0.196301 | 0.530463 | 0.61607 |
| tossup_correctness | category | Popular Culture | 108 | 0.0724391 | 0.102891 | 0.595486 | 0.357455 |
| tossup_correctness | category | Religion | 361 | 0.114646 | 0.201321 | 0.570896 | 0.61651 |
| tossup_correctness | category | Science | 1445 | 0.0782079 | 0.19243 | 0.584777 | 0.586049 |
| tossup_correctness | category | Social Science | 327 | 0.125618 | 0.210135 | 0.5895 | 0.637659 |
| tossup_correctness | category | Unknown | 2039 | 0.0931348 | 0.188793 | 0.537184 | 0.586116 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.105745 | 0.207208 | 0.483573 | 0.627478 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0924153 | 0.208643 | 0.53116 | 0.62436 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0826291 | 0.192866 | 0.545873 | 0.591141 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0830913 | 0.172642 | 0.558691 | 0.543812 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0933565 | 0.188025 | 0.565096 | 0.589917 |
