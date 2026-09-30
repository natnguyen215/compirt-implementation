# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.669694 |
| log_loss | 0.514551 |
| ece | 0.0201813 |
| brier | 0.1676 |
| accuracy | 0.769256 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00507724 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.132075 |
| probability_p10 | 0.566891 |
| probability_p50 | 0.776745 |
| probability_p90 | 0.90332 |
| mean_predictive_variance | 0.168268 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100834 |
| joint_tossup_event_log_loss | 6.88408 |
| buzz_position_mae | 0.158062 |
| buzz_position_median_absolute_error | 0.141977 |
| buzz_position_bias | -0.0592003 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349141 |
| first_buzzer_mean_reciprocal_rank | 0.560838 |
| first_buzzer_log_loss | 1.67983 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.653884 |
| tossup_scorer_player_top1_accuracy | 0.322708 |
| tossup_scorer_team_top1_accuracy | 0.500107 |
| tossup_game_winner_accuracy | 0.786957 |
| tossup_game_margin_mae | 36.7927 |
| tournament_player_ppg_spearman | 0.700086 |
| tournament_player_ppg_mae | 8.96346 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.669694 |
| neg_average_precision | 0.398579 |
| neg_precision | 0.551198 |
| neg_recall | 0.115896 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0581468 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0968015 |
| no_buzz_calibration_error | 0.0836885 |
| no_buzz_brier | 0.0266649 |
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
| overall | 9257 | -0.0592003 | -0.0749778 |
| Q1 (0-.2) | 183 | 0.385043 | 0.399609 |
| Q2 (.2-.4) | 955 | 0.212996 | 0.217943 |
| Q3 (.4-.6) | 2239 | 0.0584952 | 0.0594704 |
| Q4 (.6-.8) | 2875 | -0.0816063 | -0.0772623 |
| Q5 (.8-1) | 3005 | -0.239016 | -0.239348 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0201813 | 0.1676 | 0.669694 | 0.514551 |
| tossup_correctness | tier | fall | 2798 | 0.0235049 | 0.156055 | 0.681824 | 0.485924 |
| tossup_correctness | tier | nationals | 1545 | 0.0475771 | 0.183619 | 0.699615 | 0.547588 |
| tossup_correctness | tier | regionals | 2039 | 0.0388167 | 0.174031 | 0.63266 | 0.534443 |
| tossup_correctness | tier | winter | 2875 | 0.0241748 | 0.165666 | 0.664581 | 0.510549 |
| tossup_correctness | category | Current Events | 129 | 0.0601966 | 0.20642 | 0.673607 | 0.598947 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0353588 | 0.16654 | 0.652298 | 0.51053 |
| tossup_correctness | category | Geography | 180 | 0.0652253 | 0.202168 | 0.726727 | 0.592465 |
| tossup_correctness | category | History | 1454 | 0.0291121 | 0.1704 | 0.67476 | 0.518755 |
| tossup_correctness | category | Literature | 1435 | 0.0335513 | 0.14366 | 0.653587 | 0.463098 |
| tossup_correctness | category | Mythology | 324 | 0.0508916 | 0.156598 | 0.664208 | 0.485969 |
| tossup_correctness | category | Other Academic | 71 | 0.10076 | 0.202239 | 0.380174 | 0.600709 |
| tossup_correctness | category | Philosophy | 310 | 0.0256278 | 0.172802 | 0.65489 | 0.523165 |
| tossup_correctness | category | Popular Culture | 108 | 0.164549 | 0.134874 | 0.568576 | 0.441602 |
| tossup_correctness | category | Religion | 361 | 0.0432386 | 0.175249 | 0.680749 | 0.530435 |
| tossup_correctness | category | Science | 1445 | 0.00978156 | 0.169942 | 0.707069 | 0.515063 |
| tossup_correctness | category | Social Science | 327 | 0.0403671 | 0.179706 | 0.709852 | 0.540377 |
| tossup_correctness | category | Unknown | 2039 | 0.0388167 | 0.174031 | 0.63266 | 0.534443 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.101532 | 0.194521 | 0.601377 | 0.577236 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0321601 | 0.181344 | 0.684679 | 0.544231 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0164532 | 0.169656 | 0.686512 | 0.516746 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0242296 | 0.157056 | 0.669947 | 0.488672 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0220961 | 0.170149 | 0.653192 | 0.524424 |
