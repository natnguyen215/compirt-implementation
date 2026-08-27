# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711602 |
| log_loss | 0.497666 |
| ece | 0.0747122 |
| brier | 0.16207 |
| accuracy | 0.77562 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00226537 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.165499 |
| probability_p10 | 0.464582 |
| probability_p50 | 0.724023 |
| probability_p90 | 0.894873 |
| mean_predictive_variance | 0.183074 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10737 |
| joint_tossup_event_log_loss | 6.7559 |
| buzz_position_mae | 0.177017 |
| buzz_position_median_absolute_error | 0.157641 |
| buzz_position_bias | -0.098077 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.339266 |
| first_buzzer_mean_reciprocal_rank | 0.551385 |
| first_buzzer_log_loss | 1.71058 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711602 |
| neg_average_precision | 0.448971 |
| neg_precision | 0.508728 |
| neg_recall | 0.29129 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0948415 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0770114 |
| no_buzz_calibration_error | 0.0652843 |
| no_buzz_brier | 0.0214849 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.098077 | -0.110948 |
| Q1 (0-.2) | 179 | 0.336131 | 0.339016 |
| Q2 (.2-.4) | 957 | 0.176378 | 0.168728 |
| Q3 (.4-.6) | 2203 | 0.0221677 | 0.0170778 |
| Q4 (.6-.8) | 2978 | -0.121886 | -0.121211 |
| Q5 (.8-1) | 2953 | -0.279036 | -0.273907 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0747122 | 0.16207 | 0.711602 | 0.497666 |
| tossup_correctness | tier | fall | 2876 | 0.0691522 | 0.152635 | 0.711166 | 0.473806 |
| tossup_correctness | tier | nationals | 1579 | 0.0782506 | 0.182113 | 0.70244 | 0.54429 |
| tossup_correctness | tier | regionals | 1990 | 0.0883834 | 0.162309 | 0.73742 | 0.498224 |
| tossup_correctness | tier | winter | 2825 | 0.0747826 | 0.160304 | 0.691085 | 0.495503 |
| tossup_correctness | category | Current Events | 123 | 0.120558 | 0.168211 | 0.754219 | 0.505773 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0640426 | 0.157736 | 0.719037 | 0.488559 |
| tossup_correctness | category | Geography | 191 | 0.0795614 | 0.169104 | 0.773369 | 0.51488 |
| tossup_correctness | category | History | 1469 | 0.0581756 | 0.169012 | 0.708524 | 0.510941 |
| tossup_correctness | category | Literature | 1436 | 0.074148 | 0.150172 | 0.668708 | 0.47103 |
| tossup_correctness | category | Mythology | 325 | 0.112356 | 0.145732 | 0.644769 | 0.460786 |
| tossup_correctness | category | Other Academic | 67 | 0.12629 | 0.18605 | 0.621294 | 0.554083 |
| tossup_correctness | category | Philosophy | 322 | 0.0720577 | 0.161141 | 0.680873 | 0.493511 |
| tossup_correctness | category | Popular Culture | 100 | 0.100346 | 0.121349 | 0.547497 | 0.400267 |
| tossup_correctness | category | Religion | 365 | 0.0582972 | 0.185087 | 0.692394 | 0.55341 |
| tossup_correctness | category | Science | 1456 | 0.0851855 | 0.16718 | 0.700111 | 0.511108 |
| tossup_correctness | category | Social Science | 333 | 0.085188 | 0.165926 | 0.759945 | 0.505697 |
| tossup_correctness | category | Unknown | 1990 | 0.0883834 | 0.162309 | 0.73742 | 0.498224 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.136157 | 0.178809 | 0.724544 | 0.534615 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0864179 | 0.173858 | 0.699299 | 0.525558 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0721257 | 0.164059 | 0.716908 | 0.502157 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0798617 | 0.156759 | 0.707101 | 0.485482 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0675236 | 0.161107 | 0.713984 | 0.495325 |
