# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.72407 |
| log_loss | 0.559103 |
| ece | 0.121722 |
| brier | 0.181044 |
| accuracy | 0.735491 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0378641 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.276864 |
| probability_p10 | 0.244566 |
| probability_p50 | 0.75764 |
| probability_p90 | 0.980334 |
| mean_predictive_variance | 0.140289 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0935128 |
| joint_tossup_event_log_loss | 6.49994 |
| buzz_position_mae | 0.13688 |
| buzz_position_median_absolute_error | 0.113264 |
| buzz_position_bias | 0.0056859 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.3863 |
| first_buzzer_mean_reciprocal_rank | 0.59397 |
| first_buzzer_log_loss | 1.61624 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.72407 |
| neg_average_precision | 0.444438 |
| neg_precision | 0.427689 |
| neg_recall | 0.49405 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.177419 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0474056 |
| no_buzz_calibration_error | 0.0356785 |
| no_buzz_brier | 0.0176456 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.0056859 | -0.0145765 |
| Q1 (0-.2) | 179 | 0.395282 | 0.396746 |
| Q2 (.2-.4) | 957 | 0.243822 | 0.233789 |
| Q3 (.4-.6) | 2203 | 0.102403 | 0.0983895 |
| Q4 (.6-.8) | 2978 | -0.0192418 | -0.0178131 |
| Q5 (.8-1) | 2953 | -0.142119 | -0.133426 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.121722 | 0.181044 | 0.72407 | 0.559103 |
| tossup_correctness | tier | fall | 2876 | 0.116627 | 0.173403 | 0.725905 | 0.535725 |
| tossup_correctness | tier | nationals | 1579 | 0.110762 | 0.192101 | 0.722999 | 0.584281 |
| tossup_correctness | tier | regionals | 1990 | 0.127276 | 0.184332 | 0.730856 | 0.562636 |
| tossup_correctness | tier | winter | 2825 | 0.131524 | 0.180326 | 0.713796 | 0.566343 |
| tossup_correctness | category | Current Events | 123 | 0.130421 | 0.200614 | 0.692223 | 0.573125 |
| tossup_correctness | category | Fine Arts | 1093 | 0.124716 | 0.182076 | 0.716008 | 0.561321 |
| tossup_correctness | category | Geography | 191 | 0.119069 | 0.180296 | 0.761941 | 0.591444 |
| tossup_correctness | category | History | 1469 | 0.116205 | 0.182135 | 0.740585 | 0.559318 |
| tossup_correctness | category | Literature | 1436 | 0.107355 | 0.163337 | 0.708493 | 0.520276 |
| tossup_correctness | category | Mythology | 325 | 0.141253 | 0.169918 | 0.688135 | 0.528513 |
| tossup_correctness | category | Other Academic | 67 | 0.190218 | 0.224157 | 0.617251 | 0.702017 |
| tossup_correctness | category | Philosophy | 322 | 0.152288 | 0.189474 | 0.680587 | 0.574298 |
| tossup_correctness | category | Popular Culture | 100 | 0.137105 | 0.139034 | 0.641471 | 0.484381 |
| tossup_correctness | category | Religion | 365 | 0.11637 | 0.199855 | 0.711709 | 0.609999 |
| tossup_correctness | category | Science | 1456 | 0.133616 | 0.188075 | 0.71176 | 0.577402 |
| tossup_correctness | category | Social Science | 333 | 0.11064 | 0.178042 | 0.77476 | 0.546523 |
| tossup_correctness | category | Unknown | 1990 | 0.127276 | 0.184332 | 0.730856 | 0.562636 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.205497 | 0.207448 | 0.766667 | 0.614725 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.13256 | 0.189358 | 0.745058 | 0.576137 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.117735 | 0.179988 | 0.73103 | 0.558871 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.116607 | 0.177795 | 0.7042 | 0.54952 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.125572 | 0.180813 | 0.728515 | 0.560049 |
