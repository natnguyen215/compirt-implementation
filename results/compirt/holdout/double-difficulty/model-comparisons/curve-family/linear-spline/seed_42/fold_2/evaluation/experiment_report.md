# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.721329 |
| log_loss | 0.570935 |
| ece | 0.118738 |
| brier | 0.184719 |
| accuracy | 0.73015 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0340283 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.277797 |
| probability_p10 | 0.246843 |
| probability_p50 | 0.750212 |
| probability_p90 | 0.979485 |
| mean_predictive_variance | 0.140981 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0938393 |
| joint_tossup_event_log_loss | 6.44579 |
| buzz_position_mae | 0.136467 |
| buzz_position_median_absolute_error | 0.111543 |
| buzz_position_bias | 0.00614264 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.406395 |
| first_buzzer_mean_reciprocal_rank | 0.609265 |
| first_buzzer_log_loss | 1.57155 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.721329 |
| neg_average_precision | 0.447794 |
| neg_precision | 0.436002 |
| neg_recall | 0.491525 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.180905 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0480539 |
| no_buzz_calibration_error | 0.0349408 |
| no_buzz_brier | 0.0184158 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.00614264 | -0.014779 |
| Q1 (0-.2) | 183 | 0.402741 | 0.413699 |
| Q2 (.2-.4) | 955 | 0.240493 | 0.235538 |
| Q3 (.4-.6) | 2239 | 0.100555 | 0.0950368 |
| Q4 (.6-.8) | 2875 | -0.0183021 | -0.0199763 |
| Q5 (.8-1) | 3005 | -0.139445 | -0.131307 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.118738 | 0.184719 | 0.721329 | 0.570935 |
| tossup_correctness | tier | fall | 2798 | 0.126251 | 0.179298 | 0.713468 | 0.565407 |
| tossup_correctness | tier | nationals | 1545 | 0.103258 | 0.19013 | 0.743765 | 0.559573 |
| tossup_correctness | tier | regionals | 2039 | 0.128824 | 0.189757 | 0.716724 | 0.585924 |
| tossup_correctness | tier | winter | 2875 | 0.114404 | 0.183514 | 0.713183 | 0.571791 |
| tossup_correctness | category | Current Events | 129 | 0.159178 | 0.234952 | 0.674419 | 0.713438 |
| tossup_correctness | category | Fine Arts | 1074 | 0.122902 | 0.184933 | 0.723961 | 0.574317 |
| tossup_correctness | category | Geography | 180 | 0.104937 | 0.195799 | 0.780911 | 0.586245 |
| tossup_correctness | category | History | 1454 | 0.118214 | 0.184871 | 0.731436 | 0.572095 |
| tossup_correctness | category | Literature | 1435 | 0.118966 | 0.162265 | 0.711016 | 0.519509 |
| tossup_correctness | category | Mythology | 324 | 0.157134 | 0.199106 | 0.631105 | 0.675536 |
| tossup_correctness | category | Other Academic | 71 | 0.183649 | 0.203023 | 0.642702 | 0.621726 |
| tossup_correctness | category | Philosophy | 310 | 0.0927315 | 0.175109 | 0.737574 | 0.522909 |
| tossup_correctness | category | Popular Culture | 108 | 0.202489 | 0.206787 | 0.55816 | 0.638485 |
| tossup_correctness | category | Religion | 361 | 0.1324 | 0.191285 | 0.734152 | 0.566715 |
| tossup_correctness | category | Science | 1445 | 0.117745 | 0.187313 | 0.719705 | 0.564386 |
| tossup_correctness | category | Social Science | 327 | 0.123225 | 0.189427 | 0.744311 | 0.564387 |
| tossup_correctness | category | Unknown | 2039 | 0.128824 | 0.189757 | 0.716724 | 0.585924 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.215216 | 0.209775 | 0.780663 | 0.610812 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.134439 | 0.20109 | 0.727095 | 0.611777 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.103703 | 0.181137 | 0.732281 | 0.566782 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.110929 | 0.177102 | 0.704099 | 0.55296 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.133236 | 0.187947 | 0.723138 | 0.575819 |
