# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.564808 |
| log_loss | 0.561654 |
| ece | 0.072687 |
| brier | 0.182917 |
| accuracy | 0.764389 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000860678 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.116644 |
| probability_p10 | 0.618735 |
| probability_p50 | 0.826047 |
| probability_p90 | 0.916279 |
| mean_predictive_variance | 0.150767 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.169993 |
| joint_tossup_event_log_loss | 7.66949 |
| buzz_position_mae | 0.320297 |
| buzz_position_median_absolute_error | 0.317282 |
| buzz_position_bias | -0.303515 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.304142 |
| first_buzzer_mean_reciprocal_rank | 0.525616 |
| first_buzzer_log_loss | 1.74425 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.607746 |
| tossup_scorer_player_top1_accuracy | 0.260191 |
| tossup_scorer_team_top1_accuracy | 0.371338 |
| tossup_game_winner_accuracy | 0.69163 |
| tossup_game_margin_mae | 44.2948 |
| tournament_player_ppg_spearman | 0.533564 |
| tournament_player_ppg_mae | 10.89 |
| tournament_player_ppg_top10_overlap | 0.541379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.564808 |
| neg_average_precision | 0.300904 |
| neg_precision | 0.474359 |
| neg_recall | 0.0339138 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.036165 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.209186 |
| no_buzz_calibration_error | 0.195916 |
| no_buzz_brier | 0.0586578 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.303515 | -0.316736 |
| Q1 (0-.2) | 197 | 0.191581 | 0.185704 |
| Q2 (.2-.4) | 985 | 0.0213476 | 0.0137154 |
| Q3 (.4-.6) | 2251 | -0.155781 | -0.157231 |
| Q4 (.6-.8) | 2866 | -0.332481 | -0.331157 |
| Q5 (.8-1) | 2996 | -0.526164 | -0.525644 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.072687 | 0.182917 | 0.564808 | 0.561654 |
| tossup_correctness | tier | fall | 2933 | 0.061096 | 0.166143 | 0.569771 | 0.520368 |
| tossup_correctness | tier | nationals | 1584 | 0.0749143 | 0.199912 | 0.595078 | 0.592216 |
| tossup_correctness | tier | regionals | 1886 | 0.0915097 | 0.198321 | 0.524847 | 0.599589 |
| tossup_correctness | tier | winter | 2892 | 0.0732099 | 0.180575 | 0.552617 | 0.562048 |
| tossup_correctness | category | Current Events | 124 | 0.126545 | 0.189772 | 0.561568 | 0.569498 |
| tossup_correctness | category | Fine Arts | 1103 | 0.106844 | 0.193207 | 0.518827 | 0.596774 |
| tossup_correctness | category | Geography | 197 | 0.147242 | 0.230869 | 0.634149 | 0.665609 |
| tossup_correctness | category | History | 1491 | 0.061025 | 0.170964 | 0.569186 | 0.52843 |
| tossup_correctness | category | Literature | 1472 | 0.0666287 | 0.160071 | 0.563827 | 0.510833 |
| tossup_correctness | category | Mythology | 332 | 0.0908705 | 0.158141 | 0.558901 | 0.496999 |
| tossup_correctness | category | Other Academic | 69 | 0.1393 | 0.199749 | 0.514706 | 0.598418 |
| tossup_correctness | category | Philosophy | 324 | 0.0584926 | 0.155299 | 0.618117 | 0.490029 |
| tossup_correctness | category | Popular Culture | 102 | 0.135219 | 0.160899 | 0.389619 | 0.51205 |
| tossup_correctness | category | Religion | 372 | 0.092665 | 0.207959 | 0.612233 | 0.619505 |
| tossup_correctness | category | Science | 1487 | 0.0480636 | 0.180447 | 0.613584 | 0.55093 |
| tossup_correctness | category | Social Science | 336 | 0.116102 | 0.222716 | 0.543051 | 0.663543 |
| tossup_correctness | category | Unknown | 1886 | 0.0915097 | 0.198321 | 0.524847 | 0.599589 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0952133 | 0.206454 | 0.512599 | 0.608401 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0715168 | 0.197297 | 0.560514 | 0.590705 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0536779 | 0.176648 | 0.586376 | 0.540538 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0707972 | 0.172046 | 0.56839 | 0.533206 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0933909 | 0.191752 | 0.553193 | 0.592109 |
