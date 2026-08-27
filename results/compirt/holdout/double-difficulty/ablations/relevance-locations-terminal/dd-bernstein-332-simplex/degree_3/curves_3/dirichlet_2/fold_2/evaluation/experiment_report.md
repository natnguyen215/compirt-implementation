# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.713008 |
| log_loss | 0.504031 |
| ece | 0.0646817 |
| brier | 0.165019 |
| accuracy | 0.767203 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00302474 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.165324 |
| probability_p10 | 0.463698 |
| probability_p50 | 0.725994 |
| probability_p90 | 0.892641 |
| mean_predictive_variance | 0.182838 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.107795 |
| joint_tossup_event_log_loss | 6.74422 |
| buzz_position_mae | 0.176676 |
| buzz_position_median_absolute_error | 0.156523 |
| buzz_position_bias | -0.0967091 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.340931 |
| first_buzzer_mean_reciprocal_rank | 0.556069 |
| first_buzzer_log_loss | 1.68909 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.713008 |
| neg_average_precision | 0.44905 |
| neg_precision | 0.511824 |
| neg_recall | 0.2776 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.097015 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0782982 |
| no_buzz_calibration_error | 0.0651852 |
| no_buzz_brier | 0.0234838 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0967091 | -0.109251 |
| Q1 (0-.2) | 183 | 0.345063 | 0.347478 |
| Q2 (.2-.4) | 955 | 0.17458 | 0.172294 |
| Q3 (.4-.6) | 2239 | 0.0210637 | 0.0175685 |
| Q4 (.6-.8) | 2875 | -0.118384 | -0.117525 |
| Q5 (.8-1) | 3005 | -0.276843 | -0.272345 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0646817 | 0.165019 | 0.713008 | 0.504031 |
| tossup_correctness | tier | fall | 2798 | 0.0669193 | 0.152663 | 0.729591 | 0.473981 |
| tossup_correctness | tier | nationals | 1545 | 0.0688009 | 0.183165 | 0.711239 | 0.545077 |
| tossup_correctness | tier | regionals | 2039 | 0.0783875 | 0.170921 | 0.694266 | 0.51886 |
| tossup_correctness | tier | winter | 2875 | 0.057587 | 0.163106 | 0.705014 | 0.500699 |
| tossup_correctness | category | Current Events | 129 | 0.072457 | 0.196781 | 0.695782 | 0.573885 |
| tossup_correctness | category | Fine Arts | 1074 | 0.081549 | 0.162524 | 0.711875 | 0.497608 |
| tossup_correctness | category | Geography | 180 | 0.0458924 | 0.181345 | 0.765505 | 0.538788 |
| tossup_correctness | category | History | 1454 | 0.0552143 | 0.168859 | 0.704038 | 0.512506 |
| tossup_correctness | category | Literature | 1435 | 0.0663604 | 0.142821 | 0.71615 | 0.453097 |
| tossup_correctness | category | Mythology | 324 | 0.0710681 | 0.158458 | 0.663221 | 0.496819 |
| tossup_correctness | category | Other Academic | 71 | 0.129663 | 0.193271 | 0.599129 | 0.585927 |
| tossup_correctness | category | Philosophy | 310 | 0.0758232 | 0.158621 | 0.757845 | 0.484483 |
| tossup_correctness | category | Popular Culture | 108 | 0.154661 | 0.118565 | 0.543403 | 0.403729 |
| tossup_correctness | category | Religion | 361 | 0.100093 | 0.183122 | 0.696237 | 0.545293 |
| tossup_correctness | category | Science | 1445 | 0.0535903 | 0.16973 | 0.722647 | 0.513119 |
| tossup_correctness | category | Social Science | 327 | 0.0779319 | 0.176201 | 0.741351 | 0.527103 |
| tossup_correctness | category | Unknown | 2039 | 0.0783875 | 0.170921 | 0.694266 | 0.51886 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.118963 | 0.190844 | 0.67428 | 0.562071 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0556064 | 0.175867 | 0.720809 | 0.529321 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0556451 | 0.165968 | 0.722794 | 0.504913 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0711769 | 0.158108 | 0.706485 | 0.487724 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0695285 | 0.165902 | 0.708575 | 0.507403 |
