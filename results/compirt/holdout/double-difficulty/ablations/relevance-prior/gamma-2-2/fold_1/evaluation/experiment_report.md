# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.708573 |
| log_loss | 0.510577 |
| ece | 0.0464963 |
| brier | 0.163692 |
| accuracy | 0.770263 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00813813 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.189299 |
| probability_p10 | 0.46735 |
| probability_p50 | 0.779042 |
| probability_p90 | 0.952115 |
| mean_predictive_variance | 0.156117 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.093305 |
| joint_tossup_event_log_loss | 6.43337 |
| buzz_position_mae | 0.13501 |
| buzz_position_median_absolute_error | 0.109463 |
| buzz_position_bias | 0.00616906 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.382272 |
| first_buzzer_mean_reciprocal_rank | 0.589764 |
| first_buzzer_log_loss | 1.61473 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.708573 |
| neg_average_precision | 0.454318 |
| neg_precision | 0.534196 |
| neg_recall | 0.267221 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.195413 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00955151 |
| no_buzz_calibration_error | -0.00635758 |
| no_buzz_brier | 0.0150834 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.00616906 | -0.0169619 |
| Q1 (0-.2) | 167 | 0.399825 | 0.415363 |
| Q2 (.2-.4) | 912 | 0.241617 | 0.235237 |
| Q3 (.4-.6) | 2115 | 0.100138 | 0.0968413 |
| Q4 (.6-.8) | 2844 | -0.0154409 | -0.0166267 |
| Q5 (.8-1) | 3055 | -0.130576 | -0.119828 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0464963 | 0.163692 | 0.708573 | 0.510577 |
| tossup_correctness | tier | fall | 2842 | 0.0451529 | 0.152011 | 0.724961 | 0.475354 |
| tossup_correctness | tier | nationals | 1564 | 0.0443493 | 0.181119 | 0.704283 | 0.560377 |
| tossup_correctness | tier | regionals | 1937 | 0.0535517 | 0.169924 | 0.688812 | 0.533439 |
| tossup_correctness | tier | winter | 2750 | 0.0503276 | 0.161462 | 0.705456 | 0.502552 |
| tossup_correctness | category | Current Events | 126 | 0.0912261 | 0.165325 | 0.710274 | 0.498773 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0353034 | 0.152758 | 0.746397 | 0.472834 |
| tossup_correctness | category | Geography | 185 | 0.0887169 | 0.164408 | 0.800249 | 0.51193 |
| tossup_correctness | category | History | 1440 | 0.0438502 | 0.164897 | 0.719674 | 0.513184 |
| tossup_correctness | category | Literature | 1422 | 0.0570049 | 0.148911 | 0.662241 | 0.475459 |
| tossup_correctness | category | Mythology | 318 | 0.0761865 | 0.160475 | 0.637153 | 0.511678 |
| tossup_correctness | category | Other Academic | 66 | 0.159748 | 0.160422 | 0.826428 | 0.475402 |
| tossup_correctness | category | Philosophy | 311 | 0.0543284 | 0.170204 | 0.729703 | 0.509356 |
| tossup_correctness | category | Popular Culture | 102 | 0.0906035 | 0.116941 | 0.496296 | 0.409363 |
| tossup_correctness | category | Religion | 358 | 0.0555153 | 0.191355 | 0.693965 | 0.584876 |
| tossup_correctness | category | Science | 1433 | 0.0436866 | 0.174503 | 0.701364 | 0.537809 |
| tossup_correctness | category | Social Science | 324 | 0.0639157 | 0.154949 | 0.766332 | 0.481595 |
| tossup_correctness | category | Unknown | 1937 | 0.0535517 | 0.169924 | 0.688812 | 0.533439 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.107443 | 0.208177 | 0.623074 | 0.628713 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0606322 | 0.178725 | 0.717226 | 0.539658 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0399305 | 0.163236 | 0.720346 | 0.512278 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0444495 | 0.158091 | 0.694029 | 0.497192 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0481703 | 0.162302 | 0.712125 | 0.50672 |
