# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.712085 |
| log_loss | 0.51967 |
| ece | 0.0776917 |
| brier | 0.169396 |
| accuracy | 0.755066 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.014978 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.229123 |
| probability_p10 | 0.352093 |
| probability_p50 | 0.771493 |
| probability_p90 | 0.945461 |
| mean_predictive_variance | 0.15483 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0990884 |
| joint_tossup_event_log_loss | 6.44595 |
| buzz_position_mae | 0.150063 |
| buzz_position_median_absolute_error | 0.130925 |
| buzz_position_bias | -0.0570578 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.39967 |
| first_buzzer_mean_reciprocal_rank | 0.604231 |
| first_buzzer_log_loss | 1.56844 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.712085 |
| neg_average_precision | 0.442246 |
| neg_precision | 0.459524 |
| neg_recall | 0.369732 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.163139 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0084357 |
| no_buzz_calibration_error | -0.00674868 |
| no_buzz_brier | 0.0131088 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0570578 | -0.0750907 |
| Q1 (0-.2) | 192 | 0.360678 | 0.374378 |
| Q2 (.2-.4) | 889 | 0.183408 | 0.180173 |
| Q3 (.4-.6) | 2210 | 0.0374676 | 0.0340008 |
| Q4 (.6-.8) | 2869 | -0.0879079 | -0.0875853 |
| Q5 (.8-1) | 2920 | -0.198966 | -0.192272 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0776917 | 0.169396 | 0.712085 | 0.51967 |
| tossup_correctness | tier | fall | 2817 | 0.0632812 | 0.158317 | 0.711109 | 0.495865 |
| tossup_correctness | tier | nationals | 1542 | 0.0798874 | 0.188617 | 0.706863 | 0.562562 |
| tossup_correctness | tier | regionals | 1934 | 0.0942806 | 0.180659 | 0.701501 | 0.547111 |
| tossup_correctness | tier | winter | 2787 | 0.0849714 | 0.162145 | 0.716414 | 0.500958 |
| tossup_correctness | category | Current Events | 125 | 0.0704956 | 0.173052 | 0.751536 | 0.518811 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0762606 | 0.162648 | 0.71401 | 0.502845 |
| tossup_correctness | category | Geography | 185 | 0.085277 | 0.179888 | 0.752448 | 0.529847 |
| tossup_correctness | category | History | 1443 | 0.0739711 | 0.166509 | 0.739304 | 0.50746 |
| tossup_correctness | category | Literature | 1411 | 0.0954814 | 0.161337 | 0.688268 | 0.500523 |
| tossup_correctness | category | Mythology | 320 | 0.105378 | 0.160719 | 0.676092 | 0.506444 |
| tossup_correctness | category | Other Academic | 64 | 0.0711105 | 0.198538 | 0.583333 | 0.59333 |
| tossup_correctness | category | Philosophy | 312 | 0.0860704 | 0.147637 | 0.730323 | 0.460976 |
| tossup_correctness | category | Popular Culture | 104 | 0.070853 | 0.131934 | 0.567472 | 0.441662 |
| tossup_correctness | category | Religion | 358 | 0.0681873 | 0.180594 | 0.720173 | 0.539528 |
| tossup_correctness | category | Science | 1431 | 0.0822735 | 0.17403 | 0.701803 | 0.536832 |
| tossup_correctness | category | Social Science | 321 | 0.0849869 | 0.167998 | 0.741912 | 0.526219 |
| tossup_correctness | category | Unknown | 1934 | 0.0942806 | 0.180659 | 0.701501 | 0.547111 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.102838 | 0.178919 | 0.770072 | 0.550815 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0521105 | 0.166872 | 0.755125 | 0.506422 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0663843 | 0.170601 | 0.702992 | 0.52739 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0685588 | 0.163113 | 0.695171 | 0.504256 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.106927 | 0.1748 | 0.716293 | 0.530958 |
