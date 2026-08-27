# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.680038 |
| log_loss | 0.533534 |
| ece | 0.0688123 |
| brier | 0.175193 |
| accuracy | 0.750991 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0190529 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.198124 |
| probability_p10 | 0.43814 |
| probability_p50 | 0.751411 |
| probability_p90 | 0.934727 |
| mean_predictive_variance | 0.165164 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0929576 |
| joint_tossup_event_log_loss | 6.48065 |
| buzz_position_mae | 0.139181 |
| buzz_position_median_absolute_error | 0.118712 |
| buzz_position_bias | -0.0206494 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.398899 |
| first_buzzer_mean_reciprocal_rank | 0.603172 |
| first_buzzer_log_loss | 1.58239 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.680038 |
| neg_average_precision | 0.372981 |
| neg_precision | 0.432789 |
| neg_recall | 0.266762 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.103439 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0577035 |
| no_buzz_calibration_error | 0.0425191 |
| no_buzz_brier | 0.0212263 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0206494 | -0.0399313 |
| Q1 (0-.2) | 192 | 0.383486 | 0.399413 |
| Q2 (.2-.4) | 889 | 0.209618 | 0.208484 |
| Q3 (.4-.6) | 2210 | 0.0723441 | 0.0691299 |
| Q4 (.6-.8) | 2869 | -0.0440086 | -0.0399355 |
| Q5 (.8-1) | 2920 | -0.164759 | -0.157106 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0688123 | 0.175193 | 0.680038 | 0.533534 |
| tossup_correctness | tier | fall | 2817 | 0.0803586 | 0.170857 | 0.680822 | 0.52884 |
| tossup_correctness | tier | nationals | 1542 | 0.0212809 | 0.17788 | 0.702173 | 0.530491 |
| tossup_correctness | tier | regionals | 1934 | 0.071861 | 0.184237 | 0.664817 | 0.558704 |
| tossup_correctness | tier | winter | 2787 | 0.0876216 | 0.171814 | 0.679945 | 0.522497 |
| tossup_correctness | category | Current Events | 125 | 0.0700885 | 0.198554 | 0.713452 | 0.585248 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0598457 | 0.17625 | 0.683931 | 0.536688 |
| tossup_correctness | category | Geography | 185 | 0.0940935 | 0.188218 | 0.736923 | 0.563895 |
| tossup_correctness | category | History | 1443 | 0.0621932 | 0.172183 | 0.700428 | 0.524365 |
| tossup_correctness | category | Literature | 1411 | 0.0697474 | 0.161929 | 0.652234 | 0.499266 |
| tossup_correctness | category | Mythology | 320 | 0.111317 | 0.176927 | 0.630697 | 0.529599 |
| tossup_correctness | category | Other Academic | 64 | 0.114947 | 0.168862 | 0.679688 | 0.505947 |
| tossup_correctness | category | Philosophy | 312 | 0.0809748 | 0.156956 | 0.665742 | 0.485315 |
| tossup_correctness | category | Popular Culture | 104 | 0.224892 | 0.211365 | 0.546165 | 0.6594 |
| tossup_correctness | category | Religion | 358 | 0.0804622 | 0.190139 | 0.685597 | 0.563109 |
| tossup_correctness | category | Science | 1431 | 0.0624489 | 0.173391 | 0.689582 | 0.530014 |
| tossup_correctness | category | Social Science | 321 | 0.0777324 | 0.169316 | 0.715073 | 0.523801 |
| tossup_correctness | category | Unknown | 1934 | 0.071861 | 0.184237 | 0.664817 | 0.558704 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.133388 | 0.206994 | 0.727741 | 0.620207 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.103314 | 0.182116 | 0.732417 | 0.545137 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0749679 | 0.178333 | 0.680965 | 0.546024 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0605696 | 0.167203 | 0.665665 | 0.514872 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.063352 | 0.176469 | 0.669155 | 0.533187 |
