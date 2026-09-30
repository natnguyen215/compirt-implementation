# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 301526 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.720521 |
| log_loss | 0.494261 |
| ece | 0.0765882 |
| brier | 0.16071 |
| accuracy | 0.777994 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00463862 |
| probability_std | 0.162716 |
| probability_p10 | 0.467033 |
| probability_p50 | 0.719885 |
| probability_p90 | 0.888786 |
| mean_predictive_variance | 0.184667 |
| integrated_brier_score | 0.110038 |
| joint_tossup_event_log_loss | 6.72094 |
| buzz_position_mae | 0.165635 |
| buzz_position_median_absolute_error | 0.1499 |
| buzz_position_bias | -0.0785735 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.345739 |
| first_buzzer_mean_reciprocal_rank | 0.55771 |
| first_buzzer_log_loss | 1.69918 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.720521 |
| neg_average_precision | 0.454465 |
| neg_precision | 0.518205 |
| neg_recall | 0.29129 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.175526 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0116924 |
| no_buzz_calibration_error | -3.47284e-05 |
| no_buzz_brier | 0.0107158 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.720521 | 0.494261 | 0.0765882 | 0.16071 | 0.777994 | 0.773355 | 0.00463862 | 0.162716 | 0.467033 | 0.719885 | 0.888786 | 0.184667 |
| tossup_correctness | tier | fall | 2876 | 0.721202 | 0.468693 | 0.0692704 | 0.150491 | 0.794854 | 0.793115 | 0.00173853 | 0.15711 | 0.49826 | 0.752181 | 0.911173 | 0.174297 |
| tossup_correctness | tier | nationals | 1579 | 0.711265 | 0.540656 | 0.0794378 | 0.180573 | 0.737175 | 0.729576 | 0.00759975 | 0.16284 | 0.419176 | 0.672 | 0.847329 | 0.200882 |
| tossup_correctness | tier | regionals | 1990 | 0.737271 | 0.501566 | 0.094067 | 0.163405 | 0.777387 | 0.765829 | 0.0115578 | 0.162728 | 0.44427 | 0.694303 | 0.868291 | 0.193463 |
| tossup_correctness | tier | winter | 2825 | 0.70622 | 0.489214 | 0.0745298 | 0.158113 | 0.784071 | 0.783009 | 0.00106195 | 0.16009 | 0.485108 | 0.736791 | 0.895059 | 0.179963 |
| tossup_correctness | category | Current Events | 123 | 0.77036 | 0.490492 | 0.117953 | 0.161164 | 0.747967 | 0.764228 | -0.0162602 | 0.162196 | 0.423662 | 0.667945 | 0.843104 | 0.1984 |
| tossup_correctness | category | Fine Arts | 1093 | 0.726525 | 0.486267 | 0.0677804 | 0.156954 | 0.78957 | 0.769442 | 0.0201281 | 0.16176 | 0.483604 | 0.731542 | 0.892689 | 0.18101 |
| tossup_correctness | category | Geography | 191 | 0.763867 | 0.516538 | 0.087817 | 0.16922 | 0.78534 | 0.691099 | 0.0942408 | 0.194589 | 0.362772 | 0.677906 | 0.835431 | 0.196053 |
| tossup_correctness | category | History | 1469 | 0.719304 | 0.508326 | 0.0569467 | 0.167649 | 0.754935 | 0.758339 | -0.00340368 | 0.16403 | 0.474825 | 0.724898 | 0.897313 | 0.182535 |
| tossup_correctness | category | Literature | 1436 | 0.701671 | 0.456652 | 0.077888 | 0.144862 | 0.804318 | 0.81546 | -0.0111421 | 0.152647 | 0.523267 | 0.77514 | 0.913444 | 0.168823 |
| tossup_correctness | category | Mythology | 325 | 0.65214 | 0.458011 | 0.118842 | 0.145213 | 0.821538 | 0.843077 | -0.0215385 | 0.134575 | 0.5521 | 0.737666 | 0.891392 | 0.180871 |
| tossup_correctness | category | Other Academic | 67 | 0.59973 | 0.576011 | 0.184811 | 0.197124 | 0.671642 | 0.791045 | -0.119403 | 0.150191 | 0.425112 | 0.651975 | 0.823401 | 0.208982 |
| tossup_correctness | category | Philosophy | 322 | 0.691642 | 0.490928 | 0.0699084 | 0.160126 | 0.782609 | 0.785714 | -0.00310559 | 0.146058 | 0.513721 | 0.720355 | 0.904191 | 0.182095 |
| tossup_correctness | category | Popular Culture | 100 | 0.409602 | 0.428151 | 0.130474 | 0.129077 | 0.87 | 0.89 | -0.02 | 0.109484 | 0.647103 | 0.810568 | 0.898232 | 0.157591 |
| tossup_correctness | category | Religion | 365 | 0.681781 | 0.55965 | 0.0562644 | 0.18777 | 0.717808 | 0.723288 | -0.00547945 | 0.159194 | 0.451483 | 0.685923 | 0.880687 | 0.19404 |
| tossup_correctness | category | Science | 1456 | 0.719048 | 0.499329 | 0.0813892 | 0.162638 | 0.774725 | 0.76717 | 0.00755495 | 0.16196 | 0.465175 | 0.714406 | 0.875471 | 0.187698 |
| tossup_correctness | category | Social Science | 333 | 0.750389 | 0.513779 | 0.0908657 | 0.169388 | 0.765766 | 0.72973 | 0.036036 | 0.176294 | 0.382784 | 0.669288 | 0.862826 | 0.19612 |
| tossup_correctness | category | Unknown | 1990 | 0.737271 | 0.501566 | 0.094067 | 0.163405 | 0.777387 | 0.765829 | 0.0115578 | 0.162728 | 0.44427 | 0.694303 | 0.868291 | 0.193463 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.69801 | 0.544841 | 0.128612 | 0.181994 | 0.748603 | 0.748603 | 0 | 0.179049 | 0.385826 | 0.666083 | 0.835387 | 0.200148 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.702358 | 0.52608 | 0.0935397 | 0.1737 | 0.761755 | 0.754441 | 0.00731452 | 0.168062 | 0.427721 | 0.681894 | 0.878235 | 0.193755 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.719662 | 0.500372 | 0.0710156 | 0.163249 | 0.773491 | 0.766682 | 0.0068089 | 0.165551 | 0.466756 | 0.717116 | 0.895727 | 0.184235 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.719004 | 0.480247 | 0.0773016 | 0.154974 | 0.786434 | 0.787441 | -0.00100739 | 0.157708 | 0.490066 | 0.736465 | 0.895934 | 0.180796 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.729502 | 0.490458 | 0.0742829 | 0.1591 | 0.779885 | 0.771758 | 0.00812733 | 0.160536 | 0.469395 | 0.720832 | 0.885685 | 0.185008 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 4.39751 | 0.552828 | 2.42506 | 3.47967 | 4.03179 | 4.41761 | 4.78134 | 5.29294 | 5.80907 |
| player | theta_1 | 1196 | -1.2868 | 0.961159 | -3.39364 | -2.55324 | -1.9822 | -1.46483 | -0.756453 | 0.660087 | 2.62175 |
| player | theta_2 | 1196 | -1.0521 | 0.729452 | -3.21065 | -2.04623 | -1.55645 | -1.13647 | -0.661493 | 0.299873 | 1.90805 |
| player | theta_3 | 1196 | -1.05766 | 0.636885 | -2.99398 | -2.02316 | -1.50338 | -1.12047 | -0.655415 | 0.110136 | 1.37397 |
| player | theta_norm | 1196 | 2.30201 | 0.665228 | 0.231097 | 1.18963 | 1.83431 | 2.33434 | 2.77625 | 3.35406 | 4.28334 |
| tossup | start_difficulty_d1 | 1240 | -0.76784 | 0.659247 | -3.51306 | -2.0556 | -1.09773 | -0.679894 | -0.376312 | 0.218846 | 1.59006 |
| tossup | start_difficulty_d2 | 1240 | -0.635194 | 0.507517 | -2.96621 | -1.50804 | -0.848384 | -0.605259 | -0.372758 | 0.143852 | 1.39237 |
| tossup | start_difficulty_d3 | 1240 | -0.655869 | 0.537127 | -3.1762 | -1.74877 | -0.853157 | -0.607013 | -0.389893 | 0.137966 | 1.53415 |
| tossup | end_difficulty_d1 | 1240 | -1.94129 | 0.854978 | -5.40501 | -3.60814 | -2.36051 | -1.82025 | -1.42807 | -0.710176 | 0.817815 |
| tossup | end_difficulty_d2 | 1240 | -1.76946 | 0.65109 | -5.16536 | -2.86005 | -2.03603 | -1.70588 | -1.4319 | -0.796659 | 0.54504 |
| tossup | end_difficulty_d3 | 1240 | -1.79352 | 0.686843 | -5.05808 | -3.1239 | -2.03682 | -1.72912 | -1.44746 | -0.819259 | 0.816564 |
| tossup | total_drop_d1 | 1240 | 1.17345 | 0.248245 | 0.711082 | 0.899259 | 1.03507 | 1.12264 | 1.24266 | 1.57832 | 3.06151 |
| tossup | total_drop_d2 | 1240 | 1.13426 | 0.204968 | 0.724557 | 0.920159 | 1.03512 | 1.1068 | 1.19258 | 1.39186 | 4.02367 |
| tossup | total_drop_d3 | 1240 | 1.13765 | 0.185057 | 0.717591 | 0.91583 | 1.03677 | 1.10967 | 1.19045 | 1.45797 | 2.60545 |
| tossup | drop_share_1_d1 | 1240 | 0.317193 | 0.0218273 | 0.232321 | 0.288855 | 0.303772 | 0.314008 | 0.327199 | 0.355951 | 0.444373 |
| tossup | drop_share_2_d1 | 1240 | 0.349512 | 0.0121638 | 0.310926 | 0.330415 | 0.341619 | 0.349174 | 0.356833 | 0.368522 | 0.40857 |
| tossup | drop_share_3_d1 | 1240 | 0.333295 | 0.0214506 | 0.234106 | 0.293348 | 0.323158 | 0.335872 | 0.347075 | 0.362273 | 0.390374 |
| tossup | drop_share_1_d2 | 1240 | 0.313815 | 0.0173914 | 0.191451 | 0.288785 | 0.30361 | 0.313237 | 0.322916 | 0.340792 | 0.398051 |
| tossup | drop_share_2_d2 | 1240 | 0.349352 | 0.0128609 | 0.305989 | 0.329511 | 0.341979 | 0.349143 | 0.356258 | 0.370076 | 0.522636 |
| tossup | drop_share_3_d2 | 1240 | 0.336833 | 0.0175702 | 0.243938 | 0.308702 | 0.327391 | 0.337529 | 0.347404 | 0.362947 | 0.397254 |
| tossup | drop_share_1_d3 | 1240 | 0.315318 | 0.0186207 | 0.247933 | 0.288739 | 0.303993 | 0.313921 | 0.324057 | 0.346676 | 0.421883 |
| tossup | drop_share_2_d3 | 1240 | 0.348396 | 0.0114176 | 0.307019 | 0.329761 | 0.34057 | 0.348354 | 0.35586 | 0.366777 | 0.392645 |
| tossup | drop_share_3_d3 | 1240 | 0.336286 | 0.0183268 | 0.248225 | 0.30552 | 0.326595 | 0.337338 | 0.347061 | 0.363739 | 0.406281 |
| tossup | r_1 | 1240 | 0.363411 | 0.195968 | 0.0456717 | 0.105001 | 0.207334 | 0.322684 | 0.495753 | 0.735402 | 0.862742 |
| tossup | r_2 | 1240 | 0.316423 | 0.162811 | 0.0536696 | 0.099342 | 0.194463 | 0.290705 | 0.406673 | 0.627567 | 0.889442 |
| tossup | r_3 | 1240 | 0.320166 | 0.165481 | 0.0603751 | 0.10659 | 0.204881 | 0.291901 | 0.399777 | 0.664378 | 0.899493 |
| tossup | r_norm | 1240 | 0.649462 | 0.0715657 | 0.577385 | 0.580068 | 0.595816 | 0.622802 | 0.681746 | 0.813401 | 0.902309 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.80921 | 0.872995 | 0.277094 | 0.673805 | 1.06187 | 1.60879 | 2.54882 | 3.32115 | 4.33357 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.54182 | 0.726956 | 0.249151 | 0.573046 | 0.983275 | 1.42823 | 1.99451 | 2.91981 | 4.70163 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.55508 | 0.745327 | 0.298992 | 0.53942 | 0.993233 | 1.44843 | 1.94194 | 3.0871 | 4.12991 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.35868 | 1.46317 | -8.9146 | -3.45276 | -0.464913 | 0.00290027 | 0.428715 | 1.07803 | 2.12074 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.230324 | 1.25755 | -10.4193 | -2.59162 | -0.334579 | 0.059125 | 0.356747 | 0.828936 | 1.71623 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.331572 | 1.39449 | -9.95366 | -3.09633 | -0.372817 | 0.046205 | 0.361611 | 0.794117 | 1.8302 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.16789 | 1.96325 | 0.82432 | 0.954505 | 1.01629 | 1.11699 | 2.63452 | 6.5312 | 11.9769 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.77214 | 1.67189 | 0.817464 | 0.951714 | 1.0056 | 1.08182 | 1.50947 | 5.59836 | 13.408 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.88665 | 1.85068 | 0.682572 | 0.949708 | 1.00576 | 1.08752 | 1.5608 | 6.00758 | 12.5196 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.224247 | 0.0768317 | 0.034167 | 0.0746993 | 0.167752 | 0.257751 | 0.28306 | 0.304384 | 0.392109 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.347922 | 0.076359 | 0.0752883 | 0.19513 | 0.337044 | 0.351065 | 0.365749 | 0.471001 | 0.758021 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.427831 | 0.121899 | 0.108755 | 0.32939 | 0.359314 | 0.381501 | 0.446981 | 0.71831 | 0.890545 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.241674 | 0.0676356 | 0.0288016 | 0.0884374 | 0.215797 | 0.266402 | 0.289689 | 0.306844 | 0.563706 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.346215 | 0.0574883 | 0.0559841 | 0.236334 | 0.339241 | 0.350838 | 0.363169 | 0.40179 | 0.648233 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.41211 | 0.104497 | 0.155459 | 0.336686 | 0.355075 | 0.375594 | 0.421046 | 0.663677 | 0.904642 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.239937 | 0.0694517 | 0.0340272 | 0.0822862 | 0.216933 | 0.264212 | 0.288792 | 0.3077 | 0.419856 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349883 | 0.0608853 | 0.0484585 | 0.244712 | 0.339892 | 0.351553 | 0.365999 | 0.427538 | 0.723221 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.41018 | 0.104458 | 0.0981584 | 0.332641 | 0.356682 | 0.374728 | 0.414453 | 0.658815 | 0.917514 |
| tossup_hazard | hazard_r_1 | 1240 | 0.38941 | 0.306768 | 0.0283091 | 0.0491886 | 0.105928 | 0.279658 | 0.665433 | 0.922048 | 0.966606 |
| tossup_hazard | hazard_r_2 | 1240 | 0.304381 | 0.262687 | 0.0136209 | 0.0365837 | 0.0850149 | 0.190617 | 0.506335 | 0.832539 | 0.943961 |
| tossup_hazard | hazard_r_3 | 1240 | 0.306209 | 0.249041 | 0.0131386 | 0.0318951 | 0.0939171 | 0.226078 | 0.479067 | 0.796011 | 0.91855 |
