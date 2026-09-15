# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.553633 |
| log_loss | 0.573001 |
| ece | 0.0806123 |
| brier | 0.181946 |
| accuracy | 0.773031 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.000323625 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.107555 |
| probability_p10 | 0.677108 |
| probability_p50 | 0.868294 |
| probability_p90 | 0.94181 |
| mean_predictive_variance | 0.125674 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173329 |
| joint_tossup_event_log_loss | 7.72993 |
| buzz_position_mae | 0.334384 |
| buzz_position_median_absolute_error | 0.33599 |
| buzz_position_bias | -0.320895 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.348759 |
| first_buzzer_mean_reciprocal_rank | 0.559539 |
| first_buzzer_log_loss | 1.68794 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.624703 |
| tossup_scorer_player_top1_accuracy | 0.258209 |
| tossup_scorer_team_top1_accuracy | 0.400959 |
| tossup_game_winner_accuracy | 0.700219 |
| tossup_game_margin_mae | 45.6982 |
| tournament_player_ppg_spearman | 0.594533 |
| tournament_player_ppg_mae | 10.8177 |
| tournament_player_ppg_top10_overlap | 0.610345 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.553633 |
| neg_average_precision | 0.279233 |
| neg_precision | 0.481013 |
| neg_recall | 0.0180866 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0310736 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.227207 |
| no_buzz_calibration_error | 0.21548 |
| no_buzz_brier | 0.0679452 |
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
| overall | 9270 | -0.320895 | -0.33599 |
| Q1 (0-.2) | 179 | 0.173566 | 0.170281 |
| Q2 (.2-.4) | 957 | 0.0126651 | 0.0116815 |
| Q3 (.4-.6) | 2203 | -0.169056 | -0.171556 |
| Q4 (.6-.8) | 2978 | -0.347809 | -0.347158 |
| Q5 (.8-1) | 2953 | -0.545099 | -0.546253 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0806123 | 0.181946 | 0.553633 | 0.573001 |
| tossup_correctness | tier | fall | 2876 | 0.0808684 | 0.17031 | 0.535535 | 0.544629 |
| tossup_correctness | tier | nationals | 1579 | 0.0723239 | 0.199309 | 0.583368 | 0.602013 |
| tossup_correctness | tier | regionals | 1990 | 0.0899834 | 0.189151 | 0.536174 | 0.590956 |
| tossup_correctness | tier | winter | 2825 | 0.0933996 | 0.17901 | 0.545381 | 0.573022 |
| tossup_correctness | category | Current Events | 123 | 0.0995783 | 0.177314 | 0.622157 | 0.543765 |
| tossup_correctness | category | Fine Arts | 1093 | 0.106307 | 0.186423 | 0.552847 | 0.59021 |
| tossup_correctness | category | Geography | 191 | 0.142996 | 0.221896 | 0.65511 | 0.652799 |
| tossup_correctness | category | History | 1469 | 0.0877075 | 0.189152 | 0.559442 | 0.586521 |
| tossup_correctness | category | Literature | 1436 | 0.0787489 | 0.157405 | 0.522936 | 0.519784 |
| tossup_correctness | category | Mythology | 325 | 0.0554878 | 0.132683 | 0.601188 | 0.4363 |
| tossup_correctness | category | Other Academic | 67 | 0.0914108 | 0.162333 | 0.572776 | 0.516496 |
| tossup_correctness | category | Philosophy | 322 | 0.114188 | 0.185909 | 0.469897 | 0.602676 |
| tossup_correctness | category | Popular Culture | 100 | 0.0506209 | 0.104994 | 0.588355 | 0.363559 |
| tossup_correctness | category | Religion | 365 | 0.137673 | 0.215239 | 0.588809 | 0.6608 |
| tossup_correctness | category | Science | 1456 | 0.0646132 | 0.181188 | 0.56719 | 0.565367 |
| tossup_correctness | category | Social Science | 333 | 0.128425 | 0.215143 | 0.514449 | 0.660232 |
| tossup_correctness | category | Unknown | 1990 | 0.0899834 | 0.189151 | 0.536174 | 0.590956 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0870363 | 0.190017 | 0.533167 | 0.590285 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.106465 | 0.198201 | 0.49054 | 0.610805 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0814593 | 0.186356 | 0.544133 | 0.577889 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0649489 | 0.169967 | 0.572336 | 0.539205 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0945173 | 0.184978 | 0.556877 | 0.590139 |
