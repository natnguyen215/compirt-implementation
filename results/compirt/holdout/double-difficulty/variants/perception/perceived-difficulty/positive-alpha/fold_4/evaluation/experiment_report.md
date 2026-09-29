# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.60599 |
| log_loss | 0.636827 |
| ece | 0.211671 |
| brier | 0.222695 |
| accuracy | 0.649407 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.123948 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.149863 |
| probability_p10 | 0.343482 |
| probability_p50 | 0.581456 |
| probability_p90 | 0.741257 |
| mean_predictive_variance | 0.223736 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950001 |
| joint_tossup_event_log_loss | 6.67489 |
| buzz_position_mae | 0.136863 |
| buzz_position_median_absolute_error | 0.111577 |
| buzz_position_bias | 0.00501506 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.38932 |
| first_buzzer_mean_reciprocal_rank | 0.595546 |
| first_buzzer_log_loss | 1.62063 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.60599 |
| neg_average_precision | 0.305573 |
| neg_precision | 0.306501 |
| neg_recall | 0.433127 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.137812 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0479197 |
| no_buzz_calibration_error | 0.0361927 |
| no_buzz_brier | 0.0181184 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.00501506 | -0.0167685 |
| Q1 (0-.2) | 179 | 0.393786 | 0.397154 |
| Q2 (.2-.4) | 957 | 0.239818 | 0.231117 |
| Q3 (.4-.6) | 2203 | 0.0971621 | 0.0929346 |
| Q4 (.6-.8) | 2978 | -0.0205563 | -0.0153668 |
| Q5 (.8-1) | 2953 | -0.137601 | -0.125953 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.211671 | 0.222695 | 0.60599 | 0.636827 |
| tossup_correctness | tier | fall | 2876 | 0.234249 | 0.220555 | 0.621658 | 0.63232 |
| tossup_correctness | tier | nationals | 1579 | 0.13717 | 0.214216 | 0.608267 | 0.617544 |
| tossup_correctness | tier | regionals | 1990 | 0.198365 | 0.219832 | 0.60762 | 0.630888 |
| tossup_correctness | tier | winter | 2825 | 0.240006 | 0.231631 | 0.602374 | 0.656378 |
| tossup_correctness | category | Current Events | 123 | 0.224957 | 0.227743 | 0.619956 | 0.647261 |
| tossup_correctness | category | Fine Arts | 1093 | 0.197204 | 0.219034 | 0.617297 | 0.628836 |
| tossup_correctness | category | Geography | 191 | 0.171465 | 0.256004 | 0.531073 | 0.707051 |
| tossup_correctness | category | History | 1469 | 0.188553 | 0.216794 | 0.620171 | 0.623432 |
| tossup_correctness | category | Literature | 1436 | 0.218377 | 0.202515 | 0.61076 | 0.593975 |
| tossup_correctness | category | Mythology | 325 | 0.293347 | 0.239006 | 0.463861 | 0.671279 |
| tossup_correctness | category | Other Academic | 67 | 0.254793 | 0.232754 | 0.621294 | 0.660578 |
| tossup_correctness | category | Philosophy | 322 | 0.196718 | 0.197334 | 0.664719 | 0.58183 |
| tossup_correctness | category | Popular Culture | 100 | 0.359374 | 0.242756 | 0.588355 | 0.683812 |
| tossup_correctness | category | Religion | 365 | 0.174642 | 0.226624 | 0.630701 | 0.64509 |
| tossup_correctness | category | Science | 1456 | 0.25014 | 0.247858 | 0.573676 | 0.691299 |
| tossup_correctness | category | Social Science | 333 | 0.185679 | 0.230139 | 0.606493 | 0.65174 |
| tossup_correctness | category | Unknown | 1990 | 0.198365 | 0.219832 | 0.60762 | 0.630888 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.258822 | 0.246055 | 0.639303 | 0.685625 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.231143 | 0.240269 | 0.606342 | 0.675021 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.224945 | 0.228401 | 0.629039 | 0.650506 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.222411 | 0.220556 | 0.599979 | 0.63218 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.181824 | 0.213485 | 0.593341 | 0.615974 |
