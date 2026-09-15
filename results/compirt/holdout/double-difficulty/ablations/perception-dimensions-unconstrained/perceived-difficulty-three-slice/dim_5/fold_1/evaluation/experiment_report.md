# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.661967 |
| log_loss | 0.517769 |
| ece | 0.0187105 |
| brier | 0.169071 |
| accuracy | 0.770373 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0082481 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.1215 |
| probability_p10 | 0.593702 |
| probability_p50 | 0.786196 |
| probability_p90 | 0.901357 |
| mean_predictive_variance | 0.165618 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100992 |
| joint_tossup_event_log_loss | 6.86758 |
| buzz_position_mae | 0.161574 |
| buzz_position_median_absolute_error | 0.146567 |
| buzz_position_bias | -0.0712194 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.356318 |
| first_buzzer_mean_reciprocal_rank | 0.567789 |
| first_buzzer_log_loss | 1.66401 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.644452 |
| tossup_scorer_player_top1_accuracy | 0.329004 |
| tossup_scorer_team_top1_accuracy | 0.492965 |
| tossup_game_winner_accuracy | 0.774775 |
| tossup_game_margin_mae | 33.8929 |
| tournament_player_ppg_spearman | 0.675474 |
| tournament_player_ppg_mae | 8.87493 |
| tournament_player_ppg_top10_overlap | 0.686207 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.661967 |
| neg_average_precision | 0.397308 |
| neg_precision | 0.619048 |
| neg_recall | 0.0901526 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0561156 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0953444 |
| no_buzz_calibration_error | 0.0794353 |
| no_buzz_brier | 0.0282811 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| overall | 9093 | -0.0712194 | -0.091413 |
| Q1 (0-.2) | 167 | 0.361686 | 0.378435 |
| Q2 (.2-.4) | 912 | 0.204153 | 0.207236 |
| Q3 (.4-.6) | 2115 | 0.0492846 | 0.0517993 |
| Q4 (.6-.8) | 2844 | -0.0882301 | -0.086329 |
| Q5 (.8-1) | 3055 | -0.24468 | -0.243004 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0187105 | 0.169071 | 0.661967 | 0.517769 |
| tossup_correctness | tier | fall | 2842 | 0.0164905 | 0.152686 | 0.704137 | 0.474988 |
| tossup_correctness | tier | nationals | 1564 | 0.0453353 | 0.189554 | 0.660403 | 0.565714 |
| tossup_correctness | tier | regionals | 1937 | 0.0254317 | 0.175162 | 0.635514 | 0.531732 |
| tossup_correctness | tier | winter | 2750 | 0.0405067 | 0.170064 | 0.642472 | 0.52488 |
| tossup_correctness | category | Current Events | 126 | 0.0906988 | 0.165639 | 0.710985 | 0.508989 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0302762 | 0.163914 | 0.680711 | 0.504505 |
| tossup_correctness | category | Geography | 185 | 0.062492 | 0.171188 | 0.759275 | 0.520083 |
| tossup_correctness | category | History | 1440 | 0.0295274 | 0.170605 | 0.681272 | 0.519074 |
| tossup_correctness | category | Literature | 1422 | 0.041713 | 0.150137 | 0.606087 | 0.478378 |
| tossup_correctness | category | Mythology | 318 | 0.0744342 | 0.151504 | 0.702147 | 0.476466 |
| tossup_correctness | category | Other Academic | 66 | 0.0701543 | 0.201811 | 0.600224 | 0.59358 |
| tossup_correctness | category | Philosophy | 311 | 0.0519013 | 0.176631 | 0.677433 | 0.531781 |
| tossup_correctness | category | Popular Culture | 102 | 0.1165 | 0.116565 | 0.634259 | 0.396133 |
| tossup_correctness | category | Religion | 358 | 0.0577991 | 0.193394 | 0.660956 | 0.573612 |
| tossup_correctness | category | Science | 1433 | 0.0385331 | 0.178202 | 0.678813 | 0.539205 |
| tossup_correctness | category | Social Science | 324 | 0.0981122 | 0.178695 | 0.670838 | 0.540752 |
| tossup_correctness | category | Unknown | 1937 | 0.0254317 | 0.175162 | 0.635514 | 0.531732 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0567097 | 0.193694 | 0.636029 | 0.574732 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0369303 | 0.182179 | 0.671225 | 0.547755 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0198303 | 0.170194 | 0.671749 | 0.519221 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0210037 | 0.163231 | 0.645235 | 0.50477 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0217652 | 0.168471 | 0.666294 | 0.5168 |
