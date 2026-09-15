# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.565726 |
| log_loss | 0.554689 |
| ece | 0.0754385 |
| brier | 0.179046 |
| accuracy | 0.771413 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00194175 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.117971 |
| probability_p10 | 0.628345 |
| probability_p50 | 0.838307 |
| probability_p90 | 0.925501 |
| mean_predictive_variance | 0.144474 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.171093 |
| joint_tossup_event_log_loss | 7.69399 |
| buzz_position_mae | 0.324712 |
| buzz_position_median_absolute_error | 0.323275 |
| buzz_position_bias | -0.309001 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.32233 |
| first_buzzer_mean_reciprocal_rank | 0.534798 |
| first_buzzer_log_loss | 1.74232 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.616397 |
| tossup_scorer_player_top1_accuracy | 0.249893 |
| tossup_scorer_team_top1_accuracy | 0.379851 |
| tossup_game_winner_accuracy | 0.695842 |
| tossup_game_margin_mae | 46.5282 |
| tournament_player_ppg_spearman | 0.556303 |
| tournament_player_ppg_mae | 11.1958 |
| tournament_player_ppg_top10_overlap | 0.596552 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.565726 |
| neg_average_precision | 0.28987 |
| neg_precision | 0.439189 |
| neg_recall | 0.0309376 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0348979 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.212155 |
| no_buzz_calibration_error | 0.200428 |
| no_buzz_brier | 0.0601302 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9270 | -0.309001 | -0.323238 |
| Q1 (0-.2) | 179 | 0.183983 | 0.180935 |
| Q2 (.2-.4) | 957 | 0.024386 | 0.02225 |
| Q3 (.4-.6) | 2203 | -0.158721 | -0.161398 |
| Q4 (.6-.8) | 2978 | -0.336418 | -0.336094 |
| Q5 (.8-1) | 2953 | -0.531389 | -0.530152 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0754385 | 0.179046 | 0.565726 | 0.554689 |
| tossup_correctness | tier | fall | 2876 | 0.0655237 | 0.168213 | 0.547628 | 0.531066 |
| tossup_correctness | tier | nationals | 1579 | 0.0779833 | 0.19706 | 0.601184 | 0.585459 |
| tossup_correctness | tier | regionals | 1990 | 0.0903057 | 0.186244 | 0.54224 | 0.572603 |
| tossup_correctness | tier | winter | 2825 | 0.0739357 | 0.174936 | 0.56233 | 0.548921 |
| tossup_correctness | category | Current Events | 123 | 0.0567445 | 0.172449 | 0.632795 | 0.527411 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0706208 | 0.181227 | 0.574604 | 0.562015 |
| tossup_correctness | category | Geography | 191 | 0.107098 | 0.207159 | 0.670647 | 0.609679 |
| tossup_correctness | category | History | 1469 | 0.0709917 | 0.185205 | 0.578008 | 0.566552 |
| tossup_correctness | category | Literature | 1436 | 0.0817722 | 0.15804 | 0.53194 | 0.512293 |
| tossup_correctness | category | Mythology | 325 | 0.0361691 | 0.132817 | 0.619794 | 0.432189 |
| tossup_correctness | category | Other Academic | 67 | 0.147985 | 0.164819 | 0.617251 | 0.51512 |
| tossup_correctness | category | Philosophy | 322 | 0.115674 | 0.183975 | 0.483015 | 0.581406 |
| tossup_correctness | category | Popular Culture | 100 | 0.0841064 | 0.114447 | 0.567926 | 0.38614 |
| tossup_correctness | category | Religion | 365 | 0.110636 | 0.207383 | 0.589821 | 0.627531 |
| tossup_correctness | category | Science | 1456 | 0.0636429 | 0.179358 | 0.579336 | 0.54984 |
| tossup_correctness | category | Social Science | 333 | 0.116103 | 0.208788 | 0.535391 | 0.626279 |
| tossup_correctness | category | Unknown | 1990 | 0.0903057 | 0.186244 | 0.54224 | 0.572603 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0938842 | 0.191011 | 0.532338 | 0.577959 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.090908 | 0.194855 | 0.50735 | 0.590952 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0738632 | 0.184253 | 0.54837 | 0.564115 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0636388 | 0.167992 | 0.583555 | 0.525086 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.083051 | 0.18046 | 0.574271 | 0.564349 |
