# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.607404 |
| log_loss | 0.698998 |
| ece | 0.253628 |
| brier | 0.248963 |
| accuracy | 0.592039 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.173211 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.163819 |
| probability_p10 | 0.276685 |
| probability_p50 | 0.529378 |
| probability_p90 | 0.71466 |
| mean_predictive_variance | 0.223028 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0949567 |
| joint_tossup_event_log_loss | 6.81465 |
| buzz_position_mae | 0.139128 |
| buzz_position_median_absolute_error | 0.116817 |
| buzz_position_bias | -0.0021107 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.3773 |
| first_buzzer_mean_reciprocal_rank | 0.583775 |
| first_buzzer_log_loss | 1.64248 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.607404 |
| neg_average_precision | 0.307583 |
| neg_precision | 0.298448 |
| neg_recall | 0.546288 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.136452 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0514629 |
| no_buzz_calibration_error | 0.0381933 |
| no_buzz_brier | 0.0200786 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0021107 | -0.0236097 |
| Q1 (0-.2) | 197 | 0.387176 | 0.395264 |
| Q2 (.2-.4) | 985 | 0.231142 | 0.219154 |
| Q3 (.4-.6) | 2251 | 0.0897607 | 0.0874283 |
| Q4 (.6-.8) | 2866 | -0.0294602 | -0.0261226 |
| Q5 (.8-1) | 2996 | -0.147258 | -0.138321 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.253628 | 0.248963 | 0.607404 | 0.698998 |
| tossup_correctness | tier | fall | 2933 | 0.304139 | 0.264176 | 0.607778 | 0.734678 |
| tossup_correctness | tier | nationals | 1584 | 0.183303 | 0.236546 | 0.583746 | 0.667487 |
| tossup_correctness | tier | regionals | 1886 | 0.232092 | 0.24292 | 0.633274 | 0.685874 |
| tossup_correctness | tier | winter | 2892 | 0.256206 | 0.244275 | 0.618814 | 0.688631 |
| tossup_correctness | category | Current Events | 124 | 0.297176 | 0.2825 | 0.591398 | 0.775605 |
| tossup_correctness | category | Fine Arts | 1103 | 0.241768 | 0.245907 | 0.602508 | 0.692225 |
| tossup_correctness | category | Geography | 197 | 0.228726 | 0.28788 | 0.550583 | 0.78537 |
| tossup_correctness | category | History | 1491 | 0.291877 | 0.254924 | 0.615438 | 0.709067 |
| tossup_correctness | category | Literature | 1472 | 0.260927 | 0.237041 | 0.576659 | 0.674192 |
| tossup_correctness | category | Mythology | 332 | 0.30265 | 0.255414 | 0.58184 | 0.715339 |
| tossup_correctness | category | Other Academic | 69 | 0.249724 | 0.248714 | 0.561086 | 0.69277 |
| tossup_correctness | category | Philosophy | 324 | 0.240467 | 0.228827 | 0.583012 | 0.654397 |
| tossup_correctness | category | Popular Culture | 102 | 0.427413 | 0.34571 | 0.512803 | 0.923217 |
| tossup_correctness | category | Religion | 372 | 0.207214 | 0.25163 | 0.611216 | 0.705111 |
| tossup_correctness | category | Science | 1487 | 0.246833 | 0.252327 | 0.603963 | 0.706966 |
| tossup_correctness | category | Social Science | 336 | 0.215077 | 0.249365 | 0.62928 | 0.698031 |
| tossup_correctness | category | Unknown | 1886 | 0.232092 | 0.24292 | 0.633274 | 0.685874 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.317241 | 0.286589 | 0.646419 | 0.783633 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.284904 | 0.279837 | 0.603395 | 0.769373 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.278656 | 0.26123 | 0.594812 | 0.726753 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.269826 | 0.246721 | 0.61621 | 0.694473 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.205083 | 0.229266 | 0.612002 | 0.653772 |
