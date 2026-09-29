# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.672564 |
| log_loss | 0.501102 |
| ece | 0.0170649 |
| brier | 0.162478 |
| accuracy | 0.779935 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00658037 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.120247 |
| probability_p10 | 0.599298 |
| probability_p50 | 0.783532 |
| probability_p90 | 0.900842 |
| mean_predictive_variance | 0.165778 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0998792 |
| joint_tossup_event_log_loss | 6.85205 |
| buzz_position_mae | 0.15864 |
| buzz_position_median_absolute_error | 0.146058 |
| buzz_position_bias | -0.0634396 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.371197 |
| first_buzzer_mean_reciprocal_rank | 0.577652 |
| first_buzzer_log_loss | 1.65003 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.645847 |
| tossup_scorer_player_top1_accuracy | 0.326759 |
| tossup_scorer_team_top1_accuracy | 0.51194 |
| tossup_game_winner_accuracy | 0.814004 |
| tossup_game_margin_mae | 33.9986 |
| tournament_player_ppg_spearman | 0.699923 |
| tournament_player_ppg_mae | 9.05372 |
| tournament_player_ppg_top10_overlap | 0.675862 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.672564 |
| neg_average_precision | 0.393682 |
| neg_precision | 0.601329 |
| neg_recall | 0.0861495 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0553365 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0912841 |
| no_buzz_calibration_error | 0.079557 |
| no_buzz_brier | 0.0247176 |
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
| overall | 9270 | -0.0634396 | -0.0819799 |
| Q1 (0-.2) | 179 | 0.360276 | 0.365599 |
| Q2 (.2-.4) | 957 | 0.20841 | 0.204859 |
| Q3 (.4-.6) | 2203 | 0.0552337 | 0.0563079 |
| Q4 (.6-.8) | 2978 | -0.0867761 | -0.084497 |
| Q5 (.8-1) | 2953 | -0.242222 | -0.241517 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0170649 | 0.162478 | 0.672564 | 0.501102 |
| tossup_correctness | tier | fall | 2876 | 0.0163133 | 0.152799 | 0.673788 | 0.476818 |
| tossup_correctness | tier | nationals | 1579 | 0.0320425 | 0.182913 | 0.671718 | 0.548633 |
| tossup_correctness | tier | regionals | 1990 | 0.0442875 | 0.164186 | 0.700799 | 0.504194 |
| tossup_correctness | tier | winter | 2825 | 0.0308561 | 0.159707 | 0.663052 | 0.497081 |
| tossup_correctness | category | Current Events | 123 | 0.0770168 | 0.159235 | 0.739178 | 0.493747 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0183834 | 0.162666 | 0.683332 | 0.499887 |
| tossup_correctness | category | Geography | 191 | 0.0494018 | 0.17033 | 0.764381 | 0.519868 |
| tossup_correctness | category | History | 1469 | 0.0209011 | 0.170021 | 0.675356 | 0.518399 |
| tossup_correctness | category | Literature | 1436 | 0.0341074 | 0.14768 | 0.620054 | 0.470173 |
| tossup_correctness | category | Mythology | 325 | 0.0895777 | 0.138809 | 0.636611 | 0.446196 |
| tossup_correctness | category | Other Academic | 67 | 0.118827 | 0.171973 | 0.642857 | 0.525642 |
| tossup_correctness | category | Philosophy | 322 | 0.0421739 | 0.164831 | 0.625136 | 0.505959 |
| tossup_correctness | category | Popular Culture | 100 | 0.121836 | 0.123577 | 0.518897 | 0.41343 |
| tossup_correctness | category | Religion | 365 | 0.0589338 | 0.190971 | 0.660966 | 0.565313 |
| tossup_correctness | category | Science | 1456 | 0.0165737 | 0.162762 | 0.679113 | 0.501865 |
| tossup_correctness | category | Social Science | 333 | 0.0281693 | 0.177007 | 0.699177 | 0.532215 |
| tossup_correctness | category | Unknown | 1990 | 0.0442875 | 0.164186 | 0.700799 | 0.504194 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0968966 | 0.184802 | 0.600663 | 0.557041 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.041851 | 0.178551 | 0.630465 | 0.539876 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0280591 | 0.168215 | 0.654165 | 0.515721 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0188885 | 0.152443 | 0.691164 | 0.476596 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0231169 | 0.161756 | 0.685998 | 0.498954 |
