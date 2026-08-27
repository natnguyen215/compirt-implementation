# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 282244 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.714192 |
| log_loss | 0.499304 |
| ece | 0.0407638 |
| brier | 0.161098 |
| accuracy | 0.775148 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00989779 |
| probability_std | 0.187004 |
| probability_p10 | 0.474689 |
| probability_p50 | 0.781274 |
| probability_p90 | 0.949444 |
| mean_predictive_variance | 0.15655 |
| integrated_brier_score | 0.0936274 |
| joint_tossup_event_log_loss | 6.38816 |
| buzz_position_mae | 0.135259 |
| buzz_position_median_absolute_error | 0.109026 |
| buzz_position_bias | 0.010576 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.401076 |
| first_buzzer_mean_reciprocal_rank | 0.605051 |
| first_buzzer_log_loss | 1.57064 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.714192 |
| neg_average_precision | 0.456558 |
| neg_precision | 0.541894 |
| neg_recall | 0.272686 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.190229 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00963837 |
| no_buzz_calibration_error | -0.00363127 |
| no_buzz_brier | 0.0126433 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.714192 | 0.499304 | 0.0407638 | 0.161098 | 0.775148 | 0.76525 | 0.00989779 | 0.187004 | 0.474689 | 0.781274 | 0.949444 | 0.15655 |
| tossup_correctness | tier | fall | 2933 | 0.708267 | 0.477129 | 0.0545478 | 0.15116 | 0.794408 | 0.791681 | 0.00272758 | 0.183458 | 0.49351 | 0.79842 | 0.955511 | 0.150455 |
| tossup_correctness | tier | nationals | 1584 | 0.711686 | 0.537607 | 0.0515887 | 0.177911 | 0.746212 | 0.724747 | 0.0214646 | 0.198588 | 0.442147 | 0.759502 | 0.947053 | 0.161305 |
| tossup_correctness | tier | regionals | 1886 | 0.713909 | 0.522218 | 0.0382063 | 0.170118 | 0.750795 | 0.746023 | 0.004772 | 0.189446 | 0.455213 | 0.760898 | 0.947996 | 0.16388 |
| tossup_correctness | tier | winter | 2892 | 0.714331 | 0.48587 | 0.039001 | 0.156085 | 0.787344 | 0.773167 | 0.014177 | 0.180436 | 0.498856 | 0.787222 | 0.943951 | 0.155347 |
| tossup_correctness | category | Current Events | 124 | 0.669788 | 0.566576 | 0.123708 | 0.184292 | 0.758065 | 0.75 | 0.00806452 | 0.214612 | 0.425231 | 0.741246 | 0.983626 | 0.158362 |
| tossup_correctness | category | Fine Arts | 1103 | 0.720885 | 0.494221 | 0.0459587 | 0.158766 | 0.783318 | 0.759746 | 0.0235721 | 0.184022 | 0.478863 | 0.786015 | 0.948792 | 0.153154 |
| tossup_correctness | category | Geography | 197 | 0.791375 | 0.535302 | 0.100908 | 0.171033 | 0.766497 | 0.670051 | 0.0964467 | 0.247898 | 0.306202 | 0.677503 | 0.940173 | 0.168894 |
| tossup_correctness | category | History | 1491 | 0.72304 | 0.471032 | 0.0528422 | 0.151869 | 0.788732 | 0.787391 | 0.00134138 | 0.184239 | 0.479075 | 0.777654 | 0.950835 | 0.156514 |
| tossup_correctness | category | Literature | 1472 | 0.708436 | 0.456166 | 0.0564217 | 0.141137 | 0.827446 | 0.804348 | 0.0230978 | 0.15931 | 0.560046 | 0.831616 | 0.956052 | 0.140298 |
| tossup_correctness | category | Mythology | 332 | 0.663859 | 0.475101 | 0.0698753 | 0.149541 | 0.801205 | 0.813253 | -0.0120482 | 0.161796 | 0.541338 | 0.808304 | 0.945178 | 0.152531 |
| tossup_correctness | category | Other Academic | 69 | 0.674208 | 0.52205 | 0.155699 | 0.175567 | 0.724638 | 0.753623 | -0.0289855 | 0.149292 | 0.555895 | 0.727668 | 0.905693 | 0.179158 |
| tossup_correctness | category | Philosophy | 324 | 0.712266 | 0.457426 | 0.0502321 | 0.148971 | 0.799383 | 0.799383 | 0 | 0.17086 | 0.515332 | 0.792255 | 0.963973 | 0.149823 |
| tossup_correctness | category | Popular Culture | 102 | 0.424913 | 0.528813 | 0.121854 | 0.153254 | 0.843137 | 0.833333 | 0.00980392 | 0.119566 | 0.672344 | 0.867908 | 0.955462 | 0.122799 |
| tossup_correctness | category | Religion | 372 | 0.676768 | 0.566585 | 0.0687683 | 0.193274 | 0.706989 | 0.709677 | -0.00268817 | 0.185595 | 0.452119 | 0.715945 | 0.92269 | 0.177379 |
| tossup_correctness | category | Science | 1487 | 0.694907 | 0.522942 | 0.054508 | 0.171624 | 0.748487 | 0.752522 | -0.00403497 | 0.194079 | 0.457303 | 0.771889 | 0.945386 | 0.160296 |
| tossup_correctness | category | Social Science | 336 | 0.7425 | 0.527444 | 0.0837599 | 0.172451 | 0.741071 | 0.702381 | 0.0386905 | 0.210511 | 0.381009 | 0.735445 | 0.939642 | 0.166435 |
| tossup_correctness | category | Unknown | 1886 | 0.713909 | 0.522218 | 0.0382063 | 0.170118 | 0.750795 | 0.746023 | 0.004772 | 0.189446 | 0.455213 | 0.760898 | 0.947996 | 0.16388 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.711671 | 0.534456 | 0.143602 | 0.17426 | 0.761421 | 0.736041 | 0.0253807 | 0.20999 | 0.352439 | 0.670294 | 0.891056 | 0.185198 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.715962 | 0.525949 | 0.0528934 | 0.173961 | 0.738071 | 0.735025 | 0.00304569 | 0.203075 | 0.406836 | 0.744415 | 0.939372 | 0.167139 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.701924 | 0.505345 | 0.0474845 | 0.163844 | 0.768992 | 0.769436 | -0.000444247 | 0.186505 | 0.480396 | 0.781159 | 0.946419 | 0.157216 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.696353 | 0.491584 | 0.04949 | 0.155694 | 0.792045 | 0.78402 | 0.00802512 | 0.175848 | 0.514499 | 0.79822 | 0.957534 | 0.150254 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.736671 | 0.491078 | 0.0256781 | 0.159109 | 0.776702 | 0.756008 | 0.0206943 | 0.186593 | 0.473468 | 0.783271 | 0.947933 | 0.156707 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 1.757 | 0.636099 | -0.674877 | 0.691839 | 1.37467 | 1.78352 | 2.1158 | 2.79196 | 3.93724 |
| player | theta_1 | 1186 | -1.49642 | 0.643099 | -3.0961 | -2.5028 | -1.96219 | -1.51412 | -1.05572 | -0.379905 | 0.717895 |
| player | theta_2 | 1186 | -1.51262 | 0.655428 | -3.21959 | -2.51601 | -1.99023 | -1.55962 | -1.07895 | -0.361822 | 0.614734 |
| player | theta_3 | 1186 | -1.58414 | 0.678802 | -4.06708 | -2.70419 | -2.07126 | -1.58727 | -1.1029 | -0.487548 | 0.179579 |
| player | theta_norm | 1186 | 2.8322 | 0.5644 | 0.88116 | 1.88105 | 2.4504 | 2.84805 | 3.21822 | 3.74541 | 4.31427 |
| tossup | start_difficulty_d1 | 1240 | -1.25697 | 0.410315 | -2.52542 | -1.87753 | -1.53281 | -1.29549 | -1.01117 | -0.518018 | 0.23909 |
| tossup | start_difficulty_d2 | 1240 | -1.25494 | 0.396946 | -2.71411 | -1.85821 | -1.51826 | -1.28655 | -1.01454 | -0.545408 | 0.286218 |
| tossup | start_difficulty_d3 | 1240 | -1.27708 | 0.408157 | -2.53994 | -1.9181 | -1.55106 | -1.29611 | -1.02024 | -0.565317 | 0.544143 |
| tossup | end_difficulty_d1 | 1240 | -2.2508 | 0.476245 | -3.57384 | -2.94389 | -2.57108 | -2.29153 | -1.97313 | -1.39448 | -0.535951 |
| tossup | end_difficulty_d2 | 1240 | -2.2461 | 0.4615 | -3.75296 | -2.94598 | -2.55576 | -2.29237 | -1.96796 | -1.40706 | -0.411642 |
| tossup | end_difficulty_d3 | 1240 | -2.27195 | 0.468633 | -3.74177 | -2.99236 | -2.58695 | -2.28719 | -2.00045 | -1.44829 | -0.0917513 |
| tossup | total_drop_d1 | 1240 | 0.993829 | 0.128661 | 0.702883 | 0.806878 | 0.914548 | 0.989625 | 1.06204 | 1.17594 | 2.31442 |
| tossup | total_drop_d2 | 1240 | 0.991154 | 0.117557 | 0.613207 | 0.803781 | 0.921164 | 0.989504 | 1.05869 | 1.17304 | 1.74569 |
| tossup | total_drop_d3 | 1240 | 0.994866 | 0.118205 | 0.635894 | 0.813885 | 0.91663 | 0.98985 | 1.06296 | 1.19114 | 1.65722 |
| tossup | drop_share_1_d1 | 1240 | 0.304243 | 0.0196307 | 0.20353 | 0.271934 | 0.293337 | 0.304934 | 0.316736 | 0.33357 | 0.38426 |
| tossup | drop_share_2_d1 | 1240 | 0.347139 | 0.013948 | 0.289067 | 0.325977 | 0.338561 | 0.346782 | 0.355195 | 0.367531 | 0.493556 |
| tossup | drop_share_3_d1 | 1240 | 0.348619 | 0.0211241 | 0.270172 | 0.318217 | 0.335019 | 0.347273 | 0.360422 | 0.38337 | 0.507402 |
| tossup | drop_share_1_d2 | 1240 | 0.304439 | 0.0179963 | 0.203927 | 0.275316 | 0.294247 | 0.305182 | 0.314972 | 0.332185 | 0.366975 |
| tossup | drop_share_2_d2 | 1240 | 0.34719 | 0.012889 | 0.302472 | 0.327343 | 0.338941 | 0.346855 | 0.354824 | 0.368853 | 0.424582 |
| tossup | drop_share_3_d2 | 1240 | 0.348371 | 0.0189379 | 0.290989 | 0.31868 | 0.33646 | 0.349044 | 0.35957 | 0.379193 | 0.457061 |
| tossup | drop_share_1_d3 | 1240 | 0.304202 | 0.019175 | 0.201526 | 0.273038 | 0.293112 | 0.305244 | 0.316891 | 0.332974 | 0.3592 |
| tossup | drop_share_2_d3 | 1240 | 0.34726 | 0.0126079 | 0.30308 | 0.327361 | 0.339226 | 0.346913 | 0.355027 | 0.368922 | 0.407856 |
| tossup | drop_share_3_d3 | 1240 | 0.348538 | 0.0199717 | 0.27715 | 0.31839 | 0.336083 | 0.348069 | 0.359681 | 0.381021 | 0.452203 |
| tossup | r_1 | 1240 | 0.674026 | 0.294711 | 0.16856 | 0.324258 | 0.45665 | 0.615346 | 0.826318 | 1.25253 | 2.0632 |
| tossup | r_2 | 1240 | 0.6471 | 0.294648 | 0.17159 | 0.288449 | 0.432036 | 0.588053 | 0.80598 | 1.18599 | 2.7963 |
| tossup | r_3 | 1240 | 0.668737 | 0.30888 | 0.188459 | 0.305221 | 0.441335 | 0.58615 | 0.825073 | 1.27706 | 2.03415 |
| tossup | r_norm | 1240 | 1.21556 | 0.334107 | 0.397676 | 0.746038 | 0.955944 | 1.18531 | 1.42488 | 1.83049 | 2.84555 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 0.637269 | 0.270976 | -0.16075 | 0.204449 | 0.440575 | 0.631334 | 0.826962 | 1.07715 | 1.42117 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 0.637399 | 0.283712 | -0.204368 | 0.157147 | 0.430857 | 0.647199 | 0.840011 | 1.08718 | 1.55239 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 0.631549 | 0.292985 | -0.375768 | 0.161584 | 0.429948 | 0.621494 | 0.81435 | 1.16049 | 1.6919 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.76886 | 0.506735 | -2.84841 | -1.6563 | -1.08074 | -0.762834 | -0.418749 | 0.0225109 | 0.58944 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.727627 | 0.494743 | -2.85415 | -1.54716 | -1.0569 | -0.731224 | -0.37651 | 0.0476452 | 0.770251 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.829568 | 0.595018 | -3.14871 | -1.76137 | -1.20035 | -0.843372 | -0.457263 | 0.188054 | 0.957688 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 1.40613 | 0.428444 | 0.672566 | 0.906398 | 1.07458 | 1.30886 | 1.62762 | 2.22859 | 3.43313 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.36503 | 0.398428 | 0.651873 | 0.917503 | 1.06276 | 1.27385 | 1.56158 | 2.12937 | 3.57646 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.46112 | 0.485258 | 0.661303 | 0.907438 | 1.06915 | 1.35377 | 1.74519 | 2.35004 | 3.96046 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.245944 | 0.0662358 | 0.0824486 | 0.145581 | 0.205769 | 0.247857 | 0.281346 | 0.340272 | 0.67645 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.305475 | 0.0585256 | 0.0971167 | 0.194953 | 0.270727 | 0.316384 | 0.343172 | 0.38514 | 0.570753 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.448581 | 0.104883 | 0.0923846 | 0.305722 | 0.379371 | 0.432287 | 0.510091 | 0.64235 | 0.820435 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.24571 | 0.0623834 | 0.0752835 | 0.150334 | 0.206962 | 0.247816 | 0.277229 | 0.341418 | 0.678944 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.305106 | 0.0578779 | 0.0749885 | 0.197268 | 0.274316 | 0.31485 | 0.341518 | 0.380984 | 0.552314 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.449183 | 0.102073 | 0.124584 | 0.307742 | 0.380834 | 0.433365 | 0.50915 | 0.641261 | 0.849728 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.245855 | 0.0721273 | 0.0590233 | 0.136374 | 0.19759 | 0.248606 | 0.284584 | 0.364989 | 0.62251 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.302637 | 0.0608076 | 0.101057 | 0.190299 | 0.264876 | 0.314853 | 0.341153 | 0.387342 | 0.518354 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.451508 | 0.113527 | 0.111626 | 0.291907 | 0.376535 | 0.429228 | 0.524554 | 0.660301 | 0.832369 |
| tossup_hazard | hazard_r_1 | 1240 | 1.35926 | 0.67206 | 0.238345 | 0.539538 | 0.870686 | 1.21621 | 1.70163 | 2.67425 | 4.35302 |
| tossup_hazard | hazard_r_2 | 1240 | 1.42553 | 0.782266 | 0.197996 | 0.518215 | 0.855942 | 1.21238 | 1.83373 | 3.03405 | 5.02437 |
| tossup_hazard | hazard_r_3 | 1240 | 1.45262 | 0.717321 | 0.195862 | 0.426294 | 0.911665 | 1.38442 | 1.89447 | 2.77327 | 4.89718 |
