# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.724417 |
| log_loss | 0.48863 |
| ece | 0.0673112 |
| brier | 0.158754 |
| accuracy | 0.780906 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00755124 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.169868 |
| probability_p10 | 0.462481 |
| probability_p50 | 0.741748 |
| probability_p90 | 0.89391 |
| mean_predictive_variance | 0.178691 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101333 |
| joint_tossup_event_log_loss | 6.6192 |
| buzz_position_mae | 0.150761 |
| buzz_position_median_absolute_error | 0.133851 |
| buzz_position_bias | -0.0434658 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.351025 |
| first_buzzer_mean_reciprocal_rank | 0.563081 |
| first_buzzer_log_loss | 1.68454 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.724417 |
| neg_average_precision | 0.455036 |
| neg_precision | 0.529412 |
| neg_recall | 0.299857 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.185757 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0135759 |
| no_buzz_calibration_error | 0.00184884 |
| no_buzz_brier | 0.011053 |
| full_pmf_max_mass_error | 1.11022e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0434658 | -0.0644816 |
| Q1 (0-.2) | 179 | 0.377575 | 0.378451 |
| Q2 (.2-.4) | 957 | 0.218154 | 0.212356 |
| Q3 (.4-.6) | 2203 | 0.0648439 | 0.0599184 |
| Q4 (.6-.8) | 2978 | -0.0716003 | -0.0726789 |
| Q5 (.8-1) | 2953 | -0.206201 | -0.201763 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0673112 | 0.158754 | 0.724417 | 0.48863 |
| tossup_correctness | tier | fall | 2876 | 0.0707416 | 0.150464 | 0.72661 | 0.46793 |
| tossup_correctness | tier | nationals | 1579 | 0.0459103 | 0.174404 | 0.717801 | 0.52626 |
| tossup_correctness | tier | regionals | 1990 | 0.0733899 | 0.161068 | 0.734534 | 0.493673 |
| tossup_correctness | tier | winter | 2825 | 0.0743254 | 0.156815 | 0.715218 | 0.485118 |
| tossup_correctness | category | Current Events | 123 | 0.103732 | 0.161828 | 0.753852 | 0.490223 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0562139 | 0.153287 | 0.73818 | 0.476805 |
| tossup_correctness | category | Geography | 191 | 0.0884035 | 0.164614 | 0.794042 | 0.503332 |
| tossup_correctness | category | History | 1469 | 0.0534113 | 0.167364 | 0.71657 | 0.507199 |
| tossup_correctness | category | Literature | 1436 | 0.0647715 | 0.141929 | 0.706972 | 0.449366 |
| tossup_correctness | category | Mythology | 325 | 0.102337 | 0.138038 | 0.685273 | 0.441038 |
| tossup_correctness | category | Other Academic | 67 | 0.128557 | 0.171166 | 0.692722 | 0.519138 |
| tossup_correctness | category | Philosophy | 322 | 0.0888403 | 0.166057 | 0.677665 | 0.503666 |
| tossup_correctness | category | Popular Culture | 100 | 0.0977018 | 0.115697 | 0.53524 | 0.391848 |
| tossup_correctness | category | Religion | 365 | 0.062866 | 0.189775 | 0.662691 | 0.562155 |
| tossup_correctness | category | Science | 1456 | 0.0790956 | 0.162121 | 0.727137 | 0.497583 |
| tossup_correctness | category | Social Science | 333 | 0.0842193 | 0.1678 | 0.743484 | 0.510784 |
| tossup_correctness | category | Unknown | 1990 | 0.0733899 | 0.161068 | 0.734534 | 0.493673 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0999835 | 0.167532 | 0.756219 | 0.508128 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0721941 | 0.170481 | 0.701562 | 0.517495 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0597276 | 0.161195 | 0.724065 | 0.493795 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0652007 | 0.153016 | 0.713314 | 0.475662 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0734964 | 0.158385 | 0.738116 | 0.487318 |
