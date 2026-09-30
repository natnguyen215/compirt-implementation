# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/unconstrained/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/unconstrained/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335028 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.545424 |
| log_loss | 0.615055 |
| ece | 0.108624 |
| brier | 0.193064 |
| accuracy | 0.763314 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000864211 |
| probability_std | 0.0948454 |
| probability_p10 | 0.72865 |
| probability_p50 | 0.89229 |
| probability_p90 | 0.953417 |
| mean_predictive_variance | 0.108153 |
| integrated_brier_score | 0.175161 |
| joint_tossup_event_log_loss | 7.78683 |
| buzz_position_mae | 0.340536 |
| buzz_position_median_absolute_error | 0.342597 |
| buzz_position_bias | -0.327442 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.346873 |
| first_buzzer_mean_reciprocal_rank | 0.562584 |
| first_buzzer_log_loss | 1.67097 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.545424 |
| neg_average_precision | 0.273742 |
| neg_precision | 0.394737 |
| neg_recall | 0.00687128 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0290928 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.235952 |
| no_buzz_calibration_error | 0.222839 |
| no_buzz_brier | 0.0712042 |
| full_pmf_max_mass_error | 1.11022e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.545424 | 0.615055 | 0.108624 | 0.193064 | 0.763314 | 0.764178 | -0.000864211 | 0.0948454 | 0.72865 | 0.89229 | 0.953417 | 0.108153 |
| tossup_correctness | tier | fall | 2798 | 0.545188 | 0.562967 | 0.0907251 | 0.177044 | 0.783774 | 0.785204 | -0.00142959 | 0.0761143 | 0.768845 | 0.882579 | 0.943312 | 0.10945 |
| tossup_correctness | tier | nationals | 1545 | 0.571997 | 0.668369 | 0.120258 | 0.215796 | 0.721036 | 0.721036 | 0 | 0.115958 | 0.654777 | 0.874971 | 0.954613 | 0.122957 |
| tossup_correctness | tier | regionals | 2039 | 0.534267 | 0.626385 | 0.108137 | 0.19473 | 0.760667 | 0.762138 | -0.00147131 | 0.111222 | 0.670328 | 0.892441 | 0.956894 | 0.111872 |
| tossup_correctness | tier | winter | 2875 | 0.539181 | 0.629063 | 0.130091 | 0.195257 | 0.768 | 0.768348 | -0.000347826 | 0.0804836 | 0.770491 | 0.908308 | 0.95633 | 0.0962991 |
| tossup_correctness | category | Current Events | 129 | 0.590319 | 0.739918 | 0.184391 | 0.25068 | 0.674419 | 0.666667 | 0.00775194 | 0.0927918 | 0.708351 | 0.874909 | 0.923466 | 0.123516 |
| tossup_correctness | category | Fine Arts | 1074 | 0.541155 | 0.599313 | 0.111806 | 0.186708 | 0.774674 | 0.776536 | -0.0018622 | 0.0865358 | 0.752622 | 0.900067 | 0.952532 | 0.102353 |
| tossup_correctness | category | Geography | 180 | 0.575924 | 0.886569 | 0.251641 | 0.297346 | 0.611111 | 0.616667 | -0.00555556 | 0.0963246 | 0.704259 | 0.887267 | 0.946523 | 0.11198 |
| tossup_correctness | category | History | 1454 | 0.563665 | 0.609215 | 0.106231 | 0.194513 | 0.756534 | 0.757909 | -0.00137552 | 0.0930232 | 0.721154 | 0.883884 | 0.948267 | 0.113016 |
| tossup_correctness | category | Literature | 1435 | 0.521574 | 0.536885 | 0.0866011 | 0.162297 | 0.810453 | 0.810453 | 0 | 0.084613 | 0.757853 | 0.89768 | 0.957027 | 0.101793 |
| tossup_correctness | category | Mythology | 324 | 0.584122 | 0.550126 | 0.121847 | 0.171262 | 0.799383 | 0.79321 | 0.00617284 | 0.0938943 | 0.740585 | 0.908842 | 0.95208 | 0.0997126 |
| tossup_correctness | category | Other Academic | 71 | 0.381264 | 0.751556 | 0.202371 | 0.226241 | 0.760563 | 0.760563 | 0 | 0.107291 | 0.734771 | 0.913736 | 0.960995 | 0.0996251 |
| tossup_correctness | category | Philosophy | 310 | 0.485513 | 0.669519 | 0.157126 | 0.204716 | 0.76129 | 0.76129 | 0 | 0.083047 | 0.777069 | 0.909709 | 0.956428 | 0.0942979 |
| tossup_correctness | category | Popular Culture | 108 | 0.569444 | 0.354708 | 0.0675727 | 0.101574 | 0.87963 | 0.888889 | -0.00925926 | 0.0742662 | 0.784215 | 0.88793 | 0.94167 | 0.105748 |
| tossup_correctness | category | Religion | 361 | 0.538196 | 0.663633 | 0.153551 | 0.208494 | 0.736842 | 0.742382 | -0.00554017 | 0.0870699 | 0.756419 | 0.903022 | 0.949856 | 0.102247 |
| tossup_correctness | category | Science | 1445 | 0.551268 | 0.634085 | 0.118269 | 0.202986 | 0.746713 | 0.746021 | 0.000692042 | 0.0905048 | 0.727063 | 0.879936 | 0.947182 | 0.11451 |
| tossup_correctness | category | Social Science | 327 | 0.581776 | 0.697735 | 0.155577 | 0.224678 | 0.715596 | 0.718654 | -0.0030581 | 0.0867124 | 0.755018 | 0.895706 | 0.951335 | 0.104716 |
| tossup_correctness | category | Unknown | 2039 | 0.534267 | 0.626385 | 0.108137 | 0.19473 | 0.760667 | 0.762138 | -0.00147131 | 0.111222 | 0.670328 | 0.892441 | 0.956894 | 0.111872 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.47669 | 0.653657 | 0.112919 | 0.20975 | 0.737705 | 0.743169 | -0.00546448 | 0.0911299 | 0.704019 | 0.856821 | 0.931704 | 0.128412 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.533884 | 0.659868 | 0.13575 | 0.21639 | 0.727749 | 0.728796 | -0.00104712 | 0.0919875 | 0.722759 | 0.86662 | 0.934767 | 0.122453 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.539138 | 0.6255 | 0.111153 | 0.199709 | 0.750335 | 0.752568 | -0.00223314 | 0.0930158 | 0.724789 | 0.88026 | 0.94407 | 0.11522 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.547751 | 0.569549 | 0.0936318 | 0.176598 | 0.785739 | 0.786087 | -0.000347826 | 0.0933598 | 0.732185 | 0.896126 | 0.95273 | 0.10658 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.546842 | 0.634218 | 0.118639 | 0.195437 | 0.764393 | 0.764393 | 0 | 0.0966385 | 0.730955 | 0.911418 | 0.961097 | 0.0986153 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | -1.40153 | 0.677795 | -2.99066 | -2.33982 | -1.80383 | -1.46969 | -1.10679 | -0.204761 | 2.1604 |
| player | beta | 1197 | -3.22439 | 1.08382 | -6.79434 | -5.58697 | -3.72442 | -2.98284 | -2.41949 | -1.90918 | -1.64819 |
| player | theta_1 | 1197 | 0.901722 | 0.873127 | -2.35521 | -0.681383 | 0.357342 | 0.984578 | 1.54678 | 2.16785 | 3.07961 |
| player | theta_2 | 1197 | 0.883611 | 0.945216 | -2.23242 | -0.804684 | 0.257755 | 0.989388 | 1.56789 | 2.28319 | 3.23524 |
| player | theta_3 | 1197 | 0.878151 | 0.870986 | -2.4002 | -0.715655 | 0.331163 | 0.974376 | 1.51811 | 2.13162 | 2.99816 |
| player | theta_norm | 1197 | 2.08866 | 0.644386 | 0.314918 | 0.938619 | 1.66951 | 2.15892 | 2.54286 | 3.04928 | 4.32511 |
| tossup | start_difficulty_d1 | 1240 | -1.01289 | 0.45949 | -2.26963 | -1.84799 | -1.36263 | -0.959686 | -0.638812 | -0.364282 | -0.172697 |
| tossup | start_difficulty_d2 | 1240 | -0.989995 | 0.431582 | -1.99493 | -1.69815 | -1.35206 | -0.966611 | -0.625803 | -0.3419 | -0.165793 |
| tossup | start_difficulty_d3 | 1240 | -0.964534 | 0.420731 | -2.17225 | -1.7152 | -1.25994 | -0.927577 | -0.62472 | -0.358694 | -0.143413 |
| tossup | end_difficulty_d1 | 1240 | -1.6792 | 0.390522 | -3.13367 | -2.37274 | -1.93846 | -1.62446 | -1.37316 | -1.14116 | -0.953118 |
| tossup | end_difficulty_d2 | 1240 | -1.66266 | 0.368891 | -2.86067 | -2.25969 | -1.95092 | -1.65085 | -1.3599 | -1.12258 | -0.929277 |
| tossup | end_difficulty_d3 | 1240 | -1.64571 | 0.370364 | -2.98226 | -2.34455 | -1.85237 | -1.59952 | -1.37902 | -1.13128 | -0.92116 |
| tossup | total_drop_d1 | 1240 | 0.666308 | 0.197083 | 0.231744 | 0.302748 | 0.528997 | 0.707754 | 0.818625 | 0.926133 | 1.13947 |
| tossup | total_drop_d2 | 1240 | 0.672661 | 0.181285 | 0.237334 | 0.331914 | 0.551235 | 0.703182 | 0.808071 | 0.928262 | 1.13729 |
| tossup | total_drop_d3 | 1240 | 0.681174 | 0.174069 | 0.233938 | 0.366041 | 0.554238 | 0.705374 | 0.813752 | 0.930114 | 1.13173 |
| tossup | drop_share_1_d1 | 1240 | 0.326242 | 0.0288773 | 0.197275 | 0.286478 | 0.309336 | 0.32333 | 0.340061 | 0.378311 | 0.454091 |
| tossup | drop_share_2_d1 | 1240 | 0.322311 | 0.0180681 | 0.255006 | 0.286578 | 0.312331 | 0.325613 | 0.335607 | 0.346453 | 0.364434 |
| tossup | drop_share_3_d1 | 1240 | 0.351447 | 0.030525 | 0.245559 | 0.308847 | 0.333466 | 0.347892 | 0.365224 | 0.406098 | 0.533146 |
| tossup | drop_share_1_d2 | 1240 | 0.321576 | 0.0245183 | 0.221587 | 0.282116 | 0.30966 | 0.322342 | 0.334992 | 0.359815 | 0.433265 |
| tossup | drop_share_2_d2 | 1240 | 0.322797 | 0.0185826 | 0.249787 | 0.286897 | 0.312202 | 0.326633 | 0.335766 | 0.346922 | 0.367048 |
| tossup | drop_share_3_d2 | 1240 | 0.355627 | 0.0321575 | 0.261749 | 0.316995 | 0.335005 | 0.349194 | 0.368226 | 0.420182 | 0.50582 |
| tossup | drop_share_1_d3 | 1240 | 0.323276 | 0.0262025 | 0.196164 | 0.281116 | 0.309848 | 0.323062 | 0.337302 | 0.364891 | 0.42722 |
| tossup | drop_share_2_d3 | 1240 | 0.323728 | 0.0173381 | 0.255037 | 0.290498 | 0.313804 | 0.326783 | 0.336337 | 0.346493 | 0.366472 |
| tossup | drop_share_3_d3 | 1240 | 0.352996 | 0.0325095 | 0.241346 | 0.311226 | 0.33291 | 0.348069 | 0.365373 | 0.418195 | 0.523959 |
| tossup | r_1 | 1240 | 0.335595 | 0.238883 | 0.0419062 | 0.0770792 | 0.138785 | 0.249769 | 0.503306 | 0.822879 | 0.922741 |
| tossup | r_2 | 1240 | 0.342981 | 0.24649 | 0.0330874 | 0.0666741 | 0.132966 | 0.255819 | 0.551431 | 0.800366 | 0.91732 |
| tossup | r_3 | 1240 | 0.321424 | 0.226616 | 0.0345055 | 0.0631036 | 0.132597 | 0.246689 | 0.476295 | 0.773991 | 0.88991 |
| tossup | r_norm | 1240 | 0.703604 | 0.086956 | 0.577664 | 0.589026 | 0.629582 | 0.688029 | 0.771557 | 0.861905 | 0.924387 |
