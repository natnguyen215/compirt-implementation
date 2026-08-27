# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710245 |
| log_loss | 0.516595 |
| ece | 0.0712918 |
| brier | 0.167368 |
| accuracy | 0.762675 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.000549874 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.204099 |
| probability_p10 | 0.414822 |
| probability_p50 | 0.749419 |
| probability_p90 | 0.947577 |
| mean_predictive_variance | 0.164341 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.093426 |
| joint_tossup_event_log_loss | 6.44574 |
| buzz_position_mae | 0.135488 |
| buzz_position_median_absolute_error | 0.109694 |
| buzz_position_bias | 0.00457248 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.379523 |
| first_buzzer_mean_reciprocal_rank | 0.585948 |
| first_buzzer_log_loss | 1.62194 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710245 |
| neg_average_precision | 0.459805 |
| neg_precision | 0.501618 |
| neg_recall | 0.358299 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.193315 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00968118 |
| no_buzz_calibration_error | -0.00622791 |
| no_buzz_brier | 0.014959 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.00457248 | -0.0182787 |
| Q1 (0-.2) | 167 | 0.399326 | 0.415 |
| Q2 (.2-.4) | 912 | 0.240347 | 0.240096 |
| Q3 (.4-.6) | 2115 | 0.0990839 | 0.0955664 |
| Q4 (.6-.8) | 2844 | -0.0171713 | -0.0185043 |
| Q5 (.8-1) | 3055 | -0.132581 | -0.120912 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0712918 | 0.167368 | 0.710245 | 0.516595 |
| tossup_correctness | tier | fall | 2842 | 0.0544837 | 0.154311 | 0.725096 | 0.480072 |
| tossup_correctness | tier | nationals | 1564 | 0.0791637 | 0.186111 | 0.707535 | 0.562881 |
| tossup_correctness | tier | regionals | 1937 | 0.0852687 | 0.1731 | 0.694808 | 0.534506 |
| tossup_correctness | tier | winter | 2750 | 0.0755065 | 0.166167 | 0.701887 | 0.5154 |
| tossup_correctness | category | Current Events | 126 | 0.11486 | 0.170308 | 0.732314 | 0.510774 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0655255 | 0.158162 | 0.74246 | 0.486497 |
| tossup_correctness | category | Geography | 185 | 0.112288 | 0.16151 | 0.817276 | 0.504004 |
| tossup_correctness | category | History | 1440 | 0.0647511 | 0.16733 | 0.718047 | 0.517794 |
| tossup_correctness | category | Literature | 1422 | 0.0826887 | 0.154406 | 0.667321 | 0.485611 |
| tossup_correctness | category | Mythology | 318 | 0.0949595 | 0.159212 | 0.662782 | 0.500961 |
| tossup_correctness | category | Other Academic | 66 | 0.107892 | 0.157506 | 0.789474 | 0.480513 |
| tossup_correctness | category | Philosophy | 311 | 0.0629007 | 0.164742 | 0.747054 | 0.49596 |
| tossup_correctness | category | Popular Culture | 102 | 0.12224 | 0.127255 | 0.491667 | 0.438077 |
| tossup_correctness | category | Religion | 358 | 0.0592886 | 0.187574 | 0.709461 | 0.568294 |
| tossup_correctness | category | Science | 1433 | 0.0766285 | 0.182699 | 0.689227 | 0.555766 |
| tossup_correctness | category | Social Science | 324 | 0.0714968 | 0.157833 | 0.770697 | 0.485968 |
| tossup_correctness | category | Unknown | 1937 | 0.0852687 | 0.1731 | 0.694808 | 0.534506 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.144089 | 0.211616 | 0.668417 | 0.6248 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.101378 | 0.185223 | 0.725256 | 0.554871 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0732051 | 0.169882 | 0.710895 | 0.522721 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0650106 | 0.162592 | 0.692742 | 0.505428 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0637928 | 0.162326 | 0.721033 | 0.505409 |
