# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.718001 |
| log_loss | 0.506566 |
| ece | 0.0651583 |
| brier | 0.165726 |
| accuracy | 0.763746 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000432105 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.201958 |
| probability_p10 | 0.417747 |
| probability_p50 | 0.745556 |
| probability_p90 | 0.944395 |
| mean_predictive_variance | 0.16553 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0952098 |
| joint_tossup_event_log_loss | 6.44739 |
| buzz_position_mae | 0.137559 |
| buzz_position_median_absolute_error | 0.111825 |
| buzz_position_bias | 0.00959693 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.379605 |
| first_buzzer_mean_reciprocal_rank | 0.588673 |
| first_buzzer_log_loss | 1.60401 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.718001 |
| neg_average_precision | 0.455201 |
| neg_precision | 0.498708 |
| neg_recall | 0.353642 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.192612 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0085273 |
| no_buzz_calibration_error | -0.0045857 |
| no_buzz_brier | 0.012271 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.00959693 | -0.0129268 |
| Q1 (0-.2) | 183 | 0.407866 | 0.411732 |
| Q2 (.2-.4) | 955 | 0.244208 | 0.239058 |
| Q3 (.4-.6) | 2239 | 0.100728 | 0.0962159 |
| Q4 (.6-.8) | 2875 | -0.0168765 | -0.0188756 |
| Q5 (.8-1) | 3005 | -0.13179 | -0.122772 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0651583 | 0.165726 | 0.718001 | 0.506566 |
| tossup_correctness | tier | fall | 2798 | 0.0614049 | 0.152189 | 0.734592 | 0.474645 |
| tossup_correctness | tier | nationals | 1545 | 0.0755303 | 0.185554 | 0.711658 | 0.550652 |
| tossup_correctness | tier | regionals | 2039 | 0.08345 | 0.172256 | 0.700929 | 0.52385 |
| tossup_correctness | tier | winter | 2875 | 0.0546889 | 0.163615 | 0.710771 | 0.501683 |
| tossup_correctness | category | Current Events | 129 | 0.0986118 | 0.199055 | 0.707139 | 0.578053 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0930603 | 0.169294 | 0.701269 | 0.517538 |
| tossup_correctness | category | Geography | 180 | 0.0970572 | 0.184308 | 0.767594 | 0.544983 |
| tossup_correctness | category | History | 1454 | 0.063353 | 0.166865 | 0.715806 | 0.511666 |
| tossup_correctness | category | Literature | 1435 | 0.0565933 | 0.140543 | 0.730628 | 0.448272 |
| tossup_correctness | category | Mythology | 324 | 0.0659104 | 0.158874 | 0.673616 | 0.494756 |
| tossup_correctness | category | Other Academic | 71 | 0.123949 | 0.189118 | 0.643791 | 0.582211 |
| tossup_correctness | category | Philosophy | 310 | 0.0708666 | 0.162499 | 0.749656 | 0.488097 |
| tossup_correctness | category | Popular Culture | 108 | 0.150823 | 0.127777 | 0.427951 | 0.437884 |
| tossup_correctness | category | Religion | 361 | 0.090824 | 0.183445 | 0.695474 | 0.543529 |
| tossup_correctness | category | Science | 1445 | 0.0520467 | 0.170115 | 0.72973 | 0.511073 |
| tossup_correctness | category | Social Science | 327 | 0.062506 | 0.17372 | 0.743895 | 0.521302 |
| tossup_correctness | category | Unknown | 2039 | 0.08345 | 0.172256 | 0.700929 | 0.52385 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.185452 | 0.194579 | 0.763454 | 0.567953 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.103116 | 0.18448 | 0.716111 | 0.553715 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0634037 | 0.167869 | 0.726606 | 0.512184 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0566661 | 0.158808 | 0.70907 | 0.486439 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0594343 | 0.163032 | 0.719332 | 0.502915 |
