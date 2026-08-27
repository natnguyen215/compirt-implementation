# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709045 |
| log_loss | 0.501075 |
| ece | 0.0713461 |
| brier | 0.162502 |
| accuracy | 0.779075 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00903084 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.163377 |
| probability_p10 | 0.473126 |
| probability_p50 | 0.728518 |
| probability_p90 | 0.893444 |
| mean_predictive_variance | 0.182322 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.111109 |
| joint_tossup_event_log_loss | 6.71039 |
| buzz_position_mae | 0.168561 |
| buzz_position_median_absolute_error | 0.151878 |
| buzz_position_bias | -0.0835565 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.339868 |
| first_buzzer_mean_reciprocal_rank | 0.553206 |
| first_buzzer_log_loss | 1.71078 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709045 |
| neg_average_precision | 0.456494 |
| neg_precision | 0.536412 |
| neg_recall | 0.289272 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.16959 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0114402 |
| no_buzz_calibration_error | -0.00374418 |
| no_buzz_brier | 0.0134451 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0835565 | -0.102661 |
| Q1 (0-.2) | 192 | 0.364216 | 0.372247 |
| Q2 (.2-.4) | 889 | 0.182273 | 0.180152 |
| Q3 (.4-.6) | 2210 | 0.026278 | 0.0235945 |
| Q4 (.6-.8) | 2869 | -0.113476 | -0.112068 |
| Q5 (.8-1) | 2920 | -0.247663 | -0.245752 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0713461 | 0.162502 | 0.709045 | 0.501075 |
| tossup_correctness | tier | fall | 2817 | 0.0571326 | 0.15643 | 0.699799 | 0.488061 |
| tossup_correctness | tier | nationals | 1542 | 0.0821653 | 0.177131 | 0.723874 | 0.532556 |
| tossup_correctness | tier | regionals | 1934 | 0.0769891 | 0.167822 | 0.714324 | 0.512796 |
| tossup_correctness | tier | winter | 2787 | 0.07883 | 0.156852 | 0.697876 | 0.488678 |
| tossup_correctness | category | Current Events | 125 | 0.0465587 | 0.184914 | 0.702703 | 0.551226 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0706122 | 0.156427 | 0.729227 | 0.487279 |
| tossup_correctness | category | Geography | 185 | 0.0987104 | 0.171044 | 0.772168 | 0.516166 |
| tossup_correctness | category | History | 1443 | 0.0703507 | 0.161635 | 0.732972 | 0.495356 |
| tossup_correctness | category | Literature | 1411 | 0.0757119 | 0.152722 | 0.650232 | 0.480332 |
| tossup_correctness | category | Mythology | 320 | 0.108154 | 0.157552 | 0.663088 | 0.499093 |
| tossup_correctness | category | Other Academic | 64 | 0.0723313 | 0.178356 | 0.660156 | 0.538146 |
| tossup_correctness | category | Philosophy | 312 | 0.0887364 | 0.156896 | 0.657613 | 0.488876 |
| tossup_correctness | category | Popular Culture | 104 | 0.0902249 | 0.140165 | 0.522727 | 0.468044 |
| tossup_correctness | category | Religion | 358 | 0.0675353 | 0.174819 | 0.746193 | 0.525907 |
| tossup_correctness | category | Science | 1431 | 0.0701667 | 0.166553 | 0.69392 | 0.510372 |
| tossup_correctness | category | Social Science | 321 | 0.0845253 | 0.166622 | 0.745127 | 0.513196 |
| tossup_correctness | category | Unknown | 1934 | 0.0769891 | 0.167822 | 0.714324 | 0.512796 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0810217 | 0.180974 | 0.764282 | 0.541304 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0534509 | 0.166955 | 0.745198 | 0.508081 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0627347 | 0.170244 | 0.687214 | 0.521986 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0738235 | 0.157297 | 0.687731 | 0.489388 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0849041 | 0.159184 | 0.726288 | 0.491954 |
