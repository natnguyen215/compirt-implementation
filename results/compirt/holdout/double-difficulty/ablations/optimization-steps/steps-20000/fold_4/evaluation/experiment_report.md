# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.723911 |
| log_loss | 0.476368 |
| ece | 0.00945502 |
| brier | 0.153909 |
| accuracy | 0.787055 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0137001 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147983 |
| probability_p10 | 0.564735 |
| probability_p50 | 0.805899 |
| probability_p90 | 0.919504 |
| mean_predictive_variance | 0.155507 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0944535 |
| joint_tossup_event_log_loss | 6.45616 |
| buzz_position_mae | 0.138839 |
| buzz_position_median_absolute_error | 0.116546 |
| buzz_position_bias | -0.00341 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.361812 |
| first_buzzer_mean_reciprocal_rank | 0.572395 |
| first_buzzer_log_loss | 1.65597 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.723911 |
| neg_average_precision | 0.451119 |
| neg_precision | 0.607445 |
| neg_recall | 0.170871 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.179183 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0096886 |
| no_buzz_calibration_error | -0.00203848 |
| no_buzz_brier | 0.0110385 |
| full_pmf_max_mass_error | 1.66533e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.00341 | -0.0272338 |
| Q1 (0-.2) | 179 | 0.399924 | 0.402166 |
| Q2 (.2-.4) | 957 | 0.245321 | 0.234964 |
| Q3 (.4-.6) | 2203 | 0.0961746 | 0.0934155 |
| Q4 (.6-.8) | 2978 | -0.0310786 | -0.0306065 |
| Q5 (.8-1) | 2953 | -0.154856 | -0.146966 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.00945502 | 0.153909 | 0.723911 | 0.476368 |
| tossup_correctness | tier | fall | 2876 | 0.0156965 | 0.143876 | 0.731461 | 0.451283 |
| tossup_correctness | tier | nationals | 1579 | 0.0325796 | 0.174505 | 0.71269 | 0.528055 |
| tossup_correctness | tier | regionals | 1990 | 0.0129898 | 0.155462 | 0.736986 | 0.478649 |
| tossup_correctness | tier | winter | 2825 | 0.0164923 | 0.151518 | 0.712243 | 0.47141 |
| tossup_correctness | category | Current Events | 123 | 0.0803451 | 0.144078 | 0.802641 | 0.447649 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0131213 | 0.14976 | 0.74086 | 0.466978 |
| tossup_correctness | category | Geography | 191 | 0.0696761 | 0.158476 | 0.785953 | 0.48981 |
| tossup_correctness | category | History | 1469 | 0.0312914 | 0.165686 | 0.711735 | 0.503316 |
| tossup_correctness | category | Literature | 1436 | 0.0156688 | 0.136994 | 0.705212 | 0.436952 |
| tossup_correctness | category | Mythology | 325 | 0.0623641 | 0.131933 | 0.66087 | 0.424701 |
| tossup_correctness | category | Other Academic | 67 | 0.0703488 | 0.160951 | 0.679245 | 0.494904 |
| tossup_correctness | category | Philosophy | 322 | 0.0255468 | 0.158981 | 0.682935 | 0.488368 |
| tossup_correctness | category | Popular Culture | 100 | 0.0604915 | 0.105932 | 0.54954 | 0.364756 |
| tossup_correctness | category | Religion | 365 | 0.0549449 | 0.188757 | 0.662991 | 0.562446 |
| tossup_correctness | category | Science | 1456 | 0.0140922 | 0.156107 | 0.72185 | 0.482297 |
| tossup_correctness | category | Social Science | 333 | 0.0382768 | 0.161977 | 0.754961 | 0.495893 |
| tossup_correctness | category | Unknown | 1990 | 0.0129898 | 0.155462 | 0.736986 | 0.478649 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.055118 | 0.162185 | 0.75539 | 0.492854 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0278979 | 0.163528 | 0.705788 | 0.500778 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0196847 | 0.15641 | 0.727829 | 0.481924 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.00785886 | 0.14833 | 0.712295 | 0.464205 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0128848 | 0.154051 | 0.73341 | 0.475579 |
