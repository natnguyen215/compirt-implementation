# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.625329 |
| log_loss | 0.576157 |
| ece | 0.129312 |
| brier | 0.194522 |
| accuracy | 0.711786 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0523928 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.1593 |
| probability_p10 | 0.424702 |
| probability_p50 | 0.65732 |
| probability_p90 | 0.839401 |
| mean_predictive_variance | 0.204232 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102583 |
| joint_tossup_event_log_loss | 6.66922 |
| buzz_position_mae | 0.164633 |
| buzz_position_median_absolute_error | 0.145187 |
| buzz_position_bias | -0.0814781 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.396673 |
| first_buzzer_mean_reciprocal_rank | 0.601009 |
| first_buzzer_log_loss | 1.58547 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.667387 |
| tossup_scorer_player_top1_accuracy | 0.293923 |
| tossup_scorer_team_top1_accuracy | 0.422068 |
| tossup_game_winner_accuracy | 0.767391 |
| tossup_game_margin_mae | 41.2083 |
| tournament_player_ppg_spearman | 0.651057 |
| tournament_player_ppg_mae | 10.9573 |
| tournament_player_ppg_top10_overlap | 0.637931 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.625329 |
| neg_average_precision | 0.342377 |
| neg_precision | 0.367269 |
| neg_recall | 0.307375 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.102073 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0759525 |
| no_buzz_calibration_error | 0.0628395 |
| no_buzz_brier | 0.0249818 |
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
| overall | 9257 | -0.0814781 | -0.0938131 |
| Q1 (0-.2) | 183 | 0.342161 | 0.348044 |
| Q2 (.2-.4) | 955 | 0.178514 | 0.168446 |
| Q3 (.4-.6) | 2239 | 0.025925 | 0.0236093 |
| Q4 (.6-.8) | 2875 | -0.103465 | -0.103789 |
| Q5 (.8-1) | 3005 | -0.248892 | -0.243532 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.129312 | 0.194522 | 0.625329 | 0.576157 |
| tossup_correctness | tier | fall | 2798 | 0.107719 | 0.177745 | 0.623042 | 0.540159 |
| tossup_correctness | tier | nationals | 1545 | 0.13048 | 0.214081 | 0.622635 | 0.617588 |
| tossup_correctness | tier | regionals | 2039 | 0.133045 | 0.198402 | 0.618936 | 0.583081 |
| tossup_correctness | tier | winter | 2875 | 0.147052 | 0.197588 | 0.621166 | 0.584016 |
| tossup_correctness | category | Current Events | 129 | 0.128309 | 0.235803 | 0.5457 | 0.674413 |
| tossup_correctness | category | Fine Arts | 1074 | 0.171419 | 0.202582 | 0.609153 | 0.596478 |
| tossup_correctness | category | Geography | 180 | 0.143719 | 0.243319 | 0.559211 | 0.682608 |
| tossup_correctness | category | History | 1454 | 0.104426 | 0.187208 | 0.646745 | 0.559071 |
| tossup_correctness | category | Literature | 1435 | 0.159608 | 0.186518 | 0.583222 | 0.558731 |
| tossup_correctness | category | Mythology | 324 | 0.150561 | 0.188896 | 0.613508 | 0.560815 |
| tossup_correctness | category | Other Academic | 71 | 0.180805 | 0.232075 | 0.498911 | 0.656041 |
| tossup_correctness | category | Philosophy | 310 | 0.161903 | 0.2017 | 0.638972 | 0.596445 |
| tossup_correctness | category | Popular Culture | 108 | 0.264027 | 0.169273 | 0.635417 | 0.518233 |
| tossup_correctness | category | Religion | 361 | 0.137979 | 0.201408 | 0.655392 | 0.594004 |
| tossup_correctness | category | Science | 1445 | 0.0898128 | 0.186072 | 0.666205 | 0.556741 |
| tossup_correctness | category | Social Science | 327 | 0.111186 | 0.197065 | 0.659713 | 0.58518 |
| tossup_correctness | category | Unknown | 2039 | 0.133045 | 0.198402 | 0.618936 | 0.583081 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.306188 | 0.268481 | 0.671464 | 0.737184 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.224229 | 0.244867 | 0.612363 | 0.687531 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.162496 | 0.205556 | 0.649215 | 0.598481 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.135405 | 0.183603 | 0.627464 | 0.550889 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0590557 | 0.176245 | 0.630613 | 0.538498 |
