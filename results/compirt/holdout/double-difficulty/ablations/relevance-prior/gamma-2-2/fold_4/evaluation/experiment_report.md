# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.723938 |
| log_loss | 0.484883 |
| ece | 0.0453392 |
| brier | 0.156078 |
| accuracy | 0.785653 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0122977 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.185852 |
| probability_p10 | 0.478411 |
| probability_p50 | 0.77664 |
| probability_p90 | 0.948091 |
| mean_predictive_variance | 0.158067 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0941973 |
| joint_tossup_event_log_loss | 6.41887 |
| buzz_position_mae | 0.136297 |
| buzz_position_median_absolute_error | 0.110658 |
| buzz_position_bias | 0.00998309 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.383279 |
| first_buzzer_mean_reciprocal_rank | 0.591031 |
| first_buzzer_log_loss | 1.61217 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.723938 |
| neg_average_precision | 0.45866 |
| neg_precision | 0.552583 |
| neg_recall | 0.285102 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.189335 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0092181 |
| no_buzz_calibration_error | -0.00250898 |
| no_buzz_brier | 0.0103669 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.00998309 | -0.0133991 |
| Q1 (0-.2) | 179 | 0.397602 | 0.401646 |
| Q2 (.2-.4) | 957 | 0.246331 | 0.237129 |
| Q3 (.4-.6) | 2203 | 0.102752 | 0.0963157 |
| Q4 (.6-.8) | 2978 | -0.0175063 | -0.0166081 |
| Q5 (.8-1) | 2953 | -0.131593 | -0.120615 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0453392 | 0.156078 | 0.723938 | 0.484883 |
| tossup_correctness | tier | fall | 2876 | 0.0403213 | 0.147022 | 0.727405 | 0.458935 |
| tossup_correctness | tier | nationals | 1579 | 0.0386498 | 0.176187 | 0.712649 | 0.540464 |
| tossup_correctness | tier | regionals | 1990 | 0.0504936 | 0.156384 | 0.740724 | 0.482303 |
| tossup_correctness | tier | winter | 2825 | 0.0534032 | 0.153844 | 0.710193 | 0.482051 |
| tossup_correctness | category | Current Events | 123 | 0.120704 | 0.15792 | 0.738078 | 0.477473 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0450959 | 0.156025 | 0.718462 | 0.492669 |
| tossup_correctness | category | Geography | 191 | 0.121554 | 0.165844 | 0.773369 | 0.518484 |
| tossup_correctness | category | History | 1469 | 0.0398413 | 0.166904 | 0.71523 | 0.507519 |
| tossup_correctness | category | Literature | 1436 | 0.0381853 | 0.138152 | 0.719085 | 0.441341 |
| tossup_correctness | category | Mythology | 325 | 0.0798736 | 0.133478 | 0.686847 | 0.431918 |
| tossup_correctness | category | Other Academic | 67 | 0.138221 | 0.171492 | 0.652291 | 0.535695 |
| tossup_correctness | category | Philosophy | 322 | 0.0593977 | 0.158473 | 0.695137 | 0.485672 |
| tossup_correctness | category | Popular Culture | 100 | 0.0708119 | 0.111811 | 0.596527 | 0.375882 |
| tossup_correctness | category | Religion | 365 | 0.0618751 | 0.190408 | 0.660779 | 0.569298 |
| tossup_correctness | category | Science | 1456 | 0.0589262 | 0.158163 | 0.724 | 0.491518 |
| tossup_correctness | category | Social Science | 333 | 0.0638961 | 0.160888 | 0.758528 | 0.498021 |
| tossup_correctness | category | Unknown | 1990 | 0.0504936 | 0.156384 | 0.740724 | 0.482303 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.115138 | 0.175327 | 0.742123 | 0.521131 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0769473 | 0.169219 | 0.714611 | 0.515159 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0453487 | 0.160381 | 0.723428 | 0.495801 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0432882 | 0.150322 | 0.711606 | 0.472966 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0355031 | 0.153249 | 0.737625 | 0.476747 |
