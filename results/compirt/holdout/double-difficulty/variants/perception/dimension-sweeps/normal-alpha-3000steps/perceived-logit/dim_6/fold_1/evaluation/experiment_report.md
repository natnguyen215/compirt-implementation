# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.567186 |
| log_loss | 0.580373 |
| ece | 0.0838063 |
| brier | 0.187521 |
| accuracy | 0.760145 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00197954 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.11583 |
| probability_p10 | 0.641898 |
| probability_p50 | 0.860649 |
| probability_p90 | 0.933745 |
| mean_predictive_variance | 0.133502 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173177 |
| joint_tossup_event_log_loss | 7.70704 |
| buzz_position_mae | 0.334126 |
| buzz_position_median_absolute_error | 0.338685 |
| buzz_position_bias | -0.320191 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.319586 |
| first_buzzer_mean_reciprocal_rank | 0.538646 |
| first_buzzer_log_loss | 1.71729 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.619488 |
| tossup_scorer_player_top1_accuracy | 0.269481 |
| tossup_scorer_team_top1_accuracy | 0.385065 |
| tossup_game_winner_accuracy | 0.720721 |
| tossup_game_margin_mae | 43.3735 |
| tournament_player_ppg_spearman | 0.560972 |
| tournament_player_ppg_mae | 10.5725 |
| tournament_player_ppg_top10_overlap | 0.565517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.567186 |
| neg_average_precision | 0.294803 |
| neg_precision | 0.425 |
| neg_recall | 0.0235784 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0333597 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.219975 |
| no_buzz_calibration_error | 0.204066 |
| no_buzz_brier | 0.0646807 |
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
| overall | 9093 | -0.320191 | -0.338598 |
| Q1 (0-.2) | 167 | 0.177943 | 0.166728 |
| Q2 (.2-.4) | 912 | 0.0173282 | 0.0132283 |
| Q3 (.4-.6) | 2115 | -0.161935 | -0.165225 |
| Q4 (.6-.8) | 2844 | -0.341351 | -0.342479 |
| Q5 (.8-1) | 3055 | -0.538043 | -0.540115 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0838063 | 0.187521 | 0.567186 | 0.580373 |
| tossup_correctness | tier | fall | 2842 | 0.074207 | 0.172984 | 0.568743 | 0.542134 |
| tossup_correctness | tier | nationals | 1564 | 0.0827602 | 0.208588 | 0.561387 | 0.615486 |
| tossup_correctness | tier | regionals | 1937 | 0.0813704 | 0.189396 | 0.549035 | 0.586776 |
| tossup_correctness | tier | winter | 2750 | 0.106538 | 0.189241 | 0.561047 | 0.595413 |
| tossup_correctness | category | Current Events | 126 | 0.0957285 | 0.193334 | 0.509421 | 0.588315 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0962558 | 0.184788 | 0.587747 | 0.574523 |
| tossup_correctness | category | Geography | 185 | 0.167387 | 0.236056 | 0.543605 | 0.704987 |
| tossup_correctness | category | History | 1440 | 0.0938826 | 0.193791 | 0.556502 | 0.594317 |
| tossup_correctness | category | Literature | 1422 | 0.0686625 | 0.156327 | 0.552608 | 0.507106 |
| tossup_correctness | category | Mythology | 318 | 0.087638 | 0.170741 | 0.584765 | 0.535691 |
| tossup_correctness | category | Other Academic | 66 | 0.230006 | 0.244119 | 0.486002 | 0.723376 |
| tossup_correctness | category | Philosophy | 311 | 0.121199 | 0.195781 | 0.58457 | 0.608018 |
| tossup_correctness | category | Popular Culture | 102 | 0.0413126 | 0.112827 | 0.581481 | 0.382747 |
| tossup_correctness | category | Religion | 358 | 0.147477 | 0.224013 | 0.568894 | 0.671073 |
| tossup_correctness | category | Science | 1433 | 0.0816064 | 0.196834 | 0.581674 | 0.5979 |
| tossup_correctness | category | Social Science | 324 | 0.0971964 | 0.203418 | 0.579951 | 0.619456 |
| tossup_correctness | category | Unknown | 1937 | 0.0813704 | 0.189396 | 0.549035 | 0.586776 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0912304 | 0.211505 | 0.56215 | 0.630893 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.078604 | 0.203192 | 0.569706 | 0.608207 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0974731 | 0.194524 | 0.532834 | 0.595229 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0737125 | 0.175496 | 0.573515 | 0.547258 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0892482 | 0.187877 | 0.573903 | 0.589846 |
