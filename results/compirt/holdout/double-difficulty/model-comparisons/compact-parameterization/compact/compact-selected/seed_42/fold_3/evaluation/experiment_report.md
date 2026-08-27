# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.707212 |
| log_loss | 0.507528 |
| ece | 0.0501569 |
| brier | 0.163239 |
| accuracy | 0.772357 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00231278 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.206924 |
| probability_p10 | 0.453378 |
| probability_p50 | 0.833444 |
| probability_p90 | 0.959289 |
| mean_predictive_variance | 0.13692 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0943354 |
| joint_tossup_event_log_loss | 6.38117 |
| buzz_position_mae | 0.141222 |
| buzz_position_median_absolute_error | 0.121031 |
| buzz_position_bias | -0.0336811 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.398678 |
| first_buzzer_mean_reciprocal_rank | 0.603896 |
| first_buzzer_log_loss | 1.56512 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.707212 |
| neg_average_precision | 0.434991 |
| neg_precision | 0.509519 |
| neg_recall | 0.269157 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.169633 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.00875126 |
| no_buzz_calibration_error | -0.00643313 |
| no_buzz_brier | 0.0129895 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0336811 | -0.0553208 |
| Q1 (0-.2) | 192 | 0.379025 | 0.388574 |
| Q2 (.2-.4) | 889 | 0.201657 | 0.198318 |
| Q3 (.4-.6) | 2210 | 0.0571988 | 0.050788 |
| Q4 (.6-.8) | 2869 | -0.0641656 | -0.064635 |
| Q5 (.8-1) | 2920 | -0.171297 | -0.162525 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0501569 | 0.163239 | 0.707212 | 0.507528 |
| tossup_correctness | tier | fall | 2817 | 0.0397907 | 0.155617 | 0.708256 | 0.489924 |
| tossup_correctness | tier | nationals | 1542 | 0.0718623 | 0.18279 | 0.708887 | 0.552119 |
| tossup_correctness | tier | regionals | 1934 | 0.0609093 | 0.169107 | 0.699611 | 0.525362 |
| tossup_correctness | tier | winter | 2787 | 0.0553929 | 0.156054 | 0.707897 | 0.488273 |
| tossup_correctness | category | Current Events | 125 | 0.0624305 | 0.180591 | 0.7457 | 0.533016 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0365656 | 0.155466 | 0.722677 | 0.485197 |
| tossup_correctness | category | Geography | 185 | 0.0910864 | 0.175701 | 0.748531 | 0.526022 |
| tossup_correctness | category | History | 1443 | 0.0531523 | 0.163522 | 0.726139 | 0.49917 |
| tossup_correctness | category | Literature | 1411 | 0.0656396 | 0.152059 | 0.691116 | 0.48103 |
| tossup_correctness | category | Mythology | 320 | 0.051943 | 0.15543 | 0.674541 | 0.497954 |
| tossup_correctness | category | Other Academic | 64 | 0.120165 | 0.203758 | 0.613281 | 0.617259 |
| tossup_correctness | category | Philosophy | 312 | 0.0510874 | 0.141085 | 0.718258 | 0.446451 |
| tossup_correctness | category | Popular Culture | 104 | 0.0424175 | 0.127796 | 0.585938 | 0.436361 |
| tossup_correctness | category | Religion | 358 | 0.056339 | 0.180497 | 0.707535 | 0.537795 |
| tossup_correctness | category | Science | 1431 | 0.0759518 | 0.171343 | 0.685888 | 0.533988 |
| tossup_correctness | category | Social Science | 321 | 0.0657442 | 0.165125 | 0.73135 | 0.526481 |
| tossup_correctness | category | Unknown | 1934 | 0.0609093 | 0.169107 | 0.699611 | 0.525362 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0721671 | 0.181331 | 0.761837 | 0.542075 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0501721 | 0.162825 | 0.755934 | 0.501864 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0661542 | 0.16838 | 0.700572 | 0.528082 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0491903 | 0.156182 | 0.693542 | 0.489707 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0697476 | 0.165218 | 0.713463 | 0.508933 |
