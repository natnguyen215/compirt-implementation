# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/terminal-off/degree_3/curves_3/dirichlet_2/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/terminal-off/degree_3/curves_3/dirichlet_2/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 306297 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.713008 |
| log_loss | 0.504031 |
| ece | 0.0646817 |
| brier | 0.165019 |
| accuracy | 0.767203 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00302474 |
| probability_std | 0.165324 |
| probability_p10 | 0.463698 |
| probability_p50 | 0.725994 |
| probability_p90 | 0.892641 |
| mean_predictive_variance | 0.182838 |
| integrated_brier_score | 0.107795 |
| joint_tossup_event_log_loss | 6.74422 |
| buzz_position_mae | 0.176676 |
| buzz_position_median_absolute_error | 0.156523 |
| buzz_position_bias | -0.0967091 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.340931 |
| first_buzzer_mean_reciprocal_rank | 0.556069 |
| first_buzzer_log_loss | 1.68909 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.713008 |
| neg_average_precision | 0.44905 |
| neg_precision | 0.511824 |
| neg_recall | 0.2776 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.097015 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0782982 |
| no_buzz_calibration_error | 0.0651852 |
| no_buzz_brier | 0.0234838 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.713008 | 0.504031 | 0.0646817 | 0.165019 | 0.767203 | 0.764178 | 0.00302474 | 0.165324 | 0.463698 | 0.725994 | 0.892641 | 0.182838 |
| tossup_correctness | tier | fall | 2798 | 0.729591 | 0.473981 | 0.0669193 | 0.152663 | 0.788063 | 0.785204 | 0.00285919 | 0.159258 | 0.493333 | 0.748295 | 0.911616 | 0.175424 |
| tossup_correctness | tier | nationals | 1545 | 0.711239 | 0.545077 | 0.0688009 | 0.183165 | 0.717799 | 0.721036 | -0.00323625 | 0.16907 | 0.415669 | 0.673609 | 0.859053 | 0.198194 |
| tossup_correctness | tier | regionals | 2039 | 0.694266 | 0.51886 | 0.0783875 | 0.170921 | 0.761648 | 0.762138 | -0.000490436 | 0.165469 | 0.445048 | 0.705514 | 0.885062 | 0.188549 |
| tossup_correctness | tier | winter | 2875 | 0.705014 | 0.500699 | 0.057587 | 0.163106 | 0.777391 | 0.768348 | 0.00904348 | 0.16278 | 0.487994 | 0.744373 | 0.897643 | 0.177751 |
| tossup_correctness | category | Current Events | 129 | 0.695782 | 0.573885 | 0.072457 | 0.196781 | 0.705426 | 0.666667 | 0.0387597 | 0.180004 | 0.439067 | 0.675176 | 0.919112 | 0.187416 |
| tossup_correctness | category | Fine Arts | 1074 | 0.711875 | 0.497608 | 0.081549 | 0.162524 | 0.780261 | 0.776536 | 0.00372439 | 0.171169 | 0.45527 | 0.724472 | 0.892783 | 0.182623 |
| tossup_correctness | category | Geography | 180 | 0.765505 | 0.538788 | 0.0458924 | 0.181345 | 0.733333 | 0.616667 | 0.116667 | 0.222767 | 0.256394 | 0.66926 | 0.843 | 0.187419 |
| tossup_correctness | category | History | 1454 | 0.704038 | 0.512506 | 0.0552143 | 0.168859 | 0.759285 | 0.757909 | 0.00137552 | 0.163493 | 0.466981 | 0.726517 | 0.89537 | 0.181692 |
| tossup_correctness | category | Literature | 1435 | 0.71615 | 0.453097 | 0.0663604 | 0.142821 | 0.809059 | 0.810453 | -0.00139373 | 0.145038 | 0.52828 | 0.773718 | 0.91053 | 0.169021 |
| tossup_correctness | category | Mythology | 324 | 0.663221 | 0.496819 | 0.0710681 | 0.158458 | 0.799383 | 0.79321 | 0.00617284 | 0.150455 | 0.529908 | 0.770379 | 0.90149 | 0.170412 |
| tossup_correctness | category | Other Academic | 71 | 0.599129 | 0.585927 | 0.129663 | 0.193271 | 0.71831 | 0.760563 | -0.0422535 | 0.130118 | 0.534513 | 0.687648 | 0.856126 | 0.198505 |
| tossup_correctness | category | Philosophy | 310 | 0.757845 | 0.484483 | 0.0758232 | 0.158621 | 0.745161 | 0.76129 | -0.016129 | 0.148488 | 0.493135 | 0.721408 | 0.886301 | 0.185827 |
| tossup_correctness | category | Popular Culture | 108 | 0.543403 | 0.403729 | 0.154661 | 0.118565 | 0.888889 | 0.888889 | 0 | 0.113756 | 0.594754 | 0.808287 | 0.922759 | 0.154787 |
| tossup_correctness | category | Religion | 361 | 0.696237 | 0.545293 | 0.100093 | 0.183122 | 0.722992 | 0.742382 | -0.0193906 | 0.160897 | 0.426028 | 0.661605 | 0.847196 | 0.202082 |
| tossup_correctness | category | Science | 1445 | 0.722647 | 0.513119 | 0.0535903 | 0.16973 | 0.746021 | 0.746021 | 0 | 0.163663 | 0.463119 | 0.716391 | 0.88802 | 0.186123 |
| tossup_correctness | category | Social Science | 327 | 0.741351 | 0.527103 | 0.0779319 | 0.176201 | 0.755352 | 0.718654 | 0.0366972 | 0.184423 | 0.393826 | 0.692777 | 0.883213 | 0.188921 |
| tossup_correctness | category | Unknown | 2039 | 0.694266 | 0.51886 | 0.0783875 | 0.170921 | 0.761648 | 0.762138 | -0.000490436 | 0.165469 | 0.445048 | 0.705514 | 0.885062 | 0.188549 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.67428 | 0.562071 | 0.118963 | 0.190844 | 0.721311 | 0.743169 | -0.0218579 | 0.174023 | 0.389174 | 0.649848 | 0.846922 | 0.202297 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.720809 | 0.529321 | 0.0556064 | 0.175867 | 0.748691 | 0.728796 | 0.0198953 | 0.176161 | 0.413821 | 0.705256 | 0.883014 | 0.188538 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.722794 | 0.504913 | 0.0556451 | 0.165968 | 0.762394 | 0.752568 | 0.00982582 | 0.170335 | 0.463548 | 0.729465 | 0.896954 | 0.181178 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.706485 | 0.487724 | 0.0711769 | 0.158108 | 0.782261 | 0.786087 | -0.00382609 | 0.161684 | 0.486155 | 0.741972 | 0.902522 | 0.177613 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.708575 | 0.507403 | 0.0695285 | 0.165902 | 0.765058 | 0.764393 | 0.000665557 | 0.158577 | 0.472091 | 0.721511 | 0.881653 | 0.186078 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 4.35755 | 0.571924 | 2.32349 | 3.38334 | 3.97199 | 4.34466 | 4.77114 | 5.27703 | 6.02642 |
| player | theta_1 | 1197 | -1.15497 | 0.963809 | -3.83655 | -2.51841 | -1.85922 | -1.26121 | -0.541056 | 0.619297 | 2.04002 |
| player | theta_2 | 1197 | -1.08905 | 0.806242 | -3.86804 | -2.38058 | -1.55396 | -1.10959 | -0.63504 | 0.337672 | 1.85895 |
| player | theta_3 | 1197 | -1.09224 | 0.749055 | -3.41849 | -2.28711 | -1.58217 | -1.13744 | -0.582771 | 0.18752 | 1.0337 |
| player | theta_norm | 1197 | 2.32573 | 0.665259 | 0.354851 | 1.2795 | 1.84689 | 2.34648 | 2.78332 | 3.35284 | 4.43171 |
| tossup | start_difficulty_d1 | 1240 | -0.751093 | 0.66009 | -3.54827 | -1.99878 | -1.09285 | -0.673493 | -0.342141 | 0.216137 | 1.45974 |
| tossup | start_difficulty_d2 | 1240 | -0.627942 | 0.538764 | -3.34944 | -1.65224 | -0.821521 | -0.57053 | -0.346882 | 0.113777 | 1.24663 |
| tossup | start_difficulty_d3 | 1240 | -0.621296 | 0.510733 | -3.44058 | -1.49138 | -0.812602 | -0.561794 | -0.352722 | 0.0814305 | 1.04655 |
| tossup | end_difficulty_d1 | 1240 | -1.91255 | 0.849034 | -5.09202 | -3.57207 | -2.33191 | -1.8057 | -1.38274 | -0.705144 | 0.600824 |
| tossup | end_difficulty_d2 | 1240 | -1.75237 | 0.689095 | -4.89369 | -3.05233 | -1.99406 | -1.67052 | -1.3955 | -0.826073 | 0.49872 |
| tossup | end_difficulty_d3 | 1240 | -1.74435 | 0.638761 | -5.54172 | -2.86114 | -1.9687 | -1.67648 | -1.40403 | -0.88387 | 0.271694 |
| tossup | total_drop_d1 | 1240 | 1.16146 | 0.249506 | 0.744714 | 0.891902 | 1.01698 | 1.11229 | 1.23698 | 1.59608 | 3.95379 |
| tossup | total_drop_d2 | 1240 | 1.12443 | 0.183618 | 0.702206 | 0.908196 | 1.02806 | 1.09814 | 1.17843 | 1.4222 | 2.82122 |
| tossup | total_drop_d3 | 1240 | 1.12306 | 0.16261 | 0.753086 | 0.928896 | 1.03561 | 1.10369 | 1.17574 | 1.38648 | 2.68181 |
| tossup | drop_share_1_d1 | 1240 | 0.317058 | 0.0208703 | 0.225256 | 0.288191 | 0.304645 | 0.31508 | 0.326223 | 0.354786 | 0.410356 |
| tossup | drop_share_2_d1 | 1240 | 0.349427 | 0.0126575 | 0.310001 | 0.329672 | 0.341031 | 0.348598 | 0.357562 | 0.370408 | 0.461305 |
| tossup | drop_share_3_d1 | 1240 | 0.333515 | 0.0207163 | 0.234795 | 0.296136 | 0.322616 | 0.335242 | 0.347202 | 0.362374 | 0.410616 |
| tossup | drop_share_1_d2 | 1240 | 0.314757 | 0.0179182 | 0.246224 | 0.290502 | 0.304179 | 0.313225 | 0.323437 | 0.344259 | 0.414027 |
| tossup | drop_share_2_d2 | 1240 | 0.348565 | 0.011735 | 0.310204 | 0.328621 | 0.340231 | 0.348873 | 0.356484 | 0.367327 | 0.382617 |
| tossup | drop_share_3_d2 | 1240 | 0.336678 | 0.017687 | 0.254447 | 0.307439 | 0.328451 | 0.337616 | 0.347225 | 0.362153 | 0.411949 |
| tossup | drop_share_1_d3 | 1240 | 0.314599 | 0.0173753 | 0.261105 | 0.290233 | 0.303636 | 0.313745 | 0.323474 | 0.340038 | 0.445778 |
| tossup | drop_share_2_d3 | 1240 | 0.348468 | 0.0117349 | 0.307859 | 0.32918 | 0.340875 | 0.348204 | 0.356254 | 0.367695 | 0.382613 |
| tossup | drop_share_3_d3 | 1240 | 0.336933 | 0.016979 | 0.238796 | 0.310276 | 0.327748 | 0.337696 | 0.347866 | 0.362315 | 0.394565 |
| tossup | r_1 | 1240 | 0.378217 | 0.196362 | 0.0484022 | 0.0958749 | 0.219255 | 0.355854 | 0.511405 | 0.742527 | 0.870882 |
| tossup | r_2 | 1240 | 0.317824 | 0.179045 | 0.0566727 | 0.0988708 | 0.180411 | 0.279587 | 0.412761 | 0.67795 | 0.904796 |
| tossup | r_3 | 1240 | 0.303958 | 0.180651 | 0.0449074 | 0.0906724 | 0.165392 | 0.258242 | 0.401545 | 0.679418 | 0.894925 |
| tossup | r_norm | 1240 | 0.659002 | 0.0730625 | 0.57737 | 0.582164 | 0.602591 | 0.635622 | 0.693492 | 0.813558 | 0.907305 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.66215 | 0.935639 | 0.333039 | 0.598456 | 0.885636 | 1.37377 | 2.33864 | 3.43263 | 4.58238 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.55123 | 0.893459 | 0.301617 | 0.490432 | 0.841494 | 1.29148 | 2.17037 | 3.23646 | 4.44405 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.5173 | 0.802887 | 0.291249 | 0.486296 | 0.850077 | 1.41002 | 2.03846 | 2.95397 | 4.76375 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.565175 | 1.45037 | -8.50241 | -3.52311 | -0.735428 | -0.157427 | 0.286388 | 0.905816 | 1.73732 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.471186 | 1.28856 | -10.6098 | -3.09359 | -0.512248 | -0.1318 | 0.188088 | 0.668329 | 1.54899 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.623362 | 1.40493 | -10.368 | -3.2661 | -0.646549 | -0.234548 | 0.141634 | 0.648696 | 1.40611 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.22732 | 2.10884 | 0.790574 | 0.946058 | 0.995411 | 1.05978 | 3.06008 | 6.54978 | 11.5796 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.02242 | 1.89295 | 0.863224 | 0.94729 | 0.993417 | 1.0735 | 1.99791 | 6.06883 | 13.5107 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.14066 | 1.95532 | 0.843079 | 0.950983 | 0.997898 | 1.09482 | 2.50891 | 6.23223 | 13.9794 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.229341 | 0.0823038 | 0.0372255 | 0.0664446 | 0.179303 | 0.269133 | 0.28714 | 0.302764 | 0.425072 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.332184 | 0.0831413 | 0.0580586 | 0.143662 | 0.334162 | 0.34762 | 0.35902 | 0.434683 | 0.760541 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.438476 | 0.141981 | 0.0985986 | 0.340797 | 0.35953 | 0.377194 | 0.427331 | 0.782733 | 0.902593 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.231587 | 0.0801966 | 0.0341117 | 0.0706245 | 0.181671 | 0.270518 | 0.2917 | 0.304904 | 0.359993 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.32801 | 0.0713349 | 0.0490526 | 0.154716 | 0.332535 | 0.346865 | 0.357719 | 0.38797 | 0.699598 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.440403 | 0.136353 | 0.200209 | 0.339911 | 0.357598 | 0.376164 | 0.450767 | 0.770798 | 0.916836 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.229928 | 0.0783536 | 0.0230403 | 0.0735821 | 0.177307 | 0.264945 | 0.289679 | 0.306355 | 0.512713 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.33744 | 0.0711791 | 0.0601349 | 0.169806 | 0.335149 | 0.347616 | 0.361177 | 0.422289 | 0.718252 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.432632 | 0.127684 | 0.0934634 | 0.339322 | 0.358652 | 0.376939 | 0.448692 | 0.753318 | 0.896671 |
| tossup_hazard | hazard_r_1 | 1240 | 0.334902 | 0.307623 | 0.0251696 | 0.0418093 | 0.0778392 | 0.179157 | 0.628764 | 0.901684 | 0.947539 |
| tossup_hazard | hazard_r_2 | 1240 | 0.320105 | 0.286711 | 0.0126373 | 0.0339658 | 0.074907 | 0.201648 | 0.547902 | 0.864261 | 0.937955 |
| tossup_hazard | hazard_r_3 | 1240 | 0.344993 | 0.289895 | 0.012173 | 0.0254239 | 0.0797859 | 0.246044 | 0.611068 | 0.85303 | 0.936196 |
