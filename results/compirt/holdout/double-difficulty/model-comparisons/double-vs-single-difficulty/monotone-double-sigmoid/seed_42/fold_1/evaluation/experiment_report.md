# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.66975 |
| log_loss | 0.557206 |
| ece | 0.0768736 |
| brier | 0.183732 |
| accuracy | 0.736611 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0255141 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.204299 |
| probability_p10 | 0.415915 |
| probability_p50 | 0.741939 |
| probability_p90 | 0.930116 |
| mean_predictive_variance | 0.167947 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.093309 |
| joint_tossup_event_log_loss | 6.54546 |
| buzz_position_mae | 0.13942 |
| buzz_position_median_absolute_error | 0.118846 |
| buzz_position_bias | -0.0175427 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.386121 |
| first_buzzer_mean_reciprocal_rank | 0.592697 |
| first_buzzer_log_loss | 1.61317 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.66975 |
| neg_average_precision | 0.367908 |
| neg_precision | 0.420439 |
| neg_recall | 0.283403 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.108379 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.063106 |
| no_buzz_calibration_error | 0.0471969 |
| no_buzz_brier | 0.0248749 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0175427 | -0.0349796 |
| Q1 (0-.2) | 167 | 0.378977 | 0.393715 |
| Q2 (.2-.4) | 912 | 0.220114 | 0.227781 |
| Q3 (.4-.6) | 2115 | 0.0838973 | 0.0853602 |
| Q4 (.6-.8) | 2844 | -0.0348657 | -0.0324001 |
| Q5 (.8-1) | 3055 | -0.164266 | -0.158631 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0768736 | 0.183732 | 0.66975 | 0.557206 |
| tossup_correctness | tier | fall | 2842 | 0.0836555 | 0.171928 | 0.687089 | 0.527088 |
| tossup_correctness | tier | nationals | 1564 | 0.0299624 | 0.187105 | 0.680749 | 0.561266 |
| tossup_correctness | tier | regionals | 1937 | 0.0768423 | 0.186142 | 0.659382 | 0.560618 |
| tossup_correctness | tier | winter | 2750 | 0.100267 | 0.192315 | 0.656919 | 0.583618 |
| tossup_correctness | category | Current Events | 126 | 0.124547 | 0.200826 | 0.618557 | 0.579245 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0902195 | 0.187555 | 0.666914 | 0.566882 |
| tossup_correctness | category | Geography | 185 | 0.0966873 | 0.181234 | 0.767303 | 0.540735 |
| tossup_correctness | category | History | 1440 | 0.0567522 | 0.179824 | 0.686064 | 0.548459 |
| tossup_correctness | category | Literature | 1422 | 0.101927 | 0.167387 | 0.643073 | 0.520871 |
| tossup_correctness | category | Mythology | 318 | 0.100015 | 0.179758 | 0.670571 | 0.546591 |
| tossup_correctness | category | Other Academic | 66 | 0.147775 | 0.151702 | 0.839866 | 0.469058 |
| tossup_correctness | category | Philosophy | 311 | 0.0712187 | 0.191769 | 0.679725 | 0.575988 |
| tossup_correctness | category | Popular Culture | 102 | 0.263457 | 0.207494 | 0.469444 | 0.626866 |
| tossup_correctness | category | Religion | 358 | 0.066125 | 0.197424 | 0.690272 | 0.589622 |
| tossup_correctness | category | Science | 1433 | 0.0726401 | 0.189807 | 0.668139 | 0.574001 |
| tossup_correctness | category | Social Science | 324 | 0.101774 | 0.193805 | 0.674426 | 0.582314 |
| tossup_correctness | category | Unknown | 1937 | 0.0768423 | 0.186142 | 0.659382 | 0.560618 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.166647 | 0.204986 | 0.708859 | 0.604434 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.13217 | 0.195298 | 0.710682 | 0.586559 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0702131 | 0.179556 | 0.693988 | 0.547967 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0746154 | 0.17968 | 0.646155 | 0.549769 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0664176 | 0.18578 | 0.658615 | 0.559181 |
