# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/terminal-cell-intercepts/off/degree_3/curves_3/dirichlet_2/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/terminal-cell-intercepts/off/degree_3/curves_3/dirichlet_2/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 305824 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.71083 |
| log_loss | 0.505064 |
| ece | 0.0650813 |
| brier | 0.165056 |
| accuracy | 0.769123 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00387305 |
| probability_std | 0.165526 |
| probability_p10 | 0.464448 |
| probability_p50 | 0.727856 |
| probability_p90 | 0.89504 |
| mean_predictive_variance | 0.182534 |
| integrated_brier_score | 0.108224 |
| joint_tossup_event_log_loss | 6.75648 |
| buzz_position_mae | 0.180273 |
| buzz_position_median_absolute_error | 0.160656 |
| buzz_position_bias | -0.0980988 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.343303 |
| first_buzzer_mean_reciprocal_rank | 0.557551 |
| first_buzzer_log_loss | 1.68872 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.71083 |
| neg_average_precision | 0.443013 |
| neg_precision | 0.515126 |
| neg_recall | 0.280935 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0939205 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0809122 |
| no_buzz_calibration_error | 0.0676426 |
| no_buzz_brier | 0.0246731 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.71083 | 0.505064 | 0.0650813 | 0.165056 | 0.769123 | 0.76525 | 0.00387305 | 0.165526 | 0.464448 | 0.727856 | 0.89504 | 0.182534 |
| tossup_correctness | tier | fall | 2933 | 0.698184 | 0.485795 | 0.070622 | 0.156721 | 0.784521 | 0.791681 | -0.0071599 | 0.164378 | 0.486245 | 0.750666 | 0.912695 | 0.174113 |
| tossup_correctness | tier | nationals | 1584 | 0.695228 | 0.549322 | 0.0661985 | 0.18412 | 0.736111 | 0.724747 | 0.0113636 | 0.169966 | 0.414295 | 0.685704 | 0.859633 | 0.195929 |
| tossup_correctness | tier | regionals | 1886 | 0.706233 | 0.527847 | 0.0719302 | 0.175155 | 0.748144 | 0.746023 | 0.00212089 | 0.16207 | 0.453322 | 0.69415 | 0.873942 | 0.193346 |
| tossup_correctness | tier | winter | 2892 | 0.727194 | 0.485506 | 0.0569849 | 0.156482 | 0.78527 | 0.773167 | 0.0121024 | 0.159833 | 0.49694 | 0.74818 | 0.899373 | 0.176686 |
| tossup_correctness | category | Current Events | 124 | 0.700659 | 0.53224 | 0.121481 | 0.177074 | 0.741935 | 0.75 | -0.00806452 | 0.173969 | 0.429743 | 0.662945 | 0.896254 | 0.192896 |
| tossup_correctness | category | Fine Arts | 1103 | 0.714531 | 0.502939 | 0.0596052 | 0.162869 | 0.778785 | 0.759746 | 0.019039 | 0.168351 | 0.458592 | 0.747556 | 0.905746 | 0.175176 |
| tossup_correctness | category | Geography | 197 | 0.771911 | 0.540881 | 0.111985 | 0.177975 | 0.756345 | 0.670051 | 0.0862944 | 0.217228 | 0.269363 | 0.637265 | 0.850229 | 0.191539 |
| tossup_correctness | category | History | 1491 | 0.723897 | 0.481298 | 0.0807639 | 0.155669 | 0.788732 | 0.787391 | 0.00134138 | 0.160195 | 0.472521 | 0.730862 | 0.896877 | 0.181643 |
| tossup_correctness | category | Literature | 1472 | 0.726785 | 0.451677 | 0.0575856 | 0.143113 | 0.811141 | 0.804348 | 0.00679348 | 0.140977 | 0.544352 | 0.771811 | 0.908234 | 0.16861 |
| tossup_correctness | category | Mythology | 332 | 0.638053 | 0.493972 | 0.103262 | 0.156256 | 0.786145 | 0.813253 | -0.0271084 | 0.144736 | 0.516015 | 0.751245 | 0.893917 | 0.176888 |
| tossup_correctness | category | Other Academic | 69 | 0.683258 | 0.543063 | 0.15251 | 0.182055 | 0.681159 | 0.753623 | -0.0724638 | 0.13381 | 0.489559 | 0.689291 | 0.821475 | 0.203937 |
| tossup_correctness | category | Philosophy | 324 | 0.655836 | 0.494033 | 0.0849711 | 0.161771 | 0.780864 | 0.799383 | -0.0185185 | 0.155526 | 0.486785 | 0.737585 | 0.909037 | 0.178478 |
| tossup_correctness | category | Popular Culture | 102 | 0.480277 | 0.489084 | 0.130246 | 0.152143 | 0.803922 | 0.833333 | -0.0294118 | 0.107725 | 0.663621 | 0.793747 | 0.916734 | 0.153714 |
| tossup_correctness | category | Religion | 372 | 0.709035 | 0.552077 | 0.0555482 | 0.186932 | 0.72043 | 0.709677 | 0.0107527 | 0.160161 | 0.444549 | 0.665262 | 0.848692 | 0.199953 |
| tossup_correctness | category | Science | 1487 | 0.682247 | 0.534713 | 0.0708774 | 0.177384 | 0.741762 | 0.752522 | -0.0107599 | 0.174419 | 0.435976 | 0.717169 | 0.892397 | 0.184426 |
| tossup_correctness | category | Social Science | 336 | 0.74661 | 0.527844 | 0.0707191 | 0.174845 | 0.755952 | 0.702381 | 0.0535714 | 0.187252 | 0.371677 | 0.703877 | 0.871149 | 0.188023 |
| tossup_correctness | category | Unknown | 1886 | 0.706233 | 0.527847 | 0.0719302 | 0.175155 | 0.748144 | 0.746023 | 0.00212089 | 0.16207 | 0.453322 | 0.69415 | 0.873942 | 0.193346 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.716976 | 0.54286 | 0.121273 | 0.177492 | 0.746193 | 0.736041 | 0.0101523 | 0.174309 | 0.418977 | 0.659627 | 0.855012 | 0.198495 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.714549 | 0.531799 | 0.0595006 | 0.176991 | 0.735025 | 0.735025 | 0 | 0.177664 | 0.405056 | 0.703971 | 0.88935 | 0.187627 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.691298 | 0.512765 | 0.065231 | 0.167626 | 0.767659 | 0.769436 | -0.00177699 | 0.166597 | 0.468985 | 0.729889 | 0.901768 | 0.180346 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.707122 | 0.489107 | 0.0718231 | 0.158607 | 0.781926 | 0.78402 | -0.00209351 | 0.162806 | 0.475626 | 0.739821 | 0.902883 | 0.178412 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.725311 | 0.503266 | 0.0593176 | 0.164553 | 0.770694 | 0.756008 | 0.0146862 | 0.160795 | 0.470187 | 0.726123 | 0.884778 | 0.185396 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 4.35963 | 0.567157 | 2.58933 | 3.42757 | 3.96191 | 4.36344 | 4.76039 | 5.27574 | 5.88534 |
| player | theta_1 | 1186 | -1.26805 | 1.00577 | -3.60757 | -2.68421 | -2.00311 | -1.44554 | -0.686398 | 0.640494 | 2.62661 |
| player | theta_2 | 1186 | -1.01083 | 0.726641 | -3.49064 | -2.20713 | -1.44741 | -1.0197 | -0.541349 | 0.184388 | 1.69618 |
| player | theta_3 | 1186 | -1.08344 | 0.738525 | -3.01618 | -2.21497 | -1.5927 | -1.15743 | -0.588271 | 0.224937 | 1.6694 |
| player | theta_norm | 1186 | 2.33277 | 0.66735 | 0.267621 | 1.20671 | 1.86799 | 2.33626 | 2.79303 | 3.37025 | 4.37266 |
| tossup | start_difficulty_d1 | 1240 | -0.755 | 0.659836 | -3.63197 | -2.03476 | -1.07691 | -0.695192 | -0.35952 | 0.211073 | 1.71895 |
| tossup | start_difficulty_d2 | 1240 | -0.624662 | 0.531379 | -3.24325 | -1.57239 | -0.831592 | -0.57642 | -0.345711 | 0.134105 | 1.10441 |
| tossup | start_difficulty_d3 | 1240 | -0.630671 | 0.532517 | -3.06245 | -1.56051 | -0.828422 | -0.573874 | -0.358884 | 0.129279 | 1.25378 |
| tossup | end_difficulty_d1 | 1240 | -1.92254 | 0.862333 | -5.59672 | -3.65736 | -2.30549 | -1.80678 | -1.40883 | -0.675339 | 0.847754 |
| tossup | end_difficulty_d2 | 1240 | -1.74797 | 0.67124 | -5.02976 | -2.89544 | -2.01893 | -1.68365 | -1.39747 | -0.798418 | 0.391485 |
| tossup | end_difficulty_d3 | 1240 | -1.75731 | 0.667177 | -4.8878 | -2.9721 | -2.00683 | -1.68456 | -1.42229 | -0.837062 | 0.509418 |
| tossup | total_drop_d1 | 1240 | 1.16754 | 0.257778 | 0.713399 | 0.891393 | 1.02499 | 1.11522 | 1.24236 | 1.60454 | 3.04068 |
| tossup | total_drop_d2 | 1240 | 1.1233 | 0.170746 | 0.710351 | 0.910837 | 1.03207 | 1.10152 | 1.17953 | 1.4093 | 2.78749 |
| tossup | total_drop_d3 | 1240 | 1.12664 | 0.172011 | 0.740104 | 0.920926 | 1.03686 | 1.10553 | 1.18144 | 1.39771 | 2.7859 |
| tossup | drop_share_1_d1 | 1240 | 0.317348 | 0.0214317 | 0.23301 | 0.287764 | 0.304864 | 0.315102 | 0.327131 | 0.356819 | 0.425334 |
| tossup | drop_share_2_d1 | 1240 | 0.349523 | 0.0123236 | 0.308395 | 0.329916 | 0.341324 | 0.348707 | 0.357177 | 0.370918 | 0.403088 |
| tossup | drop_share_3_d1 | 1240 | 0.33313 | 0.0212433 | 0.244123 | 0.292942 | 0.322714 | 0.33515 | 0.346714 | 0.363802 | 0.406383 |
| tossup | drop_share_1_d2 | 1240 | 0.314428 | 0.0176713 | 0.254071 | 0.289863 | 0.303978 | 0.312639 | 0.323243 | 0.341672 | 0.412928 |
| tossup | drop_share_2_d2 | 1240 | 0.34847 | 0.0115806 | 0.309868 | 0.329095 | 0.340417 | 0.348856 | 0.355953 | 0.366782 | 0.389006 |
| tossup | drop_share_3_d2 | 1240 | 0.337101 | 0.0172679 | 0.242377 | 0.311316 | 0.328231 | 0.337931 | 0.347473 | 0.361975 | 0.397068 |
| tossup | drop_share_1_d3 | 1240 | 0.314721 | 0.0171871 | 0.257301 | 0.290592 | 0.303225 | 0.314065 | 0.323926 | 0.342638 | 0.394334 |
| tossup | drop_share_2_d3 | 1240 | 0.348479 | 0.0116971 | 0.308966 | 0.329549 | 0.340659 | 0.348281 | 0.356462 | 0.367537 | 0.387804 |
| tossup | drop_share_3_d3 | 1240 | 0.336801 | 0.0173497 | 0.237868 | 0.309108 | 0.327092 | 0.337921 | 0.348077 | 0.361908 | 0.394644 |
| tossup | r_1 | 1240 | 0.377291 | 0.20302 | 0.039693 | 0.0871975 | 0.211256 | 0.35114 | 0.53099 | 0.750238 | 0.86548 |
| tossup | r_2 | 1240 | 0.30834 | 0.167012 | 0.0563884 | 0.10599 | 0.185035 | 0.275221 | 0.398055 | 0.646688 | 0.905061 |
| tossup | r_3 | 1240 | 0.314369 | 0.181414 | 0.0452299 | 0.100407 | 0.169613 | 0.269217 | 0.41434 | 0.693204 | 0.903919 |
| tossup | r_norm | 1240 | 0.657973 | 0.0725601 | 0.577362 | 0.582373 | 0.601714 | 0.635396 | 0.694125 | 0.815541 | 0.907553 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.75911 | 0.972039 | 0.231156 | 0.530882 | 0.925313 | 1.54366 | 2.55332 | 3.4448 | 4.37634 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.4848 | 0.81836 | 0.326292 | 0.504385 | 0.829743 | 1.28164 | 1.96192 | 3.09161 | 4.63572 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.50043 | 0.81496 | 0.232408 | 0.468688 | 0.84263 | 1.32884 | 2.05865 | 3.04444 | 4.2319 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.626791 | 1.53647 | -10.3704 | -3.63777 | -1.26671 | -0.162672 | 0.301544 | 0.942848 | 1.96714 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.443273 | 1.31952 | -9.90055 | -3.1252 | -0.472428 | -0.128272 | 0.222395 | 0.650624 | 1.34901 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.54555 | 1.41252 | -10.0362 | -3.31587 | -0.560974 | -0.166428 | 0.170851 | 0.714991 | 1.5619 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.38591 | 2.18933 | 0.792525 | 0.945831 | 1.00283 | 1.08845 | 4.02891 | 6.89113 | 12.6639 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.92807 | 1.87041 | 0.848622 | 0.946718 | 0.992512 | 1.05892 | 1.73148 | 6.16222 | 13.0996 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.04598 | 1.9423 | 0.84088 | 0.949887 | 0.998083 | 1.06735 | 2.07131 | 6.23567 | 12.8986 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.220026 | 0.084807 | 0.0334399 | 0.0630222 | 0.139106 | 0.262509 | 0.284845 | 0.302808 | 0.389893 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.325997 | 0.0859514 | 0.0577217 | 0.131614 | 0.330174 | 0.347544 | 0.359655 | 0.415641 | 0.76847 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.453978 | 0.149896 | 0.104156 | 0.339878 | 0.360206 | 0.382837 | 0.482735 | 0.795911 | 0.903677 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.237155 | 0.0760626 | 0.0289053 | 0.0705921 | 0.200913 | 0.272188 | 0.291647 | 0.306391 | 0.350229 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.333947 | 0.0670842 | 0.0406479 | 0.159594 | 0.335572 | 0.347638 | 0.359096 | 0.387796 | 0.672151 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.428898 | 0.12631 | 0.245949 | 0.340422 | 0.356552 | 0.374422 | 0.431918 | 0.763832 | 0.930447 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.234781 | 0.0769082 | 0.0376719 | 0.0708767 | 0.195769 | 0.267765 | 0.290514 | 0.306236 | 0.528354 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.339896 | 0.0691434 | 0.0638459 | 0.186019 | 0.336385 | 0.348414 | 0.360332 | 0.417487 | 0.720458 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.425323 | 0.122758 | 0.143491 | 0.338825 | 0.358187 | 0.374688 | 0.427931 | 0.730101 | 0.89265 |
| tossup_hazard | hazard_r_1 | 1240 | 0.378011 | 0.316894 | 0.0250878 | 0.0400657 | 0.0926209 | 0.243426 | 0.677049 | 0.922827 | 0.961183 |
| tossup_hazard | hazard_r_2 | 1240 | 0.301688 | 0.270669 | 0.017662 | 0.0323804 | 0.0669354 | 0.1944 | 0.508424 | 0.816777 | 0.924013 |
| tossup_hazard | hazard_r_3 | 1240 | 0.320301 | 0.279824 | 0.0132994 | 0.0280086 | 0.0760097 | 0.20721 | 0.554273 | 0.845166 | 0.943071 |
