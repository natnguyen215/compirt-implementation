# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.668366 |
| log_loss | 0.548896 |
| ece | 0.108668 |
| brier | 0.184208 |
| accuracy | 0.723507 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0417429 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.180251 |
| probability_p10 | 0.410243 |
| probability_p50 | 0.673513 |
| probability_p90 | 0.892919 |
| mean_predictive_variance | 0.19152 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102975 |
| joint_tossup_event_log_loss | 6.686 |
| buzz_position_mae | 0.156231 |
| buzz_position_median_absolute_error | 0.139 |
| buzz_position_bias | -0.0589852 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.32383 |
| first_buzzer_mean_reciprocal_rank | 0.540651 |
| first_buzzer_log_loss | 1.72537 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.668366 |
| neg_average_precision | 0.376638 |
| neg_precision | 0.396918 |
| neg_recall | 0.342346 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.156542 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00663169 |
| no_buzz_calibration_error | -0.00663795 |
| no_buzz_brier | 0.0124872 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0589852 | -0.0788324 |
| Q1 (0-.2) | 197 | 0.355066 | 0.349952 |
| Q2 (.2-.4) | 985 | 0.196045 | 0.185511 |
| Q3 (.4-.6) | 2251 | 0.0442904 | 0.0397837 |
| Q4 (.6-.8) | 2866 | -0.0889221 | -0.0861864 |
| Q5 (.8-1) | 2996 | -0.219015 | -0.212619 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.108668 | 0.184208 | 0.668366 | 0.548896 |
| tossup_correctness | tier | fall | 2933 | 0.104961 | 0.17094 | 0.679583 | 0.516973 |
| tossup_correctness | tier | nationals | 1584 | 0.088264 | 0.1971 | 0.647109 | 0.58028 |
| tossup_correctness | tier | regionals | 1886 | 0.12826 | 0.19678 | 0.663987 | 0.578625 |
| tossup_correctness | tier | winter | 2892 | 0.111047 | 0.182403 | 0.664675 | 0.544694 |
| tossup_correctness | category | Current Events | 124 | 0.146507 | 0.200217 | 0.674991 | 0.57694 |
| tossup_correctness | category | Fine Arts | 1103 | 0.110462 | 0.183735 | 0.666506 | 0.552944 |
| tossup_correctness | category | Geography | 197 | 0.139686 | 0.217636 | 0.677273 | 0.642152 |
| tossup_correctness | category | History | 1491 | 0.113766 | 0.171779 | 0.691835 | 0.517992 |
| tossup_correctness | category | Literature | 1472 | 0.0918972 | 0.158526 | 0.688001 | 0.485612 |
| tossup_correctness | category | Mythology | 332 | 0.130244 | 0.168035 | 0.637336 | 0.516006 |
| tossup_correctness | category | Other Academic | 69 | 0.167798 | 0.20923 | 0.581448 | 0.610659 |
| tossup_correctness | category | Philosophy | 324 | 0.133634 | 0.182326 | 0.635343 | 0.54128 |
| tossup_correctness | category | Popular Culture | 102 | 0.0880231 | 0.146984 | 0.587543 | 0.479086 |
| tossup_correctness | category | Religion | 372 | 0.0967137 | 0.207842 | 0.646359 | 0.600869 |
| tossup_correctness | category | Science | 1487 | 0.107731 | 0.197409 | 0.632025 | 0.578176 |
| tossup_correctness | category | Social Science | 336 | 0.0660438 | 0.196713 | 0.690847 | 0.579317 |
| tossup_correctness | category | Unknown | 1886 | 0.12826 | 0.19678 | 0.663987 | 0.578625 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0608153 | 0.172734 | 0.691379 | 0.53028 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0313749 | 0.174444 | 0.70895 | 0.525942 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0665096 | 0.170536 | 0.684026 | 0.518958 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.120971 | 0.175246 | 0.68615 | 0.528012 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.16735 | 0.207017 | 0.646778 | 0.600137 |
