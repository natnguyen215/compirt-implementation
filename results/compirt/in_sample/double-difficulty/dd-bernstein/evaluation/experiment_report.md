# CompIRT Tossup Evaluation Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.825902 |
| log_loss | 0.419908 |
| ece | 0.0622887 |
| brier | 0.134458 |
| accuracy | 0.809346 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | 0.0420754 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.220242 |
| probability_p10 | 0.382531 |
| probability_p50 | 0.756941 |
| probability_p90 | 0.952637 |
| mean_predictive_variance | 0.158537 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0876191 |
| joint_tossup_event_log_loss | 6.05865 |
| buzz_position_mae | 0.126927 |
| buzz_position_median_absolute_error | 0.103092 |
| buzz_position_bias | 0.0188914 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.471804 |
| first_buzzer_mean_reciprocal_rank | 0.663265 |
| first_buzzer_log_loss | 1.38257 |
| first_buzzer_events | 47914 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.825902 |
| neg_average_precision | 0.625583 |
| neg_precision | 0.613795 |
| neg_recall | 0.48758 |
| full_pmf_events | 48612 |
| full_pmf_final_decile_mass | 0.154591 |
| no_buzz_observed_rate | 0.0143586 |
| no_buzz_predicted_rate | 0.0658797 |
| no_buzz_calibration_error | 0.0515212 |
| no_buzz_brier | 0.0224003 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 47914 | 0.0188914 | -0.00345952 |
| Q1 (0-.2) | 943 | 0.391763 | 0.403962 |
| Q2 (.2-.4) | 4869 | 0.240977 | 0.240093 |
| Q3 (.4-.6) | 11467 | 0.108204 | 0.105224 |
| Q4 (.6-.8) | 15035 | -0.00233415 | -0.00187875 |
| Q5 (.8-1) | 15600 | -0.118158 | -0.112787 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.0622887 | 0.134458 | 0.825902 | 0.419908 |
| tossup_correctness | tier | fall | 14760 | 0.0576532 | 0.128163 | 0.823302 | 0.403803 |
| tossup_correctness | tier | nationals | 7940 | 0.0728814 | 0.144959 | 0.836299 | 0.444158 |
| tossup_correctness | tier | regionals | 10202 | 0.0708247 | 0.137132 | 0.829263 | 0.426253 |
| tossup_correctness | tier | winter | 15012 | 0.0555385 | 0.133275 | 0.816815 | 0.418605 |
| tossup_correctness | category | Current Events | 640 | 0.0765245 | 0.14462 | 0.830989 | 0.442125 |
| tossup_correctness | category | Fine Arts | 5640 | 0.0594728 | 0.133712 | 0.826163 | 0.418353 |
| tossup_correctness | category | Geography | 972 | 0.0603131 | 0.144294 | 0.852939 | 0.443111 |
| tossup_correctness | category | History | 7599 | 0.0612065 | 0.132254 | 0.83555 | 0.412598 |
| tossup_correctness | category | Literature | 7469 | 0.0560352 | 0.124187 | 0.807983 | 0.394422 |
| tossup_correctness | category | Mythology | 1692 | 0.0639023 | 0.130139 | 0.777658 | 0.416775 |
| tossup_correctness | category | Other Academic | 357 | 0.0846023 | 0.144394 | 0.811026 | 0.442614 |
| tossup_correctness | category | Philosophy | 1649 | 0.067513 | 0.129658 | 0.83456 | 0.400877 |
| tossup_correctness | category | Popular Culture | 538 | 0.0637893 | 0.113064 | 0.712564 | 0.374853 |
| tossup_correctness | category | Religion | 1889 | 0.0687401 | 0.152158 | 0.812189 | 0.467387 |
| tossup_correctness | category | Science | 7556 | 0.0604659 | 0.139267 | 0.822526 | 0.432384 |
| tossup_correctness | category | Social Science | 1711 | 0.0599646 | 0.138973 | 0.845832 | 0.432786 |
| tossup_correctness | category | Unknown | 10202 | 0.0708247 | 0.137132 | 0.829263 | 0.426253 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.185181 | 0.168214 | 0.848011 | 0.502809 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.124547 | 0.150274 | 0.841092 | 0.459233 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.0819065 | 0.139139 | 0.82665 | 0.433215 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.0603865 | 0.129043 | 0.823613 | 0.405964 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.0368797 | 0.129258 | 0.834533 | 0.40628 |
