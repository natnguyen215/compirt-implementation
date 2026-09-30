# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 302097 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.716571 |
| log_loss | 0.503987 |
| ece | 0.0688554 |
| brier | 0.164678 |
| accuracy | 0.76958 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00540132 |
| probability_std | 0.163248 |
| probability_p10 | 0.462495 |
| probability_p50 | 0.72212 |
| probability_p90 | 0.88793 |
| mean_predictive_variance | 0.184995 |
| integrated_brier_score | 0.111083 |
| joint_tossup_event_log_loss | 6.73722 |
| buzz_position_mae | 0.166672 |
| buzz_position_median_absolute_error | 0.14987 |
| buzz_position_bias | -0.0763337 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.337366 |
| first_buzzer_mean_reciprocal_rank | 0.553538 |
| first_buzzer_log_loss | 1.69545 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.716571 |
| neg_average_precision | 0.454191 |
| neg_precision | 0.520358 |
| neg_recall | 0.292716 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.178157 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0112522 |
| no_buzz_calibration_error | -0.00186081 |
| no_buzz_brier | 0.0125598 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.716571 | 0.503987 | 0.0688554 | 0.164678 | 0.76958 | 0.764178 | 0.00540132 | 0.163248 | 0.462495 | 0.72212 | 0.88793 | 0.184995 |
| tossup_correctness | tier | fall | 2798 | 0.734859 | 0.472954 | 0.0670626 | 0.151164 | 0.793424 | 0.785204 | 0.00822016 | 0.16223 | 0.483726 | 0.747193 | 0.909017 | 0.175609 |
| tossup_correctness | tier | nationals | 1545 | 0.715007 | 0.545513 | 0.0725559 | 0.182789 | 0.731392 | 0.721036 | 0.010356 | 0.15998 | 0.41648 | 0.667742 | 0.843828 | 0.202113 |
| tossup_correctness | tier | regionals | 2039 | 0.70965 | 0.514148 | 0.0872814 | 0.169245 | 0.758215 | 0.762138 | -0.00392349 | 0.15928 | 0.449439 | 0.694901 | 0.871641 | 0.192552 |
| tossup_correctness | tier | winter | 2875 | 0.697528 | 0.504666 | 0.060283 | 0.164857 | 0.774957 | 0.768348 | 0.0066087 | 0.162336 | 0.482657 | 0.741157 | 0.893264 | 0.179572 |
| tossup_correctness | category | Current Events | 129 | 0.704164 | 0.568902 | 0.0853696 | 0.195238 | 0.697674 | 0.666667 | 0.0310078 | 0.172764 | 0.429934 | 0.651469 | 0.901903 | 0.189321 |
| tossup_correctness | category | Fine Arts | 1074 | 0.708608 | 0.500769 | 0.0866583 | 0.163175 | 0.787709 | 0.776536 | 0.0111732 | 0.17146 | 0.438274 | 0.719228 | 0.884476 | 0.184479 |
| tossup_correctness | category | Geography | 180 | 0.775428 | 0.535278 | 0.0581709 | 0.180185 | 0.733333 | 0.616667 | 0.116667 | 0.222975 | 0.225734 | 0.678585 | 0.850664 | 0.187387 |
| tossup_correctness | category | History | 1454 | 0.703295 | 0.514034 | 0.0610506 | 0.169055 | 0.753095 | 0.757909 | -0.00481431 | 0.163367 | 0.459763 | 0.724662 | 0.894739 | 0.183059 |
| tossup_correctness | category | Literature | 1435 | 0.727084 | 0.451704 | 0.0750658 | 0.14132 | 0.816725 | 0.810453 | 0.00627178 | 0.148052 | 0.523786 | 0.772376 | 0.904843 | 0.170698 |
| tossup_correctness | category | Mythology | 324 | 0.68134 | 0.486845 | 0.0586672 | 0.156121 | 0.790123 | 0.79321 | -0.00308642 | 0.148323 | 0.532286 | 0.766015 | 0.906415 | 0.172489 |
| tossup_correctness | category | Other Academic | 71 | 0.62963 | 0.562554 | 0.103385 | 0.186603 | 0.732394 | 0.760563 | -0.028169 | 0.125441 | 0.537318 | 0.690236 | 0.816949 | 0.201838 |
| tossup_correctness | category | Philosophy | 310 | 0.736372 | 0.496446 | 0.0681785 | 0.163111 | 0.777419 | 0.76129 | 0.016129 | 0.149196 | 0.477471 | 0.721484 | 0.875436 | 0.188386 |
| tossup_correctness | category | Popular Culture | 108 | 0.506076 | 0.423894 | 0.172598 | 0.123772 | 0.87037 | 0.888889 | -0.0185185 | 0.104803 | 0.643676 | 0.786653 | 0.908224 | 0.163793 |
| tossup_correctness | category | Religion | 361 | 0.712045 | 0.54208 | 0.097621 | 0.181496 | 0.731302 | 0.742382 | -0.0110803 | 0.152805 | 0.438732 | 0.656706 | 0.835138 | 0.205403 |
| tossup_correctness | category | Science | 1445 | 0.722877 | 0.513556 | 0.0526602 | 0.169418 | 0.754325 | 0.746021 | 0.0083045 | 0.16179 | 0.468333 | 0.720136 | 0.887352 | 0.186103 |
| tossup_correctness | category | Social Science | 327 | 0.715264 | 0.546652 | 0.0814345 | 0.182783 | 0.752294 | 0.718654 | 0.0336391 | 0.179318 | 0.393612 | 0.684444 | 0.866324 | 0.192992 |
| tossup_correctness | category | Unknown | 2039 | 0.70965 | 0.514148 | 0.0872814 | 0.169245 | 0.758215 | 0.762138 | -0.00392349 | 0.15928 | 0.449439 | 0.694901 | 0.871641 | 0.192552 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.68664 | 0.55659 | 0.114924 | 0.187809 | 0.715847 | 0.743169 | -0.0273224 | 0.177862 | 0.375709 | 0.650971 | 0.873252 | 0.200505 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.718668 | 0.531467 | 0.0605833 | 0.176168 | 0.744503 | 0.728796 | 0.0157068 | 0.173511 | 0.420441 | 0.693293 | 0.881561 | 0.190101 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.726157 | 0.503368 | 0.0577605 | 0.165478 | 0.767307 | 0.752568 | 0.0147387 | 0.167702 | 0.460414 | 0.722064 | 0.893724 | 0.183811 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.705041 | 0.488792 | 0.071607 | 0.158152 | 0.786435 | 0.786087 | 0.000347826 | 0.156006 | 0.493262 | 0.742442 | 0.894702 | 0.179564 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.71831 | 0.507049 | 0.0789457 | 0.165264 | 0.766389 | 0.764393 | 0.00199667 | 0.159917 | 0.461583 | 0.714507 | 0.87921 | 0.188507 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 4.38986 | 0.545998 | 2.57585 | 3.47493 | 4.02051 | 4.40125 | 4.75501 | 5.27111 | 5.88448 |
| player | theta_1 | 1197 | -1.20265 | 0.868074 | -3.94873 | -2.47706 | -1.83314 | -1.30447 | -0.613042 | 0.328569 | 2.14044 |
| player | theta_2 | 1197 | -1.0766 | 0.763091 | -3.01426 | -2.18844 | -1.60144 | -1.17443 | -0.615 | 0.324565 | 1.84102 |
| player | theta_3 | 1197 | -1.08376 | 0.71621 | -3.19187 | -2.23722 | -1.55396 | -1.14364 | -0.614184 | 0.151998 | 1.35472 |
| player | theta_norm | 1197 | 2.27175 | 0.68322 | 0.309666 | 1.06834 | 1.8177 | 2.27452 | 2.75804 | 3.33322 | 4.56075 |
| tossup | start_difficulty_d1 | 1240 | -0.772124 | 0.657328 | -3.53109 | -2.08547 | -1.08723 | -0.688614 | -0.377032 | 0.185667 | 1.04073 |
| tossup | start_difficulty_d2 | 1240 | -0.635933 | 0.502428 | -3.05561 | -1.53181 | -0.843301 | -0.611849 | -0.376138 | 0.110678 | 1.21124 |
| tossup | start_difficulty_d3 | 1240 | -0.654187 | 0.540025 | -3.09988 | -1.70024 | -0.867855 | -0.621826 | -0.365559 | 0.132192 | 1.15243 |
| tossup | end_difficulty_d1 | 1240 | -1.94251 | 0.840027 | -4.98719 | -3.59838 | -2.33336 | -1.83317 | -1.44038 | -0.74937 | 0.21543 |
| tossup | end_difficulty_d2 | 1240 | -1.76747 | 0.646702 | -5.511 | -2.85851 | -2.02377 | -1.71829 | -1.43834 | -0.839772 | 0.341045 |
| tossup | end_difficulty_d3 | 1240 | -1.79177 | 0.689763 | -5.19317 | -3.08825 | -2.06239 | -1.73435 | -1.41547 | -0.826318 | 0.410987 |
| tossup | total_drop_d1 | 1240 | 1.17039 | 0.238884 | 0.707074 | 0.904315 | 1.03729 | 1.12658 | 1.24193 | 1.57368 | 3.89189 |
| tossup | total_drop_d2 | 1240 | 1.13154 | 0.184693 | 0.784592 | 0.922668 | 1.03198 | 1.10311 | 1.18842 | 1.40012 | 3.32849 |
| tossup | total_drop_d3 | 1240 | 1.13758 | 0.183144 | 0.739647 | 0.924348 | 1.03233 | 1.11133 | 1.19556 | 1.45215 | 2.52792 |
| tossup | drop_share_1_d1 | 1240 | 0.31707 | 0.0212963 | 0.230372 | 0.288259 | 0.304272 | 0.314819 | 0.326509 | 0.359716 | 0.432165 |
| tossup | drop_share_2_d1 | 1240 | 0.349494 | 0.0125398 | 0.310964 | 0.329575 | 0.341861 | 0.349368 | 0.356956 | 0.369056 | 0.45811 |
| tossup | drop_share_3_d1 | 1240 | 0.333437 | 0.0207226 | 0.249758 | 0.294364 | 0.323169 | 0.335792 | 0.347084 | 0.360796 | 0.434603 |
| tossup | drop_share_1_d2 | 1240 | 0.31386 | 0.0169497 | 0.250333 | 0.289119 | 0.30309 | 0.313016 | 0.323088 | 0.340996 | 0.402711 |
| tossup | drop_share_2_d2 | 1240 | 0.349179 | 0.0117913 | 0.304692 | 0.32963 | 0.342096 | 0.349199 | 0.356236 | 0.369128 | 0.419389 |
| tossup | drop_share_3_d2 | 1240 | 0.336961 | 0.0174901 | 0.244987 | 0.309619 | 0.32727 | 0.33741 | 0.347633 | 0.363607 | 0.401105 |
| tossup | drop_share_1_d3 | 1240 | 0.315458 | 0.0185203 | 0.261253 | 0.288398 | 0.303882 | 0.313902 | 0.324286 | 0.34536 | 0.427318 |
| tossup | drop_share_2_d3 | 1240 | 0.348528 | 0.0115229 | 0.30614 | 0.329818 | 0.340472 | 0.34846 | 0.356147 | 0.367502 | 0.391431 |
| tossup | drop_share_3_d3 | 1240 | 0.336014 | 0.0180116 | 0.238764 | 0.306532 | 0.326457 | 0.337386 | 0.347115 | 0.362176 | 0.395303 |
| tossup | r_1 | 1240 | 0.35811 | 0.185892 | 0.0446354 | 0.104283 | 0.220349 | 0.325673 | 0.471739 | 0.737032 | 0.866405 |
| tossup | r_2 | 1240 | 0.314921 | 0.171957 | 0.0502368 | 0.0941963 | 0.182879 | 0.285627 | 0.404652 | 0.676984 | 0.874647 |
| tossup | r_3 | 1240 | 0.326968 | 0.172944 | 0.0585336 | 0.100733 | 0.197656 | 0.297904 | 0.424199 | 0.659332 | 0.900911 |
| tossup | r_norm | 1240 | 0.650284 | 0.0736285 | 0.57738 | 0.580263 | 0.594823 | 0.621928 | 0.680998 | 0.816666 | 0.903632 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.758 | 0.813351 | 0.259446 | 0.69726 | 1.11703 | 1.55958 | 2.39184 | 3.26335 | 4.20838 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.55776 | 0.755666 | 0.304828 | 0.563737 | 0.944183 | 1.40515 | 2.06577 | 2.95282 | 4.13075 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.59031 | 0.815697 | 0.305264 | 0.588431 | 0.945035 | 1.38359 | 2.09403 | 3.22423 | 4.11436 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.336339 | 1.3796 | -8.73291 | -3.48051 | -0.429281 | 0.0607933 | 0.398279 | 1.01045 | 2.12472 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.288398 | 1.30746 | -13.7288 | -2.75743 | -0.363247 | -0.00592759 | 0.31833 | 0.832379 | 1.80871 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.280914 | 1.38208 | -9.45748 | -3.17354 | -0.343541 | 0.0160587 | 0.3773 | 0.936616 | 2.31743 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.09434 | 1.88392 | 0.786977 | 0.948721 | 1.00955 | 1.10321 | 2.29925 | 6.21767 | 12.045 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.84616 | 1.75705 | 0.727426 | 0.950072 | 1.00139 | 1.07515 | 1.62105 | 5.71356 | 16.5916 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.87122 | 1.8524 | 0.728302 | 0.946328 | 1.0051 | 1.06504 | 1.54178 | 6.02814 | 12.4322 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.228067 | 0.0757431 | 0.041867 | 0.0754939 | 0.179435 | 0.260451 | 0.284036 | 0.304815 | 0.383942 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.346738 | 0.0749619 | 0.0778974 | 0.194017 | 0.337829 | 0.350371 | 0.364445 | 0.454755 | 0.74604 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.425196 | 0.121512 | 0.0827212 | 0.33261 | 0.359034 | 0.37913 | 0.441058 | 0.725242 | 0.880236 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.239503 | 0.0705343 | 0.0262975 | 0.0769956 | 0.210384 | 0.268629 | 0.289483 | 0.306317 | 0.44813 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.34523 | 0.0621369 | 0.0634761 | 0.219156 | 0.339078 | 0.350315 | 0.363008 | 0.417017 | 0.708124 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.415266 | 0.111036 | 0.132943 | 0.33535 | 0.355818 | 0.374665 | 0.420288 | 0.681507 | 0.892133 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.24041 | 0.071203 | 0.03605 | 0.0766292 | 0.215963 | 0.2691 | 0.289156 | 0.306564 | 0.454449 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348143 | 0.0613293 | 0.0613138 | 0.229563 | 0.340489 | 0.350728 | 0.363631 | 0.42762 | 0.654253 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.411447 | 0.106868 | 0.198735 | 0.334898 | 0.356745 | 0.374531 | 0.415343 | 0.680058 | 0.89684 |
| tossup_hazard | hazard_r_1 | 1240 | 0.369523 | 0.298268 | 0.0235563 | 0.0487728 | 0.101647 | 0.246533 | 0.658548 | 0.881723 | 0.945658 |
| tossup_hazard | hazard_r_2 | 1240 | 0.318625 | 0.274956 | 0.01525 | 0.0337191 | 0.0834702 | 0.208147 | 0.524765 | 0.861618 | 0.950776 |
| tossup_hazard | hazard_r_3 | 1240 | 0.311852 | 0.268165 | 0.0191619 | 0.037719 | 0.0845343 | 0.20789 | 0.506756 | 0.838449 | 0.931773 |
