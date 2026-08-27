# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.700198 |
| log_loss | 0.546453 |
| ece | 0.0860523 |
| brier | 0.178885 |
| accuracy | 0.74112 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0210052 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.236817 |
| probability_p10 | 0.320694 |
| probability_p50 | 0.760713 |
| probability_p90 | 0.940953 |
| mean_predictive_variance | 0.156356 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0984608 |
| joint_tossup_event_log_loss | 6.49815 |
| buzz_position_mae | 0.148944 |
| buzz_position_median_absolute_error | 0.130621 |
| buzz_position_bias | -0.052552 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.386231 |
| first_buzzer_mean_reciprocal_rank | 0.594679 |
| first_buzzer_log_loss | 1.59086 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.700198 |
| neg_average_precision | 0.425434 |
| neg_precision | 0.448406 |
| neg_recall | 0.383726 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.172708 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00908107 |
| no_buzz_calibration_error | -0.00682802 |
| no_buzz_brier | 0.0150661 |
| full_pmf_max_mass_error | 1.11022e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.052552 | -0.0707345 |
| Q1 (0-.2) | 167 | 0.355672 | 0.365571 |
| Q2 (.2-.4) | 912 | 0.192437 | 0.181076 |
| Q3 (.4-.6) | 2115 | 0.0484234 | 0.0455849 |
| Q4 (.6-.8) | 2844 | -0.0746815 | -0.0768069 |
| Q5 (.8-1) | 3055 | -0.197308 | -0.192586 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0860523 | 0.178885 | 0.700198 | 0.546453 |
| tossup_correctness | tier | fall | 2842 | 0.0719129 | 0.163268 | 0.711415 | 0.503591 |
| tossup_correctness | tier | nationals | 1564 | 0.0823959 | 0.195559 | 0.692888 | 0.584073 |
| tossup_correctness | tier | regionals | 1937 | 0.0970397 | 0.182959 | 0.691332 | 0.561237 |
| tossup_correctness | tier | winter | 2750 | 0.10263 | 0.182672 | 0.694496 | 0.558939 |
| tossup_correctness | category | Current Events | 126 | 0.130723 | 0.179904 | 0.72236 | 0.538969 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0764647 | 0.16594 | 0.730465 | 0.507527 |
| tossup_correctness | category | Geography | 185 | 0.11826 | 0.17434 | 0.791528 | 0.527374 |
| tossup_correctness | category | History | 1440 | 0.08933 | 0.183688 | 0.694457 | 0.557421 |
| tossup_correctness | category | Literature | 1422 | 0.108109 | 0.171843 | 0.668443 | 0.53881 |
| tossup_correctness | category | Mythology | 318 | 0.0708974 | 0.164184 | 0.659511 | 0.508054 |
| tossup_correctness | category | Other Academic | 66 | 0.0743127 | 0.165324 | 0.774916 | 0.499504 |
| tossup_correctness | category | Philosophy | 311 | 0.0598804 | 0.167435 | 0.765277 | 0.503377 |
| tossup_correctness | category | Popular Culture | 102 | 0.0862139 | 0.119551 | 0.498148 | 0.405448 |
| tossup_correctness | category | Religion | 358 | 0.0983125 | 0.199499 | 0.683876 | 0.595898 |
| tossup_correctness | category | Science | 1433 | 0.0928694 | 0.192336 | 0.685462 | 0.578219 |
| tossup_correctness | category | Social Science | 324 | 0.0786407 | 0.173669 | 0.727339 | 0.523195 |
| tossup_correctness | category | Unknown | 1937 | 0.0970397 | 0.182959 | 0.691332 | 0.561237 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0971053 | 0.201987 | 0.685224 | 0.600624 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0947429 | 0.188782 | 0.709202 | 0.575699 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0665698 | 0.176913 | 0.704208 | 0.539459 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0897962 | 0.174235 | 0.683405 | 0.537016 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0961012 | 0.180362 | 0.708729 | 0.548387 |
