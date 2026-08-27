# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.726087 |
| log_loss | 0.474514 |
| ece | 0.0141577 |
| brier | 0.153163 |
| accuracy | 0.78932 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0159655 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.140561 |
| probability_p10 | 0.578359 |
| probability_p50 | 0.808084 |
| probability_p90 | 0.915969 |
| mean_predictive_variance | 0.15586 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100821 |
| joint_tossup_event_log_loss | 6.60942 |
| buzz_position_mae | 0.148556 |
| buzz_position_median_absolute_error | 0.130829 |
| buzz_position_bias | -0.0366861 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34822 |
| first_buzzer_mean_reciprocal_rank | 0.560576 |
| first_buzzer_log_loss | 1.68958 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.726087 |
| neg_average_precision | 0.458566 |
| neg_precision | 0.642857 |
| neg_recall | 0.158496 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.194576 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0139921 |
| no_buzz_calibration_error | 0.00226502 |
| no_buzz_brier | 0.0111463 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0366861 | -0.0581279 |
| Q1 (0-.2) | 179 | 0.380623 | 0.38037 |
| Q2 (.2-.4) | 957 | 0.223376 | 0.216451 |
| Q3 (.4-.6) | 2203 | 0.0702899 | 0.065082 |
| Q4 (.6-.8) | 2978 | -0.0651011 | -0.065124 |
| Q5 (.8-1) | 2953 | -0.197413 | -0.19249 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0141577 | 0.153163 | 0.726087 | 0.474514 |
| tossup_correctness | tier | fall | 2876 | 0.0152334 | 0.144006 | 0.729175 | 0.451514 |
| tossup_correctness | tier | nationals | 1579 | 0.0363304 | 0.172954 | 0.72069 | 0.522718 |
| tossup_correctness | tier | regionals | 1990 | 0.0271046 | 0.155696 | 0.732378 | 0.479816 |
| tossup_correctness | tier | winter | 2825 | 0.0190732 | 0.149639 | 0.718572 | 0.467252 |
| tossup_correctness | category | Current Events | 123 | 0.0503409 | 0.151918 | 0.760088 | 0.46694 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0185504 | 0.150375 | 0.73911 | 0.468601 |
| tossup_correctness | category | Geography | 191 | 0.0720128 | 0.159661 | 0.794299 | 0.490889 |
| tossup_correctness | category | History | 1469 | 0.0287406 | 0.163322 | 0.720856 | 0.497028 |
| tossup_correctness | category | Literature | 1436 | 0.0180985 | 0.135883 | 0.713407 | 0.433129 |
| tossup_correctness | category | Mythology | 325 | 0.065642 | 0.127328 | 0.688421 | 0.4128 |
| tossup_correctness | category | Other Academic | 67 | 0.0612636 | 0.158029 | 0.668464 | 0.488804 |
| tossup_correctness | category | Philosophy | 322 | 0.0377043 | 0.159325 | 0.681961 | 0.488146 |
| tossup_correctness | category | Popular Culture | 100 | 0.0638447 | 0.105497 | 0.52094 | 0.365973 |
| tossup_correctness | category | Religion | 365 | 0.0518825 | 0.185879 | 0.669217 | 0.555925 |
| tossup_correctness | category | Science | 1456 | 0.0220482 | 0.155381 | 0.726802 | 0.480679 |
| tossup_correctness | category | Social Science | 333 | 0.0376868 | 0.16065 | 0.746456 | 0.495374 |
| tossup_correctness | category | Unknown | 1990 | 0.0271046 | 0.155696 | 0.732378 | 0.479816 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0619365 | 0.158861 | 0.762521 | 0.48563 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0248916 | 0.164085 | 0.702004 | 0.502867 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0283452 | 0.156891 | 0.724822 | 0.483077 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0172404 | 0.147799 | 0.715663 | 0.46232 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0174515 | 0.151907 | 0.740116 | 0.470562 |
