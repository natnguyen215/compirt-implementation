# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.659164 |
| log_loss | 0.831877 |
| ece | 0.219558 |
| brier | 0.256408 |
| accuracy | 0.633014 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.12911 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.315051 |
| probability_p10 | 0.0932439 |
| probability_p50 | 0.603057 |
| probability_p90 | 0.963715 |
| mean_predictive_variance | 0.146336 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.119773 |
| joint_tossup_event_log_loss | 8.16249 |
| buzz_position_mae | 0.149582 |
| buzz_position_median_absolute_error | 0.119077 |
| buzz_position_bias | 0.0408919 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.308919 |
| first_buzzer_mean_reciprocal_rank | 0.517984 |
| first_buzzer_log_loss | 2.46874 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.659164 |
| neg_average_precision | 0.340166 |
| neg_precision | 0.341779 |
| neg_recall | 0.586223 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.163358 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.20108 |
| no_buzz_calibration_error | 0.185171 |
| no_buzz_brier | 0.112159 |
| full_pmf_max_mass_error | 1.00061e-11 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.0408919 | 0.0219695 |
| Q1 (0-.2) | 167 | 0.449075 | 0.454896 |
| Q2 (.2-.4) | 912 | 0.292626 | 0.291058 |
| Q3 (.4-.6) | 2115 | 0.14818 | 0.143876 |
| Q4 (.6-.8) | 2844 | 0.0251048 | 0.0230636 |
| Q5 (.8-1) | 3055 | -0.11615 | -0.106626 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.219558 | 0.256408 | 0.659164 | 0.831877 |
| tossup_correctness | tier | fall | 2842 | 0.142837 | 0.194099 | 0.707398 | 0.647896 |
| tossup_correctness | tier | nationals | 1564 | 0.344732 | 0.340383 | 0.681397 | 1.07641 |
| tossup_correctness | tier | regionals | 1937 | 0.290244 | 0.299966 | 0.6191 | 0.964689 |
| tossup_correctness | tier | winter | 2750 | 0.183509 | 0.242363 | 0.640208 | 0.78939 |
| tossup_correctness | category | Current Events | 126 | 0.270912 | 0.26164 | 0.696054 | 0.8607 |
| tossup_correctness | category | Fine Arts | 1071 | 0.204484 | 0.232201 | 0.708721 | 0.727814 |
| tossup_correctness | category | Geography | 185 | 0.216496 | 0.242949 | 0.744601 | 0.884117 |
| tossup_correctness | category | History | 1440 | 0.195043 | 0.241312 | 0.67478 | 0.800484 |
| tossup_correctness | category | Literature | 1422 | 0.206495 | 0.237143 | 0.632278 | 0.778395 |
| tossup_correctness | category | Mythology | 318 | 0.215066 | 0.243793 | 0.586668 | 0.781604 |
| tossup_correctness | category | Other Academic | 66 | 0.252238 | 0.261382 | 0.725644 | 0.799973 |
| tossup_correctness | category | Philosophy | 311 | 0.171659 | 0.241721 | 0.682617 | 0.825824 |
| tossup_correctness | category | Popular Culture | 102 | 0.189537 | 0.175303 | 0.527778 | 0.584116 |
| tossup_correctness | category | Religion | 358 | 0.198476 | 0.263162 | 0.646754 | 0.84752 |
| tossup_correctness | category | Science | 1433 | 0.214966 | 0.261809 | 0.657845 | 0.845137 |
| tossup_correctness | category | Social Science | 324 | 0.21528 | 0.252966 | 0.694263 | 0.778785 |
| tossup_correctness | category | Unknown | 1937 | 0.290244 | 0.299966 | 0.6191 | 0.964689 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.417639 | 0.38969 | 0.584384 | 1.39676 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.284223 | 0.312219 | 0.645898 | 1.07348 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.234227 | 0.270255 | 0.646938 | 0.909538 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.217616 | 0.251368 | 0.653107 | 0.791991 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.183752 | 0.227568 | 0.679758 | 0.712237 |
