# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-20000/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-20000/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 20000 |
| pyramidal | final_loss | 275613 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.723911 |
| log_loss | 0.476368 |
| ece | 0.00945502 |
| brier | 0.153909 |
| accuracy | 0.787055 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0137001 |
| probability_std | 0.147983 |
| probability_p10 | 0.564735 |
| probability_p50 | 0.805899 |
| probability_p90 | 0.919504 |
| mean_predictive_variance | 0.155507 |
| integrated_brier_score | 0.0944535 |
| joint_tossup_event_log_loss | 6.45616 |
| buzz_position_mae | 0.138839 |
| buzz_position_median_absolute_error | 0.116546 |
| buzz_position_bias | -0.00341 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.361812 |
| first_buzzer_mean_reciprocal_rank | 0.572395 |
| first_buzzer_log_loss | 1.65597 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.723911 |
| neg_average_precision | 0.451119 |
| neg_precision | 0.607445 |
| neg_recall | 0.170871 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.179183 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0096886 |
| no_buzz_calibration_error | -0.00203848 |
| no_buzz_brier | 0.0110385 |
| full_pmf_max_mass_error | 1.66533e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.723911 | 0.476368 | 0.00945502 | 0.153909 | 0.787055 | 0.773355 | 0.0137001 | 0.147983 | 0.564735 | 0.805899 | 0.919504 | 0.155507 |
| tossup_correctness | tier | fall | 2876 | 0.731461 | 0.451283 | 0.0156965 | 0.143876 | 0.803894 | 0.793115 | 0.0107789 | 0.141508 | 0.576866 | 0.812947 | 0.924177 | 0.152182 |
| tossup_correctness | tier | nationals | 1579 | 0.71269 | 0.528055 | 0.0325796 | 0.174505 | 0.751742 | 0.729576 | 0.0221659 | 0.161211 | 0.539906 | 0.802486 | 0.916797 | 0.157156 |
| tossup_correctness | tier | regionals | 1990 | 0.736986 | 0.478649 | 0.0129898 | 0.155462 | 0.780402 | 0.765829 | 0.0145729 | 0.150633 | 0.545863 | 0.797283 | 0.916254 | 0.159521 |
| tossup_correctness | tier | winter | 2825 | 0.712243 | 0.47141 | 0.0164923 | 0.151518 | 0.794336 | 0.783009 | 0.0113274 | 0.144014 | 0.574969 | 0.807448 | 0.91834 | 0.155144 |
| tossup_correctness | category | Current Events | 123 | 0.802641 | 0.447649 | 0.0803451 | 0.144078 | 0.788618 | 0.764228 | 0.0243902 | 0.136925 | 0.560223 | 0.745105 | 0.911007 | 0.172861 |
| tossup_correctness | category | Fine Arts | 1093 | 0.74086 | 0.466978 | 0.0131213 | 0.14976 | 0.797804 | 0.769442 | 0.0283623 | 0.148153 | 0.571152 | 0.816401 | 0.922461 | 0.152246 |
| tossup_correctness | category | Geography | 191 | 0.785953 | 0.48981 | 0.0696761 | 0.158476 | 0.795812 | 0.691099 | 0.104712 | 0.208059 | 0.399112 | 0.763603 | 0.89947 | 0.167866 |
| tossup_correctness | category | History | 1469 | 0.711735 | 0.503316 | 0.0312914 | 0.165686 | 0.766508 | 0.758339 | 0.00816882 | 0.147561 | 0.55775 | 0.801954 | 0.919836 | 0.156673 |
| tossup_correctness | category | Literature | 1436 | 0.705212 | 0.436952 | 0.0156688 | 0.136994 | 0.816156 | 0.81546 | 0.000696379 | 0.124681 | 0.650114 | 0.842411 | 0.930268 | 0.139492 |
| tossup_correctness | category | Mythology | 325 | 0.66087 | 0.424701 | 0.0623641 | 0.131933 | 0.843077 | 0.843077 | 0 | 0.109623 | 0.653184 | 0.815558 | 0.910211 | 0.151221 |
| tossup_correctness | category | Other Academic | 67 | 0.679245 | 0.494904 | 0.0703488 | 0.160951 | 0.80597 | 0.791045 | 0.0149254 | 0.143251 | 0.534829 | 0.75895 | 0.896315 | 0.16838 |
| tossup_correctness | category | Philosophy | 322 | 0.682935 | 0.488368 | 0.0255468 | 0.158981 | 0.776398 | 0.785714 | -0.00931677 | 0.128761 | 0.606808 | 0.803104 | 0.930848 | 0.152577 |
| tossup_correctness | category | Popular Culture | 100 | 0.54954 | 0.364756 | 0.0604915 | 0.105932 | 0.89 | 0.89 | 0 | 0.0750467 | 0.748613 | 0.84788 | 0.923996 | 0.129914 |
| tossup_correctness | category | Religion | 365 | 0.662991 | 0.562446 | 0.0549449 | 0.188757 | 0.723288 | 0.723288 | 0 | 0.152464 | 0.533193 | 0.782625 | 0.91349 | 0.165706 |
| tossup_correctness | category | Science | 1456 | 0.72185 | 0.482297 | 0.0140922 | 0.156107 | 0.782967 | 0.76717 | 0.0157967 | 0.15246 | 0.546981 | 0.795052 | 0.911367 | 0.16127 |
| tossup_correctness | category | Social Science | 333 | 0.754961 | 0.495893 | 0.0382768 | 0.161977 | 0.75976 | 0.72973 | 0.03003 | 0.174596 | 0.4592 | 0.772783 | 0.907334 | 0.168385 |
| tossup_correctness | category | Unknown | 1990 | 0.736986 | 0.478649 | 0.0129898 | 0.155462 | 0.780402 | 0.765829 | 0.0145729 | 0.150633 | 0.545863 | 0.797283 | 0.916254 | 0.159521 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.75539 | 0.492854 | 0.055118 | 0.162185 | 0.759777 | 0.748603 | 0.0111732 | 0.158843 | 0.48378 | 0.758367 | 0.890612 | 0.176131 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.705788 | 0.500778 | 0.0278979 | 0.163528 | 0.770115 | 0.754441 | 0.015674 | 0.149246 | 0.531654 | 0.780499 | 0.904598 | 0.165844 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.727829 | 0.481924 | 0.0196847 | 0.15641 | 0.783931 | 0.766682 | 0.0172492 | 0.146251 | 0.572492 | 0.803468 | 0.916437 | 0.156069 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.712295 | 0.464205 | 0.00785886 | 0.14833 | 0.801209 | 0.787441 | 0.0137676 | 0.137557 | 0.602611 | 0.816986 | 0.92146 | 0.150613 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.73341 | 0.475579 | 0.0128848 | 0.154051 | 0.782255 | 0.771758 | 0.0104978 | 0.15636 | 0.53518 | 0.80932 | 0.923071 | 0.155424 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 0.821526 | 0.840329 | -1.60709 | -0.540485 | 0.248711 | 0.822365 | 1.34282 | 2.30933 | 3.03767 |
| player | theta_1 | 1196 | -0.373005 | 0.918133 | -3.30113 | -1.71443 | -0.959676 | -0.488056 | 0.126718 | 1.30608 | 3.86378 |
| player | theta_2 | 1196 | -0.372744 | 0.846875 | -2.61396 | -1.65208 | -0.922545 | -0.450218 | 0.105316 | 1.18744 | 2.77389 |
| player | theta_3 | 1196 | -0.43182 | 0.865144 | -2.83887 | -1.75244 | -0.990033 | -0.536885 | 0.0741051 | 1.13247 | 2.86159 |
| player | theta_norm | 1196 | 1.53498 | 0.644549 | 0.179639 | 0.574813 | 1.06167 | 1.4793 | 1.90706 | 2.69417 | 4.50607 |
| tossup | start_difficulty_d1 | 1240 | -0.944986 | 0.534521 | -2.59459 | -1.7123 | -1.28472 | -0.980719 | -0.65685 | -0.0689499 | 2.21299 |
| tossup | start_difficulty_d2 | 1240 | -0.948887 | 0.489831 | -2.85082 | -1.65751 | -1.27861 | -0.986117 | -0.65616 | -0.112075 | 1.32709 |
| tossup | start_difficulty_d3 | 1240 | -0.948225 | 0.501541 | -2.83627 | -1.68946 | -1.27361 | -0.971878 | -0.648488 | -0.136233 | 1.55391 |
| tossup | end_difficulty_d1 | 1240 | -1.94137 | 0.625233 | -3.72 | -2.83407 | -2.34493 | -1.98918 | -1.5946 | -0.910556 | 1.50344 |
| tossup | end_difficulty_d2 | 1240 | -1.94636 | 0.57792 | -4.19518 | -2.79557 | -2.33239 | -1.98105 | -1.59176 | -0.972515 | 0.445255 |
| tossup | end_difficulty_d3 | 1240 | -1.94806 | 0.585207 | -4.11665 | -2.80939 | -2.32331 | -1.97525 | -1.58703 | -1.00436 | 0.887384 |
| tossup | total_drop_d1 | 1240 | 0.996381 | 0.112153 | 0.620144 | 0.809502 | 0.926618 | 0.994346 | 1.0675 | 1.18595 | 1.46467 |
| tossup | total_drop_d2 | 1240 | 0.997472 | 0.10688 | 0.629419 | 0.826653 | 0.926627 | 0.995879 | 1.06359 | 1.16625 | 1.39681 |
| tossup | total_drop_d3 | 1240 | 0.999834 | 0.117714 | 0.639602 | 0.834487 | 0.929049 | 0.995507 | 1.06819 | 1.17354 | 2.79414 |
| tossup | drop_share_1_d1 | 1240 | 0.304751 | 0.0152472 | 0.222466 | 0.280145 | 0.295384 | 0.30535 | 0.314454 | 0.327875 | 0.355945 |
| tossup | drop_share_2_d1 | 1240 | 0.346651 | 0.0113766 | 0.30287 | 0.328428 | 0.339063 | 0.346486 | 0.35426 | 0.366319 | 0.386794 |
| tossup | drop_share_3_d1 | 1240 | 0.348598 | 0.0163003 | 0.302506 | 0.323045 | 0.337831 | 0.348497 | 0.358381 | 0.374966 | 0.440935 |
| tossup | drop_share_1_d2 | 1240 | 0.304255 | 0.0145397 | 0.24387 | 0.279715 | 0.295668 | 0.304177 | 0.312804 | 0.328723 | 0.352655 |
| tossup | drop_share_2_d2 | 1240 | 0.347368 | 0.011102 | 0.308829 | 0.329458 | 0.339897 | 0.347365 | 0.354481 | 0.365843 | 0.390588 |
| tossup | drop_share_3_d2 | 1240 | 0.348377 | 0.0156195 | 0.303792 | 0.324385 | 0.338316 | 0.347599 | 0.35767 | 0.375675 | 0.415293 |
| tossup | drop_share_1_d3 | 1240 | 0.30491 | 0.0152414 | 0.180893 | 0.281291 | 0.295919 | 0.3054 | 0.314644 | 0.328414 | 0.358093 |
| tossup | drop_share_2_d3 | 1240 | 0.347007 | 0.0118179 | 0.313627 | 0.328778 | 0.339381 | 0.346778 | 0.354511 | 0.365062 | 0.490763 |
| tossup | drop_share_3_d3 | 1240 | 0.348083 | 0.0156622 | 0.30757 | 0.323664 | 0.33779 | 0.347265 | 0.357052 | 0.373956 | 0.426829 |
| tossup | r_1 | 1240 | 0.318455 | 0.16354 | 0.0418095 | 0.107466 | 0.192444 | 0.285417 | 0.423168 | 0.626067 | 0.881095 |
| tossup | r_2 | 1240 | 0.341352 | 0.165088 | 0.0619636 | 0.122926 | 0.213903 | 0.309422 | 0.44838 | 0.651402 | 0.83767 |
| tossup | r_3 | 1240 | 0.340193 | 0.164586 | 0.0569413 | 0.125302 | 0.213838 | 0.302846 | 0.442442 | 0.665479 | 0.868496 |
| tossup | r_norm | 1240 | 0.641424 | 0.0571569 | 0.577361 | 0.581383 | 0.598412 | 0.625605 | 0.667422 | 0.756804 | 0.885105 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 8.62549 | 0.488472 | 6.32282 | 7.73106 | 8.4833 | 8.64606 | 8.8248 | 9.42705 | 10.2712 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 8.70307 | 0.487715 | 4.93577 | 7.91111 | 8.57237 | 8.69446 | 8.87594 | 9.45055 | 11.199 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 8.66619 | 0.514502 | 4.86839 | 7.80793 | 8.534 | 8.67529 | 8.86191 | 9.45979 | 10.8842 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 4.97871 | 3.8451 | -12.8153 | -2.66707 | 2.22224 | 7.47607 | 7.67192 | 7.94469 | 8.53052 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 5.56722 | 3.89051 | -11.7453 | -2.71149 | 3.90843 | 7.58755 | 7.74838 | 8.05534 | 8.76436 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 5.37175 | 3.66329 | -20.034 | -1.29849 | 2.47738 | 7.56308 | 7.72947 | 8.06847 | 9.17853 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.64679 | 3.87599 | 0.867817 | 0.94708 | 0.998548 | 1.05274 | 6.29919 | 11.3859 | 21.7832 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 3.13585 | 3.94986 | 0.871493 | 0.932057 | 0.977873 | 1.02266 | 4.67797 | 11.5087 | 20.3185 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 3.29444 | 3.6744 | 0.850018 | 0.933009 | 0.985937 | 1.03115 | 6.04255 | 10.2079 | 29.0376 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.279974 | 0.0962929 | 0.052074 | 0.107383 | 0.260149 | 0.297737 | 0.309337 | 0.432551 | 0.749977 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.325461 | 0.0814076 | 0.0591594 | 0.155716 | 0.321055 | 0.343954 | 0.355497 | 0.431199 | 0.686761 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.394564 | 0.130177 | 0.0932861 | 0.233601 | 0.341199 | 0.354716 | 0.387137 | 0.698902 | 0.884575 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.28119 | 0.0849445 | 0.0364722 | 0.114378 | 0.280969 | 0.29827 | 0.30971 | 0.346142 | 0.79146 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.331455 | 0.0721778 | 0.0611784 | 0.167205 | 0.332244 | 0.344416 | 0.354296 | 0.414699 | 0.700808 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.387355 | 0.117452 | 0.0727955 | 0.271742 | 0.342475 | 0.35352 | 0.371553 | 0.668734 | 0.898247 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.283946 | 0.0906051 | 0.033819 | 0.108924 | 0.278731 | 0.298875 | 0.31011 | 0.414819 | 0.754283 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.326641 | 0.0737072 | 0.0587668 | 0.174279 | 0.326022 | 0.343503 | 0.354948 | 0.410316 | 0.711247 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.389413 | 0.123563 | 0.0589997 | 0.250392 | 0.34128 | 0.354365 | 0.379222 | 0.69151 | 0.907414 |
| tossup_hazard | hazard_r_1 | 1240 | 0.362696 | 0.30641 | 0.0187094 | 0.0413823 | 0.0978311 | 0.21929 | 0.652474 | 0.894812 | 0.958546 |
| tossup_hazard | hazard_r_2 | 1240 | 0.302314 | 0.272715 | 0.0182484 | 0.0376307 | 0.0808954 | 0.174736 | 0.5091 | 0.847807 | 0.951265 |
| tossup_hazard | hazard_r_3 | 1240 | 0.33499 | 0.297262 | 0.00985758 | 0.0348337 | 0.0785158 | 0.190256 | 0.631862 | 0.855504 | 0.954622 |
