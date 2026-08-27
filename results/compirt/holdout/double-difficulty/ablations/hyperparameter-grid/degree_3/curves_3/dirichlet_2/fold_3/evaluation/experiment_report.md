# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710121 |
| log_loss | 0.5055 |
| ece | 0.0696329 |
| brier | 0.163854 |
| accuracy | 0.767952 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00209251 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.197386 |
| probability_p10 | 0.435077 |
| probability_p50 | 0.751115 |
| probability_p90 | 0.945745 |
| mean_predictive_variance | 0.164472 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0934133 |
| joint_tossup_event_log_loss | 6.45801 |
| buzz_position_mae | 0.137879 |
| buzz_position_median_absolute_error | 0.114891 |
| buzz_position_bias | -0.00722928 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.381718 |
| first_buzzer_mean_reciprocal_rank | 0.590734 |
| first_buzzer_log_loss | 1.59953 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710121 |
| neg_average_precision | 0.45162 |
| neg_precision | 0.493248 |
| neg_recall | 0.332375 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.125858 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0571321 |
| no_buzz_calibration_error | 0.0419477 |
| no_buzz_brier | 0.0208555 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.00722928 | -0.0284783 |
| Q1 (0-.2) | 192 | 0.402165 | 0.412836 |
| Q2 (.2-.4) | 889 | 0.230339 | 0.231212 |
| Q3 (.4-.6) | 2210 | 0.0863159 | 0.0845801 |
| Q4 (.6-.8) | 2869 | -0.0332054 | -0.0311164 |
| Q5 (.8-1) | 2920 | -0.151754 | -0.144304 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0696329 | 0.163854 | 0.710121 | 0.5055 |
| tossup_correctness | tier | fall | 2817 | 0.064268 | 0.157176 | 0.704367 | 0.49548 |
| tossup_correctness | tier | nationals | 1542 | 0.0767754 | 0.179204 | 0.722989 | 0.537797 |
| tossup_correctness | tier | regionals | 1934 | 0.0695669 | 0.171874 | 0.699916 | 0.52241 |
| tossup_correctness | tier | winter | 2787 | 0.0733692 | 0.156545 | 0.705923 | 0.486022 |
| tossup_correctness | category | Current Events | 125 | 0.0969701 | 0.167934 | 0.764742 | 0.5045 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0601975 | 0.160605 | 0.719534 | 0.499408 |
| tossup_correctness | category | Geography | 185 | 0.0927516 | 0.17178 | 0.758881 | 0.518173 |
| tossup_correctness | category | History | 1443 | 0.0672217 | 0.163118 | 0.729594 | 0.498971 |
| tossup_correctness | category | Literature | 1411 | 0.0727122 | 0.153669 | 0.659195 | 0.48621 |
| tossup_correctness | category | Mythology | 320 | 0.0863025 | 0.164898 | 0.641673 | 0.53191 |
| tossup_correctness | category | Other Academic | 64 | 0.105696 | 0.187652 | 0.634115 | 0.584025 |
| tossup_correctness | category | Philosophy | 312 | 0.0779563 | 0.153108 | 0.700258 | 0.46781 |
| tossup_correctness | category | Popular Culture | 104 | 0.0923658 | 0.138225 | 0.59375 | 0.451667 |
| tossup_correctness | category | Religion | 358 | 0.076275 | 0.173247 | 0.740502 | 0.522977 |
| tossup_correctness | category | Science | 1431 | 0.0736049 | 0.164604 | 0.718852 | 0.507044 |
| tossup_correctness | category | Social Science | 321 | 0.0958365 | 0.167449 | 0.739412 | 0.516897 |
| tossup_correctness | category | Unknown | 1934 | 0.0695669 | 0.171874 | 0.699916 | 0.52241 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.133417 | 0.194522 | 0.742023 | 0.570523 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0857317 | 0.169877 | 0.754304 | 0.513341 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0798784 | 0.174207 | 0.691814 | 0.534516 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0702177 | 0.158117 | 0.694995 | 0.492168 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0562156 | 0.157804 | 0.717273 | 0.489974 |
