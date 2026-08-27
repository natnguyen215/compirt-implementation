# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.669853 |
| log_loss | 0.551088 |
| ece | 0.0749707 |
| brier | 0.182337 |
| accuracy | 0.739332 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0248461 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.203422 |
| probability_p10 | 0.405287 |
| probability_p50 | 0.744397 |
| probability_p90 | 0.926752 |
| mean_predictive_variance | 0.168088 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950767 |
| joint_tossup_event_log_loss | 6.5439 |
| buzz_position_mae | 0.140411 |
| buzz_position_median_absolute_error | 0.119539 |
| buzz_position_bias | -0.0127499 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.39354 |
| first_buzzer_mean_reciprocal_rank | 0.599039 |
| first_buzzer_log_loss | 1.58951 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.669853 |
| neg_average_precision | 0.367138 |
| neg_precision | 0.421233 |
| neg_recall | 0.281722 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.10896 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0602481 |
| no_buzz_calibration_error | 0.0471351 |
| no_buzz_brier | 0.0221059 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0127499 | -0.0302205 |
| Q1 (0-.2) | 183 | 0.381147 | 0.385672 |
| Q2 (.2-.4) | 955 | 0.224813 | 0.219086 |
| Q3 (.4-.6) | 2239 | 0.0822857 | 0.0785445 |
| Q4 (.6-.8) | 2875 | -0.0332089 | -0.0305569 |
| Q5 (.8-1) | 3005 | -0.163472 | -0.15629 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0749707 | 0.182337 | 0.669853 | 0.551088 |
| tossup_correctness | tier | fall | 2798 | 0.10534 | 0.180825 | 0.677929 | 0.551732 |
| tossup_correctness | tier | nationals | 1545 | 0.0387528 | 0.185991 | 0.67951 | 0.551295 |
| tossup_correctness | tier | regionals | 2039 | 0.0896824 | 0.188422 | 0.64816 | 0.565567 |
| tossup_correctness | tier | winter | 2875 | 0.0743517 | 0.17753 | 0.675498 | 0.54008 |
| tossup_correctness | category | Current Events | 129 | 0.147946 | 0.217194 | 0.644673 | 0.640013 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0968168 | 0.183782 | 0.666312 | 0.550475 |
| tossup_correctness | category | Geography | 180 | 0.0911708 | 0.195703 | 0.73665 | 0.571489 |
| tossup_correctness | category | History | 1454 | 0.0738594 | 0.179275 | 0.674553 | 0.542557 |
| tossup_correctness | category | Literature | 1435 | 0.0752573 | 0.16131 | 0.675443 | 0.500492 |
| tossup_correctness | category | Mythology | 324 | 0.120863 | 0.183442 | 0.61798 | 0.572909 |
| tossup_correctness | category | Other Academic | 71 | 0.192751 | 0.196208 | 0.575163 | 0.634339 |
| tossup_correctness | category | Philosophy | 310 | 0.0671377 | 0.17432 | 0.705108 | 0.525141 |
| tossup_correctness | category | Popular Culture | 108 | 0.277031 | 0.207629 | 0.493056 | 0.692188 |
| tossup_correctness | category | Religion | 361 | 0.0792243 | 0.186533 | 0.670358 | 0.553951 |
| tossup_correctness | category | Science | 1445 | 0.0646222 | 0.189043 | 0.678173 | 0.564841 |
| tossup_correctness | category | Social Science | 327 | 0.0859511 | 0.185311 | 0.715634 | 0.550827 |
| tossup_correctness | category | Unknown | 2039 | 0.0896824 | 0.188422 | 0.64816 | 0.565567 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.19244 | 0.204405 | 0.757196 | 0.592069 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.131101 | 0.195476 | 0.699763 | 0.583827 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0709857 | 0.183668 | 0.690498 | 0.556198 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0663854 | 0.171276 | 0.66396 | 0.525063 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0633814 | 0.18641 | 0.643477 | 0.559278 |
