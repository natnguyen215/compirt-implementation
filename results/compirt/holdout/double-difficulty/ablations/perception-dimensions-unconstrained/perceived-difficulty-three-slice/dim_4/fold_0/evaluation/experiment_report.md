# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.648582 |
| log_loss | 0.521603 |
| ece | 0.0186405 |
| brier | 0.170689 |
| accuracy | 0.764605 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000645508 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.120058 |
| probability_p10 | 0.594096 |
| probability_p50 | 0.784035 |
| probability_p90 | 0.897958 |
| mean_predictive_variance | 0.166704 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.108319 |
| joint_tossup_event_log_loss | 7.04682 |
| buzz_position_mae | 0.168114 |
| buzz_position_median_absolute_error | 0.151594 |
| buzz_position_bias | -0.0728031 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.360516 |
| first_buzzer_mean_reciprocal_rank | 0.570507 |
| first_buzzer_log_loss | 1.71734 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637332 |
| tossup_scorer_player_top1_accuracy | 0.316242 |
| tossup_scorer_team_top1_accuracy | 0.487049 |
| tossup_game_winner_accuracy | 0.788546 |
| tossup_game_margin_mae | 36.797 |
| tournament_player_ppg_spearman | 0.647807 |
| tournament_player_ppg_mae | 9.95674 |
| tournament_player_ppg_top10_overlap | 0.634483 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.648582 |
| neg_average_precision | 0.362559 |
| neg_precision | 0.490625 |
| neg_recall | 0.0719523 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0552965 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0902534 |
| no_buzz_calibration_error | 0.0769838 |
| no_buzz_brier | 0.0250225 |
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
| overall | 9295 | -0.0728031 | -0.0872884 |
| Q1 (0-.2) | 197 | 0.35809 | 0.364182 |
| Q2 (.2-.4) | 985 | 0.198835 | 0.200741 |
| Q3 (.4-.6) | 2251 | 0.0426713 | 0.0493727 |
| Q4 (.6-.8) | 2866 | -0.0982654 | -0.0894775 |
| Q5 (.8-1) | 2996 | -0.252845 | -0.247853 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0186405 | 0.170689 | 0.648582 | 0.521603 |
| tossup_correctness | tier | fall | 2933 | 0.0284895 | 0.157605 | 0.644553 | 0.491358 |
| tossup_correctness | tier | nationals | 1584 | 0.0282718 | 0.189403 | 0.642685 | 0.56277 |
| tossup_correctness | tier | regionals | 1886 | 0.0181213 | 0.182105 | 0.631992 | 0.546327 |
| tossup_correctness | tier | winter | 2892 | 0.0284524 | 0.166262 | 0.654906 | 0.513606 |
| tossup_correctness | category | Current Events | 124 | 0.0675185 | 0.169284 | 0.688866 | 0.520058 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0337072 | 0.177637 | 0.619843 | 0.542285 |
| tossup_correctness | category | Geography | 197 | 0.0409104 | 0.19382 | 0.722494 | 0.568903 |
| tossup_correctness | category | History | 1491 | 0.0223564 | 0.15679 | 0.676917 | 0.487106 |
| tossup_correctness | category | Literature | 1472 | 0.0264066 | 0.153363 | 0.620189 | 0.485207 |
| tossup_correctness | category | Mythology | 332 | 0.081492 | 0.14735 | 0.695818 | 0.463622 |
| tossup_correctness | category | Other Academic | 69 | 0.101998 | 0.19606 | 0.471719 | 0.586034 |
| tossup_correctness | category | Philosophy | 324 | 0.0471173 | 0.153254 | 0.642946 | 0.482288 |
| tossup_correctness | category | Popular Culture | 102 | 0.0892059 | 0.166363 | 0.447059 | 0.521517 |
| tossup_correctness | category | Religion | 372 | 0.0536111 | 0.193251 | 0.667088 | 0.569387 |
| tossup_correctness | category | Science | 1487 | 0.0310307 | 0.175735 | 0.649435 | 0.533015 |
| tossup_correctness | category | Social Science | 336 | 0.0551263 | 0.19699 | 0.66928 | 0.578897 |
| tossup_correctness | category | Unknown | 1886 | 0.0181213 | 0.182105 | 0.631992 | 0.546327 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0863359 | 0.196533 | 0.610212 | 0.586142 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0307051 | 0.187728 | 0.625913 | 0.561849 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0248537 | 0.16826 | 0.653542 | 0.515619 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0174539 | 0.160081 | 0.659198 | 0.495308 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.033642 | 0.17536 | 0.650955 | 0.533779 |
