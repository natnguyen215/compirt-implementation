# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-6000/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-6000/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 6000 |
| pyramidal | final_loss | 279030 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.708974 |
| log_loss | 0.498245 |
| ece | 0.0158316 |
| brier | 0.162092 |
| accuracy | 0.771363 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00923788 |
| probability_std | 0.150053 |
| probability_p10 | 0.560962 |
| probability_p50 | 0.810575 |
| probability_p90 | 0.923674 |
| mean_predictive_variance | 0.153589 |
| integrated_brier_score | 0.0960105 |
| joint_tossup_event_log_loss | 6.50637 |
| buzz_position_mae | 0.143363 |
| buzz_position_median_absolute_error | 0.124143 |
| buzz_position_bias | -0.0278376 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.360497 |
| first_buzzer_mean_reciprocal_rank | 0.572724 |
| first_buzzer_log_loss | 1.65482 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.708974 |
| neg_average_precision | 0.442585 |
| neg_precision | 0.57 |
| neg_recall | 0.158114 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.185443 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0117465 |
| no_buzz_calibration_error | -0.00416257 |
| no_buzz_brier | 0.0156652 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.708974 | 0.498245 | 0.0158316 | 0.162092 | 0.771363 | 0.762125 | 0.00923788 | 0.150053 | 0.560962 | 0.810575 | 0.923674 | 0.153589 |
| tossup_correctness | tier | fall | 2842 | 0.727433 | 0.464434 | 0.0134653 | 0.14926 | 0.790992 | 0.785362 | 0.00562984 | 0.144058 | 0.567592 | 0.823172 | 0.930273 | 0.149213 |
| tossup_correctness | tier | nationals | 1564 | 0.716239 | 0.539205 | 0.0440202 | 0.17935 | 0.737212 | 0.718031 | 0.0191816 | 0.15799 | 0.538724 | 0.79919 | 0.917601 | 0.158045 |
| tossup_correctness | tier | regionals | 1937 | 0.688405 | 0.513047 | 0.0257182 | 0.167741 | 0.759938 | 0.758389 | 0.00154879 | 0.145445 | 0.568392 | 0.807422 | 0.918453 | 0.1557 |
| tossup_correctness | tier | winter | 2750 | 0.697742 | 0.499467 | 0.015181 | 0.161558 | 0.778545 | 0.765818 | 0.0127273 | 0.153861 | 0.557354 | 0.810024 | 0.92259 | 0.154091 |
| tossup_correctness | category | Current Events | 126 | 0.726982 | 0.486073 | 0.0867073 | 0.157688 | 0.801587 | 0.769841 | 0.031746 | 0.131178 | 0.540372 | 0.76749 | 0.891636 | 0.174898 |
| tossup_correctness | category | Fine Arts | 1071 | 0.749929 | 0.469844 | 0.0278216 | 0.151986 | 0.78338 | 0.766573 | 0.0168067 | 0.15967 | 0.546446 | 0.806056 | 0.926488 | 0.154109 |
| tossup_correctness | category | Geography | 185 | 0.791528 | 0.497 | 0.0823069 | 0.163834 | 0.735135 | 0.697297 | 0.0378378 | 0.224965 | 0.328792 | 0.752589 | 0.900616 | 0.166356 |
| tossup_correctness | category | History | 1440 | 0.704506 | 0.513653 | 0.0285116 | 0.168653 | 0.760417 | 0.754167 | 0.00625 | 0.14792 | 0.559169 | 0.811448 | 0.928874 | 0.152191 |
| tossup_correctness | category | Literature | 1422 | 0.675956 | 0.454313 | 0.0190308 | 0.143111 | 0.809423 | 0.814346 | -0.00492264 | 0.132552 | 0.626085 | 0.838594 | 0.935822 | 0.139621 |
| tossup_correctness | category | Mythology | 318 | 0.6563 | 0.487366 | 0.0448348 | 0.153709 | 0.801887 | 0.789308 | 0.0125786 | 0.126812 | 0.634544 | 0.831692 | 0.9309 | 0.14517 |
| tossup_correctness | category | Other Academic | 66 | 0.795073 | 0.51742 | 0.0832832 | 0.17434 | 0.727273 | 0.712121 | 0.0151515 | 0.137757 | 0.608015 | 0.802544 | 0.891382 | 0.160784 |
| tossup_correctness | category | Philosophy | 311 | 0.717809 | 0.514061 | 0.0805682 | 0.171595 | 0.73955 | 0.745981 | -0.00643087 | 0.138942 | 0.598577 | 0.812397 | 0.919522 | 0.152563 |
| tossup_correctness | category | Popular Culture | 102 | 0.519444 | 0.383823 | 0.0570234 | 0.109436 | 0.882353 | 0.882353 | 0 | 0.0785975 | 0.716151 | 0.858719 | 0.913433 | 0.132079 |
| tossup_correctness | category | Religion | 358 | 0.71521 | 0.540804 | 0.0203303 | 0.17986 | 0.740223 | 0.712291 | 0.027933 | 0.159797 | 0.489831 | 0.781257 | 0.901123 | 0.170352 |
| tossup_correctness | category | Science | 1433 | 0.696187 | 0.527414 | 0.035248 | 0.173795 | 0.757153 | 0.738311 | 0.0188416 | 0.152128 | 0.540762 | 0.79941 | 0.917798 | 0.158921 |
| tossup_correctness | category | Social Science | 324 | 0.779815 | 0.484998 | 0.0606485 | 0.158373 | 0.762346 | 0.731481 | 0.0308642 | 0.160313 | 0.493768 | 0.793931 | 0.89628 | 0.163646 |
| tossup_correctness | category | Unknown | 1937 | 0.688405 | 0.513047 | 0.0257182 | 0.167741 | 0.759938 | 0.758389 | 0.00154879 | 0.145445 | 0.568392 | 0.807422 | 0.918453 | 0.1557 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.595938 | 0.6216 | 0.0777709 | 0.209146 | 0.688623 | 0.712575 | -0.0239521 | 0.139038 | 0.556318 | 0.776958 | 0.891363 | 0.17236 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.722158 | 0.522816 | 0.0314441 | 0.172924 | 0.753289 | 0.729167 | 0.0241228 | 0.16531 | 0.509853 | 0.785423 | 0.908362 | 0.163884 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.712549 | 0.503809 | 0.026526 | 0.164575 | 0.766903 | 0.755083 | 0.0118203 | 0.142832 | 0.587815 | 0.81376 | 0.923228 | 0.152082 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.69102 | 0.485559 | 0.012608 | 0.156021 | 0.78692 | 0.780942 | 0.0059775 | 0.13417 | 0.605488 | 0.822025 | 0.924429 | 0.148726 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.720868 | 0.492126 | 0.0130776 | 0.160218 | 0.769885 | 0.762029 | 0.00785597 | 0.161949 | 0.52091 | 0.806946 | 0.927849 | 0.15506 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 1.92928 | 0.768126 | -0.31311 | 0.711553 | 1.40353 | 1.92903 | 2.43853 | 3.27626 | 4.01575 |
| player | theta_1 | 1167 | -0.856547 | 0.89696 | -3.32221 | -2.14813 | -1.45201 | -0.947931 | -0.320938 | 0.727564 | 2.43871 |
| player | theta_2 | 1167 | -0.665851 | 0.810087 | -3.15495 | -1.97673 | -1.18481 | -0.726908 | -0.197252 | 0.749851 | 2.30571 |
| player | theta_3 | 1167 | -0.686586 | 0.89353 | -3.3371 | -1.9649 | -1.26358 | -0.784491 | -0.177577 | 0.929029 | 2.4704 |
| player | theta_norm | 1167 | 1.87767 | 0.616724 | 0.523216 | 0.892768 | 1.45683 | 1.8183 | 2.27543 | 2.97196 | 3.90429 |
| tossup | start_difficulty_d1 | 1220 | -1.36725 | 0.535191 | -2.74882 | -2.1196 | -1.72055 | -1.40487 | -1.06376 | -0.535636 | 1.67992 |
| tossup | start_difficulty_d2 | 1220 | -1.35947 | 0.498892 | -2.85963 | -2.08627 | -1.69959 | -1.38952 | -1.07823 | -0.466149 | 0.810635 |
| tossup | start_difficulty_d3 | 1220 | -1.36554 | 0.495783 | -3.18325 | -2.14381 | -1.69747 | -1.35239 | -1.05636 | -0.613838 | 0.713821 |
| tossup | end_difficulty_d1 | 1220 | -2.36129 | 0.625847 | -4.09826 | -3.26072 | -2.76933 | -2.40725 | -2.00012 | -1.39068 | 1.08428 |
| tossup | end_difficulty_d2 | 1220 | -2.35159 | 0.581135 | -4.13482 | -3.20104 | -2.75934 | -2.38023 | -2.01211 | -1.32926 | -0.0730253 |
| tossup | end_difficulty_d3 | 1220 | -2.35893 | 0.582147 | -4.52814 | -3.29803 | -2.75193 | -2.335 | -1.98722 | -1.47782 | -0.0236778 |
| tossup | total_drop_d1 | 1220 | 0.994039 | 0.111659 | 0.59564 | 0.804673 | 0.925605 | 0.993795 | 1.0655 | 1.18063 | 1.37686 |
| tossup | total_drop_d2 | 1220 | 0.992122 | 0.101195 | 0.621884 | 0.819756 | 0.929784 | 0.992633 | 1.06206 | 1.15116 | 1.35418 |
| tossup | total_drop_d3 | 1220 | 0.993391 | 0.104725 | 0.617696 | 0.830281 | 0.925362 | 0.988399 | 1.05926 | 1.16898 | 1.42113 |
| tossup | drop_share_1_d1 | 1220 | 0.303537 | 0.0150301 | 0.225598 | 0.279328 | 0.294582 | 0.303971 | 0.313486 | 0.326459 | 0.345719 |
| tossup | drop_share_2_d1 | 1220 | 0.347493 | 0.0111354 | 0.313738 | 0.329215 | 0.339988 | 0.347385 | 0.354474 | 0.366492 | 0.38551 |
| tossup | drop_share_3_d1 | 1220 | 0.34897 | 0.0158894 | 0.296115 | 0.324477 | 0.338416 | 0.348164 | 0.358444 | 0.375719 | 0.435451 |
| tossup | drop_share_1_d2 | 1220 | 0.304073 | 0.0144808 | 0.245578 | 0.280082 | 0.295455 | 0.304798 | 0.313263 | 0.32652 | 0.352368 |
| tossup | drop_share_2_d2 | 1220 | 0.347013 | 0.0111697 | 0.309708 | 0.328806 | 0.339642 | 0.347266 | 0.35392 | 0.365915 | 0.39066 |
| tossup | drop_share_3_d2 | 1220 | 0.348914 | 0.0157262 | 0.299427 | 0.324654 | 0.338341 | 0.348141 | 0.358561 | 0.376631 | 0.411509 |
| tossup | drop_share_1_d3 | 1220 | 0.303434 | 0.0143656 | 0.247668 | 0.28115 | 0.294384 | 0.303375 | 0.312829 | 0.325897 | 0.352396 |
| tossup | drop_share_2_d3 | 1220 | 0.347188 | 0.01101 | 0.314057 | 0.329815 | 0.339022 | 0.347149 | 0.354358 | 0.365208 | 0.381383 |
| tossup | drop_share_3_d3 | 1220 | 0.349377 | 0.015172 | 0.298472 | 0.326034 | 0.339969 | 0.349009 | 0.357833 | 0.375337 | 0.415561 |
| tossup | r_1 | 1220 | 0.32366 | 0.16461 | 0.0495489 | 0.111252 | 0.193852 | 0.288249 | 0.433917 | 0.636948 | 0.882961 |
| tossup | r_2 | 1220 | 0.336069 | 0.163801 | 0.0449699 | 0.114967 | 0.21677 | 0.298094 | 0.437389 | 0.659076 | 0.859898 |
| tossup | r_3 | 1220 | 0.340271 | 0.164684 | 0.0528169 | 0.120547 | 0.211997 | 0.314111 | 0.442714 | 0.655087 | 0.86174 |
| tossup | r_norm | 1220 | 0.641128 | 0.0584978 | 0.577378 | 0.581639 | 0.597629 | 0.622731 | 0.666181 | 0.768234 | 0.886868 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 6.20794 | 0.541156 | 3.21886 | 5.38431 | 5.9502 | 6.13072 | 6.44554 | 7.21642 | 8.41074 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 6.16625 | 0.474408 | 3.08755 | 5.45727 | 6.00299 | 6.12085 | 6.29503 | 7.01597 | 8.55486 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 6.19141 | 0.471462 | 3.32715 | 5.44941 | 6.01803 | 6.15788 | 6.38096 | 6.99667 | 8.30328 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 2.86161 | 3.00632 | -13.2355 | -3.00311 | 0.988447 | 4.70859 | 5.08154 | 5.42078 | 6.2134 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 3.46948 | 2.93608 | -11.6465 | -2.58173 | 2.33389 | 5.00068 | 5.15431 | 5.46176 | 6.27556 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 3.67847 | 2.8996 | -11.6903 | -2.78437 | 3.68194 | 5.04339 | 5.21536 | 5.52803 | 6.33691 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 3.34632 | 3.14858 | 0.838735 | 0.957508 | 1.01785 | 1.15967 | 5.54505 | 9.42104 | 19.8029 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.69677 | 3.06672 | 0.862625 | 0.947559 | 0.995684 | 1.04642 | 3.52781 | 9.43437 | 18.2244 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.51294 | 2.99045 | 0.86962 | 0.93911 | 0.993336 | 1.03774 | 1.82637 | 9.11427 | 18.6068 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.240511 | 0.0898847 | 0.0335856 | 0.0838862 | 0.158932 | 0.283044 | 0.30215 | 0.321719 | 0.641373 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.333832 | 0.0898495 | 0.0597894 | 0.152274 | 0.327036 | 0.34703 | 0.361056 | 0.467338 | 0.712393 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.425657 | 0.147777 | 0.0916158 | 0.273496 | 0.344556 | 0.360812 | 0.476404 | 0.755283 | 0.892066 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.261195 | 0.082074 | 0.0320309 | 0.0905427 | 0.259355 | 0.292586 | 0.304221 | 0.320271 | 0.68015 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.339207 | 0.0777375 | 0.0613013 | 0.165054 | 0.336273 | 0.348398 | 0.358695 | 0.438335 | 0.706794 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.399598 | 0.130302 | 0.0828545 | 0.307975 | 0.343469 | 0.356083 | 0.377398 | 0.73197 | 0.900797 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.264127 | 0.0769007 | 0.0405965 | 0.0859253 | 0.263123 | 0.291514 | 0.304129 | 0.322309 | 0.671 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.343248 | 0.0672778 | 0.0794641 | 0.196824 | 0.337885 | 0.349131 | 0.359622 | 0.428825 | 0.695256 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.392625 | 0.115786 | 0.0666246 | 0.310193 | 0.344438 | 0.357461 | 0.378295 | 0.703623 | 0.87724 |
| tossup_hazard | hazard_r_1 | 1220 | 0.400007 | 0.301145 | 0.0186854 | 0.0402703 | 0.107627 | 0.323862 | 0.681325 | 0.882699 | 0.945993 |
| tossup_hazard | hazard_r_2 | 1220 | 0.297631 | 0.272373 | 0.0108485 | 0.0329317 | 0.0757189 | 0.17351 | 0.517247 | 0.842076 | 0.925741 |
| tossup_hazard | hazard_r_3 | 1220 | 0.302363 | 0.259327 | 0.0158895 | 0.0319034 | 0.0840181 | 0.216817 | 0.472756 | 0.821506 | 0.970466 |
