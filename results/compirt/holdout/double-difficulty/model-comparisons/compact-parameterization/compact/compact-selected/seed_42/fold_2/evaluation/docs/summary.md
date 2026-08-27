# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_2/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 278202 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.700539 |
| log_loss | 0.520366 |
| ece | 0.0591076 |
| brier | 0.169415 |
| accuracy | 0.76245 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00172842 |
| probability_std | 0.207951 |
| probability_p10 | 0.441179 |
| probability_p50 | 0.820583 |
| probability_p90 | 0.956284 |
| mean_predictive_variance | 0.142002 |
| integrated_brier_score | 0.0954239 |
| joint_tossup_event_log_loss | 6.42889 |
| buzz_position_mae | 0.141489 |
| buzz_position_median_absolute_error | 0.120857 |
| buzz_position_bias | -0.0250245 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.395484 |
| first_buzzer_mean_reciprocal_rank | 0.601722 |
| first_buzzer_log_loss | 1.56245 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.700539 |
| neg_average_precision | 0.420499 |
| neg_precision | 0.493289 |
| neg_recall | 0.269354 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.178925 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.00882969 |
| no_buzz_calibration_error | -0.00428332 |
| no_buzz_brier | 0.0122794 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.700539 | 0.520366 | 0.0591076 | 0.169415 | 0.76245 | 0.764178 | -0.00172842 | 0.207951 | 0.441179 | 0.820583 | 0.956284 | 0.142002 |
| tossup_correctness | tier | fall | 2798 | 0.717788 | 0.48292 | 0.040772 | 0.155507 | 0.782702 | 0.785204 | -0.00250179 | 0.197981 | 0.466505 | 0.823827 | 0.95471 | 0.142539 |
| tossup_correctness | tier | nationals | 1545 | 0.702366 | 0.563651 | 0.0797701 | 0.187786 | 0.721683 | 0.721036 | 0.000647249 | 0.214016 | 0.407882 | 0.800915 | 0.952299 | 0.14652 |
| tossup_correctness | tier | regionals | 2039 | 0.693646 | 0.530855 | 0.0694946 | 0.172079 | 0.762629 | 0.762138 | 0.000490436 | 0.213008 | 0.451131 | 0.81649 | 0.961284 | 0.140051 |
| tossup_correctness | tier | winter | 2875 | 0.687288 | 0.526109 | 0.0660015 | 0.171189 | 0.764522 | 0.768348 | -0.00382609 | 0.210097 | 0.425545 | 0.827513 | 0.95572 | 0.140434 |
| tossup_correctness | category | Current Events | 129 | 0.697945 | 0.613315 | 0.127839 | 0.21071 | 0.689922 | 0.666667 | 0.0232558 | 0.203878 | 0.440226 | 0.806289 | 0.958164 | 0.144283 |
| tossup_correctness | category | Fine Arts | 1074 | 0.685731 | 0.504303 | 0.0610855 | 0.162016 | 0.778399 | 0.776536 | 0.0018622 | 0.193595 | 0.459538 | 0.818558 | 0.948969 | 0.146211 |
| tossup_correctness | category | Geography | 180 | 0.746834 | 0.574412 | 0.0969749 | 0.193971 | 0.733333 | 0.616667 | 0.116667 | 0.255325 | 0.236782 | 0.762615 | 0.935078 | 0.15581 |
| tossup_correctness | category | History | 1454 | 0.67528 | 0.550666 | 0.073 | 0.1798 | 0.755846 | 0.757909 | -0.00206327 | 0.212056 | 0.415074 | 0.807714 | 0.953382 | 0.144115 |
| tossup_correctness | category | Literature | 1435 | 0.728324 | 0.458406 | 0.0520978 | 0.146044 | 0.78676 | 0.810453 | -0.0236934 | 0.21031 | 0.47473 | 0.859885 | 0.968029 | 0.124775 |
| tossup_correctness | category | Mythology | 324 | 0.658343 | 0.494743 | 0.0450461 | 0.156155 | 0.796296 | 0.79321 | 0.00308642 | 0.145504 | 0.58721 | 0.855417 | 0.943836 | 0.134013 |
| tossup_correctness | category | Other Academic | 71 | 0.663399 | 0.526348 | 0.0739482 | 0.172415 | 0.760563 | 0.760563 | 0 | 0.14171 | 0.550854 | 0.800634 | 0.938188 | 0.150455 |
| tossup_correctness | category | Philosophy | 310 | 0.735513 | 0.49328 | 0.0553985 | 0.161703 | 0.76129 | 0.76129 | 0 | 0.193799 | 0.488196 | 0.818486 | 0.949933 | 0.14536 |
| tossup_correctness | category | Popular Culture | 108 | 0.440104 | 0.38643 | 0.0618862 | 0.109147 | 0.888889 | 0.888889 | 0 | 0.0802021 | 0.750663 | 0.884602 | 0.937837 | 0.112551 |
| tossup_correctness | category | Religion | 361 | 0.697962 | 0.533929 | 0.0475745 | 0.179717 | 0.742382 | 0.742382 | 0 | 0.186694 | 0.439315 | 0.74667 | 0.920786 | 0.170545 |
| tossup_correctness | category | Science | 1445 | 0.693448 | 0.546102 | 0.073552 | 0.180712 | 0.738408 | 0.746021 | -0.00761246 | 0.213924 | 0.40851 | 0.807335 | 0.951006 | 0.148025 |
| tossup_correctness | category | Social Science | 327 | 0.734505 | 0.543772 | 0.0630298 | 0.182085 | 0.730887 | 0.718654 | 0.0122324 | 0.220329 | 0.358595 | 0.781704 | 0.942794 | 0.152538 |
| tossup_correctness | category | Unknown | 2039 | 0.693646 | 0.530855 | 0.0694946 | 0.172079 | 0.762629 | 0.762138 | 0.000490436 | 0.213008 | 0.451131 | 0.81649 | 0.961284 | 0.140051 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.720588 | 0.518073 | 0.0639806 | 0.17071 | 0.765027 | 0.743169 | 0.0218579 | 0.203849 | 0.445262 | 0.806025 | 0.950591 | 0.150943 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.714718 | 0.54111 | 0.0582525 | 0.17492 | 0.750785 | 0.728796 | 0.0219895 | 0.196676 | 0.477002 | 0.831955 | 0.957977 | 0.138432 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.709237 | 0.524636 | 0.053986 | 0.17073 | 0.765074 | 0.752568 | 0.0125056 | 0.197808 | 0.47528 | 0.840865 | 0.958904 | 0.135013 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.696259 | 0.494553 | 0.0572613 | 0.16016 | 0.776696 | 0.786087 | -0.0093913 | 0.193385 | 0.502527 | 0.836269 | 0.960008 | 0.136391 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.697729 | 0.535427 | 0.069229 | 0.175461 | 0.750416 | 0.764393 | -0.0139767 | 0.225762 | 0.369898 | 0.781193 | 0.946495 | 0.153167 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.03863 | 0.581348 | 0.229061 | 1.08489 | 1.61961 | 2.05088 | 2.45522 | 2.94314 | 3.77363 |
| player | theta_1 | 1197 | -1.38827 | 0.658212 | -3.60589 | -2.43543 | -1.87616 | -1.3659 | -0.946584 | -0.263906 | 0.362397 |
| player | theta_2 | 1197 | -1.31023 | 0.649169 | -3.7002 | -2.34723 | -1.79302 | -1.31192 | -0.825645 | -0.263274 | 0.484035 |
| player | theta_3 | 1197 | -1.27844 | 0.649429 | -3.05583 | -2.29074 | -1.79304 | -1.28691 | -0.824477 | -0.185266 | 0.559976 |
| player | theta_norm | 1197 | 2.48638 | 0.609904 | 0.811918 | 1.51729 | 2.03882 | 2.46904 | 2.91235 | 3.54209 | 4.24487 |
| tossup | start_difficulty | 1240 | -3.22639 | 0.788485 | -5.39324 | -4.49256 | -3.75954 | -3.24021 | -2.69554 | -1.87427 | -0.661528 |
| tossup | end_difficulty | 1240 | -4.25257 | 0.960756 | -7.37205 | -5.86199 | -4.86826 | -4.22417 | -3.58473 | -2.70616 | -1.39091 |
| tossup | total_drop | 1240 | 1.02618 | 0.296176 | 0.577043 | 0.726895 | 0.856032 | 0.963904 | 1.1087 | 1.5232 | 3.41076 |
| tossup | drop_share_1 | 1240 | 0.294228 | 0.0285001 | 0.126884 | 0.24341 | 0.280704 | 0.29679 | 0.312008 | 0.334904 | 0.401495 |
| tossup | drop_share_2 | 1240 | 0.34801 | 0.016978 | 0.206278 | 0.324124 | 0.338271 | 0.347132 | 0.357042 | 0.373875 | 0.469628 |
| tossup | drop_share_3 | 1240 | 0.357762 | 0.0317048 | 0.270145 | 0.314776 | 0.338898 | 0.354036 | 0.372368 | 0.409105 | 0.666839 |
| tossup | r_1 | 1240 | 0.980394 | 0.783618 | 0.0347421 | 0.137114 | 0.381579 | 0.744344 | 1.37044 | 2.65126 | 4.47647 |
| tossup | r_2 | 1240 | 0.796421 | 0.622572 | 0.04143 | 0.125694 | 0.315346 | 0.601638 | 1.1375 | 2.05627 | 3.17602 |
| tossup | r_3 | 1240 | 0.787338 | 0.696123 | 0.0367627 | 0.118907 | 0.288247 | 0.561466 | 1.001 | 2.33629 | 3.70609 |
| tossup | r_norm | 1240 | 1.81418 | 0.639902 | 0.426224 | 0.875037 | 1.34615 | 1.77847 | 2.19875 | 2.98532 | 4.50992 |
| tossup_hazard | hazard_start_difficulty | 1240 | 3.79674 | 0.612031 | 1.72361 | 2.80397 | 3.36209 | 3.80266 | 4.22881 | 4.78957 | 5.71231 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.10611 | 1.53014 | -6.90274 | -3.6931 | -2.09511 | -1.1606 | -0.0616283 | 1.41163 | 3.10108 |
| tossup_hazard | hazard_total_drop | 1240 | 4.90286 | 1.49969 | 0.70389 | 2.3846 | 3.98635 | 4.886 | 5.82668 | 7.39217 | 11.7565 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.160245 | 0.0884502 | 0.0337368 | 0.067387 | 0.0996622 | 0.135389 | 0.194759 | 0.327071 | 0.646397 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.314348 | 0.133754 | 0.0586248 | 0.118589 | 0.20912 | 0.308524 | 0.398861 | 0.549934 | 0.728862 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.525407 | 0.185871 | 0.0629575 | 0.210493 | 0.379269 | 0.535047 | 0.675876 | 0.804514 | 0.892501 |
