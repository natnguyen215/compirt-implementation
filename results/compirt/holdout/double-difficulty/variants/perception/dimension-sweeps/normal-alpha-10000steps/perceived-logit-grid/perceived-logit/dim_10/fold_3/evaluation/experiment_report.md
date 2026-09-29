# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.635199 |
| log_loss | 0.579538 |
| ece | 0.152038 |
| brier | 0.197161 |
| accuracy | 0.703194 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0668502 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.153729 |
| probability_p10 | 0.410005 |
| probability_p50 | 0.626785 |
| probability_p90 | 0.815605 |
| mean_predictive_variance | 0.212431 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10022 |
| joint_tossup_event_log_loss | 6.61183 |
| buzz_position_mae | 0.163864 |
| buzz_position_median_absolute_error | 0.144385 |
| buzz_position_bias | -0.081296 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.399009 |
| first_buzzer_mean_reciprocal_rank | 0.603105 |
| first_buzzer_log_loss | 1.57934 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.667511 |
| tossup_scorer_player_top1_accuracy | 0.287852 |
| tossup_scorer_team_top1_accuracy | 0.390564 |
| tossup_game_winner_accuracy | 0.811947 |
| tossup_game_margin_mae | 41.6504 |
| tournament_player_ppg_spearman | 0.655352 |
| tournament_player_ppg_mae | 11.6125 |
| tournament_player_ppg_top10_overlap | 0.675862 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.635199 |
| neg_average_precision | 0.342808 |
| neg_precision | 0.353594 |
| neg_recall | 0.351054 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0973064 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0793117 |
| no_buzz_calibration_error | 0.0641273 |
| no_buzz_brier | 0.025364 |
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
| overall | 9080 | -0.081296 | -0.0947236 |
| Q1 (0-.2) | 192 | 0.357008 | 0.361078 |
| Q2 (.2-.4) | 889 | 0.178931 | 0.175271 |
| Q3 (.4-.6) | 2210 | 0.0272097 | 0.0241404 |
| Q4 (.6-.8) | 2869 | -0.103698 | -0.104318 |
| Q5 (.8-1) | 2920 | -0.249454 | -0.248215 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.152038 | 0.197161 | 0.635199 | 0.579538 |
| tossup_correctness | tier | fall | 2817 | 0.120765 | 0.180957 | 0.639284 | 0.543103 |
| tossup_correctness | tier | nationals | 1542 | 0.167265 | 0.218431 | 0.626748 | 0.626831 |
| tossup_correctness | tier | regionals | 1934 | 0.150072 | 0.203481 | 0.627003 | 0.59383 |
| tossup_correctness | tier | winter | 2787 | 0.177452 | 0.197384 | 0.636583 | 0.580282 |
| tossup_correctness | category | Current Events | 125 | 0.103172 | 0.204577 | 0.629914 | 0.597835 |
| tossup_correctness | category | Fine Arts | 1072 | 0.182005 | 0.211391 | 0.595516 | 0.609225 |
| tossup_correctness | category | Geography | 185 | 0.0991845 | 0.21243 | 0.642378 | 0.61029 |
| tossup_correctness | category | History | 1443 | 0.131481 | 0.186084 | 0.671428 | 0.55374 |
| tossup_correctness | category | Literature | 1411 | 0.179958 | 0.189683 | 0.620379 | 0.56428 |
| tossup_correctness | category | Mythology | 320 | 0.20772 | 0.218733 | 0.557027 | 0.627741 |
| tossup_correctness | category | Other Academic | 64 | 0.209829 | 0.21789 | 0.651042 | 0.625021 |
| tossup_correctness | category | Philosophy | 312 | 0.196878 | 0.199083 | 0.623355 | 0.583228 |
| tossup_correctness | category | Popular Culture | 104 | 0.312733 | 0.219239 | 0.483665 | 0.629808 |
| tossup_correctness | category | Religion | 358 | 0.13079 | 0.19711 | 0.68438 | 0.581267 |
| tossup_correctness | category | Science | 1431 | 0.120073 | 0.184745 | 0.657657 | 0.552267 |
| tossup_correctness | category | Social Science | 321 | 0.146295 | 0.203277 | 0.648076 | 0.595127 |
| tossup_correctness | category | Unknown | 1934 | 0.150072 | 0.203481 | 0.627003 | 0.59383 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.2766 | 0.273535 | 0.66984 | 0.746429 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.245641 | 0.241645 | 0.677856 | 0.6765 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.19149 | 0.215162 | 0.63614 | 0.620422 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.155468 | 0.189519 | 0.617688 | 0.562681 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0827861 | 0.172479 | 0.6535 | 0.524664 |
