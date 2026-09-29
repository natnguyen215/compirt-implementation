# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-10000-steps/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-10000-steps/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 305306 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.625956 |
| log_loss | 0.641588 |
| ece | 0.210128 |
| brier | 0.223462 |
| accuracy | 0.652535 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.12082 |
| probability_std | 0.177477 |
| probability_p10 | 0.305499 |
| probability_p50 | 0.589006 |
| probability_p90 | 0.772815 |
| mean_predictive_variance | 0.214504 |
| integrated_brier_score | 0.0944982 |
| joint_tossup_event_log_loss | 6.72765 |
| buzz_position_mae | 0.138241 |
| buzz_position_median_absolute_error | 0.115044 |
| buzz_position_bias | 0.00368988 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.373894 |
| first_buzzer_mean_reciprocal_rank | 0.578967 |
| first_buzzer_log_loss | 1.65008 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.625956 |
| neg_average_precision | 0.317472 |
| neg_precision | 0.316152 |
| neg_recall | 0.458353 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.143305 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0474794 |
| no_buzz_calibration_error | 0.0357523 |
| no_buzz_brier | 0.0168542 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.625956 | 0.641588 | 0.210128 | 0.223462 | 0.652535 | 0.773355 | -0.12082 | 0.177477 | 0.305499 | 0.589006 | 0.772815 | 0.214504 |
| tossup_correctness | tier | fall | 2876 | 0.637052 | 0.621107 | 0.211821 | 0.21378 | 0.683588 | 0.793115 | -0.109527 | 0.182531 | 0.306024 | 0.61709 | 0.791671 | 0.210074 |
| tossup_correctness | tier | nationals | 1579 | 0.619515 | 0.622886 | 0.147987 | 0.216468 | 0.659278 | 0.729576 | -0.0702977 | 0.152113 | 0.372217 | 0.594871 | 0.765171 | 0.220205 |
| tossup_correctness | tier | regionals | 1990 | 0.64333 | 0.634504 | 0.208993 | 0.221407 | 0.646734 | 0.765829 | -0.119095 | 0.176651 | 0.304121 | 0.582006 | 0.770936 | 0.215564 |
| tossup_correctness | tier | winter | 2825 | 0.611035 | 0.677884 | 0.243938 | 0.238676 | 0.621239 | 0.783009 | -0.16177 | 0.182732 | 0.268101 | 0.565485 | 0.757519 | 0.215083 |
| tossup_correctness | category | Current Events | 123 | 0.669112 | 0.658491 | 0.237041 | 0.230217 | 0.626016 | 0.764228 | -0.138211 | 0.175742 | 0.275575 | 0.546171 | 0.750118 | 0.218301 |
| tossup_correctness | category | Fine Arts | 1093 | 0.620194 | 0.635035 | 0.191516 | 0.219657 | 0.672461 | 0.769442 | -0.0969808 | 0.176256 | 0.325284 | 0.612057 | 0.779198 | 0.212861 |
| tossup_correctness | category | Geography | 191 | 0.594633 | 0.732089 | 0.213061 | 0.263222 | 0.544503 | 0.691099 | -0.146597 | 0.167026 | 0.256786 | 0.481308 | 0.684437 | 0.22162 |
| tossup_correctness | category | History | 1469 | 0.629914 | 0.634426 | 0.191241 | 0.220316 | 0.655548 | 0.758339 | -0.102791 | 0.166557 | 0.331065 | 0.594432 | 0.756452 | 0.217757 |
| tossup_correctness | category | Literature | 1436 | 0.6091 | 0.585264 | 0.194694 | 0.197602 | 0.717967 | 0.81546 | -0.097493 | 0.172684 | 0.359805 | 0.660973 | 0.807679 | 0.205596 |
| tossup_correctness | category | Mythology | 325 | 0.512666 | 0.648122 | 0.25723 | 0.226172 | 0.649231 | 0.843077 | -0.193846 | 0.175603 | 0.33402 | 0.622778 | 0.788244 | 0.211794 |
| tossup_correctness | category | Other Academic | 67 | 0.622642 | 0.695515 | 0.25544 | 0.243865 | 0.597015 | 0.791045 | -0.19403 | 0.175884 | 0.305407 | 0.568768 | 0.715252 | 0.217797 |
| tossup_correctness | category | Philosophy | 322 | 0.699376 | 0.562865 | 0.181987 | 0.189436 | 0.729814 | 0.785714 | -0.0559006 | 0.182207 | 0.347897 | 0.6377 | 0.809853 | 0.205791 |
| tossup_correctness | category | Popular Culture | 100 | 0.53524 | 0.756286 | 0.371186 | 0.269372 | 0.57 | 0.89 | -0.32 | 0.186873 | 0.240518 | 0.531846 | 0.730908 | 0.214725 |
| tossup_correctness | category | Religion | 365 | 0.64574 | 0.637598 | 0.154465 | 0.222143 | 0.671233 | 0.723288 | -0.0520548 | 0.184404 | 0.297419 | 0.592472 | 0.788682 | 0.211258 |
| tossup_correctness | category | Science | 1456 | 0.598499 | 0.710524 | 0.260148 | 0.25405 | 0.585165 | 0.76717 | -0.182005 | 0.169303 | 0.271127 | 0.523812 | 0.722835 | 0.221273 |
| tossup_correctness | category | Social Science | 333 | 0.628212 | 0.649181 | 0.188045 | 0.228389 | 0.636637 | 0.72973 | -0.0930931 | 0.178343 | 0.282345 | 0.571804 | 0.752412 | 0.216456 |
| tossup_correctness | category | Unknown | 1990 | 0.64333 | 0.634504 | 0.208993 | 0.221407 | 0.646734 | 0.765829 | -0.119095 | 0.176651 | 0.304121 | 0.582006 | 0.770936 | 0.215564 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.68209 | 0.730269 | 0.295674 | 0.26309 | 0.564246 | 0.748603 | -0.184358 | 0.177482 | 0.194488 | 0.473059 | 0.654791 | 0.216285 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.610397 | 0.710766 | 0.254851 | 0.254395 | 0.574713 | 0.754441 | -0.179728 | 0.175607 | 0.254624 | 0.516753 | 0.714178 | 0.219162 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.644597 | 0.674301 | 0.238345 | 0.236258 | 0.633227 | 0.766682 | -0.133454 | 0.177133 | 0.27522 | 0.551647 | 0.741464 | 0.217821 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.629767 | 0.627916 | 0.215628 | 0.217311 | 0.667898 | 0.787441 | -0.119543 | 0.172263 | 0.319708 | 0.597827 | 0.770075 | 0.215168 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.617502 | 0.603177 | 0.163877 | 0.207692 | 0.682018 | 0.771758 | -0.0897392 | 0.169171 | 0.360213 | 0.634092 | 0.804236 | 0.209743 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | 0.126582 | 1.03885 | -3.27435 | -1.47034 | -0.498273 | -0.0226944 | 0.769719 | 2.03559 | 3.93447 |
| player | theta_2 | 1196 | -0.0792319 | 1.01736 | -3.81663 | -1.63288 | -0.621095 | -0.160988 | 0.423256 | 1.69225 | 4.37163 |
| player | theta_3 | 1196 | 1.04633 | 1.37311 | -3.00486 | -1.17864 | -0.0801972 | 1.2412 | 2.20731 | 3.03378 | 4.14746 |
| player | theta_norm | 1196 | 2.02129 | 1.01424 | 0.124598 | 0.530118 | 1.21574 | 1.95523 | 2.74947 | 3.80723 | 5.13374 |
| tossup | start_difficulty_d1 | 1240 | 1.2235 | 0.687901 | -0.94736 | 0.100134 | 0.629209 | 1.3831 | 1.73678 | 2.20423 | 2.85177 |
| tossup | start_difficulty_d2 | 1240 | 0.478142 | 0.602561 | -1.60663 | -0.552036 | 0.134269 | 0.47583 | 0.84731 | 1.45997 | 2.95774 |
| tossup | start_difficulty_d3 | 1240 | 1.60039 | 1.16847 | -1.19382 | -0.323554 | 0.623534 | 1.52607 | 2.64569 | 3.19076 | 3.98101 |
| tossup | end_difficulty_d1 | 1240 | 0.075466 | 0.538767 | -2.02952 | -0.927888 | -0.287442 | 0.252148 | 0.450532 | 0.734585 | 1.26934 |
| tossup | end_difficulty_d2 | 1240 | -0.459259 | 0.7096 | -4.95816 | -1.66442 | -0.834415 | -0.453328 | -0.0177681 | 0.654825 | 2.28258 |
| tossup | end_difficulty_d3 | 1240 | 0.345522 | 0.907012 | -5.64814 | -1.3922 | -0.257569 | 0.508914 | 1.07532 | 1.49034 | 2.05011 |
| tossup | total_drop_d1 | 1240 | 1.14803 | 0.338169 | 0.458478 | 0.774769 | 0.902947 | 1.03226 | 1.34084 | 1.77502 | 3.34955 |
| tossup | total_drop_d2 | 1240 | 0.937401 | 0.222824 | 0.645547 | 0.765713 | 0.861479 | 0.919001 | 0.975319 | 1.09156 | 5.62891 |
| tossup | total_drop_d3 | 1240 | 1.25487 | 0.533733 | 0.600837 | 0.734886 | 0.850097 | 1.02054 | 1.59424 | 2.23786 | 5.52621 |
| tossup | drop_share_1_d1 | 1240 | 0.203153 | 0.0834782 | 0.0401899 | 0.0871355 | 0.125432 | 0.195442 | 0.283339 | 0.310778 | 0.569758 |
| tossup | drop_share_2_d1 | 1240 | 0.267434 | 0.097961 | 0.0689812 | 0.112559 | 0.177089 | 0.311539 | 0.344183 | 0.369244 | 0.706601 |
| tossup | drop_share_3_d1 | 1240 | 0.529413 | 0.167824 | 0.16283 | 0.343387 | 0.371917 | 0.481364 | 0.689837 | 0.797329 | 0.890292 |
| tossup | drop_share_1_d2 | 1240 | 0.28623 | 0.0264177 | 0.0742856 | 0.242038 | 0.279359 | 0.29117 | 0.300658 | 0.313852 | 0.333218 |
| tossup | drop_share_2_d2 | 1240 | 0.341967 | 0.016797 | 0.137024 | 0.31815 | 0.335516 | 0.343825 | 0.351339 | 0.3624 | 0.38595 |
| tossup | drop_share_3_d2 | 1240 | 0.371802 | 0.0372697 | 0.315564 | 0.339125 | 0.353205 | 0.363874 | 0.378904 | 0.43165 | 0.78869 |
| tossup | drop_share_1_d3 | 1240 | 0.230269 | 0.0929059 | 0.03634 | 0.0788777 | 0.13974 | 0.269913 | 0.291228 | 0.316629 | 0.681458 |
| tossup | drop_share_2_d3 | 1240 | 0.296833 | 0.0984042 | 0.0458184 | 0.109399 | 0.238475 | 0.331541 | 0.34655 | 0.429633 | 0.64478 |
| tossup | drop_share_3_d3 | 1240 | 0.472899 | 0.162247 | 0.0726345 | 0.332762 | 0.364757 | 0.388448 | 0.576658 | 0.80348 | 0.917842 |
| tossup | r_1 | 1240 | 0.394501 | 0.29798 | 0.0118081 | 0.0191863 | 0.0602446 | 0.466202 | 0.665532 | 0.816462 | 0.914702 |
| tossup | r_2 | 1240 | 0.141104 | 0.127071 | 0.0141788 | 0.0214547 | 0.045468 | 0.0934682 | 0.197678 | 0.422476 | 0.592073 |
| tossup | r_3 | 1240 | 0.464395 | 0.344709 | 0.0280533 | 0.0556091 | 0.135243 | 0.320768 | 0.827717 | 0.948744 | 0.968443 |
| tossup | r_norm | 1240 | 0.777903 | 0.0982956 | 0.581056 | 0.638463 | 0.694956 | 0.764009 | 0.857955 | 0.949438 | 0.968702 |
