# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.677067 |
| log_loss | 0.54457 |
| ece | 0.0865596 |
| brier | 0.179951 |
| accuracy | 0.740022 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0333333 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.207216 |
| probability_p10 | 0.393985 |
| probability_p50 | 0.737791 |
| probability_p90 | 0.923301 |
| mean_predictive_variance | 0.169314 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0940055 |
| joint_tossup_event_log_loss | 6.55311 |
| buzz_position_mae | 0.14021 |
| buzz_position_median_absolute_error | 0.119821 |
| buzz_position_bias | -0.0134417 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.390615 |
| first_buzzer_mean_reciprocal_rank | 0.596126 |
| first_buzzer_log_loss | 1.61388 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.677067 |
| neg_average_precision | 0.361498 |
| neg_precision | 0.400643 |
| neg_recall | 0.296525 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.106413 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.058019 |
| no_buzz_calibration_error | 0.0462919 |
| no_buzz_brier | 0.0201298 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0134417 | -0.032497 |
| Q1 (0-.2) | 179 | 0.37503 | 0.369765 |
| Q2 (.2-.4) | 957 | 0.224663 | 0.224092 |
| Q3 (.4-.6) | 2203 | 0.0852326 | 0.0834867 |
| Q4 (.6-.8) | 2978 | -0.0356624 | -0.0322535 |
| Q5 (.8-1) | 2953 | -0.165358 | -0.159918 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0865596 | 0.179951 | 0.677067 | 0.54457 |
| tossup_correctness | tier | fall | 2876 | 0.10968 | 0.179541 | 0.67101 | 0.544296 |
| tossup_correctness | tier | nationals | 1579 | 0.0455102 | 0.184588 | 0.678771 | 0.553551 |
| tossup_correctness | tier | regionals | 1990 | 0.0852298 | 0.176576 | 0.696766 | 0.533274 |
| tossup_correctness | tier | winter | 2825 | 0.0997306 | 0.180155 | 0.674326 | 0.547785 |
| tossup_correctness | category | Current Events | 123 | 0.111251 | 0.171509 | 0.731842 | 0.513239 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0961855 | 0.182101 | 0.67876 | 0.55622 |
| tossup_correctness | category | Geography | 191 | 0.0923196 | 0.186041 | 0.747047 | 0.565269 |
| tossup_correctness | category | History | 1469 | 0.065037 | 0.178568 | 0.693087 | 0.535183 |
| tossup_correctness | category | Literature | 1436 | 0.0996629 | 0.168759 | 0.652888 | 0.523606 |
| tossup_correctness | category | Mythology | 325 | 0.144503 | 0.177234 | 0.588593 | 0.538993 |
| tossup_correctness | category | Other Academic | 67 | 0.151083 | 0.171013 | 0.707547 | 0.508874 |
| tossup_correctness | category | Philosophy | 322 | 0.108831 | 0.166924 | 0.676634 | 0.504626 |
| tossup_correctness | category | Popular Culture | 100 | 0.244879 | 0.196048 | 0.526047 | 0.62096 |
| tossup_correctness | category | Religion | 365 | 0.0810835 | 0.203734 | 0.637751 | 0.595059 |
| tossup_correctness | category | Science | 1456 | 0.0958088 | 0.190428 | 0.654923 | 0.571383 |
| tossup_correctness | category | Social Science | 333 | 0.0979615 | 0.187399 | 0.705944 | 0.561072 |
| tossup_correctness | category | Unknown | 1990 | 0.0852298 | 0.176576 | 0.696766 | 0.533274 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.202042 | 0.207931 | 0.748093 | 0.635495 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.151573 | 0.20058 | 0.70353 | 0.592438 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0882037 | 0.180947 | 0.691078 | 0.547537 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0785472 | 0.169468 | 0.674041 | 0.519863 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0678791 | 0.181399 | 0.658667 | 0.546247 |
