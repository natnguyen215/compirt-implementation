# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710435 |
| log_loss | 0.49646 |
| ece | 0.013986 |
| brier | 0.161479 |
| accuracy | 0.772242 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0101177 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.145301 |
| probability_p10 | 0.569652 |
| probability_p50 | 0.810919 |
| probability_p90 | 0.919962 |
| mean_predictive_variance | 0.154614 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0999546 |
| joint_tossup_event_log_loss | 6.59996 |
| buzz_position_mae | 0.148585 |
| buzz_position_median_absolute_error | 0.130386 |
| buzz_position_bias | -0.0405419 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.352909 |
| first_buzzer_mean_reciprocal_rank | 0.564909 |
| first_buzzer_log_loss | 1.67898 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710435 |
| neg_average_precision | 0.447515 |
| neg_precision | 0.581272 |
| neg_recall | 0.152104 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.198646 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0152455 |
| no_buzz_calibration_error | -0.00066364 |
| no_buzz_brier | 0.0156087 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0405419 | -0.0609573 |
| Q1 (0-.2) | 167 | 0.379272 | 0.381034 |
| Q2 (.2-.4) | 912 | 0.217358 | 0.220283 |
| Q3 (.4-.6) | 2115 | 0.0681437 | 0.0666965 |
| Q4 (.6-.8) | 2844 | -0.0617738 | -0.0625809 |
| Q5 (.8-1) | 3055 | -0.195959 | -0.191439 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.013986 | 0.161479 | 0.710435 | 0.49646 |
| tossup_correctness | tier | fall | 2842 | 0.0137217 | 0.148645 | 0.731079 | 0.462597 |
| tossup_correctness | tier | nationals | 1564 | 0.0436211 | 0.179497 | 0.713688 | 0.539896 |
| tossup_correctness | tier | regionals | 1937 | 0.0211651 | 0.167441 | 0.686932 | 0.512719 |
| tossup_correctness | tier | winter | 2750 | 0.014639 | 0.160296 | 0.700976 | 0.495302 |
| tossup_correctness | category | Current Events | 126 | 0.0731287 | 0.160566 | 0.718806 | 0.492981 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0153223 | 0.151033 | 0.751547 | 0.467539 |
| tossup_correctness | category | Geography | 185 | 0.0694134 | 0.162193 | 0.794158 | 0.494123 |
| tossup_correctness | category | History | 1440 | 0.0284662 | 0.167422 | 0.708951 | 0.509975 |
| tossup_correctness | category | Literature | 1422 | 0.0147129 | 0.142307 | 0.677994 | 0.451407 |
| tossup_correctness | category | Mythology | 318 | 0.033807 | 0.151356 | 0.667301 | 0.480418 |
| tossup_correctness | category | Other Academic | 66 | 0.157098 | 0.175025 | 0.804031 | 0.518319 |
| tossup_correctness | category | Philosophy | 311 | 0.0830603 | 0.168669 | 0.72883 | 0.506821 |
| tossup_correctness | category | Popular Culture | 102 | 0.0512768 | 0.108038 | 0.526852 | 0.378349 |
| tossup_correctness | category | Religion | 358 | 0.0331277 | 0.179621 | 0.714982 | 0.540409 |
| tossup_correctness | category | Science | 1433 | 0.0355812 | 0.174101 | 0.69575 | 0.52775 |
| tossup_correctness | category | Social Science | 324 | 0.057722 | 0.159275 | 0.77836 | 0.486808 |
| tossup_correctness | category | Unknown | 1937 | 0.0211651 | 0.167441 | 0.686932 | 0.512719 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0758981 | 0.203378 | 0.619748 | 0.602154 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0254332 | 0.172286 | 0.723375 | 0.520052 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0233325 | 0.163267 | 0.716726 | 0.500558 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0152943 | 0.155509 | 0.693197 | 0.483797 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.01146 | 0.160282 | 0.718423 | 0.492592 |
