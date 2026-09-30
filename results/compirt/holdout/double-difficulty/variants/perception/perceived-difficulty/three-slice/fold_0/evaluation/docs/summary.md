# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 316011 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.607404 |
| log_loss | 0.698998 |
| ece | 0.253628 |
| brier | 0.248963 |
| accuracy | 0.592039 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.173211 |
| probability_std | 0.163819 |
| probability_p10 | 0.276685 |
| probability_p50 | 0.529378 |
| probability_p90 | 0.71466 |
| mean_predictive_variance | 0.223028 |
| integrated_brier_score | 0.0949567 |
| joint_tossup_event_log_loss | 6.81465 |
| buzz_position_mae | 0.139128 |
| buzz_position_median_absolute_error | 0.116817 |
| buzz_position_bias | -0.0021107 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.3773 |
| first_buzzer_mean_reciprocal_rank | 0.583775 |
| first_buzzer_log_loss | 1.64248 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.607404 |
| neg_average_precision | 0.307583 |
| neg_precision | 0.298448 |
| neg_recall | 0.546288 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.136452 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0514629 |
| no_buzz_calibration_error | 0.0381933 |
| no_buzz_brier | 0.0200786 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.607404 | 0.698998 | 0.253628 | 0.248963 | 0.592039 | 0.76525 | -0.173211 | 0.163819 | 0.276685 | 0.529378 | 0.71466 | 0.223028 |
| tossup_correctness | tier | fall | 2933 | 0.607778 | 0.734678 | 0.304139 | 0.264176 | 0.55029 | 0.791681 | -0.241391 | 0.167767 | 0.237045 | 0.501454 | 0.697329 | 0.221699 |
| tossup_correctness | tier | nationals | 1584 | 0.583746 | 0.667487 | 0.183303 | 0.236546 | 0.609848 | 0.724747 | -0.114899 | 0.146701 | 0.33504 | 0.556597 | 0.720066 | 0.226568 |
| tossup_correctness | tier | regionals | 1886 | 0.633274 | 0.685874 | 0.232092 | 0.24292 | 0.610817 | 0.746023 | -0.135207 | 0.171118 | 0.276341 | 0.533118 | 0.729392 | 0.220524 |
| tossup_correctness | tier | winter | 2892 | 0.618814 | 0.688631 | 0.256206 | 0.244275 | 0.612379 | 0.773167 | -0.160788 | 0.160132 | 0.294337 | 0.533712 | 0.716507 | 0.22407 |
| tossup_correctness | category | Current Events | 124 | 0.591398 | 0.775605 | 0.297176 | 0.2825 | 0.516129 | 0.75 | -0.233871 | 0.166912 | 0.228368 | 0.472802 | 0.671067 | 0.220492 |
| tossup_correctness | category | Fine Arts | 1103 | 0.602508 | 0.692225 | 0.241768 | 0.245907 | 0.592928 | 0.759746 | -0.166818 | 0.165299 | 0.271856 | 0.545172 | 0.714673 | 0.222353 |
| tossup_correctness | category | Geography | 197 | 0.550583 | 0.78537 | 0.228726 | 0.28788 | 0.532995 | 0.670051 | -0.137056 | 0.164585 | 0.212288 | 0.458371 | 0.653113 | 0.219469 |
| tossup_correctness | category | History | 1491 | 0.615438 | 0.709067 | 0.291877 | 0.254924 | 0.568075 | 0.787391 | -0.219316 | 0.154363 | 0.279014 | 0.508297 | 0.692505 | 0.226152 |
| tossup_correctness | category | Literature | 1472 | 0.576659 | 0.674192 | 0.260927 | 0.237041 | 0.627038 | 0.804348 | -0.17731 | 0.156566 | 0.325677 | 0.563128 | 0.731951 | 0.223481 |
| tossup_correctness | category | Mythology | 332 | 0.58184 | 0.715339 | 0.30265 | 0.255414 | 0.593373 | 0.813253 | -0.21988 | 0.161335 | 0.269037 | 0.538182 | 0.69658 | 0.223851 |
| tossup_correctness | category | Other Academic | 69 | 0.561086 | 0.69277 | 0.249724 | 0.248714 | 0.57971 | 0.753623 | -0.173913 | 0.150813 | 0.299549 | 0.539779 | 0.675754 | 0.227029 |
| tossup_correctness | category | Philosophy | 324 | 0.583012 | 0.654397 | 0.240467 | 0.228827 | 0.623457 | 0.799383 | -0.175926 | 0.154348 | 0.347417 | 0.578496 | 0.736874 | 0.222706 |
| tossup_correctness | category | Popular Culture | 102 | 0.512803 | 0.923217 | 0.427413 | 0.34571 | 0.392157 | 0.833333 | -0.441176 | 0.166168 | 0.188148 | 0.409 | 0.62201 | 0.213537 |
| tossup_correctness | category | Religion | 372 | 0.611216 | 0.705111 | 0.207214 | 0.25163 | 0.599462 | 0.709677 | -0.110215 | 0.157846 | 0.276787 | 0.516705 | 0.704902 | 0.225079 |
| tossup_correctness | category | Science | 1487 | 0.603963 | 0.706966 | 0.246833 | 0.252327 | 0.576328 | 0.752522 | -0.176194 | 0.163086 | 0.284538 | 0.51783 | 0.706315 | 0.223371 |
| tossup_correctness | category | Social Science | 336 | 0.62928 | 0.698031 | 0.215077 | 0.249365 | 0.592262 | 0.702381 | -0.110119 | 0.159981 | 0.251724 | 0.506297 | 0.68822 | 0.224245 |
| tossup_correctness | category | Unknown | 1886 | 0.633274 | 0.685874 | 0.232092 | 0.24292 | 0.610817 | 0.746023 | -0.135207 | 0.171118 | 0.276341 | 0.533118 | 0.729392 | 0.220524 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.646419 | 0.783633 | 0.317241 | 0.286589 | 0.467005 | 0.736041 | -0.269036 | 0.153631 | 0.212701 | 0.425842 | 0.622043 | 0.220334 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.603395 | 0.769373 | 0.284904 | 0.279837 | 0.511675 | 0.735025 | -0.22335 | 0.158388 | 0.225012 | 0.456349 | 0.651183 | 0.222426 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.594812 | 0.726753 | 0.278656 | 0.26123 | 0.563749 | 0.769436 | -0.205686 | 0.158401 | 0.267908 | 0.509544 | 0.685109 | 0.224824 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.61621 | 0.694473 | 0.269826 | 0.246721 | 0.604327 | 0.78402 | -0.179693 | 0.163903 | 0.274871 | 0.533002 | 0.717102 | 0.222934 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.612002 | 0.653772 | 0.205083 | 0.229266 | 0.636182 | 0.756008 | -0.119826 | 0.158942 | 0.31849 | 0.569574 | 0.740072 | 0.222144 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | 0.202287 | 0.929995 | -2.20196 | -1.06884 | -0.491302 | 0.0448111 | 0.821709 | 1.93052 | 3.22311 |
| player | theta_2 | 1186 | 0.180641 | 0.875965 | -2.18062 | -1.11645 | -0.407907 | 0.0593327 | 0.721822 | 1.73444 | 3.23304 |
| player | theta_3 | 1186 | 0.631969 | 1.12938 | -2.21282 | -1.1792 | -0.276824 | 0.634015 | 1.48406 | 2.47603 | 3.33624 |
| player | theta_norm | 1186 | 1.66859 | 0.771034 | 0.0697439 | 0.533133 | 1.06877 | 1.59912 | 2.23059 | 3.0562 | 4.31973 |
| tossup | start_difficulty_d1 | 1240 | 1.54466 | 0.372689 | -0.194056 | 0.79809 | 1.38844 | 1.60577 | 1.77764 | 2.04668 | 2.52048 |
| tossup | start_difficulty_d2 | 1240 | 1.44912 | 0.449142 | -0.64344 | 0.594504 | 1.21356 | 1.49815 | 1.75142 | 2.08231 | 2.62386 |
| tossup | start_difficulty_d3 | 1240 | 1.60211 | 0.515743 | -0.0998663 | 0.60629 | 1.26196 | 1.69618 | 1.99467 | 2.28875 | 2.68935 |
| tossup | end_difficulty_d1 | 1240 | 0.331754 | 0.471064 | -2.42351 | -0.548897 | 0.139452 | 0.382746 | 0.632671 | 0.980758 | 1.38299 |
| tossup | end_difficulty_d2 | 1240 | 0.287481 | 0.559642 | -1.76484 | -0.768061 | 0.0095686 | 0.34062 | 0.668547 | 1.09337 | 1.93684 |
| tossup | end_difficulty_d3 | 1240 | 0.526783 | 0.562743 | -2.22032 | -0.534898 | 0.227116 | 0.607418 | 0.912464 | 1.30237 | 1.93125 |
| tossup | total_drop_d1 | 1240 | 1.21291 | 0.385871 | 0.489138 | 0.736313 | 0.928972 | 1.14742 | 1.42239 | 1.91359 | 3.5164 |
| tossup | total_drop_d2 | 1240 | 1.16164 | 0.425074 | 0.549191 | 0.694811 | 0.853859 | 1.02408 | 1.3864 | 2.01852 | 3.37354 |
| tossup | total_drop_d3 | 1240 | 1.07533 | 0.38438 | 0.449209 | 0.681225 | 0.807724 | 0.939747 | 1.25311 | 1.82725 | 3.10703 |
| tossup | drop_share_1_d1 | 1240 | 0.187833 | 0.0636633 | 0.0526728 | 0.0987008 | 0.135347 | 0.176111 | 0.24036 | 0.294381 | 0.398676 |
| tossup | drop_share_2_d1 | 1240 | 0.264516 | 0.0762003 | 0.0770872 | 0.133477 | 0.204281 | 0.271386 | 0.3269 | 0.366267 | 0.608057 |
| tossup | drop_share_3_d1 | 1240 | 0.547651 | 0.130859 | 0.209665 | 0.363106 | 0.428725 | 0.546484 | 0.65473 | 0.759454 | 0.863624 |
| tossup | drop_share_1_d2 | 1240 | 0.209889 | 0.0629708 | 0.0614253 | 0.103531 | 0.159718 | 0.217858 | 0.262728 | 0.299578 | 0.347292 |
| tossup | drop_share_2_d2 | 1240 | 0.283184 | 0.0677944 | 0.0822149 | 0.150714 | 0.239647 | 0.302759 | 0.332522 | 0.362089 | 0.606207 |
| tossup | drop_share_3_d2 | 1240 | 0.506927 | 0.123169 | 0.22924 | 0.362809 | 0.404177 | 0.472044 | 0.601207 | 0.736707 | 0.846796 |
| tossup | drop_share_1_d3 | 1240 | 0.212002 | 0.0718607 | 0.0388542 | 0.0857753 | 0.153523 | 0.234419 | 0.266976 | 0.297915 | 0.527222 |
| tossup | drop_share_2_d3 | 1240 | 0.287698 | 0.0760665 | 0.0540144 | 0.132303 | 0.249093 | 0.315235 | 0.333932 | 0.364954 | 0.649762 |
| tossup | drop_share_3_d3 | 1240 | 0.5003 | 0.135161 | 0.159273 | 0.363757 | 0.39991 | 0.44594 | 0.585421 | 0.77593 | 0.902665 |
| tossup | r_1 | 1240 | 0.379555 | 0.232293 | 0.0169893 | 0.0524363 | 0.167016 | 0.367955 | 0.580115 | 0.754149 | 0.919469 |
| tossup | r_2 | 1240 | 0.252401 | 0.159341 | 0.0244888 | 0.0470427 | 0.129796 | 0.217719 | 0.352213 | 0.553001 | 0.795432 |
| tossup | r_3 | 1240 | 0.368044 | 0.255331 | 0.0261215 | 0.0583717 | 0.12993 | 0.286675 | 0.597829 | 0.800196 | 0.90778 |
| tossup | r_norm | 1240 | 0.694817 | 0.0698904 | 0.578171 | 0.600029 | 0.64199 | 0.682566 | 0.737557 | 0.831376 | 0.92128 |
