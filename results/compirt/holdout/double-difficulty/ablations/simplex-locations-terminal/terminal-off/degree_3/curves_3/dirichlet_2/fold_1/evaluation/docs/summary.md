# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/terminal-off/degree_3/curves_3/dirichlet_2/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/terminal-off/degree_3/curves_3/dirichlet_2/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 307016 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709588 |
| log_loss | 0.506994 |
| ece | 0.0636272 |
| brier | 0.165554 |
| accuracy | 0.767074 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00494886 |
| probability_std | 0.166516 |
| probability_p10 | 0.463908 |
| probability_p50 | 0.725952 |
| probability_p90 | 0.898097 |
| mean_predictive_variance | 0.181581 |
| integrated_brier_score | 0.106916 |
| joint_tossup_event_log_loss | 6.73337 |
| buzz_position_mae | 0.177669 |
| buzz_position_median_absolute_error | 0.160718 |
| buzz_position_bias | -0.10181 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.333223 |
| first_buzzer_mean_reciprocal_rank | 0.550355 |
| first_buzzer_log_loss | 1.70571 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.709588 |
| neg_average_precision | 0.45574 |
| neg_precision | 0.518828 |
| neg_recall | 0.286639 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0963825 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0794862 |
| no_buzz_calibration_error | 0.0635771 |
| no_buzz_brier | 0.0254892 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.709588 | 0.506994 | 0.0636272 | 0.165554 | 0.767074 | 0.762125 | 0.00494886 | 0.166516 | 0.463908 | 0.725952 | 0.898097 | 0.181581 |
| tossup_correctness | tier | fall | 2842 | 0.727585 | 0.472962 | 0.0557528 | 0.15179 | 0.789937 | 0.785362 | 0.00457424 | 0.159853 | 0.503126 | 0.758577 | 0.914466 | 0.171726 |
| tossup_correctness | tier | nationals | 1564 | 0.712454 | 0.544278 | 0.0639047 | 0.181873 | 0.736573 | 0.718031 | 0.0185422 | 0.170237 | 0.415105 | 0.676268 | 0.862591 | 0.197009 |
| tossup_correctness | tier | regionals | 1937 | 0.688835 | 0.527932 | 0.0804483 | 0.173812 | 0.753227 | 0.758389 | -0.00516262 | 0.166062 | 0.445994 | 0.710446 | 0.878183 | 0.188572 |
| tossup_correctness | tier | winter | 2750 | 0.696573 | 0.506214 | 0.0642588 | 0.164679 | 0.770545 | 0.765818 | 0.00472727 | 0.164296 | 0.477102 | 0.738134 | 0.901868 | 0.178066 |
| tossup_correctness | category | Current Events | 126 | 0.723782 | 0.518652 | 0.130475 | 0.17319 | 0.746032 | 0.769841 | -0.0238095 | 0.164714 | 0.4048 | 0.65726 | 0.876507 | 0.200875 |
| tossup_correctness | category | Fine Arts | 1071 | 0.747727 | 0.481803 | 0.0677422 | 0.155469 | 0.786181 | 0.766573 | 0.0196078 | 0.175028 | 0.444574 | 0.740431 | 0.903492 | 0.178344 |
| tossup_correctness | category | Geography | 185 | 0.793605 | 0.528731 | 0.120493 | 0.170212 | 0.756757 | 0.697297 | 0.0594595 | 0.216526 | 0.280882 | 0.658614 | 0.848129 | 0.189989 |
| tossup_correctness | category | History | 1440 | 0.716445 | 0.505554 | 0.0542771 | 0.165699 | 0.763194 | 0.754167 | 0.00902778 | 0.162585 | 0.478957 | 0.727372 | 0.905151 | 0.180486 |
| tossup_correctness | category | Literature | 1422 | 0.672908 | 0.471422 | 0.0756598 | 0.150371 | 0.799578 | 0.814346 | -0.0147679 | 0.149782 | 0.533946 | 0.768577 | 0.912809 | 0.167994 |
| tossup_correctness | category | Mythology | 318 | 0.671463 | 0.491174 | 0.0736082 | 0.156431 | 0.805031 | 0.789308 | 0.0157233 | 0.152089 | 0.52903 | 0.77369 | 0.902681 | 0.170897 |
| tossup_correctness | category | Other Academic | 66 | 0.824188 | 0.49081 | 0.13242 | 0.159239 | 0.772727 | 0.712121 | 0.0606061 | 0.144149 | 0.48343 | 0.675336 | 0.843089 | 0.201389 |
| tossup_correctness | category | Philosophy | 311 | 0.736087 | 0.505179 | 0.0327446 | 0.168639 | 0.742765 | 0.745981 | -0.00321543 | 0.146285 | 0.509605 | 0.725952 | 0.887789 | 0.182304 |
| tossup_correctness | category | Popular Culture | 102 | 0.493519 | 0.424876 | 0.11774 | 0.123999 | 0.872549 | 0.882353 | -0.00980392 | 0.108103 | 0.632046 | 0.78608 | 0.916277 | 0.158058 |
| tossup_correctness | category | Religion | 358 | 0.700438 | 0.55729 | 0.0815027 | 0.187436 | 0.695531 | 0.712291 | -0.0167598 | 0.159886 | 0.444511 | 0.690187 | 0.872347 | 0.195105 |
| tossup_correctness | category | Science | 1433 | 0.694381 | 0.530678 | 0.0485343 | 0.175484 | 0.748779 | 0.738311 | 0.0104676 | 0.169361 | 0.459908 | 0.71237 | 0.897616 | 0.184263 |
| tossup_correctness | category | Social Science | 324 | 0.764732 | 0.496769 | 0.0705848 | 0.162137 | 0.787037 | 0.731481 | 0.0555556 | 0.176617 | 0.411633 | 0.701041 | 0.889758 | 0.189032 |
| tossup_correctness | category | Unknown | 1937 | 0.688835 | 0.527932 | 0.0804483 | 0.173812 | 0.753227 | 0.758389 | -0.00516262 | 0.166062 | 0.445994 | 0.710446 | 0.878183 | 0.188572 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.702031 | 0.555246 | 0.107483 | 0.188292 | 0.706587 | 0.712575 | -0.00598802 | 0.159402 | 0.445744 | 0.682388 | 0.847105 | 0.198078 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.723126 | 0.531948 | 0.0646807 | 0.177288 | 0.743421 | 0.729167 | 0.0142544 | 0.186949 | 0.389563 | 0.688662 | 0.885668 | 0.18793 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.715077 | 0.509026 | 0.0521372 | 0.16641 | 0.761702 | 0.755083 | 0.00661939 | 0.166078 | 0.471282 | 0.733581 | 0.904429 | 0.179819 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.692574 | 0.498337 | 0.0718599 | 0.161645 | 0.774965 | 0.780942 | -0.0059775 | 0.160418 | 0.486855 | 0.735979 | 0.900548 | 0.179073 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.713645 | 0.503561 | 0.0671288 | 0.163854 | 0.773813 | 0.762029 | 0.011784 | 0.16443 | 0.464457 | 0.724424 | 0.894588 | 0.182338 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 4.36776 | 0.576854 | 2.35249 | 3.41654 | 3.9582 | 4.39271 | 4.76073 | 5.33236 | 5.93571 |
| player | theta_1 | 1167 | -1.17704 | 1.0126 | -3.4878 | -2.59002 | -1.92674 | -1.27408 | -0.546816 | 0.666359 | 2.47168 |
| player | theta_2 | 1167 | -1.07621 | 0.779002 | -3.60083 | -2.37342 | -1.5417 | -1.07563 | -0.625308 | 0.228349 | 1.83889 |
| player | theta_3 | 1167 | -1.08192 | 0.739432 | -3.18184 | -2.31149 | -1.57078 | -1.14255 | -0.598332 | 0.180107 | 1.48259 |
| player | theta_norm | 1167 | 2.33089 | 0.677233 | 0.29264 | 1.19981 | 1.84658 | 2.36595 | 2.80311 | 3.38863 | 4.25797 |
| tossup | start_difficulty_d1 | 1220 | -0.753199 | 0.66233 | -3.45464 | -2.01426 | -1.06703 | -0.683381 | -0.341875 | 0.210012 | 0.962831 |
| tossup | start_difficulty_d2 | 1220 | -0.622251 | 0.528045 | -3.21424 | -1.64424 | -0.81644 | -0.563124 | -0.362105 | 0.115569 | 0.918393 |
| tossup | start_difficulty_d3 | 1220 | -0.636902 | 0.535607 | -3.06028 | -1.64785 | -0.840522 | -0.562617 | -0.356192 | 0.110785 | 1.47669 |
| tossup | end_difficulty_d1 | 1220 | -1.91596 | 0.860712 | -6.23722 | -3.63429 | -2.31164 | -1.78994 | -1.38152 | -0.696675 | 0.149092 |
| tossup | end_difficulty_d2 | 1220 | -1.74425 | 0.670751 | -5.38126 | -2.94908 | -1.97207 | -1.66468 | -1.41843 | -0.812358 | 0.195907 |
| tossup | end_difficulty_d3 | 1220 | -1.76556 | 0.674471 | -5.49344 | -3.05569 | -2.02605 | -1.66838 | -1.41707 | -0.858068 | 0.617749 |
| tossup | total_drop_d1 | 1220 | 1.16276 | 0.253678 | 0.723626 | 0.892551 | 1.02343 | 1.10998 | 1.22764 | 1.61324 | 3.48009 |
| tossup | total_drop_d2 | 1220 | 1.122 | 0.178918 | 0.722486 | 0.913875 | 1.03255 | 1.09588 | 1.17798 | 1.38987 | 2.66606 |
| tossup | total_drop_d3 | 1220 | 1.12866 | 0.176834 | 0.735621 | 0.921054 | 1.03591 | 1.10221 | 1.18447 | 1.40742 | 2.91088 |
| tossup | drop_share_1_d1 | 1220 | 0.317434 | 0.0213756 | 0.227138 | 0.288841 | 0.30455 | 0.315077 | 0.32692 | 0.355912 | 0.446162 |
| tossup | drop_share_2_d1 | 1220 | 0.349325 | 0.0122062 | 0.308194 | 0.33046 | 0.340884 | 0.348525 | 0.357361 | 0.370313 | 0.402634 |
| tossup | drop_share_3_d1 | 1220 | 0.333241 | 0.0213061 | 0.233369 | 0.2936 | 0.323328 | 0.335502 | 0.346757 | 0.364188 | 0.406769 |
| tossup | drop_share_1_d2 | 1220 | 0.314491 | 0.0180561 | 0.234495 | 0.290954 | 0.303963 | 0.313394 | 0.322909 | 0.343053 | 0.449491 |
| tossup | drop_share_2_d2 | 1220 | 0.348453 | 0.0115614 | 0.309885 | 0.32952 | 0.340423 | 0.348795 | 0.35627 | 0.366736 | 0.386205 |
| tossup | drop_share_3_d2 | 1220 | 0.337056 | 0.0174245 | 0.240624 | 0.309748 | 0.328543 | 0.337665 | 0.347007 | 0.362398 | 0.413266 |
| tossup | drop_share_1_d3 | 1220 | 0.314929 | 0.0177875 | 0.256255 | 0.290367 | 0.303516 | 0.313754 | 0.323655 | 0.343587 | 0.420158 |
| tossup | drop_share_2_d3 | 1220 | 0.348471 | 0.0118603 | 0.308192 | 0.329155 | 0.340969 | 0.348053 | 0.356276 | 0.367551 | 0.403215 |
| tossup | drop_share_3_d3 | 1220 | 0.3366 | 0.0175864 | 0.240782 | 0.307769 | 0.327101 | 0.3374 | 0.347603 | 0.361778 | 0.405157 |
| tossup | r_1 | 1220 | 0.378148 | 0.202794 | 0.0462904 | 0.0982301 | 0.210949 | 0.353059 | 0.53211 | 0.748765 | 0.860341 |
| tossup | r_2 | 1220 | 0.30694 | 0.173141 | 0.0565929 | 0.100622 | 0.174386 | 0.269393 | 0.40257 | 0.663502 | 0.894854 |
| tossup | r_3 | 1220 | 0.314911 | 0.186093 | 0.0477741 | 0.0945623 | 0.168237 | 0.265751 | 0.429712 | 0.69039 | 0.894114 |
| tossup | r_norm | 1220 | 0.660847 | 0.0728713 | 0.577383 | 0.583181 | 0.603352 | 0.639002 | 0.701028 | 0.815504 | 0.897963 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 1.69573 | 0.964863 | 0.187726 | 0.601313 | 0.86247 | 1.38465 | 2.50061 | 3.4166 | 4.55466 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 1.52121 | 0.852071 | 0.230765 | 0.493942 | 0.813172 | 1.3167 | 2.0936 | 3.18805 | 4.50709 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 1.51848 | 0.828851 | 0.189694 | 0.473021 | 0.845862 | 1.33113 | 2.09547 | 3.03162 | 4.1773 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | -0.586471 | 1.44039 | -8.84551 | -3.66635 | -0.986232 | -0.161953 | 0.264212 | 0.894362 | 2.21023 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | -0.526938 | 1.34767 | -9.27241 | -3.16674 | -0.535027 | -0.186156 | 0.180046 | 0.664037 | 1.37544 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | -0.638926 | 1.48446 | -9.75556 | -3.58608 | -0.665595 | -0.222666 | 0.119473 | 0.742035 | 2.02494 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.28221 | 2.11993 | 0.790799 | 0.94712 | 0.998768 | 1.06695 | 3.59129 | 6.70439 | 10.7816 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.04815 | 1.92825 | 0.87489 | 0.949483 | 0.993154 | 1.06902 | 2.08149 | 6.18633 | 12.2598 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.1574 | 2.0443 | 0.861499 | 0.946194 | 0.995321 | 1.07503 | 2.52132 | 6.26306 | 12.7436 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.226389 | 0.0837934 | 0.0337001 | 0.0680055 | 0.163822 | 0.269528 | 0.287619 | 0.30203 | 0.398378 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.3296 | 0.0851815 | 0.0673097 | 0.134367 | 0.331917 | 0.347313 | 0.359419 | 0.440847 | 0.765345 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.444011 | 0.146836 | 0.0902071 | 0.338521 | 0.359263 | 0.376714 | 0.453071 | 0.792943 | 0.894764 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.232224 | 0.0799196 | 0.0286852 | 0.0706191 | 0.180553 | 0.269921 | 0.291685 | 0.306068 | 0.361328 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.330046 | 0.0709193 | 0.0398166 | 0.149927 | 0.333831 | 0.346936 | 0.358558 | 0.394539 | 0.660361 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.437729 | 0.134703 | 0.248112 | 0.340113 | 0.35701 | 0.373904 | 0.45404 | 0.769745 | 0.931498 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.231004 | 0.0794613 | 0.0257935 | 0.0710447 | 0.179764 | 0.267749 | 0.290975 | 0.306008 | 0.491632 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.336727 | 0.0702847 | 0.0676474 | 0.174546 | 0.334613 | 0.348179 | 0.360433 | 0.421366 | 0.717503 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.432269 | 0.12852 | 0.121619 | 0.338114 | 0.357622 | 0.374668 | 0.444047 | 0.747098 | 0.885207 |
| tossup_hazard | hazard_r_1 | 1220 | 0.345409 | 0.316923 | 0.0269217 | 0.0440678 | 0.0782646 | 0.179365 | 0.650389 | 0.923255 | 0.963933 |
| tossup_hazard | hazard_r_2 | 1220 | 0.320741 | 0.290045 | 0.0159211 | 0.0318107 | 0.0699413 | 0.188341 | 0.560179 | 0.860075 | 0.939018 |
| tossup_hazard | hazard_r_3 | 1220 | 0.33385 | 0.289677 | 0.00845055 | 0.026466 | 0.0743599 | 0.232443 | 0.591907 | 0.855168 | 0.937749 |
