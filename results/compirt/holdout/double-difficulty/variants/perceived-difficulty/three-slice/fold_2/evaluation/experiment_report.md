# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.595159 |
| log_loss | 0.708387 |
| ece | 0.256768 |
| brier | 0.253321 |
| accuracy | 0.583234 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.180944 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.166151 |
| probability_p10 | 0.264328 |
| probability_p50 | 0.527078 |
| probability_p90 | 0.710262 |
| mean_predictive_variance | 0.222339 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0955413 |
| joint_tossup_event_log_loss | 6.80208 |
| buzz_position_mae | 0.139455 |
| buzz_position_median_absolute_error | 0.116647 |
| buzz_position_bias | -0.00182625 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.380145 |
| first_buzzer_mean_reciprocal_rank | 0.58744 |
| first_buzzer_log_loss | 1.61441 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.595159 |
| neg_average_precision | 0.307066 |
| neg_precision | 0.293668 |
| neg_recall | 0.546038 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.137558 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0518724 |
| no_buzz_calibration_error | 0.0387594 |
| no_buzz_brier | 0.0194886 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.00182625 | -0.0224326 |
| Q1 (0-.2) | 183 | 0.40869 | 0.409681 |
| Q2 (.2-.4) | 955 | 0.236082 | 0.233138 |
| Q3 (.4-.6) | 2239 | 0.0938672 | 0.0893003 |
| Q4 (.6-.8) | 2875 | -0.0257412 | -0.0239262 |
| Q5 (.8-1) | 3005 | -0.150854 | -0.142822 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.256768 | 0.253321 | 0.595159 | 0.708387 |
| tossup_correctness | tier | fall | 2798 | 0.306366 | 0.268895 | 0.609506 | 0.7435 |
| tossup_correctness | tier | nationals | 1545 | 0.189822 | 0.243719 | 0.564408 | 0.682427 |
| tossup_correctness | tier | regionals | 2039 | 0.251754 | 0.25154 | 0.608431 | 0.708483 |
| tossup_correctness | tier | winter | 2875 | 0.24803 | 0.244588 | 0.603431 | 0.688098 |
| tossup_correctness | category | Current Events | 129 | 0.203456 | 0.270392 | 0.567063 | 0.744163 |
| tossup_correctness | category | Fine Arts | 1074 | 0.2776 | 0.262831 | 0.574395 | 0.730068 |
| tossup_correctness | category | Geography | 180 | 0.179586 | 0.26999 | 0.536885 | 0.743459 |
| tossup_correctness | category | History | 1454 | 0.257886 | 0.25509 | 0.586614 | 0.708671 |
| tossup_correctness | category | Literature | 1435 | 0.28032 | 0.242404 | 0.589082 | 0.68354 |
| tossup_correctness | category | Mythology | 324 | 0.284044 | 0.25388 | 0.59022 | 0.710726 |
| tossup_correctness | category | Other Academic | 71 | 0.229688 | 0.247735 | 0.528322 | 0.689959 |
| tossup_correctness | category | Philosophy | 310 | 0.238113 | 0.23551 | 0.616984 | 0.664451 |
| tossup_correctness | category | Popular Culture | 108 | 0.474025 | 0.352515 | 0.474826 | 0.939309 |
| tossup_correctness | category | Religion | 361 | 0.252537 | 0.256856 | 0.58887 | 0.711551 |
| tossup_correctness | category | Science | 1445 | 0.241048 | 0.253464 | 0.604761 | 0.709719 |
| tossup_correctness | category | Social Science | 327 | 0.207585 | 0.237576 | 0.630527 | 0.668637 |
| tossup_correctness | category | Unknown | 2039 | 0.251754 | 0.25154 | 0.608431 | 0.708483 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.335928 | 0.299148 | 0.650344 | 0.816974 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.280705 | 0.273668 | 0.622626 | 0.753207 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.270643 | 0.261806 | 0.618391 | 0.729913 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.274473 | 0.25267 | 0.589486 | 0.706605 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.217062 | 0.238365 | 0.570262 | 0.673198 |
