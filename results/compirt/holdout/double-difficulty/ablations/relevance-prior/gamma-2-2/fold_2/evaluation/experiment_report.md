# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.717893 |
| log_loss | 0.498194 |
| ece | 0.0376258 |
| brier | 0.161159 |
| accuracy | 0.77174 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00756185 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.186308 |
| probability_p10 | 0.477884 |
| probability_p50 | 0.777479 |
| probability_p90 | 0.950448 |
| mean_predictive_variance | 0.157522 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950543 |
| joint_tossup_event_log_loss | 6.42366 |
| buzz_position_mae | 0.137071 |
| buzz_position_median_absolute_error | 0.111402 |
| buzz_position_bias | 0.0111019 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.388463 |
| first_buzzer_mean_reciprocal_rank | 0.595251 |
| first_buzzer_log_loss | 1.58862 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.717893 |
| neg_average_precision | 0.457927 |
| neg_precision | 0.533081 |
| neg_recall | 0.25836 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.195057 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0088353 |
| no_buzz_calibration_error | -0.00427771 |
| no_buzz_brier | 0.0121257 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.0111019 | -0.0110121 |
| Q1 (0-.2) | 183 | 0.404182 | 0.409555 |
| Q2 (.2-.4) | 955 | 0.24361 | 0.241342 |
| Q3 (.4-.6) | 2239 | 0.101846 | 0.097054 |
| Q4 (.6-.8) | 2875 | -0.0146232 | -0.0167235 |
| Q5 (.8-1) | 3005 | -0.129728 | -0.11975 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0376258 | 0.161159 | 0.717893 | 0.498194 |
| tossup_correctness | tier | fall | 2798 | 0.038215 | 0.14842 | 0.738129 | 0.465458 |
| tossup_correctness | tier | nationals | 1545 | 0.033017 | 0.178704 | 0.715196 | 0.538957 |
| tossup_correctness | tier | regionals | 2039 | 0.0521092 | 0.165463 | 0.702753 | 0.513326 |
| tossup_correctness | tier | winter | 2875 | 0.0345478 | 0.161075 | 0.70664 | 0.497416 |
| tossup_correctness | category | Current Events | 129 | 0.0945062 | 0.202058 | 0.705246 | 0.584921 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0645485 | 0.164103 | 0.694005 | 0.50884 |
| tossup_correctness | category | Geography | 180 | 0.0738441 | 0.191211 | 0.756626 | 0.564812 |
| tossup_correctness | category | History | 1454 | 0.040148 | 0.161472 | 0.720178 | 0.501476 |
| tossup_correctness | category | Literature | 1435 | 0.0348546 | 0.136156 | 0.736505 | 0.438135 |
| tossup_correctness | category | Mythology | 324 | 0.053422 | 0.154332 | 0.673152 | 0.489045 |
| tossup_correctness | category | Other Academic | 71 | 0.0821984 | 0.182221 | 0.639434 | 0.550132 |
| tossup_correctness | category | Philosophy | 310 | 0.0482043 | 0.160408 | 0.742327 | 0.488885 |
| tossup_correctness | category | Popular Culture | 108 | 0.114575 | 0.117353 | 0.455729 | 0.41306 |
| tossup_correctness | category | Religion | 361 | 0.0618243 | 0.180125 | 0.690098 | 0.536793 |
| tossup_correctness | category | Science | 1445 | 0.025958 | 0.16609 | 0.728875 | 0.501373 |
| tossup_correctness | category | Social Science | 327 | 0.0666798 | 0.174947 | 0.732516 | 0.525028 |
| tossup_correctness | category | Unknown | 2039 | 0.0521092 | 0.165463 | 0.702753 | 0.513326 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.109832 | 0.183597 | 0.727785 | 0.544671 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0659085 | 0.173454 | 0.720282 | 0.530931 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0317298 | 0.163218 | 0.72775 | 0.503266 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0302009 | 0.153897 | 0.708771 | 0.475955 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0394929 | 0.161298 | 0.716701 | 0.502458 |
