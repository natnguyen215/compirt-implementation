# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-6000/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-6000/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 6000 |
| pyramidal | final_loss | 277728 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.713728 |
| log_loss | 0.490477 |
| ece | 0.0117137 |
| brier | 0.159407 |
| accuracy | 0.775901 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0106509 |
| probability_std | 0.147079 |
| probability_p10 | 0.567338 |
| probability_p50 | 0.812558 |
| probability_p90 | 0.91948 |
| mean_predictive_variance | 0.153715 |
| integrated_brier_score | 0.0975055 |
| joint_tossup_event_log_loss | 6.50634 |
| buzz_position_mae | 0.14499 |
| buzz_position_median_absolute_error | 0.125846 |
| buzz_position_bias | -0.0233491 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.371382 |
| first_buzzer_mean_reciprocal_rank | 0.581251 |
| first_buzzer_log_loss | 1.63583 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.713728 |
| neg_average_precision | 0.447956 |
| neg_precision | 0.584041 |
| neg_recall | 0.157654 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.183597 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0121959 |
| no_buzz_calibration_error | -0.0010737 |
| no_buzz_brier | 0.0130309 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.713728 | 0.490477 | 0.0117137 | 0.159407 | 0.775901 | 0.76525 | 0.0106509 | 0.147079 | 0.567338 | 0.812558 | 0.91948 | 0.153715 |
| tossup_correctness | tier | fall | 2933 | 0.711434 | 0.463386 | 0.0142347 | 0.148418 | 0.796113 | 0.791681 | 0.00443232 | 0.146729 | 0.564583 | 0.818079 | 0.922727 | 0.151494 |
| tossup_correctness | tier | nationals | 1584 | 0.706438 | 0.533354 | 0.0375772 | 0.176118 | 0.75 | 0.724747 | 0.0252525 | 0.158815 | 0.529363 | 0.808107 | 0.915921 | 0.157201 |
| tossup_correctness | tier | regionals | 1886 | 0.709475 | 0.516414 | 0.0283934 | 0.170798 | 0.753446 | 0.746023 | 0.00742312 | 0.140907 | 0.579202 | 0.798789 | 0.91274 | 0.158669 |
| tossup_correctness | tier | winter | 2892 | 0.720442 | 0.477553 | 0.0178425 | 0.153971 | 0.784232 | 0.773167 | 0.011065 | 0.144033 | 0.585886 | 0.816401 | 0.921366 | 0.150826 |
| tossup_correctness | category | Current Events | 124 | 0.681929 | 0.520267 | 0.0648894 | 0.168393 | 0.774194 | 0.75 | 0.0241935 | 0.165017 | 0.502652 | 0.762314 | 0.916242 | 0.167587 |
| tossup_correctness | category | Fine Arts | 1103 | 0.709222 | 0.496302 | 0.0253091 | 0.160577 | 0.780598 | 0.759746 | 0.0208522 | 0.152086 | 0.579161 | 0.819142 | 0.922747 | 0.151297 |
| tossup_correctness | category | Geography | 197 | 0.790093 | 0.512102 | 0.0873116 | 0.169323 | 0.746193 | 0.670051 | 0.0761421 | 0.217742 | 0.373496 | 0.737222 | 0.914973 | 0.167632 |
| tossup_correctness | category | History | 1491 | 0.720508 | 0.46389 | 0.0183761 | 0.149257 | 0.790074 | 0.787391 | 0.00268276 | 0.138103 | 0.576691 | 0.810299 | 0.91947 | 0.154076 |
| tossup_correctness | category | Literature | 1472 | 0.731985 | 0.435881 | 0.0279343 | 0.13705 | 0.815217 | 0.804348 | 0.0108696 | 0.123482 | 0.641042 | 0.845484 | 0.92942 | 0.137591 |
| tossup_correctness | category | Mythology | 332 | 0.695998 | 0.448372 | 0.0339976 | 0.141551 | 0.810241 | 0.813253 | -0.00301205 | 0.116699 | 0.640352 | 0.825096 | 0.91467 | 0.147139 |
| tossup_correctness | category | Other Academic | 69 | 0.692308 | 0.522383 | 0.0786791 | 0.174102 | 0.73913 | 0.753623 | -0.0144928 | 0.112783 | 0.632776 | 0.805594 | 0.902191 | 0.161102 |
| tossup_correctness | category | Philosophy | 324 | 0.684704 | 0.467813 | 0.0189717 | 0.149774 | 0.790123 | 0.799383 | -0.00925926 | 0.130554 | 0.601285 | 0.815955 | 0.918868 | 0.152766 |
| tossup_correctness | category | Popular Culture | 102 | 0.43737 | 0.484466 | 0.066987 | 0.148678 | 0.833333 | 0.833333 | 0 | 0.0793368 | 0.724466 | 0.843424 | 0.914944 | 0.133038 |
| tossup_correctness | category | Religion | 372 | 0.716084 | 0.543716 | 0.0438365 | 0.183494 | 0.72043 | 0.709677 | 0.0107527 | 0.151362 | 0.52178 | 0.767489 | 0.907066 | 0.168956 |
| tossup_correctness | category | Science | 1487 | 0.684897 | 0.518104 | 0.026829 | 0.170191 | 0.762609 | 0.752522 | 0.0100874 | 0.158634 | 0.52909 | 0.801328 | 0.917268 | 0.158579 |
| tossup_correctness | category | Social Science | 336 | 0.729619 | 0.536784 | 0.0464328 | 0.178261 | 0.732143 | 0.702381 | 0.0297619 | 0.182018 | 0.439488 | 0.786398 | 0.919777 | 0.16337 |
| tossup_correctness | category | Unknown | 1886 | 0.709475 | 0.516414 | 0.0283934 | 0.170798 | 0.753446 | 0.746023 | 0.00742312 | 0.140907 | 0.579202 | 0.798789 | 0.91274 | 0.158669 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.682891 | 0.526151 | 0.0607005 | 0.170749 | 0.761421 | 0.736041 | 0.0253807 | 0.149707 | 0.521241 | 0.759445 | 0.887641 | 0.175116 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.720418 | 0.517346 | 0.033217 | 0.171594 | 0.745178 | 0.735025 | 0.0101523 | 0.148888 | 0.550479 | 0.793658 | 0.908362 | 0.16204 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.694436 | 0.49818 | 0.0244188 | 0.161987 | 0.770769 | 0.769436 | 0.00133274 | 0.143877 | 0.586967 | 0.814848 | 0.92015 | 0.151767 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.700217 | 0.477389 | 0.0119978 | 0.153586 | 0.791347 | 0.78402 | 0.00732729 | 0.140718 | 0.596681 | 0.826156 | 0.924908 | 0.147875 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.736824 | 0.486031 | 0.0239593 | 0.158284 | 0.776035 | 0.756008 | 0.0200267 | 0.152845 | 0.542297 | 0.807775 | 0.917413 | 0.156621 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 1.91086 | 0.76171 | -0.250693 | 0.652287 | 1.40035 | 1.90477 | 2.38874 | 3.25148 | 3.90803 |
| player | theta_1 | 1186 | -0.798785 | 0.909416 | -3.3943 | -2.21432 | -1.36426 | -0.860214 | -0.286095 | 0.795061 | 3.25201 |
| player | theta_2 | 1186 | -0.670593 | 0.776887 | -3.25759 | -1.86528 | -1.16006 | -0.747872 | -0.222896 | 0.694566 | 2.24772 |
| player | theta_3 | 1186 | -0.755327 | 0.8859 | -3.46177 | -2.05847 | -1.31643 | -0.859818 | -0.218913 | 0.83274 | 2.83829 |
| player | theta_norm | 1186 | 1.86908 | 0.615368 | 0.406273 | 0.926755 | 1.43731 | 1.82711 | 2.26552 | 2.99917 | 4.74969 |
| tossup | start_difficulty_d1 | 1240 | -1.35158 | 0.544576 | -3.06626 | -2.08214 | -1.70582 | -1.41139 | -1.05392 | -0.465564 | 1.87755 |
| tossup | start_difficulty_d2 | 1240 | -1.35393 | 0.494199 | -2.78826 | -2.09805 | -1.67545 | -1.39851 | -1.05717 | -0.455042 | 0.91466 |
| tossup | start_difficulty_d3 | 1240 | -1.36015 | 0.494038 | -3.17154 | -2.15394 | -1.67236 | -1.36543 | -1.05751 | -0.581128 | 0.752745 |
| tossup | end_difficulty_d1 | 1240 | -2.34542 | 0.63305 | -4.29151 | -3.1994 | -2.75172 | -2.40084 | -1.99431 | -1.28808 | 1.16367 |
| tossup | end_difficulty_d2 | 1240 | -2.34572 | 0.577995 | -4.03153 | -3.21975 | -2.72913 | -2.39723 | -2.00218 | -1.32759 | 0.200228 |
| tossup | end_difficulty_d3 | 1240 | -2.35374 | 0.581853 | -4.48729 | -3.25693 | -2.72699 | -2.36226 | -1.98697 | -1.46869 | -0.0287709 |
| tossup | total_drop_d1 | 1240 | 0.993839 | 0.11103 | 0.592621 | 0.812331 | 0.928924 | 0.991897 | 1.06509 | 1.16637 | 1.51874 |
| tossup | total_drop_d2 | 1240 | 0.991784 | 0.100305 | 0.627467 | 0.82158 | 0.931931 | 0.993668 | 1.05828 | 1.1532 | 1.41725 |
| tossup | total_drop_d3 | 1240 | 0.993595 | 0.106399 | 0.593374 | 0.822475 | 0.927385 | 0.991015 | 1.05764 | 1.16761 | 1.53041 |
| tossup | drop_share_1_d1 | 1240 | 0.303458 | 0.0154109 | 0.218332 | 0.279151 | 0.294137 | 0.304164 | 0.31348 | 0.327243 | 0.346034 |
| tossup | drop_share_2_d1 | 1240 | 0.347521 | 0.0113751 | 0.312013 | 0.329305 | 0.340368 | 0.347229 | 0.354753 | 0.36658 | 0.412823 |
| tossup | drop_share_3_d1 | 1240 | 0.349021 | 0.0163724 | 0.300855 | 0.324887 | 0.338025 | 0.348639 | 0.357829 | 0.376417 | 0.42927 |
| tossup | drop_share_1_d2 | 1240 | 0.304205 | 0.0142246 | 0.244988 | 0.28055 | 0.295341 | 0.304956 | 0.313418 | 0.327518 | 0.350973 |
| tossup | drop_share_2_d2 | 1240 | 0.346928 | 0.0111702 | 0.308796 | 0.328661 | 0.339679 | 0.347077 | 0.353572 | 0.365092 | 0.382284 |
| tossup | drop_share_3_d2 | 1240 | 0.348867 | 0.0156496 | 0.297063 | 0.324878 | 0.338142 | 0.347801 | 0.358932 | 0.376548 | 0.420396 |
| tossup | drop_share_1_d3 | 1240 | 0.303672 | 0.0143752 | 0.243389 | 0.280736 | 0.294679 | 0.303744 | 0.313063 | 0.326506 | 0.351378 |
| tossup | drop_share_2_d3 | 1240 | 0.347261 | 0.0109694 | 0.315121 | 0.329645 | 0.339139 | 0.347287 | 0.35429 | 0.365581 | 0.382749 |
| tossup | drop_share_3_d3 | 1240 | 0.349067 | 0.015137 | 0.300265 | 0.324677 | 0.3395 | 0.348286 | 0.35866 | 0.374367 | 0.423126 |
| tossup | r_1 | 1240 | 0.321948 | 0.164219 | 0.059186 | 0.112019 | 0.193798 | 0.291679 | 0.426596 | 0.633721 | 0.877138 |
| tossup | r_2 | 1240 | 0.333072 | 0.160263 | 0.0537618 | 0.124862 | 0.21059 | 0.300624 | 0.425922 | 0.650279 | 0.840119 |
| tossup | r_3 | 1240 | 0.34498 | 0.162512 | 0.0690998 | 0.119312 | 0.216992 | 0.321128 | 0.451968 | 0.650197 | 0.847608 |
| tossup | r_norm | 1240 | 0.63985 | 0.0564959 | 0.577379 | 0.58115 | 0.597377 | 0.623489 | 0.664204 | 0.757573 | 0.881497 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 6.18175 | 0.531317 | 2.70187 | 5.3767 | 5.94727 | 6.13151 | 6.3959 | 7.18278 | 8.20871 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 6.16356 | 0.494822 | 3.52854 | 5.31781 | 5.99195 | 6.13619 | 6.3233 | 7.04402 | 8.46566 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 6.21572 | 0.500983 | 3.66355 | 5.43915 | 6.00852 | 6.16839 | 6.40154 | 7.16277 | 8.54774 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 3.02379 | 3.02132 | -12.9704 | -3.03834 | 1.25054 | 4.80706 | 5.09266 | 5.40657 | 6.24143 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 3.47849 | 2.97053 | -9.95632 | -3.15779 | 2.45288 | 4.99497 | 5.1746 | 5.47166 | 6.4079 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 3.56602 | 2.92054 | -14.9098 | -2.61695 | 2.97232 | 5.00785 | 5.19876 | 5.57364 | 6.40303 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.15795 | 3.15921 | 0.854591 | 0.960489 | 1.01941 | 1.1125 | 5.22289 | 9.62375 | 19.6281 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.68507 | 3.09143 | 0.8459 | 0.945379 | 0.997115 | 1.04753 | 3.41084 | 9.61732 | 17.0018 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.6497 | 3.04775 | 0.838426 | 0.944636 | 0.999573 | 1.05114 | 3.18394 | 8.94685 | 21.2367 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.247248 | 0.0875038 | 0.046097 | 0.0841719 | 0.176597 | 0.285888 | 0.302858 | 0.321126 | 0.687233 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.33592 | 0.0828513 | 0.0562613 | 0.160939 | 0.330653 | 0.34763 | 0.360568 | 0.451869 | 0.737108 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.416832 | 0.139333 | 0.109769 | 0.292027 | 0.343979 | 0.360466 | 0.429526 | 0.73805 | 0.896775 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.261701 | 0.080418 | 0.0317082 | 0.0864736 | 0.259097 | 0.292552 | 0.304474 | 0.322332 | 0.688442 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.340478 | 0.0750705 | 0.0627973 | 0.179088 | 0.336525 | 0.348486 | 0.359141 | 0.439837 | 0.700367 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.397822 | 0.127702 | 0.0898644 | 0.298953 | 0.342827 | 0.356243 | 0.378785 | 0.71947 | 0.898709 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.257998 | 0.0787781 | 0.0365719 | 0.0844518 | 0.245515 | 0.289449 | 0.303206 | 0.321907 | 0.661755 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.342037 | 0.0752685 | 0.071099 | 0.185863 | 0.336678 | 0.348995 | 0.359748 | 0.448693 | 0.725621 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.399965 | 0.124798 | 0.093432 | 0.308235 | 0.343436 | 0.358069 | 0.386124 | 0.719968 | 0.885637 |
| tossup_hazard | hazard_r_1 | 1240 | 0.373317 | 0.292262 | 0.0140038 | 0.037412 | 0.102231 | 0.271351 | 0.609332 | 0.890516 | 0.95002 |
| tossup_hazard | hazard_r_2 | 1240 | 0.29989 | 0.267198 | 0.0125168 | 0.0339379 | 0.0773099 | 0.184723 | 0.515194 | 0.813044 | 0.922785 |
| tossup_hazard | hazard_r_3 | 1240 | 0.326793 | 0.267584 | 0.0130663 | 0.0332014 | 0.0914182 | 0.251659 | 0.530435 | 0.839661 | 0.97348 |
