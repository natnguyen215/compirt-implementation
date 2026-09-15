# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.624508 |
| log_loss | 0.534808 |
| ece | 0.0401774 |
| brier | 0.175125 |
| accuracy | 0.760409 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00484131 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.131828 |
| probability_p10 | 0.577509 |
| probability_p50 | 0.785159 |
| probability_p90 | 0.908936 |
| mean_predictive_variance | 0.164965 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.103709 |
| joint_tossup_event_log_loss | 6.97249 |
| buzz_position_mae | 0.162414 |
| buzz_position_median_absolute_error | 0.149089 |
| buzz_position_bias | -0.0649313 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.334158 |
| first_buzzer_mean_reciprocal_rank | 0.550878 |
| first_buzzer_log_loss | 1.70197 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.63206 |
| tossup_scorer_player_top1_accuracy | 0.303503 |
| tossup_scorer_team_top1_accuracy | 0.470276 |
| tossup_game_winner_accuracy | 0.788546 |
| tossup_game_margin_mae | 34.5952 |
| tournament_player_ppg_spearman | 0.679022 |
| tournament_player_ppg_mae | 9.13949 |
| tournament_player_ppg_top10_overlap | 0.648276 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.624508 |
| neg_average_precision | 0.341518 |
| neg_precision | 0.449664 |
| neg_recall | 0.0921173 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0574527 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0925886 |
| no_buzz_calibration_error | 0.079319 |
| no_buzz_brier | 0.0253783 |
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
| overall | 9295 | -0.0649313 | -0.0815579 |
| Q1 (0-.2) | 197 | 0.356508 | 0.358917 |
| Q2 (.2-.4) | 985 | 0.206414 | 0.203576 |
| Q3 (.4-.6) | 2251 | 0.0529313 | 0.0534555 |
| Q4 (.6-.8) | 2866 | -0.0912814 | -0.0863092 |
| Q5 (.8-1) | 2996 | -0.245201 | -0.241152 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0401774 | 0.175125 | 0.624508 | 0.534808 |
| tossup_correctness | tier | fall | 2933 | 0.0463888 | 0.164154 | 0.604106 | 0.512843 |
| tossup_correctness | tier | nationals | 1584 | 0.0588426 | 0.192884 | 0.643538 | 0.570856 |
| tossup_correctness | tier | regionals | 1886 | 0.0548955 | 0.187909 | 0.610513 | 0.563931 |
| tossup_correctness | tier | winter | 2892 | 0.032622 | 0.168189 | 0.63195 | 0.518347 |
| tossup_correctness | category | Current Events | 124 | 0.081465 | 0.187783 | 0.61984 | 0.558842 |
| tossup_correctness | category | Fine Arts | 1103 | 0.051085 | 0.180295 | 0.596244 | 0.551732 |
| tossup_correctness | category | Geography | 197 | 0.0520373 | 0.1985 | 0.700233 | 0.57949 |
| tossup_correctness | category | History | 1491 | 0.0620722 | 0.162715 | 0.654923 | 0.503185 |
| tossup_correctness | category | Literature | 1472 | 0.0498394 | 0.157416 | 0.595111 | 0.502072 |
| tossup_correctness | category | Mythology | 332 | 0.0885891 | 0.151226 | 0.686858 | 0.470675 |
| tossup_correctness | category | Other Academic | 69 | 0.157614 | 0.194356 | 0.5 | 0.58254 |
| tossup_correctness | category | Philosophy | 324 | 0.025117 | 0.152986 | 0.648946 | 0.481183 |
| tossup_correctness | category | Popular Culture | 102 | 0.170389 | 0.18914 | 0.468512 | 0.566028 |
| tossup_correctness | category | Religion | 372 | 0.0687497 | 0.198358 | 0.647832 | 0.585023 |
| tossup_correctness | category | Science | 1487 | 0.0369722 | 0.176938 | 0.652859 | 0.536659 |
| tossup_correctness | category | Social Science | 336 | 0.0513745 | 0.203695 | 0.604153 | 0.596456 |
| tossup_correctness | category | Unknown | 1886 | 0.0548955 | 0.187909 | 0.610513 | 0.563931 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0948208 | 0.206153 | 0.572414 | 0.60509 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0806039 | 0.197667 | 0.585265 | 0.587318 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0415843 | 0.174252 | 0.619152 | 0.531154 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0284352 | 0.161739 | 0.643635 | 0.501918 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0495161 | 0.179136 | 0.633871 | 0.547131 |
