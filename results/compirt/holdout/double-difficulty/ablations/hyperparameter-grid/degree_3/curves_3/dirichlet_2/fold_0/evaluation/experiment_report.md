# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.708339 |
| log_loss | 0.513183 |
| ece | 0.0697186 |
| brier | 0.168261 |
| accuracy | 0.75503 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0102205 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.199328 |
| probability_p10 | 0.42057 |
| probability_p50 | 0.739125 |
| probability_p90 | 0.942232 |
| mean_predictive_variance | 0.167021 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0948416 |
| joint_tossup_event_log_loss | 6.49835 |
| buzz_position_mae | 0.139524 |
| buzz_position_median_absolute_error | 0.117585 |
| buzz_position_bias | -0.0010397 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.389564 |
| first_buzzer_mean_reciprocal_rank | 0.594442 |
| first_buzzer_log_loss | 1.60175 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.708339 |
| neg_average_precision | 0.434032 |
| neg_precision | 0.469015 |
| neg_recall | 0.329514 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.129046 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.059984 |
| no_buzz_calibration_error | 0.0467143 |
| no_buzz_brier | 0.0225399 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0010397 | -0.0223248 |
| Q1 (0-.2) | 197 | 0.387103 | 0.384747 |
| Q2 (.2-.4) | 985 | 0.234703 | 0.226453 |
| Q3 (.4-.6) | 2251 | 0.0938381 | 0.0917689 |
| Q4 (.6-.8) | 2866 | -0.026788 | -0.0267797 |
| Q5 (.8-1) | 2996 | -0.150721 | -0.143724 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0697186 | 0.168261 | 0.708339 | 0.513183 |
| tossup_correctness | tier | fall | 2933 | 0.0781888 | 0.158538 | 0.701735 | 0.491279 |
| tossup_correctness | tier | nationals | 1584 | 0.0735305 | 0.187801 | 0.695506 | 0.557592 |
| tossup_correctness | tier | regionals | 1886 | 0.0644722 | 0.176879 | 0.708021 | 0.533329 |
| tossup_correctness | tier | winter | 2892 | 0.062696 | 0.1618 | 0.71328 | 0.497936 |
| tossup_correctness | category | Current Events | 124 | 0.129359 | 0.186 | 0.666667 | 0.565529 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0580508 | 0.163783 | 0.717256 | 0.506573 |
| tossup_correctness | category | Geography | 197 | 0.106136 | 0.182151 | 0.773077 | 0.560032 |
| tossup_correctness | category | History | 1491 | 0.0856344 | 0.160815 | 0.719936 | 0.490257 |
| tossup_correctness | category | Literature | 1472 | 0.0609657 | 0.149625 | 0.699175 | 0.470687 |
| tossup_correctness | category | Mythology | 332 | 0.0970536 | 0.151476 | 0.685663 | 0.47671 |
| tossup_correctness | category | Other Academic | 69 | 0.114132 | 0.197439 | 0.618778 | 0.568208 |
| tossup_correctness | category | Philosophy | 324 | 0.103606 | 0.162845 | 0.682863 | 0.494274 |
| tossup_correctness | category | Popular Culture | 102 | 0.16156 | 0.164088 | 0.402768 | 0.56558 |
| tossup_correctness | category | Religion | 372 | 0.0657071 | 0.196472 | 0.678241 | 0.574253 |
| tossup_correctness | category | Science | 1487 | 0.0708127 | 0.177695 | 0.695018 | 0.532173 |
| tossup_correctness | category | Social Science | 336 | 0.0869304 | 0.178679 | 0.739025 | 0.538338 |
| tossup_correctness | category | Unknown | 1886 | 0.0644722 | 0.176879 | 0.708021 | 0.533329 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.206122 | 0.201674 | 0.712069 | 0.600131 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0883622 | 0.184747 | 0.713295 | 0.544827 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0850474 | 0.172351 | 0.696316 | 0.523787 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0755832 | 0.161357 | 0.700104 | 0.499335 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0387586 | 0.164175 | 0.725873 | 0.502342 |
