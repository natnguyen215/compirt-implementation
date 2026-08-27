# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.660885 |
| log_loss | 0.510529 |
| ece | 0.0385675 |
| brier | 0.166691 |
| accuracy | 0.772276 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00107875 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.136941 |
| probability_p10 | 0.53792 |
| probability_p50 | 0.763656 |
| probability_p90 | 0.886832 |
| mean_predictive_variance | 0.175654 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.16738 |
| joint_tossup_event_log_loss | 7.6197 |
| buzz_position_mae | 0.327091 |
| buzz_position_median_absolute_error | 0.329784 |
| buzz_position_bias | -0.31327 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.353506 |
| first_buzzer_mean_reciprocal_rank | 0.563337 |
| first_buzzer_log_loss | 1.68939 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.660885 |
| neg_average_precision | 0.372663 |
| neg_precision | 0.492212 |
| neg_recall | 0.150405 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0317596 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.223143 |
| no_buzz_calibration_error | 0.211416 |
| no_buzz_brier | 0.0671504 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.31327 | -0.329784 |
| Q1 (0-.2) | 179 | 0.178135 | 0.178442 |
| Q2 (.2-.4) | 957 | 0.0142851 | 0.0125728 |
| Q3 (.4-.6) | 2203 | -0.161416 | -0.162817 |
| Q4 (.6-.8) | 2978 | -0.341007 | -0.341479 |
| Q5 (.8-1) | 2953 | -0.534525 | -0.537221 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0385675 | 0.166691 | 0.660885 | 0.510529 |
| tossup_correctness | tier | fall | 2876 | 0.0222995 | 0.156362 | 0.640759 | 0.487585 |
| tossup_correctness | tier | nationals | 1579 | 0.119496 | 0.196227 | 0.677653 | 0.576809 |
| tossup_correctness | tier | regionals | 1990 | 0.0471083 | 0.170862 | 0.662404 | 0.520696 |
| tossup_correctness | tier | winter | 2825 | 0.0290563 | 0.157759 | 0.67491 | 0.48968 |
| tossup_correctness | category | Current Events | 123 | 0.13827 | 0.185411 | 0.669846 | 0.552547 |
| tossup_correctness | category | Fine Arts | 1093 | 0.033823 | 0.166122 | 0.661613 | 0.508928 |
| tossup_correctness | category | Geography | 191 | 0.0462824 | 0.179568 | 0.748716 | 0.536645 |
| tossup_correctness | category | History | 1469 | 0.0332657 | 0.170796 | 0.684987 | 0.517916 |
| tossup_correctness | category | Literature | 1436 | 0.0410547 | 0.15084 | 0.619016 | 0.474537 |
| tossup_correctness | category | Mythology | 325 | 0.107575 | 0.147902 | 0.60176 | 0.468405 |
| tossup_correctness | category | Other Academic | 67 | 0.18329 | 0.194714 | 0.6469 | 0.574878 |
| tossup_correctness | category | Philosophy | 322 | 0.0713868 | 0.166218 | 0.606118 | 0.51341 |
| tossup_correctness | category | Popular Culture | 100 | 0.154808 | 0.136068 | 0.463739 | 0.445432 |
| tossup_correctness | category | Religion | 365 | 0.0342108 | 0.189308 | 0.662729 | 0.560569 |
| tossup_correctness | category | Science | 1456 | 0.0445933 | 0.166103 | 0.660709 | 0.51039 |
| tossup_correctness | category | Social Science | 333 | 0.0566273 | 0.179708 | 0.696159 | 0.537848 |
| tossup_correctness | category | Unknown | 1990 | 0.0471083 | 0.170862 | 0.662404 | 0.520696 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0662598 | 0.178467 | 0.638474 | 0.540397 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0486223 | 0.181388 | 0.624589 | 0.545077 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0344387 | 0.170775 | 0.656388 | 0.520058 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0444808 | 0.157758 | 0.676662 | 0.487801 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0442456 | 0.167176 | 0.659551 | 0.513335 |
