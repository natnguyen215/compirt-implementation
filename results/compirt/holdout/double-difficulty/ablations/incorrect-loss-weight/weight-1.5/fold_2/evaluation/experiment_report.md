# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.713353 |
| log_loss | 0.502237 |
| ece | 0.0596247 |
| brier | 0.164236 |
| accuracy | 0.769688 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00550934 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.170614 |
| probability_p10 | 0.459625 |
| probability_p50 | 0.74113 |
| probability_p90 | 0.894364 |
| mean_predictive_variance | 0.178981 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102549 |
| joint_tossup_event_log_loss | 6.63349 |
| buzz_position_mae | 0.152309 |
| buzz_position_median_absolute_error | 0.133877 |
| buzz_position_bias | -0.0432211 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.35411 |
| first_buzzer_mean_reciprocal_rank | 0.568365 |
| first_buzzer_log_loss | 1.66277 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.713353 |
| neg_average_precision | 0.449042 |
| neg_precision | 0.520782 |
| neg_recall | 0.292716 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190416 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0138288 |
| no_buzz_calibration_error | 0.000715765 |
| no_buzz_brier | 0.0128386 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0432211 | -0.0642698 |
| Q1 (0-.2) | 183 | 0.387182 | 0.400473 |
| Q2 (.2-.4) | 955 | 0.216837 | 0.215876 |
| Q3 (.4-.6) | 2239 | 0.0629871 | 0.0580434 |
| Q4 (.6-.8) | 2875 | -0.0688867 | -0.0690688 |
| Q5 (.8-1) | 3005 | -0.206659 | -0.206705 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0596247 | 0.164236 | 0.713353 | 0.502237 |
| tossup_correctness | tier | fall | 2798 | 0.0708139 | 0.151549 | 0.74062 | 0.471119 |
| tossup_correctness | tier | nationals | 1545 | 0.038862 | 0.178341 | 0.713399 | 0.535466 |
| tossup_correctness | tier | regionals | 2039 | 0.06149 | 0.166729 | 0.705944 | 0.508175 |
| tossup_correctness | tier | winter | 2875 | 0.0615856 | 0.167235 | 0.688488 | 0.510454 |
| tossup_correctness | category | Current Events | 129 | 0.0562548 | 0.200461 | 0.700919 | 0.581807 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0835989 | 0.161548 | 0.709123 | 0.4967 |
| tossup_correctness | category | Geography | 180 | 0.101706 | 0.185895 | 0.75284 | 0.549672 |
| tossup_correctness | category | History | 1454 | 0.0542151 | 0.170095 | 0.696925 | 0.515996 |
| tossup_correctness | category | Literature | 1435 | 0.063837 | 0.139348 | 0.727224 | 0.445102 |
| tossup_correctness | category | Mythology | 324 | 0.0675514 | 0.155666 | 0.676694 | 0.485308 |
| tossup_correctness | category | Other Academic | 71 | 0.129799 | 0.183705 | 0.59695 | 0.56106 |
| tossup_correctness | category | Philosophy | 310 | 0.055643 | 0.162146 | 0.726924 | 0.495295 |
| tossup_correctness | category | Popular Culture | 108 | 0.102164 | 0.119509 | 0.478299 | 0.407083 |
| tossup_correctness | category | Religion | 361 | 0.0883356 | 0.187756 | 0.673166 | 0.556123 |
| tossup_correctness | category | Science | 1445 | 0.0513478 | 0.170936 | 0.719705 | 0.515844 |
| tossup_correctness | category | Social Science | 327 | 0.0607423 | 0.179916 | 0.734968 | 0.537848 |
| tossup_correctness | category | Unknown | 2039 | 0.06149 | 0.166729 | 0.705944 | 0.508175 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0915824 | 0.188906 | 0.661765 | 0.556712 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0438424 | 0.174268 | 0.722174 | 0.525977 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0467532 | 0.16348 | 0.728561 | 0.500138 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0594122 | 0.156142 | 0.707785 | 0.482407 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0733276 | 0.167853 | 0.705176 | 0.511912 |
