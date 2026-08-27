# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.626634 |
| log_loss | 0.647109 |
| ece | 0.217535 |
| brier | 0.226113 |
| accuracy | 0.645631 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.127724 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.174426 |
| probability_p10 | 0.304311 |
| probability_p50 | 0.577683 |
| probability_p90 | 0.768484 |
| mean_predictive_variance | 0.21646 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0956139 |
| joint_tossup_event_log_loss | 6.77765 |
| buzz_position_mae | 0.139718 |
| buzz_position_median_absolute_error | 0.115208 |
| buzz_position_bias | 0.00169304 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.363107 |
| first_buzzer_mean_reciprocal_rank | 0.570248 |
| first_buzzer_log_loss | 1.67632 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.626634 |
| neg_average_precision | 0.316088 |
| neg_precision | 0.31407 |
| neg_recall | 0.475964 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.141207 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0496648 |
| no_buzz_calibration_error | 0.0379378 |
| no_buzz_brier | 0.0173085 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.00169304 | -0.0186427 |
| Q1 (0-.2) | 179 | 0.394724 | 0.405245 |
| Q2 (.2-.4) | 957 | 0.24492 | 0.240086 |
| Q3 (.4-.6) | 2203 | 0.101921 | 0.0982185 |
| Q4 (.6-.8) | 2978 | -0.0237186 | -0.0214487 |
| Q5 (.8-1) | 2953 | -0.150101 | -0.138648 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.217535 | 0.226113 | 0.626634 | 0.647109 |
| tossup_correctness | tier | fall | 2876 | 0.250943 | 0.233095 | 0.63065 | 0.666237 |
| tossup_correctness | tier | nationals | 1579 | 0.158768 | 0.21701 | 0.6407 | 0.623324 |
| tossup_correctness | tier | regionals | 1990 | 0.188077 | 0.214926 | 0.635597 | 0.621572 |
| tossup_correctness | tier | winter | 2825 | 0.237121 | 0.231975 | 0.61522 | 0.65892 |
| tossup_correctness | category | Current Events | 123 | 0.27921 | 0.246326 | 0.684153 | 0.691608 |
| tossup_correctness | category | Fine Arts | 1093 | 0.194296 | 0.220544 | 0.624847 | 0.63526 |
| tossup_correctness | category | Geography | 191 | 0.217874 | 0.268268 | 0.585516 | 0.742344 |
| tossup_correctness | category | History | 1469 | 0.231986 | 0.236596 | 0.629502 | 0.669319 |
| tossup_correctness | category | Literature | 1436 | 0.214574 | 0.20389 | 0.616287 | 0.598729 |
| tossup_correctness | category | Mythology | 325 | 0.292732 | 0.245364 | 0.497925 | 0.690314 |
| tossup_correctness | category | Other Academic | 67 | 0.275668 | 0.243525 | 0.632075 | 0.682871 |
| tossup_correctness | category | Philosophy | 322 | 0.182632 | 0.185231 | 0.715243 | 0.553778 |
| tossup_correctness | category | Popular Culture | 100 | 0.40128 | 0.286991 | 0.552605 | 0.792965 |
| tossup_correctness | category | Religion | 365 | 0.188202 | 0.230605 | 0.647915 | 0.656028 |
| tossup_correctness | category | Science | 1456 | 0.247536 | 0.247002 | 0.602095 | 0.694564 |
| tossup_correctness | category | Social Science | 333 | 0.193372 | 0.231907 | 0.627801 | 0.658023 |
| tossup_correctness | category | Unknown | 1990 | 0.188077 | 0.214926 | 0.635597 | 0.621572 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.313403 | 0.283982 | 0.619071 | 0.775972 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.269617 | 0.259462 | 0.617723 | 0.721861 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.245543 | 0.238808 | 0.646967 | 0.678729 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.226287 | 0.221341 | 0.630902 | 0.636616 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.16552 | 0.20714 | 0.618978 | 0.602066 |
