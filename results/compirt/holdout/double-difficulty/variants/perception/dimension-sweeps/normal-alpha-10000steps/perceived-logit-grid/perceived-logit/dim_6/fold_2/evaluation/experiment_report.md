# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.604728 |
| log_loss | 0.57677 |
| ece | 0.110685 |
| brier | 0.189964 |
| accuracy | 0.735443 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.028735 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.166988 |
| probability_p10 | 0.464851 |
| probability_p50 | 0.704046 |
| probability_p90 | 0.912666 |
| mean_predictive_variance | 0.185038 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.113913 |
| joint_tossup_event_log_loss | 6.88293 |
| buzz_position_mae | 0.185087 |
| buzz_position_median_absolute_error | 0.160257 |
| buzz_position_bias | -0.120277 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.390623 |
| first_buzzer_mean_reciprocal_rank | 0.595008 |
| first_buzzer_log_loss | 1.6041 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.656692 |
| tossup_scorer_player_top1_accuracy | 0.302239 |
| tossup_scorer_team_top1_accuracy | 0.452665 |
| tossup_game_winner_accuracy | 0.773913 |
| tossup_game_margin_mae | 41.9864 |
| tournament_player_ppg_spearman | 0.594879 |
| tournament_player_ppg_mae | 10.5956 |
| tournament_player_ppg_top10_overlap | 0.613793 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.604728 |
| neg_average_precision | 0.333286 |
| neg_precision | 0.396417 |
| neg_recall | 0.233165 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.102566 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0926452 |
| no_buzz_calibration_error | 0.0795322 |
| no_buzz_brier | 0.0278067 |
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
| overall | 9257 | -0.120277 | -0.125024 |
| Q1 (0-.2) | 183 | 0.308947 | 0.303556 |
| Q2 (.2-.4) | 955 | 0.143622 | 0.131964 |
| Q3 (.4-.6) | 2239 | -0.0145143 | -0.0240597 |
| Q4 (.6-.8) | 2875 | -0.142591 | -0.145126 |
| Q5 (.8-1) | 3005 | -0.287738 | -0.28446 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.110685 | 0.189964 | 0.604728 | 0.57677 |
| tossup_correctness | tier | fall | 2798 | 0.105356 | 0.177863 | 0.583372 | 0.556175 |
| tossup_correctness | tier | nationals | 1545 | 0.0987275 | 0.207811 | 0.62523 | 0.604145 |
| tossup_correctness | tier | regionals | 2039 | 0.110777 | 0.191569 | 0.614097 | 0.572291 |
| tossup_correctness | tier | winter | 2875 | 0.122821 | 0.19101 | 0.59086 | 0.58528 |
| tossup_correctness | category | Current Events | 129 | 0.215953 | 0.264415 | 0.435911 | 0.753318 |
| tossup_correctness | category | Fine Arts | 1074 | 0.12736 | 0.186535 | 0.611965 | 0.570721 |
| tossup_correctness | category | Geography | 180 | 0.108924 | 0.245744 | 0.569004 | 0.702355 |
| tossup_correctness | category | History | 1454 | 0.100912 | 0.189522 | 0.600414 | 0.573245 |
| tossup_correctness | category | Literature | 1435 | 0.12763 | 0.175146 | 0.563584 | 0.55344 |
| tossup_correctness | category | Mythology | 324 | 0.143927 | 0.186014 | 0.574714 | 0.565132 |
| tossup_correctness | category | Other Academic | 71 | 0.19319 | 0.240409 | 0.434641 | 0.693906 |
| tossup_correctness | category | Philosophy | 310 | 0.124947 | 0.194948 | 0.615094 | 0.593834 |
| tossup_correctness | category | Popular Culture | 108 | 0.22115 | 0.157111 | 0.568576 | 0.493 |
| tossup_correctness | category | Religion | 361 | 0.125802 | 0.196428 | 0.635973 | 0.595932 |
| tossup_correctness | category | Science | 1445 | 0.0800971 | 0.187668 | 0.638178 | 0.568024 |
| tossup_correctness | category | Social Science | 327 | 0.116279 | 0.200226 | 0.628677 | 0.618938 |
| tossup_correctness | category | Unknown | 2039 | 0.110777 | 0.191569 | 0.614097 | 0.572291 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.222261 | 0.238772 | 0.585889 | 0.683607 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.174993 | 0.232235 | 0.561205 | 0.668825 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.138674 | 0.199723 | 0.614114 | 0.594213 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.114997 | 0.178632 | 0.615516 | 0.548845 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0590013 | 0.177127 | 0.615977 | 0.55473 |
