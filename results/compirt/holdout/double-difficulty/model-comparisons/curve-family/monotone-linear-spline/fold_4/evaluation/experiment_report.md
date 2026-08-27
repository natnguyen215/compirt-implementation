# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.666865 |
| log_loss | 0.830007 |
| ece | 0.235456 |
| brier | 0.260851 |
| accuracy | 0.628371 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.144984 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.319339 |
| probability_p10 | 0.086929 |
| probability_p50 | 0.591047 |
| probability_p90 | 0.961305 |
| mean_predictive_variance | 0.145027 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.122643 |
| joint_tossup_event_log_loss | 8.02489 |
| buzz_position_mae | 0.151581 |
| buzz_position_median_absolute_error | 0.120145 |
| buzz_position_bias | 0.0536197 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.329126 |
| first_buzzer_mean_reciprocal_rank | 0.534054 |
| first_buzzer_log_loss | 2.3242 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.666865 |
| neg_average_precision | 0.332419 |
| neg_precision | 0.329181 |
| neg_recall | 0.616373 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.170783 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.195885 |
| no_buzz_calibration_error | 0.184158 |
| no_buzz_brier | 0.105808 |
| full_pmf_max_mass_error | 1.01796e-11 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.0536197 | 0.0367229 |
| Q1 (0-.2) | 179 | 0.454208 | 0.457377 |
| Q2 (.2-.4) | 957 | 0.305901 | 0.299672 |
| Q3 (.4-.6) | 2203 | 0.157314 | 0.150267 |
| Q4 (.6-.8) | 2978 | 0.0316271 | 0.0321422 |
| Q5 (.8-1) | 2953 | -0.1076 | -0.100215 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.235456 | 0.260851 | 0.666865 | 0.830007 |
| tossup_correctness | tier | fall | 2876 | 0.145864 | 0.198535 | 0.701081 | 0.638216 |
| tossup_correctness | tier | nationals | 1579 | 0.370634 | 0.347819 | 0.705701 | 1.09335 |
| tossup_correctness | tier | regionals | 1990 | 0.303977 | 0.31664 | 0.618562 | 1.00645 |
| tossup_correctness | tier | winter | 2825 | 0.202841 | 0.236383 | 0.653636 | 0.753774 |
| tossup_correctness | category | Current Events | 123 | 0.251989 | 0.265577 | 0.694057 | 0.798299 |
| tossup_correctness | category | Fine Arts | 1093 | 0.20806 | 0.235199 | 0.694095 | 0.757332 |
| tossup_correctness | category | Geography | 191 | 0.191279 | 0.224895 | 0.754494 | 0.699245 |
| tossup_correctness | category | History | 1469 | 0.210703 | 0.251289 | 0.67972 | 0.822875 |
| tossup_correctness | category | Literature | 1436 | 0.21361 | 0.233211 | 0.658528 | 0.747686 |
| tossup_correctness | category | Mythology | 325 | 0.212074 | 0.215559 | 0.65901 | 0.65284 |
| tossup_correctness | category | Other Academic | 67 | 0.324669 | 0.284303 | 0.696765 | 1.04319 |
| tossup_correctness | category | Philosophy | 322 | 0.214728 | 0.261303 | 0.640202 | 0.790753 |
| tossup_correctness | category | Popular Culture | 100 | 0.209625 | 0.210567 | 0.52094 | 0.684628 |
| tossup_correctness | category | Religion | 365 | 0.197494 | 0.257802 | 0.650653 | 0.788661 |
| tossup_correctness | category | Science | 1456 | 0.231632 | 0.256204 | 0.677943 | 0.80567 |
| tossup_correctness | category | Social Science | 333 | 0.247163 | 0.26972 | 0.676497 | 0.850649 |
| tossup_correctness | category | Unknown | 1990 | 0.303977 | 0.31664 | 0.618562 | 1.00645 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.419232 | 0.380037 | 0.685406 | 1.32775 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.326973 | 0.32594 | 0.651011 | 1.13148 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.246685 | 0.26829 | 0.678392 | 0.866103 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.229021 | 0.251022 | 0.664912 | 0.776622 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.195575 | 0.236895 | 0.665323 | 0.729045 |
