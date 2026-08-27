# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.717038 |
| log_loss | 0.501531 |
| ece | 0.0801578 |
| brier | 0.163226 |
| accuracy | 0.768069 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00528587 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.199258 |
| probability_p10 | 0.426532 |
| probability_p50 | 0.740783 |
| probability_p90 | 0.942234 |
| mean_predictive_variance | 0.167459 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0945458 |
| joint_tossup_event_log_loss | 6.50844 |
| buzz_position_mae | 0.138885 |
| buzz_position_median_absolute_error | 0.11761 |
| buzz_position_bias | -0.000859831 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.372492 |
| first_buzzer_mean_reciprocal_rank | 0.583878 |
| first_buzzer_log_loss | 1.62592 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.717038 |
| neg_average_precision | 0.444193 |
| neg_precision | 0.484122 |
| neg_recall | 0.355545 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.127998 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0581337 |
| no_buzz_calibration_error | 0.0464066 |
| no_buzz_brier | 0.0201433 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.000859831 | -0.0194507 |
| Q1 (0-.2) | 179 | 0.395334 | 0.396513 |
| Q2 (.2-.4) | 957 | 0.242128 | 0.237436 |
| Q3 (.4-.6) | 2203 | 0.0969901 | 0.0946201 |
| Q4 (.6-.8) | 2978 | -0.0248253 | -0.0193439 |
| Q5 (.8-1) | 2953 | -0.152452 | -0.1449 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0801578 | 0.163226 | 0.717038 | 0.501531 |
| tossup_correctness | tier | fall | 2876 | 0.0685134 | 0.152761 | 0.717861 | 0.472596 |
| tossup_correctness | tier | nationals | 1579 | 0.0860293 | 0.185319 | 0.706335 | 0.557015 |
| tossup_correctness | tier | regionals | 1990 | 0.0850888 | 0.16173 | 0.743183 | 0.495876 |
| tossup_correctness | tier | winter | 2825 | 0.0856221 | 0.162585 | 0.696094 | 0.503959 |
| tossup_correctness | category | Current Events | 123 | 0.123888 | 0.167341 | 0.737344 | 0.495413 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0771199 | 0.16258 | 0.710237 | 0.502806 |
| tossup_correctness | category | Geography | 191 | 0.0907897 | 0.168393 | 0.772984 | 0.516528 |
| tossup_correctness | category | History | 1469 | 0.0723201 | 0.172443 | 0.704701 | 0.524298 |
| tossup_correctness | category | Literature | 1436 | 0.0808971 | 0.149944 | 0.686531 | 0.4707 |
| tossup_correctness | category | Mythology | 325 | 0.105002 | 0.142052 | 0.686561 | 0.449101 |
| tossup_correctness | category | Other Academic | 67 | 0.160312 | 0.184864 | 0.687332 | 0.57446 |
| tossup_correctness | category | Philosophy | 322 | 0.0903288 | 0.169571 | 0.671822 | 0.51335 |
| tossup_correctness | category | Popular Culture | 100 | 0.130476 | 0.118305 | 0.595506 | 0.393767 |
| tossup_correctness | category | Religion | 365 | 0.0894177 | 0.195405 | 0.665242 | 0.58177 |
| tossup_correctness | category | Science | 1456 | 0.0797812 | 0.164251 | 0.723443 | 0.503962 |
| tossup_correctness | category | Social Science | 333 | 0.0925427 | 0.170328 | 0.753224 | 0.516157 |
| tossup_correctness | category | Unknown | 1990 | 0.0850888 | 0.16173 | 0.743183 | 0.495876 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.18456 | 0.196523 | 0.733499 | 0.566771 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.134296 | 0.184352 | 0.714057 | 0.550325 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0869429 | 0.167969 | 0.721075 | 0.511832 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0743646 | 0.154816 | 0.717846 | 0.482081 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0575248 | 0.159304 | 0.717538 | 0.493692 |
