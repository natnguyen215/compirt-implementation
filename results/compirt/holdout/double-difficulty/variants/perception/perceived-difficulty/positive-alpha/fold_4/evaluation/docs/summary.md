# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299331 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.60599 |
| log_loss | 0.636827 |
| ece | 0.211671 |
| brier | 0.222695 |
| accuracy | 0.649407 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.123948 |
| probability_std | 0.149863 |
| probability_p10 | 0.343482 |
| probability_p50 | 0.581456 |
| probability_p90 | 0.741257 |
| mean_predictive_variance | 0.223736 |
| integrated_brier_score | 0.0950001 |
| joint_tossup_event_log_loss | 6.67489 |
| buzz_position_mae | 0.136863 |
| buzz_position_median_absolute_error | 0.111577 |
| buzz_position_bias | 0.00501506 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.38932 |
| first_buzzer_mean_reciprocal_rank | 0.595546 |
| first_buzzer_log_loss | 1.62063 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.60599 |
| neg_average_precision | 0.305573 |
| neg_precision | 0.306501 |
| neg_recall | 0.433127 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.137812 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0479197 |
| no_buzz_calibration_error | 0.0361927 |
| no_buzz_brier | 0.0181184 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.60599 | 0.636827 | 0.211671 | 0.222695 | 0.649407 | 0.773355 | -0.123948 | 0.149863 | 0.343482 | 0.581456 | 0.741257 | 0.223736 |
| tossup_correctness | tier | fall | 2876 | 0.621658 | 0.63232 | 0.234249 | 0.220555 | 0.654381 | 0.793115 | -0.138734 | 0.150799 | 0.335928 | 0.577193 | 0.742301 | 0.223794 |
| tossup_correctness | tier | nationals | 1579 | 0.608267 | 0.617544 | 0.13717 | 0.214216 | 0.664978 | 0.729576 | -0.0645978 | 0.135952 | 0.407619 | 0.606952 | 0.76624 | 0.222877 |
| tossup_correctness | tier | regionals | 1990 | 0.60762 | 0.630888 | 0.198365 | 0.219832 | 0.661809 | 0.765829 | -0.10402 | 0.154223 | 0.340374 | 0.595337 | 0.748314 | 0.221664 |
| tossup_correctness | tier | winter | 2825 | 0.602374 | 0.656378 | 0.240006 | 0.231631 | 0.626903 | 0.783009 | -0.156106 | 0.150112 | 0.320958 | 0.561193 | 0.723163 | 0.225617 |
| tossup_correctness | category | Current Events | 123 | 0.619956 | 0.647261 | 0.224957 | 0.227743 | 0.626016 | 0.764228 | -0.138211 | 0.14109 | 0.340419 | 0.55099 | 0.7094 | 0.228551 |
| tossup_correctness | category | Fine Arts | 1093 | 0.617297 | 0.628836 | 0.197204 | 0.219034 | 0.656908 | 0.769442 | -0.112534 | 0.152774 | 0.346736 | 0.595688 | 0.754175 | 0.221442 |
| tossup_correctness | category | Geography | 191 | 0.531073 | 0.707051 | 0.171465 | 0.256004 | 0.549738 | 0.691099 | -0.141361 | 0.145371 | 0.303791 | 0.5373 | 0.690439 | 0.228482 |
| tossup_correctness | category | History | 1469 | 0.620171 | 0.623432 | 0.188553 | 0.216794 | 0.66644 | 0.758339 | -0.0918993 | 0.142026 | 0.366671 | 0.586125 | 0.741252 | 0.224959 |
| tossup_correctness | category | Literature | 1436 | 0.61076 | 0.593975 | 0.218377 | 0.202515 | 0.701253 | 0.81546 | -0.114206 | 0.151659 | 0.367913 | 0.632172 | 0.764202 | 0.217574 |
| tossup_correctness | category | Mythology | 325 | 0.463861 | 0.671279 | 0.293347 | 0.239006 | 0.603077 | 0.843077 | -0.24 | 0.136411 | 0.35326 | 0.574567 | 0.711459 | 0.228919 |
| tossup_correctness | category | Other Academic | 67 | 0.621294 | 0.660578 | 0.254793 | 0.232754 | 0.626866 | 0.791045 | -0.164179 | 0.147128 | 0.304149 | 0.548187 | 0.708315 | 0.227039 |
| tossup_correctness | category | Philosophy | 322 | 0.664719 | 0.58183 | 0.196718 | 0.197334 | 0.732919 | 0.785714 | -0.052795 | 0.144475 | 0.386564 | 0.617738 | 0.750721 | 0.221207 |
| tossup_correctness | category | Popular Culture | 100 | 0.588355 | 0.683812 | 0.359374 | 0.242756 | 0.62 | 0.89 | -0.27 | 0.141656 | 0.359848 | 0.533644 | 0.68951 | 0.228996 |
| tossup_correctness | category | Religion | 365 | 0.630701 | 0.64509 | 0.174642 | 0.226624 | 0.632877 | 0.723288 | -0.090411 | 0.147314 | 0.349472 | 0.568107 | 0.732013 | 0.225932 |
| tossup_correctness | category | Science | 1456 | 0.573676 | 0.691299 | 0.25014 | 0.247858 | 0.581731 | 0.76717 | -0.18544 | 0.140795 | 0.31396 | 0.531631 | 0.689692 | 0.229881 |
| tossup_correctness | category | Social Science | 333 | 0.606493 | 0.65174 | 0.185679 | 0.230139 | 0.60961 | 0.72973 | -0.12012 | 0.147547 | 0.315286 | 0.565082 | 0.724573 | 0.226199 |
| tossup_correctness | category | Unknown | 1990 | 0.60762 | 0.630888 | 0.198365 | 0.219832 | 0.661809 | 0.765829 | -0.10402 | 0.154223 | 0.340374 | 0.595337 | 0.748314 | 0.221664 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.639303 | 0.685625 | 0.258822 | 0.246055 | 0.569832 | 0.748603 | -0.178771 | 0.154644 | 0.266151 | 0.510407 | 0.668209 | 0.225998 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.606342 | 0.675021 | 0.231143 | 0.240269 | 0.599791 | 0.754441 | -0.15465 | 0.151064 | 0.301068 | 0.542801 | 0.706153 | 0.226637 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.629039 | 0.650506 | 0.224945 | 0.228401 | 0.642306 | 0.766682 | -0.124376 | 0.150498 | 0.324866 | 0.559132 | 0.719757 | 0.225608 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.599979 | 0.63218 | 0.222411 | 0.220556 | 0.654466 | 0.787441 | -0.132975 | 0.146243 | 0.353864 | 0.584779 | 0.738131 | 0.224384 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.593341 | 0.615974 | 0.181824 | 0.213485 | 0.670505 | 0.771758 | -0.101253 | 0.145955 | 0.371333 | 0.612845 | 0.764424 | 0.220609 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | 0.334404 | 0.920916 | -1.92133 | -1.0128 | -0.405322 | 0.255368 | 0.971074 | 1.87449 | 3.18203 |
| player | theta_2 | 1196 | 0.448547 | 0.962972 | -1.9023 | -0.903513 | -0.323783 | 0.334865 | 1.13206 | 2.15141 | 3.26967 |
| player | theta_3 | 1196 | 0.133316 | 0.765455 | -1.7519 | -0.962362 | -0.437036 | 0.0594718 | 0.620931 | 1.53353 | 2.77121 |
| player | alpha_1 | 1196 | 8.71862 | 3.85256 | 1.15413 | 3.63447 | 6.07313 | 8.05182 | 10.7067 | 15.785 | 30.1799 |
| player | alpha_2 | 1196 | 10.3789 | 5.07236 | 1.62478 | 4.62032 | 7.10775 | 9.34625 | 12.4402 | 19.3947 | 43.5698 |
| player | alpha_3 | 1196 | 5.71379 | 3.45802 | 0.587177 | 1.37833 | 3.19546 | 5.06661 | 7.5667 | 11.7726 | 24.1828 |
| player | beta_1 | 1196 | -1.68705 | 0.587479 | -3.74866 | -2.72806 | -2.06696 | -1.65279 | -1.26044 | -0.796705 | -0.181175 |
| player | beta_2 | 1196 | -1.56672 | 0.570457 | -4.03599 | -2.55033 | -1.91398 | -1.54466 | -1.1657 | -0.696597 | -0.0362915 |
| player | beta_3 | 1196 | -1.43529 | 0.608367 | -3.70201 | -2.54604 | -1.81534 | -1.36951 | -0.994049 | -0.550576 | -0.0344322 |
| player | theta_norm | 1196 | 1.48342 | 0.700003 | 0.111104 | 0.500191 | 0.947083 | 1.37283 | 1.95824 | 2.74213 | 3.78515 |
| tossup | start_difficulty_d1 | 1240 | 1.15432 | 0.288396 | -0.165655 | 0.647065 | 0.987927 | 1.16971 | 1.34425 | 1.6035 | 2.03519 |
| tossup | start_difficulty_d2 | 1240 | 1.23933 | 0.306577 | -0.292675 | 0.782814 | 1.05368 | 1.22232 | 1.4294 | 1.74772 | 2.35156 |
| tossup | start_difficulty_d3 | 1240 | 1.01398 | 0.389738 | -0.590567 | 0.274534 | 0.811167 | 1.06144 | 1.2752 | 1.57329 | 1.97578 |
| tossup | end_difficulty_d1 | 1240 | 0.142164 | 0.366799 | -1.99784 | -0.553388 | -0.0176857 | 0.194109 | 0.365661 | 0.612271 | 0.997809 |
| tossup | end_difficulty_d2 | 1240 | 0.328947 | 0.364942 | -1.27604 | -0.2677 | 0.133416 | 0.314809 | 0.542899 | 0.917831 | 1.67297 |
| tossup | end_difficulty_d3 | 1240 | 0.00246199 | 0.554416 | -2.96288 | -1.06121 | -0.24954 | 0.0979853 | 0.370377 | 0.715509 | 1.12936 |
| tossup | total_drop_d1 | 1240 | 1.01216 | 0.292995 | 0.41241 | 0.640062 | 0.808982 | 0.960825 | 1.14934 | 1.52664 | 2.63737 |
| tossup | total_drop_d2 | 1240 | 0.910387 | 0.243505 | 0.37754 | 0.592295 | 0.751693 | 0.859531 | 1.02193 | 1.39995 | 1.98945 |
| tossup | total_drop_d3 | 1240 | 1.01152 | 0.340932 | 0.443457 | 0.645828 | 0.790322 | 0.908405 | 1.15749 | 1.66869 | 3.60648 |
| tossup | drop_share_1_d1 | 1240 | 0.219668 | 0.0795103 | 0.0480732 | 0.114678 | 0.161801 | 0.210462 | 0.264804 | 0.366256 | 0.642275 |
| tossup | drop_share_2_d1 | 1240 | 0.255288 | 0.0654904 | 0.0869989 | 0.145308 | 0.211604 | 0.261346 | 0.301895 | 0.349409 | 0.536703 |
| tossup | drop_share_3_d1 | 1240 | 0.525044 | 0.126823 | 0.158424 | 0.334499 | 0.431344 | 0.515315 | 0.616297 | 0.729511 | 0.856844 |
| tossup | drop_share_1_d2 | 1240 | 0.221297 | 0.0675182 | 0.0661212 | 0.122599 | 0.172877 | 0.218315 | 0.261623 | 0.332673 | 0.622347 |
| tossup | drop_share_2_d2 | 1240 | 0.261172 | 0.0640395 | 0.0538203 | 0.143147 | 0.216871 | 0.268998 | 0.309756 | 0.348504 | 0.491871 |
| tossup | drop_share_3_d2 | 1240 | 0.517532 | 0.114171 | 0.177096 | 0.357308 | 0.430974 | 0.505419 | 0.598401 | 0.721733 | 0.874961 |
| tossup | drop_share_1_d3 | 1240 | 0.236721 | 0.0599811 | 0.077339 | 0.130781 | 0.197195 | 0.243251 | 0.279753 | 0.318153 | 0.53782 |
| tossup | drop_share_2_d3 | 1240 | 0.287333 | 0.0523396 | 0.102033 | 0.180393 | 0.260151 | 0.298882 | 0.323607 | 0.349966 | 0.462094 |
| tossup | drop_share_3_d3 | 1240 | 0.475946 | 0.10177 | 0.176083 | 0.350521 | 0.399683 | 0.456322 | 0.530738 | 0.678028 | 0.820628 |
| tossup | r_1 | 1240 | 0.379592 | 0.178989 | 0.0292083 | 0.0963682 | 0.23282 | 0.386633 | 0.515639 | 0.668839 | 0.871891 |
| tossup | r_2 | 1240 | 0.373494 | 0.175387 | 0.0349428 | 0.0922058 | 0.246754 | 0.369182 | 0.486076 | 0.695204 | 0.925526 |
| tossup | r_3 | 1240 | 0.246915 | 0.13527 | 0.0326432 | 0.0717663 | 0.137347 | 0.222954 | 0.340573 | 0.50764 | 0.672139 |
| tossup | r_norm | 1240 | 0.650131 | 0.0540062 | 0.577356 | 0.583494 | 0.60943 | 0.640602 | 0.677738 | 0.753939 | 0.927046 |
