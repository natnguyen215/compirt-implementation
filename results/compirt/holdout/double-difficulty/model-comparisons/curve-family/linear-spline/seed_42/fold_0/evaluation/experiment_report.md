# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.724566 |
| log_loss | 0.563064 |
| ece | 0.113858 |
| brier | 0.182772 |
| accuracy | 0.735019 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0302313 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.276006 |
| probability_p10 | 0.246735 |
| probability_p50 | 0.75566 |
| probability_p90 | 0.978702 |
| mean_predictive_variance | 0.141595 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0930388 |
| joint_tossup_event_log_loss | 6.46448 |
| buzz_position_mae | 0.136218 |
| buzz_position_median_absolute_error | 0.112417 |
| buzz_position_bias | 0.00580359 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.397848 |
| first_buzzer_mean_reciprocal_rank | 0.602233 |
| first_buzzer_log_loss | 1.5867 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.724566 |
| neg_average_precision | 0.451444 |
| neg_precision | 0.442583 |
| neg_recall | 0.496334 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.177973 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0473446 |
| no_buzz_calibration_error | 0.0340749 |
| no_buzz_brier | 0.0185727 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.00580359 | -0.0147932 |
| Q1 (0-.2) | 197 | 0.38594 | 0.387779 |
| Q2 (.2-.4) | 985 | 0.238201 | 0.227737 |
| Q3 (.4-.6) | 2251 | 0.0987262 | 0.09289 |
| Q4 (.6-.8) | 2866 | -0.0208878 | -0.0201431 |
| Q5 (.8-1) | 2996 | -0.13988 | -0.130126 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.113858 | 0.182772 | 0.724566 | 0.563064 |
| tossup_correctness | tier | fall | 2933 | 0.118921 | 0.173991 | 0.719447 | 0.547083 |
| tossup_correctness | tier | nationals | 1584 | 0.119225 | 0.194015 | 0.726319 | 0.575304 |
| tossup_correctness | tier | regionals | 1886 | 0.114283 | 0.193556 | 0.722136 | 0.592772 |
| tossup_correctness | tier | winter | 2892 | 0.111813 | 0.178486 | 0.723233 | 0.553192 |
| tossup_correctness | category | Current Events | 124 | 0.148498 | 0.16235 | 0.79119 | 0.50683 |
| tossup_correctness | category | Fine Arts | 1103 | 0.121648 | 0.189431 | 0.705868 | 0.580753 |
| tossup_correctness | category | Geography | 197 | 0.105844 | 0.181771 | 0.802098 | 0.572387 |
| tossup_correctness | category | History | 1491 | 0.118672 | 0.171248 | 0.743988 | 0.517818 |
| tossup_correctness | category | Literature | 1472 | 0.101834 | 0.165657 | 0.709855 | 0.52863 |
| tossup_correctness | category | Mythology | 332 | 0.156024 | 0.178275 | 0.67049 | 0.569435 |
| tossup_correctness | category | Other Academic | 69 | 0.16851 | 0.187477 | 0.725113 | 0.563049 |
| tossup_correctness | category | Philosophy | 324 | 0.139259 | 0.17585 | 0.708346 | 0.527508 |
| tossup_correctness | category | Popular Culture | 102 | 0.159021 | 0.17656 | 0.594464 | 0.59905 |
| tossup_correctness | category | Religion | 372 | 0.096917 | 0.192708 | 0.735269 | 0.584179 |
| tossup_correctness | category | Science | 1487 | 0.123688 | 0.19455 | 0.706908 | 0.592308 |
| tossup_correctness | category | Social Science | 336 | 0.113518 | 0.183528 | 0.76428 | 0.569417 |
| tossup_correctness | category | Unknown | 1886 | 0.114283 | 0.193556 | 0.722136 | 0.592772 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.18354 | 0.221057 | 0.714191 | 0.667314 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.117391 | 0.190667 | 0.748529 | 0.574249 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.118371 | 0.183675 | 0.713322 | 0.569592 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.102279 | 0.169702 | 0.718369 | 0.537429 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.125762 | 0.189482 | 0.726813 | 0.572148 |
