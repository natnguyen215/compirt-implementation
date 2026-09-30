# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.631536 |
| log_loss | 0.528069 |
| ece | 0.0401181 |
| brier | 0.17212 |
| accuracy | 0.76685 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00319383 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.135005 |
| probability_p10 | 0.569315 |
| probability_p50 | 0.783937 |
| probability_p90 | 0.911014 |
| mean_predictive_variance | 0.164835 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10428 |
| joint_tossup_event_log_loss | 6.92067 |
| buzz_position_mae | 0.163756 |
| buzz_position_median_absolute_error | 0.147599 |
| buzz_position_bias | -0.0736129 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34185 |
| first_buzzer_mean_reciprocal_rank | 0.55468 |
| first_buzzer_log_loss | 1.70651 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.647137 |
| tossup_scorer_player_top1_accuracy | 0.307375 |
| tossup_scorer_team_top1_accuracy | 0.486876 |
| tossup_game_winner_accuracy | 0.772124 |
| tossup_game_margin_mae | 36.1602 |
| tournament_player_ppg_spearman | 0.706108 |
| tournament_player_ppg_mae | 8.81494 |
| tournament_player_ppg_top10_overlap | 0.672414 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.631536 |
| neg_average_precision | 0.343072 |
| neg_precision | 0.468132 |
| neg_recall | 0.102011 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0548206 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0853905 |
| no_buzz_calibration_error | 0.0702061 |
| no_buzz_brier | 0.0240688 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0736129 | -0.0903804 |
| Q1 (0-.2) | 192 | 0.363731 | 0.373475 |
| Q2 (.2-.4) | 889 | 0.199169 | 0.196647 |
| Q3 (.4-.6) | 2210 | 0.0436155 | 0.0471132 |
| Q4 (.6-.8) | 2869 | -0.0975108 | -0.0948304 |
| Q5 (.8-1) | 2920 | -0.250662 | -0.251217 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0401181 | 0.17212 | 0.631536 | 0.528069 |
| tossup_correctness | tier | fall | 2817 | 0.0406828 | 0.168826 | 0.605132 | 0.523411 |
| tossup_correctness | tier | nationals | 1542 | 0.0659474 | 0.184583 | 0.683468 | 0.549702 |
| tossup_correctness | tier | regionals | 1934 | 0.0413125 | 0.18112 | 0.620332 | 0.549687 |
| tossup_correctness | tier | winter | 2787 | 0.0392511 | 0.16231 | 0.630877 | 0.505806 |
| tossup_correctness | category | Current Events | 125 | 0.0705054 | 0.194902 | 0.657555 | 0.574799 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0403759 | 0.171848 | 0.625908 | 0.525801 |
| tossup_correctness | category | Geography | 185 | 0.0671464 | 0.172558 | 0.757203 | 0.521172 |
| tossup_correctness | category | History | 1443 | 0.0266156 | 0.165397 | 0.687626 | 0.506388 |
| tossup_correctness | category | Literature | 1411 | 0.0475572 | 0.154907 | 0.567314 | 0.501642 |
| tossup_correctness | category | Mythology | 320 | 0.11315 | 0.169999 | 0.578144 | 0.524791 |
| tossup_correctness | category | Other Academic | 64 | 0.0705121 | 0.18808 | 0.595052 | 0.564429 |
| tossup_correctness | category | Philosophy | 312 | 0.0556721 | 0.160095 | 0.58129 | 0.501344 |
| tossup_correctness | category | Popular Culture | 104 | 0.16371 | 0.162093 | 0.50142 | 0.508343 |
| tossup_correctness | category | Religion | 358 | 0.0603032 | 0.192301 | 0.641091 | 0.573727 |
| tossup_correctness | category | Science | 1431 | 0.0689973 | 0.176774 | 0.648163 | 0.534455 |
| tossup_correctness | category | Social Science | 321 | 0.050096 | 0.186185 | 0.636136 | 0.553793 |
| tossup_correctness | category | Unknown | 1934 | 0.0413125 | 0.18112 | 0.620332 | 0.549687 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0791721 | 0.200321 | 0.681163 | 0.584676 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0540263 | 0.192265 | 0.628802 | 0.570367 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0417356 | 0.18136 | 0.612267 | 0.549365 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0378879 | 0.161624 | 0.632471 | 0.503092 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0385475 | 0.167452 | 0.634693 | 0.519891 |
