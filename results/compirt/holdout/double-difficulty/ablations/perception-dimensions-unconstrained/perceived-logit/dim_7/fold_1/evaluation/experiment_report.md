# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.570207 |
| log_loss | 0.570985 |
| ece | 0.0754357 |
| brier | 0.185783 |
| accuracy | 0.759925 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00219949 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.117908 |
| probability_p10 | 0.623947 |
| probability_p50 | 0.844112 |
| probability_p90 | 0.925397 |
| mean_predictive_variance | 0.142267 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173274 |
| joint_tossup_event_log_loss | 7.68781 |
| buzz_position_mae | 0.330725 |
| buzz_position_median_absolute_error | 0.333973 |
| buzz_position_bias | -0.315921 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.312878 |
| first_buzzer_mean_reciprocal_rank | 0.53223 |
| first_buzzer_log_loss | 1.73568 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.618058 |
| tossup_scorer_player_top1_accuracy | 0.265801 |
| tossup_scorer_team_top1_accuracy | 0.379329 |
| tossup_game_winner_accuracy | 0.704955 |
| tossup_game_margin_mae | 43.9839 |
| tournament_player_ppg_spearman | 0.545262 |
| tournament_player_ppg_mae | 10.8268 |
| tournament_player_ppg_top10_overlap | 0.562069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.570207 |
| neg_average_precision | 0.298166 |
| neg_precision | 0.432432 |
| neg_recall | 0.0295885 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0347987 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.213133 |
| no_buzz_calibration_error | 0.197224 |
| no_buzz_brier | 0.0616194 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9093 | -0.315921 | -0.333954 |
| Q1 (0-.2) | 167 | 0.182744 | 0.173891 |
| Q2 (.2-.4) | 912 | 0.0212663 | 0.017477 |
| Q3 (.4-.6) | 2115 | -0.158372 | -0.160382 |
| Q4 (.6-.8) | 2844 | -0.337373 | -0.338445 |
| Q5 (.8-1) | 3055 | -0.532941 | -0.532684 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0754357 | 0.185783 | 0.570207 | 0.570985 |
| tossup_correctness | tier | fall | 2842 | 0.0653307 | 0.17144 | 0.576543 | 0.534163 |
| tossup_correctness | tier | nationals | 1564 | 0.0781724 | 0.207715 | 0.565127 | 0.609919 |
| tossup_correctness | tier | regionals | 1937 | 0.0810569 | 0.187889 | 0.552082 | 0.57779 |
| tossup_correctness | tier | winter | 2750 | 0.0891176 | 0.186648 | 0.559971 | 0.582104 |
| tossup_correctness | category | Current Events | 126 | 0.105444 | 0.192492 | 0.512975 | 0.580427 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0836325 | 0.182806 | 0.591518 | 0.563349 |
| tossup_correctness | category | Geography | 185 | 0.15868 | 0.232603 | 0.547619 | 0.687528 |
| tossup_correctness | category | History | 1440 | 0.0805915 | 0.190712 | 0.56397 | 0.581682 |
| tossup_correctness | category | Literature | 1422 | 0.0672894 | 0.155811 | 0.560243 | 0.501538 |
| tossup_correctness | category | Mythology | 318 | 0.0758085 | 0.169568 | 0.580841 | 0.528578 |
| tossup_correctness | category | Other Academic | 66 | 0.189515 | 0.238965 | 0.486002 | 0.698999 |
| tossup_correctness | category | Philosophy | 311 | 0.0977338 | 0.193193 | 0.587462 | 0.594199 |
| tossup_correctness | category | Popular Culture | 102 | 0.0645338 | 0.115511 | 0.55463 | 0.391133 |
| tossup_correctness | category | Religion | 358 | 0.121991 | 0.220047 | 0.564325 | 0.65577 |
| tossup_correctness | category | Science | 1433 | 0.0727913 | 0.196098 | 0.576837 | 0.592568 |
| tossup_correctness | category | Social Science | 324 | 0.0874607 | 0.199929 | 0.590911 | 0.603333 |
| tossup_correctness | category | Unknown | 1937 | 0.0810569 | 0.187889 | 0.552082 | 0.57779 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0786366 | 0.208079 | 0.578431 | 0.615456 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0782142 | 0.20053 | 0.574229 | 0.59793 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.087532 | 0.192636 | 0.541242 | 0.585192 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0656906 | 0.174148 | 0.576225 | 0.539928 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0836907 | 0.186248 | 0.574619 | 0.579588 |
