# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.627578 |
| log_loss | 0.533894 |
| ece | 0.0308369 |
| brier | 0.17474 |
| accuracy | 0.762785 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.000659848 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.118471 |
| probability_p10 | 0.599659 |
| probability_p50 | 0.784401 |
| probability_p90 | 0.903517 |
| mean_predictive_variance | 0.165421 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102553 |
| joint_tossup_event_log_loss | 6.90317 |
| buzz_position_mae | 0.163734 |
| buzz_position_median_absolute_error | 0.149169 |
| buzz_position_bias | -0.0735155 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.356428 |
| first_buzzer_mean_reciprocal_rank | 0.566348 |
| first_buzzer_log_loss | 1.67132 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.643572 |
| tossup_scorer_player_top1_accuracy | 0.321753 |
| tossup_scorer_team_top1_accuracy | 0.486364 |
| tossup_game_winner_accuracy | 0.779279 |
| tossup_game_margin_mae | 35.4344 |
| tournament_player_ppg_spearman | 0.652266 |
| tournament_player_ppg_mae | 9.13518 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.627578 |
| neg_average_precision | 0.353803 |
| neg_precision | 0.511278 |
| neg_recall | 0.0628756 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0562188 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0922294 |
| no_buzz_calibration_error | 0.0763203 |
| no_buzz_brier | 0.0270267 |
| full_pmf_max_mass_error | 1.55431e-15 |
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
| overall | 9093 | -0.0735155 | -0.0913432 |
| Q1 (0-.2) | 167 | 0.363017 | 0.377269 |
| Q2 (.2-.4) | 912 | 0.204506 | 0.207343 |
| Q3 (.4-.6) | 2115 | 0.0519093 | 0.0525949 |
| Q4 (.6-.8) | 2844 | -0.0902746 | -0.0878922 |
| Q5 (.8-1) | 3055 | -0.251606 | -0.251917 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0308369 | 0.17474 | 0.627578 | 0.533894 |
| tossup_correctness | tier | fall | 2842 | 0.0319144 | 0.162766 | 0.626553 | 0.505302 |
| tossup_correctness | tier | nationals | 1564 | 0.0265247 | 0.193996 | 0.635268 | 0.57562 |
| tossup_correctness | tier | regionals | 1937 | 0.0236993 | 0.178523 | 0.614131 | 0.540238 |
| tossup_correctness | tier | winter | 2750 | 0.0434107 | 0.1735 | 0.623747 | 0.535245 |
| tossup_correctness | category | Current Events | 126 | 0.113007 | 0.18242 | 0.611091 | 0.549694 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0374912 | 0.171209 | 0.635035 | 0.525629 |
| tossup_correctness | category | Geography | 185 | 0.0548782 | 0.18414 | 0.712763 | 0.547858 |
| tossup_correctness | category | History | 1440 | 0.0328962 | 0.178832 | 0.630992 | 0.540469 |
| tossup_correctness | category | Literature | 1422 | 0.0518001 | 0.151894 | 0.575655 | 0.488866 |
| tossup_correctness | category | Mythology | 318 | 0.0818727 | 0.159392 | 0.68294 | 0.497736 |
| tossup_correctness | category | Other Academic | 66 | 0.106662 | 0.208626 | 0.548712 | 0.611204 |
| tossup_correctness | category | Philosophy | 311 | 0.078209 | 0.183409 | 0.639622 | 0.553329 |
| tossup_correctness | category | Popular Culture | 102 | 0.122666 | 0.123888 | 0.619444 | 0.409901 |
| tossup_correctness | category | Religion | 358 | 0.077263 | 0.201819 | 0.628403 | 0.594044 |
| tossup_correctness | category | Science | 1433 | 0.0308876 | 0.182031 | 0.644963 | 0.55133 |
| tossup_correctness | category | Social Science | 324 | 0.0599831 | 0.191216 | 0.594743 | 0.574118 |
| tossup_correctness | category | Unknown | 1937 | 0.0236993 | 0.178523 | 0.614131 | 0.540238 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0897193 | 0.204241 | 0.597164 | 0.601946 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0539424 | 0.189162 | 0.634958 | 0.567096 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0389294 | 0.177257 | 0.629159 | 0.537737 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0324657 | 0.167128 | 0.617986 | 0.515318 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0342911 | 0.174167 | 0.635355 | 0.534896 |
