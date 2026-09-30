# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.708974 |
| log_loss | 0.498245 |
| ece | 0.0158316 |
| brier | 0.162092 |
| accuracy | 0.771363 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00923788 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.150053 |
| probability_p10 | 0.560962 |
| probability_p50 | 0.810575 |
| probability_p90 | 0.923674 |
| mean_predictive_variance | 0.153589 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0960105 |
| joint_tossup_event_log_loss | 6.50637 |
| buzz_position_mae | 0.143363 |
| buzz_position_median_absolute_error | 0.124143 |
| buzz_position_bias | -0.0278376 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.360497 |
| first_buzzer_mean_reciprocal_rank | 0.572724 |
| first_buzzer_log_loss | 1.65482 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.708974 |
| neg_average_precision | 0.442585 |
| neg_precision | 0.57 |
| neg_recall | 0.158114 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.185443 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0117465 |
| no_buzz_calibration_error | -0.00416257 |
| no_buzz_brier | 0.0156652 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0278376 | -0.0490995 |
| Q1 (0-.2) | 167 | 0.383049 | 0.390381 |
| Q2 (.2-.4) | 912 | 0.223653 | 0.22709 |
| Q3 (.4-.6) | 2115 | 0.0772181 | 0.0747893 |
| Q4 (.6-.8) | 2844 | -0.0493942 | -0.0500482 |
| Q5 (.8-1) | 3055 | -0.178039 | -0.172916 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0158316 | 0.162092 | 0.708974 | 0.498245 |
| tossup_correctness | tier | fall | 2842 | 0.0134653 | 0.14926 | 0.727433 | 0.464434 |
| tossup_correctness | tier | nationals | 1564 | 0.0440202 | 0.17935 | 0.716239 | 0.539205 |
| tossup_correctness | tier | regionals | 1937 | 0.0257182 | 0.167741 | 0.688405 | 0.513047 |
| tossup_correctness | tier | winter | 2750 | 0.015181 | 0.161558 | 0.697742 | 0.499467 |
| tossup_correctness | category | Current Events | 126 | 0.0867073 | 0.157688 | 0.726982 | 0.486073 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0278216 | 0.151986 | 0.749929 | 0.469844 |
| tossup_correctness | category | Geography | 185 | 0.0823069 | 0.163834 | 0.791528 | 0.497 |
| tossup_correctness | category | History | 1440 | 0.0285116 | 0.168653 | 0.704506 | 0.513653 |
| tossup_correctness | category | Literature | 1422 | 0.0190308 | 0.143111 | 0.675956 | 0.454313 |
| tossup_correctness | category | Mythology | 318 | 0.0448348 | 0.153709 | 0.6563 | 0.487366 |
| tossup_correctness | category | Other Academic | 66 | 0.0832832 | 0.17434 | 0.795073 | 0.51742 |
| tossup_correctness | category | Philosophy | 311 | 0.0805682 | 0.171595 | 0.717809 | 0.514061 |
| tossup_correctness | category | Popular Culture | 102 | 0.0570234 | 0.109436 | 0.519444 | 0.383823 |
| tossup_correctness | category | Religion | 358 | 0.0203303 | 0.17986 | 0.71521 | 0.540804 |
| tossup_correctness | category | Science | 1433 | 0.035248 | 0.173795 | 0.696187 | 0.527414 |
| tossup_correctness | category | Social Science | 324 | 0.0606485 | 0.158373 | 0.779815 | 0.484998 |
| tossup_correctness | category | Unknown | 1937 | 0.0257182 | 0.167741 | 0.688405 | 0.513047 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0777709 | 0.209146 | 0.595938 | 0.6216 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0314441 | 0.172924 | 0.722158 | 0.522816 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.026526 | 0.164575 | 0.712549 | 0.503809 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.012608 | 0.156021 | 0.69102 | 0.485559 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0130776 | 0.160218 | 0.720868 | 0.492126 |
