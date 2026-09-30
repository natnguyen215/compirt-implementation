# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.607158 |
| log_loss | 0.673627 |
| ece | 0.222216 |
| brier | 0.237924 |
| accuracy | 0.616078 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.146046 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.176575 |
| probability_p10 | 0.293515 |
| probability_p50 | 0.557117 |
| probability_p90 | 0.762137 |
| mean_predictive_variance | 0.217226 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0938343 |
| joint_tossup_event_log_loss | 6.7758 |
| buzz_position_mae | 0.137838 |
| buzz_position_median_absolute_error | 0.113972 |
| buzz_position_bias | -0.00358214 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.362037 |
| first_buzzer_mean_reciprocal_rank | 0.574517 |
| first_buzzer_log_loss | 1.65341 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.607158 |
| neg_average_precision | 0.314098 |
| neg_precision | 0.310394 |
| neg_recall | 0.502543 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.144306 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0519004 |
| no_buzz_calibration_error | 0.0359913 |
| no_buzz_brier | 0.0213995 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.00358214 | -0.0248693 |
| Q1 (0-.2) | 167 | 0.388366 | 0.405715 |
| Q2 (.2-.4) | 912 | 0.237669 | 0.233542 |
| Q3 (.4-.6) | 2115 | 0.0946894 | 0.0913608 |
| Q4 (.6-.8) | 2844 | -0.0225349 | -0.0221624 |
| Q5 (.8-1) | 3055 | -0.147418 | -0.139441 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.222216 | 0.237924 | 0.607158 | 0.673627 |
| tossup_correctness | tier | fall | 2842 | 0.244623 | 0.235053 | 0.613259 | 0.667177 |
| tossup_correctness | tier | nationals | 1564 | 0.185682 | 0.23608 | 0.604713 | 0.666209 |
| tossup_correctness | tier | regionals | 1937 | 0.205605 | 0.234972 | 0.608295 | 0.668265 |
| tossup_correctness | tier | winter | 2750 | 0.234314 | 0.244019 | 0.603461 | 0.688289 |
| tossup_correctness | category | Current Events | 126 | 0.300503 | 0.279206 | 0.576964 | 0.764139 |
| tossup_correctness | category | Fine Arts | 1071 | 0.232727 | 0.239739 | 0.617082 | 0.678382 |
| tossup_correctness | category | Geography | 185 | 0.243024 | 0.280023 | 0.546512 | 0.761559 |
| tossup_correctness | category | History | 1440 | 0.232197 | 0.244006 | 0.597739 | 0.684601 |
| tossup_correctness | category | Literature | 1422 | 0.225765 | 0.218602 | 0.576706 | 0.632811 |
| tossup_correctness | category | Mythology | 318 | 0.244639 | 0.244209 | 0.562229 | 0.688767 |
| tossup_correctness | category | Other Academic | 66 | 0.239002 | 0.236028 | 0.697648 | 0.664339 |
| tossup_correctness | category | Philosophy | 311 | 0.189474 | 0.22818 | 0.622818 | 0.649363 |
| tossup_correctness | category | Popular Culture | 102 | 0.428744 | 0.306813 | 0.503704 | 0.841645 |
| tossup_correctness | category | Religion | 358 | 0.179087 | 0.242423 | 0.603807 | 0.684364 |
| tossup_correctness | category | Science | 1433 | 0.217265 | 0.23839 | 0.630803 | 0.673739 |
| tossup_correctness | category | Social Science | 324 | 0.21568 | 0.242106 | 0.607546 | 0.680001 |
| tossup_correctness | category | Unknown | 1937 | 0.205605 | 0.234972 | 0.608295 | 0.668265 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.265256 | 0.287925 | 0.550595 | 0.784431 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.259549 | 0.269301 | 0.608249 | 0.746524 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.243495 | 0.247005 | 0.621608 | 0.695745 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.236576 | 0.23619 | 0.603129 | 0.670346 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.181229 | 0.221152 | 0.603353 | 0.633552 |
