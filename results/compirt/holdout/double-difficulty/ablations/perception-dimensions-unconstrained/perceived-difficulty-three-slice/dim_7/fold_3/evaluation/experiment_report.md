# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.666783 |
| log_loss | 0.506155 |
| ece | 0.0192047 |
| brier | 0.164024 |
| accuracy | 0.776322 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00627753 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.119976 |
| probability_p10 | 0.597189 |
| probability_p50 | 0.786776 |
| probability_p90 | 0.89836 |
| mean_predictive_variance | 0.165894 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101744 |
| joint_tossup_event_log_loss | 6.85266 |
| buzz_position_mae | 0.162025 |
| buzz_position_median_absolute_error | 0.146761 |
| buzz_position_bias | -0.0719973 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.359471 |
| first_buzzer_mean_reciprocal_rank | 0.569369 |
| first_buzzer_log_loss | 1.67532 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.653084 |
| tossup_scorer_player_top1_accuracy | 0.318655 |
| tossup_scorer_team_top1_accuracy | 0.510954 |
| tossup_game_winner_accuracy | 0.774336 |
| tossup_game_margin_mae | 36.215 |
| tournament_player_ppg_spearman | 0.710116 |
| tournament_player_ppg_mae | 8.86881 |
| tournament_player_ppg_top10_overlap | 0.655172 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.666783 |
| neg_average_precision | 0.403568 |
| neg_precision | 0.59164 |
| neg_recall | 0.0881226 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0537725 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0896999 |
| no_buzz_calibration_error | 0.0745155 |
| no_buzz_brier | 0.0254884 |
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
| overall | 9080 | -0.0719973 | -0.0902138 |
| Q1 (0-.2) | 192 | 0.370494 | 0.37631 |
| Q2 (.2-.4) | 889 | 0.198536 | 0.198743 |
| Q3 (.4-.6) | 2210 | 0.0436814 | 0.0465307 |
| Q4 (.6-.8) | 2869 | -0.0970971 | -0.092752 |
| Q5 (.8-1) | 2920 | -0.246347 | -0.246177 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0192047 | 0.164024 | 0.666783 | 0.506155 |
| tossup_correctness | tier | fall | 2817 | 0.017278 | 0.158304 | 0.666134 | 0.492077 |
| tossup_correctness | tier | nationals | 1542 | 0.0613967 | 0.178403 | 0.708261 | 0.537728 |
| tossup_correctness | tier | regionals | 1934 | 0.0275191 | 0.173708 | 0.652131 | 0.528791 |
| tossup_correctness | tier | winter | 2787 | 0.0263137 | 0.155131 | 0.660021 | 0.487209 |
| tossup_correctness | category | Current Events | 125 | 0.0673681 | 0.185018 | 0.709152 | 0.54951 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0286875 | 0.163174 | 0.67429 | 0.502097 |
| tossup_correctness | category | Geography | 185 | 0.0790714 | 0.165441 | 0.780979 | 0.504572 |
| tossup_correctness | category | History | 1443 | 0.0405533 | 0.15983 | 0.715321 | 0.493095 |
| tossup_correctness | category | Literature | 1411 | 0.0454975 | 0.151992 | 0.589884 | 0.484926 |
| tossup_correctness | category | Mythology | 320 | 0.0604115 | 0.15933 | 0.603675 | 0.501722 |
| tossup_correctness | category | Other Academic | 64 | 0.090558 | 0.184916 | 0.602865 | 0.55592 |
| tossup_correctness | category | Philosophy | 312 | 0.0545792 | 0.157802 | 0.596 | 0.495505 |
| tossup_correctness | category | Popular Culture | 104 | 0.106922 | 0.138552 | 0.514915 | 0.454741 |
| tossup_correctness | category | Religion | 358 | 0.0207924 | 0.181583 | 0.687794 | 0.542967 |
| tossup_correctness | category | Science | 1431 | 0.0199165 | 0.162828 | 0.687315 | 0.50147 |
| tossup_correctness | category | Social Science | 321 | 0.0406075 | 0.171835 | 0.701755 | 0.520728 |
| tossup_correctness | category | Unknown | 1934 | 0.0275191 | 0.173708 | 0.652131 | 0.528791 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0715733 | 0.190537 | 0.712043 | 0.564145 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0314504 | 0.175027 | 0.701017 | 0.529088 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0181896 | 0.172728 | 0.644446 | 0.527685 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.028893 | 0.156636 | 0.653317 | 0.489407 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0259112 | 0.159602 | 0.676182 | 0.495522 |
