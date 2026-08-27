# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.69394 |
| log_loss | 0.533138 |
| ece | 0.062714 |
| brier | 0.172199 |
| accuracy | 0.759815 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00230947 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.214429 |
| probability_p10 | 0.418627 |
| probability_p50 | 0.824146 |
| probability_p90 | 0.95748 |
| mean_predictive_variance | 0.139777 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.094299 |
| joint_tossup_event_log_loss | 6.44195 |
| buzz_position_mae | 0.140845 |
| buzz_position_median_absolute_error | 0.119811 |
| buzz_position_bias | -0.0295804 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.386891 |
| first_buzzer_mean_reciprocal_rank | 0.595039 |
| first_buzzer_log_loss | 1.58928 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.69394 |
| neg_average_precision | 0.417458 |
| neg_precision | 0.491633 |
| neg_recall | 0.285252 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.179092 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00909266 |
| no_buzz_calibration_error | -0.00681643 |
| no_buzz_brier | 0.0150279 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0295804 | -0.0506204 |
| Q1 (0-.2) | 167 | 0.371426 | 0.386612 |
| Q2 (.2-.4) | 912 | 0.211409 | 0.204077 |
| Q3 (.4-.6) | 2115 | 0.0674391 | 0.0630903 |
| Q4 (.6-.8) | 2844 | -0.0516679 | -0.0529524 |
| Q5 (.8-1) | 3055 | -0.170048 | -0.161414 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.062714 | 0.172199 | 0.69394 | 0.533138 |
| tossup_correctness | tier | fall | 2842 | 0.0552433 | 0.160637 | 0.700867 | 0.498023 |
| tossup_correctness | tier | nationals | 1564 | 0.0759708 | 0.189548 | 0.694102 | 0.579127 |
| tossup_correctness | tier | regionals | 1937 | 0.0609106 | 0.173186 | 0.693003 | 0.540369 |
| tossup_correctness | tier | winter | 2750 | 0.0706098 | 0.173586 | 0.686015 | 0.538178 |
| tossup_correctness | category | Current Events | 126 | 0.0680351 | 0.167712 | 0.713118 | 0.508199 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0397484 | 0.158208 | 0.732395 | 0.486399 |
| tossup_correctness | category | Geography | 185 | 0.0565339 | 0.167962 | 0.776301 | 0.507379 |
| tossup_correctness | category | History | 1440 | 0.0705086 | 0.181095 | 0.678242 | 0.554076 |
| tossup_correctness | category | Literature | 1422 | 0.0898503 | 0.161301 | 0.662339 | 0.514382 |
| tossup_correctness | category | Mythology | 318 | 0.0537063 | 0.16349 | 0.625201 | 0.515553 |
| tossup_correctness | category | Other Academic | 66 | 0.0608794 | 0.166894 | 0.792833 | 0.499026 |
| tossup_correctness | category | Philosophy | 311 | 0.0527767 | 0.167287 | 0.751691 | 0.498672 |
| tossup_correctness | category | Popular Culture | 102 | 0.0544392 | 0.111442 | 0.473148 | 0.390388 |
| tossup_correctness | category | Religion | 358 | 0.107722 | 0.191117 | 0.68795 | 0.579377 |
| tossup_correctness | category | Science | 1433 | 0.0884247 | 0.18771 | 0.676509 | 0.577016 |
| tossup_correctness | category | Social Science | 324 | 0.0526947 | 0.168969 | 0.734468 | 0.515142 |
| tossup_correctness | category | Unknown | 1937 | 0.0609106 | 0.173186 | 0.693003 | 0.540369 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.114775 | 0.202232 | 0.658964 | 0.606287 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0643343 | 0.17867 | 0.711096 | 0.553869 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0682749 | 0.172989 | 0.696146 | 0.536135 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0640627 | 0.165835 | 0.678926 | 0.520279 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0777695 | 0.174003 | 0.705405 | 0.532846 |
