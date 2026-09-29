# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.587771 |
| log_loss | 0.736191 |
| ece | 0.277484 |
| brier | 0.265983 |
| accuracy | 0.552073 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.210052 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.159887 |
| probability_p10 | 0.254427 |
| probability_p50 | 0.503028 |
| probability_p90 | 0.680026 |
| mean_predictive_variance | 0.2242 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0943879 |
| joint_tossup_event_log_loss | 6.88402 |
| buzz_position_mae | 0.138799 |
| buzz_position_median_absolute_error | 0.116143 |
| buzz_position_bias | -0.0055423 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34774 |
| first_buzzer_mean_reciprocal_rank | 0.559448 |
| first_buzzer_log_loss | 1.69195 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.587771 |
| neg_average_precision | 0.299161 |
| neg_precision | 0.286258 |
| neg_recall | 0.591308 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.141334 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0497538 |
| no_buzz_calibration_error | 0.0338447 |
| no_buzz_brier | 0.0214899 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0055423 | -0.0285576 |
| Q1 (0-.2) | 167 | 0.389996 | 0.40787 |
| Q2 (.2-.4) | 912 | 0.237529 | 0.23644 |
| Q3 (.4-.6) | 2115 | 0.0938401 | 0.092843 |
| Q4 (.6-.8) | 2844 | -0.0238395 | -0.0244215 |
| Q5 (.8-1) | 3055 | -0.151497 | -0.141897 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.277484 | 0.265983 | 0.587771 | 0.736191 |
| tossup_correctness | tier | fall | 2842 | 0.315472 | 0.273374 | 0.602403 | 0.751861 |
| tossup_correctness | tier | nationals | 1564 | 0.192488 | 0.240783 | 0.581193 | 0.675846 |
| tossup_correctness | tier | regionals | 1937 | 0.25799 | 0.2554 | 0.605355 | 0.714607 |
| tossup_correctness | tier | winter | 2750 | 0.301311 | 0.28013 | 0.584633 | 0.769518 |
| tossup_correctness | category | Current Events | 126 | 0.335042 | 0.308801 | 0.537504 | 0.832632 |
| tossup_correctness | category | Fine Arts | 1071 | 0.293291 | 0.272574 | 0.594675 | 0.752369 |
| tossup_correctness | category | Geography | 185 | 0.2715 | 0.29164 | 0.564922 | 0.789933 |
| tossup_correctness | category | History | 1440 | 0.267814 | 0.263811 | 0.579666 | 0.728704 |
| tossup_correctness | category | Literature | 1422 | 0.309416 | 0.261041 | 0.561466 | 0.726724 |
| tossup_correctness | category | Mythology | 318 | 0.307766 | 0.274765 | 0.559493 | 0.756263 |
| tossup_correctness | category | Other Academic | 66 | 0.236695 | 0.233548 | 0.707727 | 0.658547 |
| tossup_correctness | category | Philosophy | 311 | 0.246272 | 0.254763 | 0.601811 | 0.709822 |
| tossup_correctness | category | Popular Culture | 102 | 0.477167 | 0.362867 | 0.441667 | 0.960342 |
| tossup_correctness | category | Religion | 358 | 0.225037 | 0.260551 | 0.586065 | 0.722797 |
| tossup_correctness | category | Science | 1433 | 0.27556 | 0.272838 | 0.594813 | 0.749851 |
| tossup_correctness | category | Social Science | 324 | 0.250837 | 0.261439 | 0.597459 | 0.723616 |
| tossup_correctness | category | Unknown | 1937 | 0.25799 | 0.2554 | 0.605355 | 0.714607 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.32558 | 0.312115 | 0.566702 | 0.842761 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.318399 | 0.302443 | 0.576415 | 0.819166 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.301185 | 0.27593 | 0.618172 | 0.760146 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.292354 | 0.266988 | 0.575414 | 0.73862 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.234498 | 0.244755 | 0.583467 | 0.686749 |
