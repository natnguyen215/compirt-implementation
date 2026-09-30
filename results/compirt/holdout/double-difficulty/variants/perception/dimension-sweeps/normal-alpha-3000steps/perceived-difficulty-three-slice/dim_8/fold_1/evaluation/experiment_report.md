# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.64712 |
| log_loss | 0.525094 |
| ece | 0.0189992 |
| brier | 0.171567 |
| accuracy | 0.765754 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00362917 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.115595 |
| probability_p10 | 0.61095 |
| probability_p50 | 0.793693 |
| probability_p90 | 0.906656 |
| mean_predictive_variance | 0.16188 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0997923 |
| joint_tossup_event_log_loss | 6.8861 |
| buzz_position_mae | 0.159799 |
| buzz_position_median_absolute_error | 0.145995 |
| buzz_position_bias | -0.065738 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34917 |
| first_buzzer_mean_reciprocal_rank | 0.563374 |
| first_buzzer_log_loss | 1.67218 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.643572 |
| tossup_scorer_player_top1_accuracy | 0.323377 |
| tossup_scorer_team_top1_accuracy | 0.491017 |
| tossup_game_winner_accuracy | 0.786036 |
| tossup_game_margin_mae | 33.7687 |
| tournament_player_ppg_spearman | 0.685349 |
| tournament_player_ppg_mae | 8.67677 |
| tournament_player_ppg_top10_overlap | 0.658621 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.64712 |
| neg_average_precision | 0.377277 |
| neg_precision | 0.578947 |
| neg_recall | 0.0559408 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0576997 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.103192 |
| no_buzz_calibration_error | 0.0872829 |
| no_buzz_brier | 0.0306008 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.065738 | -0.0839299 |
| Q1 (0-.2) | 167 | 0.36603 | 0.378902 |
| Q2 (.2-.4) | 912 | 0.209932 | 0.21574 |
| Q3 (.4-.6) | 2115 | 0.0554406 | 0.0557283 |
| Q4 (.6-.8) | 2844 | -0.082781 | -0.0797514 |
| Q5 (.8-1) | 3055 | -0.239662 | -0.238012 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0189992 | 0.171567 | 0.64712 | 0.525094 |
| tossup_correctness | tier | fall | 2842 | 0.0201256 | 0.156297 | 0.679684 | 0.486178 |
| tossup_correctness | tier | nationals | 1564 | 0.0448887 | 0.194635 | 0.634499 | 0.576816 |
| tossup_correctness | tier | regionals | 1937 | 0.0261562 | 0.176887 | 0.614816 | 0.53937 |
| tossup_correctness | tier | winter | 2750 | 0.0380318 | 0.170481 | 0.64017 | 0.525841 |
| tossup_correctness | category | Current Events | 126 | 0.0706232 | 0.175503 | 0.644152 | 0.530446 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0268863 | 0.168175 | 0.657929 | 0.515514 |
| tossup_correctness | category | Geography | 185 | 0.046168 | 0.183667 | 0.702658 | 0.549389 |
| tossup_correctness | category | History | 1440 | 0.018581 | 0.172315 | 0.670405 | 0.523599 |
| tossup_correctness | category | Literature | 1422 | 0.0462704 | 0.150793 | 0.592492 | 0.482187 |
| tossup_correctness | category | Mythology | 318 | 0.0542648 | 0.156491 | 0.679788 | 0.490651 |
| tossup_correctness | category | Other Academic | 66 | 0.0727297 | 0.206806 | 0.550952 | 0.605578 |
| tossup_correctness | category | Philosophy | 311 | 0.065377 | 0.179358 | 0.662593 | 0.541424 |
| tossup_correctness | category | Popular Culture | 102 | 0.0991086 | 0.115282 | 0.601852 | 0.391669 |
| tossup_correctness | category | Religion | 358 | 0.0519368 | 0.193849 | 0.664154 | 0.572586 |
| tossup_correctness | category | Science | 1433 | 0.0403775 | 0.180693 | 0.667047 | 0.54544 |
| tossup_correctness | category | Social Science | 324 | 0.0616162 | 0.183261 | 0.646249 | 0.551699 |
| tossup_correctness | category | Unknown | 1937 | 0.0261562 | 0.176887 | 0.614816 | 0.53937 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0723785 | 0.198447 | 0.601541 | 0.589605 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0201719 | 0.184717 | 0.658105 | 0.55452 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0165456 | 0.17298 | 0.657325 | 0.526201 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0226999 | 0.163992 | 0.638745 | 0.506795 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0300872 | 0.172245 | 0.645654 | 0.529052 |
