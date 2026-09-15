# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.611071 |
| log_loss | 0.563457 |
| ece | 0.0993276 |
| brier | 0.185496 |
| accuracy | 0.743943 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0261013 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.16523 |
| probability_p10 | 0.474336 |
| probability_p50 | 0.713906 |
| probability_p90 | 0.909059 |
| mean_predictive_variance | 0.183116 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.114855 |
| joint_tossup_event_log_loss | 6.83702 |
| buzz_position_mae | 0.189555 |
| buzz_position_median_absolute_error | 0.165213 |
| buzz_position_bias | -0.126364 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.39207 |
| first_buzzer_mean_reciprocal_rank | 0.596708 |
| first_buzzer_log_loss | 1.59862 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.658921 |
| tossup_scorer_player_top1_accuracy | 0.300542 |
| tossup_scorer_team_top1_accuracy | 0.459328 |
| tossup_game_winner_accuracy | 0.774336 |
| tossup_game_margin_mae | 41.4372 |
| tournament_player_ppg_spearman | 0.593661 |
| tournament_player_ppg_mae | 10.8186 |
| tournament_player_ppg_top10_overlap | 0.634483 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.611071 |
| neg_average_precision | 0.326495 |
| neg_precision | 0.395225 |
| neg_recall | 0.21408 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0974807 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0916369 |
| no_buzz_calibration_error | 0.0764525 |
| no_buzz_brier | 0.0271094 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| overall | 9080 | -0.126364 | -0.132214 |
| Q1 (0-.2) | 192 | 0.308923 | 0.302335 |
| Q2 (.2-.4) | 889 | 0.141281 | 0.128318 |
| Q3 (.4-.6) | 2210 | -0.0183583 | -0.0288616 |
| Q4 (.6-.8) | 2869 | -0.150205 | -0.156616 |
| Q5 (.8-1) | 2920 | -0.29479 | -0.293765 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0993276 | 0.185496 | 0.611071 | 0.563457 |
| tossup_correctness | tier | fall | 2817 | 0.087827 | 0.175074 | 0.589491 | 0.548005 |
| tossup_correctness | tier | nationals | 1542 | 0.112472 | 0.207821 | 0.625237 | 0.603862 |
| tossup_correctness | tier | regionals | 1934 | 0.0981857 | 0.191858 | 0.627969 | 0.56699 |
| tossup_correctness | tier | winter | 2787 | 0.11189 | 0.179263 | 0.593396 | 0.554269 |
| tossup_correctness | category | Current Events | 125 | 0.110321 | 0.210209 | 0.586609 | 0.611422 |
| tossup_correctness | category | Fine Arts | 1072 | 0.113708 | 0.191707 | 0.578235 | 0.581073 |
| tossup_correctness | category | Geography | 185 | 0.0881306 | 0.209201 | 0.619161 | 0.612071 |
| tossup_correctness | category | History | 1443 | 0.0811275 | 0.180213 | 0.631052 | 0.547993 |
| tossup_correctness | category | Literature | 1411 | 0.128979 | 0.173636 | 0.591663 | 0.548283 |
| tossup_correctness | category | Mythology | 320 | 0.140628 | 0.185445 | 0.587032 | 0.569215 |
| tossup_correctness | category | Other Academic | 64 | 0.133577 | 0.172888 | 0.736979 | 0.520626 |
| tossup_correctness | category | Philosophy | 312 | 0.141624 | 0.185412 | 0.560323 | 0.571451 |
| tossup_correctness | category | Popular Culture | 104 | 0.184319 | 0.170777 | 0.509943 | 0.538444 |
| tossup_correctness | category | Religion | 358 | 0.112409 | 0.201856 | 0.590777 | 0.60442 |
| tossup_correctness | category | Science | 1431 | 0.0850432 | 0.178887 | 0.627337 | 0.547961 |
| tossup_correctness | category | Social Science | 321 | 0.114424 | 0.197651 | 0.591744 | 0.599397 |
| tossup_correctness | category | Unknown | 1934 | 0.0981857 | 0.191858 | 0.627969 | 0.56699 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.200974 | 0.241567 | 0.602934 | 0.683169 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.159518 | 0.217705 | 0.61406 | 0.630753 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.144978 | 0.20138 | 0.588192 | 0.601873 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.113151 | 0.1782 | 0.599925 | 0.545986 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0437327 | 0.167151 | 0.650391 | 0.523188 |
