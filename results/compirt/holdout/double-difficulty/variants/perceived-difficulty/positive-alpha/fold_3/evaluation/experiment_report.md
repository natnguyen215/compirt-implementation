# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.601595 |
| log_loss | 0.630779 |
| ece | 0.202388 |
| brier | 0.22 |
| accuracy | 0.650551 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.119493 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.145772 |
| probability_p10 | 0.356658 |
| probability_p50 | 0.586181 |
| probability_p90 | 0.743963 |
| mean_predictive_variance | 0.224173 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0932378 |
| joint_tossup_event_log_loss | 6.59304 |
| buzz_position_mae | 0.135432 |
| buzz_position_median_absolute_error | 0.110562 |
| buzz_position_bias | -0.00190791 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.395705 |
| first_buzzer_mean_reciprocal_rank | 0.600064 |
| first_buzzer_log_loss | 1.59138 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.601595 |
| neg_average_precision | 0.313931 |
| neg_precision | 0.304222 |
| neg_recall | 0.403736 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.134976 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0468609 |
| no_buzz_calibration_error | 0.0316765 |
| no_buzz_brier | 0.0182009 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.00190791 | -0.0250941 |
| Q1 (0-.2) | 192 | 0.392401 | 0.399103 |
| Q2 (.2-.4) | 889 | 0.227799 | 0.226087 |
| Q3 (.4-.6) | 2210 | 0.0855683 | 0.079396 |
| Q4 (.6-.8) | 2869 | -0.0288221 | -0.0254194 |
| Q5 (.8-1) | 2920 | -0.137532 | -0.125512 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.202388 | 0.22 | 0.601595 | 0.630779 |
| tossup_correctness | tier | fall | 2817 | 0.221536 | 0.219189 | 0.612393 | 0.628997 |
| tossup_correctness | tier | nationals | 1542 | 0.143572 | 0.216777 | 0.590459 | 0.623157 |
| tossup_correctness | tier | regionals | 1934 | 0.178339 | 0.215681 | 0.619432 | 0.62204 |
| tossup_correctness | tier | winter | 2787 | 0.232264 | 0.225601 | 0.596473 | 0.642861 |
| tossup_correctness | category | Current Events | 125 | 0.152233 | 0.228641 | 0.612408 | 0.650525 |
| tossup_correctness | category | Fine Arts | 1072 | 0.189747 | 0.21923 | 0.579957 | 0.629334 |
| tossup_correctness | category | Geography | 185 | 0.178674 | 0.251272 | 0.529091 | 0.696593 |
| tossup_correctness | category | History | 1443 | 0.20169 | 0.219813 | 0.607092 | 0.63034 |
| tossup_correctness | category | Literature | 1411 | 0.212034 | 0.205418 | 0.575534 | 0.598989 |
| tossup_correctness | category | Mythology | 320 | 0.237231 | 0.225131 | 0.577547 | 0.641272 |
| tossup_correctness | category | Other Academic | 64 | 0.193353 | 0.219222 | 0.591146 | 0.628838 |
| tossup_correctness | category | Philosophy | 312 | 0.215119 | 0.204019 | 0.617484 | 0.595882 |
| tossup_correctness | category | Popular Culture | 104 | 0.360261 | 0.275313 | 0.566761 | 0.752466 |
| tossup_correctness | category | Religion | 358 | 0.192269 | 0.228993 | 0.625078 | 0.649209 |
| tossup_correctness | category | Science | 1431 | 0.229148 | 0.231584 | 0.603305 | 0.655659 |
| tossup_correctness | category | Social Science | 321 | 0.190036 | 0.223138 | 0.616134 | 0.637295 |
| tossup_correctness | category | Unknown | 1934 | 0.178339 | 0.215681 | 0.619432 | 0.62204 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.195136 | 0.22199 | 0.70561 | 0.635349 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.210378 | 0.233991 | 0.630096 | 0.66073 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.206124 | 0.224577 | 0.610376 | 0.640822 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.214861 | 0.216806 | 0.596191 | 0.624066 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.185835 | 0.215286 | 0.577715 | 0.620353 |
