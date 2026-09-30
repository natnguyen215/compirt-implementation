# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 300762 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.595436 |
| log_loss | 0.640015 |
| ece | 0.197288 |
| brier | 0.22416 |
| accuracy | 0.643132 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.118993 |
| probability_std | 0.148767 |
| probability_p10 | 0.351152 |
| probability_p50 | 0.586549 |
| probability_p90 | 0.745557 |
| mean_predictive_variance | 0.223664 |
| integrated_brier_score | 0.0933036 |
| joint_tossup_event_log_loss | 6.64596 |
| buzz_position_mae | 0.135419 |
| buzz_position_median_absolute_error | 0.112394 |
| buzz_position_bias | 0.000442197 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.382052 |
| first_buzzer_mean_reciprocal_rank | 0.590099 |
| first_buzzer_log_loss | 1.61611 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.595436 |
| neg_average_precision | 0.306222 |
| neg_precision | 0.310971 |
| neg_recall | 0.411466 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.140273 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.050312 |
| no_buzz_calibration_error | 0.0344029 |
| no_buzz_brier | 0.0221703 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.595436 | 0.640015 | 0.197288 | 0.22416 | 0.643132 | 0.762125 | -0.118993 | 0.148767 | 0.351152 | 0.586549 | 0.745557 | 0.223664 |
| tossup_correctness | tier | fall | 2842 | 0.606806 | 0.630132 | 0.221629 | 0.219918 | 0.654469 | 0.785362 | -0.130894 | 0.146858 | 0.355235 | 0.577406 | 0.749346 | 0.224371 |
| tossup_correctness | tier | nationals | 1564 | 0.599469 | 0.625522 | 0.130108 | 0.217323 | 0.664322 | 0.718031 | -0.0537084 | 0.135126 | 0.401568 | 0.606291 | 0.749912 | 0.223861 |
| tossup_correctness | tier | regionals | 1937 | 0.602915 | 0.63392 | 0.185354 | 0.221149 | 0.653072 | 0.758389 | -0.105318 | 0.153109 | 0.34495 | 0.600933 | 0.750902 | 0.221223 |
| tossup_correctness | tier | winter | 2750 | 0.586075 | 0.662765 | 0.219228 | 0.234553 | 0.612364 | 0.765818 | -0.153455 | 0.1526 | 0.323563 | 0.569455 | 0.731523 | 0.224542 |
| tossup_correctness | category | Current Events | 126 | 0.579097 | 0.69498 | 0.256738 | 0.249815 | 0.555556 | 0.769841 | -0.214286 | 0.147465 | 0.297433 | 0.516771 | 0.696662 | 0.228083 |
| tossup_correctness | category | Fine Arts | 1071 | 0.604546 | 0.627742 | 0.191463 | 0.218547 | 0.662932 | 0.766573 | -0.103641 | 0.155868 | 0.357992 | 0.600569 | 0.754964 | 0.220064 |
| tossup_correctness | category | Geography | 185 | 0.572398 | 0.703979 | 0.200699 | 0.254276 | 0.545946 | 0.697297 | -0.151351 | 0.140147 | 0.311852 | 0.521204 | 0.668494 | 0.230346 |
| tossup_correctness | category | History | 1440 | 0.571118 | 0.646713 | 0.189946 | 0.227527 | 0.625694 | 0.754167 | -0.128472 | 0.13971 | 0.365943 | 0.582609 | 0.735535 | 0.226357 |
| tossup_correctness | category | Literature | 1422 | 0.5835 | 0.59784 | 0.209594 | 0.204333 | 0.707454 | 0.814346 | -0.106892 | 0.151277 | 0.390784 | 0.632578 | 0.777011 | 0.216142 |
| tossup_correctness | category | Mythology | 318 | 0.571564 | 0.651935 | 0.23432 | 0.229664 | 0.628931 | 0.789308 | -0.160377 | 0.141435 | 0.346393 | 0.576799 | 0.717379 | 0.226973 |
| tossup_correctness | category | Other Academic | 66 | 0.786114 | 0.588007 | 0.184392 | 0.199913 | 0.69697 | 0.712121 | -0.0151515 | 0.137114 | 0.391662 | 0.538478 | 0.700147 | 0.23004 |
| tossup_correctness | category | Philosophy | 311 | 0.600502 | 0.636248 | 0.17136 | 0.222918 | 0.633441 | 0.745981 | -0.11254 | 0.148834 | 0.367583 | 0.601705 | 0.748971 | 0.22228 |
| tossup_correctness | category | Popular Culture | 102 | 0.425926 | 0.764576 | 0.392577 | 0.282249 | 0.5 | 0.882353 | -0.382353 | 0.147499 | 0.28644 | 0.501326 | 0.684937 | 0.228219 |
| tossup_correctness | category | Religion | 358 | 0.588768 | 0.655754 | 0.159178 | 0.23188 | 0.592179 | 0.712291 | -0.120112 | 0.143311 | 0.347962 | 0.566369 | 0.736922 | 0.226641 |
| tossup_correctness | category | Science | 1433 | 0.601774 | 0.663565 | 0.205445 | 0.234934 | 0.618981 | 0.738311 | -0.11933 | 0.13771 | 0.33891 | 0.544003 | 0.706772 | 0.229956 |
| tossup_correctness | category | Social Science | 324 | 0.589747 | 0.656212 | 0.185042 | 0.231858 | 0.623457 | 0.731481 | -0.108025 | 0.133568 | 0.355645 | 0.557247 | 0.712489 | 0.229912 |
| tossup_correctness | category | Unknown | 1937 | 0.602915 | 0.63392 | 0.185354 | 0.221149 | 0.653072 | 0.758389 | -0.105318 | 0.153109 | 0.34495 | 0.600933 | 0.750902 | 0.221223 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.547094 | 0.70867 | 0.20793 | 0.25548 | 0.556886 | 0.712575 | -0.155689 | 0.151206 | 0.277806 | 0.543925 | 0.697823 | 0.226892 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.582862 | 0.684876 | 0.207962 | 0.244633 | 0.600877 | 0.729167 | -0.128289 | 0.148558 | 0.31355 | 0.537777 | 0.701336 | 0.227448 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.632445 | 0.640935 | 0.206101 | 0.22411 | 0.653428 | 0.755083 | -0.101655 | 0.148298 | 0.334564 | 0.568738 | 0.72555 | 0.225608 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.581951 | 0.639415 | 0.212726 | 0.223851 | 0.644163 | 0.780942 | -0.136779 | 0.146925 | 0.35311 | 0.591685 | 0.746088 | 0.22376 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.587555 | 0.622792 | 0.173872 | 0.216659 | 0.652373 | 0.762029 | -0.109656 | 0.145959 | 0.378362 | 0.612201 | 0.762303 | 0.220924 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | 0.280465 | 0.96879 | -2.13209 | -1.12457 | -0.505359 | 0.173953 | 0.994975 | 2.01263 | 3.0308 |
| player | theta_2 | 1167 | 0.48193 | 0.9564 | -1.55498 | -0.855808 | -0.283774 | 0.400399 | 1.15155 | 2.23146 | 3.40076 |
| player | theta_3 | 1167 | 0.177778 | 0.769481 | -1.64348 | -0.925388 | -0.40396 | 0.0963757 | 0.691396 | 1.53563 | 2.82931 |
| player | alpha_1 | 1167 | 7.84213 | 4.02348 | 0.766423 | 2.32982 | 5.01768 | 7.27486 | 9.95764 | 14.9822 | 26.7237 |
| player | alpha_2 | 1167 | 10.4438 | 5.06007 | 1.90751 | 4.71094 | 7.15086 | 9.63246 | 12.4518 | 19.0228 | 42.4008 |
| player | alpha_3 | 1167 | 6.43424 | 4.21539 | 0.70048 | 1.52473 | 3.55677 | 5.55119 | 8.31156 | 14.5803 | 35.9569 |
| player | beta_1 | 1167 | -1.67148 | 0.60066 | -4.0736 | -2.66087 | -2.06832 | -1.62125 | -1.22992 | -0.767008 | -0.244348 |
| player | beta_2 | 1167 | -1.5889 | 0.581759 | -3.71531 | -2.59133 | -1.99286 | -1.55786 | -1.16795 | -0.704444 | -0.280177 |
| player | beta_3 | 1167 | -1.46078 | 0.636187 | -3.52546 | -2.63146 | -1.86831 | -1.38288 | -0.97262 | -0.54668 | -0.0683155 |
| player | theta_norm | 1167 | 1.51165 | 0.707905 | 0.0527786 | 0.519514 | 0.962277 | 1.42153 | 2.00946 | 2.81946 | 4.05232 |
| tossup | start_difficulty_d1 | 1220 | 1.09981 | 0.330333 | -0.316673 | 0.513201 | 0.90663 | 1.12574 | 1.32822 | 1.58982 | 2.06115 |
| tossup | start_difficulty_d2 | 1220 | 1.2408 | 0.30056 | -0.419512 | 0.764625 | 1.07669 | 1.23532 | 1.42081 | 1.7281 | 2.27696 |
| tossup | start_difficulty_d3 | 1220 | 1.04869 | 0.375615 | -0.436902 | 0.306787 | 0.852306 | 1.11283 | 1.2968 | 1.55398 | 1.99405 |
| tossup | end_difficulty_d1 | 1220 | 0.0600643 | 0.434109 | -1.98259 | -0.824614 | -0.131036 | 0.136024 | 0.340632 | 0.645556 | 1.15814 |
| tossup | end_difficulty_d2 | 1220 | 0.334944 | 0.369561 | -1.49736 | -0.326441 | 0.159461 | 0.343143 | 0.545087 | 0.91768 | 1.59141 |
| tossup | end_difficulty_d3 | 1220 | 0.0519322 | 0.520609 | -2.44108 | -0.959802 | -0.187854 | 0.151012 | 0.393619 | 0.716859 | 1.22505 |
| tossup | total_drop_d1 | 1220 | 1.03975 | 0.31025 | 0.377813 | 0.646139 | 0.817315 | 0.981239 | 1.20123 | 1.60458 | 2.64741 |
| tossup | total_drop_d2 | 1220 | 0.905859 | 0.243332 | 0.359539 | 0.596999 | 0.743142 | 0.857991 | 1.03318 | 1.37824 | 2.21391 |
| tossup | total_drop_d3 | 1220 | 0.996753 | 0.323414 | 0.434864 | 0.642864 | 0.783811 | 0.923449 | 1.10791 | 1.65485 | 2.70209 |
| tossup | drop_share_1_d1 | 1220 | 0.221403 | 0.0781715 | 0.0553803 | 0.11425 | 0.162677 | 0.215401 | 0.266175 | 0.353804 | 0.579206 |
| tossup | drop_share_2_d1 | 1220 | 0.25827 | 0.0654481 | 0.0799646 | 0.14904 | 0.212612 | 0.260961 | 0.308737 | 0.351378 | 0.536614 |
| tossup | drop_share_3_d1 | 1220 | 0.520327 | 0.127526 | 0.152937 | 0.329734 | 0.423165 | 0.512589 | 0.614089 | 0.728848 | 0.864655 |
| tossup | drop_share_1_d2 | 1220 | 0.221058 | 0.068636 | 0.0718794 | 0.121555 | 0.173443 | 0.215675 | 0.259337 | 0.333037 | 0.604834 |
| tossup | drop_share_2_d2 | 1220 | 0.259549 | 0.0649437 | 0.0578593 | 0.141628 | 0.213397 | 0.26866 | 0.309766 | 0.346191 | 0.487585 |
| tossup | drop_share_3_d2 | 1220 | 0.519394 | 0.113258 | 0.156687 | 0.356612 | 0.434862 | 0.506058 | 0.600465 | 0.715289 | 0.86511 |
| tossup | drop_share_1_d3 | 1220 | 0.232682 | 0.0597952 | 0.0638664 | 0.128519 | 0.193345 | 0.23795 | 0.273905 | 0.320178 | 0.523323 |
| tossup | drop_share_2_d3 | 1220 | 0.282213 | 0.054929 | 0.0798192 | 0.174658 | 0.252586 | 0.293424 | 0.321712 | 0.350023 | 0.417048 |
| tossup | drop_share_3_d3 | 1220 | 0.485105 | 0.104557 | 0.252882 | 0.354031 | 0.401796 | 0.465379 | 0.547189 | 0.695721 | 0.856314 |
| tossup | r_1 | 1220 | 0.352288 | 0.175527 | 0.0309629 | 0.0819255 | 0.202086 | 0.357694 | 0.482189 | 0.636989 | 0.821227 |
| tossup | r_2 | 1220 | 0.386086 | 0.180152 | 0.0297738 | 0.0977697 | 0.26059 | 0.373506 | 0.499285 | 0.721628 | 0.925493 |
| tossup | r_3 | 1220 | 0.261626 | 0.141874 | 0.0291382 | 0.075585 | 0.141781 | 0.244253 | 0.358663 | 0.524629 | 0.667668 |
| tossup | r_norm | 1220 | 0.649532 | 0.0552487 | 0.577353 | 0.582928 | 0.607633 | 0.639858 | 0.674196 | 0.760451 | 0.926996 |
