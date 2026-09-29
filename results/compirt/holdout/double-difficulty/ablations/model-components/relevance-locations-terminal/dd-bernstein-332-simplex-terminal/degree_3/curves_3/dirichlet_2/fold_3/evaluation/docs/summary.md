# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 303711 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709045 |
| log_loss | 0.501075 |
| ece | 0.0713461 |
| brier | 0.162502 |
| accuracy | 0.779075 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00903084 |
| probability_std | 0.163377 |
| probability_p10 | 0.473126 |
| probability_p50 | 0.728518 |
| probability_p90 | 0.893444 |
| mean_predictive_variance | 0.182322 |
| integrated_brier_score | 0.111109 |
| joint_tossup_event_log_loss | 6.71039 |
| buzz_position_mae | 0.168561 |
| buzz_position_median_absolute_error | 0.151878 |
| buzz_position_bias | -0.0835565 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.339868 |
| first_buzzer_mean_reciprocal_rank | 0.553206 |
| first_buzzer_log_loss | 1.71078 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.709045 |
| neg_average_precision | 0.456494 |
| neg_precision | 0.536412 |
| neg_recall | 0.289272 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.16959 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0114402 |
| no_buzz_calibration_error | -0.00374418 |
| no_buzz_brier | 0.0134451 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.709045 | 0.501075 | 0.0713461 | 0.162502 | 0.779075 | 0.770044 | 0.00903084 | 0.163377 | 0.473126 | 0.728518 | 0.893444 | 0.182322 |
| tossup_correctness | tier | fall | 2817 | 0.699799 | 0.488061 | 0.0571326 | 0.15643 | 0.793752 | 0.781683 | 0.0120696 | 0.160482 | 0.500508 | 0.760333 | 0.916381 | 0.170684 |
| tossup_correctness | tier | nationals | 1542 | 0.723874 | 0.532556 | 0.0821653 | 0.177131 | 0.743839 | 0.73476 | 0.00907912 | 0.159242 | 0.428994 | 0.67127 | 0.841041 | 0.201357 |
| tossup_correctness | tier | regionals | 1934 | 0.714324 | 0.512796 | 0.0769891 | 0.167822 | 0.768356 | 0.75698 | 0.0113754 | 0.16064 | 0.460173 | 0.706643 | 0.869461 | 0.191397 |
| tossup_correctness | tier | winter | 2787 | 0.697876 | 0.488678 | 0.07883 | 0.156852 | 0.791173 | 0.786868 | 0.00430571 | 0.162115 | 0.489163 | 0.740869 | 0.900394 | 0.177257 |
| tossup_correctness | category | Current Events | 125 | 0.702703 | 0.551226 | 0.0465587 | 0.184914 | 0.712 | 0.704 | 0.008 | 0.165612 | 0.466443 | 0.695733 | 0.902827 | 0.189591 |
| tossup_correctness | category | Fine Arts | 1072 | 0.729227 | 0.487279 | 0.0706122 | 0.156427 | 0.791045 | 0.770522 | 0.0205224 | 0.165465 | 0.472734 | 0.738282 | 0.900314 | 0.179196 |
| tossup_correctness | category | Geography | 185 | 0.772168 | 0.516166 | 0.0987104 | 0.171044 | 0.767568 | 0.702703 | 0.0648649 | 0.206783 | 0.33462 | 0.665754 | 0.855687 | 0.191825 |
| tossup_correctness | category | History | 1443 | 0.732972 | 0.495356 | 0.0703507 | 0.161635 | 0.772696 | 0.765073 | 0.00762301 | 0.166875 | 0.463449 | 0.715511 | 0.895896 | 0.184153 |
| tossup_correctness | category | Literature | 1411 | 0.650232 | 0.480332 | 0.0757119 | 0.152722 | 0.801559 | 0.81219 | -0.0106308 | 0.143997 | 0.544869 | 0.773516 | 0.91151 | 0.168124 |
| tossup_correctness | category | Mythology | 320 | 0.663088 | 0.499093 | 0.108154 | 0.157552 | 0.796875 | 0.79375 | 0.003125 | 0.147736 | 0.529157 | 0.759452 | 0.915153 | 0.172408 |
| tossup_correctness | category | Other Academic | 64 | 0.660156 | 0.538146 | 0.0723313 | 0.178356 | 0.71875 | 0.75 | -0.03125 | 0.128341 | 0.508915 | 0.715215 | 0.83418 | 0.196098 |
| tossup_correctness | category | Philosophy | 312 | 0.657613 | 0.488876 | 0.0887364 | 0.156896 | 0.798077 | 0.801282 | -0.00320513 | 0.137799 | 0.529448 | 0.73333 | 0.88047 | 0.181937 |
| tossup_correctness | category | Popular Culture | 104 | 0.522727 | 0.468044 | 0.0902249 | 0.140165 | 0.836538 | 0.846154 | -0.00961538 | 0.103844 | 0.665435 | 0.819006 | 0.915505 | 0.146909 |
| tossup_correctness | category | Religion | 358 | 0.746193 | 0.525907 | 0.0675353 | 0.174819 | 0.748603 | 0.726257 | 0.0223464 | 0.152389 | 0.458486 | 0.673007 | 0.84804 | 0.201302 |
| tossup_correctness | category | Science | 1431 | 0.69392 | 0.510372 | 0.0701667 | 0.166553 | 0.77638 | 0.765199 | 0.011181 | 0.168143 | 0.453633 | 0.729491 | 0.901896 | 0.181192 |
| tossup_correctness | category | Social Science | 321 | 0.745127 | 0.513196 | 0.0845253 | 0.166622 | 0.76947 | 0.744548 | 0.0249221 | 0.184417 | 0.387292 | 0.702373 | 0.89825 | 0.186821 |
| tossup_correctness | category | Unknown | 1934 | 0.714324 | 0.512796 | 0.0769891 | 0.167822 | 0.768356 | 0.75698 | 0.0113754 | 0.16064 | 0.460173 | 0.706643 | 0.869461 | 0.191397 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.764282 | 0.541304 | 0.0810217 | 0.180974 | 0.729167 | 0.697917 | 0.03125 | 0.171069 | 0.365284 | 0.646288 | 0.83075 | 0.207071 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.745198 | 0.508081 | 0.0534509 | 0.166955 | 0.768279 | 0.733408 | 0.0348706 | 0.174293 | 0.432108 | 0.705169 | 0.892624 | 0.186682 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.687214 | 0.521986 | 0.0627347 | 0.170244 | 0.765158 | 0.759276 | 0.00588235 | 0.166265 | 0.47218 | 0.733 | 0.898975 | 0.18035 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.687731 | 0.489388 | 0.0738235 | 0.157297 | 0.789474 | 0.789125 | 0.000348554 | 0.152244 | 0.506253 | 0.745016 | 0.900388 | 0.177523 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.726288 | 0.491954 | 0.0849041 | 0.159184 | 0.785959 | 0.775342 | 0.0106164 | 0.164478 | 0.460044 | 0.719021 | 0.883477 | 0.185576 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 4.40079 | 0.55055 | 2.51411 | 3.49224 | 4.04963 | 4.41104 | 4.77617 | 5.3145 | 5.8142 |
| player | theta_1 | 1133 | -1.17567 | 0.817362 | -3.1553 | -2.34091 | -1.76252 | -1.27567 | -0.675053 | 0.263419 | 2.84399 |
| player | theta_2 | 1133 | -1.11222 | 0.745872 | -3.51607 | -2.23515 | -1.61191 | -1.17803 | -0.644148 | 0.142625 | 1.73579 |
| player | theta_3 | 1133 | -1.10118 | 0.735057 | -2.98027 | -2.21111 | -1.61833 | -1.16673 | -0.625709 | 0.229587 | 1.90451 |
| player | theta_norm | 1133 | 2.2552 | 0.713811 | 0.52355 | 1.0664 | 1.73817 | 2.2916 | 2.78265 | 3.37006 | 4.6952 |
| tossup | start_difficulty_d1 | 1240 | -0.763699 | 0.639019 | -3.35398 | -2.02744 | -1.05359 | -0.669503 | -0.405525 | 0.165657 | 1.32022 |
| tossup | start_difficulty_d2 | 1240 | -0.65622 | 0.534921 | -3.2217 | -1.53222 | -0.874402 | -0.616399 | -0.382553 | 0.122702 | 1.27319 |
| tossup | start_difficulty_d3 | 1240 | -0.653951 | 0.549459 | -3.22815 | -1.63079 | -0.896984 | -0.606806 | -0.357791 | 0.157889 | 1.12197 |
| tossup | end_difficulty_d1 | 1240 | -1.93254 | 0.828694 | -5.64328 | -3.57451 | -2.24976 | -1.81229 | -1.45798 | -0.745841 | 0.477385 |
| tossup | end_difficulty_d2 | 1240 | -1.79748 | 0.690155 | -5.05192 | -3.06018 | -2.07269 | -1.73893 | -1.44137 | -0.816346 | 0.406682 |
| tossup | end_difficulty_d3 | 1240 | -1.79218 | 0.710209 | -5.7152 | -3.04889 | -2.06757 | -1.73468 | -1.42454 | -0.762933 | 0.321313 |
| tossup | total_drop_d1 | 1240 | 1.16884 | 0.243528 | 0.764196 | 0.912373 | 1.03848 | 1.12252 | 1.23017 | 1.59667 | 3.22534 |
| tossup | total_drop_d2 | 1240 | 1.14126 | 0.2151 | 0.767659 | 0.919835 | 1.0366 | 1.1107 | 1.20192 | 1.42713 | 3.40704 |
| tossup | total_drop_d3 | 1240 | 1.13822 | 0.196531 | 0.773417 | 0.904936 | 1.0343 | 1.10896 | 1.19196 | 1.46959 | 3.26803 |
| tossup | drop_share_1_d1 | 1240 | 0.316697 | 0.0205851 | 0.220664 | 0.288279 | 0.304315 | 0.314468 | 0.325714 | 0.353446 | 0.428115 |
| tossup | drop_share_2_d1 | 1240 | 0.349379 | 0.0121181 | 0.310822 | 0.330663 | 0.341614 | 0.34923 | 0.356862 | 0.368498 | 0.405808 |
| tossup | drop_share_3_d1 | 1240 | 0.333924 | 0.020709 | 0.220725 | 0.293804 | 0.324672 | 0.336081 | 0.347488 | 0.361178 | 0.397208 |
| tossup | drop_share_1_d2 | 1240 | 0.314445 | 0.0183754 | 0.199678 | 0.288775 | 0.303815 | 0.312991 | 0.323156 | 0.343843 | 0.411456 |
| tossup | drop_share_2_d2 | 1240 | 0.349361 | 0.0126323 | 0.305305 | 0.329569 | 0.341906 | 0.348998 | 0.356366 | 0.369629 | 0.483849 |
| tossup | drop_share_3_d2 | 1240 | 0.336194 | 0.0183242 | 0.246022 | 0.304516 | 0.326397 | 0.337049 | 0.347631 | 0.36327 | 0.402419 |
| tossup | drop_share_1_d3 | 1240 | 0.315742 | 0.0194908 | 0.254114 | 0.288572 | 0.303937 | 0.314076 | 0.324291 | 0.347136 | 0.475285 |
| tossup | drop_share_2_d3 | 1240 | 0.348398 | 0.0115273 | 0.307425 | 0.329956 | 0.340691 | 0.348168 | 0.355964 | 0.366918 | 0.391485 |
| tossup | drop_share_3_d3 | 1240 | 0.33586 | 0.0189516 | 0.216273 | 0.30452 | 0.326666 | 0.337056 | 0.347383 | 0.363612 | 0.40451 |
| tossup | r_1 | 1240 | 0.344727 | 0.189708 | 0.0439674 | 0.100102 | 0.200729 | 0.301024 | 0.459977 | 0.729072 | 0.858238 |
| tossup | r_2 | 1240 | 0.323116 | 0.167291 | 0.052546 | 0.100729 | 0.205226 | 0.292201 | 0.41136 | 0.667876 | 0.883763 |
| tossup | r_3 | 1240 | 0.332158 | 0.169674 | 0.0588854 | 0.102909 | 0.203474 | 0.307438 | 0.423051 | 0.660775 | 0.897084 |
| tossup | r_norm | 1240 | 0.648683 | 0.0739846 | 0.577358 | 0.580023 | 0.594495 | 0.619503 | 0.679441 | 0.815995 | 0.900093 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.71689 | 0.802716 | 0.252877 | 0.719941 | 1.08752 | 1.49662 | 2.30846 | 3.252 | 3.86479 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.5869 | 0.763699 | 0.229756 | 0.565907 | 0.971582 | 1.48286 | 2.10283 | 2.99216 | 4.41815 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.61046 | 0.81391 | 0.372516 | 0.580627 | 0.977332 | 1.43824 | 2.11101 | 3.1914 | 4.53996 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.368577 | 1.36571 | -8.32426 | -3.25175 | -0.401536 | 0.0403528 | 0.378591 | 0.833993 | 2.14478 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.287064 | 1.3074 | -10.261 | -2.81022 | -0.370187 | 0.00826028 | 0.37568 | 0.869158 | 1.93043 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.262398 | 1.34335 | -8.82075 | -3.24942 | -0.35311 | 0.0408346 | 0.416678 | 1.00434 | 1.98251 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.08547 | 1.88326 | 0.811665 | 0.952081 | 1.01384 | 1.09675 | 2.28369 | 6.13045 | 11.7157 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.87396 | 1.75727 | 0.771324 | 0.950542 | 1.00183 | 1.08725 | 1.68565 | 5.8499 | 13.0433 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.87286 | 1.81671 | 0.696726 | 0.947142 | 1.00387 | 1.06593 | 1.43136 | 6.25461 | 12.2362 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.230002 | 0.0757981 | 0.0397938 | 0.0752642 | 0.181947 | 0.264194 | 0.284428 | 0.303619 | 0.442426 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.347267 | 0.0725726 | 0.0787289 | 0.19398 | 0.33843 | 0.351181 | 0.366348 | 0.455992 | 0.728365 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.422731 | 0.119369 | 0.0775704 | 0.33 | 0.358672 | 0.378278 | 0.429041 | 0.718915 | 0.881477 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.236948 | 0.0712897 | 0.0266299 | 0.0802561 | 0.207348 | 0.26473 | 0.289919 | 0.308349 | 0.398985 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.343807 | 0.0604792 | 0.0527242 | 0.216577 | 0.338506 | 0.350189 | 0.362622 | 0.409331 | 0.64238 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.419245 | 0.111621 | 0.151562 | 0.335198 | 0.356717 | 0.376118 | 0.4287 | 0.694737 | 0.909678 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.239431 | 0.0708785 | 0.0398758 | 0.0761013 | 0.218486 | 0.267594 | 0.288524 | 0.305743 | 0.405586 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348295 | 0.0634132 | 0.0542678 | 0.228556 | 0.340116 | 0.350492 | 0.363091 | 0.430125 | 0.700509 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.412274 | 0.107753 | 0.195502 | 0.334458 | 0.357482 | 0.375505 | 0.413317 | 0.679698 | 0.905856 |
| tossup_hazard | hazard_r_1 | 1240 | 0.361404 | 0.30325 | 0.0244538 | 0.0514919 | 0.100251 | 0.222014 | 0.648937 | 0.896157 | 0.945935 |
| tossup_hazard | hazard_r_2 | 1240 | 0.329631 | 0.275962 | 0.0180467 | 0.0399142 | 0.0865134 | 0.224294 | 0.556075 | 0.823825 | 0.945162 |
| tossup_hazard | hazard_r_3 | 1240 | 0.308965 | 0.266139 | 0.022074 | 0.0431829 | 0.0900013 | 0.194459 | 0.491391 | 0.836411 | 0.94966 |
