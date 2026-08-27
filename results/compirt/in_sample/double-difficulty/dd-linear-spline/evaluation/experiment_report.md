# CompIRT Tossup Evaluation Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.888226 |
| log_loss | 0.346675 |
| ece | 0.0513153 |
| brier | 0.108463 |
| accuracy | 0.848896 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | 0.0816254 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.257549 |
| probability_p10 | 0.315539 |
| probability_p50 | 0.811175 |
| probability_p90 | 0.983334 |
| mean_predictive_variance | 0.132715 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0830843 |
| joint_tossup_event_log_loss | 5.76376 |
| buzz_position_mae | 0.12588 |
| buzz_position_median_absolute_error | 0.102763 |
| buzz_position_bias | 0.00294578 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.472826 |
| first_buzzer_mean_reciprocal_rank | 0.66389 |
| first_buzzer_log_loss | 1.37533 |
| first_buzzer_events | 47914 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.888226 |
| neg_average_precision | 0.749855 |
| neg_precision | 0.702958 |
| neg_recall | 0.607389 |
| full_pmf_events | 48612 |
| full_pmf_final_decile_mass | 0.178406 |
| no_buzz_observed_rate | 0.0143586 |
| no_buzz_predicted_rate | 0.0442454 |
| no_buzz_calibration_error | 0.0298868 |
| no_buzz_brier | 0.0154092 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 47914 | 0.00294578 | -0.0191387 |
| Q1 (0-.2) | 943 | 0.376262 | 0.37916 |
| Q2 (.2-.4) | 4869 | 0.222619 | 0.217326 |
| Q3 (.4-.6) | 11467 | 0.0911629 | 0.0827142 |
| Q4 (.6-.8) | 15035 | -0.0207153 | -0.022213 |
| Q5 (.8-1) | 15600 | -0.130225 | -0.121734 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.0513153 | 0.108463 | 0.888226 | 0.346675 |
| tossup_correctness | tier | fall | 14760 | 0.036042 | 0.107609 | 0.875811 | 0.343428 |
| tossup_correctness | tier | nationals | 7940 | 0.0765983 | 0.112814 | 0.906751 | 0.360561 |
| tossup_correctness | tier | regionals | 10202 | 0.0641751 | 0.106414 | 0.901774 | 0.341745 |
| tossup_correctness | tier | winter | 15012 | 0.0442203 | 0.108394 | 0.880912 | 0.345875 |
| tossup_correctness | category | Current Events | 640 | 0.0527056 | 0.124652 | 0.871677 | 0.38558 |
| tossup_correctness | category | Fine Arts | 5640 | 0.0532276 | 0.110996 | 0.880239 | 0.354876 |
| tossup_correctness | category | Geography | 972 | 0.0560917 | 0.117255 | 0.897615 | 0.376187 |
| tossup_correctness | category | History | 7599 | 0.0494266 | 0.107065 | 0.892992 | 0.341837 |
| tossup_correctness | category | Literature | 7469 | 0.045703 | 0.0989535 | 0.880729 | 0.32122 |
| tossup_correctness | category | Mythology | 1692 | 0.0426898 | 0.102229 | 0.874526 | 0.32994 |
| tossup_correctness | category | Other Academic | 357 | 0.0813592 | 0.111574 | 0.903193 | 0.356257 |
| tossup_correctness | category | Philosophy | 1649 | 0.0619131 | 0.106575 | 0.892543 | 0.339047 |
| tossup_correctness | category | Popular Culture | 538 | 0.0366913 | 0.0925201 | 0.837826 | 0.300271 |
| tossup_correctness | category | Religion | 1889 | 0.0498985 | 0.122149 | 0.878029 | 0.384293 |
| tossup_correctness | category | Science | 7556 | 0.043377 | 0.115846 | 0.87731 | 0.365796 |
| tossup_correctness | category | Social Science | 1711 | 0.0495483 | 0.113637 | 0.894822 | 0.360857 |
| tossup_correctness | category | Unknown | 10202 | 0.0641751 | 0.106414 | 0.901774 | 0.341745 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.10346 | 0.097609 | 0.931027 | 0.321783 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.060512 | 0.10203 | 0.915686 | 0.327944 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.0387905 | 0.110213 | 0.885365 | 0.350174 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.0400364 | 0.107348 | 0.877609 | 0.34358 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.0664655 | 0.110916 | 0.889238 | 0.354438 |
