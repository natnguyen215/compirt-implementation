# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.610693 |
| log_loss | 0.645311 |
| ece | 0.194259 |
| brier | 0.22518 |
| accuracy | 0.649181 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.112944 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.174224 |
| probability_p10 | 0.319826 |
| probability_p50 | 0.591657 |
| probability_p90 | 0.77806 |
| mean_predictive_variance | 0.21504 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0934756 |
| joint_tossup_event_log_loss | 6.70594 |
| buzz_position_mae | 0.13795 |
| buzz_position_median_absolute_error | 0.114544 |
| buzz_position_bias | -0.00311037 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.370285 |
| first_buzzer_mean_reciprocal_rank | 0.579352 |
| first_buzzer_log_loss | 1.64047 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.610693 |
| neg_average_precision | 0.313848 |
| neg_precision | 0.324684 |
| neg_recall | 0.439667 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.145664 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0507069 |
| no_buzz_calibration_error | 0.0347978 |
| no_buzz_brier | 0.0206719 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.00311037 | -0.0241683 |
| Q1 (0-.2) | 167 | 0.394757 | 0.411961 |
| Q2 (.2-.4) | 912 | 0.242645 | 0.23762 |
| Q3 (.4-.6) | 2115 | 0.0962966 | 0.0934323 |
| Q4 (.6-.8) | 2844 | -0.0218112 | -0.0208353 |
| Q5 (.8-1) | 3055 | -0.149635 | -0.141343 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.194259 | 0.22518 | 0.610693 | 0.645311 |
| tossup_correctness | tier | fall | 2842 | 0.201311 | 0.211079 | 0.635726 | 0.613998 |
| tossup_correctness | tier | nationals | 1564 | 0.121844 | 0.216063 | 0.604766 | 0.622674 |
| tossup_correctness | tier | regionals | 1937 | 0.19674 | 0.228391 | 0.604153 | 0.649935 |
| tossup_correctness | tier | winter | 2750 | 0.226459 | 0.242676 | 0.600396 | 0.68729 |
| tossup_correctness | category | Current Events | 126 | 0.243033 | 0.249115 | 0.573765 | 0.695401 |
| tossup_correctness | category | Fine Arts | 1071 | 0.20578 | 0.226787 | 0.623225 | 0.650304 |
| tossup_correctness | category | Geography | 185 | 0.213537 | 0.256881 | 0.597868 | 0.711112 |
| tossup_correctness | category | History | 1440 | 0.178631 | 0.223708 | 0.598412 | 0.640476 |
| tossup_correctness | category | Literature | 1422 | 0.198881 | 0.202272 | 0.59698 | 0.597656 |
| tossup_correctness | category | Mythology | 318 | 0.192811 | 0.222305 | 0.559493 | 0.642648 |
| tossup_correctness | category | Other Academic | 66 | 0.16456 | 0.186969 | 0.792833 | 0.558147 |
| tossup_correctness | category | Philosophy | 311 | 0.153408 | 0.218275 | 0.621344 | 0.627879 |
| tossup_correctness | category | Popular Culture | 102 | 0.396632 | 0.298388 | 0.485185 | 0.819046 |
| tossup_correctness | category | Religion | 358 | 0.132362 | 0.226234 | 0.610699 | 0.647972 |
| tossup_correctness | category | Science | 1433 | 0.202286 | 0.235446 | 0.62028 | 0.668693 |
| tossup_correctness | category | Social Science | 324 | 0.185274 | 0.227956 | 0.635579 | 0.650814 |
| tossup_correctness | category | Unknown | 1937 | 0.19674 | 0.228391 | 0.604153 | 0.649935 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.260175 | 0.283323 | 0.507178 | 0.775699 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.233845 | 0.252656 | 0.621333 | 0.707463 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.210282 | 0.229632 | 0.634006 | 0.65774 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.206774 | 0.222748 | 0.605088 | 0.640505 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.157868 | 0.212981 | 0.604171 | 0.6155 |
