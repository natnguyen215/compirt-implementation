# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-1.5/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-1.5/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 287541 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.724417 |
| log_loss | 0.48863 |
| ece | 0.0673112 |
| brier | 0.158754 |
| accuracy | 0.780906 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00755124 |
| probability_std | 0.169868 |
| probability_p10 | 0.462481 |
| probability_p50 | 0.741748 |
| probability_p90 | 0.89391 |
| mean_predictive_variance | 0.178691 |
| integrated_brier_score | 0.101333 |
| joint_tossup_event_log_loss | 6.6192 |
| buzz_position_mae | 0.150761 |
| buzz_position_median_absolute_error | 0.133851 |
| buzz_position_bias | -0.0434658 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.351025 |
| first_buzzer_mean_reciprocal_rank | 0.563081 |
| first_buzzer_log_loss | 1.68454 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.724417 |
| neg_average_precision | 0.455036 |
| neg_precision | 0.529412 |
| neg_recall | 0.299857 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.185757 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0135759 |
| no_buzz_calibration_error | 0.00184884 |
| no_buzz_brier | 0.011053 |
| full_pmf_max_mass_error | 1.11022e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.724417 | 0.48863 | 0.0673112 | 0.158754 | 0.780906 | 0.773355 | 0.00755124 | 0.169868 | 0.462481 | 0.741748 | 0.89391 | 0.178691 |
| tossup_correctness | tier | fall | 2876 | 0.72661 | 0.46793 | 0.0707416 | 0.150464 | 0.79242 | 0.793115 | -0.00069541 | 0.168212 | 0.475666 | 0.760102 | 0.904181 | 0.172204 |
| tossup_correctness | tier | nationals | 1579 | 0.717801 | 0.52626 | 0.0459103 | 0.174404 | 0.754275 | 0.729576 | 0.0246992 | 0.179876 | 0.429764 | 0.727207 | 0.885151 | 0.182368 |
| tossup_correctness | tier | regionals | 1990 | 0.734534 | 0.493673 | 0.0733899 | 0.161068 | 0.776382 | 0.765829 | 0.0105528 | 0.168728 | 0.450208 | 0.726665 | 0.881148 | 0.184424 |
| tossup_correctness | tier | winter | 2825 | 0.715218 | 0.485118 | 0.0743254 | 0.156815 | 0.787257 | 0.783009 | 0.00424779 | 0.164757 | 0.477122 | 0.742307 | 0.892912 | 0.1792 |
| tossup_correctness | category | Current Events | 123 | 0.753852 | 0.490223 | 0.103732 | 0.161828 | 0.780488 | 0.764228 | 0.0162602 | 0.169415 | 0.446615 | 0.660984 | 0.891648 | 0.192626 |
| tossup_correctness | category | Fine Arts | 1093 | 0.73818 | 0.476805 | 0.0562139 | 0.153287 | 0.799634 | 0.769442 | 0.0301921 | 0.170413 | 0.484589 | 0.758721 | 0.899777 | 0.174723 |
| tossup_correctness | category | Geography | 191 | 0.794042 | 0.503332 | 0.0884035 | 0.164614 | 0.769634 | 0.691099 | 0.078534 | 0.21678 | 0.352214 | 0.682329 | 0.858085 | 0.186935 |
| tossup_correctness | category | History | 1469 | 0.71657 | 0.507199 | 0.0534113 | 0.167364 | 0.751532 | 0.758339 | -0.00680735 | 0.173508 | 0.446707 | 0.740791 | 0.899919 | 0.1779 |
| tossup_correctness | category | Literature | 1436 | 0.706972 | 0.449366 | 0.0647715 | 0.141929 | 0.809889 | 0.81546 | -0.00557103 | 0.150693 | 0.536397 | 0.792325 | 0.909505 | 0.164447 |
| tossup_correctness | category | Mythology | 325 | 0.685273 | 0.441038 | 0.102337 | 0.138038 | 0.830769 | 0.843077 | -0.0123077 | 0.130652 | 0.562495 | 0.756114 | 0.891467 | 0.174974 |
| tossup_correctness | category | Other Academic | 67 | 0.692722 | 0.519138 | 0.128557 | 0.171166 | 0.776119 | 0.791045 | -0.0149254 | 0.16292 | 0.467116 | 0.689396 | 0.857687 | 0.196185 |
| tossup_correctness | category | Philosophy | 322 | 0.677665 | 0.503666 | 0.0888403 | 0.166057 | 0.770186 | 0.785714 | -0.015528 | 0.158034 | 0.506268 | 0.745014 | 0.916963 | 0.175525 |
| tossup_correctness | category | Popular Culture | 100 | 0.53524 | 0.391848 | 0.0977018 | 0.115697 | 0.87 | 0.89 | -0.02 | 0.0877921 | 0.674243 | 0.802266 | 0.896755 | 0.156854 |
| tossup_correctness | category | Religion | 365 | 0.662691 | 0.562155 | 0.062866 | 0.189775 | 0.731507 | 0.723288 | 0.00821918 | 0.17342 | 0.437101 | 0.718444 | 0.890283 | 0.185446 |
| tossup_correctness | category | Science | 1456 | 0.727137 | 0.497583 | 0.0790956 | 0.162121 | 0.776786 | 0.76717 | 0.00961538 | 0.172353 | 0.446702 | 0.724687 | 0.881109 | 0.184832 |
| tossup_correctness | category | Social Science | 333 | 0.743484 | 0.510784 | 0.0842193 | 0.1678 | 0.765766 | 0.72973 | 0.036036 | 0.190446 | 0.374615 | 0.700788 | 0.882551 | 0.187957 |
| tossup_correctness | category | Unknown | 1990 | 0.734534 | 0.493673 | 0.0733899 | 0.161068 | 0.776382 | 0.765829 | 0.0105528 | 0.168728 | 0.450208 | 0.726665 | 0.881148 | 0.184424 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.756219 | 0.508128 | 0.0999835 | 0.167532 | 0.765363 | 0.748603 | 0.0167598 | 0.175449 | 0.404352 | 0.690288 | 0.850374 | 0.195444 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.701562 | 0.517495 | 0.0721941 | 0.170481 | 0.761755 | 0.754441 | 0.00731452 | 0.168736 | 0.440442 | 0.71267 | 0.876924 | 0.187125 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.724065 | 0.493795 | 0.0597276 | 0.161195 | 0.777122 | 0.766682 | 0.0104403 | 0.167878 | 0.469992 | 0.741713 | 0.893972 | 0.178987 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.713314 | 0.475662 | 0.0652007 | 0.153016 | 0.787777 | 0.787441 | 0.000335796 | 0.159522 | 0.502748 | 0.755951 | 0.897477 | 0.174907 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.738116 | 0.487318 | 0.0734964 | 0.158385 | 0.783949 | 0.771758 | 0.012191 | 0.179322 | 0.427965 | 0.739819 | 0.895902 | 0.178536 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.68337 | 0.753504 | 0.402063 | 1.44733 | 2.16627 | 2.68171 | 3.18387 | 3.99379 | 4.66803 |
| player | theta_1 | 1196 | -1.22209 | 0.879089 | -3.70512 | -2.54736 | -1.80175 | -1.28981 | -0.713855 | 0.350633 | 2.2496 |
| player | theta_2 | 1196 | -1.01092 | 0.6904 | -3.36449 | -2.21084 | -1.44781 | -1.01498 | -0.565151 | 0.0840142 | 1.59261 |
| player | theta_3 | 1196 | -1.1221 | 0.786799 | -3.54116 | -2.35759 | -1.61628 | -1.18532 | -0.654925 | 0.287108 | 2.08544 |
| player | theta_norm | 1196 | 2.28047 | 0.664351 | 0.296814 | 1.29239 | 1.81126 | 2.22596 | 2.70921 | 3.40189 | 4.41721 |
| tossup | start_difficulty_d1 | 1240 | -1.38507 | 0.597172 | -3.45467 | -2.25016 | -1.79061 | -1.41992 | -1.05389 | -0.296723 | 1.87063 |
| tossup | start_difficulty_d2 | 1240 | -1.37037 | 0.54811 | -3.30544 | -2.20569 | -1.7591 | -1.39235 | -1.02348 | -0.405469 | 0.439311 |
| tossup | start_difficulty_d3 | 1240 | -1.37096 | 0.552531 | -3.54663 | -2.2404 | -1.75937 | -1.40474 | -1.01358 | -0.395626 | 1.15235 |
| tossup | end_difficulty_d1 | 1240 | -2.37543 | 0.694085 | -4.61403 | -3.38204 | -2.84605 | -2.42863 | -1.97477 | -1.15806 | 1.19623 |
| tossup | end_difficulty_d2 | 1240 | -2.35696 | 0.644007 | -4.67683 | -3.35993 | -2.80025 | -2.36408 | -1.95182 | -1.23582 | -0.254249 |
| tossup | end_difficulty_d3 | 1240 | -2.35664 | 0.644564 | -4.91806 | -3.38956 | -2.79659 | -2.3746 | -1.94913 | -1.25476 | 0.492452 |
| tossup | total_drop_d1 | 1240 | 0.990365 | 0.131396 | 0.582454 | 0.777484 | 0.905408 | 0.989031 | 1.06816 | 1.1998 | 2.03498 |
| tossup | total_drop_d2 | 1240 | 0.986584 | 0.119139 | 0.587623 | 0.795914 | 0.908368 | 0.981735 | 1.05714 | 1.18641 | 1.7473 |
| tossup | total_drop_d3 | 1240 | 0.985685 | 0.116772 | 0.659902 | 0.802578 | 0.903851 | 0.982134 | 1.05789 | 1.19099 | 1.40353 |
| tossup | drop_share_1_d1 | 1240 | 0.303278 | 0.0178091 | 0.202481 | 0.275084 | 0.292972 | 0.304082 | 0.315287 | 0.329957 | 0.372389 |
| tossup | drop_share_2_d1 | 1240 | 0.347182 | 0.0122108 | 0.309703 | 0.327286 | 0.339239 | 0.347292 | 0.355168 | 0.365847 | 0.448756 |
| tossup | drop_share_3_d1 | 1240 | 0.34954 | 0.01888 | 0.293294 | 0.320447 | 0.336895 | 0.348737 | 0.360643 | 0.380942 | 0.453903 |
| tossup | drop_share_1_d2 | 1240 | 0.303011 | 0.0159188 | 0.201042 | 0.27728 | 0.29357 | 0.303074 | 0.313261 | 0.32836 | 0.355597 |
| tossup | drop_share_2_d2 | 1240 | 0.346941 | 0.0117271 | 0.307054 | 0.327503 | 0.338912 | 0.346806 | 0.35468 | 0.366262 | 0.386679 |
| tossup | drop_share_3_d2 | 1240 | 0.350048 | 0.0171464 | 0.29717 | 0.323556 | 0.338372 | 0.34977 | 0.359993 | 0.379606 | 0.453386 |
| tossup | drop_share_1_d3 | 1240 | 0.302766 | 0.0167564 | 0.221596 | 0.275599 | 0.293251 | 0.303023 | 0.313848 | 0.328047 | 0.370645 |
| tossup | drop_share_2_d3 | 1240 | 0.347121 | 0.0115166 | 0.308301 | 0.328168 | 0.339691 | 0.347042 | 0.354641 | 0.365583 | 0.384719 |
| tossup | drop_share_3_d3 | 1240 | 0.350113 | 0.0177274 | 0.298794 | 0.323257 | 0.338141 | 0.34958 | 0.360287 | 0.380759 | 0.452761 |
| tossup | r_1 | 1240 | 0.330781 | 0.174461 | 0.0531291 | 0.106181 | 0.189779 | 0.292057 | 0.448754 | 0.667746 | 0.854129 |
| tossup | r_2 | 1240 | 0.332203 | 0.145563 | 0.0483497 | 0.126614 | 0.222399 | 0.316911 | 0.420449 | 0.614268 | 0.860474 |
| tossup | r_3 | 1240 | 0.337015 | 0.15315 | 0.0724094 | 0.129569 | 0.217111 | 0.316476 | 0.428438 | 0.625986 | 0.883188 |
| tossup | r_norm | 1240 | 0.636698 | 0.0547072 | 0.57739 | 0.580792 | 0.595568 | 0.620717 | 0.659374 | 0.749233 | 0.887156 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47402 | 0.492906 | 1.93269 | 3.73972 | 4.20902 | 4.42875 | 4.69897 | 5.408 | 6.38864 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45784 | 0.435213 | 2.10227 | 3.77758 | 4.22696 | 4.43374 | 4.6662 | 5.2055 | 6.62425 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.46155 | 0.436263 | 2.52781 | 3.75527 | 4.22399 | 4.43033 | 4.70697 | 5.1886 | 6.23837 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.75304 | 2.37597 | -11.8299 | -3.29317 | 0.708733 | 2.93942 | 3.32109 | 3.64002 | 4.3815 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.28637 | 2.0762 | -9.54843 | -2.59909 | 2.41358 | 3.14689 | 3.38235 | 3.71129 | 4.2706 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.17525 | 2.05814 | -10.9428 | -2.27912 | 1.82949 | 3.0703 | 3.36217 | 3.73536 | 4.26087 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.72098 | 2.54342 | 0.859882 | 0.981929 | 1.05387 | 1.2705 | 4.04942 | 7.92479 | 16.6095 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.17147 | 2.244 | 0.900097 | 0.959838 | 1.02068 | 1.16397 | 1.83468 | 7.35901 | 14.4108 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.2863 | 2.19096 | 0.851602 | 0.967845 | 1.02678 | 1.18217 | 2.517 | 7.16557 | 15.3689 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.238215 | 0.0807418 | 0.0362199 | 0.0826892 | 0.184013 | 0.274 | 0.294117 | 0.316018 | 0.556756 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.342609 | 0.0762123 | 0.0551423 | 0.178168 | 0.336472 | 0.351185 | 0.365096 | 0.449245 | 0.692196 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.419176 | 0.130428 | 0.119512 | 0.299354 | 0.348071 | 0.368818 | 0.432416 | 0.735081 | 0.901645 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.25322 | 0.0711932 | 0.0310306 | 0.0906085 | 0.23799 | 0.28026 | 0.296996 | 0.315086 | 0.653012 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.346857 | 0.0608843 | 0.0605215 | 0.230104 | 0.340032 | 0.350515 | 0.36286 | 0.410529 | 0.682628 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.399923 | 0.106839 | 0.0930822 | 0.320739 | 0.349129 | 0.365597 | 0.398135 | 0.67347 | 0.896017 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.248729 | 0.0709769 | 0.0389971 | 0.0928477 | 0.220262 | 0.277149 | 0.29679 | 0.315713 | 0.559096 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348876 | 0.0612126 | 0.0823654 | 0.23405 | 0.338425 | 0.350634 | 0.364024 | 0.435466 | 0.7166 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.402395 | 0.107354 | 0.0742176 | 0.317921 | 0.348774 | 0.367135 | 0.406568 | 0.66182 | 0.877871 |
| tossup_hazard | hazard_r_1 | 1240 | 0.378065 | 0.282585 | 0.0317098 | 0.0636915 | 0.130763 | 0.266047 | 0.621101 | 0.87813 | 0.950494 |
| tossup_hazard | hazard_r_2 | 1240 | 0.292772 | 0.218631 | 0.0229 | 0.0532194 | 0.117934 | 0.214266 | 0.428591 | 0.729592 | 0.869991 |
| tossup_hazard | hazard_r_3 | 1240 | 0.329163 | 0.249115 | 0.024134 | 0.0501304 | 0.119475 | 0.239194 | 0.539542 | 0.778078 | 0.925285 |
