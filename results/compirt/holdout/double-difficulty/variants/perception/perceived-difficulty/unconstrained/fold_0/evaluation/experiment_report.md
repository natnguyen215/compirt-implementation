# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.668761 |
| log_loss | 0.514791 |
| ece | 0.0301573 |
| brier | 0.16863 |
| accuracy | 0.767509 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00225928 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.132465 |
| probability_p10 | 0.551232 |
| probability_p50 | 0.763973 |
| probability_p90 | 0.888255 |
| mean_predictive_variance | 0.17581 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.171009 |
| joint_tossup_event_log_loss | 7.68831 |
| buzz_position_mae | 0.329093 |
| buzz_position_median_absolute_error | 0.331221 |
| buzz_position_bias | -0.314085 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.347283 |
| first_buzzer_mean_reciprocal_rank | 0.562402 |
| first_buzzer_log_loss | 1.69637 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.668761 |
| neg_average_precision | 0.385086 |
| neg_precision | 0.519196 |
| neg_recall | 0.130156 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0315866 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.222867 |
| no_buzz_calibration_error | 0.209597 |
| no_buzz_brier | 0.0674402 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.314085 | -0.330804 |
| Q1 (0-.2) | 197 | 0.182295 | 0.186278 |
| Q2 (.2-.4) | 985 | 0.0139343 | 0.0104308 |
| Q3 (.4-.6) | 2251 | -0.164049 | -0.163595 |
| Q4 (.6-.8) | 2866 | -0.344088 | -0.343163 |
| Q5 (.8-1) | 2996 | -0.538594 | -0.542436 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0301573 | 0.16863 | 0.668761 | 0.514791 |
| tossup_correctness | tier | fall | 2933 | 0.00944489 | 0.154399 | 0.669619 | 0.481379 |
| tossup_correctness | tier | nationals | 1584 | 0.11636 | 0.195093 | 0.682909 | 0.576175 |
| tossup_correctness | tier | regionals | 1886 | 0.0381255 | 0.179743 | 0.651772 | 0.541113 |
| tossup_correctness | tier | winter | 2892 | 0.0183689 | 0.161322 | 0.681907 | 0.497891 |
| tossup_correctness | category | Current Events | 124 | 0.0972273 | 0.182286 | 0.637183 | 0.547681 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0328162 | 0.17556 | 0.632238 | 0.534189 |
| tossup_correctness | category | Geography | 197 | 0.05753 | 0.198851 | 0.707459 | 0.579119 |
| tossup_correctness | category | History | 1491 | 0.0342713 | 0.158369 | 0.678333 | 0.489404 |
| tossup_correctness | category | Literature | 1472 | 0.0260689 | 0.147466 | 0.666953 | 0.465839 |
| tossup_correctness | category | Mythology | 332 | 0.0703713 | 0.146048 | 0.703286 | 0.458942 |
| tossup_correctness | category | Other Academic | 69 | 0.174656 | 0.221972 | 0.433258 | 0.638971 |
| tossup_correctness | category | Philosophy | 324 | 0.0551047 | 0.151787 | 0.679299 | 0.475361 |
| tossup_correctness | category | Popular Culture | 102 | 0.0924084 | 0.160223 | 0.52526 | 0.497586 |
| tossup_correctness | category | Religion | 372 | 0.0596876 | 0.195747 | 0.657934 | 0.573634 |
| tossup_correctness | category | Science | 1487 | 0.0318459 | 0.169526 | 0.687233 | 0.516936 |
| tossup_correctness | category | Social Science | 336 | 0.0204954 | 0.19517 | 0.655127 | 0.578915 |
| tossup_correctness | category | Unknown | 1886 | 0.0381255 | 0.179743 | 0.651772 | 0.541113 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.083614 | 0.189963 | 0.629045 | 0.572469 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0230875 | 0.18413 | 0.656929 | 0.550996 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0261981 | 0.166841 | 0.668022 | 0.510393 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0414886 | 0.160406 | 0.672388 | 0.494584 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0290707 | 0.171344 | 0.671849 | 0.52173 |
