# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.569059 |
| log_loss | 0.601421 |
| ece | 0.114961 |
| brier | 0.18699 |
| accuracy | 0.772816 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.000539374 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0803842 |
| probability_p10 | 0.789926 |
| probability_p50 | 0.901739 |
| probability_p90 | 0.959314 |
| mean_predictive_variance | 0.0971994 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172559 |
| joint_tossup_event_log_loss | 7.84346 |
| buzz_position_mae | 0.337116 |
| buzz_position_median_absolute_error | 0.340396 |
| buzz_position_bias | -0.324663 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.309061 |
| first_buzzer_mean_reciprocal_rank | 0.52467 |
| first_buzzer_log_loss | 1.76321 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.612621 |
| tossup_scorer_player_top1_accuracy | 0.248934 |
| tossup_scorer_team_top1_accuracy | 0.4258 |
| tossup_game_winner_accuracy | 0.724289 |
| tossup_game_margin_mae | 42.9532 |
| tournament_player_ppg_spearman | 0.633196 |
| tournament_player_ppg_mae | 10.2034 |
| tournament_player_ppg_top10_overlap | 0.634483 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.569059 |
| neg_average_precision | 0.27553 |
| neg_precision | 0.407407 |
| neg_recall | 0.0052356 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0292159 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.227944 |
| no_buzz_calibration_error | 0.216217 |
| no_buzz_brier | 0.0674018 |
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
| overall | 9270 | -0.324663 | -0.340396 |
| Q1 (0-.2) | 179 | 0.16973 | 0.168232 |
| Q2 (.2-.4) | 957 | 0.00674675 | 0.000293497 |
| Q3 (.4-.6) | 2203 | -0.171785 | -0.174038 |
| Q4 (.6-.8) | 2978 | -0.352191 | -0.351551 |
| Q5 (.8-1) | 2953 | -0.548322 | -0.550999 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.114961 | 0.18699 | 0.569059 | 0.601421 |
| tossup_correctness | tier | fall | 2876 | 0.0903138 | 0.171497 | 0.565083 | 0.556115 |
| tossup_correctness | tier | nationals | 1579 | 0.156387 | 0.218188 | 0.587155 | 0.687602 |
| tossup_correctness | tier | regionals | 1990 | 0.120227 | 0.193189 | 0.55647 | 0.620472 |
| tossup_correctness | tier | winter | 2825 | 0.116161 | 0.180957 | 0.57289 | 0.585955 |
| tossup_correctness | category | Current Events | 123 | 0.115128 | 0.189414 | 0.595011 | 0.595576 |
| tossup_correctness | category | Fine Arts | 1093 | 0.133104 | 0.191868 | 0.571042 | 0.621099 |
| tossup_correctness | category | Geography | 191 | 0.191142 | 0.231942 | 0.704802 | 0.691497 |
| tossup_correctness | category | History | 1469 | 0.123179 | 0.196508 | 0.580274 | 0.620863 |
| tossup_correctness | category | Literature | 1436 | 0.0966767 | 0.158484 | 0.55308 | 0.534998 |
| tossup_correctness | category | Mythology | 325 | 0.0574899 | 0.135819 | 0.581437 | 0.455214 |
| tossup_correctness | category | Other Academic | 67 | 0.102319 | 0.173457 | 0.586253 | 0.558261 |
| tossup_correctness | category | Philosophy | 322 | 0.124906 | 0.184666 | 0.501862 | 0.610557 |
| tossup_correctness | category | Popular Culture | 100 | 0.0387596 | 0.105383 | 0.496425 | 0.377452 |
| tossup_correctness | category | Religion | 365 | 0.165494 | 0.220991 | 0.596835 | 0.68947 |
| tossup_correctness | category | Science | 1456 | 0.107793 | 0.189406 | 0.559822 | 0.59924 |
| tossup_correctness | category | Social Science | 333 | 0.14201 | 0.219772 | 0.510562 | 0.696977 |
| tossup_correctness | category | Unknown | 1990 | 0.120227 | 0.193189 | 0.55647 | 0.620472 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.12263 | 0.195571 | 0.523217 | 0.629733 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.116595 | 0.201354 | 0.514605 | 0.638827 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.121307 | 0.191835 | 0.565575 | 0.608279 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.104671 | 0.174588 | 0.588224 | 0.564193 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.12664 | 0.190706 | 0.575006 | 0.620009 |
