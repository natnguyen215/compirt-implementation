# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.562686 |
| log_loss | 0.621626 |
| ece | 0.120017 |
| brier | 0.194425 |
| accuracy | 0.761795 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000329924 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0858528 |
| probability_p10 | 0.769594 |
| probability_p50 | 0.900706 |
| probability_p90 | 0.955427 |
| mean_predictive_variance | 0.100523 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.175309 |
| joint_tossup_event_log_loss | 7.80779 |
| buzz_position_mae | 0.34585 |
| buzz_position_median_absolute_error | 0.353516 |
| buzz_position_bias | -0.334303 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.334213 |
| first_buzzer_mean_reciprocal_rank | 0.551504 |
| first_buzzer_log_loss | 1.69985 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.619597 |
| tossup_scorer_player_top1_accuracy | 0.265368 |
| tossup_scorer_team_top1_accuracy | 0.410931 |
| tossup_game_winner_accuracy | 0.745495 |
| tossup_game_margin_mae | 41.2662 |
| tournament_player_ppg_spearman | 0.609368 |
| tournament_player_ppg_mae | 10.0515 |
| tournament_player_ppg_top10_overlap | 0.593103 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.562686 |
| neg_average_precision | 0.287662 |
| neg_precision | 0.44 |
| neg_recall | 0.00508553 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0285451 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.233759 |
| no_buzz_calibration_error | 0.217849 |
| no_buzz_brier | 0.071348 |
| full_pmf_max_mass_error | 1.44329e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.334303 | -0.353516 |
| Q1 (0-.2) | 167 | 0.164925 | 0.164282 |
| Q2 (.2-.4) | 912 | 0.00423439 | 0.00181591 |
| Q3 (.4-.6) | 2115 | -0.174099 | -0.178582 |
| Q4 (.6-.8) | 2844 | -0.355317 | -0.357439 |
| Q5 (.8-1) | 3055 | -0.554005 | -0.558344 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.120017 | 0.194425 | 0.562686 | 0.621626 |
| tossup_correctness | tier | fall | 2842 | 0.0933387 | 0.175464 | 0.579977 | 0.557805 |
| tossup_correctness | tier | nationals | 1564 | 0.146336 | 0.222592 | 0.576622 | 0.694793 |
| tossup_correctness | tier | regionals | 1937 | 0.127935 | 0.199004 | 0.53803 | 0.644448 |
| tossup_correctness | tier | winter | 2750 | 0.127899 | 0.194776 | 0.555293 | 0.629896 |
| tossup_correctness | category | Current Events | 126 | 0.138056 | 0.196908 | 0.495912 | 0.619252 |
| tossup_correctness | category | Fine Arts | 1071 | 0.125305 | 0.193244 | 0.568831 | 0.619645 |
| tossup_correctness | category | Geography | 185 | 0.182687 | 0.235946 | 0.61448 | 0.71824 |
| tossup_correctness | category | History | 1440 | 0.129699 | 0.201925 | 0.55002 | 0.639079 |
| tossup_correctness | category | Literature | 1422 | 0.0819573 | 0.157516 | 0.546099 | 0.525897 |
| tossup_correctness | category | Mythology | 318 | 0.0964029 | 0.169031 | 0.620444 | 0.54073 |
| tossup_correctness | category | Other Academic | 66 | 0.176794 | 0.236063 | 0.539754 | 0.751094 |
| tossup_correctness | category | Philosophy | 311 | 0.146162 | 0.203963 | 0.605031 | 0.648767 |
| tossup_correctness | category | Popular Culture | 102 | 0.0213827 | 0.109358 | 0.572222 | 0.380118 |
| tossup_correctness | category | Religion | 358 | 0.175917 | 0.23196 | 0.597982 | 0.712176 |
| tossup_correctness | category | Science | 1433 | 0.132561 | 0.207581 | 0.571749 | 0.651556 |
| tossup_correctness | category | Social Science | 324 | 0.14688 | 0.209345 | 0.611911 | 0.650652 |
| tossup_correctness | category | Unknown | 1937 | 0.127935 | 0.199004 | 0.53803 | 0.644448 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.151335 | 0.231234 | 0.482143 | 0.714702 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.134075 | 0.212498 | 0.575979 | 0.651522 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.114882 | 0.19825 | 0.556568 | 0.622403 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.104639 | 0.181082 | 0.558482 | 0.583008 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.13264 | 0.196791 | 0.563663 | 0.643027 |
