# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.708728 |
| log_loss | 0.592947 |
| ece | 0.18373 |
| brier | 0.202743 |
| accuracy | 0.688442 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0736831 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.217762 |
| probability_p10 | 0.267166 |
| probability_p50 | 0.601984 |
| probability_p90 | 0.854204 |
| mean_predictive_variance | 0.196271 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101009 |
| joint_tossup_event_log_loss | 6.70839 |
| buzz_position_mae | 0.151454 |
| buzz_position_median_absolute_error | 0.133826 |
| buzz_position_bias | -0.0474003 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34884 |
| first_buzzer_mean_reciprocal_rank | 0.561042 |
| first_buzzer_log_loss | 1.69079 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.708728 |
| neg_average_precision | 0.443121 |
| neg_precision | 0.395833 |
| neg_recall | 0.588534 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190919 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0148608 |
| no_buzz_calibration_error | -0.00104826 |
| no_buzz_brier | 0.0153788 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0474003 | -0.0678537 |
| Q1 (0-.2) | 167 | 0.37721 | 0.378476 |
| Q2 (.2-.4) | 912 | 0.214538 | 0.215073 |
| Q3 (.4-.6) | 2115 | 0.0626446 | 0.060339 |
| Q4 (.6-.8) | 2844 | -0.068801 | -0.0702494 |
| Q5 (.8-1) | 3055 | -0.20507 | -0.202812 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.18373 | 0.202743 | 0.708728 | 0.592947 |
| tossup_correctness | tier | fall | 2842 | 0.179505 | 0.188196 | 0.725768 | 0.558674 |
| tossup_correctness | tier | nationals | 1564 | 0.173346 | 0.212343 | 0.712248 | 0.615209 |
| tossup_correctness | tier | regionals | 1937 | 0.186209 | 0.210928 | 0.685716 | 0.613146 |
| tossup_correctness | tier | winter | 2750 | 0.192256 | 0.206552 | 0.700485 | 0.601478 |
| tossup_correctness | category | Current Events | 126 | 0.238991 | 0.226898 | 0.696765 | 0.64356 |
| tossup_correctness | category | Fine Arts | 1071 | 0.190048 | 0.195962 | 0.739269 | 0.576145 |
| tossup_correctness | category | Geography | 185 | 0.241263 | 0.220538 | 0.786268 | 0.643974 |
| tossup_correctness | category | History | 1440 | 0.174043 | 0.202919 | 0.707276 | 0.592839 |
| tossup_correctness | category | Literature | 1422 | 0.185477 | 0.187227 | 0.67804 | 0.557048 |
| tossup_correctness | category | Mythology | 318 | 0.184366 | 0.191982 | 0.676756 | 0.568559 |
| tossup_correctness | category | Other Academic | 66 | 0.195218 | 0.17952 | 0.818589 | 0.548064 |
| tossup_correctness | category | Philosophy | 311 | 0.16082 | 0.197352 | 0.721519 | 0.57783 |
| tossup_correctness | category | Popular Culture | 102 | 0.224086 | 0.162966 | 0.547222 | 0.507633 |
| tossup_correctness | category | Religion | 358 | 0.192605 | 0.219603 | 0.721188 | 0.634965 |
| tossup_correctness | category | Science | 1433 | 0.175753 | 0.212569 | 0.694931 | 0.612966 |
| tossup_correctness | category | Social Science | 324 | 0.191687 | 0.194895 | 0.782773 | 0.57642 |
| tossup_correctness | category | Unknown | 1937 | 0.186209 | 0.210928 | 0.685716 | 0.613146 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.191957 | 0.238988 | 0.62605 | 0.685388 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.182481 | 0.212204 | 0.722511 | 0.613471 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.164696 | 0.197846 | 0.709779 | 0.582202 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.184728 | 0.197003 | 0.691892 | 0.578956 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.197328 | 0.206672 | 0.720315 | 0.60223 |
