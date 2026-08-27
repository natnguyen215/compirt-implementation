# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710264 |
| log_loss | 0.496537 |
| ece | 0.0160277 |
| brier | 0.161333 |
| accuracy | 0.774552 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0124271 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.146847 |
| probability_p10 | 0.571154 |
| probability_p50 | 0.815186 |
| probability_p90 | 0.924707 |
| mean_predictive_variance | 0.151701 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100022 |
| joint_tossup_event_log_loss | 6.56931 |
| buzz_position_mae | 0.150432 |
| buzz_position_median_absolute_error | 0.132862 |
| buzz_position_bias | -0.0467924 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.359507 |
| first_buzzer_mean_reciprocal_rank | 0.570719 |
| first_buzzer_log_loss | 1.66321 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710264 |
| neg_average_precision | 0.451168 |
| neg_precision | 0.602541 |
| neg_recall | 0.153491 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.189999 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0146661 |
| no_buzz_calibration_error | -0.00124302 |
| no_buzz_brier | 0.0150808 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0467924 | -0.0663548 |
| Q1 (0-.2) | 167 | 0.37231 | 0.386424 |
| Q2 (.2-.4) | 912 | 0.212276 | 0.212977 |
| Q3 (.4-.6) | 2115 | 0.0621622 | 0.0608783 |
| Q4 (.6-.8) | 2844 | -0.0673374 | -0.0665074 |
| Q5 (.8-1) | 3055 | -0.203346 | -0.200293 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0160277 | 0.161333 | 0.710264 | 0.496537 |
| tossup_correctness | tier | fall | 2842 | 0.0143388 | 0.148386 | 0.732812 | 0.461941 |
| tossup_correctness | tier | nationals | 1564 | 0.0438202 | 0.178104 | 0.718379 | 0.536442 |
| tossup_correctness | tier | regionals | 1937 | 0.0250017 | 0.166873 | 0.690665 | 0.511384 |
| tossup_correctness | tier | winter | 2750 | 0.0206944 | 0.161275 | 0.691538 | 0.499138 |
| tossup_correctness | category | Current Events | 126 | 0.0654061 | 0.159607 | 0.71134 | 0.491876 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0174928 | 0.152069 | 0.747415 | 0.470466 |
| tossup_correctness | category | Geography | 185 | 0.0736699 | 0.161172 | 0.803156 | 0.492451 |
| tossup_correctness | category | History | 1440 | 0.0286223 | 0.167326 | 0.705848 | 0.510422 |
| tossup_correctness | category | Literature | 1422 | 0.0186902 | 0.141258 | 0.684036 | 0.448707 |
| tossup_correctness | category | Mythology | 318 | 0.0326673 | 0.148933 | 0.685497 | 0.47149 |
| tossup_correctness | category | Other Academic | 66 | 0.118884 | 0.171641 | 0.797312 | 0.509173 |
| tossup_correctness | category | Philosophy | 311 | 0.0528047 | 0.173374 | 0.707715 | 0.520615 |
| tossup_correctness | category | Popular Culture | 102 | 0.0424023 | 0.106078 | 0.587037 | 0.370278 |
| tossup_correctness | category | Religion | 358 | 0.0646646 | 0.181111 | 0.710223 | 0.544786 |
| tossup_correctness | category | Science | 1433 | 0.034332 | 0.173933 | 0.695902 | 0.52878 |
| tossup_correctness | category | Social Science | 324 | 0.0401612 | 0.15941 | 0.767787 | 0.489045 |
| tossup_correctness | category | Unknown | 1937 | 0.0250017 | 0.166873 | 0.690665 | 0.511384 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0783061 | 0.204277 | 0.618522 | 0.600876 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0260313 | 0.17229 | 0.719868 | 0.521214 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0301269 | 0.162748 | 0.722529 | 0.498925 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0175912 | 0.155641 | 0.693019 | 0.484625 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0173463 | 0.160035 | 0.71658 | 0.492904 |
