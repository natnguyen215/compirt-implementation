# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.717208 |
| log_loss | 0.488918 |
| ece | 0.0109146 |
| brier | 0.158905 |
| accuracy | 0.776547 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0112964 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.140958 |
| probability_p10 | 0.575977 |
| probability_p50 | 0.8129 |
| probability_p90 | 0.916634 |
| mean_predictive_variance | 0.154817 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101528 |
| joint_tossup_event_log_loss | 6.6213 |
| buzz_position_mae | 0.150281 |
| buzz_position_median_absolute_error | 0.133162 |
| buzz_position_bias | -0.0359489 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.352663 |
| first_buzzer_mean_reciprocal_rank | 0.566423 |
| first_buzzer_log_loss | 1.6687 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.717208 |
| neg_average_precision | 0.450046 |
| neg_precision | 0.59962 |
| neg_recall | 0.144821 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.196489 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0164849 |
| no_buzz_calibration_error | 0.00321531 |
| no_buzz_brier | 0.0132672 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0359489 | -0.0589446 |
| Q1 (0-.2) | 197 | 0.37334 | 0.374346 |
| Q2 (.2-.4) | 985 | 0.218828 | 0.212177 |
| Q3 (.4-.6) | 2251 | 0.0684499 | 0.0667952 |
| Q4 (.6-.8) | 2866 | -0.065466 | -0.0664481 |
| Q5 (.8-1) | 2996 | -0.196827 | -0.192884 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0109146 | 0.158905 | 0.717208 | 0.488918 |
| tossup_correctness | tier | fall | 2933 | 0.0126913 | 0.147746 | 0.71388 | 0.461859 |
| tossup_correctness | tier | nationals | 1584 | 0.039675 | 0.175557 | 0.711617 | 0.531064 |
| tossup_correctness | tier | regionals | 1886 | 0.0247751 | 0.170183 | 0.712447 | 0.514484 |
| tossup_correctness | tier | winter | 2892 | 0.0174708 | 0.153748 | 0.72294 | 0.476603 |
| tossup_correctness | category | Current Events | 124 | 0.09827 | 0.170041 | 0.674644 | 0.525515 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0178864 | 0.16113 | 0.711262 | 0.496211 |
| tossup_correctness | category | Geography | 197 | 0.0648072 | 0.171452 | 0.784848 | 0.519258 |
| tossup_correctness | category | History | 1491 | 0.0201263 | 0.147898 | 0.728798 | 0.460617 |
| tossup_correctness | category | Literature | 1472 | 0.0276365 | 0.137425 | 0.731193 | 0.436812 |
| tossup_correctness | category | Mythology | 332 | 0.0135909 | 0.141316 | 0.688172 | 0.448829 |
| tossup_correctness | category | Other Academic | 69 | 0.0745669 | 0.166762 | 0.692308 | 0.50667 |
| tossup_correctness | category | Philosophy | 324 | 0.0251475 | 0.147841 | 0.695099 | 0.462788 |
| tossup_correctness | category | Popular Culture | 102 | 0.0565108 | 0.148099 | 0.431142 | 0.483729 |
| tossup_correctness | category | Religion | 372 | 0.0464437 | 0.182544 | 0.720504 | 0.54064 |
| tossup_correctness | category | Science | 1487 | 0.0260806 | 0.168986 | 0.690162 | 0.514327 |
| tossup_correctness | category | Social Science | 336 | 0.0479165 | 0.178718 | 0.730127 | 0.537053 |
| tossup_correctness | category | Unknown | 1886 | 0.0247751 | 0.170183 | 0.712447 | 0.514484 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.076157 | 0.16794 | 0.68992 | 0.52451 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.026941 | 0.172247 | 0.717422 | 0.519235 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0169879 | 0.160624 | 0.703333 | 0.493777 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0116889 | 0.152466 | 0.704534 | 0.474535 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0221145 | 0.158794 | 0.737728 | 0.486718 |
