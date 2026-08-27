# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.626346 |
| log_loss | 0.658207 |
| ece | 0.218973 |
| brier | 0.230699 |
| accuracy | 0.632383 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.132867 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.175539 |
| probability_p10 | 0.298277 |
| probability_p50 | 0.567258 |
| probability_p90 | 0.762426 |
| mean_predictive_variance | 0.217044 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0955285 |
| joint_tossup_event_log_loss | 6.77488 |
| buzz_position_mae | 0.139664 |
| buzz_position_median_absolute_error | 0.115638 |
| buzz_position_bias | 0.000369254 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.367509 |
| first_buzzer_mean_reciprocal_rank | 0.576757 |
| first_buzzer_log_loss | 1.65727 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.626346 |
| neg_average_precision | 0.324931 |
| neg_precision | 0.318756 |
| neg_recall | 0.497709 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.141272 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0509311 |
| no_buzz_calibration_error | 0.0376614 |
| no_buzz_brier | 0.0195103 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.000369254 | -0.0187602 |
| Q1 (0-.2) | 197 | 0.388502 | 0.396733 |
| Q2 (.2-.4) | 985 | 0.237845 | 0.225739 |
| Q3 (.4-.6) | 2251 | 0.095308 | 0.0895848 |
| Q4 (.6-.8) | 2866 | -0.0272598 | -0.0241651 |
| Q5 (.8-1) | 2996 | -0.148128 | -0.138294 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.218973 | 0.230699 | 0.626346 | 0.658207 |
| tossup_correctness | tier | fall | 2933 | 0.253991 | 0.236157 | 0.620791 | 0.672269 |
| tossup_correctness | tier | nationals | 1584 | 0.211501 | 0.247964 | 0.594576 | 0.693016 |
| tossup_correctness | tier | regionals | 1886 | 0.173057 | 0.217878 | 0.646163 | 0.631129 |
| tossup_correctness | tier | winter | 2892 | 0.217747 | 0.224069 | 0.63776 | 0.642538 |
| tossup_correctness | category | Current Events | 124 | 0.290509 | 0.2767 | 0.599376 | 0.761663 |
| tossup_correctness | category | Fine Arts | 1103 | 0.2027 | 0.228622 | 0.620381 | 0.654026 |
| tossup_correctness | category | Geography | 197 | 0.237653 | 0.27897 | 0.570396 | 0.763921 |
| tossup_correctness | category | History | 1491 | 0.277685 | 0.242384 | 0.644014 | 0.681035 |
| tossup_correctness | category | Literature | 1472 | 0.212742 | 0.210707 | 0.610224 | 0.614187 |
| tossup_correctness | category | Mythology | 332 | 0.275213 | 0.24127 | 0.597611 | 0.682617 |
| tossup_correctness | category | Other Academic | 69 | 0.281241 | 0.264629 | 0.514706 | 0.725476 |
| tossup_correctness | category | Philosophy | 324 | 0.205424 | 0.215404 | 0.58117 | 0.621699 |
| tossup_correctness | category | Popular Culture | 102 | 0.38537 | 0.324496 | 0.494118 | 0.877343 |
| tossup_correctness | category | Religion | 372 | 0.187343 | 0.241487 | 0.627841 | 0.682418 |
| tossup_correctness | category | Science | 1487 | 0.221625 | 0.234075 | 0.642436 | 0.666744 |
| tossup_correctness | category | Social Science | 336 | 0.195102 | 0.241915 | 0.634576 | 0.681464 |
| tossup_correctness | category | Unknown | 1886 | 0.173057 | 0.217878 | 0.646163 | 0.631129 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.294563 | 0.2752 | 0.647082 | 0.75986 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.254432 | 0.262394 | 0.616318 | 0.730717 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.23765 | 0.239407 | 0.612174 | 0.679168 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.230037 | 0.225563 | 0.633303 | 0.646032 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.177729 | 0.215723 | 0.633648 | 0.623581 |
