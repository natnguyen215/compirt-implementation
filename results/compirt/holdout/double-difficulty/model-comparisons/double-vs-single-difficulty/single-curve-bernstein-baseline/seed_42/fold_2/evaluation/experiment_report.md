# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.623769 |
| log_loss | 0.744138 |
| ece | 0.197272 |
| brier | 0.242461 |
| accuracy | 0.650535 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.113644 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.293163 |
| probability_p10 | 0.15061 |
| probability_p50 | 0.685242 |
| probability_p90 | 0.946534 |
| mean_predictive_variance | 0.151328 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0965915 |
| joint_tossup_event_log_loss | 6.74156 |
| buzz_position_mae | 0.138154 |
| buzz_position_median_absolute_error | 0.112823 |
| buzz_position_bias | 0.0109094 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.400454 |
| first_buzzer_mean_reciprocal_rank | 0.605651 |
| first_buzzer_log_loss | 1.5847 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.623769 |
| neg_average_precision | 0.335447 |
| neg_precision | 0.33065 |
| neg_recall | 0.470454 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.141702 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0626236 |
| no_buzz_calibration_error | 0.0495106 |
| no_buzz_brier | 0.0247092 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.0109094 | -0.00919825 |
| Q1 (0-.2) | 183 | 0.396378 | 0.406901 |
| Q2 (.2-.4) | 955 | 0.23968 | 0.236331 |
| Q3 (.4-.6) | 2239 | 0.104585 | 0.102527 |
| Q4 (.6-.8) | 2875 | -0.0113935 | -0.00857957 |
| Q5 (.8-1) | 3005 | -0.133728 | -0.124608 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.197272 | 0.242461 | 0.623769 | 0.744138 |
| tossup_correctness | tier | fall | 2798 | 0.194386 | 0.230736 | 0.644384 | 0.702849 |
| tossup_correctness | tier | nationals | 1545 | 0.187463 | 0.247815 | 0.610794 | 0.770364 |
| tossup_correctness | tier | regionals | 2039 | 0.20355 | 0.250586 | 0.617413 | 0.774635 |
| tossup_correctness | tier | winter | 2875 | 0.200901 | 0.245233 | 0.623791 | 0.7486 |
| tossup_correctness | category | Current Events | 129 | 0.227139 | 0.287441 | 0.567875 | 0.864764 |
| tossup_correctness | category | Fine Arts | 1074 | 0.224634 | 0.258972 | 0.614046 | 0.801393 |
| tossup_correctness | category | Geography | 180 | 0.181204 | 0.260323 | 0.609348 | 0.750007 |
| tossup_correctness | category | History | 1454 | 0.171941 | 0.225282 | 0.636271 | 0.703492 |
| tossup_correctness | category | Literature | 1435 | 0.224285 | 0.237898 | 0.579235 | 0.742533 |
| tossup_correctness | category | Mythology | 324 | 0.244694 | 0.259773 | 0.61647 | 0.756766 |
| tossup_correctness | category | Other Academic | 71 | 0.250362 | 0.27164 | 0.533769 | 0.814118 |
| tossup_correctness | category | Philosophy | 310 | 0.202886 | 0.242716 | 0.654776 | 0.720819 |
| tossup_correctness | category | Popular Culture | 108 | 0.359614 | 0.290463 | 0.569444 | 0.898433 |
| tossup_correctness | category | Religion | 361 | 0.21001 | 0.254533 | 0.659043 | 0.759858 |
| tossup_correctness | category | Science | 1445 | 0.153753 | 0.22382 | 0.65345 | 0.684412 |
| tossup_correctness | category | Social Science | 327 | 0.187971 | 0.235873 | 0.657031 | 0.692908 |
| tossup_correctness | category | Unknown | 2039 | 0.20355 | 0.250586 | 0.617413 | 0.774635 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.507007 | 0.439539 | 0.696026 | 1.44379 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.344179 | 0.33423 | 0.655278 | 1.01005 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.240538 | 0.26583 | 0.661128 | 0.79947 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.174622 | 0.224417 | 0.627744 | 0.682356 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.124856 | 0.201147 | 0.606447 | 0.634903 |
