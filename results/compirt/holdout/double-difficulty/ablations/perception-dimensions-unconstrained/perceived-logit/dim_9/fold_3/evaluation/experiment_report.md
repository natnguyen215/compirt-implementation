# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.566571 |
| log_loss | 0.551873 |
| ece | 0.072777 |
| brier | 0.180065 |
| accuracy | 0.768282 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00176211 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.117914 |
| probability_p10 | 0.606171 |
| probability_p50 | 0.809982 |
| probability_p90 | 0.908747 |
| mean_predictive_variance | 0.157539 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174133 |
| joint_tossup_event_log_loss | 7.66121 |
| buzz_position_mae | 0.321826 |
| buzz_position_median_absolute_error | 0.318516 |
| buzz_position_bias | -0.304207 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.295264 |
| first_buzzer_mean_reciprocal_rank | 0.51626 |
| first_buzzer_log_loss | 1.7758 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.618943 |
| tossup_scorer_player_top1_accuracy | 0.249349 |
| tossup_scorer_team_top1_accuracy | 0.390347 |
| tossup_game_winner_accuracy | 0.712389 |
| tossup_game_margin_mae | 48.2466 |
| tournament_player_ppg_spearman | 0.508591 |
| tournament_player_ppg_mae | 11.3844 |
| tournament_player_ppg_top10_overlap | 0.524138 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.566571 |
| neg_average_precision | 0.29497 |
| neg_precision | 0.449367 |
| neg_recall | 0.0340038 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0367958 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.195783 |
| no_buzz_calibration_error | 0.180598 |
| no_buzz_brier | 0.053884 |
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
| overall | 9080 | -0.304207 | -0.318219 |
| Q1 (0-.2) | 192 | 0.201503 | 0.19317 |
| Q2 (.2-.4) | 889 | 0.0274451 | 0.0217712 |
| Q3 (.4-.6) | 2210 | -0.153609 | -0.15444 |
| Q4 (.6-.8) | 2869 | -0.330779 | -0.331033 |
| Q5 (.8-1) | 2920 | -0.526303 | -0.525102 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.072777 | 0.180065 | 0.566571 | 0.551873 |
| tossup_correctness | tier | fall | 2817 | 0.0588904 | 0.174021 | 0.562309 | 0.538544 |
| tossup_correctness | tier | nationals | 1542 | 0.0878656 | 0.195671 | 0.623239 | 0.579258 |
| tossup_correctness | tier | regionals | 1934 | 0.0893295 | 0.189802 | 0.534987 | 0.575299 |
| tossup_correctness | tier | winter | 2787 | 0.0683351 | 0.170782 | 0.550856 | 0.533937 |
| tossup_correctness | category | Current Events | 125 | 0.0872009 | 0.202702 | 0.6336 | 0.591503 |
| tossup_correctness | category | Fine Arts | 1072 | 0.089784 | 0.184193 | 0.548121 | 0.56332 |
| tossup_correctness | category | Geography | 185 | 0.0868262 | 0.200938 | 0.646713 | 0.594309 |
| tossup_correctness | category | History | 1443 | 0.051141 | 0.175982 | 0.605524 | 0.539231 |
| tossup_correctness | category | Literature | 1411 | 0.0843131 | 0.159933 | 0.533819 | 0.510752 |
| tossup_correctness | category | Mythology | 320 | 0.0562135 | 0.170622 | 0.536328 | 0.533041 |
| tossup_correctness | category | Other Academic | 64 | 0.0864631 | 0.178244 | 0.653646 | 0.541024 |
| tossup_correctness | category | Philosophy | 312 | 0.126679 | 0.173724 | 0.481419 | 0.547041 |
| tossup_correctness | category | Popular Culture | 104 | 0.0962748 | 0.144862 | 0.5 | 0.464965 |
| tossup_correctness | category | Religion | 358 | 0.095187 | 0.202926 | 0.590816 | 0.605344 |
| tossup_correctness | category | Science | 1431 | 0.053825 | 0.177989 | 0.608401 | 0.540695 |
| tossup_correctness | category | Social Science | 321 | 0.103283 | 0.204714 | 0.512501 | 0.61417 |
| tossup_correctness | category | Unknown | 1934 | 0.0893295 | 0.189802 | 0.534987 | 0.575299 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.111541 | 0.217696 | 0.540916 | 0.631048 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0727399 | 0.198095 | 0.567439 | 0.588248 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0724729 | 0.189848 | 0.535922 | 0.574946 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0719512 | 0.168784 | 0.566527 | 0.525103 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0785887 | 0.175779 | 0.583147 | 0.54443 |
