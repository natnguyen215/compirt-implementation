# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.545424 |
| log_loss | 0.615055 |
| ece | 0.108624 |
| brier | 0.193064 |
| accuracy | 0.763314 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000864211 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0948454 |
| probability_p10 | 0.72865 |
| probability_p50 | 0.89229 |
| probability_p90 | 0.953417 |
| mean_predictive_variance | 0.108153 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.175161 |
| joint_tossup_event_log_loss | 7.78683 |
| buzz_position_mae | 0.340536 |
| buzz_position_median_absolute_error | 0.342597 |
| buzz_position_bias | -0.327442 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.346873 |
| first_buzzer_mean_reciprocal_rank | 0.562584 |
| first_buzzer_log_loss | 1.67097 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.545424 |
| neg_average_precision | 0.273742 |
| neg_precision | 0.394737 |
| neg_recall | 0.00687128 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0290928 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.235952 |
| no_buzz_calibration_error | 0.222839 |
| no_buzz_brier | 0.0712042 |
| full_pmf_max_mass_error | 1.11022e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.327442 | -0.342597 |
| Q1 (0-.2) | 183 | 0.181162 | 0.181787 |
| Q2 (.2-.4) | 955 | 0.00450873 | 0.000590543 |
| Q3 (.4-.6) | 2239 | -0.175649 | -0.178582 |
| Q4 (.6-.8) | 2875 | -0.353785 | -0.356447 |
| Q5 (.8-1) | 3005 | -0.551805 | -0.553695 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.108624 | 0.193064 | 0.545424 | 0.615055 |
| tossup_correctness | tier | fall | 2798 | 0.0907251 | 0.177044 | 0.545188 | 0.562967 |
| tossup_correctness | tier | nationals | 1545 | 0.120258 | 0.215796 | 0.571997 | 0.668369 |
| tossup_correctness | tier | regionals | 2039 | 0.108137 | 0.19473 | 0.534267 | 0.626385 |
| tossup_correctness | tier | winter | 2875 | 0.130091 | 0.195257 | 0.539181 | 0.629063 |
| tossup_correctness | category | Current Events | 129 | 0.184391 | 0.25068 | 0.590319 | 0.739918 |
| tossup_correctness | category | Fine Arts | 1074 | 0.111806 | 0.186708 | 0.541155 | 0.599313 |
| tossup_correctness | category | Geography | 180 | 0.251641 | 0.297346 | 0.575924 | 0.886569 |
| tossup_correctness | category | History | 1454 | 0.106231 | 0.194513 | 0.563665 | 0.609215 |
| tossup_correctness | category | Literature | 1435 | 0.0866011 | 0.162297 | 0.521574 | 0.536885 |
| tossup_correctness | category | Mythology | 324 | 0.121847 | 0.171262 | 0.584122 | 0.550126 |
| tossup_correctness | category | Other Academic | 71 | 0.202371 | 0.226241 | 0.381264 | 0.751556 |
| tossup_correctness | category | Philosophy | 310 | 0.157126 | 0.204716 | 0.485513 | 0.669519 |
| tossup_correctness | category | Popular Culture | 108 | 0.0675727 | 0.101574 | 0.569444 | 0.354708 |
| tossup_correctness | category | Religion | 361 | 0.153551 | 0.208494 | 0.538196 | 0.663633 |
| tossup_correctness | category | Science | 1445 | 0.118269 | 0.202986 | 0.551268 | 0.634085 |
| tossup_correctness | category | Social Science | 327 | 0.155577 | 0.224678 | 0.581776 | 0.697735 |
| tossup_correctness | category | Unknown | 2039 | 0.108137 | 0.19473 | 0.534267 | 0.626385 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.112919 | 0.20975 | 0.47669 | 0.653657 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.13575 | 0.21639 | 0.533884 | 0.659868 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.111153 | 0.199709 | 0.539138 | 0.6255 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0936318 | 0.176598 | 0.547751 | 0.569549 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.118639 | 0.195437 | 0.546842 | 0.634218 |
