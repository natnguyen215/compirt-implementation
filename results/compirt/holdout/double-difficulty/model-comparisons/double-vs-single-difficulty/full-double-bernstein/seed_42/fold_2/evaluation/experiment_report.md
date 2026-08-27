# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.71097 |
| log_loss | 0.528245 |
| ece | 0.0917026 |
| brier | 0.174005 |
| accuracy | 0.74495 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0192287 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.226328 |
| probability_p10 | 0.352417 |
| probability_p50 | 0.732806 |
| probability_p90 | 0.948948 |
| mean_predictive_variance | 0.163411 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.097749 |
| joint_tossup_event_log_loss | 6.52263 |
| buzz_position_mae | 0.138904 |
| buzz_position_median_absolute_error | 0.113805 |
| buzz_position_bias | 0.0225871 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.398185 |
| first_buzzer_mean_reciprocal_rank | 0.601583 |
| first_buzzer_log_loss | 1.58721 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.71097 |
| neg_average_precision | 0.447905 |
| neg_precision | 0.455096 |
| neg_recall | 0.413193 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.157123 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0684689 |
| no_buzz_calibration_error | 0.0553559 |
| no_buzz_brier | 0.0249388 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.0225871 | 0.00152773 |
| Q1 (0-.2) | 183 | 0.421364 | 0.438309 |
| Q2 (.2-.4) | 955 | 0.261939 | 0.267382 |
| Q3 (.4-.6) | 2239 | 0.119499 | 0.119473 |
| Q4 (.6-.8) | 2875 | -0.000959981 | 0.00295139 |
| Q5 (.8-1) | 3005 | -0.127445 | -0.121052 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0917026 | 0.174005 | 0.71097 | 0.528245 |
| tossup_correctness | tier | fall | 2798 | 0.0816035 | 0.159709 | 0.726577 | 0.493177 |
| tossup_correctness | tier | nationals | 1545 | 0.0997139 | 0.193476 | 0.7102 | 0.571904 |
| tossup_correctness | tier | regionals | 2039 | 0.11011 | 0.182872 | 0.690808 | 0.550404 |
| tossup_correctness | tier | winter | 2875 | 0.0846699 | 0.171168 | 0.704011 | 0.523195 |
| tossup_correctness | category | Current Events | 129 | 0.132204 | 0.215116 | 0.687399 | 0.622017 |
| tossup_correctness | category | Fine Arts | 1074 | 0.120366 | 0.181669 | 0.694944 | 0.549904 |
| tossup_correctness | category | Geography | 180 | 0.0851207 | 0.189917 | 0.755843 | 0.569301 |
| tossup_correctness | category | History | 1454 | 0.0849191 | 0.172296 | 0.716708 | 0.52471 |
| tossup_correctness | category | Literature | 1435 | 0.0836574 | 0.150069 | 0.709922 | 0.474448 |
| tossup_correctness | category | Mythology | 324 | 0.10283 | 0.168073 | 0.641559 | 0.523413 |
| tossup_correctness | category | Other Academic | 71 | 0.125417 | 0.195012 | 0.603486 | 0.612313 |
| tossup_correctness | category | Philosophy | 310 | 0.0880716 | 0.169452 | 0.749256 | 0.503783 |
| tossup_correctness | category | Popular Culture | 108 | 0.14148 | 0.135222 | 0.503472 | 0.444808 |
| tossup_correctness | category | Religion | 361 | 0.109749 | 0.192387 | 0.702857 | 0.566875 |
| tossup_correctness | category | Science | 1445 | 0.0679934 | 0.172983 | 0.733751 | 0.518258 |
| tossup_correctness | category | Social Science | 327 | 0.0984583 | 0.183885 | 0.733534 | 0.549895 |
| tossup_correctness | category | Unknown | 2039 | 0.11011 | 0.182872 | 0.690808 | 0.550404 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.249915 | 0.227216 | 0.764862 | 0.65182 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.155229 | 0.204911 | 0.716399 | 0.602082 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.103888 | 0.178544 | 0.727871 | 0.535851 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0850237 | 0.165116 | 0.707708 | 0.501798 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0637751 | 0.166066 | 0.702457 | 0.516888 |
