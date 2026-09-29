# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 302242 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.603269 |
| log_loss | 0.78927 |
| ece | 0.344049 |
| brier | 0.295362 |
| accuracy | 0.371935 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.392244 |
| probability_std | 0.0973596 |
| probability_p10 | 0.293939 |
| probability_p50 | 0.42174 |
| probability_p90 | 0.544244 |
| mean_predictive_variance | 0.234142 |
| integrated_brier_score | 0.0955014 |
| joint_tossup_event_log_loss | 6.7806 |
| buzz_position_mae | 0.139242 |
| buzz_position_median_absolute_error | 0.115755 |
| buzz_position_bias | -0.00521591 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.383169 |
| first_buzzer_mean_reciprocal_rank | 0.592995 |
| first_buzzer_log_loss | 1.60134 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.603269 |
| neg_average_precision | 0.321043 |
| neg_precision | 0.254762 |
| neg_recall | 0.863949 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.129382 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0510545 |
| no_buzz_calibration_error | 0.0379415 |
| no_buzz_brier | 0.0197651 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.603269 | 0.78927 | 0.344049 | 0.295362 | 0.371935 | 0.764178 | -0.392244 | 0.0973596 | 0.293939 | 0.42174 | 0.544244 | 0.234142 |
| tossup_correctness | tier | fall | 2798 | 0.622021 | 0.793939 | 0.366697 | 0.29795 | 0.350965 | 0.785204 | -0.434239 | 0.0927646 | 0.295276 | 0.421474 | 0.537682 | 0.234754 |
| tossup_correctness | tier | nationals | 1545 | 0.576122 | 0.779753 | 0.299993 | 0.290459 | 0.399353 | 0.721036 | -0.321683 | 0.100621 | 0.287349 | 0.423269 | 0.554225 | 0.233641 |
| tossup_correctness | tier | regionals | 2039 | 0.60889 | 0.77422 | 0.33116 | 0.287865 | 0.41589 | 0.762138 | -0.346248 | 0.108887 | 0.290739 | 0.430118 | 0.574087 | 0.23338 |
| tossup_correctness | tier | winter | 2875 | 0.602077 | 0.800514 | 0.355182 | 0.300796 | 0.346435 | 0.768348 | -0.421913 | 0.0903646 | 0.296449 | 0.416586 | 0.527948 | 0.234356 |
| tossup_correctness | category | Current Events | 129 | 0.583829 | 0.7739 | 0.270243 | 0.288317 | 0.387597 | 0.666667 | -0.27907 | 0.0951157 | 0.284497 | 0.404513 | 0.516147 | 0.231836 |
| tossup_correctness | category | Fine Arts | 1074 | 0.574745 | 0.823954 | 0.371257 | 0.311567 | 0.327747 | 0.776536 | -0.44879 | 0.0988015 | 0.279444 | 0.406362 | 0.537601 | 0.231447 |
| tossup_correctness | category | Geography | 180 | 0.512861 | 0.771872 | 0.220135 | 0.287059 | 0.416667 | 0.616667 | -0.2 | 0.0851545 | 0.301137 | 0.402174 | 0.499797 | 0.233081 |
| tossup_correctness | category | History | 1454 | 0.61986 | 0.777689 | 0.335523 | 0.290168 | 0.363824 | 0.757909 | -0.394085 | 0.0903805 | 0.304139 | 0.426141 | 0.535484 | 0.235808 |
| tossup_correctness | category | Literature | 1435 | 0.560537 | 0.802788 | 0.380791 | 0.301486 | 0.342857 | 0.810453 | -0.467596 | 0.095579 | 0.306526 | 0.437687 | 0.548479 | 0.235917 |
| tossup_correctness | category | Mythology | 324 | 0.608804 | 0.823266 | 0.390351 | 0.312151 | 0.320988 | 0.79321 | -0.472222 | 0.0853042 | 0.294269 | 0.397328 | 0.51475 | 0.233287 |
| tossup_correctness | category | Other Academic | 71 | 0.546841 | 0.816627 | 0.353338 | 0.308975 | 0.352113 | 0.760563 | -0.408451 | 0.0959405 | 0.287708 | 0.392704 | 0.545233 | 0.232188 |
| tossup_correctness | category | Philosophy | 310 | 0.648133 | 0.795306 | 0.355102 | 0.298536 | 0.341935 | 0.76129 | -0.419355 | 0.093121 | 0.291085 | 0.412291 | 0.532449 | 0.232528 |
| tossup_correctness | category | Popular Culture | 108 | 0.550347 | 0.925693 | 0.506385 | 0.35943 | 0.175926 | 0.888889 | -0.712963 | 0.0812424 | 0.286804 | 0.373058 | 0.491609 | 0.229594 |
| tossup_correctness | category | Religion | 361 | 0.63148 | 0.794553 | 0.338196 | 0.297963 | 0.373961 | 0.742382 | -0.368421 | 0.0923642 | 0.276742 | 0.404322 | 0.526647 | 0.232289 |
| tossup_correctness | category | Science | 1445 | 0.631083 | 0.772215 | 0.324722 | 0.287543 | 0.393772 | 0.746021 | -0.352249 | 0.0913713 | 0.302552 | 0.423269 | 0.534843 | 0.235457 |
| tossup_correctness | category | Social Science | 327 | 0.635291 | 0.756141 | 0.300154 | 0.280385 | 0.425076 | 0.718654 | -0.293578 | 0.0954467 | 0.293025 | 0.429347 | 0.539043 | 0.234578 |
| tossup_correctness | category | Unknown | 2039 | 0.60889 | 0.77422 | 0.33116 | 0.287865 | 0.41589 | 0.762138 | -0.346248 | 0.108887 | 0.290739 | 0.430118 | 0.574087 | 0.23338 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.681633 | 0.962235 | 0.440742 | 0.370955 | 0.284153 | 0.743169 | -0.459016 | 0.0938481 | 0.185365 | 0.298829 | 0.426263 | 0.202157 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.630403 | 0.882442 | 0.38341 | 0.337404 | 0.305759 | 0.728796 | -0.423037 | 0.0888526 | 0.239681 | 0.339784 | 0.464922 | 0.2182 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.631761 | 0.825148 | 0.365157 | 0.312204 | 0.330058 | 0.752568 | -0.42251 | 0.0917266 | 0.274804 | 0.383497 | 0.505578 | 0.22891 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.603031 | 0.789535 | 0.361753 | 0.296165 | 0.34887 | 0.786087 | -0.437217 | 0.087457 | 0.313948 | 0.422106 | 0.537071 | 0.236626 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.585897 | 0.722141 | 0.292985 | 0.264081 | 0.451581 | 0.764393 | -0.312812 | 0.0806513 | 0.372292 | 0.468871 | 0.575948 | 0.242678 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | 5.07653 | 1.55627 | 1.97473 | 3.49327 | 4.14509 | 4.7523 | 5.51692 | 7.87469 | 13.4071 |
| player | beta | 1197 | -2.90276 | 0.824711 | -6.27597 | -4.37307 | -3.41267 | -2.78723 | -2.33013 | -1.71372 | -0.927486 |
| player | theta_1 | 1197 | -1.57443 | 0.536489 | -3.49929 | -2.45223 | -1.92462 | -1.58342 | -1.22223 | -0.705078 | 0.0240433 |
| player | theta_2 | 1197 | -1.57479 | 0.593324 | -3.89545 | -2.49832 | -1.99025 | -1.5971 | -1.19641 | -0.557686 | 0.636032 |
| player | theta_3 | 1197 | -1.58262 | 0.588957 | -3.22712 | -2.50771 | -2.0004 | -1.60211 | -1.19559 | -0.592829 | 0.81311 |
| player | theta_norm | 1197 | 2.85569 | 0.542817 | 0.556775 | 1.90267 | 2.49744 | 2.89763 | 3.247 | 3.66876 | 4.33929 |
| tossup | start_difficulty_d1 | 1240 | 0.148032 | 0.318626 | -0.927506 | -0.405224 | -0.0595622 | 0.171265 | 0.360064 | 0.656242 | 1.27937 |
| tossup | start_difficulty_d2 | 1240 | 0.175008 | 0.308928 | -0.940044 | -0.339769 | -0.0409377 | 0.187177 | 0.389823 | 0.642265 | 1.04242 |
| tossup | start_difficulty_d3 | 1240 | 0.175821 | 0.306765 | -0.883455 | -0.319563 | -0.0325719 | 0.170864 | 0.382856 | 0.680413 | 1.12984 |
| tossup | end_difficulty_d1 | 1240 | -1.32571 | 0.589717 | -4.03366 | -2.2381 | -1.70397 | -1.36326 | -0.861181 | -0.413324 | 0.125765 |
| tossup | end_difficulty_d2 | 1240 | -1.20323 | 0.543218 | -3.46199 | -2.0282 | -1.591 | -1.22615 | -0.779777 | -0.382848 | 0.184489 |
| tossup | end_difficulty_d3 | 1240 | -1.19897 | 0.547217 | -3.27633 | -2.07225 | -1.58366 | -1.19965 | -0.780225 | -0.337509 | 0.148697 |
| tossup | total_drop_d1 | 1240 | 1.47374 | 0.547005 | 0.493494 | 0.882032 | 1.01078 | 1.35698 | 1.78724 | 2.51577 | 5.14447 |
| tossup | total_drop_d2 | 1240 | 1.37824 | 0.487225 | 0.541493 | 0.869764 | 0.972526 | 1.24294 | 1.66103 | 2.34587 | 3.71627 |
| tossup | total_drop_d3 | 1240 | 1.37479 | 0.494535 | 0.751197 | 0.871415 | 0.958022 | 1.21069 | 1.68074 | 2.36308 | 3.30882 |
| tossup | drop_share_1_d1 | 1240 | 0.26166 | 0.0905818 | 0.0408777 | 0.135505 | 0.207763 | 0.259116 | 0.293334 | 0.458015 | 0.738213 |
| tossup | drop_share_2_d1 | 1240 | 0.278423 | 0.0621663 | 0.085982 | 0.159023 | 0.238859 | 0.292695 | 0.325786 | 0.353312 | 0.484163 |
| tossup | drop_share_3_d1 | 1240 | 0.459917 | 0.118953 | 0.0597097 | 0.295993 | 0.38201 | 0.431794 | 0.53038 | 0.687753 | 0.84477 |
| tossup | drop_share_1_d2 | 1240 | 0.256545 | 0.0760149 | 0.0531681 | 0.139023 | 0.216598 | 0.25868 | 0.289674 | 0.381989 | 0.703452 |
| tossup | drop_share_2_d2 | 1240 | 0.281626 | 0.0661399 | 0.0701747 | 0.146326 | 0.245784 | 0.300995 | 0.329644 | 0.354511 | 0.545728 |
| tossup | drop_share_3_d2 | 1240 | 0.461829 | 0.11467 | 0.0813621 | 0.320929 | 0.382739 | 0.434247 | 0.526394 | 0.692995 | 0.860289 |
| tossup | drop_share_1_d3 | 1240 | 0.254738 | 0.0764447 | 0.081453 | 0.135286 | 0.209371 | 0.260861 | 0.288784 | 0.357613 | 0.715143 |
| tossup | drop_share_2_d3 | 1240 | 0.284486 | 0.0620556 | 0.0732293 | 0.157811 | 0.247056 | 0.303015 | 0.329128 | 0.351794 | 0.528145 |
| tossup | drop_share_3_d3 | 1240 | 0.460775 | 0.112992 | 0.111923 | 0.333947 | 0.383603 | 0.429516 | 0.523693 | 0.681172 | 0.844218 |
| tossup | r_1 | 1240 | 0.355064 | 0.19485 | 0.027852 | 0.0976172 | 0.192889 | 0.320058 | 0.503219 | 0.698862 | 0.848164 |
| tossup | r_2 | 1240 | 0.330063 | 0.191501 | 0.0307614 | 0.0955971 | 0.180888 | 0.279723 | 0.456115 | 0.694674 | 0.902365 |
| tossup | r_3 | 1240 | 0.314874 | 0.178893 | 0.02817 | 0.0922665 | 0.177152 | 0.266982 | 0.429858 | 0.660023 | 0.819369 |
| tossup | r_norm | 1240 | 0.661123 | 0.060261 | 0.57736 | 0.584054 | 0.611473 | 0.650023 | 0.701852 | 0.769337 | 0.905473 |
