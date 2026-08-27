# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.725409 |
| log_loss | 0.475582 |
| ece | 0.00982917 |
| brier | 0.153641 |
| accuracy | 0.786516 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0131607 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.146415 |
| probability_p10 | 0.569671 |
| probability_p50 | 0.809007 |
| probability_p90 | 0.919779 |
| mean_predictive_variance | 0.154673 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0964467 |
| joint_tossup_event_log_loss | 6.50353 |
| buzz_position_mae | 0.143001 |
| buzz_position_median_absolute_error | 0.123169 |
| buzz_position_bias | -0.0240573 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.363107 |
| first_buzzer_mean_reciprocal_rank | 0.572075 |
| first_buzzer_log_loss | 1.66163 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.725409 |
| neg_average_precision | 0.453115 |
| neg_precision | 0.607018 |
| neg_recall | 0.164683 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.180432 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0110406 |
| no_buzz_calibration_error | -0.00068652 |
| no_buzz_brier | 0.011107 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0240573 | -0.0459255 |
| Q1 (0-.2) | 179 | 0.386338 | 0.388611 |
| Q2 (.2-.4) | 957 | 0.227856 | 0.21616 |
| Q3 (.4-.6) | 2203 | 0.0778367 | 0.0752425 |
| Q4 (.6-.8) | 2978 | -0.0514925 | -0.051217 |
| Q5 (.8-1) | 2953 | -0.178921 | -0.172962 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.00982917 | 0.153641 | 0.725409 | 0.475582 |
| tossup_correctness | tier | fall | 2876 | 0.0151019 | 0.143553 | 0.733139 | 0.450125 |
| tossup_correctness | tier | nationals | 1579 | 0.0328081 | 0.174325 | 0.713901 | 0.527375 |
| tossup_correctness | tier | regionals | 1990 | 0.0168094 | 0.155802 | 0.736147 | 0.479358 |
| tossup_correctness | tier | winter | 2825 | 0.016278 | 0.150829 | 0.715048 | 0.469888 |
| tossup_correctness | category | Current Events | 123 | 0.0669279 | 0.144082 | 0.801174 | 0.44671 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0157326 | 0.149412 | 0.744262 | 0.465905 |
| tossup_correctness | category | Geography | 191 | 0.0640935 | 0.15707 | 0.791602 | 0.485421 |
| tossup_correctness | category | History | 1469 | 0.0309516 | 0.165252 | 0.713617 | 0.502228 |
| tossup_correctness | category | Literature | 1436 | 0.0135151 | 0.136593 | 0.707626 | 0.435648 |
| tossup_correctness | category | Mythology | 325 | 0.0669774 | 0.1305 | 0.667096 | 0.420961 |
| tossup_correctness | category | Other Academic | 67 | 0.0556699 | 0.160462 | 0.685984 | 0.494231 |
| tossup_correctness | category | Philosophy | 322 | 0.027998 | 0.158222 | 0.691528 | 0.484647 |
| tossup_correctness | category | Popular Culture | 100 | 0.0572428 | 0.105174 | 0.546476 | 0.363063 |
| tossup_correctness | category | Religion | 365 | 0.0654956 | 0.18672 | 0.666067 | 0.558961 |
| tossup_correctness | category | Science | 1456 | 0.01551 | 0.156196 | 0.721551 | 0.48261 |
| tossup_correctness | category | Social Science | 333 | 0.0407482 | 0.16239 | 0.751257 | 0.496903 |
| tossup_correctness | category | Unknown | 1990 | 0.0168094 | 0.155802 | 0.736147 | 0.479358 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0761893 | 0.159293 | 0.768988 | 0.485391 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0112512 | 0.162996 | 0.70732 | 0.499881 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0226407 | 0.156428 | 0.727615 | 0.481926 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.00963046 | 0.148134 | 0.714165 | 0.463485 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0150876 | 0.153742 | 0.735114 | 0.474578 |
