# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 284815 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710917 |
| log_loss | 0.485753 |
| ece | 0.00585183 |
| brier | 0.157027 |
| accuracy | 0.7837 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0136564 |
| probability_std | 0.141996 |
| probability_p10 | 0.578993 |
| probability_p50 | 0.810067 |
| probability_p90 | 0.917762 |
| mean_predictive_variance | 0.154363 |
| integrated_brier_score | 0.100696 |
| joint_tossup_event_log_loss | 6.58558 |
| buzz_position_mae | 0.149771 |
| buzz_position_median_absolute_error | 0.133058 |
| buzz_position_bias | -0.0423669 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.350441 |
| first_buzzer_mean_reciprocal_rank | 0.56587 |
| first_buzzer_log_loss | 1.67579 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.710917 |
| neg_average_precision | 0.448768 |
| neg_precision | 0.626016 |
| neg_recall | 0.14751 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.191835 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0156471 |
| no_buzz_calibration_error | 0.000462706 |
| no_buzz_brier | 0.013796 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.710917 | 0.485753 | 0.00585183 | 0.157027 | 0.7837 | 0.770044 | 0.0136564 | 0.141996 | 0.578993 | 0.810067 | 0.917762 | 0.154363 |
| tossup_correctness | tier | fall | 2817 | 0.703875 | 0.477371 | 0.00880349 | 0.15305 | 0.790202 | 0.781683 | 0.0085197 | 0.141153 | 0.571439 | 0.819792 | 0.921682 | 0.151076 |
| tossup_correctness | tier | nationals | 1542 | 0.72528 | 0.515514 | 0.0337993 | 0.170696 | 0.754215 | 0.73476 | 0.0194553 | 0.144725 | 0.56026 | 0.79367 | 0.909718 | 0.161618 |
| tossup_correctness | tier | regionals | 1934 | 0.71771 | 0.497333 | 0.0191985 | 0.162206 | 0.772492 | 0.75698 | 0.0155119 | 0.137695 | 0.583543 | 0.805177 | 0.915793 | 0.156394 |
| tossup_correctness | tier | winter | 2787 | 0.699818 | 0.469725 | 0.0188586 | 0.14989 | 0.80122 | 0.786868 | 0.0143524 | 0.143629 | 0.590475 | 0.81414 | 0.918636 | 0.152262 |
| tossup_correctness | category | Current Events | 125 | 0.742629 | 0.532257 | 0.0636828 | 0.180174 | 0.712 | 0.704 | 0.008 | 0.146868 | 0.533409 | 0.781148 | 0.899493 | 0.169953 |
| tossup_correctness | category | Fine Arts | 1072 | 0.725999 | 0.474463 | 0.024999 | 0.152438 | 0.794776 | 0.770522 | 0.0242537 | 0.148003 | 0.565712 | 0.813958 | 0.917808 | 0.154076 |
| tossup_correctness | category | Geography | 185 | 0.77972 | 0.490882 | 0.0572429 | 0.160595 | 0.756757 | 0.702703 | 0.0540541 | 0.206889 | 0.397001 | 0.758819 | 0.895465 | 0.170143 |
| tossup_correctness | category | History | 1443 | 0.728734 | 0.485208 | 0.0281997 | 0.158772 | 0.775468 | 0.765073 | 0.010395 | 0.146957 | 0.551926 | 0.801631 | 0.916883 | 0.158036 |
| tossup_correctness | category | Literature | 1411 | 0.65837 | 0.459453 | 0.0276038 | 0.144489 | 0.810773 | 0.81219 | -0.00141743 | 0.115476 | 0.655385 | 0.842468 | 0.926432 | 0.138742 |
| tossup_correctness | category | Mythology | 320 | 0.665056 | 0.482392 | 0.0212172 | 0.151695 | 0.803125 | 0.79375 | 0.009375 | 0.11481 | 0.645069 | 0.823764 | 0.925351 | 0.145779 |
| tossup_correctness | category | Other Academic | 64 | 0.632812 | 0.569711 | 0.172863 | 0.191904 | 0.71875 | 0.75 | -0.03125 | 0.114886 | 0.646801 | 0.804916 | 0.901197 | 0.155351 |
| tossup_correctness | category | Philosophy | 312 | 0.66129 | 0.467985 | 0.0548394 | 0.148834 | 0.810897 | 0.801282 | 0.00961538 | 0.112874 | 0.642962 | 0.813789 | 0.916181 | 0.15287 |
| tossup_correctness | category | Popular Culture | 104 | 0.600142 | 0.422493 | 0.0345966 | 0.125897 | 0.846154 | 0.846154 | 0 | 0.0716496 | 0.736868 | 0.864498 | 0.916755 | 0.12746 |
| tossup_correctness | category | Religion | 358 | 0.719309 | 0.532421 | 0.0319385 | 0.178634 | 0.73743 | 0.726257 | 0.0111732 | 0.141354 | 0.541761 | 0.768289 | 0.898487 | 0.170584 |
| tossup_correctness | category | Science | 1431 | 0.701057 | 0.492294 | 0.0156339 | 0.159214 | 0.782669 | 0.765199 | 0.0174703 | 0.14574 | 0.563297 | 0.797985 | 0.913314 | 0.158938 |
| tossup_correctness | category | Social Science | 321 | 0.733748 | 0.49386 | 0.0430734 | 0.159913 | 0.778816 | 0.744548 | 0.0342679 | 0.176443 | 0.485378 | 0.791527 | 0.91416 | 0.160119 |
| tossup_correctness | category | Unknown | 1934 | 0.71771 | 0.497333 | 0.0191985 | 0.162206 | 0.772492 | 0.75698 | 0.0155119 | 0.137695 | 0.583543 | 0.805177 | 0.915793 | 0.156394 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.745754 | 0.544309 | 0.0861649 | 0.184443 | 0.713542 | 0.697917 | 0.015625 | 0.155802 | 0.479763 | 0.746105 | 0.869693 | 0.180228 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.75222 | 0.497218 | 0.0284173 | 0.163139 | 0.768279 | 0.733408 | 0.0348706 | 0.147851 | 0.5494 | 0.789697 | 0.904047 | 0.164523 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.686691 | 0.512415 | 0.0218212 | 0.167121 | 0.767421 | 0.759276 | 0.0081448 | 0.142556 | 0.581575 | 0.813017 | 0.918585 | 0.15342 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.693353 | 0.47238 | 0.0133613 | 0.151286 | 0.800279 | 0.789125 | 0.0111537 | 0.12489 | 0.615759 | 0.82473 | 0.921374 | 0.148077 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.727229 | 0.471374 | 0.0134223 | 0.151364 | 0.789041 | 0.775342 | 0.0136986 | 0.151323 | 0.551241 | 0.803788 | 0.916961 | 0.156459 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.63941 | 0.744122 | 0.594033 | 1.42507 | 2.1038 | 2.64087 | 3.13091 | 3.94549 | 4.59517 |
| player | theta_1 | 1133 | -1.20551 | 0.870009 | -3.56215 | -2.52058 | -1.78601 | -1.27528 | -0.726747 | 0.441526 | 2.30242 |
| player | theta_2 | 1133 | -0.974678 | 0.595361 | -3.23053 | -1.97261 | -1.33956 | -0.986094 | -0.58076 | 0.029219 | 0.989627 |
| player | theta_3 | 1133 | -1.10788 | 0.758514 | -3.26051 | -2.28311 | -1.60563 | -1.16683 | -0.64464 | 0.248239 | 1.57131 |
| player | theta_norm | 1133 | 2.21558 | 0.638332 | 0.323381 | 1.19713 | 1.78497 | 2.19894 | 2.61841 | 3.32009 | 4.52834 |
| tossup | start_difficulty_d1 | 1240 | -1.77362 | 0.548453 | -3.65286 | -2.51002 | -2.14157 | -1.83761 | -1.47694 | -0.773391 | 1.3776 |
| tossup | start_difficulty_d2 | 1240 | -1.76133 | 0.504153 | -3.73478 | -2.5381 | -2.10497 | -1.79738 | -1.43096 | -0.90387 | 0.0377365 |
| tossup | start_difficulty_d3 | 1240 | -1.76106 | 0.50986 | -3.5081 | -2.53736 | -2.11107 | -1.7963 | -1.42361 | -0.884906 | 0.186821 |
| tossup | end_difficulty_d1 | 1240 | -2.7615 | 0.641102 | -5.17359 | -3.64049 | -3.19691 | -2.83344 | -2.39229 | -1.61283 | 0.684217 |
| tossup | end_difficulty_d2 | 1240 | -2.74619 | 0.591425 | -5.10325 | -3.65863 | -3.15429 | -2.78104 | -2.36769 | -1.71581 | -0.677722 |
| tossup | end_difficulty_d3 | 1240 | -2.74391 | 0.594569 | -4.80468 | -3.678 | -3.15067 | -2.77433 | -2.35338 | -1.72222 | -0.549277 |
| tossup | total_drop_d1 | 1240 | 0.987881 | 0.112357 | 0.593555 | 0.796608 | 0.912722 | 0.99523 | 1.05929 | 1.15561 | 1.52073 |
| tossup | total_drop_d2 | 1240 | 0.984865 | 0.104264 | 0.680966 | 0.8178 | 0.913107 | 0.981789 | 1.05542 | 1.15396 | 1.36848 |
| tossup | total_drop_d3 | 1240 | 0.982856 | 0.10371 | 0.60209 | 0.822504 | 0.909555 | 0.984897 | 1.05083 | 1.14858 | 1.37022 |
| tossup | drop_share_1_d1 | 1240 | 0.249006 | 0.031807 | 0.117441 | 0.19838 | 0.230569 | 0.249568 | 0.268694 | 0.298596 | 0.425445 |
| tossup | drop_share_2_d1 | 1240 | 0.372554 | 0.0221533 | 0.293315 | 0.335873 | 0.358242 | 0.373197 | 0.386996 | 0.407265 | 0.458444 |
| tossup | drop_share_3_d1 | 1240 | 0.37844 | 0.0402303 | 0.198134 | 0.318609 | 0.35246 | 0.375967 | 0.400705 | 0.44649 | 0.573341 |
| tossup | drop_share_1_d2 | 1240 | 0.247984 | 0.0289702 | 0.134494 | 0.199855 | 0.230256 | 0.247997 | 0.266256 | 0.293571 | 0.418925 |
| tossup | drop_share_2_d2 | 1240 | 0.371793 | 0.0207762 | 0.27585 | 0.33663 | 0.358489 | 0.372458 | 0.385144 | 0.404817 | 0.451766 |
| tossup | drop_share_3_d2 | 1240 | 0.380223 | 0.0371588 | 0.220592 | 0.322649 | 0.355956 | 0.38037 | 0.402273 | 0.439907 | 0.584839 |
| tossup | drop_share_1_d3 | 1240 | 0.247942 | 0.0302586 | 0.140418 | 0.196131 | 0.230584 | 0.247881 | 0.267607 | 0.29642 | 0.404903 |
| tossup | drop_share_2_d3 | 1240 | 0.372302 | 0.0210677 | 0.274668 | 0.33893 | 0.358868 | 0.373008 | 0.386347 | 0.404969 | 0.464693 |
| tossup | drop_share_3_d3 | 1240 | 0.379756 | 0.0377453 | 0.263922 | 0.323181 | 0.355168 | 0.377108 | 0.402073 | 0.439756 | 0.563903 |
| tossup | r_1 | 1240 | 0.321957 | 0.144202 | 0.055065 | 0.134034 | 0.211617 | 0.294634 | 0.406579 | 0.599614 | 0.846232 |
| tossup | r_2 | 1240 | 0.335765 | 0.105769 | 0.0733131 | 0.172993 | 0.265604 | 0.329335 | 0.395188 | 0.528566 | 0.824682 |
| tossup | r_3 | 1240 | 0.342278 | 0.119685 | 0.0737865 | 0.166151 | 0.257358 | 0.333607 | 0.411467 | 0.575472 | 0.79504 |
| tossup | r_norm | 1240 | 0.614938 | 0.0408627 | 0.577382 | 0.578899 | 0.586612 | 0.601136 | 0.627022 | 0.701104 | 0.8532 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.42329 | 0.484924 | 2.14595 | 3.70566 | 4.13799 | 4.37728 | 4.66306 | 5.34472 | 6.31047 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.40707 | 0.41019 | 2.24533 | 3.79809 | 4.17725 | 4.386 | 4.60078 | 5.09359 | 6.56546 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.41197 | 0.428355 | 2.40375 | 3.71751 | 4.16785 | 4.39557 | 4.6512 | 5.12397 | 6.00868 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.59561 | 2.42022 | -9.69325 | -3.34667 | 0.293237 | 2.80824 | 3.25442 | 3.58079 | 4.33049 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.31084 | 2.00493 | -8.87217 | -2.38267 | 2.47402 | 3.09971 | 3.35782 | 3.67462 | 4.16931 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.07443 | 2.16172 | -9.14939 | -2.81231 | 1.89103 | 3.00348 | 3.34455 | 3.69938 | 4.25418 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.82768 | 2.57187 | 0.876178 | 0.983034 | 1.06079 | 1.34538 | 4.38097 | 8.08534 | 14.8193 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.09623 | 2.15905 | 0.892739 | 0.961703 | 1.02129 | 1.15423 | 1.65682 | 7.19745 | 13.5072 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.33754 | 2.27157 | 0.879602 | 0.966296 | 1.02934 | 1.21007 | 2.42061 | 7.44988 | 13.6164 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.157675 | 0.0825524 | 0.0116724 | 0.0312155 | 0.0836895 | 0.173927 | 0.216196 | 0.268237 | 0.53558 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.32709 | 0.12703 | 0.0204184 | 0.081656 | 0.285627 | 0.34522 | 0.376903 | 0.525278 | 0.861273 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.515235 | 0.17854 | 0.0515541 | 0.28035 | 0.402394 | 0.46955 | 0.592445 | 0.881317 | 0.965388 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.175635 | 0.0723284 | 0.0130085 | 0.0356128 | 0.135757 | 0.189974 | 0.221702 | 0.266998 | 0.59413 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.338189 | 0.0982964 | 0.0187078 | 0.129861 | 0.311024 | 0.345342 | 0.375891 | 0.458025 | 0.768042 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.486176 | 0.141054 | 0.130975 | 0.32173 | 0.405866 | 0.452658 | 0.527569 | 0.827522 | 0.968284 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.167551 | 0.0743057 | 0.0141252 | 0.0354586 | 0.119508 | 0.178506 | 0.219847 | 0.264031 | 0.638689 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.339085 | 0.105899 | 0.0321583 | 0.118535 | 0.305374 | 0.344018 | 0.378252 | 0.512991 | 0.858426 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.493364 | 0.147575 | 0.0300521 | 0.315113 | 0.405682 | 0.462011 | 0.544257 | 0.840406 | 0.949546 |
| tossup_hazard | hazard_r_1 | 1240 | 0.384448 | 0.276344 | 0.0254966 | 0.0630207 | 0.138347 | 0.298992 | 0.606522 | 0.885957 | 0.952822 |
| tossup_hazard | hazard_r_2 | 1240 | 0.279953 | 0.197339 | 0.0287355 | 0.0586452 | 0.124199 | 0.212828 | 0.396404 | 0.682158 | 0.855881 |
| tossup_hazard | hazard_r_3 | 1240 | 0.335599 | 0.233094 | 0.018442 | 0.0461753 | 0.144665 | 0.272294 | 0.517116 | 0.761698 | 0.931233 |
