# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.631047 |
| log_loss | 0.565096 |
| ece | 0.124917 |
| brier | 0.190033 |
| accuracy | 0.72533 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0447137 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.15846 |
| probability_p10 | 0.433503 |
| probability_p50 | 0.662596 |
| probability_p90 | 0.846484 |
| mean_predictive_variance | 0.202678 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101954 |
| joint_tossup_event_log_loss | 6.62535 |
| buzz_position_mae | 0.166564 |
| buzz_position_median_absolute_error | 0.14642 |
| buzz_position_bias | -0.0876957 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.404736 |
| first_buzzer_mean_reciprocal_rank | 0.606423 |
| first_buzzer_log_loss | 1.57852 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.667952 |
| tossup_scorer_player_top1_accuracy | 0.296204 |
| tossup_scorer_team_top1_accuracy | 0.423861 |
| tossup_game_winner_accuracy | 0.800885 |
| tossup_game_margin_mae | 40.8861 |
| tournament_player_ppg_spearman | 0.646674 |
| tournament_player_ppg_mae | 11.1071 |
| tournament_player_ppg_top10_overlap | 0.672414 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.631047 |
| neg_average_precision | 0.342612 |
| neg_precision | 0.37682 |
| neg_recall | 0.297414 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0981215 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0734581 |
| no_buzz_calibration_error | 0.0582737 |
| no_buzz_brier | 0.0237132 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9080 | -0.0876957 | -0.0996475 |
| Q1 (0-.2) | 192 | 0.34654 | 0.341949 |
| Q2 (.2-.4) | 889 | 0.172492 | 0.168644 |
| Q3 (.4-.6) | 2210 | 0.0195327 | 0.0156409 |
| Q4 (.6-.8) | 2869 | -0.110961 | -0.110718 |
| Q5 (.8-1) | 2920 | -0.25376 | -0.250852 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.124917 | 0.190033 | 0.631047 | 0.565096 |
| tossup_correctness | tier | fall | 2817 | 0.0932917 | 0.176108 | 0.627029 | 0.534107 |
| tossup_correctness | tier | nationals | 1542 | 0.139493 | 0.210152 | 0.633983 | 0.608281 |
| tossup_correctness | tier | regionals | 1934 | 0.129496 | 0.196481 | 0.633441 | 0.577755 |
| tossup_correctness | tier | winter | 2787 | 0.146086 | 0.188503 | 0.621512 | 0.56374 |
| tossup_correctness | category | Current Events | 125 | 0.0762645 | 0.199047 | 0.621314 | 0.586122 |
| tossup_correctness | category | Fine Arts | 1072 | 0.146939 | 0.20208 | 0.591045 | 0.590675 |
| tossup_correctness | category | Geography | 185 | 0.0914545 | 0.205901 | 0.652028 | 0.595921 |
| tossup_correctness | category | History | 1443 | 0.102539 | 0.181447 | 0.659458 | 0.543765 |
| tossup_correctness | category | Literature | 1411 | 0.15833 | 0.181128 | 0.621407 | 0.547443 |
| tossup_correctness | category | Mythology | 320 | 0.163159 | 0.203604 | 0.552195 | 0.601175 |
| tossup_correctness | category | Other Academic | 64 | 0.166353 | 0.196802 | 0.677083 | 0.576984 |
| tossup_correctness | category | Philosophy | 312 | 0.167162 | 0.192158 | 0.597484 | 0.57285 |
| tossup_correctness | category | Popular Culture | 104 | 0.238107 | 0.198457 | 0.480824 | 0.59816 |
| tossup_correctness | category | Religion | 358 | 0.0986312 | 0.191345 | 0.670487 | 0.569278 |
| tossup_correctness | category | Science | 1431 | 0.0989501 | 0.180704 | 0.651204 | 0.544782 |
| tossup_correctness | category | Social Science | 321 | 0.100242 | 0.196505 | 0.636391 | 0.580241 |
| tossup_correctness | category | Unknown | 1934 | 0.129496 | 0.196481 | 0.633441 | 0.577755 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.250239 | 0.258617 | 0.663664 | 0.715691 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.215773 | 0.235249 | 0.645414 | 0.663704 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.165789 | 0.206932 | 0.62757 | 0.603231 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.129902 | 0.181577 | 0.619205 | 0.546607 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0562677 | 0.167276 | 0.660661 | 0.514476 |
