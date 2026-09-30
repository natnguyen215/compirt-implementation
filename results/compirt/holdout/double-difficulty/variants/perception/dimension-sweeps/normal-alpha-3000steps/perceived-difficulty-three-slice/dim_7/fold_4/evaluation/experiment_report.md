# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.655466 |
| log_loss | 0.50736 |
| ece | 0.01733 |
| brier | 0.164666 |
| accuracy | 0.778209 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00485437 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.116797 |
| probability_p10 | 0.612619 |
| probability_p50 | 0.799634 |
| probability_p90 | 0.904204 |
| mean_predictive_variance | 0.16021 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100632 |
| joint_tossup_event_log_loss | 6.90319 |
| buzz_position_mae | 0.158989 |
| buzz_position_median_absolute_error | 0.146034 |
| buzz_position_bias | -0.0633157 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.358037 |
| first_buzzer_mean_reciprocal_rank | 0.566061 |
| first_buzzer_log_loss | 1.67865 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.644444 |
| tossup_scorer_player_top1_accuracy | 0.323348 |
| tossup_scorer_team_top1_accuracy | 0.502452 |
| tossup_game_winner_accuracy | 0.798687 |
| tossup_game_margin_mae | 33.4436 |
| tournament_player_ppg_spearman | 0.701712 |
| tournament_player_ppg_mae | 9.01218 |
| tournament_player_ppg_top10_overlap | 0.67931 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.655466 |
| neg_average_precision | 0.375829 |
| neg_precision | 0.585551 |
| neg_recall | 0.0732984 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0559948 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0956378 |
| no_buzz_calibration_error | 0.0839107 |
| no_buzz_brier | 0.0263399 |
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
| overall | 9270 | -0.0633157 | -0.0801442 |
| Q1 (0-.2) | 179 | 0.359476 | 0.359495 |
| Q2 (.2-.4) | 957 | 0.205289 | 0.203696 |
| Q3 (.4-.6) | 2203 | 0.0552709 | 0.0571554 |
| Q4 (.6-.8) | 2978 | -0.0862014 | -0.0811052 |
| Q5 (.8-1) | 2953 | -0.241381 | -0.239986 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.01733 | 0.164666 | 0.655466 | 0.50736 |
| tossup_correctness | tier | fall | 2876 | 0.0317804 | 0.158191 | 0.629938 | 0.494279 |
| tossup_correctness | tier | nationals | 1579 | 0.0596778 | 0.185638 | 0.668836 | 0.555378 |
| tossup_correctness | tier | regionals | 1990 | 0.0140249 | 0.16539 | 0.676601 | 0.507171 |
| tossup_correctness | tier | winter | 2825 | 0.0264491 | 0.159025 | 0.666234 | 0.493971 |
| tossup_correctness | category | Current Events | 123 | 0.0565383 | 0.168115 | 0.669479 | 0.516116 |
| tossup_correctness | category | Fine Arts | 1093 | 0.038222 | 0.168129 | 0.644329 | 0.515491 |
| tossup_correctness | category | Geography | 191 | 0.0544729 | 0.178142 | 0.753595 | 0.534166 |
| tossup_correctness | category | History | 1469 | 0.0217829 | 0.170035 | 0.676137 | 0.517014 |
| tossup_correctness | category | Literature | 1436 | 0.0418219 | 0.150733 | 0.589324 | 0.481398 |
| tossup_correctness | category | Mythology | 325 | 0.0912991 | 0.140386 | 0.623587 | 0.450917 |
| tossup_correctness | category | Other Academic | 67 | 0.120572 | 0.178738 | 0.592992 | 0.542722 |
| tossup_correctness | category | Philosophy | 322 | 0.0326325 | 0.16566 | 0.615627 | 0.510748 |
| tossup_correctness | category | Popular Culture | 100 | 0.114516 | 0.120964 | 0.517875 | 0.40663 |
| tossup_correctness | category | Religion | 365 | 0.0470391 | 0.191278 | 0.657141 | 0.568238 |
| tossup_correctness | category | Science | 1456 | 0.029247 | 0.164597 | 0.662439 | 0.507504 |
| tossup_correctness | category | Social Science | 333 | 0.0250131 | 0.180518 | 0.684179 | 0.540148 |
| tossup_correctness | category | Unknown | 1990 | 0.0140249 | 0.16539 | 0.676601 | 0.507171 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0695318 | 0.180776 | 0.627197 | 0.545469 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0450282 | 0.179793 | 0.613986 | 0.543426 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0180582 | 0.168531 | 0.651663 | 0.515739 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0191951 | 0.155596 | 0.665241 | 0.484889 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0261752 | 0.165049 | 0.661426 | 0.509772 |
