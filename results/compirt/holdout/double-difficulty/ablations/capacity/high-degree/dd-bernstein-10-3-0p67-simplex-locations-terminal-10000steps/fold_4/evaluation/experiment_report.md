# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.723955 |
| log_loss | 0.47829 |
| ece | 0.0222659 |
| brier | 0.154547 |
| accuracy | 0.785113 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0117584 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.151908 |
| probability_p10 | 0.53825 |
| probability_p50 | 0.78692 |
| probability_p90 | 0.909378 |
| mean_predictive_variance | 0.163878 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0993127 |
| joint_tossup_event_log_loss | 6.5146 |
| buzz_position_mae | 0.138341 |
| buzz_position_median_absolute_error | 0.112171 |
| buzz_position_bias | 0.0293337 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.361489 |
| first_buzzer_mean_reciprocal_rank | 0.572993 |
| first_buzzer_log_loss | 1.6511 |
| first_buzzer_events | 9270 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.215534 |
| first_buzzer_team_replay_accuracy | 0.484035 |
| tossup_scorer_player_replay_accuracy | 0.238166 |
| tossup_scorer_team_replay_accuracy | 0.458635 |
| tossup_game_winner_accuracy | 0.700873 |
| tossup_game_margin_mae | 50.9382 |
| tossup_game_zero_margin_mae | 58.0704 |
| tournament_player_ppg_spearman | 0.58927 |
| tournament_player_ppg_mae | 12.7195 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| tournament_player_ppg_top10_random_overlap | 0.291672 |
| tournament_player_ppg_top10_adjusted_overlap | 0.444395 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.723955 |
| neg_average_precision | 0.449162 |
| neg_precision | 0.576438 |
| neg_recall | 0.195621 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.247752 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0251657 |
| no_buzz_calibration_error | 0.0134386 |
| no_buzz_brier | 0.0131157 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9380 |
| tossup_replay_seed | 42 |
| first_buzzer_player_replay_accuracy_events | 9270 |
| first_buzzer_team_replay_accuracy_events | 9270 |
| tossup_scorer_player_replay_accuracy_events | 9380 |
| tossup_scorer_team_replay_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 458 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.0293337 | 0.00644832 |
| Q1 (0-.2) | 179 | 0.432162 | 0.451279 |
| Q2 (.2-.4) | 957 | 0.27934 | 0.275524 |
| Q3 (.4-.6) | 2203 | 0.131134 | 0.130297 |
| Q4 (.6-.8) | 2978 | 0.00341178 | 0.00640843 |
| Q5 (.8-1) | 2953 | -0.125909 | -0.116861 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0222659 | 0.154547 | 0.723955 | 0.47829 |
| tossup_correctness | tier | fall | 2876 | 0.0335398 | 0.144719 | 0.731622 | 0.453764 |
| tossup_correctness | tier | nationals | 1579 | 0.0230621 | 0.174845 | 0.709053 | 0.527932 |
| tossup_correctness | tier | regionals | 1990 | 0.0241588 | 0.156005 | 0.73748 | 0.480727 |
| tossup_correctness | tier | winter | 2825 | 0.0310348 | 0.152178 | 0.714483 | 0.473794 |
| tossup_correctness | category | Current Events | 123 | 0.0977602 | 0.144613 | 0.803008 | 0.452364 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0266847 | 0.151099 | 0.735552 | 0.471101 |
| tossup_correctness | category | Geography | 191 | 0.0745719 | 0.158081 | 0.790832 | 0.488637 |
| tossup_correctness | category | History | 1469 | 0.0249427 | 0.165724 | 0.71283 | 0.50303 |
| tossup_correctness | category | Literature | 1436 | 0.0322994 | 0.13799 | 0.704213 | 0.439931 |
| tossup_correctness | category | Mythology | 325 | 0.0690162 | 0.133069 | 0.666452 | 0.427699 |
| tossup_correctness | category | Other Academic | 67 | 0.120015 | 0.161617 | 0.681941 | 0.498514 |
| tossup_correctness | category | Philosophy | 322 | 0.0403054 | 0.159557 | 0.684138 | 0.489664 |
| tossup_correctness | category | Popular Culture | 100 | 0.0604081 | 0.107008 | 0.545455 | 0.367774 |
| tossup_correctness | category | Religion | 365 | 0.0458976 | 0.185912 | 0.669067 | 0.554871 |
| tossup_correctness | category | Science | 1456 | 0.0321271 | 0.157695 | 0.71965 | 0.486382 |
| tossup_correctness | category | Social Science | 333 | 0.037717 | 0.161702 | 0.756241 | 0.495408 |
| tossup_correctness | category | Unknown | 1990 | 0.0241588 | 0.156005 | 0.73748 | 0.480727 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0551431 | 0.160511 | 0.765008 | 0.489424 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0339882 | 0.163034 | 0.709731 | 0.499009 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0221788 | 0.157147 | 0.727267 | 0.484355 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0305716 | 0.149218 | 0.7131 | 0.466863 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0185501 | 0.154868 | 0.731582 | 0.477899 |
