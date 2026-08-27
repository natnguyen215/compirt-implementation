# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709342 |
| log_loss | 0.498123 |
| ece | 0.0618507 |
| brier | 0.162254 |
| accuracy | 0.773238 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00319383 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.171978 |
| probability_p10 | 0.461333 |
| probability_p50 | 0.744939 |
| probability_p90 | 0.895415 |
| mean_predictive_variance | 0.177002 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101401 |
| joint_tossup_event_log_loss | 6.59926 |
| buzz_position_mae | 0.152138 |
| buzz_position_median_absolute_error | 0.136049 |
| buzz_position_bias | -0.0491965 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.352093 |
| first_buzzer_mean_reciprocal_rank | 0.567675 |
| first_buzzer_log_loss | 1.67235 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709342 |
| neg_average_precision | 0.448278 |
| neg_precision | 0.51234 |
| neg_recall | 0.288314 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.183788 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0151345 |
| no_buzz_calibration_error | -4.99214e-05 |
| no_buzz_brier | 0.0137026 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0491965 | -0.0706015 |
| Q1 (0-.2) | 192 | 0.386994 | 0.393894 |
| Q2 (.2-.4) | 889 | 0.208358 | 0.20798 |
| Q3 (.4-.6) | 2210 | 0.0556641 | 0.0544072 |
| Q4 (.6-.8) | 2869 | -0.0800241 | -0.0777854 |
| Q5 (.8-1) | 2920 | -0.205365 | -0.202284 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0618507 | 0.162254 | 0.709342 | 0.498123 |
| tossup_correctness | tier | fall | 2817 | 0.0622898 | 0.159101 | 0.701589 | 0.491561 |
| tossup_correctness | tier | nationals | 1542 | 0.0496558 | 0.171987 | 0.726217 | 0.519018 |
| tossup_correctness | tier | regionals | 1934 | 0.0558612 | 0.16581 | 0.713974 | 0.506084 |
| tossup_correctness | tier | winter | 2787 | 0.0748237 | 0.157589 | 0.698617 | 0.487671 |
| tossup_correctness | category | Current Events | 125 | 0.0449383 | 0.177253 | 0.747543 | 0.526431 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0669601 | 0.15842 | 0.722701 | 0.488574 |
| tossup_correctness | category | Geography | 185 | 0.112507 | 0.168509 | 0.777063 | 0.511133 |
| tossup_correctness | category | History | 1443 | 0.0686096 | 0.163797 | 0.730032 | 0.497917 |
| tossup_correctness | category | Literature | 1411 | 0.0608898 | 0.150149 | 0.659255 | 0.472275 |
| tossup_correctness | category | Mythology | 320 | 0.0701608 | 0.156698 | 0.663982 | 0.49352 |
| tossup_correctness | category | Other Academic | 64 | 0.0842549 | 0.191872 | 0.638021 | 0.567974 |
| tossup_correctness | category | Philosophy | 312 | 0.0895596 | 0.155594 | 0.660581 | 0.483027 |
| tossup_correctness | category | Popular Culture | 104 | 0.0856112 | 0.130168 | 0.602983 | 0.435457 |
| tossup_correctness | category | Religion | 358 | 0.0739493 | 0.181772 | 0.713383 | 0.541862 |
| tossup_correctness | category | Science | 1431 | 0.071044 | 0.166375 | 0.698549 | 0.508221 |
| tossup_correctness | category | Social Science | 321 | 0.0723374 | 0.166837 | 0.731044 | 0.509918 |
| tossup_correctness | category | Unknown | 1934 | 0.0558612 | 0.16581 | 0.713974 | 0.506084 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0859502 | 0.184683 | 0.747555 | 0.549418 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0531418 | 0.164768 | 0.74921 | 0.50268 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0497388 | 0.171002 | 0.683435 | 0.520661 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0602867 | 0.156678 | 0.691968 | 0.484643 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0811587 | 0.158872 | 0.728403 | 0.48955 |
