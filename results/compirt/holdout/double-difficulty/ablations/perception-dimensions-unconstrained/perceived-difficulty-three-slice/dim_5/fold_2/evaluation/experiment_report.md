# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.667897 |
| log_loss | 0.513142 |
| ece | 0.015045 |
| brier | 0.167866 |
| accuracy | 0.765475 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00129632 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.121009 |
| probability_p10 | 0.593629 |
| probability_p50 | 0.786663 |
| probability_p90 | 0.896825 |
| mean_predictive_variance | 0.166622 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101784 |
| joint_tossup_event_log_loss | 6.88248 |
| buzz_position_mae | 0.160429 |
| buzz_position_median_absolute_error | 0.143952 |
| buzz_position_bias | -0.0667609 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.350762 |
| first_buzzer_mean_reciprocal_rank | 0.563455 |
| first_buzzer_log_loss | 1.66667 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.659501 |
| tossup_scorer_player_top1_accuracy | 0.321322 |
| tossup_scorer_team_top1_accuracy | 0.500107 |
| tossup_game_winner_accuracy | 0.793478 |
| tossup_game_margin_mae | 35.4009 |
| tournament_player_ppg_spearman | 0.710035 |
| tournament_player_ppg_mae | 8.52453 |
| tournament_player_ppg_top10_overlap | 0.655172 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.667897 |
| neg_average_precision | 0.388654 |
| neg_precision | 0.518182 |
| neg_recall | 0.0783326 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0557846 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0926974 |
| no_buzz_calibration_error | 0.0795844 |
| no_buzz_brier | 0.0254164 |
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
| overall | 9257 | -0.0667609 | -0.0828606 |
| Q1 (0-.2) | 183 | 0.376122 | 0.38932 |
| Q2 (.2-.4) | 955 | 0.203837 | 0.208378 |
| Q3 (.4-.6) | 2239 | 0.0493818 | 0.0515641 |
| Q4 (.6-.8) | 2875 | -0.0889677 | -0.08671 |
| Q5 (.8-1) | 3005 | -0.24502 | -0.245291 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.015045 | 0.167866 | 0.667897 | 0.513142 |
| tossup_correctness | tier | fall | 2798 | 0.0115506 | 0.155649 | 0.682099 | 0.482983 |
| tossup_correctness | tier | nationals | 1545 | 0.0497468 | 0.18787 | 0.678521 | 0.557947 |
| tossup_correctness | tier | regionals | 2039 | 0.0239331 | 0.172142 | 0.641821 | 0.525537 |
| tossup_correctness | tier | winter | 2875 | 0.0205987 | 0.165973 | 0.664173 | 0.509624 |
| tossup_correctness | category | Current Events | 129 | 0.0605523 | 0.209304 | 0.659005 | 0.6078 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0314977 | 0.167046 | 0.653018 | 0.510721 |
| tossup_correctness | category | Geography | 180 | 0.100052 | 0.204472 | 0.73665 | 0.598353 |
| tossup_correctness | category | History | 1454 | 0.0218266 | 0.170265 | 0.671976 | 0.517278 |
| tossup_correctness | category | Literature | 1435 | 0.0445276 | 0.14591 | 0.647947 | 0.465143 |
| tossup_correctness | category | Mythology | 324 | 0.053879 | 0.156873 | 0.662117 | 0.485392 |
| tossup_correctness | category | Other Academic | 71 | 0.11651 | 0.203285 | 0.407407 | 0.599124 |
| tossup_correctness | category | Philosophy | 310 | 0.042712 | 0.167961 | 0.685925 | 0.509272 |
| tossup_correctness | category | Popular Culture | 108 | 0.144237 | 0.127984 | 0.571181 | 0.422428 |
| tossup_correctness | category | Religion | 361 | 0.0340689 | 0.180073 | 0.655152 | 0.541463 |
| tossup_correctness | category | Science | 1445 | 0.0351968 | 0.17143 | 0.705871 | 0.518324 |
| tossup_correctness | category | Social Science | 327 | 0.0207014 | 0.180138 | 0.707909 | 0.54009 |
| tossup_correctness | category | Unknown | 2039 | 0.0239331 | 0.172142 | 0.641821 | 0.525537 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0771046 | 0.19007 | 0.615926 | 0.566479 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0304312 | 0.184306 | 0.669063 | 0.551448 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0106356 | 0.170324 | 0.687067 | 0.516899 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0195191 | 0.158346 | 0.659486 | 0.490624 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0218743 | 0.168566 | 0.661402 | 0.516464 |
