# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/terminal-off/degree_3/curves_3/dirichlet_2/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/terminal-off/degree_3/curves_3/dirichlet_2/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 306367 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711602 |
| log_loss | 0.497666 |
| ece | 0.0747122 |
| brier | 0.16207 |
| accuracy | 0.77562 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00226537 |
| probability_std | 0.165499 |
| probability_p10 | 0.464582 |
| probability_p50 | 0.724023 |
| probability_p90 | 0.894873 |
| mean_predictive_variance | 0.183074 |
| integrated_brier_score | 0.10737 |
| joint_tossup_event_log_loss | 6.7559 |
| buzz_position_mae | 0.177017 |
| buzz_position_median_absolute_error | 0.157641 |
| buzz_position_bias | -0.098077 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.339266 |
| first_buzzer_mean_reciprocal_rank | 0.551385 |
| first_buzzer_log_loss | 1.71058 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.711602 |
| neg_average_precision | 0.448971 |
| neg_precision | 0.508728 |
| neg_recall | 0.29129 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0948415 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0770114 |
| no_buzz_calibration_error | 0.0652843 |
| no_buzz_brier | 0.0214849 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.711602 | 0.497666 | 0.0747122 | 0.16207 | 0.77562 | 0.773355 | 0.00226537 | 0.165499 | 0.464582 | 0.724023 | 0.894873 | 0.183074 |
| tossup_correctness | tier | fall | 2876 | 0.711166 | 0.473806 | 0.0691522 | 0.152635 | 0.790682 | 0.793115 | -0.00243394 | 0.159273 | 0.495027 | 0.752518 | 0.914854 | 0.1738 |
| tossup_correctness | tier | nationals | 1579 | 0.70244 | 0.54429 | 0.0782506 | 0.182113 | 0.737175 | 0.729576 | 0.00759975 | 0.170815 | 0.408074 | 0.679672 | 0.857764 | 0.19723 |
| tossup_correctness | tier | regionals | 1990 | 0.73742 | 0.498224 | 0.0883834 | 0.162309 | 0.773869 | 0.765829 | 0.0080402 | 0.166218 | 0.439739 | 0.698372 | 0.876069 | 0.190852 |
| tossup_correctness | tier | winter | 2825 | 0.691085 | 0.495503 | 0.0747826 | 0.160304 | 0.783009 | 0.783009 | 0 | 0.161005 | 0.485435 | 0.737381 | 0.898339 | 0.179126 |
| tossup_correctness | category | Current Events | 123 | 0.754219 | 0.505773 | 0.120558 | 0.168211 | 0.747967 | 0.764228 | -0.0162602 | 0.161491 | 0.429072 | 0.632277 | 0.887801 | 0.201535 |
| tossup_correctness | category | Fine Arts | 1093 | 0.719037 | 0.488559 | 0.0640426 | 0.157736 | 0.788655 | 0.769442 | 0.0192132 | 0.168375 | 0.468286 | 0.744197 | 0.908046 | 0.176577 |
| tossup_correctness | category | Geography | 191 | 0.773369 | 0.51488 | 0.0795614 | 0.169104 | 0.764398 | 0.691099 | 0.0732984 | 0.191089 | 0.369759 | 0.674273 | 0.83376 | 0.196605 |
| tossup_correctness | category | History | 1469 | 0.708524 | 0.510941 | 0.0581756 | 0.169012 | 0.755616 | 0.758339 | -0.00272294 | 0.166903 | 0.454987 | 0.728108 | 0.905562 | 0.181769 |
| tossup_correctness | category | Literature | 1436 | 0.668708 | 0.47103 | 0.074148 | 0.150172 | 0.793872 | 0.81546 | -0.0215877 | 0.149926 | 0.534629 | 0.773969 | 0.91079 | 0.168784 |
| tossup_correctness | category | Mythology | 325 | 0.644769 | 0.460786 | 0.112356 | 0.145732 | 0.809231 | 0.843077 | -0.0338462 | 0.135767 | 0.535516 | 0.750811 | 0.884975 | 0.178335 |
| tossup_correctness | category | Other Academic | 67 | 0.621294 | 0.554083 | 0.12629 | 0.18605 | 0.746269 | 0.791045 | -0.0447761 | 0.150913 | 0.47458 | 0.675829 | 0.859809 | 0.200081 |
| tossup_correctness | category | Philosophy | 322 | 0.680873 | 0.493511 | 0.0720577 | 0.161141 | 0.78882 | 0.785714 | 0.00310559 | 0.15179 | 0.519511 | 0.730607 | 0.919233 | 0.177287 |
| tossup_correctness | category | Popular Culture | 100 | 0.547497 | 0.400267 | 0.100346 | 0.121349 | 0.88 | 0.89 | -0.01 | 0.113954 | 0.612026 | 0.80902 | 0.925335 | 0.153115 |
| tossup_correctness | category | Religion | 365 | 0.692394 | 0.55341 | 0.0582972 | 0.185087 | 0.726027 | 0.723288 | 0.00273973 | 0.163625 | 0.452661 | 0.693318 | 0.888492 | 0.192905 |
| tossup_correctness | category | Science | 1456 | 0.700111 | 0.511108 | 0.0851855 | 0.16718 | 0.767857 | 0.76717 | 0.000686813 | 0.165461 | 0.466478 | 0.706271 | 0.87918 | 0.188318 |
| tossup_correctness | category | Social Science | 333 | 0.759945 | 0.505697 | 0.085188 | 0.165926 | 0.786787 | 0.72973 | 0.0570571 | 0.182492 | 0.380098 | 0.677031 | 0.870554 | 0.192822 |
| tossup_correctness | category | Unknown | 1990 | 0.73742 | 0.498224 | 0.0883834 | 0.162309 | 0.773869 | 0.765829 | 0.0080402 | 0.166218 | 0.439739 | 0.698372 | 0.876069 | 0.190852 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.724544 | 0.534615 | 0.136157 | 0.178809 | 0.75419 | 0.748603 | 0.00558659 | 0.179413 | 0.369753 | 0.645621 | 0.845965 | 0.202947 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.699299 | 0.525558 | 0.0864179 | 0.173858 | 0.757576 | 0.754441 | 0.0031348 | 0.173221 | 0.426799 | 0.681535 | 0.883933 | 0.191205 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.716908 | 0.502157 | 0.0721257 | 0.164059 | 0.771221 | 0.766682 | 0.00453926 | 0.168276 | 0.461285 | 0.71963 | 0.897854 | 0.18378 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.707101 | 0.485482 | 0.0798617 | 0.156759 | 0.787777 | 0.787441 | 0.000335796 | 0.16189 | 0.481291 | 0.736776 | 0.898098 | 0.179497 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.713984 | 0.495325 | 0.0675236 | 0.161107 | 0.773789 | 0.771758 | 0.00203183 | 0.161053 | 0.473625 | 0.734325 | 0.892306 | 0.182317 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 4.366 | 0.582007 | 2.30814 | 3.38342 | 3.99176 | 4.37181 | 4.76358 | 5.30833 | 5.84491 |
| player | theta_1 | 1196 | -1.25768 | 0.992496 | -4.05201 | -2.59744 | -1.97228 | -1.4368 | -0.632452 | 0.642741 | 2.56217 |
| player | theta_2 | 1196 | -0.984537 | 0.722515 | -3.40618 | -2.24082 | -1.43247 | -0.939536 | -0.471892 | 0.0976417 | 1.72237 |
| player | theta_3 | 1196 | -1.12424 | 0.725442 | -3.55891 | -2.2592 | -1.62335 | -1.14157 | -0.626331 | 0.114161 | 1.56517 |
| player | theta_norm | 1196 | 2.32471 | 0.665369 | 0.394778 | 1.21784 | 1.8422 | 2.35383 | 2.79685 | 3.37107 | 4.5805 |
| tossup | start_difficulty_d1 | 1240 | -0.745671 | 0.658359 | -3.56195 | -2.00897 | -1.08139 | -0.659887 | -0.350863 | 0.216508 | 1.57624 |
| tossup | start_difficulty_d2 | 1240 | -0.623052 | 0.525402 | -3.16916 | -1.59935 | -0.805802 | -0.577499 | -0.361561 | 0.172424 | 1.3851 |
| tossup | start_difficulty_d3 | 1240 | -0.630534 | 0.530081 | -3.13778 | -1.63926 | -0.821195 | -0.564325 | -0.359299 | 0.0853136 | 1.46701 |
| tossup | end_difficulty_d1 | 1240 | -1.9083 | 0.854918 | -5.50717 | -3.71593 | -2.29044 | -1.77647 | -1.40718 | -0.70971 | 0.728104 |
| tossup | end_difficulty_d2 | 1240 | -1.75008 | 0.672458 | -5.04894 | -2.96741 | -1.97302 | -1.68464 | -1.42026 | -0.764399 | 0.612323 |
| tossup | end_difficulty_d3 | 1240 | -1.7555 | 0.659353 | -5.0358 | -3.02537 | -1.98545 | -1.67225 | -1.40642 | -0.856292 | 0.73875 |
| tossup | total_drop_d1 | 1240 | 1.16263 | 0.256072 | 0.757677 | 0.894752 | 1.02393 | 1.10983 | 1.23372 | 1.56516 | 3.22432 |
| tossup | total_drop_d2 | 1240 | 1.12703 | 0.192484 | 0.737934 | 0.921511 | 1.03113 | 1.09921 | 1.17491 | 1.42636 | 3.20201 |
| tossup | total_drop_d3 | 1240 | 1.12497 | 0.167578 | 0.728261 | 0.92104 | 1.03662 | 1.10416 | 1.17689 | 1.39855 | 3.17986 |
| tossup | drop_share_1_d1 | 1240 | 0.317199 | 0.0212972 | 0.231181 | 0.288514 | 0.30511 | 0.314736 | 0.326998 | 0.354299 | 0.431173 |
| tossup | drop_share_2_d1 | 1240 | 0.349367 | 0.0121233 | 0.309023 | 0.330077 | 0.341231 | 0.348765 | 0.357028 | 0.370186 | 0.412073 |
| tossup | drop_share_3_d1 | 1240 | 0.333434 | 0.0213425 | 0.235709 | 0.293946 | 0.323579 | 0.33562 | 0.346626 | 0.363588 | 0.409323 |
| tossup | drop_share_1_d2 | 1240 | 0.314197 | 0.017711 | 0.195959 | 0.289876 | 0.303595 | 0.312731 | 0.323667 | 0.341298 | 0.411385 |
| tossup | drop_share_2_d2 | 1240 | 0.348656 | 0.0121619 | 0.310384 | 0.329473 | 0.340561 | 0.348844 | 0.356269 | 0.36698 | 0.474029 |
| tossup | drop_share_3_d2 | 1240 | 0.337147 | 0.017155 | 0.250347 | 0.307771 | 0.32837 | 0.338237 | 0.347131 | 0.362638 | 0.403118 |
| tossup | drop_share_1_d3 | 1240 | 0.314682 | 0.0177183 | 0.245805 | 0.289934 | 0.303196 | 0.313794 | 0.323599 | 0.342904 | 0.433167 |
| tossup | drop_share_2_d3 | 1240 | 0.348389 | 0.0117814 | 0.307006 | 0.329465 | 0.340634 | 0.34802 | 0.356387 | 0.367762 | 0.389591 |
| tossup | drop_share_3_d3 | 1240 | 0.336929 | 0.0177346 | 0.258875 | 0.307074 | 0.327505 | 0.337388 | 0.347872 | 0.363033 | 0.417136 |
| tossup | r_1 | 1240 | 0.374041 | 0.20272 | 0.0461533 | 0.091883 | 0.203726 | 0.34305 | 0.536044 | 0.739435 | 0.846095 |
| tossup | r_2 | 1240 | 0.312001 | 0.169433 | 0.0621838 | 0.11002 | 0.184118 | 0.276683 | 0.396914 | 0.649872 | 0.893424 |
| tossup | r_3 | 1240 | 0.313958 | 0.181415 | 0.0493287 | 0.0909125 | 0.172598 | 0.272844 | 0.42811 | 0.673604 | 0.888117 |
| tossup | r_norm | 1240 | 0.658171 | 0.0725841 | 0.577384 | 0.582141 | 0.601742 | 0.635852 | 0.693225 | 0.816255 | 0.896635 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.74471 | 0.960578 | 0.250493 | 0.554469 | 0.935009 | 1.52736 | 2.5161 | 3.44374 | 4.66444 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.47714 | 0.806652 | 0.278236 | 0.531155 | 0.86654 | 1.24969 | 1.94213 | 3.0859 | 4.87816 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.52733 | 0.807728 | 0.237712 | 0.46465 | 0.883385 | 1.38272 | 2.046 | 3.0453 | 4.37383 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.590099 | 1.46129 | -8.24572 | -3.57916 | -1.17958 | -0.155583 | 0.28597 | 0.905827 | 2.13828 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.434017 | 1.27519 | -8.96466 | -2.99903 | -0.453089 | -0.107919 | 0.20105 | 0.627629 | 1.21756 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.595637 | 1.39686 | -9.66563 | -3.43848 | -0.634478 | -0.181205 | 0.168343 | 0.745494 | 1.5608 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.33481 | 2.12574 | 0.831924 | 0.948373 | 1.00516 | 1.08329 | 3.78584 | 6.65992 | 11.4419 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.91116 | 1.829 | 0.875139 | 0.945042 | 0.991005 | 1.05707 | 1.734 | 5.94914 | 11.5614 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.12297 | 1.94335 | 0.844518 | 0.950788 | 1.00015 | 1.09472 | 2.42513 | 6.08787 | 12.5166 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.221626 | 0.0839891 | 0.0340359 | 0.0644873 | 0.14754 | 0.262201 | 0.285914 | 0.302294 | 0.403453 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.32699 | 0.0852576 | 0.0572394 | 0.129965 | 0.330092 | 0.34706 | 0.359029 | 0.42348 | 0.768472 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.451384 | 0.148361 | 0.0893704 | 0.339539 | 0.360514 | 0.381536 | 0.474563 | 0.795457 | 0.904168 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.237596 | 0.0759532 | 0.0273563 | 0.0728625 | 0.198801 | 0.273462 | 0.291683 | 0.305944 | 0.362786 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.333216 | 0.0663389 | 0.0392169 | 0.166778 | 0.335778 | 0.347427 | 0.358386 | 0.386806 | 0.676865 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.429188 | 0.126421 | 0.241685 | 0.34145 | 0.356976 | 0.373236 | 0.43737 | 0.76012 | 0.931043 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.230804 | 0.0775532 | 0.0367461 | 0.0738917 | 0.182381 | 0.265508 | 0.289113 | 0.30657 | 0.572476 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.339184 | 0.0705131 | 0.0579107 | 0.17817 | 0.334806 | 0.347996 | 0.36179 | 0.426836 | 0.713807 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.430012 | 0.124652 | 0.120658 | 0.339479 | 0.358753 | 0.37781 | 0.445693 | 0.739236 | 0.89952 |
| tossup_hazard | hazard_r_1 | 1240 | 0.367691 | 0.311915 | 0.0252098 | 0.0417464 | 0.0911402 | 0.235078 | 0.658488 | 0.914984 | 0.961335 |
| tossup_hazard | hazard_r_2 | 1240 | 0.293489 | 0.265891 | 0.0139446 | 0.0328927 | 0.0690124 | 0.178135 | 0.502151 | 0.808861 | 0.922691 |
| tossup_hazard | hazard_r_3 | 1240 | 0.33882 | 0.281879 | 0.00962533 | 0.0265843 | 0.0826891 | 0.246866 | 0.587182 | 0.844932 | 0.932632 |
