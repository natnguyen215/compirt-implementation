# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.595436 |
| log_loss | 0.640015 |
| ece | 0.197288 |
| brier | 0.22416 |
| accuracy | 0.643132 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.118993 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.148767 |
| probability_p10 | 0.351152 |
| probability_p50 | 0.586549 |
| probability_p90 | 0.745557 |
| mean_predictive_variance | 0.223664 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0933036 |
| joint_tossup_event_log_loss | 6.64596 |
| buzz_position_mae | 0.135419 |
| buzz_position_median_absolute_error | 0.112394 |
| buzz_position_bias | 0.000442197 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.382052 |
| first_buzzer_mean_reciprocal_rank | 0.590099 |
| first_buzzer_log_loss | 1.61611 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.595436 |
| neg_average_precision | 0.306222 |
| neg_precision | 0.310971 |
| neg_recall | 0.411466 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.140273 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.050312 |
| no_buzz_calibration_error | 0.0344029 |
| no_buzz_brier | 0.0221703 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.000442197 | -0.0225483 |
| Q1 (0-.2) | 167 | 0.385099 | 0.401101 |
| Q2 (.2-.4) | 912 | 0.234117 | 0.228999 |
| Q3 (.4-.6) | 2115 | 0.0963936 | 0.0936927 |
| Q4 (.6-.8) | 2844 | -0.0192932 | -0.0196358 |
| Q5 (.8-1) | 3055 | -0.138399 | -0.128687 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.197288 | 0.22416 | 0.595436 | 0.640015 |
| tossup_correctness | tier | fall | 2842 | 0.221629 | 0.219918 | 0.606806 | 0.630132 |
| tossup_correctness | tier | nationals | 1564 | 0.130108 | 0.217323 | 0.599469 | 0.625522 |
| tossup_correctness | tier | regionals | 1937 | 0.185354 | 0.221149 | 0.602915 | 0.63392 |
| tossup_correctness | tier | winter | 2750 | 0.219228 | 0.234553 | 0.586075 | 0.662765 |
| tossup_correctness | category | Current Events | 126 | 0.256738 | 0.249815 | 0.579097 | 0.69498 |
| tossup_correctness | category | Fine Arts | 1071 | 0.191463 | 0.218547 | 0.604546 | 0.627742 |
| tossup_correctness | category | Geography | 185 | 0.200699 | 0.254276 | 0.572398 | 0.703979 |
| tossup_correctness | category | History | 1440 | 0.189946 | 0.227527 | 0.571118 | 0.646713 |
| tossup_correctness | category | Literature | 1422 | 0.209594 | 0.204333 | 0.5835 | 0.59784 |
| tossup_correctness | category | Mythology | 318 | 0.23432 | 0.229664 | 0.571564 | 0.651935 |
| tossup_correctness | category | Other Academic | 66 | 0.184392 | 0.199913 | 0.786114 | 0.588007 |
| tossup_correctness | category | Philosophy | 311 | 0.17136 | 0.222918 | 0.600502 | 0.636248 |
| tossup_correctness | category | Popular Culture | 102 | 0.392577 | 0.282249 | 0.425926 | 0.764576 |
| tossup_correctness | category | Religion | 358 | 0.159178 | 0.23188 | 0.588768 | 0.655754 |
| tossup_correctness | category | Science | 1433 | 0.205445 | 0.234934 | 0.601774 | 0.663565 |
| tossup_correctness | category | Social Science | 324 | 0.185042 | 0.231858 | 0.589747 | 0.656212 |
| tossup_correctness | category | Unknown | 1937 | 0.185354 | 0.221149 | 0.602915 | 0.63392 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.20793 | 0.25548 | 0.547094 | 0.70867 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.207962 | 0.244633 | 0.582862 | 0.684876 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.206101 | 0.22411 | 0.632445 | 0.640935 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.212726 | 0.223851 | 0.581951 | 0.639415 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.173872 | 0.216659 | 0.587555 | 0.622792 |
