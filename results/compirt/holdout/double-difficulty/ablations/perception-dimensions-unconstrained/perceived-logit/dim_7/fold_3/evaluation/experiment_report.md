# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.560837 |
| log_loss | 0.562474 |
| ece | 0.0805483 |
| brier | 0.181791 |
| accuracy | 0.769273 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000770925 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.118722 |
| probability_p10 | 0.627042 |
| probability_p50 | 0.841748 |
| probability_p90 | 0.925831 |
| mean_predictive_variance | 0.143185 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.175661 |
| joint_tossup_event_log_loss | 7.69315 |
| buzz_position_mae | 0.329477 |
| buzz_position_median_absolute_error | 0.32801 |
| buzz_position_bias | -0.313718 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.312996 |
| first_buzzer_mean_reciprocal_rank | 0.531548 |
| first_buzzer_log_loss | 1.74637 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.62478 |
| tossup_scorer_player_top1_accuracy | 0.253905 |
| tossup_scorer_team_top1_accuracy | 0.404338 |
| tossup_game_winner_accuracy | 0.688053 |
| tossup_game_margin_mae | 47.7894 |
| tournament_player_ppg_spearman | 0.540159 |
| tournament_player_ppg_mae | 11.1168 |
| tournament_player_ppg_top10_overlap | 0.541379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.560837 |
| neg_average_precision | 0.292699 |
| neg_precision | 0.477419 |
| neg_recall | 0.0354406 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0340665 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.205166 |
| no_buzz_calibration_error | 0.189981 |
| no_buzz_brier | 0.0579457 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9080 | -0.313718 | -0.327903 |
| Q1 (0-.2) | 192 | 0.191763 | 0.182042 |
| Q2 (.2-.4) | 889 | 0.0181891 | 0.00992346 |
| Q3 (.4-.6) | 2210 | -0.161648 | -0.162064 |
| Q4 (.6-.8) | 2869 | -0.340309 | -0.338934 |
| Q5 (.8-1) | 2920 | -0.536973 | -0.536023 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0805483 | 0.181791 | 0.560837 | 0.562474 |
| tossup_correctness | tier | fall | 2817 | 0.0722749 | 0.17616 | 0.555268 | 0.548294 |
| tossup_correctness | tier | nationals | 1542 | 0.0804568 | 0.193979 | 0.611776 | 0.577663 |
| tossup_correctness | tier | regionals | 1934 | 0.097978 | 0.191753 | 0.533413 | 0.588102 |
| tossup_correctness | tier | winter | 2787 | 0.0785233 | 0.173826 | 0.542094 | 0.55062 |
| tossup_correctness | category | Current Events | 125 | 0.102631 | 0.210113 | 0.625 | 0.609959 |
| tossup_correctness | category | Fine Arts | 1072 | 0.09987 | 0.185481 | 0.553293 | 0.573691 |
| tossup_correctness | category | Geography | 185 | 0.103343 | 0.203952 | 0.659021 | 0.605633 |
| tossup_correctness | category | History | 1443 | 0.0545706 | 0.178359 | 0.595699 | 0.549127 |
| tossup_correctness | category | Literature | 1411 | 0.0858951 | 0.15987 | 0.530394 | 0.517327 |
| tossup_correctness | category | Mythology | 320 | 0.0681937 | 0.171638 | 0.534479 | 0.54066 |
| tossup_correctness | category | Other Academic | 64 | 0.0690868 | 0.182315 | 0.636719 | 0.553376 |
| tossup_correctness | category | Philosophy | 312 | 0.117154 | 0.174401 | 0.471613 | 0.559216 |
| tossup_correctness | category | Popular Culture | 104 | 0.063389 | 0.143334 | 0.471591 | 0.467204 |
| tossup_correctness | category | Religion | 358 | 0.0998216 | 0.207926 | 0.58387 | 0.6279 |
| tossup_correctness | category | Science | 1431 | 0.0638689 | 0.179438 | 0.592319 | 0.548788 |
| tossup_correctness | category | Social Science | 321 | 0.124163 | 0.208422 | 0.510766 | 0.631337 |
| tossup_correctness | category | Unknown | 1934 | 0.097978 | 0.191753 | 0.533413 | 0.588102 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.126062 | 0.225447 | 0.501158 | 0.65799 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0756542 | 0.20019 | 0.562049 | 0.598103 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.087939 | 0.192358 | 0.525259 | 0.588001 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0732782 | 0.168958 | 0.567717 | 0.529138 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0867359 | 0.177928 | 0.575525 | 0.558781 |
