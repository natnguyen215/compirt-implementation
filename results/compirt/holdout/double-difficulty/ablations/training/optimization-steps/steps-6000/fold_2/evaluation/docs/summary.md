# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-6000/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-6000/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 6000 |
| pyramidal | final_loss | 278004 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.712137 |
| log_loss | 0.492209 |
| ece | 0.0108435 |
| brier | 0.159937 |
| accuracy | 0.774333 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0101545 |
| probability_std | 0.145929 |
| probability_p10 | 0.570384 |
| probability_p50 | 0.808235 |
| probability_p90 | 0.9194 |
| mean_predictive_variance | 0.155168 |
| integrated_brier_score | 0.0976811 |
| joint_tossup_event_log_loss | 6.51699 |
| buzz_position_mae | 0.144253 |
| buzz_position_median_absolute_error | 0.124853 |
| buzz_position_bias | -0.0234385 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.364265 |
| first_buzzer_mean_reciprocal_rank | 0.576904 |
| first_buzzer_log_loss | 1.63857 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.712137 |
| neg_average_precision | 0.449958 |
| neg_precision | 0.585455 |
| neg_recall | 0.147503 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.184448 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0102631 |
| no_buzz_calibration_error | -0.00284987 |
| no_buzz_brier | 0.0127642 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.712137 | 0.492209 | 0.0108435 | 0.159937 | 0.774333 | 0.764178 | 0.0101545 | 0.145929 | 0.570384 | 0.808235 | 0.9194 | 0.155168 |
| tossup_correctness | tier | fall | 2798 | 0.735716 | 0.458598 | 0.0149222 | 0.146737 | 0.794853 | 0.785204 | 0.00964975 | 0.144921 | 0.571826 | 0.815601 | 0.921688 | 0.152564 |
| tossup_correctness | tier | nationals | 1545 | 0.713684 | 0.53536 | 0.0417094 | 0.177899 | 0.743689 | 0.721036 | 0.0226537 | 0.154175 | 0.546329 | 0.796327 | 0.915595 | 0.159632 |
| tossup_correctness | tier | regionals | 2039 | 0.700601 | 0.499911 | 0.0194549 | 0.162652 | 0.770476 | 0.762138 | 0.00833742 | 0.141757 | 0.568724 | 0.800867 | 0.921096 | 0.157354 |
| tossup_correctness | tier | winter | 2875 | 0.695145 | 0.496268 | 0.0187172 | 0.161205 | 0.773565 | 0.768348 | 0.00521739 | 0.144809 | 0.58585 | 0.810373 | 0.917923 | 0.153753 |
| tossup_correctness | category | Current Events | 129 | 0.683072 | 0.61066 | 0.116987 | 0.208988 | 0.682171 | 0.666667 | 0.0155039 | 0.158759 | 0.516905 | 0.793563 | 0.925819 | 0.161856 |
| tossup_correctness | category | Fine Arts | 1074 | 0.716057 | 0.474061 | 0.0359678 | 0.152118 | 0.793296 | 0.776536 | 0.0167598 | 0.156992 | 0.557196 | 0.797984 | 0.916478 | 0.158226 |
| tossup_correctness | category | Geography | 180 | 0.756887 | 0.565035 | 0.0921079 | 0.191196 | 0.722222 | 0.616667 | 0.105556 | 0.23445 | 0.246371 | 0.772753 | 0.909256 | 0.161223 |
| tossup_correctness | category | History | 1454 | 0.689722 | 0.512374 | 0.0227862 | 0.167524 | 0.763411 | 0.757909 | 0.00550206 | 0.145521 | 0.562079 | 0.810811 | 0.923445 | 0.154504 |
| tossup_correctness | category | Literature | 1435 | 0.725981 | 0.432945 | 0.0159465 | 0.135459 | 0.818815 | 0.810453 | 0.00836237 | 0.124955 | 0.631435 | 0.840481 | 0.929195 | 0.139895 |
| tossup_correctness | category | Mythology | 324 | 0.702073 | 0.469611 | 0.0433767 | 0.150551 | 0.777778 | 0.79321 | -0.0154321 | 0.113747 | 0.664558 | 0.836133 | 0.919204 | 0.143815 |
| tossup_correctness | category | Other Academic | 71 | 0.62963 | 0.541317 | 0.114596 | 0.175815 | 0.760563 | 0.760563 | 0 | 0.113401 | 0.605637 | 0.801845 | 0.908428 | 0.160709 |
| tossup_correctness | category | Philosophy | 310 | 0.723431 | 0.489635 | 0.019133 | 0.160151 | 0.774194 | 0.76129 | 0.0129032 | 0.122598 | 0.605071 | 0.803055 | 0.916447 | 0.158654 |
| tossup_correctness | category | Popular Culture | 108 | 0.524306 | 0.373568 | 0.0847612 | 0.107398 | 0.87963 | 0.888889 | -0.00925926 | 0.0795958 | 0.732562 | 0.84628 | 0.914829 | 0.133106 |
| tossup_correctness | category | Religion | 361 | 0.681753 | 0.531193 | 0.0423371 | 0.176091 | 0.736842 | 0.742382 | -0.00554017 | 0.145042 | 0.512032 | 0.761266 | 0.897058 | 0.174432 |
| tossup_correctness | category | Science | 1445 | 0.716295 | 0.509889 | 0.0333157 | 0.168363 | 0.757785 | 0.746021 | 0.0117647 | 0.142913 | 0.571633 | 0.79796 | 0.911081 | 0.16008 |
| tossup_correctness | category | Social Science | 327 | 0.746577 | 0.519566 | 0.0445975 | 0.173734 | 0.733945 | 0.718654 | 0.0152905 | 0.177575 | 0.459488 | 0.774991 | 0.913155 | 0.166546 |
| tossup_correctness | category | Unknown | 2039 | 0.700601 | 0.499911 | 0.0194549 | 0.162652 | 0.770476 | 0.762138 | 0.00833742 | 0.141757 | 0.568724 | 0.800867 | 0.921096 | 0.157354 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.66724 | 0.538856 | 0.10883 | 0.18075 | 0.715847 | 0.743169 | -0.0273224 | 0.152316 | 0.496343 | 0.768386 | 0.902378 | 0.172186 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.720049 | 0.52362 | 0.0266116 | 0.173065 | 0.748691 | 0.728796 | 0.0198953 | 0.151914 | 0.533276 | 0.79003 | 0.908893 | 0.164018 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.724007 | 0.496147 | 0.0201833 | 0.161892 | 0.771326 | 0.752568 | 0.0187584 | 0.146078 | 0.575508 | 0.809193 | 0.917511 | 0.154392 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.70519 | 0.472421 | 0.0130377 | 0.15205 | 0.789565 | 0.786087 | 0.00347826 | 0.133228 | 0.612343 | 0.823866 | 0.923757 | 0.148335 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.707039 | 0.495382 | 0.0208771 | 0.160585 | 0.77371 | 0.764393 | 0.0093178 | 0.152731 | 0.544806 | 0.799716 | 0.919826 | 0.158435 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 1.90677 | 0.764657 | -0.286424 | 0.656747 | 1.39933 | 1.88169 | 2.41567 | 3.22391 | 3.96892 |
| player | theta_1 | 1197 | -0.804178 | 0.899855 | -3.01457 | -2.13968 | -1.39846 | -0.867658 | -0.303335 | 0.799651 | 2.8856 |
| player | theta_2 | 1197 | -0.6663 | 0.797328 | -3.27971 | -1.91408 | -1.19476 | -0.694948 | -0.168254 | 0.623921 | 1.92966 |
| player | theta_3 | 1197 | -0.735288 | 0.858736 | -3.09076 | -2.02443 | -1.30139 | -0.837602 | -0.241731 | 0.88771 | 2.84776 |
| player | theta_norm | 1197 | 1.85005 | 0.624506 | 0.237956 | 0.88062 | 1.39904 | 1.81005 | 2.26682 | 2.88525 | 4.2481 |
| tossup | start_difficulty_d1 | 1240 | -1.35324 | 0.538752 | -2.9871 | -2.11663 | -1.70328 | -1.40985 | -1.05588 | -0.433815 | 1.48435 |
| tossup | start_difficulty_d2 | 1240 | -1.35713 | 0.485835 | -2.80662 | -2.06966 | -1.67124 | -1.38762 | -1.06866 | -0.573849 | 1.47707 |
| tossup | start_difficulty_d3 | 1240 | -1.3616 | 0.495713 | -3.09599 | -2.12669 | -1.6867 | -1.36929 | -1.06282 | -0.540013 | 0.787363 |
| tossup | end_difficulty_d1 | 1240 | -2.34569 | 0.628918 | -4.4299 | -3.24319 | -2.76114 | -2.40564 | -1.9868 | -1.25913 | 0.772873 |
| tossup | end_difficulty_d2 | 1240 | -2.34891 | 0.569813 | -4.05212 | -3.19876 | -2.72056 | -2.38315 | -2.01072 | -1.43168 | 0.809504 |
| tossup | end_difficulty_d3 | 1240 | -2.3548 | 0.580689 | -4.40932 | -3.2668 | -2.73449 | -2.35877 | -1.98171 | -1.3905 | 0.107854 |
| tossup | total_drop_d1 | 1240 | 0.992458 | 0.112228 | 0.578019 | 0.805615 | 0.924162 | 0.99067 | 1.06469 | 1.16658 | 1.50046 |
| tossup | total_drop_d2 | 1240 | 0.99178 | 0.100948 | 0.601695 | 0.82481 | 0.925551 | 0.993536 | 1.0594 | 1.15158 | 1.38282 |
| tossup | total_drop_d3 | 1240 | 0.993196 | 0.103446 | 0.642059 | 0.824308 | 0.922047 | 0.992426 | 1.05967 | 1.1679 | 1.37819 |
| tossup | drop_share_1_d1 | 1240 | 0.303451 | 0.0154566 | 0.22636 | 0.279401 | 0.294115 | 0.303856 | 0.313289 | 0.327631 | 0.35609 |
| tossup | drop_share_2_d1 | 1240 | 0.347373 | 0.011413 | 0.311824 | 0.32897 | 0.340085 | 0.347077 | 0.354519 | 0.365993 | 0.39767 |
| tossup | drop_share_3_d1 | 1240 | 0.349176 | 0.016468 | 0.287619 | 0.324106 | 0.338342 | 0.348397 | 0.3581 | 0.376439 | 0.433536 |
| tossup | drop_share_1_d2 | 1240 | 0.30441 | 0.0139542 | 0.245588 | 0.281441 | 0.295775 | 0.30495 | 0.313181 | 0.326864 | 0.352115 |
| tossup | drop_share_2_d2 | 1240 | 0.347032 | 0.0111471 | 0.306681 | 0.328821 | 0.339636 | 0.34719 | 0.353909 | 0.365197 | 0.383714 |
| tossup | drop_share_3_d2 | 1240 | 0.348558 | 0.0151755 | 0.298234 | 0.325072 | 0.338207 | 0.347737 | 0.358027 | 0.374327 | 0.408259 |
| tossup | drop_share_1_d3 | 1240 | 0.303569 | 0.0145188 | 0.247263 | 0.280614 | 0.293983 | 0.303529 | 0.313135 | 0.326934 | 0.352349 |
| tossup | drop_share_2_d3 | 1240 | 0.34724 | 0.0110229 | 0.314341 | 0.32996 | 0.339184 | 0.347082 | 0.354402 | 0.365925 | 0.383972 |
| tossup | drop_share_3_d3 | 1240 | 0.349191 | 0.0150998 | 0.290907 | 0.325543 | 0.339082 | 0.348558 | 0.358752 | 0.372944 | 0.41883 |
| tossup | r_1 | 1240 | 0.323977 | 0.16734 | 0.0470205 | 0.109903 | 0.196727 | 0.284385 | 0.427739 | 0.656319 | 0.863571 |
| tossup | r_2 | 1240 | 0.33343 | 0.154748 | 0.0573257 | 0.123721 | 0.215818 | 0.309292 | 0.431117 | 0.626729 | 0.850218 |
| tossup | r_3 | 1240 | 0.342593 | 0.158682 | 0.0642564 | 0.125804 | 0.219848 | 0.318919 | 0.43622 | 0.652222 | 0.849236 |
| tossup | r_norm | 1240 | 0.638324 | 0.0558418 | 0.577398 | 0.580808 | 0.597131 | 0.621583 | 0.662664 | 0.754276 | 0.868961 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 6.15411 | 0.517975 | 4.06397 | 5.31378 | 5.93083 | 6.11283 | 6.36802 | 7.11402 | 8.24245 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 6.19109 | 0.496008 | 3.49739 | 5.49061 | 5.99034 | 6.12909 | 6.34391 | 7.12129 | 8.67079 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 6.18311 | 0.494378 | 3.00609 | 5.40528 | 5.99791 | 6.14073 | 6.35497 | 7.14453 | 8.3195 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 2.85578 | 3.1319 | -13.6244 | -3.6261 | 0.812823 | 4.76023 | 5.08655 | 5.35888 | 5.99662 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 3.6595 | 2.81628 | -11.7547 | -2.37552 | 3.41016 | 4.99413 | 5.16684 | 5.47629 | 6.35315 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 3.48672 | 2.936 | -14.9182 | -2.54336 | 2.41149 | 4.99416 | 5.17727 | 5.48309 | 6.41923 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.29833 | 3.25599 | 0.855949 | 0.961754 | 1.019 | 1.12102 | 5.52471 | 10.0461 | 19.8214 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.53159 | 2.9541 | 0.885158 | 0.948026 | 0.99707 | 1.04421 | 2.15419 | 8.92483 | 18.4055 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.69639 | 3.05212 | 0.815191 | 0.944905 | 0.9976 | 1.04677 | 3.907 | 8.7652 | 20.9893 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.246918 | 0.0894623 | 0.047879 | 0.0847645 | 0.171279 | 0.288239 | 0.302804 | 0.322727 | 0.675422 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.336476 | 0.0860947 | 0.0631385 | 0.162492 | 0.330538 | 0.347347 | 0.360279 | 0.468451 | 0.707239 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.416606 | 0.14125 | 0.0864798 | 0.268156 | 0.343878 | 0.359311 | 0.449295 | 0.745316 | 0.882512 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.260627 | 0.0803731 | 0.0293914 | 0.0909598 | 0.252087 | 0.291294 | 0.304817 | 0.320492 | 0.693038 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.338163 | 0.0755413 | 0.0622885 | 0.173203 | 0.336166 | 0.34739 | 0.358001 | 0.416514 | 0.717846 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.40121 | 0.127922 | 0.0921577 | 0.304605 | 0.343649 | 0.357325 | 0.381032 | 0.721278 | 0.908106 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.259968 | 0.0807353 | 0.0448831 | 0.0837108 | 0.249162 | 0.290813 | 0.304431 | 0.323713 | 0.654795 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.34007 | 0.0705973 | 0.0810102 | 0.174076 | 0.33645 | 0.349056 | 0.359755 | 0.441679 | 0.722846 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.399962 | 0.125757 | 0.0562078 | 0.309352 | 0.343709 | 0.357244 | 0.384375 | 0.721176 | 0.870268 |
| tossup_hazard | hazard_r_1 | 1240 | 0.373683 | 0.299565 | 0.0154803 | 0.0436058 | 0.0989823 | 0.256373 | 0.628341 | 0.891985 | 0.958717 |
| tossup_hazard | hazard_r_2 | 1240 | 0.302295 | 0.261228 | 0.0135888 | 0.0332623 | 0.0775971 | 0.200758 | 0.509654 | 0.811749 | 0.93751 |
| tossup_hazard | hazard_r_3 | 1240 | 0.324022 | 0.286584 | 0.0158775 | 0.0382302 | 0.0834615 | 0.201214 | 0.563174 | 0.872029 | 0.970931 |
