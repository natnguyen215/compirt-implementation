# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 298104 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.667227 |
| log_loss | 0.549899 |
| ece | 0.105784 |
| brier | 0.184749 |
| accuracy | 0.719894 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0422303 |
| probability_std | 0.177595 |
| probability_p10 | 0.412096 |
| probability_p50 | 0.672174 |
| probability_p90 | 0.889638 |
| mean_predictive_variance | 0.192537 |
| integrated_brier_score | 0.102317 |
| joint_tossup_event_log_loss | 6.65373 |
| buzz_position_mae | 0.156229 |
| buzz_position_median_absolute_error | 0.139128 |
| buzz_position_bias | -0.0639178 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.323766 |
| first_buzzer_mean_reciprocal_rank | 0.540484 |
| first_buzzer_log_loss | 1.72544 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.667227 |
| neg_average_precision | 0.382394 |
| neg_precision | 0.394505 |
| neg_recall | 0.331946 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.160044 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00647949 |
| no_buzz_calibration_error | -0.0094296 |
| no_buzz_brier | 0.0150098 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.667227 | 0.549899 | 0.105784 | 0.184749 | 0.719894 | 0.762125 | -0.0422303 | 0.177595 | 0.412096 | 0.672174 | 0.889638 | 0.192537 |
| tossup_correctness | tier | fall | 2842 | 0.690569 | 0.508998 | 0.0900394 | 0.168065 | 0.74525 | 0.785362 | -0.0401126 | 0.186931 | 0.421996 | 0.736755 | 0.916157 | 0.175771 |
| tossup_correctness | tier | nationals | 1564 | 0.660282 | 0.580831 | 0.0915099 | 0.197149 | 0.70844 | 0.718031 | -0.00959079 | 0.132124 | 0.455042 | 0.639713 | 0.790574 | 0.216269 |
| tossup_correctness | tier | regionals | 1937 | 0.648239 | 0.575436 | 0.128384 | 0.195443 | 0.694373 | 0.758389 | -0.0640165 | 0.16984 | 0.400245 | 0.651007 | 0.848947 | 0.203281 |
| tossup_correctness | tier | winter | 2750 | 0.656852 | 0.556588 | 0.114313 | 0.187407 | 0.718182 | 0.765818 | -0.0476364 | 0.187987 | 0.397971 | 0.669023 | 0.904268 | 0.1888 |
| tossup_correctness | category | Current Events | 126 | 0.684323 | 0.577703 | 0.171658 | 0.198494 | 0.68254 | 0.769841 | -0.0873016 | 0.185514 | 0.366732 | 0.579539 | 0.869033 | 0.204716 |
| tossup_correctness | category | Fine Arts | 1071 | 0.68199 | 0.536372 | 0.105655 | 0.179064 | 0.739496 | 0.766573 | -0.0270775 | 0.182462 | 0.395758 | 0.67896 | 0.889592 | 0.190277 |
| tossup_correctness | category | Geography | 185 | 0.700305 | 0.591262 | 0.161432 | 0.203451 | 0.648649 | 0.697297 | -0.0486486 | 0.211874 | 0.29552 | 0.592628 | 0.831061 | 0.200432 |
| tossup_correctness | category | History | 1440 | 0.666516 | 0.551469 | 0.0929055 | 0.186553 | 0.700694 | 0.754167 | -0.0534722 | 0.179657 | 0.43222 | 0.665635 | 0.906971 | 0.189843 |
| tossup_correctness | category | Literature | 1422 | 0.660458 | 0.497735 | 0.111935 | 0.161662 | 0.779184 | 0.814346 | -0.0351617 | 0.16401 | 0.474684 | 0.717907 | 0.909728 | 0.181235 |
| tossup_correctness | category | Mythology | 318 | 0.639948 | 0.52638 | 0.122862 | 0.170701 | 0.77044 | 0.789308 | -0.0188679 | 0.172224 | 0.457332 | 0.738708 | 0.907831 | 0.176959 |
| tossup_correctness | category | Other Academic | 66 | 0.730123 | 0.547751 | 0.146527 | 0.181455 | 0.712121 | 0.712121 | 0 | 0.156522 | 0.408244 | 0.660931 | 0.781487 | 0.210978 |
| tossup_correctness | category | Philosophy | 311 | 0.631766 | 0.570386 | 0.0983339 | 0.194739 | 0.694534 | 0.745981 | -0.0514469 | 0.159049 | 0.455681 | 0.669238 | 0.879196 | 0.198089 |
| tossup_correctness | category | Popular Culture | 102 | 0.535185 | 0.411789 | 0.111196 | 0.122327 | 0.862745 | 0.882353 | -0.0196078 | 0.123293 | 0.60451 | 0.80593 | 0.920067 | 0.153771 |
| tossup_correctness | category | Religion | 358 | 0.660499 | 0.593758 | 0.10052 | 0.202778 | 0.681564 | 0.712291 | -0.0307263 | 0.17447 | 0.400251 | 0.623572 | 0.845385 | 0.204389 |
| tossup_correctness | category | Science | 1433 | 0.65814 | 0.56767 | 0.0936994 | 0.192597 | 0.706211 | 0.738311 | -0.0321005 | 0.181621 | 0.403355 | 0.674325 | 0.893194 | 0.191244 |
| tossup_correctness | category | Social Science | 324 | 0.704156 | 0.54974 | 0.0905457 | 0.186781 | 0.722222 | 0.731481 | -0.00925926 | 0.176053 | 0.385952 | 0.640793 | 0.882206 | 0.199142 |
| tossup_correctness | category | Unknown | 1937 | 0.648239 | 0.575436 | 0.128384 | 0.195443 | 0.694373 | 0.758389 | -0.0640165 | 0.16984 | 0.400245 | 0.651007 | 0.848947 | 0.203281 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.652136 | 0.590842 | 0.0741232 | 0.197397 | 0.700599 | 0.712575 | -0.011976 | 0.143933 | 0.540369 | 0.796944 | 0.92599 | 0.158651 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.70972 | 0.52996 | 0.0446658 | 0.174551 | 0.753289 | 0.729167 | 0.0241228 | 0.184501 | 0.444126 | 0.775959 | 0.926719 | 0.165059 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.720563 | 0.502938 | 0.0432176 | 0.164712 | 0.762175 | 0.755083 | 0.0070922 | 0.1751 | 0.469611 | 0.753899 | 0.922324 | 0.171902 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.667432 | 0.53598 | 0.115564 | 0.178752 | 0.734177 | 0.780942 | -0.0467651 | 0.171667 | 0.431824 | 0.677802 | 0.884289 | 0.193097 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.641817 | 0.599081 | 0.169664 | 0.206556 | 0.668412 | 0.762029 | -0.093617 | 0.158466 | 0.371397 | 0.60415 | 0.797527 | 0.216357 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 4.04215 | 0.545646 | 1.89308 | 3.147 | 3.66858 | 4.07602 | 4.40779 | 4.8996 | 5.58307 |
| player | theta_1 | 1167 | -0.205073 | 0.961486 | -2.60213 | -1.76037 | -0.923777 | -0.204697 | 0.492588 | 1.34711 | 3.28976 |
| player | theta_2 | 1167 | -0.611163 | 0.75027 | -2.56802 | -1.70742 | -1.18001 | -0.666854 | -0.120591 | 0.769379 | 1.90019 |
| player | theta_3 | 1167 | -0.472659 | 0.838983 | -2.4702 | -1.71467 | -1.06719 | -0.542616 | -0.00105289 | 1.12067 | 2.24304 |
| player | theta_norm | 1167 | 1.5623 | 0.622822 | 0.153256 | 0.565835 | 1.12194 | 1.52264 | 1.99912 | 2.64578 | 4.00162 |
| tossup | beta_1 | 1220 | -0.610809 | 0.750986 | -3.37844 | -2.2937 | -0.818747 | -0.367215 | -0.141329 | 0.166659 | 1.2004 |
| tossup | beta_2 | 1220 | -0.409503 | 0.679243 | -3.54425 | -2.19808 | -0.362613 | -0.220308 | -0.129786 | 0.115792 | 1.94394 |
| tossup | beta_3 | 1220 | -0.474757 | 0.719458 | -3.53339 | -2.35645 | -0.423464 | -0.251727 | -0.126236 | 0.139811 | 1.11991 |
| tossup | gamma_1 | 1220 | 5.44347 | 3.70068 | 0.742125 | 3.02974 | 4.37744 | 4.78571 | 5.18151 | 11.3197 | 69.0727 |
| tossup | gamma_2 | 1220 | 5.50759 | 3.27102 | 0.502853 | 4.111 | 4.61971 | 4.89191 | 5.18332 | 9.65925 | 41.2186 |
| tossup | gamma_3 | 1220 | 5.54121 | 3.5359 | 0.411781 | 3.78063 | 4.62969 | 4.8961 | 5.2038 | 9.89594 | 58.6551 |
| tossup | mu_1 | 1220 | 0.563407 | 0.119585 | 0.44648 | 0.474485 | 0.495614 | 0.512338 | 0.563173 | 0.871647 | 0.962162 |
| tossup | mu_2 | 1220 | 0.537899 | 0.103934 | 0.452796 | 0.476546 | 0.493624 | 0.505306 | 0.519416 | 0.847548 | 0.969231 |
| tossup | mu_3 | 1220 | 0.547175 | 0.113369 | 0.452579 | 0.476758 | 0.493655 | 0.507162 | 0.524314 | 0.874165 | 0.981292 |
| tossup | r_1 | 1220 | 0.409922 | 0.239172 | 0.0398627 | 0.0806492 | 0.192149 | 0.385473 | 0.61404 | 0.807136 | 0.888908 |
| tossup | r_2 | 1220 | 0.272104 | 0.211536 | 0.0436427 | 0.0681417 | 0.11462 | 0.190872 | 0.370061 | 0.767623 | 0.901814 |
| tossup | r_3 | 1220 | 0.317974 | 0.222444 | 0.0478426 | 0.0820201 | 0.144186 | 0.252802 | 0.422943 | 0.809473 | 0.902021 |
| tossup | r_norm | 1220 | 0.697483 | 0.0895305 | 0.577357 | 0.584235 | 0.619294 | 0.673563 | 0.774775 | 0.854211 | 0.904743 |
| tossup_hazard | hazard_beta_1 | 1220 | 1.9233 | 1.47792 | -0.0234459 | 0.420999 | 0.674246 | 1.16026 | 3.52405 | 4.42893 | 5.60965 |
| tossup_hazard | hazard_beta_2 | 1220 | 2.00717 | 1.304 | 0.145006 | 0.390335 | 0.714685 | 1.75903 | 3.32214 | 3.95952 | 4.94441 |
| tossup_hazard | hazard_beta_3 | 1220 | 1.85054 | 1.40045 | -0.106898 | 0.370379 | 0.670543 | 1.16097 | 3.28204 | 4.2678 | 5.01168 |
| tossup_hazard | hazard_gamma_1 | 1220 | 13.1371 | 32.7337 | 3.70486 | 5.47735 | 6.25555 | 7.21813 | 10.7336 | 38.221 | 921.663 |
| tossup_hazard | hazard_gamma_2 | 1220 | 14.9969 | 23.0801 | 3.67053 | 5.57005 | 6.45391 | 8.32945 | 13.274 | 47.4148 | 277.584 |
| tossup_hazard | hazard_gamma_3 | 1220 | 14.046 | 33.004 | 2.9772 | 5.50275 | 6.2869 | 7.4857 | 10.7061 | 37.0049 | 634.129 |
| tossup_hazard | hazard_mu_1 | 1220 | 0.601919 | 0.105676 | 0.301362 | 0.48965 | 0.53145 | 0.565469 | 0.649316 | 0.824209 | 0.953614 |
| tossup_hazard | hazard_mu_2 | 1220 | 0.597574 | 0.110144 | 0.210478 | 0.464376 | 0.525416 | 0.56443 | 0.668682 | 0.809599 | 0.965979 |
| tossup_hazard | hazard_mu_3 | 1220 | 0.599014 | 0.105039 | 0.248479 | 0.48817 | 0.527684 | 0.564838 | 0.65011 | 0.814792 | 0.968554 |
| tossup_hazard | hazard_r_1 | 1220 | 0.310623 | 0.341506 | 0.0194059 | 0.0334927 | 0.0501499 | 0.0943081 | 0.687821 | 0.914322 | 0.955148 |
| tossup_hazard | hazard_r_2 | 1220 | 0.384029 | 0.347203 | 0.0140362 | 0.027204 | 0.061082 | 0.210954 | 0.783033 | 0.899693 | 0.955416 |
| tossup_hazard | hazard_r_3 | 1220 | 0.305348 | 0.322341 | 0.0145139 | 0.0295728 | 0.0554953 | 0.126005 | 0.603266 | 0.897726 | 0.949947 |
