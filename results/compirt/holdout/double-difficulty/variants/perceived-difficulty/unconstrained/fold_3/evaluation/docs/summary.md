# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 339112 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.661646 |
| log_loss | 0.512578 |
| ece | 0.0365519 |
| brier | 0.167061 |
| accuracy | 0.773128 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0030837 |
| probability_std | 0.133809 |
| probability_p10 | 0.552824 |
| probability_p50 | 0.763338 |
| probability_p90 | 0.89244 |
| mean_predictive_variance | 0.174842 |
| integrated_brier_score | 0.1673 |
| joint_tossup_event_log_loss | 7.57409 |
| buzz_position_mae | 0.325361 |
| buzz_position_median_absolute_error | 0.326363 |
| buzz_position_bias | -0.310058 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.350551 |
| first_buzzer_mean_reciprocal_rank | 0.563427 |
| first_buzzer_log_loss | 1.68418 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.661646 |
| neg_average_precision | 0.385052 |
| neg_precision | 0.526119 |
| neg_recall | 0.135057 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0328142 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.216943 |
| no_buzz_calibration_error | 0.201758 |
| no_buzz_brier | 0.0644995 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.661646 | 0.512578 | 0.0365519 | 0.167061 | 0.773128 | 0.770044 | 0.0030837 | 0.133809 | 0.552824 | 0.763338 | 0.89244 | 0.174842 |
| tossup_correctness | tier | fall | 2817 | 0.656333 | 0.496659 | 0.0129398 | 0.16033 | 0.785942 | 0.781683 | 0.00425985 | 0.102455 | 0.645145 | 0.805188 | 0.899685 | 0.157386 |
| tossup_correctness | tier | nationals | 1542 | 0.712709 | 0.560192 | 0.121175 | 0.188049 | 0.732815 | 0.73476 | -0.00194553 | 0.139035 | 0.430188 | 0.623548 | 0.795278 | 0.217451 |
| tossup_correctness | tier | regionals | 1934 | 0.659698 | 0.529057 | 0.0458959 | 0.174668 | 0.758014 | 0.75698 | 0.00103413 | 0.120985 | 0.552137 | 0.724813 | 0.859939 | 0.190086 |
| tossup_correctness | tier | winter | 2787 | 0.656868 | 0.49089 | 0.0269388 | 0.156974 | 0.792967 | 0.786868 | 0.00609975 | 0.118426 | 0.61531 | 0.801877 | 0.90904 | 0.158333 |
| tossup_correctness | category | Current Events | 125 | 0.627764 | 0.595293 | 0.0855678 | 0.204609 | 0.672 | 0.704 | -0.032 | 0.137943 | 0.502546 | 0.717498 | 0.846026 | 0.19515 |
| tossup_correctness | category | Fine Arts | 1072 | 0.65146 | 0.511621 | 0.0443253 | 0.167395 | 0.779851 | 0.770522 | 0.00932836 | 0.12649 | 0.569194 | 0.76717 | 0.888893 | 0.173302 |
| tossup_correctness | category | Geography | 185 | 0.738601 | 0.532598 | 0.0682339 | 0.177609 | 0.718919 | 0.702703 | 0.0162162 | 0.150033 | 0.477196 | 0.716462 | 0.866598 | 0.192238 |
| tossup_correctness | category | History | 1443 | 0.693758 | 0.501463 | 0.0304581 | 0.163577 | 0.776161 | 0.765073 | 0.011088 | 0.145246 | 0.527315 | 0.764805 | 0.904919 | 0.172223 |
| tossup_correctness | category | Literature | 1411 | 0.597738 | 0.483651 | 0.0508812 | 0.151328 | 0.807938 | 0.81219 | -0.0042523 | 0.119896 | 0.626771 | 0.827592 | 0.921978 | 0.144983 |
| tossup_correctness | category | Mythology | 320 | 0.614591 | 0.504876 | 0.0612082 | 0.161874 | 0.784375 | 0.79375 | -0.009375 | 0.119962 | 0.56852 | 0.77147 | 0.878008 | 0.174721 |
| tossup_correctness | category | Other Academic | 64 | 0.601562 | 0.569351 | 0.143355 | 0.190936 | 0.765625 | 0.75 | 0.015625 | 0.129007 | 0.45438 | 0.661773 | 0.81028 | 0.209616 |
| tossup_correctness | category | Philosophy | 312 | 0.571935 | 0.506853 | 0.0649785 | 0.163213 | 0.791667 | 0.801282 | -0.00961538 | 0.118625 | 0.583428 | 0.779943 | 0.88417 | 0.170999 |
| tossup_correctness | category | Popular Culture | 104 | 0.53267 | 0.47131 | 0.133547 | 0.144847 | 0.846154 | 0.846154 | 0 | 0.105316 | 0.60345 | 0.764334 | 0.879183 | 0.176167 |
| tossup_correctness | category | Religion | 358 | 0.673587 | 0.547153 | 0.0306623 | 0.18279 | 0.740223 | 0.726257 | 0.0139665 | 0.139754 | 0.537259 | 0.749615 | 0.876275 | 0.180886 |
| tossup_correctness | category | Science | 1431 | 0.676201 | 0.511329 | 0.0373631 | 0.167415 | 0.770091 | 0.765199 | 0.00489168 | 0.137125 | 0.539824 | 0.756867 | 0.880032 | 0.178288 |
| tossup_correctness | category | Social Science | 321 | 0.692979 | 0.532164 | 0.03819 | 0.176459 | 0.744548 | 0.744548 | 0 | 0.137145 | 0.527917 | 0.725676 | 0.865018 | 0.187619 |
| tossup_correctness | category | Unknown | 1934 | 0.659698 | 0.529057 | 0.0458959 | 0.174668 | 0.758014 | 0.75698 | 0.00103413 | 0.120985 | 0.552137 | 0.724813 | 0.859939 | 0.190086 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.708312 | 0.559755 | 0.0504225 | 0.190252 | 0.708333 | 0.697917 | 0.0104167 | 0.140539 | 0.500901 | 0.723402 | 0.856593 | 0.192466 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.679273 | 0.539956 | 0.0233729 | 0.179862 | 0.736783 | 0.733408 | 0.00337458 | 0.133628 | 0.524479 | 0.738992 | 0.869811 | 0.185008 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.64429 | 0.531148 | 0.0344822 | 0.174793 | 0.760181 | 0.759276 | 0.000904977 | 0.130313 | 0.567644 | 0.76556 | 0.887033 | 0.174738 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.652331 | 0.496966 | 0.0549523 | 0.160106 | 0.784245 | 0.789125 | -0.00487975 | 0.128587 | 0.565334 | 0.766653 | 0.893384 | 0.17348 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.669866 | 0.502427 | 0.0451952 | 0.16262 | 0.787329 | 0.775342 | 0.0119863 | 0.139713 | 0.546208 | 0.767963 | 0.89988 | 0.172006 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -1.83847 | 0.779009 | -4.50784 | -3.07018 | -2.40165 | -1.89716 | -1.26048 | -0.523317 | 0.0506642 |
| player | theta_2 | 1133 | -1.35846 | 0.755255 | -4.44916 | -2.72811 | -1.87567 | -1.2639 | -0.765878 | -0.294163 | 0.0855214 |
| player | theta_3 | 1133 | -1.22428 | 0.938884 | -3.80362 | -2.90507 | -2.00945 | -0.904485 | -0.419667 | -0.127383 | 0.25996 |
| player | alpha_1 | 1133 | -0.738462 | 0.712574 | -2.89745 | -1.91138 | -1.17708 | -0.718896 | -0.284408 | 0.346039 | 1.68406 |
| player | alpha_2 | 1133 | 0.101357 | 1.11191 | -2.79602 | -1.66101 | -0.736236 | 0.111992 | 0.932104 | 1.92908 | 2.86232 |
| player | alpha_3 | 1133 | 0.0566819 | 1.12696 | -3.07268 | -1.95401 | -0.698096 | 0.0976493 | 0.929332 | 1.78118 | 3.24102 |
| player | beta_1 | 1133 | -2.07722 | 1.09079 | -5.39428 | -4.15359 | -2.73591 | -1.96789 | -1.29372 | -0.519869 | -0.0661309 |
| player | beta_2 | 1133 | -1.49052 | 0.790625 | -3.81612 | -2.83629 | -2.03578 | -1.47571 | -0.819996 | -0.317275 | -0.0138016 |
| player | beta_3 | 1133 | -1.49011 | 1.32083 | -5.79269 | -4.12842 | -2.38202 | -0.949478 | -0.417042 | -0.135386 | 0.182297 |
| player | theta_norm | 1133 | 2.83776 | 0.853791 | 0.993965 | 1.40509 | 2.22715 | 2.82476 | 3.40341 | 4.27852 | 5.3548 |
| tossup | start_difficulty_d1 | 1240 | -2.1513 | 1.10663 | -5.29364 | -4.09261 | -2.96251 | -2.07684 | -1.3443 | -0.399997 | 0.269442 |
| tossup | start_difficulty_d2 | 1240 | -0.631251 | 1.53471 | -4.61852 | -3.78526 | -0.805628 | -0.0276799 | 0.414282 | 0.832642 | 1.50533 |
| tossup | start_difficulty_d3 | 1240 | -1.11832 | 1.22187 | -4.06906 | -3.16295 | -2.13876 | -1.07322 | 0.0478138 | 0.542099 | 1.1528 |
| tossup | end_difficulty_d1 | 1240 | -2.97661 | 1.03159 | -6.13336 | -4.6705 | -3.70375 | -3.01284 | -2.24919 | -1.27956 | -0.567741 |
| tossup | end_difficulty_d2 | 1240 | -1.83471 | 1.42957 | -9.75452 | -4.42163 | -2.991 | -1.32769 | -0.771602 | -0.219588 | 0.531947 |
| tossup | end_difficulty_d3 | 1240 | -2.27664 | 1.34549 | -7.90101 | -4.51549 | -3.2095 | -2.1931 | -1.12265 | -0.51002 | 0.261117 |
| tossup | total_drop_d1 | 1240 | 0.825308 | 0.238773 | 0.275826 | 0.420056 | 0.669112 | 0.852878 | 0.962352 | 1.1895 | 1.90491 |
| tossup | total_drop_d2 | 1240 | 1.20346 | 0.698994 | 0.306154 | 0.435677 | 0.950175 | 1.109 | 1.35199 | 2.29266 | 9.40497 |
| tossup | total_drop_d3 | 1240 | 1.15832 | 0.657362 | 0.550937 | 0.720046 | 0.884192 | 0.997943 | 1.16561 | 2.07372 | 8.00253 |
| tossup | drop_share_1_d1 | 1240 | 0.340904 | 0.0283311 | 0.251163 | 0.301938 | 0.322421 | 0.337224 | 0.355251 | 0.393367 | 0.46369 |
| tossup | drop_share_2_d1 | 1240 | 0.326634 | 0.0175329 | 0.267205 | 0.292253 | 0.316279 | 0.329891 | 0.339496 | 0.349713 | 0.371791 |
| tossup | drop_share_3_d1 | 1240 | 0.332462 | 0.026281 | 0.235454 | 0.289979 | 0.317017 | 0.331636 | 0.346774 | 0.374571 | 0.453944 |
| tossup | drop_share_1_d2 | 1240 | 0.296886 | 0.036257 | 0.117883 | 0.246964 | 0.278493 | 0.294391 | 0.310419 | 0.367049 | 0.460926 |
| tossup | drop_share_2_d2 | 1240 | 0.34828 | 0.0283337 | 0.268642 | 0.293335 | 0.337675 | 0.353059 | 0.363908 | 0.387464 | 0.459279 |
| tossup | drop_share_3_d2 | 1240 | 0.354834 | 0.0305628 | 0.237926 | 0.310179 | 0.338413 | 0.353055 | 0.368945 | 0.40724 | 0.58197 |
| tossup | drop_share_1_d3 | 1240 | 0.321732 | 0.0344879 | 0.114529 | 0.277508 | 0.301281 | 0.32093 | 0.342873 | 0.377522 | 0.434464 |
| tossup | drop_share_2_d3 | 1240 | 0.344111 | 0.0185195 | 0.295772 | 0.317991 | 0.332656 | 0.343097 | 0.353092 | 0.373158 | 0.492081 |
| tossup | drop_share_3_d3 | 1240 | 0.334157 | 0.0282279 | 0.235164 | 0.286069 | 0.319552 | 0.336708 | 0.351222 | 0.367468 | 0.574231 |
| tossup | r_1 | 1240 | 0.463399 | 0.280272 | 0.033523 | 0.0642002 | 0.198113 | 0.44117 | 0.757612 | 0.846679 | 0.934121 |
| tossup | r_2 | 1240 | 0.252817 | 0.283129 | 0.0394679 | 0.056988 | 0.0828744 | 0.116692 | 0.191745 | 0.843099 | 0.924073 |
| tossup | r_3 | 1240 | 0.283783 | 0.235683 | 0.0200933 | 0.0391435 | 0.0790433 | 0.174262 | 0.486212 | 0.727743 | 0.843671 |
| tossup | r_norm | 1240 | 0.752848 | 0.0806322 | 0.587163 | 0.629389 | 0.672798 | 0.764448 | 0.818513 | 0.871286 | 0.935333 |
