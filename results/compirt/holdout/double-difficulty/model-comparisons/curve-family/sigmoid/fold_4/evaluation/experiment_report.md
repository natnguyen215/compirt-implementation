# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.671743 |
| log_loss | 0.541486 |
| ece | 0.116437 |
| brier | 0.181282 |
| accuracy | 0.731176 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0421791 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.177491 |
| probability_p10 | 0.410121 |
| probability_p50 | 0.67159 |
| probability_p90 | 0.889731 |
| mean_predictive_variance | 0.193392 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102993 |
| joint_tossup_event_log_loss | 6.7055 |
| buzz_position_mae | 0.156255 |
| buzz_position_median_absolute_error | 0.138971 |
| buzz_position_bias | -0.0589967 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.328695 |
| first_buzzer_mean_reciprocal_rank | 0.539053 |
| first_buzzer_log_loss | 1.74724 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.671743 |
| neg_average_precision | 0.384671 |
| neg_precision | 0.39551 |
| neg_recall | 0.352213 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.15786 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.00609846 |
| no_buzz_calibration_error | -0.00562862 |
| no_buzz_brier | 0.0108443 |
| full_pmf_max_mass_error | 1.11022e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0589967 | -0.0783498 |
| Q1 (0-.2) | 179 | 0.360927 | 0.361655 |
| Q2 (.2-.4) | 957 | 0.202171 | 0.190003 |
| Q3 (.4-.6) | 2203 | 0.0494402 | 0.0452117 |
| Q4 (.6-.8) | 2978 | -0.086596 | -0.0860579 |
| Q5 (.8-1) | 2953 | -0.222153 | -0.215539 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.116437 | 0.181282 | 0.671743 | 0.541486 |
| tossup_correctness | tier | fall | 2876 | 0.106073 | 0.168882 | 0.680746 | 0.512136 |
| tossup_correctness | tier | nationals | 1579 | 0.0937325 | 0.193463 | 0.657214 | 0.571988 |
| tossup_correctness | tier | regionals | 1990 | 0.140492 | 0.186447 | 0.689766 | 0.553702 |
| tossup_correctness | tier | winter | 2825 | 0.124992 | 0.183459 | 0.656286 | 0.545712 |
| tossup_correctness | category | Current Events | 123 | 0.148927 | 0.182341 | 0.710198 | 0.533663 |
| tossup_correctness | category | Fine Arts | 1093 | 0.107151 | 0.178398 | 0.681303 | 0.534462 |
| tossup_correctness | category | Geography | 191 | 0.103084 | 0.182195 | 0.75077 | 0.542884 |
| tossup_correctness | category | History | 1469 | 0.0904797 | 0.184242 | 0.673073 | 0.546466 |
| tossup_correctness | category | Literature | 1436 | 0.119077 | 0.163923 | 0.643076 | 0.50425 |
| tossup_correctness | category | Mythology | 325 | 0.155015 | 0.168259 | 0.586232 | 0.508049 |
| tossup_correctness | category | Other Academic | 67 | 0.191397 | 0.207271 | 0.597035 | 0.601088 |
| tossup_correctness | category | Philosophy | 322 | 0.135818 | 0.173993 | 0.691356 | 0.52878 |
| tossup_correctness | category | Popular Culture | 100 | 0.129389 | 0.121701 | 0.574055 | 0.404007 |
| tossup_correctness | category | Religion | 365 | 0.135046 | 0.216615 | 0.597697 | 0.62628 |
| tossup_correctness | category | Science | 1456 | 0.126203 | 0.186975 | 0.657252 | 0.554392 |
| tossup_correctness | category | Social Science | 333 | 0.102308 | 0.189573 | 0.69209 | 0.557073 |
| tossup_correctness | category | Unknown | 1990 | 0.140492 | 0.186447 | 0.689766 | 0.553702 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0818367 | 0.161878 | 0.710945 | 0.500299 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0663369 | 0.169402 | 0.679643 | 0.521807 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0670309 | 0.167093 | 0.70486 | 0.507965 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.125843 | 0.174648 | 0.684914 | 0.52521 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.177545 | 0.203584 | 0.643009 | 0.591782 |
