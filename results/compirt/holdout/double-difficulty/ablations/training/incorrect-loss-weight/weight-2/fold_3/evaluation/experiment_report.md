# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.70801 |
| log_loss | 0.525086 |
| ece | 0.113832 |
| brier | 0.17392 |
| accuracy | 0.74989 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0201542 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.1917 |
| probability_p10 | 0.379487 |
| probability_p50 | 0.689825 |
| probability_p90 | 0.876929 |
| mean_predictive_variance | 0.188849 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101352 |
| joint_tossup_event_log_loss | 6.62329 |
| buzz_position_mae | 0.152056 |
| buzz_position_median_absolute_error | 0.136026 |
| buzz_position_bias | -0.0490917 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.351652 |
| first_buzzer_mean_reciprocal_rank | 0.567483 |
| first_buzzer_log_loss | 1.67123 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.70801 |
| neg_average_precision | 0.447568 |
| neg_precision | 0.452566 |
| neg_recall | 0.418103 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.183493 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0150874 |
| no_buzz_calibration_error | -9.69646e-05 |
| no_buzz_brier | 0.0137037 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0490917 | -0.0699338 |
| Q1 (0-.2) | 192 | 0.387095 | 0.393694 |
| Q2 (.2-.4) | 889 | 0.208082 | 0.207607 |
| Q3 (.4-.6) | 2210 | 0.055693 | 0.0537352 |
| Q4 (.6-.8) | 2869 | -0.0799089 | -0.0775547 |
| Q5 (.8-1) | 2920 | -0.205097 | -0.20238 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.113832 | 0.17392 | 0.70801 | 0.525086 |
| tossup_correctness | tier | fall | 2817 | 0.110535 | 0.170423 | 0.700186 | 0.5177 |
| tossup_correctness | tier | nationals | 1542 | 0.107556 | 0.182328 | 0.726157 | 0.543251 |
| tossup_correctness | tier | regionals | 1934 | 0.105663 | 0.176604 | 0.711317 | 0.531043 |
| tossup_correctness | tier | winter | 2787 | 0.12655 | 0.170942 | 0.697939 | 0.518368 |
| tossup_correctness | category | Current Events | 125 | 0.102432 | 0.184188 | 0.744472 | 0.542137 |
| tossup_correctness | category | Fine Arts | 1072 | 0.117021 | 0.170697 | 0.720004 | 0.516664 |
| tossup_correctness | category | Geography | 185 | 0.151033 | 0.183126 | 0.774126 | 0.545798 |
| tossup_correctness | category | History | 1443 | 0.122841 | 0.175206 | 0.732106 | 0.525419 |
| tossup_correctness | category | Literature | 1411 | 0.10556 | 0.161136 | 0.657496 | 0.497772 |
| tossup_correctness | category | Mythology | 320 | 0.111511 | 0.167833 | 0.66267 | 0.518203 |
| tossup_correctness | category | Other Academic | 64 | 0.103576 | 0.198379 | 0.643229 | 0.585434 |
| tossup_correctness | category | Philosophy | 312 | 0.128516 | 0.167584 | 0.664645 | 0.509321 |
| tossup_correctness | category | Popular Culture | 104 | 0.136556 | 0.140027 | 0.607955 | 0.459731 |
| tossup_correctness | category | Religion | 358 | 0.114364 | 0.19264 | 0.712127 | 0.568131 |
| tossup_correctness | category | Science | 1431 | 0.122968 | 0.179971 | 0.6971 | 0.538658 |
| tossup_correctness | category | Social Science | 321 | 0.122041 | 0.180108 | 0.728595 | 0.540141 |
| tossup_correctness | category | Unknown | 1934 | 0.105663 | 0.176604 | 0.711317 | 0.531043 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.117167 | 0.193173 | 0.747427 | 0.572242 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.10176 | 0.17445 | 0.745405 | 0.525479 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0959564 | 0.180706 | 0.682567 | 0.542832 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.11083 | 0.168144 | 0.691031 | 0.510863 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.134988 | 0.173032 | 0.7275 | 0.522411 |
