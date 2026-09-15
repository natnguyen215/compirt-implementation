# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.666095 |
| log_loss | 0.513879 |
| ece | 0.0159339 |
| brier | 0.167831 |
| accuracy | 0.767959 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00378092 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.119107 |
| probability_p10 | 0.598022 |
| probability_p50 | 0.78736 |
| probability_p90 | 0.898245 |
| mean_predictive_variance | 0.165707 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101938 |
| joint_tossup_event_log_loss | 6.87545 |
| buzz_position_mae | 0.161058 |
| buzz_position_median_absolute_error | 0.144288 |
| buzz_position_bias | -0.0679495 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.355407 |
| first_buzzer_mean_reciprocal_rank | 0.568937 |
| first_buzzer_log_loss | 1.65794 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.657016 |
| tossup_scorer_player_top1_accuracy | 0.32452 |
| tossup_scorer_team_top1_accuracy | 0.504371 |
| tossup_game_winner_accuracy | 0.795652 |
| tossup_game_margin_mae | 36.4207 |
| tournament_player_ppg_spearman | 0.697179 |
| tournament_player_ppg_mae | 8.78673 |
| tournament_player_ppg_top10_overlap | 0.658621 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.666095 |
| neg_average_precision | 0.390953 |
| neg_precision | 0.559727 |
| neg_recall | 0.075126 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0550303 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.091386 |
| no_buzz_calibration_error | 0.078273 |
| no_buzz_brier | 0.0252873 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9257 | -0.0679495 | -0.0838089 |
| Q1 (0-.2) | 183 | 0.379313 | 0.397211 |
| Q2 (.2-.4) | 955 | 0.2033 | 0.205247 |
| Q3 (.4-.6) | 2239 | 0.049357 | 0.0503159 |
| Q4 (.6-.8) | 2875 | -0.0904736 | -0.0878629 |
| Q5 (.8-1) | 3005 | -0.247245 | -0.246432 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0159339 | 0.167831 | 0.666095 | 0.513879 |
| tossup_correctness | tier | fall | 2798 | 0.0169274 | 0.155692 | 0.681244 | 0.484314 |
| tossup_correctness | tier | nationals | 1545 | 0.0556624 | 0.186672 | 0.686666 | 0.555499 |
| tossup_correctness | tier | regionals | 2039 | 0.033181 | 0.174083 | 0.631416 | 0.531087 |
| tossup_correctness | tier | winter | 2875 | 0.0269782 | 0.165085 | 0.668485 | 0.508081 |
| tossup_correctness | category | Current Events | 129 | 0.0549977 | 0.207597 | 0.658464 | 0.602115 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0241213 | 0.163698 | 0.662235 | 0.503209 |
| tossup_correctness | category | Geography | 180 | 0.108854 | 0.203039 | 0.735866 | 0.595617 |
| tossup_correctness | category | History | 1454 | 0.0368947 | 0.171006 | 0.671349 | 0.519631 |
| tossup_correctness | category | Literature | 1435 | 0.0462692 | 0.145029 | 0.648124 | 0.464364 |
| tossup_correctness | category | Mythology | 324 | 0.0449065 | 0.156438 | 0.657471 | 0.487072 |
| tossup_correctness | category | Other Academic | 71 | 0.116956 | 0.204045 | 0.38671 | 0.60362 |
| tossup_correctness | category | Philosophy | 310 | 0.0431659 | 0.169851 | 0.679283 | 0.513931 |
| tossup_correctness | category | Popular Culture | 108 | 0.132439 | 0.122255 | 0.572917 | 0.409856 |
| tossup_correctness | category | Religion | 361 | 0.0373061 | 0.177586 | 0.668954 | 0.536253 |
| tossup_correctness | category | Science | 1445 | 0.0359493 | 0.172064 | 0.703015 | 0.520566 |
| tossup_correctness | category | Social Science | 327 | 0.0361185 | 0.180378 | 0.708834 | 0.540662 |
| tossup_correctness | category | Unknown | 2039 | 0.033181 | 0.174083 | 0.631416 | 0.531087 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0862907 | 0.192686 | 0.595588 | 0.573823 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0286397 | 0.181478 | 0.683337 | 0.544957 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.00768621 | 0.170465 | 0.683973 | 0.517929 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.020358 | 0.157851 | 0.661796 | 0.490021 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0235947 | 0.169565 | 0.65404 | 0.520159 |
