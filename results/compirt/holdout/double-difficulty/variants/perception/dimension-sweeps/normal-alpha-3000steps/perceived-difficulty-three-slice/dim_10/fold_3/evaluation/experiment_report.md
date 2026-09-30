# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.659061 |
| log_loss | 0.51015 |
| ece | 0.0188985 |
| brier | 0.16543 |
| accuracy | 0.774559 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00451542 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.110043 |
| probability_p10 | 0.623338 |
| probability_p50 | 0.792324 |
| probability_p90 | 0.902974 |
| mean_predictive_variance | 0.161899 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102093 |
| joint_tossup_event_log_loss | 6.86495 |
| buzz_position_mae | 0.164024 |
| buzz_position_median_absolute_error | 0.15091 |
| buzz_position_bias | -0.0753426 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.350441 |
| first_buzzer_mean_reciprocal_rank | 0.562992 |
| first_buzzer_log_loss | 1.67821 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.654405 |
| tossup_scorer_player_top1_accuracy | 0.321909 |
| tossup_scorer_team_top1_accuracy | 0.514859 |
| tossup_game_winner_accuracy | 0.811947 |
| tossup_game_margin_mae | 35.4262 |
| tournament_player_ppg_spearman | 0.707288 |
| tournament_player_ppg_mae | 8.80648 |
| tournament_player_ppg_top10_overlap | 0.658621 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.659061 |
| neg_average_precision | 0.391547 |
| neg_precision | 0.617143 |
| neg_recall | 0.0517241 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0529272 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0881515 |
| no_buzz_calibration_error | 0.0729671 |
| no_buzz_brier | 0.0253394 |
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
| overall | 9080 | -0.0753426 | -0.0919439 |
| Q1 (0-.2) | 192 | 0.367034 | 0.369442 |
| Q2 (.2-.4) | 889 | 0.198575 | 0.200371 |
| Q3 (.4-.6) | 2210 | 0.0425707 | 0.0442351 |
| Q4 (.6-.8) | 2869 | -0.100289 | -0.0947234 |
| Q5 (.8-1) | 2920 | -0.252557 | -0.253441 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0188985 | 0.16543 | 0.659061 | 0.51015 |
| tossup_correctness | tier | fall | 2817 | 0.0234084 | 0.161138 | 0.645326 | 0.500866 |
| tossup_correctness | tier | nationals | 1542 | 0.0417515 | 0.178923 | 0.702672 | 0.537749 |
| tossup_correctness | tier | regionals | 1934 | 0.0148213 | 0.171833 | 0.660258 | 0.523123 |
| tossup_correctness | tier | winter | 2787 | 0.0218768 | 0.157861 | 0.645755 | 0.495261 |
| tossup_correctness | category | Current Events | 125 | 0.0733967 | 0.193057 | 0.650184 | 0.571203 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0221284 | 0.165494 | 0.660594 | 0.508773 |
| tossup_correctness | category | Geography | 185 | 0.0643066 | 0.175254 | 0.756503 | 0.526003 |
| tossup_correctness | category | History | 1443 | 0.0264475 | 0.1625 | 0.697822 | 0.49965 |
| tossup_correctness | category | Literature | 1411 | 0.042684 | 0.150679 | 0.59001 | 0.484288 |
| tossup_correctness | category | Mythology | 320 | 0.054083 | 0.160472 | 0.593116 | 0.506069 |
| tossup_correctness | category | Other Academic | 64 | 0.0818202 | 0.183901 | 0.585938 | 0.554615 |
| tossup_correctness | category | Philosophy | 312 | 0.0356927 | 0.159112 | 0.576258 | 0.502441 |
| tossup_correctness | category | Popular Culture | 104 | 0.0696881 | 0.138263 | 0.524148 | 0.450808 |
| tossup_correctness | category | Religion | 358 | 0.0374322 | 0.187664 | 0.659066 | 0.560884 |
| tossup_correctness | category | Science | 1431 | 0.0200501 | 0.166053 | 0.668357 | 0.509596 |
| tossup_correctness | category | Social Science | 321 | 0.0269618 | 0.176868 | 0.679049 | 0.532366 |
| tossup_correctness | category | Unknown | 1934 | 0.0148213 | 0.171833 | 0.660258 | 0.523123 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0478629 | 0.190122 | 0.708183 | 0.562669 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0209624 | 0.178088 | 0.681642 | 0.537412 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0257391 | 0.174073 | 0.634664 | 0.532048 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0177674 | 0.15768 | 0.645712 | 0.492434 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0325032 | 0.161027 | 0.672975 | 0.49923 |
