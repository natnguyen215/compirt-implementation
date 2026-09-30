# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299799 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.607153 |
| log_loss | 0.633846 |
| ece | 0.199908 |
| brier | 0.221247 |
| accuracy | 0.653039 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.112211 |
| probability_std | 0.147883 |
| probability_p10 | 0.355818 |
| probability_p50 | 0.582117 |
| probability_p90 | 0.745891 |
| mean_predictive_variance | 0.223861 |
| integrated_brier_score | 0.0942424 |
| joint_tossup_event_log_loss | 6.64241 |
| buzz_position_mae | 0.136366 |
| buzz_position_median_absolute_error | 0.111625 |
| buzz_position_bias | 0.00448255 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.398924 |
| first_buzzer_mean_reciprocal_rank | 0.602392 |
| first_buzzer_log_loss | 1.59517 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.607153 |
| neg_average_precision | 0.31516 |
| neg_precision | 0.319613 |
| neg_recall | 0.423465 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.138782 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.047259 |
| no_buzz_calibration_error | 0.0339894 |
| no_buzz_brier | 0.0193613 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.607153 | 0.633846 | 0.199908 | 0.221247 | 0.653039 | 0.76525 | -0.112211 | 0.147883 | 0.355818 | 0.582117 | 0.745891 | 0.223861 |
| tossup_correctness | tier | fall | 2933 | 0.620011 | 0.636276 | 0.236652 | 0.222436 | 0.648483 | 0.791681 | -0.143198 | 0.151458 | 0.340988 | 0.570188 | 0.741592 | 0.224032 |
| tossup_correctness | tier | nationals | 1584 | 0.580293 | 0.628381 | 0.126629 | 0.218816 | 0.664773 | 0.724747 | -0.0599747 | 0.14126 | 0.40918 | 0.613578 | 0.767828 | 0.220399 |
| tossup_correctness | tier | regionals | 1886 | 0.623963 | 0.634498 | 0.183926 | 0.221349 | 0.649523 | 0.746023 | -0.0965005 | 0.150925 | 0.352568 | 0.57998 | 0.750861 | 0.223365 |
| tossup_correctness | tier | winter | 2892 | 0.614102 | 0.633949 | 0.213319 | 0.221305 | 0.653527 | 0.773167 | -0.11964 | 0.143191 | 0.358168 | 0.576228 | 0.734539 | 0.225907 |
| tossup_correctness | category | Current Events | 124 | 0.591398 | 0.690699 | 0.240626 | 0.24632 | 0.604839 | 0.75 | -0.145161 | 0.156285 | 0.318011 | 0.52353 | 0.728449 | 0.224952 |
| tossup_correctness | category | Fine Arts | 1103 | 0.617886 | 0.620777 | 0.181991 | 0.215227 | 0.671804 | 0.759746 | -0.087942 | 0.148276 | 0.352677 | 0.598805 | 0.753198 | 0.221968 |
| tossup_correctness | category | Geography | 197 | 0.529487 | 0.714892 | 0.175077 | 0.259519 | 0.532995 | 0.670051 | -0.137056 | 0.145231 | 0.31342 | 0.514946 | 0.689853 | 0.228817 |
| tossup_correctness | category | History | 1491 | 0.626891 | 0.622606 | 0.226046 | 0.216072 | 0.669349 | 0.787391 | -0.118042 | 0.138065 | 0.367591 | 0.580472 | 0.724893 | 0.22716 |
| tossup_correctness | category | Literature | 1472 | 0.59475 | 0.586983 | 0.187743 | 0.199779 | 0.70856 | 0.804348 | -0.095788 | 0.148989 | 0.398235 | 0.642917 | 0.787777 | 0.214206 |
| tossup_correctness | category | Mythology | 332 | 0.555018 | 0.653253 | 0.261594 | 0.229975 | 0.653614 | 0.813253 | -0.159639 | 0.142618 | 0.345429 | 0.57337 | 0.720241 | 0.226776 |
| tossup_correctness | category | Other Academic | 69 | 0.61991 | 0.630911 | 0.22183 | 0.219401 | 0.681159 | 0.753623 | -0.0724638 | 0.140311 | 0.342317 | 0.57348 | 0.705584 | 0.227541 |
| tossup_correctness | category | Philosophy | 324 | 0.550639 | 0.606413 | 0.197295 | 0.209118 | 0.645062 | 0.799383 | -0.154321 | 0.133996 | 0.428272 | 0.625946 | 0.758486 | 0.221377 |
| tossup_correctness | category | Popular Culture | 102 | 0.483045 | 0.785987 | 0.361091 | 0.292471 | 0.45098 | 0.833333 | -0.382353 | 0.151864 | 0.272967 | 0.479987 | 0.659832 | 0.226167 |
| tossup_correctness | category | Religion | 372 | 0.585543 | 0.659238 | 0.156128 | 0.233389 | 0.615591 | 0.709677 | -0.094086 | 0.139795 | 0.357352 | 0.565697 | 0.731462 | 0.22759 |
| tossup_correctness | category | Science | 1487 | 0.599218 | 0.663919 | 0.217704 | 0.235017 | 0.618695 | 0.752522 | -0.133826 | 0.139963 | 0.341631 | 0.548038 | 0.704422 | 0.229198 |
| tossup_correctness | category | Social Science | 336 | 0.602839 | 0.660258 | 0.173444 | 0.233196 | 0.639881 | 0.702381 | -0.0625 | 0.145307 | 0.333238 | 0.553799 | 0.714337 | 0.227519 |
| tossup_correctness | category | Unknown | 1886 | 0.623963 | 0.634498 | 0.183926 | 0.221349 | 0.649523 | 0.746023 | -0.0965005 | 0.150925 | 0.352568 | 0.57998 | 0.750861 | 0.223365 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.637666 | 0.682059 | 0.230705 | 0.24247 | 0.629442 | 0.736041 | -0.106599 | 0.145428 | 0.315197 | 0.510344 | 0.691228 | 0.228822 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.609333 | 0.675937 | 0.216224 | 0.240867 | 0.601015 | 0.735025 | -0.13401 | 0.145863 | 0.318447 | 0.533133 | 0.69934 | 0.22835 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.599061 | 0.643841 | 0.213807 | 0.225814 | 0.639271 | 0.769436 | -0.130164 | 0.144957 | 0.352897 | 0.570739 | 0.734542 | 0.225865 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.616111 | 0.623607 | 0.214196 | 0.21661 | 0.662596 | 0.78402 | -0.121424 | 0.148745 | 0.357754 | 0.58736 | 0.752418 | 0.222999 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.599867 | 0.619123 | 0.168776 | 0.214405 | 0.672897 | 0.756008 | -0.0831108 | 0.144957 | 0.373228 | 0.608234 | 0.761103 | 0.221378 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | 0.239652 | 0.909452 | -1.98641 | -1.07055 | -0.479552 | 0.162306 | 0.892763 | 1.83796 | 3.09152 |
| player | theta_2 | 1186 | 0.473812 | 0.962624 | -1.85802 | -0.917835 | -0.274216 | 0.396165 | 1.1439 | 2.17133 | 3.44626 |
| player | theta_3 | 1186 | 0.199268 | 0.795313 | -2.07339 | -0.945765 | -0.409209 | 0.149081 | 0.710896 | 1.61808 | 2.57126 |
| player | alpha_1 | 1186 | 7.82743 | 4.13568 | 0.56014 | 2.26177 | 4.94288 | 7.21766 | 9.9865 | 15.413 | 31.5304 |
| player | alpha_2 | 1186 | 10.306 | 4.90895 | 1.58911 | 4.79355 | 7.10949 | 9.29734 | 12.3538 | 18.8511 | 43.3673 |
| player | alpha_3 | 1186 | 6.6486 | 4.26461 | 0.788191 | 1.66049 | 3.74155 | 5.78768 | 8.4631 | 14.3734 | 38.3224 |
| player | beta_1 | 1186 | -1.64204 | 0.612619 | -3.88893 | -2.71273 | -2.02891 | -1.5698 | -1.20379 | -0.725869 | 0.0584714 |
| player | beta_2 | 1186 | -1.59762 | 0.580629 | -4.22698 | -2.60546 | -1.96964 | -1.57048 | -1.19862 | -0.697535 | -0.0534466 |
| player | beta_3 | 1186 | -1.4608 | 0.58456 | -4.1732 | -2.53439 | -1.82358 | -1.39143 | -1.06102 | -0.622548 | 0.0311621 |
| player | theta_norm | 1186 | 1.49213 | 0.692719 | 0.177154 | 0.520033 | 0.971299 | 1.38943 | 1.97602 | 2.76676 | 3.8445 |
| tossup | start_difficulty_d1 | 1240 | 1.09733 | 0.318428 | -0.339479 | 0.534143 | 0.917178 | 1.11591 | 1.30953 | 1.56489 | 2.03566 |
| tossup | start_difficulty_d2 | 1240 | 1.23937 | 0.293111 | -0.386129 | 0.776437 | 1.07923 | 1.22921 | 1.42007 | 1.71178 | 2.21269 |
| tossup | start_difficulty_d3 | 1240 | 1.06078 | 0.361991 | -0.482556 | 0.367871 | 0.867899 | 1.1041 | 1.29509 | 1.58913 | 2.11298 |
| tossup | end_difficulty_d1 | 1240 | 0.0611877 | 0.410359 | -1.78801 | -0.754748 | -0.119695 | 0.125255 | 0.321551 | 0.617319 | 1.12317 |
| tossup | end_difficulty_d2 | 1240 | 0.327669 | 0.350327 | -1.33257 | -0.268768 | 0.157669 | 0.331296 | 0.521873 | 0.893189 | 1.55563 |
| tossup | end_difficulty_d3 | 1240 | 0.0903136 | 0.489402 | -2.38926 | -0.852922 | -0.148394 | 0.173446 | 0.414121 | 0.752664 | 1.25955 |
| tossup | total_drop_d1 | 1240 | 1.03614 | 0.307632 | 0.391618 | 0.647922 | 0.825844 | 0.976494 | 1.18686 | 1.63547 | 2.69634 |
| tossup | total_drop_d2 | 1240 | 0.911699 | 0.242893 | 0.362229 | 0.593446 | 0.749139 | 0.864488 | 1.04058 | 1.38135 | 2.08662 |
| tossup | total_drop_d3 | 1240 | 0.970468 | 0.294068 | 0.45213 | 0.636653 | 0.772716 | 0.895654 | 1.09261 | 1.56579 | 2.8466 |
| tossup | drop_share_1_d1 | 1240 | 0.220746 | 0.0735394 | 0.0475868 | 0.115204 | 0.165092 | 0.213312 | 0.271603 | 0.338347 | 0.519146 |
| tossup | drop_share_2_d1 | 1240 | 0.260971 | 0.0656212 | 0.0719064 | 0.147199 | 0.216431 | 0.268339 | 0.310927 | 0.351644 | 0.579524 |
| tossup | drop_share_3_d1 | 1240 | 0.518282 | 0.124719 | 0.159899 | 0.338737 | 0.420887 | 0.505228 | 0.612714 | 0.731181 | 0.880507 |
| tossup | drop_share_1_d2 | 1240 | 0.220227 | 0.0673524 | 0.0719488 | 0.125707 | 0.171774 | 0.215913 | 0.257441 | 0.334172 | 0.598642 |
| tossup | drop_share_2_d2 | 1240 | 0.260356 | 0.0653985 | 0.0642216 | 0.144213 | 0.215815 | 0.266785 | 0.309402 | 0.349426 | 0.496063 |
| tossup | drop_share_3_d2 | 1240 | 0.519416 | 0.114751 | 0.163865 | 0.356346 | 0.435608 | 0.508319 | 0.602982 | 0.715092 | 0.861295 |
| tossup | drop_share_1_d3 | 1240 | 0.235179 | 0.0582488 | 0.0714718 | 0.130231 | 0.197442 | 0.237259 | 0.276331 | 0.316786 | 0.540178 |
| tossup | drop_share_2_d3 | 1240 | 0.285152 | 0.0523702 | 0.0929158 | 0.182938 | 0.253854 | 0.295855 | 0.322327 | 0.348484 | 0.447667 |
| tossup | drop_share_3_d3 | 1240 | 0.479669 | 0.100041 | 0.241303 | 0.358489 | 0.403041 | 0.460832 | 0.536061 | 0.671481 | 0.835612 |
| tossup | r_1 | 1240 | 0.347273 | 0.179897 | 0.029697 | 0.0812568 | 0.191188 | 0.348826 | 0.476402 | 0.658296 | 0.807509 |
| tossup | r_2 | 1240 | 0.389795 | 0.179164 | 0.0414747 | 0.09849 | 0.266495 | 0.385236 | 0.498421 | 0.724239 | 0.909761 |
| tossup | r_3 | 1240 | 0.262932 | 0.143809 | 0.0366439 | 0.0779838 | 0.146665 | 0.238021 | 0.358401 | 0.52591 | 0.704058 |
| tossup | r_norm | 1240 | 0.650774 | 0.0569392 | 0.577634 | 0.584424 | 0.607758 | 0.640512 | 0.674959 | 0.764285 | 0.912015 |
