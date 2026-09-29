# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.569417 |
| log_loss | 0.54969 |
| ece | 0.0736273 |
| brier | 0.178227 |
| accuracy | 0.771845 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00151025 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.119483 |
| probability_p10 | 0.611868 |
| probability_p50 | 0.821652 |
| probability_p90 | 0.917394 |
| mean_predictive_variance | 0.152034 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.170773 |
| joint_tossup_event_log_loss | 7.68687 |
| buzz_position_mae | 0.321069 |
| buzz_position_median_absolute_error | 0.318942 |
| buzz_position_bias | -0.304448 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.312837 |
| first_buzzer_mean_reciprocal_rank | 0.525439 |
| first_buzzer_log_loss | 1.76588 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.612298 |
| tossup_scorer_player_top1_accuracy | 0.247655 |
| tossup_scorer_team_top1_accuracy | 0.376119 |
| tossup_game_winner_accuracy | 0.698031 |
| tossup_game_margin_mae | 46.9457 |
| tournament_player_ppg_spearman | 0.546148 |
| tournament_player_ppg_mae | 11.3521 |
| tournament_player_ppg_top10_overlap | 0.589655 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.569417 |
| neg_average_precision | 0.293136 |
| neg_precision | 0.457317 |
| neg_recall | 0.0356973 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0363515 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.206075 |
| no_buzz_calibration_error | 0.194348 |
| no_buzz_brier | 0.0572837 |
| full_pmf_max_mass_error | 9.99201e-16 |
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
| overall | 9270 | -0.304448 | -0.318686 |
| Q1 (0-.2) | 179 | 0.187648 | 0.183924 |
| Q2 (.2-.4) | 957 | 0.0286173 | 0.0266004 |
| Q3 (.4-.6) | 2203 | -0.154541 | -0.157354 |
| Q4 (.6-.8) | 2978 | -0.331893 | -0.33145 |
| Q5 (.8-1) | 2953 | -0.52637 | -0.524211 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0736273 | 0.178227 | 0.569417 | 0.54969 |
| tossup_correctness | tier | fall | 2876 | 0.0643525 | 0.167296 | 0.553943 | 0.526208 |
| tossup_correctness | tier | nationals | 1579 | 0.081877 | 0.197473 | 0.605907 | 0.584466 |
| tossup_correctness | tier | regionals | 1990 | 0.0892256 | 0.185943 | 0.54327 | 0.568825 |
| tossup_correctness | tier | winter | 2825 | 0.0683363 | 0.173161 | 0.565676 | 0.540679 |
| tossup_correctness | category | Current Events | 123 | 0.0575688 | 0.168921 | 0.658474 | 0.516921 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0661629 | 0.179158 | 0.581899 | 0.553216 |
| tossup_correctness | category | Geography | 191 | 0.0982279 | 0.203538 | 0.682075 | 0.596919 |
| tossup_correctness | category | History | 1469 | 0.0649408 | 0.183948 | 0.586684 | 0.559913 |
| tossup_correctness | category | Literature | 1436 | 0.082753 | 0.158749 | 0.529307 | 0.511314 |
| tossup_correctness | category | Mythology | 325 | 0.0506818 | 0.133689 | 0.614785 | 0.434589 |
| tossup_correctness | category | Other Academic | 67 | 0.0986364 | 0.167622 | 0.617251 | 0.519417 |
| tossup_correctness | category | Philosophy | 322 | 0.105944 | 0.182494 | 0.484619 | 0.573509 |
| tossup_correctness | category | Popular Culture | 100 | 0.0850614 | 0.115536 | 0.552605 | 0.389976 |
| tossup_correctness | category | Religion | 365 | 0.110746 | 0.205542 | 0.587384 | 0.618341 |
| tossup_correctness | category | Science | 1456 | 0.0640464 | 0.178658 | 0.583506 | 0.546478 |
| tossup_correctness | category | Social Science | 333 | 0.10569 | 0.205204 | 0.549017 | 0.611319 |
| tossup_correctness | category | Unknown | 1990 | 0.0892256 | 0.185943 | 0.54327 | 0.568825 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0743911 | 0.192456 | 0.530017 | 0.579774 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0913055 | 0.194341 | 0.5153 | 0.585964 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0737141 | 0.183411 | 0.553814 | 0.55901 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0639917 | 0.167285 | 0.587039 | 0.521206 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0782395 | 0.179309 | 0.576937 | 0.557882 |
