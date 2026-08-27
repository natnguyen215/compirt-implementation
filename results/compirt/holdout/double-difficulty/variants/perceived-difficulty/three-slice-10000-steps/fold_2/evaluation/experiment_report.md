# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.616626 |
| log_loss | 0.64184 |
| ece | 0.199425 |
| brier | 0.223618 |
| accuracy | 0.651075 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.113104 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.169253 |
| probability_p10 | 0.319326 |
| probability_p50 | 0.589267 |
| probability_p90 | 0.765998 |
| mean_predictive_variance | 0.21716 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0952519 |
| joint_tossup_event_log_loss | 6.71613 |
| buzz_position_mae | 0.138938 |
| buzz_position_median_absolute_error | 0.115595 |
| buzz_position_bias | 0.0020665 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.365021 |
| first_buzzer_mean_reciprocal_rank | 0.575228 |
| first_buzzer_log_loss | 1.64079 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.616626 |
| neg_average_precision | 0.321357 |
| neg_precision | 0.323202 |
| neg_recall | 0.438388 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.145732 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0488143 |
| no_buzz_calibration_error | 0.0357013 |
| no_buzz_brier | 0.01835 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.0020665 | -0.016833 |
| Q1 (0-.2) | 183 | 0.414956 | 0.423847 |
| Q2 (.2-.4) | 955 | 0.242739 | 0.242528 |
| Q3 (.4-.6) | 2239 | 0.0984162 | 0.0948617 |
| Q4 (.6-.8) | 2875 | -0.0220302 | -0.0221281 |
| Q5 (.8-1) | 3005 | -0.1483 | -0.141307 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.199425 | 0.223618 | 0.616626 | 0.64184 |
| tossup_correctness | tier | fall | 2798 | 0.223482 | 0.221487 | 0.633141 | 0.637983 |
| tossup_correctness | tier | nationals | 1545 | 0.137977 | 0.222742 | 0.590112 | 0.636957 |
| tossup_correctness | tier | regionals | 2039 | 0.201681 | 0.225705 | 0.621297 | 0.644936 |
| tossup_correctness | tier | winter | 2875 | 0.209142 | 0.224682 | 0.61904 | 0.646022 |
| tossup_correctness | category | Current Events | 129 | 0.161885 | 0.243536 | 0.579502 | 0.686555 |
| tossup_correctness | category | Fine Arts | 1074 | 0.223392 | 0.232178 | 0.595768 | 0.661701 |
| tossup_correctness | category | Geography | 180 | 0.100699 | 0.237514 | 0.632589 | 0.673956 |
| tossup_correctness | category | History | 1454 | 0.165253 | 0.212545 | 0.612043 | 0.617594 |
| tossup_correctness | category | Literature | 1435 | 0.235486 | 0.216806 | 0.595825 | 0.62724 |
| tossup_correctness | category | Mythology | 324 | 0.206893 | 0.21747 | 0.6041 | 0.630084 |
| tossup_correctness | category | Other Academic | 71 | 0.202493 | 0.219871 | 0.535948 | 0.63037 |
| tossup_correctness | category | Philosophy | 310 | 0.174798 | 0.201784 | 0.668003 | 0.591468 |
| tossup_correctness | category | Popular Culture | 108 | 0.425577 | 0.310864 | 0.489583 | 0.843603 |
| tossup_correctness | category | Religion | 361 | 0.169488 | 0.213941 | 0.646485 | 0.618618 |
| tossup_correctness | category | Science | 1445 | 0.208304 | 0.233745 | 0.631174 | 0.665417 |
| tossup_correctness | category | Social Science | 327 | 0.145053 | 0.210821 | 0.666374 | 0.610564 |
| tossup_correctness | category | Unknown | 2039 | 0.201681 | 0.225705 | 0.621297 | 0.644936 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.268889 | 0.259267 | 0.649718 | 0.726337 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.225168 | 0.245383 | 0.630375 | 0.690353 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.216021 | 0.232101 | 0.638389 | 0.661861 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.214089 | 0.218758 | 0.616185 | 0.630842 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.160619 | 0.212858 | 0.592732 | 0.616881 |
