# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.545439 |
| log_loss | 0.583902 |
| ece | 0.0886575 |
| brier | 0.185395 |
| accuracy | 0.769824 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000220264 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.111331 |
| probability_p10 | 0.66526 |
| probability_p50 | 0.871392 |
| probability_p90 | 0.941716 |
| mean_predictive_variance | 0.125296 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.175292 |
| joint_tossup_event_log_loss | 7.71366 |
| buzz_position_mae | 0.33756 |
| buzz_position_median_absolute_error | 0.337853 |
| buzz_position_bias | -0.323793 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.353304 |
| first_buzzer_mean_reciprocal_rank | 0.564725 |
| first_buzzer_log_loss | 1.67987 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.634471 |
| tossup_scorer_player_top1_accuracy | 0.261388 |
| tossup_scorer_team_top1_accuracy | 0.41551 |
| tossup_game_winner_accuracy | 0.719027 |
| tossup_game_margin_mae | 46.7183 |
| tournament_player_ppg_spearman | 0.594757 |
| tournament_player_ppg_mae | 10.6414 |
| tournament_player_ppg_top10_overlap | 0.586207 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.545439 |
| neg_average_precision | 0.279314 |
| neg_precision | 0.491228 |
| neg_recall | 0.0268199 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0307124 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.223176 |
| no_buzz_calibration_error | 0.207992 |
| no_buzz_brier | 0.0664536 |
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
| overall | 9080 | -0.323793 | -0.337853 |
| Q1 (0-.2) | 192 | 0.180223 | 0.178481 |
| Q2 (.2-.4) | 889 | 0.00749879 | 0.00118494 |
| Q3 (.4-.6) | 2210 | -0.170874 | -0.172216 |
| Q4 (.6-.8) | 2869 | -0.350654 | -0.349519 |
| Q5 (.8-1) | 2920 | -0.547141 | -0.549668 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0886575 | 0.185395 | 0.545439 | 0.583902 |
| tossup_correctness | tier | fall | 2817 | 0.0834253 | 0.179202 | 0.534956 | 0.56431 |
| tossup_correctness | tier | nationals | 1542 | 0.0551076 | 0.193934 | 0.60217 | 0.584068 |
| tossup_correctness | tier | regionals | 1934 | 0.104212 | 0.195791 | 0.526177 | 0.615035 |
| tossup_correctness | tier | winter | 2787 | 0.103005 | 0.179716 | 0.51549 | 0.582009 |
| tossup_correctness | category | Current Events | 125 | 0.144234 | 0.22154 | 0.587224 | 0.652369 |
| tossup_correctness | category | Fine Arts | 1072 | 0.105941 | 0.189136 | 0.539388 | 0.597839 |
| tossup_correctness | category | Geography | 185 | 0.130452 | 0.217086 | 0.611049 | 0.652731 |
| tossup_correctness | category | History | 1443 | 0.0717336 | 0.18478 | 0.559475 | 0.575882 |
| tossup_correctness | category | Literature | 1411 | 0.0758969 | 0.159516 | 0.523458 | 0.52433 |
| tossup_correctness | category | Mythology | 320 | 0.087719 | 0.172355 | 0.542293 | 0.550433 |
| tossup_correctness | category | Other Academic | 64 | 0.108968 | 0.189351 | 0.638021 | 0.570313 |
| tossup_correctness | category | Philosophy | 312 | 0.113269 | 0.174762 | 0.46071 | 0.57387 |
| tossup_correctness | category | Popular Culture | 104 | 0.0674029 | 0.139425 | 0.489347 | 0.470505 |
| tossup_correctness | category | Religion | 358 | 0.137135 | 0.213408 | 0.569898 | 0.660649 |
| tossup_correctness | category | Science | 1431 | 0.0739169 | 0.182364 | 0.5733 | 0.565283 |
| tossup_correctness | category | Social Science | 321 | 0.13213 | 0.214153 | 0.494438 | 0.661342 |
| tossup_correctness | category | Unknown | 1934 | 0.104212 | 0.195791 | 0.526177 | 0.615035 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.153216 | 0.231338 | 0.485203 | 0.69037 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0961672 | 0.206539 | 0.533257 | 0.626966 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0939106 | 0.195975 | 0.510159 | 0.608808 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0740138 | 0.171158 | 0.554039 | 0.543503 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0989513 | 0.181917 | 0.557682 | 0.584635 |
