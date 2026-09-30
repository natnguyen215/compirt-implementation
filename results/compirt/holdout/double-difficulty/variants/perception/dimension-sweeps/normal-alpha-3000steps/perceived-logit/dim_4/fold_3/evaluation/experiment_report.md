# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.539079 |
| log_loss | 0.596175 |
| ece | 0.0962202 |
| brier | 0.187444 |
| accuracy | 0.769163 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000881057 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.101623 |
| probability_p10 | 0.700639 |
| probability_p50 | 0.882233 |
| probability_p90 | 0.947665 |
| mean_predictive_variance | 0.11601 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.175777 |
| joint_tossup_event_log_loss | 7.72459 |
| buzz_position_mae | 0.342079 |
| buzz_position_median_absolute_error | 0.344064 |
| buzz_position_bias | -0.329265 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.368833 |
| first_buzzer_mean_reciprocal_rank | 0.579789 |
| first_buzzer_log_loss | 1.6394 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.635242 |
| tossup_scorer_player_top1_accuracy | 0.263666 |
| tossup_scorer_team_top1_accuracy | 0.419089 |
| tossup_game_winner_accuracy | 0.699115 |
| tossup_game_margin_mae | 46.681 |
| tournament_player_ppg_spearman | 0.601576 |
| tournament_player_ppg_mae | 10.486 |
| tournament_player_ppg_top10_overlap | 0.593103 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.539079 |
| neg_average_precision | 0.271709 |
| neg_precision | 0.439394 |
| neg_recall | 0.0138889 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0288114 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.231462 |
| no_buzz_calibration_error | 0.216278 |
| no_buzz_brier | 0.07077 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| overall | 9080 | -0.329265 | -0.344064 |
| Q1 (0-.2) | 192 | 0.17379 | 0.172824 |
| Q2 (.2-.4) | 889 | 0.00207403 | -0.00310053 |
| Q3 (.4-.6) | 2210 | -0.176252 | -0.177207 |
| Q4 (.6-.8) | 2869 | -0.356472 | -0.355348 |
| Q5 (.8-1) | 2920 | -0.552295 | -0.555324 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0962202 | 0.187444 | 0.539079 | 0.596175 |
| tossup_correctness | tier | fall | 2817 | 0.0912015 | 0.180738 | 0.52839 | 0.571958 |
| tossup_correctness | tier | nationals | 1542 | 0.0833278 | 0.198862 | 0.592086 | 0.607189 |
| tossup_correctness | tier | regionals | 1934 | 0.109681 | 0.197628 | 0.531331 | 0.629518 |
| tossup_correctness | tier | winter | 2787 | 0.109761 | 0.180838 | 0.505031 | 0.591419 |
| tossup_correctness | category | Current Events | 125 | 0.151016 | 0.221636 | 0.623157 | 0.653269 |
| tossup_correctness | category | Fine Arts | 1072 | 0.114876 | 0.190584 | 0.538812 | 0.607174 |
| tossup_correctness | category | Geography | 185 | 0.144259 | 0.221721 | 0.584895 | 0.681679 |
| tossup_correctness | category | History | 1443 | 0.0795932 | 0.185881 | 0.56328 | 0.583194 |
| tossup_correctness | category | Literature | 1411 | 0.0835873 | 0.161708 | 0.496628 | 0.53727 |
| tossup_correctness | category | Mythology | 320 | 0.0884982 | 0.17235 | 0.532093 | 0.556411 |
| tossup_correctness | category | Other Academic | 64 | 0.155874 | 0.201397 | 0.596354 | 0.607419 |
| tossup_correctness | category | Philosophy | 312 | 0.121801 | 0.174281 | 0.463935 | 0.578534 |
| tossup_correctness | category | Popular Culture | 104 | 0.0680842 | 0.137822 | 0.509943 | 0.466765 |
| tossup_correctness | category | Religion | 358 | 0.151065 | 0.219632 | 0.538383 | 0.690598 |
| tossup_correctness | category | Science | 1431 | 0.0844328 | 0.185665 | 0.563739 | 0.578421 |
| tossup_correctness | category | Social Science | 321 | 0.154556 | 0.215846 | 0.502296 | 0.674623 |
| tossup_correctness | category | Unknown | 1934 | 0.109681 | 0.197628 | 0.531331 | 0.629518 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.137148 | 0.231239 | 0.493181 | 0.702019 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.108421 | 0.209073 | 0.517136 | 0.640083 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.1044 | 0.197933 | 0.499659 | 0.621461 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0847748 | 0.173129 | 0.546532 | 0.55458 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.102501 | 0.184105 | 0.557402 | 0.597578 |
