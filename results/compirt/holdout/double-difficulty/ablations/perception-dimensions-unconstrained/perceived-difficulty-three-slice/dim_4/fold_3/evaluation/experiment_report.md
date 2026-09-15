# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.646764 |
| log_loss | 0.516335 |
| ece | 0.0267581 |
| brier | 0.167746 |
| accuracy | 0.773458 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0034141 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.122199 |
| probability_p10 | 0.599261 |
| probability_p50 | 0.784884 |
| probability_p90 | 0.906032 |
| mean_predictive_variance | 0.164432 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102719 |
| joint_tossup_event_log_loss | 6.85154 |
| buzz_position_mae | 0.163021 |
| buzz_position_median_absolute_error | 0.147837 |
| buzz_position_bias | -0.0744458 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.368833 |
| first_buzzer_mean_reciprocal_rank | 0.576325 |
| first_buzzer_log_loss | 1.65723 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.657159 |
| tossup_scorer_player_top1_accuracy | 0.327223 |
| tossup_scorer_team_top1_accuracy | 0.504121 |
| tossup_game_winner_accuracy | 0.800885 |
| tossup_game_margin_mae | 35.1611 |
| tournament_player_ppg_spearman | 0.707553 |
| tournament_player_ppg_mae | 8.74282 |
| tournament_player_ppg_top10_overlap | 0.672414 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.646764 |
| neg_average_precision | 0.37248 |
| neg_precision | 0.551495 |
| neg_recall | 0.0795019 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0540512 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0869659 |
| no_buzz_calibration_error | 0.0717815 |
| no_buzz_brier | 0.0244936 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| overall | 9080 | -0.0744458 | -0.0905377 |
| Q1 (0-.2) | 192 | 0.361569 | 0.358996 |
| Q2 (.2-.4) | 889 | 0.196272 | 0.196247 |
| Q3 (.4-.6) | 2210 | 0.0425437 | 0.0450224 |
| Q4 (.6-.8) | 2869 | -0.0982786 | -0.0933858 |
| Q5 (.8-1) | 2920 | -0.250663 | -0.250864 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0267581 | 0.167746 | 0.646764 | 0.516335 |
| tossup_correctness | tier | fall | 2817 | 0.0412555 | 0.165723 | 0.612967 | 0.514797 |
| tossup_correctness | tier | nationals | 1542 | 0.0587404 | 0.179486 | 0.702134 | 0.538812 |
| tossup_correctness | tier | regionals | 1934 | 0.0172162 | 0.173557 | 0.651735 | 0.526902 |
| tossup_correctness | tier | winter | 2787 | 0.028719 | 0.159263 | 0.640892 | 0.498118 |
| tossup_correctness | category | Current Events | 125 | 0.0821946 | 0.195791 | 0.639435 | 0.578031 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0357723 | 0.168769 | 0.640106 | 0.518394 |
| tossup_correctness | category | Geography | 185 | 0.0486441 | 0.172088 | 0.763357 | 0.518039 |
| tossup_correctness | category | History | 1443 | 0.0216282 | 0.164179 | 0.686763 | 0.504336 |
| tossup_correctness | category | Literature | 1411 | 0.0489114 | 0.152662 | 0.575478 | 0.491494 |
| tossup_correctness | category | Mythology | 320 | 0.0851647 | 0.165815 | 0.596099 | 0.516316 |
| tossup_correctness | category | Other Academic | 64 | 0.0951229 | 0.188036 | 0.561198 | 0.565485 |
| tossup_correctness | category | Philosophy | 312 | 0.0481226 | 0.160656 | 0.574774 | 0.505927 |
| tossup_correctness | category | Popular Culture | 104 | 0.114221 | 0.143639 | 0.524858 | 0.459376 |
| tossup_correctness | category | Religion | 358 | 0.0586519 | 0.193816 | 0.626413 | 0.579148 |
| tossup_correctness | category | Science | 1431 | 0.0350365 | 0.167614 | 0.664558 | 0.513782 |
| tossup_correctness | category | Social Science | 321 | 0.0267075 | 0.182331 | 0.651393 | 0.544018 |
| tossup_correctness | category | Unknown | 1934 | 0.0172162 | 0.173557 | 0.651735 | 0.526902 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0542209 | 0.191905 | 0.706511 | 0.566378 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0392155 | 0.184749 | 0.653665 | 0.553237 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0305376 | 0.177016 | 0.62256 | 0.539239 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0300927 | 0.158648 | 0.638687 | 0.495034 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0348169 | 0.162904 | 0.658541 | 0.505402 |
