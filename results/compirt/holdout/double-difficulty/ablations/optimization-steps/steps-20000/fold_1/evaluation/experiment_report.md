# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.708619 |
| log_loss | 0.498203 |
| ece | 0.0129313 |
| brier | 0.162059 |
| accuracy | 0.772242 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0101177 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.152276 |
| probability_p10 | 0.553869 |
| probability_p50 | 0.809278 |
| probability_p90 | 0.923975 |
| mean_predictive_variance | 0.154435 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0937498 |
| joint_tossup_event_log_loss | 6.45292 |
| buzz_position_mae | 0.138577 |
| buzz_position_median_absolute_error | 0.117046 |
| buzz_position_bias | -0.00711534 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.362587 |
| first_buzzer_mean_reciprocal_rank | 0.57602 |
| first_buzzer_log_loss | 1.64308 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.708619 |
| neg_average_precision | 0.443197 |
| neg_precision | 0.572555 |
| neg_recall | 0.167822 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.185309 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00987379 |
| no_buzz_calibration_error | -0.0060353 |
| no_buzz_brier | 0.0153507 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.00711534 | -0.0296568 |
| Q1 (0-.2) | 167 | 0.399599 | 0.406544 |
| Q2 (.2-.4) | 912 | 0.241226 | 0.239235 |
| Q3 (.4-.6) | 2115 | 0.0943867 | 0.0925228 |
| Q4 (.6-.8) | 2844 | -0.0286216 | -0.0294113 |
| Q5 (.8-1) | 3055 | -0.153734 | -0.146671 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0129313 | 0.162059 | 0.708619 | 0.498203 |
| tossup_correctness | tier | fall | 2842 | 0.0153143 | 0.149345 | 0.726332 | 0.464632 |
| tossup_correctness | tier | nationals | 1564 | 0.0417829 | 0.17956 | 0.714754 | 0.540088 |
| tossup_correctness | tier | regionals | 1937 | 0.0199917 | 0.167107 | 0.691364 | 0.51122 |
| tossup_correctness | tier | winter | 2750 | 0.0147137 | 0.161688 | 0.696626 | 0.499907 |
| tossup_correctness | category | Current Events | 126 | 0.0985532 | 0.159041 | 0.724849 | 0.488875 |
| tossup_correctness | category | Fine Arts | 1071 | 0.028639 | 0.152614 | 0.744706 | 0.472056 |
| tossup_correctness | category | Geography | 185 | 0.0737109 | 0.162066 | 0.798726 | 0.492999 |
| tossup_correctness | category | History | 1440 | 0.0348797 | 0.168614 | 0.703127 | 0.513393 |
| tossup_correctness | category | Literature | 1422 | 0.0234682 | 0.143724 | 0.673434 | 0.456377 |
| tossup_correctness | category | Mythology | 318 | 0.044212 | 0.154373 | 0.654933 | 0.488591 |
| tossup_correctness | category | Other Academic | 66 | 0.10519 | 0.173703 | 0.795073 | 0.516045 |
| tossup_correctness | category | Philosophy | 311 | 0.0738349 | 0.172862 | 0.711971 | 0.517614 |
| tossup_correctness | category | Popular Culture | 102 | 0.0701233 | 0.110002 | 0.526852 | 0.384992 |
| tossup_correctness | category | Religion | 358 | 0.0282463 | 0.179803 | 0.71285 | 0.540828 |
| tossup_correctness | category | Science | 1433 | 0.028643 | 0.173431 | 0.699302 | 0.526083 |
| tossup_correctness | category | Social Science | 324 | 0.049922 | 0.156883 | 0.782094 | 0.481871 |
| tossup_correctness | category | Unknown | 1937 | 0.0199917 | 0.167107 | 0.691364 | 0.51122 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.090616 | 0.209206 | 0.592262 | 0.621002 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0212555 | 0.173272 | 0.719704 | 0.524176 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0266523 | 0.164963 | 0.71081 | 0.504691 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0101906 | 0.15541 | 0.69287 | 0.484178 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0152274 | 0.160312 | 0.720509 | 0.492301 |
