# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 297223 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.668266 |
| log_loss | 0.548664 |
| ece | 0.108636 |
| brier | 0.184581 |
| accuracy | 0.718591 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0455871 |
| probability_std | 0.178641 |
| probability_p10 | 0.41065 |
| probability_p50 | 0.67424 |
| probability_p90 | 0.889391 |
| mean_predictive_variance | 0.192681 |
| integrated_brier_score | 0.103666 |
| joint_tossup_event_log_loss | 6.67714 |
| buzz_position_mae | 0.15628 |
| buzz_position_median_absolute_error | 0.138651 |
| buzz_position_bias | -0.0599995 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.333261 |
| first_buzzer_mean_reciprocal_rank | 0.549005 |
| first_buzzer_log_loss | 1.7101 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.668266 |
| neg_average_precision | 0.380494 |
| neg_precision | 0.38999 |
| neg_recall | 0.342648 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.15848 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0058814 |
| no_buzz_calibration_error | -0.00723161 |
| no_buzz_brier | 0.0124261 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.668266 | 0.548664 | 0.108636 | 0.184581 | 0.718591 | 0.764178 | -0.0455871 | 0.178641 | 0.41065 | 0.67424 | 0.889391 | 0.192681 |
| tossup_correctness | tier | fall | 2798 | 0.680504 | 0.521481 | 0.104169 | 0.173299 | 0.735525 | 0.785204 | -0.0496783 | 0.188331 | 0.41019 | 0.710469 | 0.909818 | 0.180818 |
| tossup_correctness | tier | nationals | 1545 | 0.656798 | 0.580387 | 0.0950159 | 0.197516 | 0.704854 | 0.721036 | -0.0161812 | 0.141688 | 0.441315 | 0.643219 | 0.799677 | 0.21338 |
| tossup_correctness | tier | regionals | 2039 | 0.647876 | 0.571023 | 0.127669 | 0.194557 | 0.69691 | 0.762138 | -0.0652281 | 0.170977 | 0.391117 | 0.648258 | 0.852667 | 0.20267 |
| tossup_correctness | tier | winter | 2875 | 0.672357 | 0.542213 | 0.106974 | 0.181534 | 0.72487 | 0.768348 | -0.0434783 | 0.187305 | 0.412869 | 0.690085 | 0.9093 | 0.186018 |
| tossup_correctness | category | Current Events | 129 | 0.687939 | 0.586276 | 0.077785 | 0.204687 | 0.643411 | 0.666667 | -0.0232558 | 0.198432 | 0.375574 | 0.6274 | 0.931882 | 0.19192 |
| tossup_correctness | category | Fine Arts | 1074 | 0.683643 | 0.535635 | 0.11939 | 0.179143 | 0.736499 | 0.776536 | -0.0400372 | 0.186222 | 0.392935 | 0.686784 | 0.887136 | 0.189723 |
| tossup_correctness | category | Geography | 180 | 0.742003 | 0.568083 | 0.0582491 | 0.193937 | 0.694444 | 0.616667 | 0.0777778 | 0.210075 | 0.256503 | 0.631392 | 0.858801 | 0.196818 |
| tossup_correctness | category | History | 1454 | 0.662514 | 0.550591 | 0.0994891 | 0.185214 | 0.716644 | 0.757909 | -0.0412655 | 0.177703 | 0.421984 | 0.677698 | 0.898617 | 0.190428 |
| tossup_correctness | category | Literature | 1435 | 0.679998 | 0.493353 | 0.109981 | 0.161317 | 0.76446 | 0.810453 | -0.045993 | 0.170512 | 0.449469 | 0.724292 | 0.910858 | 0.180737 |
| tossup_correctness | category | Mythology | 324 | 0.626982 | 0.531743 | 0.098995 | 0.174659 | 0.753086 | 0.79321 | -0.0401235 | 0.174085 | 0.436075 | 0.758247 | 0.92397 | 0.174469 |
| tossup_correctness | category | Other Academic | 71 | 0.61329 | 0.591392 | 0.138581 | 0.198348 | 0.71831 | 0.760563 | -0.0422535 | 0.144418 | 0.456592 | 0.631466 | 0.821203 | 0.208668 |
| tossup_correctness | category | Philosophy | 310 | 0.631356 | 0.574298 | 0.12467 | 0.194354 | 0.703226 | 0.76129 | -0.0580645 | 0.165882 | 0.426572 | 0.661151 | 0.863793 | 0.200207 |
| tossup_correctness | category | Popular Culture | 108 | 0.37066 | 0.466204 | 0.162191 | 0.141199 | 0.833333 | 0.888889 | -0.0555556 | 0.148352 | 0.519467 | 0.822005 | 0.916431 | 0.15345 |
| tossup_correctness | category | Religion | 361 | 0.672926 | 0.579423 | 0.134882 | 0.198723 | 0.67867 | 0.742382 | -0.0637119 | 0.162612 | 0.402828 | 0.596293 | 0.827434 | 0.21191 |
| tossup_correctness | category | Science | 1445 | 0.662183 | 0.563324 | 0.098079 | 0.191105 | 0.701038 | 0.746021 | -0.0449827 | 0.181246 | 0.413621 | 0.658947 | 0.890998 | 0.193319 |
| tossup_correctness | category | Social Science | 327 | 0.68654 | 0.572341 | 0.0806392 | 0.193892 | 0.70948 | 0.718654 | -0.00917431 | 0.180529 | 0.417792 | 0.636735 | 0.895067 | 0.196913 |
| tossup_correctness | category | Unknown | 2039 | 0.647876 | 0.571023 | 0.127669 | 0.194557 | 0.69691 | 0.762138 | -0.0652281 | 0.170977 | 0.391117 | 0.648258 | 0.852667 | 0.20267 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.663173 | 0.540782 | 0.058352 | 0.180719 | 0.743169 | 0.743169 | 0 | 0.168766 | 0.503211 | 0.779797 | 0.907806 | 0.163091 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.703113 | 0.53063 | 0.0397596 | 0.174073 | 0.751832 | 0.728796 | 0.0230366 | 0.174933 | 0.474629 | 0.771744 | 0.925437 | 0.164066 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.708511 | 0.51509 | 0.052103 | 0.170173 | 0.749888 | 0.752568 | -0.00267977 | 0.182303 | 0.430949 | 0.737591 | 0.920321 | 0.174242 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.684768 | 0.523839 | 0.120937 | 0.174426 | 0.73913 | 0.786087 | -0.0469565 | 0.171577 | 0.426625 | 0.6859 | 0.882201 | 0.193102 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.635539 | 0.603641 | 0.175509 | 0.208607 | 0.663561 | 0.764393 | -0.100832 | 0.158441 | 0.376707 | 0.596293 | 0.796316 | 0.216912 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 4.02689 | 0.554802 | 2.17191 | 3.13905 | 3.64808 | 4.03287 | 4.41727 | 4.92131 | 5.48931 |
| player | theta_1 | 1197 | -0.304871 | 1.04855 | -3.12791 | -1.89547 | -1.128 | -0.345082 | 0.47548 | 1.53098 | 2.71317 |
| player | theta_2 | 1197 | -0.517627 | 0.742324 | -2.56122 | -1.58421 | -1.08407 | -0.582332 | -0.0220391 | 0.784745 | 1.70419 |
| player | theta_3 | 1197 | -0.47999 | 0.758666 | -2.73865 | -1.66922 | -0.992892 | -0.482275 | 0.00564021 | 0.821814 | 1.84371 |
| player | theta_norm | 1197 | 1.55364 | 0.634068 | 0.0555295 | 0.573138 | 1.08566 | 1.53037 | 1.98767 | 2.68537 | 4.09682 |
| tossup | beta_1 | 1240 | -0.595468 | 0.7544 | -3.55039 | -2.35628 | -0.781858 | -0.343196 | -0.131736 | 0.156199 | 1.45257 |
| tossup | beta_2 | 1240 | -0.421053 | 0.682609 | -3.59247 | -2.20419 | -0.395687 | -0.223506 | -0.119815 | 0.115404 | 1.47791 |
| tossup | beta_3 | 1240 | -0.45581 | 0.708349 | -3.43092 | -2.32415 | -0.396074 | -0.236932 | -0.127145 | 0.128771 | 1.2938 |
| tossup | gamma_1 | 1240 | 5.5154 | 3.80748 | 0.654633 | 2.98041 | 4.36832 | 4.80497 | 5.18623 | 11.9742 | 59.5519 |
| tossup | gamma_2 | 1240 | 5.49815 | 3.30589 | 0.514683 | 3.96767 | 4.62604 | 4.90158 | 5.17722 | 9.34495 | 43.6373 |
| tossup | gamma_3 | 1240 | 5.48373 | 3.12289 | 0.364246 | 3.99173 | 4.63863 | 4.90038 | 5.20583 | 10.2574 | 35.0134 |
| tossup | mu_1 | 1240 | 0.560904 | 0.118419 | 0.433977 | 0.47364 | 0.495697 | 0.512215 | 0.557918 | 0.87257 | 0.958998 |
| tossup | mu_2 | 1240 | 0.539309 | 0.105637 | 0.446482 | 0.476859 | 0.494624 | 0.506367 | 0.520837 | 0.858277 | 0.966518 |
| tossup | mu_3 | 1240 | 0.544542 | 0.111044 | 0.456594 | 0.477469 | 0.49316 | 0.505962 | 0.521846 | 0.863805 | 0.97708 |
| tossup | r_1 | 1240 | 0.410869 | 0.243723 | 0.0387861 | 0.0747636 | 0.179855 | 0.394858 | 0.624451 | 0.804866 | 0.872898 |
| tossup | r_2 | 1240 | 0.285315 | 0.218527 | 0.0412932 | 0.0676356 | 0.116978 | 0.206401 | 0.375504 | 0.795102 | 0.897663 |
| tossup | r_3 | 1240 | 0.303815 | 0.21594 | 0.0446306 | 0.0762009 | 0.138305 | 0.240712 | 0.379897 | 0.803943 | 0.899663 |
| tossup | r_norm | 1240 | 0.698633 | 0.0900096 | 0.577479 | 0.585039 | 0.618537 | 0.67889 | 0.769779 | 0.858322 | 0.902556 |
| tossup_hazard | hazard_beta_1 | 1240 | 1.99551 | 1.5 | -0.0378893 | 0.421194 | 0.658532 | 1.30262 | 3.54928 | 4.53846 | 5.22225 |
| tossup_hazard | hazard_beta_2 | 1240 | 1.9795 | 1.31216 | 0.0495328 | 0.398992 | 0.716311 | 1.68229 | 3.303 | 3.98602 | 5.22639 |
| tossup_hazard | hazard_beta_3 | 1240 | 1.80183 | 1.32249 | -0.112001 | 0.37977 | 0.680475 | 1.21953 | 3.09363 | 4.10419 | 4.86365 |
| tossup_hazard | hazard_gamma_1 | 1240 | 13.8407 | 37.6278 | 3.07935 | 5.54197 | 6.22011 | 7.29812 | 11.0362 | 36.666 | 1068.1 |
| tossup_hazard | hazard_gamma_2 | 1240 | 14.704 | 22.6756 | 2.69357 | 5.49855 | 6.46666 | 8.15868 | 13.2977 | 47.2048 | 336.304 |
| tossup_hazard | hazard_gamma_3 | 1240 | 13.8429 | 38.9059 | 1.91459 | 5.54577 | 6.31081 | 7.57297 | 11.0538 | 32.068 | 1056.36 |
| tossup_hazard | hazard_mu_1 | 1240 | 0.600873 | 0.104794 | 0.266871 | 0.485816 | 0.532726 | 0.566154 | 0.65799 | 0.813051 | 0.961488 |
| tossup_hazard | hazard_mu_2 | 1240 | 0.599357 | 0.11033 | 0.211317 | 0.45956 | 0.528581 | 0.567843 | 0.657856 | 0.817889 | 0.940145 |
| tossup_hazard | hazard_mu_3 | 1240 | 0.599831 | 0.102933 | 0.266968 | 0.487287 | 0.529612 | 0.563931 | 0.652481 | 0.808897 | 0.950653 |
| tossup_hazard | hazard_r_1 | 1240 | 0.332092 | 0.341913 | 0.0191901 | 0.0329238 | 0.051498 | 0.122264 | 0.726141 | 0.907828 | 0.955608 |
| tossup_hazard | hazard_r_2 | 1240 | 0.36889 | 0.338428 | 0.0101311 | 0.0247634 | 0.0648415 | 0.200002 | 0.750974 | 0.899378 | 0.951234 |
| tossup_hazard | hazard_r_3 | 1240 | 0.299017 | 0.311717 | 0.0148521 | 0.0284704 | 0.0560655 | 0.127457 | 0.589683 | 0.877539 | 0.938841 |
