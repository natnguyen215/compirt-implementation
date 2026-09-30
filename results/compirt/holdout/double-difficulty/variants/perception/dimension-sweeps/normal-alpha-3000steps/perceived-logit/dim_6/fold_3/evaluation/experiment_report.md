# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.553538 |
| log_loss | 0.571831 |
| ece | 0.0850872 |
| brier | 0.183348 |
| accuracy | 0.769493 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000550661 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.116415 |
| probability_p10 | 0.640385 |
| probability_p50 | 0.855904 |
| probability_p90 | 0.934293 |
| mean_predictive_variance | 0.135135 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174892 |
| joint_tossup_event_log_loss | 7.69023 |
| buzz_position_mae | 0.332779 |
| buzz_position_median_absolute_error | 0.332347 |
| buzz_position_bias | -0.318017 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.334912 |
| first_buzzer_mean_reciprocal_rank | 0.549773 |
| first_buzzer_log_loss | 1.70598 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.627863 |
| tossup_scorer_player_top1_accuracy | 0.25987 |
| tossup_scorer_team_top1_accuracy | 0.410304 |
| tossup_game_winner_accuracy | 0.712389 |
| tossup_game_margin_mae | 47.2342 |
| tournament_player_ppg_spearman | 0.560641 |
| tournament_player_ppg_mae | 10.9088 |
| tournament_player_ppg_top10_overlap | 0.544828 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.553538 |
| neg_average_precision | 0.287364 |
| neg_precision | 0.48 |
| neg_recall | 0.0287356 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0326116 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.213868 |
| no_buzz_calibration_error | 0.198684 |
| no_buzz_brier | 0.0620756 |
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
| overall | 9080 | -0.318017 | -0.332347 |
| Q1 (0-.2) | 192 | 0.185749 | 0.181785 |
| Q2 (.2-.4) | 889 | 0.0126589 | 0.00712405 |
| Q3 (.4-.6) | 2210 | -0.16558 | -0.165915 |
| Q4 (.6-.8) | 2869 | -0.344458 | -0.343843 |
| Q5 (.8-1) | 2920 | -0.54121 | -0.541595 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0850872 | 0.183348 | 0.553538 | 0.571831 |
| tossup_correctness | tier | fall | 2817 | 0.0778814 | 0.178023 | 0.541892 | 0.557577 |
| tossup_correctness | tier | nationals | 1542 | 0.0684536 | 0.192926 | 0.608845 | 0.577575 |
| tossup_correctness | tier | regionals | 1934 | 0.107749 | 0.193766 | 0.528315 | 0.599486 |
| tossup_correctness | tier | winter | 2787 | 0.0868166 | 0.176201 | 0.531959 | 0.563868 |
| tossup_correctness | category | Current Events | 125 | 0.135895 | 0.216544 | 0.601658 | 0.63134 |
| tossup_correctness | category | Fine Arts | 1072 | 0.105235 | 0.18748 | 0.544851 | 0.586209 |
| tossup_correctness | category | Geography | 185 | 0.111865 | 0.206444 | 0.662378 | 0.614483 |
| tossup_correctness | category | History | 1443 | 0.0653759 | 0.18103 | 0.577161 | 0.560392 |
| tossup_correctness | category | Literature | 1411 | 0.0784126 | 0.159852 | 0.526183 | 0.521164 |
| tossup_correctness | category | Mythology | 320 | 0.0680803 | 0.172249 | 0.540444 | 0.54606 |
| tossup_correctness | category | Other Academic | 64 | 0.0737817 | 0.185085 | 0.640625 | 0.564199 |
| tossup_correctness | category | Philosophy | 312 | 0.119524 | 0.173235 | 0.474194 | 0.563062 |
| tossup_correctness | category | Popular Culture | 104 | 0.0636829 | 0.139737 | 0.488636 | 0.46429 |
| tossup_correctness | category | Religion | 358 | 0.115332 | 0.210107 | 0.578807 | 0.641249 |
| tossup_correctness | category | Science | 1431 | 0.071231 | 0.180571 | 0.581618 | 0.555888 |
| tossup_correctness | category | Social Science | 321 | 0.134695 | 0.211455 | 0.496887 | 0.647796 |
| tossup_correctness | category | Unknown | 1934 | 0.107749 | 0.193766 | 0.528315 | 0.599486 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.143743 | 0.227801 | 0.494725 | 0.670948 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0925657 | 0.202729 | 0.551254 | 0.608757 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0911883 | 0.194469 | 0.515867 | 0.598364 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0754695 | 0.169668 | 0.559871 | 0.535362 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0917569 | 0.179548 | 0.568736 | 0.569821 |
