# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.668266 |
| log_loss | 0.548664 |
| ece | 0.108636 |
| brier | 0.184581 |
| accuracy | 0.718591 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0455871 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.178641 |
| probability_p10 | 0.41065 |
| probability_p50 | 0.67424 |
| probability_p90 | 0.889391 |
| mean_predictive_variance | 0.192681 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.103666 |
| joint_tossup_event_log_loss | 6.67714 |
| buzz_position_mae | 0.15628 |
| buzz_position_median_absolute_error | 0.138651 |
| buzz_position_bias | -0.0599995 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.333261 |
| first_buzzer_mean_reciprocal_rank | 0.549005 |
| first_buzzer_log_loss | 1.7101 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.668266 |
| neg_average_precision | 0.380494 |
| neg_precision | 0.38999 |
| neg_recall | 0.342648 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.15848 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0058814 |
| no_buzz_calibration_error | -0.00723161 |
| no_buzz_brier | 0.0124261 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0599995 | -0.0753852 |
| Q1 (0-.2) | 183 | 0.370406 | 0.370831 |
| Q2 (.2-.4) | 955 | 0.197575 | 0.190981 |
| Q3 (.4-.6) | 2239 | 0.0453356 | 0.0400758 |
| Q4 (.6-.8) | 2875 | -0.0842332 | -0.0841489 |
| Q5 (.8-1) | 3005 | -0.223368 | -0.219156 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.108636 | 0.184581 | 0.668266 | 0.548664 |
| tossup_correctness | tier | fall | 2798 | 0.104169 | 0.173299 | 0.680504 | 0.521481 |
| tossup_correctness | tier | nationals | 1545 | 0.0950159 | 0.197516 | 0.656798 | 0.580387 |
| tossup_correctness | tier | regionals | 2039 | 0.127669 | 0.194557 | 0.647876 | 0.571023 |
| tossup_correctness | tier | winter | 2875 | 0.106974 | 0.181534 | 0.672357 | 0.542213 |
| tossup_correctness | category | Current Events | 129 | 0.077785 | 0.204687 | 0.687939 | 0.586276 |
| tossup_correctness | category | Fine Arts | 1074 | 0.11939 | 0.179143 | 0.683643 | 0.535635 |
| tossup_correctness | category | Geography | 180 | 0.0582491 | 0.193937 | 0.742003 | 0.568083 |
| tossup_correctness | category | History | 1454 | 0.0994891 | 0.185214 | 0.662514 | 0.550591 |
| tossup_correctness | category | Literature | 1435 | 0.109981 | 0.161317 | 0.679998 | 0.493353 |
| tossup_correctness | category | Mythology | 324 | 0.098995 | 0.174659 | 0.626982 | 0.531743 |
| tossup_correctness | category | Other Academic | 71 | 0.138581 | 0.198348 | 0.61329 | 0.591392 |
| tossup_correctness | category | Philosophy | 310 | 0.12467 | 0.194354 | 0.631356 | 0.574298 |
| tossup_correctness | category | Popular Culture | 108 | 0.162191 | 0.141199 | 0.37066 | 0.466204 |
| tossup_correctness | category | Religion | 361 | 0.134882 | 0.198723 | 0.672926 | 0.579423 |
| tossup_correctness | category | Science | 1445 | 0.098079 | 0.191105 | 0.662183 | 0.563324 |
| tossup_correctness | category | Social Science | 327 | 0.0806392 | 0.193892 | 0.68654 | 0.572341 |
| tossup_correctness | category | Unknown | 2039 | 0.127669 | 0.194557 | 0.647876 | 0.571023 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.058352 | 0.180719 | 0.663173 | 0.540782 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0397596 | 0.174073 | 0.703113 | 0.53063 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.052103 | 0.170173 | 0.708511 | 0.51509 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.120937 | 0.174426 | 0.684768 | 0.523839 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.175509 | 0.208607 | 0.635539 | 0.603641 |
