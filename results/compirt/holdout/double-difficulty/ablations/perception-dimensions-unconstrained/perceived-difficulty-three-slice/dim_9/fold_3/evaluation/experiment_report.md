# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.658743 |
| log_loss | 0.509377 |
| ece | 0.0170499 |
| brier | 0.165302 |
| accuracy | 0.77522 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00517621 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.112495 |
| probability_p10 | 0.618909 |
| probability_p50 | 0.793722 |
| probability_p90 | 0.901958 |
| mean_predictive_variance | 0.162257 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101248 |
| joint_tossup_event_log_loss | 6.83782 |
| buzz_position_mae | 0.161255 |
| buzz_position_median_absolute_error | 0.147217 |
| buzz_position_bias | -0.0706487 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.365419 |
| first_buzzer_mean_reciprocal_rank | 0.57425 |
| first_buzzer_log_loss | 1.65692 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.656938 |
| tossup_scorer_player_top1_accuracy | 0.329826 |
| tossup_scorer_team_top1_accuracy | 0.509436 |
| tossup_game_winner_accuracy | 0.763274 |
| tossup_game_margin_mae | 35.9874 |
| tournament_player_ppg_spearman | 0.698745 |
| tournament_player_ppg_mae | 8.9954 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.658743 |
| neg_average_precision | 0.392152 |
| neg_precision | 0.620513 |
| neg_recall | 0.0579502 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0541261 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0916621 |
| no_buzz_calibration_error | 0.0764777 |
| no_buzz_brier | 0.0261457 |
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
| overall | 9080 | -0.0706487 | -0.0890897 |
| Q1 (0-.2) | 192 | 0.366205 | 0.379913 |
| Q2 (.2-.4) | 889 | 0.198907 | 0.198235 |
| Q3 (.4-.6) | 2210 | 0.044494 | 0.0476406 |
| Q4 (.6-.8) | 2869 | -0.0949603 | -0.0904051 |
| Q5 (.8-1) | 2920 | -0.244699 | -0.246201 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0170499 | 0.165302 | 0.658743 | 0.509377 |
| tossup_correctness | tier | fall | 2817 | 0.0122368 | 0.160885 | 0.648473 | 0.498466 |
| tossup_correctness | tier | nationals | 1542 | 0.0569892 | 0.17869 | 0.708453 | 0.538483 |
| tossup_correctness | tier | regionals | 1934 | 0.0227541 | 0.173142 | 0.652603 | 0.52727 |
| tossup_correctness | tier | winter | 2787 | 0.0295668 | 0.156919 | 0.653189 | 0.491884 |
| tossup_correctness | category | Current Events | 125 | 0.078629 | 0.188353 | 0.700553 | 0.558621 |
| tossup_correctness | category | Fine Arts | 1072 | 0.023743 | 0.165495 | 0.659624 | 0.508071 |
| tossup_correctness | category | Geography | 185 | 0.0803774 | 0.168748 | 0.777762 | 0.511594 |
| tossup_correctness | category | History | 1443 | 0.0192528 | 0.161739 | 0.700673 | 0.497338 |
| tossup_correctness | category | Literature | 1411 | 0.0469018 | 0.152961 | 0.584876 | 0.487438 |
| tossup_correctness | category | Mythology | 320 | 0.0586339 | 0.15891 | 0.603734 | 0.500103 |
| tossup_correctness | category | Other Academic | 64 | 0.0690663 | 0.182966 | 0.595052 | 0.553569 |
| tossup_correctness | category | Philosophy | 312 | 0.0439231 | 0.15922 | 0.580968 | 0.499274 |
| tossup_correctness | category | Popular Culture | 104 | 0.110673 | 0.139228 | 0.519176 | 0.456469 |
| tossup_correctness | category | Religion | 358 | 0.0304162 | 0.185649 | 0.666994 | 0.55427 |
| tossup_correctness | category | Science | 1431 | 0.025376 | 0.164245 | 0.67834 | 0.50562 |
| tossup_correctness | category | Social Science | 321 | 0.0136102 | 0.175955 | 0.683233 | 0.530104 |
| tossup_correctness | category | Unknown | 1934 | 0.0227541 | 0.173142 | 0.652603 | 0.52727 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0597698 | 0.189908 | 0.700206 | 0.563207 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0252589 | 0.17856 | 0.680561 | 0.538122 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0199823 | 0.175817 | 0.625587 | 0.535355 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0188687 | 0.157332 | 0.645972 | 0.491055 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0304226 | 0.159521 | 0.678319 | 0.495426 |
