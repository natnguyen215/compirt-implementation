# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.608291 |
| log_loss | 0.669546 |
| ece | 0.223451 |
| brier | 0.236088 |
| accuracy | 0.620611 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.143567 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.17309 |
| probability_p10 | 0.291619 |
| probability_p50 | 0.558145 |
| probability_p90 | 0.75281 |
| mean_predictive_variance | 0.218375 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0964814 |
| joint_tossup_event_log_loss | 6.79488 |
| buzz_position_mae | 0.1399 |
| buzz_position_median_absolute_error | 0.114613 |
| buzz_position_bias | -0.000623426 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.36729 |
| first_buzzer_mean_reciprocal_rank | 0.576756 |
| first_buzzer_log_loss | 1.6533 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.608291 |
| neg_average_precision | 0.316502 |
| neg_precision | 0.308997 |
| neg_recall | 0.492442 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.144185 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0496517 |
| no_buzz_calibration_error | 0.0365386 |
| no_buzz_brier | 0.0189605 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.000623426 | -0.0203477 |
| Q1 (0-.2) | 183 | 0.408174 | 0.414113 |
| Q2 (.2-.4) | 955 | 0.237739 | 0.232893 |
| Q3 (.4-.6) | 2239 | 0.0959298 | 0.0916837 |
| Q4 (.6-.8) | 2875 | -0.0247034 | -0.024774 |
| Q5 (.8-1) | 3005 | -0.150174 | -0.14136 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.223451 | 0.236088 | 0.608291 | 0.669546 |
| tossup_correctness | tier | fall | 2798 | 0.255041 | 0.240697 | 0.61296 | 0.681668 |
| tossup_correctness | tier | nationals | 1545 | 0.210215 | 0.247527 | 0.597045 | 0.691232 |
| tossup_correctness | tier | regionals | 2039 | 0.20019 | 0.231455 | 0.602961 | 0.66077 |
| tossup_correctness | tier | winter | 2875 | 0.21657 | 0.228743 | 0.612085 | 0.65232 |
| tossup_correctness | category | Current Events | 129 | 0.186197 | 0.25633 | 0.599784 | 0.711341 |
| tossup_correctness | category | Fine Arts | 1074 | 0.257066 | 0.250623 | 0.584782 | 0.702177 |
| tossup_correctness | category | Geography | 180 | 0.163479 | 0.266203 | 0.546808 | 0.738166 |
| tossup_correctness | category | History | 1454 | 0.219763 | 0.234802 | 0.606988 | 0.665686 |
| tossup_correctness | category | Literature | 1435 | 0.24258 | 0.219417 | 0.614751 | 0.633002 |
| tossup_correctness | category | Mythology | 324 | 0.247092 | 0.237693 | 0.592485 | 0.674661 |
| tossup_correctness | category | Other Academic | 71 | 0.248345 | 0.254955 | 0.521786 | 0.705571 |
| tossup_correctness | category | Philosophy | 310 | 0.209412 | 0.216548 | 0.658268 | 0.622034 |
| tossup_correctness | category | Popular Culture | 108 | 0.449828 | 0.327223 | 0.505208 | 0.88174 |
| tossup_correctness | category | Religion | 361 | 0.216994 | 0.231803 | 0.643877 | 0.659158 |
| tossup_correctness | category | Science | 1445 | 0.227028 | 0.244135 | 0.614489 | 0.687177 |
| tossup_correctness | category | Social Science | 327 | 0.186752 | 0.223469 | 0.65666 | 0.636004 |
| tossup_correctness | category | Unknown | 2039 | 0.20019 | 0.231455 | 0.602961 | 0.66077 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.302579 | 0.279954 | 0.642835 | 0.773575 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.248646 | 0.257328 | 0.624551 | 0.716854 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.234112 | 0.242818 | 0.629723 | 0.68644 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.240213 | 0.232463 | 0.612894 | 0.661166 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.186873 | 0.225121 | 0.578857 | 0.643606 |
