# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.589948 |
| log_loss | 0.710169 |
| ece | 0.254507 |
| brier | 0.254219 |
| accuracy | 0.578577 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.183548 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.164729 |
| probability_p10 | 0.27114 |
| probability_p50 | 0.527048 |
| probability_p90 | 0.709532 |
| mean_predictive_variance | 0.222806 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0936081 |
| joint_tossup_event_log_loss | 6.82661 |
| buzz_position_mae | 0.137959 |
| buzz_position_median_absolute_error | 0.115909 |
| buzz_position_bias | -0.00543226 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.367535 |
| first_buzzer_mean_reciprocal_rank | 0.577356 |
| first_buzzer_log_loss | 1.64846 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.589948 |
| neg_average_precision | 0.30155 |
| neg_precision | 0.290168 |
| neg_recall | 0.533518 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.139094 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0539502 |
| no_buzz_calibration_error | 0.0380412 |
| no_buzz_brier | 0.0222478 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.00543226 | -0.0286607 |
| Q1 (0-.2) | 167 | 0.389373 | 0.409766 |
| Q2 (.2-.4) | 912 | 0.235577 | 0.22846 |
| Q3 (.4-.6) | 2115 | 0.0939099 | 0.0894704 |
| Q4 (.6-.8) | 2844 | -0.0236757 | -0.0244136 |
| Q5 (.8-1) | 3055 | -0.150754 | -0.140464 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.254507 | 0.254219 | 0.589948 | 0.710169 |
| tossup_correctness | tier | fall | 2842 | 0.291509 | 0.259476 | 0.603102 | 0.720801 |
| tossup_correctness | tier | nationals | 1564 | 0.174391 | 0.234222 | 0.585995 | 0.662054 |
| tossup_correctness | tier | regionals | 1937 | 0.244916 | 0.249989 | 0.601817 | 0.702568 |
| tossup_correctness | tier | winter | 2750 | 0.268828 | 0.263139 | 0.586517 | 0.731899 |
| tossup_correctness | category | Current Events | 126 | 0.316338 | 0.297801 | 0.529684 | 0.807068 |
| tossup_correctness | category | Fine Arts | 1071 | 0.265963 | 0.255576 | 0.605442 | 0.713462 |
| tossup_correctness | category | Geography | 185 | 0.253091 | 0.283337 | 0.569352 | 0.771253 |
| tossup_correctness | category | History | 1440 | 0.250993 | 0.258394 | 0.568879 | 0.715612 |
| tossup_correctness | category | Literature | 1422 | 0.285008 | 0.24623 | 0.573487 | 0.694946 |
| tossup_correctness | category | Mythology | 318 | 0.276669 | 0.257726 | 0.558066 | 0.718584 |
| tossup_correctness | category | Other Academic | 66 | 0.214788 | 0.217044 | 0.740202 | 0.624722 |
| tossup_correctness | category | Philosophy | 311 | 0.22576 | 0.247762 | 0.600447 | 0.694461 |
| tossup_correctness | category | Popular Culture | 102 | 0.460859 | 0.343044 | 0.475 | 0.916992 |
| tossup_correctness | category | Religion | 358 | 0.205085 | 0.252513 | 0.582905 | 0.704078 |
| tossup_correctness | category | Science | 1433 | 0.233395 | 0.251889 | 0.600996 | 0.705019 |
| tossup_correctness | category | Social Science | 324 | 0.235355 | 0.252507 | 0.597847 | 0.703413 |
| tossup_correctness | category | Unknown | 1937 | 0.244916 | 0.249989 | 0.601817 | 0.702568 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.294295 | 0.296368 | 0.551996 | 0.805038 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.286111 | 0.284231 | 0.588585 | 0.778474 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.274423 | 0.260977 | 0.622868 | 0.72756 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.269629 | 0.25592 | 0.574465 | 0.714189 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.215799 | 0.236694 | 0.585837 | 0.668811 |
