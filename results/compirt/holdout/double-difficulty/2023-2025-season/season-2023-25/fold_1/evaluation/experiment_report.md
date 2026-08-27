# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710065 |
| log_loss | 0.495081 |
| ece | 0.0146181 |
| brier | 0.161179 |
| accuracy | 0.773032 |
| all_correct_accuracy | 0.764146 |
| accuracy_lift_over_all_correct | 0.00888588 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147377 |
| probability_p10 | 0.565587 |
| probability_p50 | 0.811731 |
| probability_p90 | 0.924987 |
| mean_predictive_variance | 0.153036 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.089271 |
| joint_tossup_event_log_loss | 5.53515 |
| buzz_position_mae | 0.159107 |
| buzz_position_median_absolute_error | 0.141572 |
| buzz_position_bias | -0.0490005 |
| survival_events | 31254 |
| joint_tossup_event_log_loss_events | 31254 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.334276 |
| first_buzzer_mean_reciprocal_rank | 0.548849 |
| first_buzzer_log_loss | 1.71714 |
| first_buzzer_events | 25096 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710065 |
| neg_average_precision | 0.437777 |
| neg_precision | 0.572638 |
| neg_recall | 0.148505 |
| full_pmf_events | 31254 |
| full_pmf_final_decile_mass | 0.140644 |
| no_buzz_observed_rate | 0.197031 |
| no_buzz_predicted_rate | 0.206566 |
| no_buzz_calibration_error | 0.00953533 |
| no_buzz_brier | 0.0422229 |
| full_pmf_max_mass_error | 1.66533e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 25096 | -0.0490005 | -0.0673858 |
| Q1 (0-.2) | 548 | 0.370787 | 0.377362 |
| Q2 (.2-.4) | 2666 | 0.223279 | 0.224843 |
| Q3 (.4-.6) | 5868 | 0.067302 | 0.0652533 |
| Q4 (.6-.8) | 7956 | -0.0751167 | -0.0747326 |
| Q5 (.8-1) | 8058 | -0.226541 | -0.224055 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 25096 | 0.0146181 | 0.161179 | 0.710065 | 0.495081 |
| tossup_correctness | tier | bowl | 690 | 0.0594051 | 0.168493 | 0.756616 | 0.506499 |
| tossup_correctness | tier | fall | 8459 | 0.00888212 | 0.151475 | 0.708351 | 0.470793 |
| tossup_correctness | tier | nationals | 4747 | 0.0526414 | 0.181751 | 0.695088 | 0.544655 |
| tossup_correctness | tier | open | 478 | 0.069959 | 0.190924 | 0.64138 | 0.578641 |
| tossup_correctness | tier | regionals | 4864 | 0.0155569 | 0.16025 | 0.723497 | 0.49346 |
| tossup_correctness | tier | winter | 5858 | 0.0121148 | 0.156001 | 0.716945 | 0.483166 |
| tossup_correctness | category | Current Events | 394 | 0.0391689 | 0.165897 | 0.711385 | 0.506963 |
| tossup_correctness | category | Fine Arts | 3468 | 0.0184522 | 0.161884 | 0.706699 | 0.49694 |
| tossup_correctness | category | Geography | 531 | 0.0374348 | 0.176477 | 0.719533 | 0.532024 |
| tossup_correctness | category | History | 4665 | 0.017886 | 0.1628 | 0.713369 | 0.498156 |
| tossup_correctness | category | Literature | 4595 | 0.0126814 | 0.137962 | 0.707546 | 0.439089 |
| tossup_correctness | category | Mythology | 1024 | 0.0286637 | 0.159026 | 0.656814 | 0.495402 |
| tossup_correctness | category | Other Academic | 229 | 0.0642727 | 0.191869 | 0.659186 | 0.56733 |
| tossup_correctness | category | Philosophy | 1053 | 0.0279284 | 0.155933 | 0.69539 | 0.48331 |
| tossup_correctness | category | Popular Culture | 349 | 0.0331874 | 0.124632 | 0.710166 | 0.406322 |
| tossup_correctness | category | Religion | 1132 | 0.0403266 | 0.172129 | 0.727124 | 0.518308 |
| tossup_correctness | category | Science | 4644 | 0.0253847 | 0.178518 | 0.688941 | 0.536368 |
| tossup_correctness | category | Social Science | 1049 | 0.0334538 | 0.16788 | 0.739371 | 0.511998 |
| tossup_correctness | category | Unknown | 1963 | 0.0168358 | 0.161274 | 0.721979 | 0.496573 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 548 | 0.0178331 | 0.172827 | 0.717738 | 0.519399 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 2666 | 0.0170282 | 0.16552 | 0.715974 | 0.503117 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 5868 | 0.0246155 | 0.167355 | 0.707415 | 0.509829 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 7956 | 0.0155693 | 0.153944 | 0.688407 | 0.479549 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 8058 | 0.012132 | 0.161595 | 0.725213 | 0.495365 |
