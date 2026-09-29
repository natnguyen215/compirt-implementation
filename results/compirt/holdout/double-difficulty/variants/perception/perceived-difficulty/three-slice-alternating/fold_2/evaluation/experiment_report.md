# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.58939 |
| log_loss | 0.735988 |
| ece | 0.280365 |
| brier | 0.265929 |
| accuracy | 0.549638 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.21454 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.159897 |
| probability_p10 | 0.249921 |
| probability_p50 | 0.502203 |
| probability_p90 | 0.680833 |
| mean_predictive_variance | 0.224171 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0962067 |
| joint_tossup_event_log_loss | 6.88097 |
| buzz_position_mae | 0.140158 |
| buzz_position_median_absolute_error | 0.117669 |
| buzz_position_bias | -0.002582 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.359188 |
| first_buzzer_mean_reciprocal_rank | 0.569924 |
| first_buzzer_log_loss | 1.65801 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.58939 |
| neg_average_precision | 0.303078 |
| neg_precision | 0.283093 |
| neg_recall | 0.593678 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.13937 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0487791 |
| no_buzz_calibration_error | 0.0356661 |
| no_buzz_brier | 0.0186069 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.002582 | -0.0221182 |
| Q1 (0-.2) | 183 | 0.406979 | 0.411864 |
| Q2 (.2-.4) | 955 | 0.235881 | 0.232765 |
| Q3 (.4-.6) | 2239 | 0.0938175 | 0.0888642 |
| Q4 (.6-.8) | 2875 | -0.0259746 | -0.0244335 |
| Q5 (.8-1) | 3005 | -0.152754 | -0.144735 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.280365 | 0.265929 | 0.58939 | 0.735988 |
| tossup_correctness | tier | fall | 2798 | 0.333101 | 0.285793 | 0.603484 | 0.781135 |
| tossup_correctness | tier | nationals | 1545 | 0.199081 | 0.244488 | 0.575648 | 0.684459 |
| tossup_correctness | tier | regionals | 2039 | 0.264624 | 0.2581 | 0.599899 | 0.72251 |
| tossup_correctness | tier | winter | 2875 | 0.284265 | 0.263671 | 0.597806 | 0.729302 |
| tossup_correctness | category | Current Events | 129 | 0.255393 | 0.281343 | 0.55814 | 0.768609 |
| tossup_correctness | category | Fine Arts | 1074 | 0.307537 | 0.279684 | 0.570803 | 0.76753 |
| tossup_correctness | category | Geography | 180 | 0.195024 | 0.279602 | 0.521347 | 0.762968 |
| tossup_correctness | category | History | 1454 | 0.2688 | 0.260156 | 0.589574 | 0.72053 |
| tossup_correctness | category | Literature | 1435 | 0.309383 | 0.259523 | 0.578315 | 0.721629 |
| tossup_correctness | category | Mythology | 324 | 0.316788 | 0.271605 | 0.593588 | 0.748798 |
| tossup_correctness | category | Other Academic | 71 | 0.281292 | 0.254764 | 0.533769 | 0.705129 |
| tossup_correctness | category | Philosophy | 310 | 0.263804 | 0.248946 | 0.613262 | 0.692683 |
| tossup_correctness | category | Popular Culture | 108 | 0.495839 | 0.372321 | 0.46875 | 0.986747 |
| tossup_correctness | category | Religion | 361 | 0.263816 | 0.261801 | 0.606363 | 0.722906 |
| tossup_correctness | category | Science | 1445 | 0.283989 | 0.275481 | 0.593735 | 0.756514 |
| tossup_correctness | category | Social Science | 327 | 0.228767 | 0.249847 | 0.620074 | 0.696452 |
| tossup_correctness | category | Unknown | 2039 | 0.264624 | 0.2581 | 0.599899 | 0.72251 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.36585 | 0.317851 | 0.651596 | 0.861909 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.311805 | 0.292563 | 0.616313 | 0.795215 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.29874 | 0.278005 | 0.610645 | 0.765506 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.298455 | 0.265411 | 0.586494 | 0.734344 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.23417 | 0.245799 | 0.564024 | 0.689077 |
