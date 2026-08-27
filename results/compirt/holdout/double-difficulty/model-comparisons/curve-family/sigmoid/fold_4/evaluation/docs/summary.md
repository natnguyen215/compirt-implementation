# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 296995 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.671743 |
| log_loss | 0.541486 |
| ece | 0.116437 |
| brier | 0.181282 |
| accuracy | 0.731176 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0421791 |
| probability_std | 0.177491 |
| probability_p10 | 0.410121 |
| probability_p50 | 0.67159 |
| probability_p90 | 0.889731 |
| mean_predictive_variance | 0.193392 |
| integrated_brier_score | 0.102993 |
| joint_tossup_event_log_loss | 6.7055 |
| buzz_position_mae | 0.156255 |
| buzz_position_median_absolute_error | 0.138971 |
| buzz_position_bias | -0.0589967 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.328695 |
| first_buzzer_mean_reciprocal_rank | 0.539053 |
| first_buzzer_log_loss | 1.74724 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.671743 |
| neg_average_precision | 0.384671 |
| neg_precision | 0.39551 |
| neg_recall | 0.352213 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.15786 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.00609846 |
| no_buzz_calibration_error | -0.00562862 |
| no_buzz_brier | 0.0108443 |
| full_pmf_max_mass_error | 1.11022e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.671743 | 0.541486 | 0.116437 | 0.181282 | 0.731176 | 0.773355 | -0.0421791 | 0.177491 | 0.410121 | 0.67159 | 0.889731 | 0.193392 |
| tossup_correctness | tier | fall | 2876 | 0.680746 | 0.512136 | 0.106073 | 0.168882 | 0.756259 | 0.793115 | -0.0368567 | 0.187113 | 0.420972 | 0.716203 | 0.914791 | 0.178855 |
| tossup_correctness | tier | nationals | 1579 | 0.657214 | 0.571988 | 0.0937325 | 0.193463 | 0.721976 | 0.729576 | -0.00759975 | 0.137097 | 0.448826 | 0.648298 | 0.80289 | 0.212699 |
| tossup_correctness | tier | regionals | 1990 | 0.689766 | 0.553702 | 0.140492 | 0.186447 | 0.717588 | 0.765829 | -0.0482412 | 0.170433 | 0.382949 | 0.638905 | 0.843008 | 0.205243 |
| tossup_correctness | tier | winter | 2825 | 0.656286 | 0.545712 | 0.124992 | 0.183459 | 0.720354 | 0.783009 | -0.0626549 | 0.186221 | 0.404275 | 0.676341 | 0.903875 | 0.189054 |
| tossup_correctness | category | Current Events | 123 | 0.710198 | 0.533663 | 0.148927 | 0.182341 | 0.715447 | 0.764228 | -0.0487805 | 0.180994 | 0.420455 | 0.588291 | 0.901332 | 0.20185 |
| tossup_correctness | category | Fine Arts | 1093 | 0.681303 | 0.534462 | 0.107151 | 0.178398 | 0.748399 | 0.769442 | -0.021043 | 0.177119 | 0.419208 | 0.680908 | 0.898032 | 0.191072 |
| tossup_correctness | category | Geography | 191 | 0.75077 | 0.542884 | 0.103084 | 0.182195 | 0.727749 | 0.691099 | 0.0366492 | 0.20475 | 0.317047 | 0.640069 | 0.847896 | 0.196957 |
| tossup_correctness | category | History | 1469 | 0.673073 | 0.546466 | 0.0904797 | 0.184242 | 0.704561 | 0.758339 | -0.0537781 | 0.180001 | 0.41863 | 0.681283 | 0.896292 | 0.189423 |
| tossup_correctness | category | Literature | 1436 | 0.643076 | 0.50425 | 0.119077 | 0.163923 | 0.779944 | 0.81546 | -0.0355153 | 0.16759 | 0.463854 | 0.73025 | 0.908997 | 0.18004 |
| tossup_correctness | category | Mythology | 325 | 0.586232 | 0.508049 | 0.155015 | 0.168259 | 0.753846 | 0.843077 | -0.0892308 | 0.162746 | 0.485372 | 0.697853 | 0.908281 | 0.184941 |
| tossup_correctness | category | Other Academic | 67 | 0.597035 | 0.601088 | 0.191397 | 0.207271 | 0.671642 | 0.791045 | -0.119403 | 0.139147 | 0.43006 | 0.594715 | 0.767188 | 0.220708 |
| tossup_correctness | category | Philosophy | 322 | 0.691356 | 0.52878 | 0.135818 | 0.173993 | 0.776398 | 0.785714 | -0.00931677 | 0.165968 | 0.439985 | 0.654614 | 0.883947 | 0.197292 |
| tossup_correctness | category | Popular Culture | 100 | 0.574055 | 0.404007 | 0.129389 | 0.121701 | 0.85 | 0.89 | -0.04 | 0.143548 | 0.601607 | 0.834497 | 0.937093 | 0.142473 |
| tossup_correctness | category | Religion | 365 | 0.597697 | 0.62628 | 0.135046 | 0.216615 | 0.673973 | 0.723288 | -0.0493151 | 0.17533 | 0.394891 | 0.618912 | 0.869027 | 0.203512 |
| tossup_correctness | category | Science | 1456 | 0.657252 | 0.554392 | 0.126203 | 0.186975 | 0.716346 | 0.76717 | -0.0508242 | 0.179503 | 0.405112 | 0.660697 | 0.891598 | 0.195065 |
| tossup_correctness | category | Social Science | 333 | 0.69209 | 0.557073 | 0.102308 | 0.189573 | 0.708709 | 0.72973 | -0.021021 | 0.18742 | 0.369039 | 0.644684 | 0.887089 | 0.195977 |
| tossup_correctness | category | Unknown | 1990 | 0.689766 | 0.553702 | 0.140492 | 0.186447 | 0.717588 | 0.765829 | -0.0482412 | 0.170433 | 0.382949 | 0.638905 | 0.843008 | 0.205243 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.710945 | 0.500299 | 0.0818367 | 0.161878 | 0.782123 | 0.748603 | 0.0335196 | 0.184956 | 0.473584 | 0.783417 | 0.921486 | 0.161319 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.679643 | 0.521807 | 0.0663369 | 0.169402 | 0.77534 | 0.754441 | 0.0208986 | 0.172087 | 0.483728 | 0.766534 | 0.926111 | 0.167567 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.70486 | 0.507965 | 0.0670309 | 0.167093 | 0.759419 | 0.766682 | -0.00726282 | 0.180302 | 0.447204 | 0.729219 | 0.914491 | 0.176246 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.684914 | 0.52521 | 0.125843 | 0.174648 | 0.740094 | 0.787441 | -0.0473472 | 0.175056 | 0.416037 | 0.680275 | 0.885929 | 0.19322 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.643009 | 0.591782 | 0.177545 | 0.203584 | 0.683711 | 0.771758 | -0.0880461 | 0.156371 | 0.383606 | 0.598505 | 0.794768 | 0.216672 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 4.0279 | 0.555981 | 1.9874 | 3.10781 | 3.6536 | 4.04699 | 4.43254 | 4.9047 | 5.53228 |
| player | theta_1 | 1196 | -0.353914 | 1.06858 | -2.76575 | -1.92283 | -1.17193 | -0.473959 | 0.378834 | 1.53798 | 2.82341 |
| player | theta_2 | 1196 | -0.525799 | 0.722835 | -2.47784 | -1.6008 | -1.04996 | -0.575911 | -0.042128 | 0.749999 | 2.32217 |
| player | theta_3 | 1196 | -0.432361 | 0.705833 | -2.60985 | -1.58656 | -0.942168 | -0.430699 | 0.0577143 | 0.756285 | 1.5778 |
| player | theta_norm | 1196 | 1.53336 | 0.631294 | 0.114855 | 0.561693 | 1.06774 | 1.51014 | 1.95453 | 2.621 | 3.61699 |
| tossup | beta_1 | 1240 | -0.601241 | 0.759711 | -3.51714 | -2.39429 | -0.785978 | -0.337811 | -0.137663 | 0.146329 | 0.866573 |
| tossup | beta_2 | 1240 | -0.419877 | 0.676742 | -3.50921 | -2.23896 | -0.390738 | -0.231085 | -0.125994 | 0.109095 | 2.10328 |
| tossup | beta_3 | 1240 | -0.448401 | 0.693165 | -3.23627 | -2.36273 | -0.406576 | -0.237005 | -0.134359 | 0.117161 | 1.36475 |
| tossup | gamma_1 | 1240 | 5.53222 | 4.01776 | 0.53559 | 2.93965 | 4.37335 | 4.80615 | 5.19518 | 12.4838 | 72.0091 |
| tossup | gamma_2 | 1240 | 5.49721 | 3.27417 | 0.543086 | 4.00845 | 4.64272 | 4.89105 | 5.19289 | 9.40445 | 41.3867 |
| tossup | gamma_3 | 1240 | 5.42769 | 3.00187 | 0.341572 | 3.86468 | 4.64596 | 4.90335 | 5.1794 | 9.07351 | 43.3425 |
| tossup | mu_1 | 1240 | 0.560986 | 0.118534 | 0.44267 | 0.475021 | 0.495031 | 0.511622 | 0.560398 | 0.873762 | 0.969185 |
| tossup | mu_2 | 1240 | 0.539333 | 0.105075 | 0.450471 | 0.477797 | 0.494035 | 0.505753 | 0.520358 | 0.85032 | 0.971648 |
| tossup | mu_3 | 1240 | 0.542874 | 0.109217 | 0.446877 | 0.476875 | 0.493124 | 0.506149 | 0.521925 | 0.865212 | 0.978007 |
| tossup | r_1 | 1240 | 0.411578 | 0.245275 | 0.0416088 | 0.0759421 | 0.181914 | 0.379676 | 0.644454 | 0.799138 | 0.875345 |
| tossup | r_2 | 1240 | 0.286345 | 0.213972 | 0.0447815 | 0.0703135 | 0.128136 | 0.210362 | 0.374477 | 0.779688 | 0.896931 |
| tossup | r_3 | 1240 | 0.302076 | 0.214473 | 0.0469679 | 0.079578 | 0.141626 | 0.233363 | 0.396965 | 0.812427 | 0.898244 |
| tossup | r_norm | 1240 | 0.697535 | 0.0889483 | 0.577388 | 0.584454 | 0.617252 | 0.681917 | 0.76975 | 0.856789 | 0.901126 |
| tossup_hazard | hazard_beta_1 | 1240 | 2.05912 | 1.53449 | -0.0857487 | 0.426462 | 0.659474 | 1.37794 | 3.65487 | 4.54631 | 5.21952 |
| tossup_hazard | hazard_beta_2 | 1240 | 1.94215 | 1.31734 | 0.132392 | 0.391701 | 0.706528 | 1.49496 | 3.30391 | 4.04289 | 5.11817 |
| tossup_hazard | hazard_beta_3 | 1240 | 1.74659 | 1.29192 | -0.104097 | 0.400068 | 0.687454 | 1.1804 | 2.94744 | 4.04575 | 4.84108 |
| tossup_hazard | hazard_gamma_1 | 1240 | 13.2291 | 33.192 | 2.9586 | 5.49364 | 6.27221 | 7.38924 | 10.9731 | 33.488 | 987.164 |
| tossup_hazard | hazard_gamma_2 | 1240 | 14.2362 | 22.7572 | 3.24072 | 5.51037 | 6.33172 | 8.05252 | 12.8268 | 40.508 | 315.095 |
| tossup_hazard | hazard_gamma_3 | 1240 | 13.8364 | 32.0402 | 2.72817 | 5.51106 | 6.29568 | 7.46996 | 10.9273 | 32.3068 | 577.624 |
| tossup_hazard | hazard_mu_1 | 1240 | 0.604784 | 0.109057 | 0.255311 | 0.48219 | 0.531536 | 0.566964 | 0.667029 | 0.828237 | 0.947814 |
| tossup_hazard | hazard_mu_2 | 1240 | 0.59972 | 0.109138 | 0.20937 | 0.472543 | 0.526356 | 0.567665 | 0.659106 | 0.821899 | 0.943147 |
| tossup_hazard | hazard_mu_3 | 1240 | 0.594362 | 0.097079 | 0.330646 | 0.484079 | 0.528884 | 0.56572 | 0.640023 | 0.796617 | 0.935804 |
| tossup_hazard | hazard_r_1 | 1240 | 0.352897 | 0.353111 | 0.0201 | 0.0334715 | 0.0523261 | 0.142752 | 0.769127 | 0.918365 | 0.96354 |
| tossup_hazard | hazard_r_2 | 1240 | 0.35923 | 0.340077 | 0.00836061 | 0.024496 | 0.0610431 | 0.167554 | 0.743882 | 0.90607 | 0.951523 |
| tossup_hazard | hazard_r_3 | 1240 | 0.287873 | 0.309942 | 0.0160068 | 0.0301509 | 0.0545116 | 0.111627 | 0.551606 | 0.876325 | 0.928257 |
