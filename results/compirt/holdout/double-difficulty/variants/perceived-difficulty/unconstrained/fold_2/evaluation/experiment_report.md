# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.6581 |
| log_loss | 0.52133 |
| ece | 0.040565 |
| brier | 0.171117 |
| accuracy | 0.763422 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000756185 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.141076 |
| probability_p10 | 0.529679 |
| probability_p50 | 0.759118 |
| probability_p90 | 0.892019 |
| mean_predictive_variance | 0.175642 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.16566 |
| joint_tossup_event_log_loss | 7.59068 |
| buzz_position_mae | 0.323343 |
| buzz_position_median_absolute_error | 0.321944 |
| buzz_position_bias | -0.307388 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.354218 |
| first_buzzer_mean_reciprocal_rank | 0.565649 |
| first_buzzer_log_loss | 1.67754 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.6581 |
| neg_average_precision | 0.381889 |
| neg_precision | 0.495132 |
| neg_recall | 0.163078 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0335375 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.222787 |
| no_buzz_calibration_error | 0.209674 |
| no_buzz_brier | 0.0662907 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.307388 | -0.321662 |
| Q1 (0-.2) | 183 | 0.198814 | 0.192556 |
| Q2 (.2-.4) | 955 | 0.0204116 | 0.0159285 |
| Q3 (.4-.6) | 2239 | -0.158241 | -0.162742 |
| Q4 (.6-.8) | 2875 | -0.333508 | -0.333881 |
| Q5 (.8-1) | 3005 | -0.528529 | -0.532088 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.040565 | 0.171117 | 0.6581 | 0.52133 |
| tossup_correctness | tier | fall | 2798 | 0.0223425 | 0.159719 | 0.647501 | 0.495346 |
| tossup_correctness | tier | nationals | 1545 | 0.104552 | 0.197779 | 0.673893 | 0.579403 |
| tossup_correctness | tier | regionals | 2039 | 0.0487995 | 0.172002 | 0.664818 | 0.522828 |
| tossup_correctness | tier | winter | 2875 | 0.0350089 | 0.167252 | 0.653713 | 0.514349 |
| tossup_correctness | category | Current Events | 129 | 0.0717262 | 0.210543 | 0.633856 | 0.610938 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0507722 | 0.170905 | 0.624995 | 0.522141 |
| tossup_correctness | category | Geography | 180 | 0.0800969 | 0.206792 | 0.720721 | 0.604915 |
| tossup_correctness | category | History | 1454 | 0.040451 | 0.172747 | 0.664752 | 0.525158 |
| tossup_correctness | category | Literature | 1435 | 0.0365363 | 0.147734 | 0.639437 | 0.468602 |
| tossup_correctness | category | Mythology | 324 | 0.075055 | 0.162729 | 0.618561 | 0.502741 |
| tossup_correctness | category | Other Academic | 71 | 0.148705 | 0.226108 | 0.374728 | 0.648384 |
| tossup_correctness | category | Philosophy | 310 | 0.0246539 | 0.168143 | 0.677336 | 0.511297 |
| tossup_correctness | category | Popular Culture | 108 | 0.148883 | 0.127234 | 0.572049 | 0.422446 |
| tossup_correctness | category | Religion | 361 | 0.0617839 | 0.186277 | 0.640908 | 0.553426 |
| tossup_correctness | category | Science | 1445 | 0.0572333 | 0.181078 | 0.661908 | 0.543463 |
| tossup_correctness | category | Social Science | 327 | 0.0856244 | 0.179388 | 0.696161 | 0.542109 |
| tossup_correctness | category | Unknown | 2039 | 0.0487995 | 0.172002 | 0.664818 | 0.522828 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0803384 | 0.184407 | 0.639237 | 0.554613 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0293827 | 0.191433 | 0.634469 | 0.569081 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0311283 | 0.173162 | 0.668583 | 0.524783 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0474706 | 0.160165 | 0.66539 | 0.495501 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0496716 | 0.172805 | 0.649875 | 0.526268 |
