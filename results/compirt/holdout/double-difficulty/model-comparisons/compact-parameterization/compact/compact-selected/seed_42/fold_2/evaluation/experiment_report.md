# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.700539 |
| log_loss | 0.520366 |
| ece | 0.0591076 |
| brier | 0.169415 |
| accuracy | 0.76245 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00172842 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.207951 |
| probability_p10 | 0.441179 |
| probability_p50 | 0.820583 |
| probability_p90 | 0.956284 |
| mean_predictive_variance | 0.142002 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0954239 |
| joint_tossup_event_log_loss | 6.42889 |
| buzz_position_mae | 0.141489 |
| buzz_position_median_absolute_error | 0.120857 |
| buzz_position_bias | -0.0250245 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.395484 |
| first_buzzer_mean_reciprocal_rank | 0.601722 |
| first_buzzer_log_loss | 1.56245 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.700539 |
| neg_average_precision | 0.420499 |
| neg_precision | 0.493289 |
| neg_recall | 0.269354 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.178925 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.00882969 |
| no_buzz_calibration_error | -0.00428332 |
| no_buzz_brier | 0.0122794 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0250245 | -0.0469855 |
| Q1 (0-.2) | 183 | 0.381869 | 0.384461 |
| Q2 (.2-.4) | 955 | 0.213357 | 0.208564 |
| Q3 (.4-.6) | 2239 | 0.0672006 | 0.0590915 |
| Q4 (.6-.8) | 2875 | -0.051881 | -0.0548849 |
| Q5 (.8-1) | 3005 | -0.168584 | -0.162834 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0591076 | 0.169415 | 0.700539 | 0.520366 |
| tossup_correctness | tier | fall | 2798 | 0.040772 | 0.155507 | 0.717788 | 0.48292 |
| tossup_correctness | tier | nationals | 1545 | 0.0797701 | 0.187786 | 0.702366 | 0.563651 |
| tossup_correctness | tier | regionals | 2039 | 0.0694946 | 0.172079 | 0.693646 | 0.530855 |
| tossup_correctness | tier | winter | 2875 | 0.0660015 | 0.171189 | 0.687288 | 0.526109 |
| tossup_correctness | category | Current Events | 129 | 0.127839 | 0.21071 | 0.697945 | 0.613315 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0610855 | 0.162016 | 0.685731 | 0.504303 |
| tossup_correctness | category | Geography | 180 | 0.0969749 | 0.193971 | 0.746834 | 0.574412 |
| tossup_correctness | category | History | 1454 | 0.073 | 0.1798 | 0.67528 | 0.550666 |
| tossup_correctness | category | Literature | 1435 | 0.0520978 | 0.146044 | 0.728324 | 0.458406 |
| tossup_correctness | category | Mythology | 324 | 0.0450461 | 0.156155 | 0.658343 | 0.494743 |
| tossup_correctness | category | Other Academic | 71 | 0.0739482 | 0.172415 | 0.663399 | 0.526348 |
| tossup_correctness | category | Philosophy | 310 | 0.0553985 | 0.161703 | 0.735513 | 0.49328 |
| tossup_correctness | category | Popular Culture | 108 | 0.0618862 | 0.109147 | 0.440104 | 0.38643 |
| tossup_correctness | category | Religion | 361 | 0.0475745 | 0.179717 | 0.697962 | 0.533929 |
| tossup_correctness | category | Science | 1445 | 0.073552 | 0.180712 | 0.693448 | 0.546102 |
| tossup_correctness | category | Social Science | 327 | 0.0630298 | 0.182085 | 0.734505 | 0.543772 |
| tossup_correctness | category | Unknown | 2039 | 0.0694946 | 0.172079 | 0.693646 | 0.530855 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0639806 | 0.17071 | 0.720588 | 0.518073 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0582525 | 0.17492 | 0.714718 | 0.54111 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.053986 | 0.17073 | 0.709237 | 0.524636 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0572613 | 0.16016 | 0.696259 | 0.494553 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.069229 | 0.175461 | 0.697729 | 0.535427 |
