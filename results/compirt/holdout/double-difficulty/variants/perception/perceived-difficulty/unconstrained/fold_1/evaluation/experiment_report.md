# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.653021 |
| log_loss | 0.523943 |
| ece | 0.029309 |
| brier | 0.171912 |
| accuracy | 0.765314 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00318927 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.129878 |
| probability_p10 | 0.556782 |
| probability_p50 | 0.762264 |
| probability_p90 | 0.891555 |
| mean_predictive_variance | 0.175 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.169461 |
| joint_tossup_event_log_loss | 7.6164 |
| buzz_position_mae | 0.333751 |
| buzz_position_median_absolute_error | 0.33794 |
| buzz_position_bias | -0.320288 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34928 |
| first_buzzer_mean_reciprocal_rank | 0.561948 |
| first_buzzer_log_loss | 1.68307 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.653021 |
| neg_average_precision | 0.378498 |
| neg_precision | 0.530786 |
| neg_recall | 0.11558 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0316161 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.224212 |
| no_buzz_calibration_error | 0.208303 |
| no_buzz_brier | 0.0685025 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.320288 | -0.33794 |
| Q1 (0-.2) | 167 | 0.178151 | 0.18213 |
| Q2 (.2-.4) | 912 | 0.0165176 | 0.0119976 |
| Q3 (.4-.6) | 2115 | -0.161784 | -0.163293 |
| Q4 (.6-.8) | 2844 | -0.341566 | -0.342985 |
| Q5 (.8-1) | 3055 | -0.538005 | -0.542308 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.029309 | 0.171912 | 0.653021 | 0.523943 |
| tossup_correctness | tier | fall | 2842 | 0.0138904 | 0.155266 | 0.682925 | 0.483299 |
| tossup_correctness | tier | nationals | 1564 | 0.095886 | 0.196324 | 0.672627 | 0.580169 |
| tossup_correctness | tier | regionals | 1937 | 0.0491588 | 0.179766 | 0.619959 | 0.542809 |
| tossup_correctness | tier | winter | 2750 | 0.0239106 | 0.169699 | 0.642587 | 0.520681 |
| tossup_correctness | category | Current Events | 126 | 0.081094 | 0.171289 | 0.693566 | 0.518152 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0410773 | 0.165757 | 0.667357 | 0.509946 |
| tossup_correctness | category | Geography | 185 | 0.0818156 | 0.192774 | 0.674972 | 0.57196 |
| tossup_correctness | category | History | 1440 | 0.0266141 | 0.172582 | 0.66907 | 0.525287 |
| tossup_correctness | category | Literature | 1422 | 0.0358256 | 0.149138 | 0.624516 | 0.472676 |
| tossup_correctness | category | Mythology | 318 | 0.0754341 | 0.158664 | 0.665755 | 0.494828 |
| tossup_correctness | category | Other Academic | 66 | 0.0619776 | 0.210811 | 0.591265 | 0.609617 |
| tossup_correctness | category | Philosophy | 311 | 0.058439 | 0.181278 | 0.650589 | 0.543248 |
| tossup_correctness | category | Popular Culture | 102 | 0.134146 | 0.123104 | 0.616667 | 0.412374 |
| tossup_correctness | category | Religion | 358 | 0.0677845 | 0.199572 | 0.638835 | 0.584903 |
| tossup_correctness | category | Science | 1433 | 0.0353667 | 0.179867 | 0.664376 | 0.541939 |
| tossup_correctness | category | Social Science | 324 | 0.0461285 | 0.176319 | 0.690237 | 0.53206 |
| tossup_correctness | category | Unknown | 1937 | 0.0491588 | 0.179766 | 0.619959 | 0.542809 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0629054 | 0.193708 | 0.643207 | 0.576532 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0300448 | 0.187181 | 0.646586 | 0.559416 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0150839 | 0.172794 | 0.666433 | 0.524821 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0378866 | 0.165576 | 0.64629 | 0.508341 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0414829 | 0.17145 | 0.650843 | 0.524396 |
