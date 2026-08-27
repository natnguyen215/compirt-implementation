# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.623137 |
| log_loss | 0.741294 |
| ece | 0.193269 |
| brier | 0.240747 |
| accuracy | 0.654899 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.107225 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.292588 |
| probability_p10 | 0.148729 |
| probability_p50 | 0.692941 |
| probability_p90 | 0.952435 |
| mean_predictive_variance | 0.149969 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950096 |
| joint_tossup_event_log_loss | 6.74999 |
| buzz_position_mae | 0.1371 |
| buzz_position_median_absolute_error | 0.111732 |
| buzz_position_bias | 0.00682347 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.395799 |
| first_buzzer_mean_reciprocal_rank | 0.599427 |
| first_buzzer_log_loss | 1.60417 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.623137 |
| neg_average_precision | 0.334721 |
| neg_precision | 0.335248 |
| neg_recall | 0.458622 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.141738 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0634435 |
| no_buzz_calibration_error | 0.0475345 |
| no_buzz_brier | 0.0271587 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.00682347 | -0.0112104 |
| Q1 (0-.2) | 167 | 0.393809 | 0.411059 |
| Q2 (.2-.4) | 912 | 0.237968 | 0.238033 |
| Q3 (.4-.6) | 2115 | 0.10561 | 0.102777 |
| Q4 (.6-.8) | 2844 | -0.00909019 | -0.00350994 |
| Q5 (.8-1) | 3055 | -0.13691 | -0.12705 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.193269 | 0.240747 | 0.623137 | 0.741294 |
| tossup_correctness | tier | fall | 2842 | 0.188099 | 0.226473 | 0.638387 | 0.689355 |
| tossup_correctness | tier | nationals | 1564 | 0.189132 | 0.256141 | 0.599358 | 0.802496 |
| tossup_correctness | tier | regionals | 1937 | 0.189825 | 0.240078 | 0.621651 | 0.744758 |
| tossup_correctness | tier | winter | 2750 | 0.204563 | 0.247215 | 0.63274 | 0.757722 |
| tossup_correctness | category | Current Events | 126 | 0.276629 | 0.286101 | 0.583007 | 0.86884 |
| tossup_correctness | category | Fine Arts | 1071 | 0.206341 | 0.24017 | 0.642982 | 0.721768 |
| tossup_correctness | category | Geography | 185 | 0.208194 | 0.268721 | 0.631091 | 0.794079 |
| tossup_correctness | category | History | 1440 | 0.166359 | 0.231611 | 0.630976 | 0.717149 |
| tossup_correctness | category | Literature | 1422 | 0.219062 | 0.239962 | 0.581152 | 0.761333 |
| tossup_correctness | category | Mythology | 318 | 0.271292 | 0.268299 | 0.562704 | 0.805705 |
| tossup_correctness | category | Other Academic | 66 | 0.223105 | 0.217113 | 0.702128 | 0.616843 |
| tossup_correctness | category | Philosophy | 311 | 0.17227 | 0.234498 | 0.690419 | 0.726068 |
| tossup_correctness | category | Popular Culture | 102 | 0.373423 | 0.291461 | 0.452778 | 0.83572 |
| tossup_correctness | category | Religion | 358 | 0.156331 | 0.237247 | 0.66343 | 0.721297 |
| tossup_correctness | category | Science | 1433 | 0.173342 | 0.237023 | 0.624454 | 0.731677 |
| tossup_correctness | category | Social Science | 324 | 0.186895 | 0.245238 | 0.630244 | 0.736385 |
| tossup_correctness | category | Unknown | 1937 | 0.189825 | 0.240078 | 0.621651 | 0.744758 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.44655 | 0.41634 | 0.66194 | 1.32388 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.355244 | 0.341136 | 0.636559 | 1.05647 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.244647 | 0.267981 | 0.645665 | 0.803992 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.173705 | 0.222062 | 0.63645 | 0.680345 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.119447 | 0.19972 | 0.623737 | 0.628691 |
