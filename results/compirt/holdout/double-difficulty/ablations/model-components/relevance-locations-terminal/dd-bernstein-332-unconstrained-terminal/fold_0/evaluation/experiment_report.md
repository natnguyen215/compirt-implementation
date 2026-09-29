# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.714173 |
| log_loss | 0.508628 |
| ece | 0.0684723 |
| brier | 0.165719 |
| accuracy | 0.760194 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00505648 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.202362 |
| probability_p10 | 0.416791 |
| probability_p50 | 0.750111 |
| probability_p90 | 0.945069 |
| mean_predictive_variance | 0.164328 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0946731 |
| joint_tossup_event_log_loss | 6.45348 |
| buzz_position_mae | 0.137196 |
| buzz_position_median_absolute_error | 0.111077 |
| buzz_position_bias | 0.00855097 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.382571 |
| first_buzzer_mean_reciprocal_rank | 0.589728 |
| first_buzzer_log_loss | 1.61719 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.714173 |
| neg_average_precision | 0.451851 |
| neg_precision | 0.484984 |
| neg_recall | 0.347846 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188906 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00913144 |
| no_buzz_calibration_error | -0.0041382 |
| no_buzz_brier | 0.0123741 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.00855097 | -0.013445 |
| Q1 (0-.2) | 197 | 0.388144 | 0.377441 |
| Q2 (.2-.4) | 985 | 0.240134 | 0.2323 |
| Q3 (.4-.6) | 2251 | 0.0991605 | 0.0931162 |
| Q4 (.6-.8) | 2866 | -0.0213866 | -0.0210227 |
| Q5 (.8-1) | 2996 | -0.131987 | -0.121828 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0684723 | 0.165719 | 0.714173 | 0.508628 |
| tossup_correctness | tier | fall | 2933 | 0.0757304 | 0.15616 | 0.706102 | 0.487491 |
| tossup_correctness | tier | nationals | 1584 | 0.0731964 | 0.18395 | 0.709711 | 0.549509 |
| tossup_correctness | tier | regionals | 1886 | 0.0680026 | 0.173666 | 0.716275 | 0.526702 |
| tossup_correctness | tier | winter | 2892 | 0.0645077 | 0.160246 | 0.713516 | 0.495888 |
| tossup_correctness | category | Current Events | 124 | 0.132091 | 0.189253 | 0.654873 | 0.581613 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0725354 | 0.16714 | 0.700428 | 0.516957 |
| tossup_correctness | category | Geography | 197 | 0.0851723 | 0.175583 | 0.784149 | 0.542254 |
| tossup_correctness | category | History | 1491 | 0.075686 | 0.157629 | 0.726095 | 0.482486 |
| tossup_correctness | category | Literature | 1472 | 0.0622198 | 0.143491 | 0.715595 | 0.457196 |
| tossup_correctness | category | Mythology | 332 | 0.10148 | 0.15428 | 0.654898 | 0.487954 |
| tossup_correctness | category | Other Academic | 69 | 0.134753 | 0.165011 | 0.7681 | 0.489071 |
| tossup_correctness | category | Philosophy | 324 | 0.0840454 | 0.159425 | 0.689813 | 0.481703 |
| tossup_correctness | category | Popular Culture | 102 | 0.138344 | 0.160625 | 0.432526 | 0.539381 |
| tossup_correctness | category | Religion | 372 | 0.0814839 | 0.197094 | 0.677153 | 0.577423 |
| tossup_correctness | category | Science | 1487 | 0.0730451 | 0.17579 | 0.702214 | 0.531945 |
| tossup_correctness | category | Social Science | 336 | 0.0804075 | 0.175024 | 0.74678 | 0.536237 |
| tossup_correctness | category | Unknown | 1886 | 0.0680026 | 0.173666 | 0.716275 | 0.526702 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.206325 | 0.19487 | 0.716578 | 0.586079 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0834266 | 0.182046 | 0.720121 | 0.541453 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0837399 | 0.171285 | 0.695588 | 0.522647 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0708587 | 0.160095 | 0.698473 | 0.498314 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0423467 | 0.159634 | 0.739614 | 0.492079 |
