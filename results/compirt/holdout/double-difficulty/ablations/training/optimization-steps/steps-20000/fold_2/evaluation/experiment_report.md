# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711248 |
| log_loss | 0.492184 |
| ece | 0.0119162 |
| brier | 0.159794 |
| accuracy | 0.774225 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0100465 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147787 |
| probability_p10 | 0.563292 |
| probability_p50 | 0.804525 |
| probability_p90 | 0.919099 |
| mean_predictive_variance | 0.156274 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0954624 |
| joint_tossup_event_log_loss | 6.45691 |
| buzz_position_mae | 0.139837 |
| buzz_position_median_absolute_error | 0.11782 |
| buzz_position_bias | -0.00254644 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.368586 |
| first_buzzer_mean_reciprocal_rank | 0.580313 |
| first_buzzer_log_loss | 1.62822 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711248 |
| neg_average_precision | 0.451877 |
| neg_precision | 0.57976 |
| neg_recall | 0.154833 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.182861 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0083959 |
| no_buzz_calibration_error | -0.00471711 |
| no_buzz_brier | 0.0124044 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.00254644 | -0.024853 |
| Q1 (0-.2) | 183 | 0.417883 | 0.430458 |
| Q2 (.2-.4) | 955 | 0.24476 | 0.239915 |
| Q3 (.4-.6) | 2239 | 0.0947855 | 0.088977 |
| Q4 (.6-.8) | 2875 | -0.0290907 | -0.0309792 |
| Q5 (.8-1) | 3005 | -0.15387 | -0.148873 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0119162 | 0.159794 | 0.711248 | 0.492184 |
| tossup_correctness | tier | fall | 2798 | 0.0198342 | 0.146622 | 0.735102 | 0.458668 |
| tossup_correctness | tier | nationals | 1545 | 0.0383459 | 0.177339 | 0.71367 | 0.53405 |
| tossup_correctness | tier | regionals | 2039 | 0.0193844 | 0.162579 | 0.698874 | 0.500177 |
| tossup_correctness | tier | winter | 2875 | 0.0156006 | 0.16121 | 0.694195 | 0.496635 |
| tossup_correctness | category | Current Events | 129 | 0.0808337 | 0.208002 | 0.682261 | 0.612258 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0283655 | 0.153245 | 0.711216 | 0.477103 |
| tossup_correctness | category | Geography | 180 | 0.0809685 | 0.189925 | 0.761588 | 0.562606 |
| tossup_correctness | category | History | 1454 | 0.0219264 | 0.167605 | 0.688351 | 0.512605 |
| tossup_correctness | category | Literature | 1435 | 0.0184585 | 0.135401 | 0.725137 | 0.433313 |
| tossup_correctness | category | Mythology | 324 | 0.0434639 | 0.149986 | 0.70248 | 0.468775 |
| tossup_correctness | category | Other Academic | 71 | 0.118843 | 0.173632 | 0.660131 | 0.533848 |
| tossup_correctness | category | Philosophy | 310 | 0.0336948 | 0.16157 | 0.713754 | 0.493984 |
| tossup_correctness | category | Popular Culture | 108 | 0.0877627 | 0.108518 | 0.517361 | 0.377187 |
| tossup_correctness | category | Religion | 361 | 0.0333211 | 0.173357 | 0.694551 | 0.525506 |
| tossup_correctness | category | Science | 1445 | 0.0315846 | 0.167564 | 0.71763 | 0.507762 |
| tossup_correctness | category | Social Science | 327 | 0.0428415 | 0.173309 | 0.746438 | 0.51809 |
| tossup_correctness | category | Unknown | 2039 | 0.0193844 | 0.162579 | 0.698874 | 0.500177 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.067226 | 0.177905 | 0.677253 | 0.53236 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0234421 | 0.172231 | 0.722429 | 0.522332 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0205099 | 0.162403 | 0.719987 | 0.497525 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0106071 | 0.152334 | 0.701864 | 0.473522 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.025409 | 0.159932 | 0.709156 | 0.494031 |
