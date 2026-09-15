# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.631074 |
| log_loss | 0.587524 |
| ece | 0.152068 |
| brier | 0.200253 |
| accuracy | 0.700875 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0633034 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.152637 |
| probability_p10 | 0.406273 |
| probability_p50 | 0.624714 |
| probability_p90 | 0.808475 |
| mean_predictive_variance | 0.213596 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100904 |
| joint_tossup_event_log_loss | 6.65293 |
| buzz_position_mae | 0.162382 |
| buzz_position_median_absolute_error | 0.14259 |
| buzz_position_bias | -0.075904 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.397753 |
| first_buzzer_mean_reciprocal_rank | 0.601491 |
| first_buzzer_log_loss | 1.58033 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.664146 |
| tossup_scorer_player_top1_accuracy | 0.283262 |
| tossup_scorer_team_top1_accuracy | 0.379851 |
| tossup_game_winner_accuracy | 0.771739 |
| tossup_game_margin_mae | 41.9729 |
| tournament_player_ppg_spearman | 0.661128 |
| tournament_player_ppg_mae | 11.3293 |
| tournament_player_ppg_top10_overlap | 0.644828 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.631074 |
| neg_average_precision | 0.343913 |
| neg_precision | 0.3641 |
| neg_recall | 0.359597 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.102344 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0815758 |
| no_buzz_calibration_error | 0.0684628 |
| no_buzz_brier | 0.0261735 |
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
| overall | 9257 | -0.075904 | -0.0878452 |
| Q1 (0-.2) | 183 | 0.346805 | 0.347881 |
| Q2 (.2-.4) | 955 | 0.18444 | 0.180577 |
| Q3 (.4-.6) | 2239 | 0.0333052 | 0.0301741 |
| Q4 (.6-.8) | 2875 | -0.0968357 | -0.0971535 |
| Q5 (.8-1) | 3005 | -0.24573 | -0.242294 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.152068 | 0.200253 | 0.631074 | 0.587524 |
| tossup_correctness | tier | fall | 2798 | 0.13557 | 0.183784 | 0.635254 | 0.55111 |
| tossup_correctness | tier | nationals | 1545 | 0.153177 | 0.219614 | 0.621093 | 0.629473 |
| tossup_correctness | tier | regionals | 2039 | 0.15325 | 0.203113 | 0.620059 | 0.593702 |
| tossup_correctness | tier | winter | 2875 | 0.16669 | 0.203847 | 0.629517 | 0.596039 |
| tossup_correctness | category | Current Events | 129 | 0.112146 | 0.227505 | 0.586263 | 0.646488 |
| tossup_correctness | category | Fine Arts | 1074 | 0.191827 | 0.209888 | 0.620843 | 0.609175 |
| tossup_correctness | category | Geography | 180 | 0.0751083 | 0.238267 | 0.582583 | 0.66758 |
| tossup_correctness | category | History | 1454 | 0.131477 | 0.193009 | 0.649109 | 0.573076 |
| tossup_correctness | category | Literature | 1435 | 0.176176 | 0.193091 | 0.588321 | 0.571539 |
| tossup_correctness | category | Mythology | 324 | 0.204658 | 0.206834 | 0.611243 | 0.59978 |
| tossup_correctness | category | Other Academic | 71 | 0.213939 | 0.236493 | 0.54902 | 0.665019 |
| tossup_correctness | category | Philosophy | 310 | 0.184518 | 0.205257 | 0.65678 | 0.596448 |
| tossup_correctness | category | Popular Culture | 108 | 0.296012 | 0.19324 | 0.618056 | 0.571746 |
| tossup_correctness | category | Religion | 361 | 0.165745 | 0.208911 | 0.66121 | 0.609731 |
| tossup_correctness | category | Science | 1445 | 0.111211 | 0.189547 | 0.673088 | 0.562766 |
| tossup_correctness | category | Social Science | 327 | 0.138881 | 0.203658 | 0.662072 | 0.597624 |
| tossup_correctness | category | Unknown | 2039 | 0.15325 | 0.203113 | 0.620059 | 0.593702 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.323489 | 0.280729 | 0.690394 | 0.764598 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.24397 | 0.250373 | 0.631907 | 0.69626 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.189791 | 0.212911 | 0.658866 | 0.614894 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.158817 | 0.190205 | 0.631683 | 0.564579 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0800233 | 0.179605 | 0.631778 | 0.543744 |
