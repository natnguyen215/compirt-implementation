# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709685 |
| log_loss | 0.590703 |
| ece | 0.187329 |
| brier | 0.20248 |
| accuracy | 0.689964 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0742141 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.21318 |
| probability_p10 | 0.272286 |
| probability_p50 | 0.597937 |
| probability_p90 | 0.84918 |
| mean_predictive_variance | 0.198648 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102513 |
| joint_tossup_event_log_loss | 6.72128 |
| buzz_position_mae | 0.152093 |
| buzz_position_median_absolute_error | 0.133384 |
| buzz_position_bias | -0.0432934 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.358431 |
| first_buzzer_mean_reciprocal_rank | 0.569125 |
| first_buzzer_log_loss | 1.66558 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709685 |
| neg_average_precision | 0.447593 |
| neg_precision | 0.394145 |
| neg_recall | 0.585891 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190318 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.013754 |
| no_buzz_calibration_error | 0.000641 |
| no_buzz_brier | 0.0128588 |
| full_pmf_max_mass_error | 1.11022e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0432934 | -0.0634124 |
| Q1 (0-.2) | 183 | 0.386196 | 0.399177 |
| Q2 (.2-.4) | 955 | 0.216185 | 0.212089 |
| Q3 (.4-.6) | 2239 | 0.0622632 | 0.0585971 |
| Q4 (.6-.8) | 2875 | -0.0692279 | -0.0688797 |
| Q5 (.8-1) | 3005 | -0.205748 | -0.20487 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.187329 | 0.20248 | 0.709685 | 0.590703 |
| tossup_correctness | tier | fall | 2798 | 0.192961 | 0.190054 | 0.73457 | 0.562489 |
| tossup_correctness | tier | nationals | 1545 | 0.175359 | 0.214991 | 0.70607 | 0.619609 |
| tossup_correctness | tier | regionals | 2039 | 0.192016 | 0.206732 | 0.703731 | 0.598925 |
| tossup_correctness | tier | winter | 2875 | 0.185665 | 0.204835 | 0.687638 | 0.596795 |
| tossup_correctness | category | Current Events | 129 | 0.121424 | 0.215732 | 0.709843 | 0.615172 |
| tossup_correctness | category | Fine Arts | 1074 | 0.209988 | 0.207879 | 0.704007 | 0.601852 |
| tossup_correctness | category | Geography | 180 | 0.133889 | 0.208573 | 0.741611 | 0.602267 |
| tossup_correctness | category | History | 1454 | 0.180218 | 0.207167 | 0.694458 | 0.601648 |
| tossup_correctness | category | Literature | 1435 | 0.186511 | 0.175412 | 0.72355 | 0.53019 |
| tossup_correctness | category | Mythology | 324 | 0.164724 | 0.184985 | 0.687613 | 0.55208 |
| tossup_correctness | category | Other Academic | 71 | 0.255753 | 0.233032 | 0.59695 | 0.666524 |
| tossup_correctness | category | Philosophy | 310 | 0.186045 | 0.198006 | 0.725378 | 0.577101 |
| tossup_correctness | category | Popular Culture | 108 | 0.217534 | 0.168744 | 0.4375 | 0.519974 |
| tossup_correctness | category | Religion | 361 | 0.226974 | 0.235917 | 0.674691 | 0.666101 |
| tossup_correctness | category | Science | 1445 | 0.183215 | 0.207415 | 0.711558 | 0.602916 |
| tossup_correctness | category | Social Science | 327 | 0.192202 | 0.214968 | 0.733626 | 0.624532 |
| tossup_correctness | category | Unknown | 2039 | 0.192016 | 0.206732 | 0.703731 | 0.598925 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.219727 | 0.231544 | 0.667397 | 0.65629 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.168824 | 0.205075 | 0.723694 | 0.596868 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.171224 | 0.196459 | 0.722542 | 0.576763 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.18553 | 0.193885 | 0.704748 | 0.570057 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.20678 | 0.212596 | 0.701958 | 0.614888 |
