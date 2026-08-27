# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710917 |
| log_loss | 0.485753 |
| ece | 0.00585183 |
| brier | 0.157027 |
| accuracy | 0.7837 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0136564 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.141996 |
| probability_p10 | 0.578993 |
| probability_p50 | 0.810067 |
| probability_p90 | 0.917762 |
| mean_predictive_variance | 0.154363 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100696 |
| joint_tossup_event_log_loss | 6.58558 |
| buzz_position_mae | 0.149771 |
| buzz_position_median_absolute_error | 0.133058 |
| buzz_position_bias | -0.0423669 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.350441 |
| first_buzzer_mean_reciprocal_rank | 0.56587 |
| first_buzzer_log_loss | 1.67579 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710917 |
| neg_average_precision | 0.448768 |
| neg_precision | 0.626016 |
| neg_recall | 0.14751 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.191835 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0156471 |
| no_buzz_calibration_error | 0.000462706 |
| no_buzz_brier | 0.013796 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0423669 | -0.0645442 |
| Q1 (0-.2) | 192 | 0.392105 | 0.39992 |
| Q2 (.2-.4) | 889 | 0.213228 | 0.210328 |
| Q3 (.4-.6) | 2210 | 0.0607713 | 0.0581164 |
| Q4 (.6-.8) | 2869 | -0.0733853 | -0.0717424 |
| Q5 (.8-1) | 2920 | -0.196335 | -0.192146 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.00585183 | 0.157027 | 0.710917 | 0.485753 |
| tossup_correctness | tier | fall | 2817 | 0.00880349 | 0.15305 | 0.703875 | 0.477371 |
| tossup_correctness | tier | nationals | 1542 | 0.0337993 | 0.170696 | 0.72528 | 0.515514 |
| tossup_correctness | tier | regionals | 1934 | 0.0191985 | 0.162206 | 0.71771 | 0.497333 |
| tossup_correctness | tier | winter | 2787 | 0.0188586 | 0.14989 | 0.699818 | 0.469725 |
| tossup_correctness | category | Current Events | 125 | 0.0636828 | 0.180174 | 0.742629 | 0.532257 |
| tossup_correctness | category | Fine Arts | 1072 | 0.024999 | 0.152438 | 0.725999 | 0.474463 |
| tossup_correctness | category | Geography | 185 | 0.0572429 | 0.160595 | 0.77972 | 0.490882 |
| tossup_correctness | category | History | 1443 | 0.0281997 | 0.158772 | 0.728734 | 0.485208 |
| tossup_correctness | category | Literature | 1411 | 0.0276038 | 0.144489 | 0.65837 | 0.459453 |
| tossup_correctness | category | Mythology | 320 | 0.0212172 | 0.151695 | 0.665056 | 0.482392 |
| tossup_correctness | category | Other Academic | 64 | 0.172863 | 0.191904 | 0.632812 | 0.569711 |
| tossup_correctness | category | Philosophy | 312 | 0.0548394 | 0.148834 | 0.66129 | 0.467985 |
| tossup_correctness | category | Popular Culture | 104 | 0.0345966 | 0.125897 | 0.600142 | 0.422493 |
| tossup_correctness | category | Religion | 358 | 0.0319385 | 0.178634 | 0.719309 | 0.532421 |
| tossup_correctness | category | Science | 1431 | 0.0156339 | 0.159214 | 0.701057 | 0.492294 |
| tossup_correctness | category | Social Science | 321 | 0.0430734 | 0.159913 | 0.733748 | 0.49386 |
| tossup_correctness | category | Unknown | 1934 | 0.0191985 | 0.162206 | 0.71771 | 0.497333 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0861649 | 0.184443 | 0.745754 | 0.544309 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0284173 | 0.163139 | 0.75222 | 0.497218 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0218212 | 0.167121 | 0.686691 | 0.512415 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0133613 | 0.151286 | 0.693353 | 0.47238 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0134223 | 0.151364 | 0.727229 | 0.471374 |
