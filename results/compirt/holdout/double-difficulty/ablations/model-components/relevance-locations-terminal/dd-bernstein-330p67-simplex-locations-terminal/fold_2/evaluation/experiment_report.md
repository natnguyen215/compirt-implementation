# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.715498 |
| log_loss | 0.491008 |
| ece | 0.0102672 |
| brier | 0.159735 |
| accuracy | 0.775305 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0111267 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.14095 |
| probability_p10 | 0.577205 |
| probability_p50 | 0.808242 |
| probability_p90 | 0.916716 |
| mean_predictive_variance | 0.155981 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102033 |
| joint_tossup_event_log_loss | 6.62884 |
| buzz_position_mae | 0.150045 |
| buzz_position_median_absolute_error | 0.130976 |
| buzz_position_bias | -0.0366293 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.351302 |
| first_buzzer_mean_reciprocal_rank | 0.565824 |
| first_buzzer_log_loss | 1.66659 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.715498 |
| neg_average_precision | 0.449458 |
| neg_precision | 0.601578 |
| neg_recall | 0.139716 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.199321 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0142358 |
| no_buzz_calibration_error | 0.00112282 |
| no_buzz_brier | 0.0129761 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0366293 | -0.057372 |
| Q1 (0-.2) | 183 | 0.390569 | 0.402207 |
| Q2 (.2-.4) | 955 | 0.220766 | 0.220038 |
| Q3 (.4-.6) | 2239 | 0.0685744 | 0.0634533 |
| Q4 (.6-.8) | 2875 | -0.0626304 | -0.061759 |
| Q5 (.8-1) | 3005 | -0.197956 | -0.196592 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0102672 | 0.159735 | 0.715498 | 0.491008 |
| tossup_correctness | tier | fall | 2798 | 0.0239593 | 0.146185 | 0.741946 | 0.456453 |
| tossup_correctness | tier | nationals | 1545 | 0.0476238 | 0.178268 | 0.713332 | 0.535789 |
| tossup_correctness | tier | regionals | 2039 | 0.00967863 | 0.161912 | 0.708555 | 0.496536 |
| tossup_correctness | tier | winter | 2875 | 0.0166804 | 0.161419 | 0.69329 | 0.496653 |
| tossup_correctness | category | Current Events | 129 | 0.0999235 | 0.20813 | 0.689832 | 0.605383 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0250521 | 0.152899 | 0.710557 | 0.476032 |
| tossup_correctness | category | Geography | 180 | 0.0783853 | 0.18974 | 0.753884 | 0.562172 |
| tossup_correctness | category | History | 1454 | 0.0262932 | 0.166156 | 0.697624 | 0.507697 |
| tossup_correctness | category | Literature | 1435 | 0.0274054 | 0.135198 | 0.730565 | 0.431888 |
| tossup_correctness | category | Mythology | 324 | 0.0312064 | 0.152388 | 0.684476 | 0.475725 |
| tossup_correctness | category | Other Academic | 71 | 0.0928849 | 0.177116 | 0.589325 | 0.547048 |
| tossup_correctness | category | Philosophy | 310 | 0.0293993 | 0.160658 | 0.727726 | 0.489686 |
| tossup_correctness | category | Popular Culture | 108 | 0.114282 | 0.106406 | 0.499132 | 0.373329 |
| tossup_correctness | category | Religion | 361 | 0.0240443 | 0.177507 | 0.681833 | 0.533101 |
| tossup_correctness | category | Science | 1445 | 0.0299594 | 0.167894 | 0.723388 | 0.507899 |
| tossup_correctness | category | Social Science | 327 | 0.0364147 | 0.176704 | 0.734297 | 0.528659 |
| tossup_correctness | category | Unknown | 2039 | 0.00967863 | 0.161912 | 0.708555 | 0.496536 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0500867 | 0.180857 | 0.661295 | 0.538297 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0235699 | 0.1729 | 0.722346 | 0.522045 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.02055 | 0.16093 | 0.732388 | 0.49309 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0131047 | 0.151647 | 0.711075 | 0.470792 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0181258 | 0.161112 | 0.704554 | 0.496055 |
