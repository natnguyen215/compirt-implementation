# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.657519 |
| log_loss | 0.506173 |
| ece | 0.0124195 |
| brier | 0.164379 |
| accuracy | 0.778425 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00507012 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.107484 |
| probability_p10 | 0.630155 |
| probability_p50 | 0.791324 |
| probability_p90 | 0.900368 |
| mean_predictive_variance | 0.162591 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102895 |
| joint_tossup_event_log_loss | 6.95287 |
| buzz_position_mae | 0.163301 |
| buzz_position_median_absolute_error | 0.149288 |
| buzz_position_bias | -0.0680206 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349838 |
| first_buzzer_mean_reciprocal_rank | 0.559855 |
| first_buzzer_log_loss | 1.69688 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.645955 |
| tossup_scorer_player_top1_accuracy | 0.317271 |
| tossup_scorer_team_top1_accuracy | 0.510128 |
| tossup_game_winner_accuracy | 0.809628 |
| tossup_game_margin_mae | 34.5248 |
| tournament_player_ppg_spearman | 0.69436 |
| tournament_player_ppg_mae | 9.2836 |
| tournament_player_ppg_top10_overlap | 0.668966 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.657519 |
| neg_average_precision | 0.377359 |
| neg_precision | 0.645963 |
| neg_recall | 0.0495002 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0543423 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0902407 |
| no_buzz_calibration_error | 0.0785136 |
| no_buzz_brier | 0.024455 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0680206 | -0.0845718 |
| Q1 (0-.2) | 179 | 0.362376 | 0.365098 |
| Q2 (.2-.4) | 957 | 0.209451 | 0.209405 |
| Q3 (.4-.6) | 2203 | 0.0550283 | 0.0598435 |
| Q4 (.6-.8) | 2978 | -0.091531 | -0.087086 |
| Q5 (.8-1) | 2953 | -0.25212 | -0.251085 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0124195 | 0.164379 | 0.657519 | 0.506173 |
| tossup_correctness | tier | fall | 2876 | 0.0187226 | 0.154136 | 0.661545 | 0.481491 |
| tossup_correctness | tier | nationals | 1579 | 0.0234195 | 0.183806 | 0.665096 | 0.549885 |
| tossup_correctness | tier | regionals | 1990 | 0.0481374 | 0.166942 | 0.676114 | 0.512197 |
| tossup_correctness | tier | winter | 2825 | 0.0303806 | 0.162142 | 0.645887 | 0.502627 |
| tossup_correctness | category | Current Events | 123 | 0.0721483 | 0.16357 | 0.69369 | 0.506371 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0313664 | 0.167427 | 0.658414 | 0.512863 |
| tossup_correctness | category | Geography | 191 | 0.0786683 | 0.174715 | 0.772984 | 0.525539 |
| tossup_correctness | category | History | 1469 | 0.0307384 | 0.170162 | 0.685582 | 0.517359 |
| tossup_correctness | category | Literature | 1436 | 0.0395194 | 0.149079 | 0.602375 | 0.475251 |
| tossup_correctness | category | Mythology | 325 | 0.0787526 | 0.134376 | 0.640117 | 0.437189 |
| tossup_correctness | category | Other Academic | 67 | 0.0914685 | 0.174662 | 0.557951 | 0.532778 |
| tossup_correctness | category | Philosophy | 322 | 0.0395861 | 0.164115 | 0.62084 | 0.507382 |
| tossup_correctness | category | Popular Culture | 100 | 0.107232 | 0.117322 | 0.52094 | 0.397843 |
| tossup_correctness | category | Religion | 365 | 0.0660323 | 0.193303 | 0.652715 | 0.571877 |
| tossup_correctness | category | Science | 1456 | 0.0111933 | 0.165416 | 0.668811 | 0.507158 |
| tossup_correctness | category | Social Science | 333 | 0.0362939 | 0.17925 | 0.693599 | 0.538054 |
| tossup_correctness | category | Unknown | 1990 | 0.0481374 | 0.166942 | 0.676114 | 0.512197 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0676029 | 0.181957 | 0.6 | 0.549872 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0425841 | 0.180245 | 0.609436 | 0.545044 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0179059 | 0.168756 | 0.647294 | 0.516531 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0169879 | 0.154384 | 0.6765 | 0.480765 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0255988 | 0.164986 | 0.666766 | 0.508824 |
