# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 301832 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.611355 |
| log_loss | 0.786612 |
| ece | 0.344156 |
| brier | 0.294051 |
| accuracy | 0.379559 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.385691 |
| probability_std | 0.0965866 |
| probability_p10 | 0.295826 |
| probability_p50 | 0.420877 |
| probability_p90 | 0.545136 |
| mean_predictive_variance | 0.234445 |
| integrated_brier_score | 0.0942375 |
| joint_tossup_event_log_loss | 6.7712 |
| buzz_position_mae | 0.138316 |
| buzz_position_median_absolute_error | 0.116939 |
| buzz_position_bias | -0.00475391 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.39376 |
| first_buzzer_mean_reciprocal_rank | 0.599511 |
| first_buzzer_log_loss | 1.59468 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.611355 |
| neg_average_precision | 0.31809 |
| neg_precision | 0.25589 |
| neg_recall | 0.861137 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.127483 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0496625 |
| no_buzz_calibration_error | 0.0363929 |
| no_buzz_brier | 0.0197215 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.611355 | 0.786612 | 0.344156 | 0.294051 | 0.379559 | 0.76525 | -0.385691 | 0.0965866 | 0.295826 | 0.420877 | 0.545136 | 0.234445 |
| tossup_correctness | tier | fall | 2933 | 0.614801 | 0.798374 | 0.372467 | 0.299763 | 0.35629 | 0.791681 | -0.43539 | 0.0925217 | 0.29887 | 0.41977 | 0.536377 | 0.235008 |
| tossup_correctness | tier | nationals | 1584 | 0.576529 | 0.767642 | 0.292944 | 0.284715 | 0.421717 | 0.724747 | -0.30303 | 0.102499 | 0.298043 | 0.433431 | 0.562024 | 0.23486 |
| tossup_correctness | tier | regionals | 1886 | 0.622397 | 0.769783 | 0.320987 | 0.286025 | 0.411983 | 0.746023 | -0.33404 | 0.104537 | 0.294205 | 0.424057 | 0.561084 | 0.233516 |
| tossup_correctness | tier | winter | 2892 | 0.631551 | 0.796048 | 0.35961 | 0.298604 | 0.358921 | 0.773167 | -0.414246 | 0.0910315 | 0.293262 | 0.414206 | 0.531533 | 0.234252 |
| tossup_correctness | category | Current Events | 124 | 0.623656 | 0.782536 | 0.345234 | 0.292614 | 0.379032 | 0.75 | -0.370968 | 0.0938975 | 0.294669 | 0.422741 | 0.528348 | 0.234291 |
| tossup_correctness | category | Fine Arts | 1103 | 0.608578 | 0.791902 | 0.343913 | 0.29672 | 0.371714 | 0.759746 | -0.388033 | 0.0951043 | 0.290372 | 0.41355 | 0.532812 | 0.233871 |
| tossup_correctness | category | Geography | 197 | 0.568182 | 0.793981 | 0.277861 | 0.297092 | 0.416244 | 0.670051 | -0.253807 | 0.0917215 | 0.272696 | 0.388193 | 0.52533 | 0.229964 |
| tossup_correctness | category | History | 1491 | 0.655412 | 0.780154 | 0.362028 | 0.291043 | 0.374245 | 0.787391 | -0.413146 | 0.0939636 | 0.304885 | 0.426601 | 0.540767 | 0.235618 |
| tossup_correctness | category | Literature | 1472 | 0.565928 | 0.794005 | 0.370971 | 0.297233 | 0.371603 | 0.804348 | -0.432745 | 0.0989427 | 0.298673 | 0.437006 | 0.555843 | 0.235772 |
| tossup_correctness | category | Mythology | 332 | 0.594564 | 0.838786 | 0.413072 | 0.319602 | 0.274096 | 0.813253 | -0.539157 | 0.0826711 | 0.288879 | 0.404234 | 0.51366 | 0.23332 |
| tossup_correctness | category | Other Academic | 69 | 0.606335 | 0.808212 | 0.357998 | 0.304184 | 0.376812 | 0.753623 | -0.376812 | 0.0944529 | 0.293321 | 0.40946 | 0.520248 | 0.232512 |
| tossup_correctness | category | Philosophy | 324 | 0.601396 | 0.79083 | 0.369973 | 0.296046 | 0.388889 | 0.799383 | -0.410494 | 0.09259 | 0.30395 | 0.429533 | 0.55043 | 0.236444 |
| tossup_correctness | category | Popular Culture | 102 | 0.488581 | 0.915339 | 0.454698 | 0.354174 | 0.196078 | 0.833333 | -0.637255 | 0.0841091 | 0.265021 | 0.384477 | 0.472548 | 0.228196 |
| tossup_correctness | category | Religion | 372 | 0.610655 | 0.774487 | 0.294494 | 0.287787 | 0.405914 | 0.709677 | -0.303763 | 0.0934998 | 0.296826 | 0.412883 | 0.544725 | 0.234064 |
| tossup_correctness | category | Science | 1487 | 0.606126 | 0.785608 | 0.334198 | 0.293621 | 0.381305 | 0.752522 | -0.371217 | 0.0924453 | 0.301446 | 0.417755 | 0.538458 | 0.234878 |
| tossup_correctness | category | Social Science | 336 | 0.62572 | 0.775887 | 0.299379 | 0.289821 | 0.375 | 0.702381 | -0.327381 | 0.0860261 | 0.292076 | 0.401957 | 0.52539 | 0.233191 |
| tossup_correctness | category | Unknown | 1886 | 0.622397 | 0.769783 | 0.320987 | 0.286025 | 0.411983 | 0.746023 | -0.33404 | 0.104537 | 0.294205 | 0.424057 | 0.561084 | 0.233516 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.614058 | 0.950286 | 0.423244 | 0.366684 | 0.274112 | 0.736041 | -0.461929 | 0.0841739 | 0.209601 | 0.30535 | 0.435265 | 0.20787 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.630559 | 0.882585 | 0.388623 | 0.337519 | 0.301523 | 0.735025 | -0.433503 | 0.0893669 | 0.233197 | 0.342176 | 0.458348 | 0.218421 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.607038 | 0.834536 | 0.379348 | 0.316679 | 0.320302 | 0.769436 | -0.449134 | 0.0886329 | 0.279398 | 0.389376 | 0.506334 | 0.230203 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.63517 | 0.78056 | 0.358276 | 0.291776 | 0.372296 | 0.78402 | -0.411724 | 0.0886604 | 0.31498 | 0.421936 | 0.540853 | 0.236625 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.613002 | 0.714079 | 0.284863 | 0.260159 | 0.463618 | 0.756008 | -0.29239 | 0.0812724 | 0.370227 | 0.468656 | 0.575103 | 0.242562 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | 5.11932 | 1.61238 | 1.6465 | 3.49411 | 4.18559 | 4.72587 | 5.57248 | 7.78638 | 13.5519 |
| player | beta | 1186 | -2.88222 | 0.828097 | -6.5887 | -4.36285 | -3.36033 | -2.75642 | -2.32044 | -1.7258 | -0.94477 |
| player | theta_1 | 1186 | -1.58019 | 0.521807 | -3.31001 | -2.40929 | -1.92906 | -1.59443 | -1.23191 | -0.700919 | 0.0682425 |
| player | theta_2 | 1186 | -1.54342 | 0.567325 | -3.86586 | -2.45062 | -1.91477 | -1.57621 | -1.16781 | -0.580514 | 0.730645 |
| player | theta_3 | 1186 | -1.62295 | 0.602654 | -3.21905 | -2.55486 | -2.02093 | -1.65844 | -1.26437 | -0.514425 | 0.768163 |
| player | theta_norm | 1186 | 2.86162 | 0.530108 | 0.772531 | 1.95688 | 2.52078 | 2.88758 | 3.21479 | 3.68085 | 4.31838 |
| tossup | start_difficulty_d1 | 1240 | 0.146185 | 0.317978 | -0.978768 | -0.426038 | -0.058857 | 0.155961 | 0.364678 | 0.648614 | 1.09263 |
| tossup | start_difficulty_d2 | 1240 | 0.173666 | 0.307655 | -0.862776 | -0.333835 | -0.0336381 | 0.182694 | 0.390059 | 0.648843 | 1.05995 |
| tossup | start_difficulty_d3 | 1240 | 0.179483 | 0.309397 | -0.905702 | -0.343106 | -0.0303464 | 0.180061 | 0.3785 | 0.680285 | 1.17496 |
| tossup | end_difficulty_d1 | 1240 | -1.31326 | 0.597992 | -3.86005 | -2.24053 | -1.71441 | -1.34656 | -0.828941 | -0.390794 | 0.0538846 |
| tossup | end_difficulty_d2 | 1240 | -1.18674 | 0.54288 | -3.23396 | -2.04257 | -1.57775 | -1.17365 | -0.744045 | -0.381713 | 0.108555 |
| tossup | end_difficulty_d3 | 1240 | -1.20576 | 0.534934 | -3.08756 | -2.02042 | -1.586 | -1.22871 | -0.808056 | -0.314619 | 0.114987 |
| tossup | total_drop_d1 | 1240 | 1.45944 | 0.544564 | 0.540288 | 0.884355 | 1.00723 | 1.32474 | 1.79441 | 2.47458 | 4.8257 |
| tossup | total_drop_d2 | 1240 | 1.3604 | 0.476979 | 0.614558 | 0.871632 | 0.971095 | 1.21 | 1.63941 | 2.29967 | 3.36088 |
| tossup | total_drop_d3 | 1240 | 1.38524 | 0.493047 | 0.683375 | 0.871943 | 0.966935 | 1.23174 | 1.6835 | 2.35339 | 3.65671 |
| tossup | drop_share_1_d1 | 1240 | 0.262662 | 0.0892288 | 0.0449815 | 0.137358 | 0.208896 | 0.263022 | 0.292828 | 0.454347 | 0.749432 |
| tossup | drop_share_2_d1 | 1240 | 0.279977 | 0.062533 | 0.0815503 | 0.162729 | 0.240238 | 0.295939 | 0.327811 | 0.355053 | 0.486754 |
| tossup | drop_share_3_d1 | 1240 | 0.457361 | 0.118778 | 0.0942358 | 0.294709 | 0.37934 | 0.427915 | 0.526598 | 0.683696 | 0.848053 |
| tossup | drop_share_1_d2 | 1240 | 0.25802 | 0.0714796 | 0.0692615 | 0.141676 | 0.219318 | 0.262159 | 0.290836 | 0.370647 | 0.671571 |
| tossup | drop_share_2_d2 | 1240 | 0.284949 | 0.0645618 | 0.0694072 | 0.147475 | 0.251902 | 0.305361 | 0.33032 | 0.354957 | 0.566513 |
| tossup | drop_share_3_d2 | 1240 | 0.457031 | 0.110274 | 0.080019 | 0.333073 | 0.383322 | 0.429368 | 0.513117 | 0.681235 | 0.843927 |
| tossup | drop_share_1_d3 | 1240 | 0.253003 | 0.0766009 | 0.0677952 | 0.131127 | 0.207317 | 0.258524 | 0.288826 | 0.371622 | 0.676447 |
| tossup | drop_share_2_d3 | 1240 | 0.282095 | 0.0634288 | 0.0740534 | 0.160705 | 0.247118 | 0.29838 | 0.329892 | 0.351638 | 0.543856 |
| tossup | drop_share_3_d3 | 1240 | 0.464901 | 0.115746 | 0.116942 | 0.328154 | 0.385347 | 0.432315 | 0.532201 | 0.696611 | 0.850405 |
| tossup | r_1 | 1240 | 0.351049 | 0.196302 | 0.0338046 | 0.0941537 | 0.184047 | 0.318318 | 0.499756 | 0.691201 | 0.856691 |
| tossup | r_2 | 1240 | 0.315214 | 0.191036 | 0.03177 | 0.0839259 | 0.169584 | 0.262409 | 0.431784 | 0.684611 | 0.913347 |
| tossup | r_3 | 1240 | 0.333738 | 0.187919 | 0.0296115 | 0.0985751 | 0.190206 | 0.285013 | 0.458226 | 0.69737 | 0.833604 |
| tossup | r_norm | 1240 | 0.663523 | 0.0630132 | 0.577608 | 0.582837 | 0.609591 | 0.65426 | 0.707007 | 0.778455 | 0.915417 |
