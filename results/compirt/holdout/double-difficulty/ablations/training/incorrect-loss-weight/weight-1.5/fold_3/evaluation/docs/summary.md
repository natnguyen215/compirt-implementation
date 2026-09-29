# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-1.5/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-1.5/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 289503 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709342 |
| log_loss | 0.498123 |
| ece | 0.0618507 |
| brier | 0.162254 |
| accuracy | 0.773238 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00319383 |
| probability_std | 0.171978 |
| probability_p10 | 0.461333 |
| probability_p50 | 0.744939 |
| probability_p90 | 0.895415 |
| mean_predictive_variance | 0.177002 |
| integrated_brier_score | 0.101401 |
| joint_tossup_event_log_loss | 6.59926 |
| buzz_position_mae | 0.152138 |
| buzz_position_median_absolute_error | 0.136049 |
| buzz_position_bias | -0.0491965 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.352093 |
| first_buzzer_mean_reciprocal_rank | 0.567675 |
| first_buzzer_log_loss | 1.67235 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.709342 |
| neg_average_precision | 0.448278 |
| neg_precision | 0.51234 |
| neg_recall | 0.288314 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.183788 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0151345 |
| no_buzz_calibration_error | -4.99214e-05 |
| no_buzz_brier | 0.0137026 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.709342 | 0.498123 | 0.0618507 | 0.162254 | 0.773238 | 0.770044 | 0.00319383 | 0.171978 | 0.461333 | 0.744939 | 0.895415 | 0.177002 |
| tossup_correctness | tier | fall | 2817 | 0.701589 | 0.491561 | 0.0622898 | 0.159101 | 0.781328 | 0.781683 | -0.000354988 | 0.171122 | 0.460312 | 0.760203 | 0.902785 | 0.172532 |
| tossup_correctness | tier | nationals | 1542 | 0.726217 | 0.519018 | 0.0496558 | 0.171987 | 0.749676 | 0.73476 | 0.0149157 | 0.177356 | 0.427698 | 0.722281 | 0.885371 | 0.184281 |
| tossup_correctness | tier | regionals | 1934 | 0.713974 | 0.506084 | 0.0558612 | 0.16581 | 0.761117 | 0.75698 | 0.0041365 | 0.168812 | 0.463289 | 0.738336 | 0.891777 | 0.179555 |
| tossup_correctness | tier | winter | 2787 | 0.698617 | 0.487671 | 0.0748237 | 0.157589 | 0.786509 | 0.786868 | -0.000358809 | 0.170681 | 0.472962 | 0.751557 | 0.896666 | 0.175722 |
| tossup_correctness | category | Current Events | 125 | 0.747543 | 0.526431 | 0.0449383 | 0.177253 | 0.712 | 0.704 | 0.008 | 0.180452 | 0.418825 | 0.700455 | 0.886983 | 0.188362 |
| tossup_correctness | category | Fine Arts | 1072 | 0.722701 | 0.488574 | 0.0669601 | 0.15842 | 0.780784 | 0.770522 | 0.0102612 | 0.177176 | 0.447445 | 0.752715 | 0.895001 | 0.176039 |
| tossup_correctness | category | Geography | 185 | 0.777063 | 0.511133 | 0.112507 | 0.168509 | 0.772973 | 0.702703 | 0.0702703 | 0.223752 | 0.2905 | 0.673945 | 0.865437 | 0.185731 |
| tossup_correctness | category | History | 1443 | 0.730032 | 0.497917 | 0.0686096 | 0.163797 | 0.759529 | 0.765073 | -0.00554401 | 0.177692 | 0.432715 | 0.733997 | 0.893438 | 0.179828 |
| tossup_correctness | category | Literature | 1411 | 0.659255 | 0.472275 | 0.0608898 | 0.150149 | 0.809355 | 0.81219 | -0.00283487 | 0.146443 | 0.54721 | 0.788847 | 0.90825 | 0.164106 |
| tossup_correctness | category | Mythology | 320 | 0.663982 | 0.49352 | 0.0701608 | 0.156698 | 0.790625 | 0.79375 | -0.003125 | 0.147702 | 0.524526 | 0.766411 | 0.908533 | 0.170123 |
| tossup_correctness | category | Other Academic | 64 | 0.638021 | 0.567974 | 0.0842549 | 0.191872 | 0.703125 | 0.75 | -0.046875 | 0.141726 | 0.546571 | 0.7364 | 0.870059 | 0.180795 |
| tossup_correctness | category | Philosophy | 312 | 0.660581 | 0.483027 | 0.0895596 | 0.155594 | 0.798077 | 0.801282 | -0.00320513 | 0.142016 | 0.531006 | 0.74763 | 0.895978 | 0.17873 |
| tossup_correctness | category | Popular Culture | 104 | 0.602983 | 0.435457 | 0.0856112 | 0.130168 | 0.855769 | 0.846154 | 0.00961538 | 0.0971778 | 0.654924 | 0.815134 | 0.89651 | 0.155189 |
| tossup_correctness | category | Religion | 358 | 0.713383 | 0.541862 | 0.0739493 | 0.181772 | 0.731844 | 0.726257 | 0.00558659 | 0.168906 | 0.420114 | 0.689573 | 0.868635 | 0.192679 |
| tossup_correctness | category | Science | 1431 | 0.698549 | 0.508221 | 0.071044 | 0.166375 | 0.766597 | 0.765199 | 0.00139762 | 0.176953 | 0.441168 | 0.729434 | 0.890826 | 0.180273 |
| tossup_correctness | category | Social Science | 321 | 0.731044 | 0.509918 | 0.0723374 | 0.166837 | 0.76947 | 0.744548 | 0.0249221 | 0.201115 | 0.38865 | 0.720243 | 0.892046 | 0.178793 |
| tossup_correctness | category | Unknown | 1934 | 0.713974 | 0.506084 | 0.0558612 | 0.16581 | 0.761117 | 0.75698 | 0.0041365 | 0.168812 | 0.463289 | 0.738336 | 0.891777 | 0.179555 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.747555 | 0.549418 | 0.0859502 | 0.184683 | 0.708333 | 0.697917 | 0.0104167 | 0.179072 | 0.3726 | 0.664125 | 0.835416 | 0.197928 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.74921 | 0.50268 | 0.0531418 | 0.164768 | 0.76378 | 0.733408 | 0.0303712 | 0.176159 | 0.427609 | 0.721607 | 0.884348 | 0.184569 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.683435 | 0.520661 | 0.0497388 | 0.171002 | 0.762896 | 0.759276 | 0.00361991 | 0.171057 | 0.468174 | 0.750705 | 0.900308 | 0.174971 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.691968 | 0.484643 | 0.0602867 | 0.156678 | 0.782851 | 0.789125 | -0.00627396 | 0.156384 | 0.502449 | 0.763832 | 0.899158 | 0.172725 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.728403 | 0.48955 | 0.0811587 | 0.158872 | 0.778767 | 0.775342 | 0.00342466 | 0.181979 | 0.428419 | 0.734697 | 0.892485 | 0.179063 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.66005 | 0.763199 | 0.590267 | 1.42573 | 2.11816 | 2.66306 | 3.16661 | 3.99218 | 4.63138 |
| player | theta_1 | 1133 | -1.22629 | 0.895038 | -3.78666 | -2.56779 | -1.79735 | -1.29711 | -0.717644 | 0.438403 | 2.51103 |
| player | theta_2 | 1133 | -0.992704 | 0.642209 | -3.26412 | -2.08058 | -1.37805 | -1.00579 | -0.580244 | 0.0891668 | 1.22574 |
| player | theta_3 | 1133 | -1.13506 | 0.788834 | -3.36024 | -2.38381 | -1.64582 | -1.18211 | -0.665847 | 0.270394 | 1.60326 |
| player | theta_norm | 1133 | 2.2655 | 0.692618 | 0.318201 | 1.17126 | 1.79373 | 2.25694 | 2.68936 | 3.46953 | 4.5257 |
| tossup | start_difficulty_d1 | 1240 | -1.39531 | 0.60265 | -3.59301 | -2.25458 | -1.78359 | -1.44949 | -1.06672 | -0.346904 | 1.80458 |
| tossup | start_difficulty_d2 | 1240 | -1.37827 | 0.549037 | -3.70983 | -2.2304 | -1.74766 | -1.404 | -1.02516 | -0.45273 | 0.570277 |
| tossup | start_difficulty_d3 | 1240 | -1.3802 | 0.560064 | -3.49666 | -2.26272 | -1.7567 | -1.40931 | -1.01556 | -0.436784 | 0.661519 |
| tossup | end_difficulty_d1 | 1240 | -2.38618 | 0.706421 | -5.30216 | -3.40049 | -2.84763 | -2.44741 | -1.9711 | -1.1386 | 1.1295 |
| tossup | end_difficulty_d2 | 1240 | -2.36415 | 0.64565 | -5.16745 | -3.38789 | -2.7903 | -2.3846 | -1.95878 | -1.26883 | -0.176696 |
| tossup | end_difficulty_d3 | 1240 | -2.36438 | 0.653798 | -4.87312 | -3.40672 | -2.80494 | -2.38304 | -1.9278 | -1.28247 | -0.0675967 |
| tossup | total_drop_d1 | 1240 | 0.990869 | 0.131533 | 0.586194 | 0.772534 | 0.903628 | 0.992982 | 1.06862 | 1.18637 | 1.70915 |
| tossup | total_drop_d2 | 1240 | 0.98588 | 0.118341 | 0.66594 | 0.802678 | 0.90505 | 0.980045 | 1.0592 | 1.18314 | 1.45762 |
| tossup | total_drop_d3 | 1240 | 0.984177 | 0.118159 | 0.582493 | 0.804378 | 0.903153 | 0.982374 | 1.05833 | 1.18098 | 1.46064 |
| tossup | drop_share_1_d1 | 1240 | 0.303311 | 0.0174849 | 0.219644 | 0.275607 | 0.292994 | 0.303841 | 0.314588 | 0.328462 | 0.386318 |
| tossup | drop_share_2_d1 | 1240 | 0.34719 | 0.0119865 | 0.306547 | 0.327219 | 0.339203 | 0.347449 | 0.355281 | 0.366417 | 0.393299 |
| tossup | drop_share_3_d1 | 1240 | 0.349498 | 0.0185686 | 0.263624 | 0.320879 | 0.33732 | 0.348917 | 0.360741 | 0.379409 | 0.424529 |
| tossup | drop_share_1_d2 | 1240 | 0.302978 | 0.0155261 | 0.235172 | 0.276057 | 0.293557 | 0.303225 | 0.313267 | 0.327337 | 0.370765 |
| tossup | drop_share_2_d2 | 1240 | 0.3469 | 0.011757 | 0.307056 | 0.327858 | 0.33903 | 0.34703 | 0.354911 | 0.366026 | 0.400684 |
| tossup | drop_share_3_d2 | 1240 | 0.350122 | 0.0170227 | 0.27371 | 0.323115 | 0.339004 | 0.350398 | 0.360365 | 0.377262 | 0.450571 |
| tossup | drop_share_1_d3 | 1240 | 0.302853 | 0.0166846 | 0.22997 | 0.274897 | 0.293296 | 0.303139 | 0.313843 | 0.328984 | 0.368551 |
| tossup | drop_share_2_d3 | 1240 | 0.347154 | 0.011643 | 0.305461 | 0.328113 | 0.339747 | 0.346907 | 0.354326 | 0.366016 | 0.398104 |
| tossup | drop_share_3_d3 | 1240 | 0.349993 | 0.0175353 | 0.300154 | 0.322404 | 0.338762 | 0.349437 | 0.359896 | 0.380562 | 0.436441 |
| tossup | r_1 | 1240 | 0.331882 | 0.173076 | 0.0489754 | 0.109449 | 0.191595 | 0.292782 | 0.447751 | 0.659835 | 0.849378 |
| tossup | r_2 | 1240 | 0.329395 | 0.133055 | 0.0596613 | 0.138038 | 0.23372 | 0.318299 | 0.401966 | 0.580158 | 0.859819 |
| tossup | r_3 | 1240 | 0.338724 | 0.14841 | 0.0681251 | 0.134941 | 0.224248 | 0.320827 | 0.424496 | 0.631581 | 0.845812 |
| tossup | r_norm | 1240 | 0.632615 | 0.0530036 | 0.577392 | 0.580081 | 0.592454 | 0.616287 | 0.654109 | 0.745626 | 0.865518 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47484 | 0.49568 | 2.13526 | 3.75769 | 4.18014 | 4.42672 | 4.71948 | 5.41176 | 6.36202 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45262 | 0.416119 | 2.22435 | 3.8174 | 4.22766 | 4.43712 | 4.65413 | 5.16211 | 6.58269 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.46219 | 0.443917 | 2.44929 | 3.74985 | 4.21463 | 4.44419 | 4.70941 | 5.22173 | 6.06648 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.71941 | 2.31953 | -11.4306 | -2.95446 | 0.567619 | 2.82434 | 3.28372 | 3.62064 | 4.46361 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.41949 | 1.89365 | -8.08456 | -1.98837 | 2.54486 | 3.1326 | 3.40582 | 3.72851 | 4.15608 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.14008 | 2.05428 | -9.08204 | -2.41263 | 1.86373 | 3.02777 | 3.36296 | 3.75916 | 4.2305 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.75543 | 2.48797 | 0.844892 | 0.983973 | 1.06455 | 1.33777 | 4.15561 | 7.95403 | 16.0342 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.03314 | 2.05231 | 0.895288 | 0.959324 | 1.0212 | 1.15912 | 1.64149 | 6.93334 | 13.5064 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.32211 | 2.18914 | 0.87525 | 0.967043 | 1.03204 | 1.23071 | 2.56632 | 7.32249 | 13.6429 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236232 | 0.0808229 | 0.0320088 | 0.0810043 | 0.17881 | 0.271221 | 0.294326 | 0.31639 | 0.508033 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.342274 | 0.0752643 | 0.0605378 | 0.182229 | 0.334943 | 0.351058 | 0.364786 | 0.447386 | 0.716087 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.421494 | 0.130659 | 0.108294 | 0.302867 | 0.347978 | 0.368983 | 0.445663 | 0.719964 | 0.896036 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.255669 | 0.0663304 | 0.0385231 | 0.0912791 | 0.241724 | 0.279341 | 0.296215 | 0.313829 | 0.52126 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348606 | 0.0571806 | 0.0528601 | 0.251061 | 0.341045 | 0.351135 | 0.363019 | 0.407251 | 0.685647 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.395724 | 0.0995424 | 0.198384 | 0.321706 | 0.349217 | 0.364306 | 0.394546 | 0.649388 | 0.908617 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.247016 | 0.0713329 | 0.0416482 | 0.0903165 | 0.218136 | 0.273399 | 0.295579 | 0.315203 | 0.551079 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349326 | 0.0607649 | 0.0836746 | 0.233571 | 0.339139 | 0.351361 | 0.366157 | 0.428618 | 0.706117 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.403659 | 0.106182 | 0.0697386 | 0.317222 | 0.349386 | 0.367835 | 0.409991 | 0.6594 | 0.863946 |
| tossup_hazard | hazard_r_1 | 1240 | 0.380941 | 0.279498 | 0.0259329 | 0.0631198 | 0.134354 | 0.285409 | 0.603316 | 0.89256 | 0.952987 |
| tossup_hazard | hazard_r_2 | 1240 | 0.279092 | 0.199946 | 0.0294689 | 0.0575707 | 0.121455 | 0.21574 | 0.393075 | 0.690426 | 0.841034 |
| tossup_hazard | hazard_r_3 | 1240 | 0.339967 | 0.239546 | 0.0175439 | 0.0455778 | 0.137078 | 0.270848 | 0.536696 | 0.772563 | 0.930755 |
