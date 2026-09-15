# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.562697 |
| log_loss | 0.557084 |
| ece | 0.0787625 |
| brier | 0.180998 |
| accuracy | 0.768722 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00132159 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.119164 |
| probability_p10 | 0.614991 |
| probability_p50 | 0.825871 |
| probability_p90 | 0.917372 |
| mean_predictive_variance | 0.15089 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174248 |
| joint_tossup_event_log_loss | 7.66672 |
| buzz_position_mae | 0.325353 |
| buzz_position_median_absolute_error | 0.323426 |
| buzz_position_bias | -0.308727 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.312225 |
| first_buzzer_mean_reciprocal_rank | 0.529718 |
| first_buzzer_log_loss | 1.75019 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.625881 |
| tossup_scorer_player_top1_accuracy | 0.253254 |
| tossup_scorer_team_top1_accuracy | 0.400108 |
| tossup_game_winner_accuracy | 0.70354 |
| tossup_game_margin_mae | 48.1012 |
| tournament_player_ppg_spearman | 0.520813 |
| tournament_player_ppg_mae | 11.2243 |
| tournament_player_ppg_top10_overlap | 0.527586 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.562697 |
| neg_average_precision | 0.292763 |
| neg_precision | 0.464706 |
| neg_recall | 0.0378352 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0354909 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.202131 |
| no_buzz_calibration_error | 0.186947 |
| no_buzz_brier | 0.0565004 |
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
| overall | 9080 | -0.308727 | -0.323231 |
| Q1 (0-.2) | 192 | 0.196032 | 0.187167 |
| Q2 (.2-.4) | 889 | 0.0225395 | 0.0144757 |
| Q3 (.4-.6) | 2210 | -0.157547 | -0.158428 |
| Q4 (.6-.8) | 2869 | -0.335096 | -0.3344 |
| Q5 (.8-1) | 2920 | -0.531283 | -0.530151 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0787625 | 0.180998 | 0.562697 | 0.557084 |
| tossup_correctness | tier | fall | 2817 | 0.0721654 | 0.175346 | 0.557462 | 0.544123 |
| tossup_correctness | tier | nationals | 1542 | 0.0874826 | 0.195422 | 0.615172 | 0.57948 |
| tossup_correctness | tier | regionals | 1934 | 0.0946611 | 0.19061 | 0.533966 | 0.580461 |
| tossup_correctness | tier | winter | 2787 | 0.0705958 | 0.172062 | 0.543476 | 0.541572 |
| tossup_correctness | category | Current Events | 125 | 0.108845 | 0.206679 | 0.628993 | 0.601247 |
| tossup_correctness | category | Fine Arts | 1072 | 0.100785 | 0.185082 | 0.551477 | 0.569171 |
| tossup_correctness | category | Geography | 185 | 0.0875764 | 0.201846 | 0.651469 | 0.598095 |
| tossup_correctness | category | History | 1443 | 0.0497552 | 0.177099 | 0.600386 | 0.543556 |
| tossup_correctness | category | Literature | 1411 | 0.0852884 | 0.160242 | 0.529444 | 0.515012 |
| tossup_correctness | category | Mythology | 320 | 0.0669118 | 0.171536 | 0.537163 | 0.538298 |
| tossup_correctness | category | Other Academic | 64 | 0.0742862 | 0.180764 | 0.648438 | 0.546972 |
| tossup_correctness | category | Philosophy | 312 | 0.130407 | 0.174112 | 0.476387 | 0.552596 |
| tossup_correctness | category | Popular Culture | 104 | 0.0793705 | 0.145209 | 0.473722 | 0.469887 |
| tossup_correctness | category | Religion | 358 | 0.103701 | 0.205454 | 0.587049 | 0.616125 |
| tossup_correctness | category | Science | 1431 | 0.0568673 | 0.178736 | 0.596374 | 0.544661 |
| tossup_correctness | category | Social Science | 321 | 0.126849 | 0.206782 | 0.512144 | 0.623679 |
| tossup_correctness | category | Unknown | 1934 | 0.0946611 | 0.19061 | 0.533966 | 0.580461 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.126334 | 0.222306 | 0.508749 | 0.646053 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0708467 | 0.19854 | 0.566883 | 0.591406 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0832855 | 0.19104 | 0.530937 | 0.580584 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0758339 | 0.169278 | 0.564495 | 0.52799 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0838239 | 0.176857 | 0.57844 | 0.551585 |
