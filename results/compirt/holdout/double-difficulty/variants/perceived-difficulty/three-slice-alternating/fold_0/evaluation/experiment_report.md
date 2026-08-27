# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.599927 |
| log_loss | 0.732452 |
| ece | 0.281189 |
| brier | 0.264226 |
| accuracy | 0.549758 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.215492 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.159985 |
| probability_p10 | 0.255289 |
| probability_p50 | 0.499498 |
| probability_p90 | 0.684203 |
| mean_predictive_variance | 0.224151 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0954455 |
| joint_tossup_event_log_loss | 6.86464 |
| buzz_position_mae | 0.139895 |
| buzz_position_median_absolute_error | 0.116492 |
| buzz_position_bias | -0.000969683 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.369661 |
| first_buzzer_mean_reciprocal_rank | 0.575914 |
| first_buzzer_log_loss | 1.65801 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.599927 |
| neg_average_precision | 0.304087 |
| neg_precision | 0.285132 |
| neg_recall | 0.609074 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.137678 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.049627 |
| no_buzz_calibration_error | 0.0363573 |
| no_buzz_brier | 0.0196755 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.000969683 | -0.0211973 |
| Q1 (0-.2) | 197 | 0.386189 | 0.39023 |
| Q2 (.2-.4) | 985 | 0.234978 | 0.229011 |
| Q3 (.4-.6) | 2251 | 0.0950764 | 0.0882401 |
| Q4 (.6-.8) | 2866 | -0.0282944 | -0.0274026 |
| Q5 (.8-1) | 2996 | -0.150024 | -0.143535 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.281189 | 0.264226 | 0.599927 | 0.732452 |
| tossup_correctness | tier | fall | 2933 | 0.334873 | 0.283174 | 0.606184 | 0.776235 |
| tossup_correctness | tier | nationals | 1584 | 0.192615 | 0.240842 | 0.578084 | 0.67677 |
| tossup_correctness | tier | regionals | 1886 | 0.255376 | 0.254144 | 0.628939 | 0.711371 |
| tossup_correctness | tier | winter | 2892 | 0.292304 | 0.264392 | 0.6127 | 0.732295 |
| tossup_correctness | category | Current Events | 124 | 0.306096 | 0.289306 | 0.591051 | 0.789791 |
| tossup_correctness | category | Fine Arts | 1103 | 0.272745 | 0.259388 | 0.61386 | 0.722118 |
| tossup_correctness | category | Geography | 197 | 0.247909 | 0.302356 | 0.525058 | 0.817638 |
| tossup_correctness | category | History | 1491 | 0.312711 | 0.265951 | 0.624009 | 0.733865 |
| tossup_correctness | category | Literature | 1472 | 0.286417 | 0.251095 | 0.577345 | 0.704321 |
| tossup_correctness | category | Mythology | 332 | 0.338376 | 0.278987 | 0.576464 | 0.768404 |
| tossup_correctness | category | Other Academic | 69 | 0.260051 | 0.253561 | 0.578054 | 0.701605 |
| tossup_correctness | category | Philosophy | 324 | 0.273459 | 0.250683 | 0.539412 | 0.700626 |
| tossup_correctness | category | Popular Culture | 102 | 0.462467 | 0.372855 | 0.509343 | 0.986388 |
| tossup_correctness | category | Religion | 372 | 0.235196 | 0.264196 | 0.60564 | 0.73385 |
| tossup_correctness | category | Science | 1487 | 0.285784 | 0.277167 | 0.570766 | 0.759907 |
| tossup_correctness | category | Social Science | 336 | 0.237789 | 0.265415 | 0.601992 | 0.731934 |
| tossup_correctness | category | Unknown | 1886 | 0.255376 | 0.254144 | 0.628939 | 0.711371 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.343764 | 0.305266 | 0.644695 | 0.82581 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.321593 | 0.300778 | 0.600384 | 0.817221 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.311293 | 0.281281 | 0.582424 | 0.770669 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.295391 | 0.26058 | 0.615621 | 0.724697 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.227588 | 0.240185 | 0.598099 | 0.677148 |
