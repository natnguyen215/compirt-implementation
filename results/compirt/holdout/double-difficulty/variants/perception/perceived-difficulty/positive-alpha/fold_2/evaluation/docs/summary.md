# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299647 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.598231 |
| log_loss | 0.638274 |
| ece | 0.199603 |
| brier | 0.223357 |
| accuracy | 0.64751 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.116668 |
| probability_std | 0.149097 |
| probability_p10 | 0.348333 |
| probability_p50 | 0.585101 |
| probability_p90 | 0.744333 |
| mean_predictive_variance | 0.2236 |
| integrated_brier_score | 0.0956429 |
| joint_tossup_event_log_loss | 6.63045 |
| buzz_position_mae | 0.13762 |
| buzz_position_median_absolute_error | 0.113412 |
| buzz_position_bias | 0.00516905 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.393216 |
| first_buzzer_mean_reciprocal_rank | 0.599262 |
| first_buzzer_log_loss | 1.58717 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.598231 |
| neg_average_precision | 0.311021 |
| neg_precision | 0.31237 |
| neg_recall | 0.411819 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.140748 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0484989 |
| no_buzz_calibration_error | 0.0353859 |
| no_buzz_brier | 0.0195912 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.598231 | 0.638274 | 0.199603 | 0.223357 | 0.64751 | 0.764178 | -0.116668 | 0.149097 | 0.348333 | 0.585101 | 0.744333 | 0.2236 |
| tossup_correctness | tier | fall | 2798 | 0.613022 | 0.644918 | 0.235812 | 0.226623 | 0.637598 | 0.785204 | -0.147605 | 0.15397 | 0.326829 | 0.564785 | 0.739661 | 0.223854 |
| tossup_correctness | tier | nationals | 1545 | 0.583892 | 0.633365 | 0.135011 | 0.221262 | 0.653074 | 0.721036 | -0.0679612 | 0.135711 | 0.396886 | 0.604073 | 0.74937 | 0.224182 |
| tossup_correctness | tier | regionals | 2039 | 0.603588 | 0.633804 | 0.188153 | 0.220981 | 0.658166 | 0.762138 | -0.103973 | 0.15781 | 0.342418 | 0.602382 | 0.762707 | 0.219622 |
| tossup_correctness | tier | winter | 2875 | 0.600893 | 0.637615 | 0.207196 | 0.222989 | 0.646609 | 0.768348 | -0.121739 | 0.142825 | 0.352976 | 0.582467 | 0.729605 | 0.225861 |
| tossup_correctness | category | Current Events | 129 | 0.589778 | 0.679605 | 0.147732 | 0.242453 | 0.573643 | 0.666667 | -0.0930233 | 0.15325 | 0.304011 | 0.564975 | 0.716395 | 0.225657 |
| tossup_correctness | category | Fine Arts | 1074 | 0.569469 | 0.646382 | 0.210149 | 0.227197 | 0.630354 | 0.776536 | -0.146182 | 0.152197 | 0.343781 | 0.59293 | 0.747812 | 0.222429 |
| tossup_correctness | category | Geography | 180 | 0.518214 | 0.71303 | 0.126458 | 0.257893 | 0.538889 | 0.616667 | -0.0777778 | 0.135916 | 0.33487 | 0.535074 | 0.68796 | 0.230911 |
| tossup_correctness | category | History | 1454 | 0.589875 | 0.637305 | 0.193328 | 0.223076 | 0.644429 | 0.757909 | -0.11348 | 0.138472 | 0.365638 | 0.58362 | 0.730622 | 0.226655 |
| tossup_correctness | category | Literature | 1435 | 0.596647 | 0.591988 | 0.206348 | 0.20214 | 0.708014 | 0.810453 | -0.102439 | 0.14981 | 0.380386 | 0.634528 | 0.774526 | 0.216719 |
| tossup_correctness | category | Mythology | 324 | 0.595737 | 0.642429 | 0.239977 | 0.225695 | 0.632716 | 0.79321 | -0.160494 | 0.141063 | 0.361545 | 0.565426 | 0.725507 | 0.227268 |
| tossup_correctness | category | Other Academic | 71 | 0.456427 | 0.670329 | 0.22804 | 0.238811 | 0.577465 | 0.760563 | -0.183099 | 0.137302 | 0.388739 | 0.586484 | 0.729956 | 0.22645 |
| tossup_correctness | category | Philosophy | 310 | 0.6112 | 0.611323 | 0.188458 | 0.211104 | 0.674194 | 0.76129 | -0.0870968 | 0.136646 | 0.395735 | 0.599775 | 0.74069 | 0.225183 |
| tossup_correctness | category | Popular Culture | 108 | 0.469618 | 0.767222 | 0.402559 | 0.282318 | 0.509259 | 0.888889 | -0.37963 | 0.14269 | 0.292551 | 0.501677 | 0.661368 | 0.229555 |
| tossup_correctness | category | Religion | 361 | 0.605481 | 0.648188 | 0.19573 | 0.228346 | 0.609418 | 0.742382 | -0.132964 | 0.139263 | 0.353284 | 0.55874 | 0.718208 | 0.228182 |
| tossup_correctness | category | Science | 1445 | 0.608301 | 0.667045 | 0.216162 | 0.236378 | 0.624221 | 0.746021 | -0.121799 | 0.141575 | 0.317397 | 0.546298 | 0.703882 | 0.229065 |
| tossup_correctness | category | Social Science | 327 | 0.651804 | 0.623284 | 0.167369 | 0.216797 | 0.669725 | 0.718654 | -0.0489297 | 0.141267 | 0.351272 | 0.570962 | 0.721076 | 0.2271 |
| tossup_correctness | category | Unknown | 2039 | 0.603588 | 0.633804 | 0.188153 | 0.220981 | 0.658166 | 0.762138 | -0.103973 | 0.15781 | 0.342418 | 0.602382 | 0.762707 | 0.219622 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.665676 | 0.688049 | 0.251158 | 0.245084 | 0.590164 | 0.743169 | -0.153005 | 0.157963 | 0.24376 | 0.501563 | 0.683632 | 0.224984 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.620324 | 0.667751 | 0.209771 | 0.23675 | 0.61466 | 0.728796 | -0.114136 | 0.150337 | 0.308761 | 0.536125 | 0.711396 | 0.226855 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.618688 | 0.646718 | 0.202595 | 0.227052 | 0.642251 | 0.752568 | -0.110317 | 0.152505 | 0.321915 | 0.573138 | 0.729325 | 0.224245 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.598771 | 0.630677 | 0.217603 | 0.21996 | 0.653217 | 0.786087 | -0.13287 | 0.146373 | 0.361942 | 0.588788 | 0.747588 | 0.223885 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.568493 | 0.626851 | 0.175151 | 0.218274 | 0.6599 | 0.764393 | -0.104493 | 0.142504 | 0.386273 | 0.610475 | 0.759852 | 0.221728 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | 0.289078 | 0.930071 | -1.81756 | -1.07454 | -0.43563 | 0.199762 | 0.94912 | 1.85705 | 2.87717 |
| player | theta_2 | 1197 | 0.490732 | 0.960637 | -1.89061 | -0.904087 | -0.266546 | 0.378151 | 1.21935 | 2.11726 | 3.24852 |
| player | theta_3 | 1197 | 0.177234 | 0.766117 | -1.73683 | -0.919565 | -0.416222 | 0.0912426 | 0.687214 | 1.56632 | 2.92341 |
| player | alpha_1 | 1197 | 7.79953 | 3.99526 | 0.602824 | 2.49959 | 5.20713 | 7.18824 | 9.67033 | 14.8733 | 34.4893 |
| player | alpha_2 | 1197 | 10.4731 | 5.02123 | 1.55108 | 4.77355 | 7.33316 | 9.60565 | 12.4831 | 18.576 | 42.4934 |
| player | alpha_3 | 1197 | 6.32653 | 3.73588 | 0.742222 | 1.63959 | 3.63144 | 5.65981 | 8.22063 | 13.4049 | 31.6428 |
| player | beta_1 | 1197 | -1.66772 | 0.585314 | -4.01465 | -2.68076 | -2.05426 | -1.62457 | -1.24635 | -0.790736 | -0.0252625 |
| player | beta_2 | 1197 | -1.60037 | 0.571403 | -3.44968 | -2.57132 | -1.98574 | -1.57218 | -1.22114 | -0.680903 | -0.0953622 |
| player | beta_3 | 1197 | -1.43899 | 0.59332 | -3.67445 | -2.51577 | -1.81937 | -1.38465 | -1.00391 | -0.57675 | -0.0991859 |
| player | theta_norm | 1197 | 1.49147 | 0.710317 | 0.158007 | 0.475231 | 0.930909 | 1.39549 | 1.98768 | 2.7606 | 3.93765 |
| tossup | start_difficulty_d1 | 1240 | 1.10725 | 0.314227 | -0.471983 | 0.560016 | 0.925146 | 1.12244 | 1.32324 | 1.59052 | 2.21047 |
| tossup | start_difficulty_d2 | 1240 | 1.24698 | 0.278603 | 0.0741353 | 0.816114 | 1.075 | 1.23604 | 1.41871 | 1.70702 | 2.18479 |
| tossup | start_difficulty_d3 | 1240 | 1.04054 | 0.359469 | -0.479971 | 0.405651 | 0.835154 | 1.07086 | 1.27655 | 1.57641 | 1.97853 |
| tossup | end_difficulty_d1 | 1240 | 0.0759709 | 0.41086 | -2.12748 | -0.725017 | -0.0872651 | 0.144944 | 0.330996 | 0.597678 | 1.29449 |
| tossup | end_difficulty_d2 | 1240 | 0.332888 | 0.339645 | -1.63215 | -0.232119 | 0.159612 | 0.334437 | 0.524634 | 0.868184 | 1.44053 |
| tossup | end_difficulty_d3 | 1240 | 0.0554201 | 0.487084 | -2.29612 | -0.878277 | -0.165556 | 0.126692 | 0.368559 | 0.711158 | 1.20818 |
| tossup | total_drop_d1 | 1240 | 1.03128 | 0.311227 | 0.375061 | 0.653335 | 0.821192 | 0.960515 | 1.17828 | 1.61574 | 2.7156 |
| tossup | total_drop_d2 | 1240 | 0.914087 | 0.245486 | 0.370287 | 0.596151 | 0.747209 | 0.868494 | 1.03837 | 1.39429 | 2.13958 |
| tossup | total_drop_d3 | 1240 | 0.985117 | 0.29656 | 0.44884 | 0.644441 | 0.780144 | 0.917127 | 1.11096 | 1.58077 | 2.66012 |
| tossup | drop_share_1_d1 | 1240 | 0.220597 | 0.0757859 | 0.0448283 | 0.11655 | 0.163668 | 0.212379 | 0.265841 | 0.353753 | 0.64952 |
| tossup | drop_share_2_d1 | 1240 | 0.259506 | 0.0637958 | 0.0826936 | 0.146589 | 0.217653 | 0.263622 | 0.307009 | 0.350233 | 0.54723 |
| tossup | drop_share_3_d1 | 1240 | 0.519897 | 0.124092 | 0.144578 | 0.338779 | 0.425222 | 0.511337 | 0.611125 | 0.73056 | 0.865528 |
| tossup | drop_share_1_d2 | 1240 | 0.220479 | 0.070374 | 0.0722017 | 0.121309 | 0.172439 | 0.213045 | 0.258649 | 0.341542 | 0.650233 |
| tossup | drop_share_2_d2 | 1240 | 0.257933 | 0.0639432 | 0.062227 | 0.141388 | 0.21724 | 0.2644 | 0.306751 | 0.346122 | 0.50214 |
| tossup | drop_share_3_d2 | 1240 | 0.521588 | 0.115183 | 0.127257 | 0.351535 | 0.437985 | 0.517919 | 0.60194 | 0.716716 | 0.834602 |
| tossup | drop_share_1_d3 | 1240 | 0.235002 | 0.0594406 | 0.0721366 | 0.134234 | 0.194342 | 0.23769 | 0.276582 | 0.321633 | 0.580481 |
| tossup | drop_share_2_d3 | 1240 | 0.283764 | 0.0528524 | 0.0832415 | 0.17887 | 0.255306 | 0.293971 | 0.320886 | 0.348839 | 0.43855 |
| tossup | drop_share_3_d3 | 1240 | 0.481235 | 0.101479 | 0.214589 | 0.351442 | 0.403822 | 0.461569 | 0.540783 | 0.673543 | 0.844622 |
| tossup | r_1 | 1240 | 0.353239 | 0.179126 | 0.0336951 | 0.0841638 | 0.202254 | 0.35515 | 0.48767 | 0.650062 | 0.857188 |
| tossup | r_2 | 1240 | 0.393151 | 0.18036 | 0.039426 | 0.0980449 | 0.264436 | 0.385859 | 0.514628 | 0.723913 | 0.923174 |
| tossup | r_3 | 1240 | 0.25361 | 0.141687 | 0.0332877 | 0.068572 | 0.139918 | 0.22645 | 0.346599 | 0.529975 | 0.659882 |
| tossup | r_norm | 1240 | 0.651995 | 0.0564908 | 0.577487 | 0.584773 | 0.610143 | 0.643819 | 0.674818 | 0.764962 | 0.924771 |
