# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283393 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.715498 |
| log_loss | 0.491008 |
| ece | 0.0102672 |
| brier | 0.159735 |
| accuracy | 0.775305 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0111267 |
| probability_std | 0.14095 |
| probability_p10 | 0.577205 |
| probability_p50 | 0.808242 |
| probability_p90 | 0.916716 |
| mean_predictive_variance | 0.155981 |
| integrated_brier_score | 0.102033 |
| joint_tossup_event_log_loss | 6.62884 |
| buzz_position_mae | 0.150045 |
| buzz_position_median_absolute_error | 0.130976 |
| buzz_position_bias | -0.0366293 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.351302 |
| first_buzzer_mean_reciprocal_rank | 0.565824 |
| first_buzzer_log_loss | 1.66659 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.715498 |
| neg_average_precision | 0.449458 |
| neg_precision | 0.601578 |
| neg_recall | 0.139716 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.199321 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0142358 |
| no_buzz_calibration_error | 0.00112282 |
| no_buzz_brier | 0.0129761 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.715498 | 0.491008 | 0.0102672 | 0.159735 | 0.775305 | 0.764178 | 0.0111267 | 0.14095 | 0.577205 | 0.808242 | 0.916716 | 0.155981 |
| tossup_correctness | tier | fall | 2798 | 0.741946 | 0.456453 | 0.0239593 | 0.146185 | 0.792709 | 0.785204 | 0.00750536 | 0.142119 | 0.575812 | 0.818332 | 0.920924 | 0.152545 |
| tossup_correctness | tier | nationals | 1545 | 0.713332 | 0.535789 | 0.0476238 | 0.178268 | 0.746278 | 0.721036 | 0.0252427 | 0.144116 | 0.563688 | 0.792735 | 0.911323 | 0.162027 |
| tossup_correctness | tier | regionals | 2039 | 0.708555 | 0.496536 | 0.00967863 | 0.161912 | 0.773418 | 0.762138 | 0.01128 | 0.133905 | 0.57792 | 0.801314 | 0.914085 | 0.158995 |
| tossup_correctness | tier | winter | 2875 | 0.69329 | 0.496653 | 0.0166804 | 0.161419 | 0.775304 | 0.768348 | 0.00695652 | 0.142473 | 0.58726 | 0.810612 | 0.916484 | 0.153939 |
| tossup_correctness | category | Current Events | 129 | 0.689832 | 0.605383 | 0.0999235 | 0.20813 | 0.682171 | 0.666667 | 0.0155039 | 0.151723 | 0.508222 | 0.78926 | 0.925441 | 0.162913 |
| tossup_correctness | category | Fine Arts | 1074 | 0.710557 | 0.476032 | 0.0250521 | 0.152899 | 0.792365 | 0.776536 | 0.0158287 | 0.152577 | 0.571288 | 0.796849 | 0.916535 | 0.158574 |
| tossup_correctness | category | Geography | 180 | 0.753884 | 0.562172 | 0.0783853 | 0.18974 | 0.727778 | 0.616667 | 0.111111 | 0.230607 | 0.229851 | 0.767473 | 0.910678 | 0.16301 |
| tossup_correctness | category | History | 1454 | 0.697624 | 0.507697 | 0.0262932 | 0.166156 | 0.767538 | 0.757909 | 0.00962861 | 0.140176 | 0.568666 | 0.809737 | 0.921748 | 0.155306 |
| tossup_correctness | category | Literature | 1435 | 0.730565 | 0.431888 | 0.0274054 | 0.135198 | 0.815331 | 0.810453 | 0.00487805 | 0.119496 | 0.64021 | 0.840903 | 0.923871 | 0.140612 |
| tossup_correctness | category | Mythology | 324 | 0.684476 | 0.475725 | 0.0312064 | 0.152388 | 0.780864 | 0.79321 | -0.0123457 | 0.115293 | 0.65643 | 0.836249 | 0.91738 | 0.143256 |
| tossup_correctness | category | Other Academic | 71 | 0.589325 | 0.547048 | 0.0928849 | 0.177116 | 0.760563 | 0.760563 | 0 | 0.107806 | 0.639668 | 0.808038 | 0.899591 | 0.161061 |
| tossup_correctness | category | Philosophy | 310 | 0.727726 | 0.489686 | 0.0293993 | 0.160658 | 0.770968 | 0.76129 | 0.00967742 | 0.119746 | 0.619795 | 0.796853 | 0.916803 | 0.159417 |
| tossup_correctness | category | Popular Culture | 108 | 0.499132 | 0.373329 | 0.114282 | 0.106406 | 0.888889 | 0.888889 | 0 | 0.0737723 | 0.748567 | 0.848834 | 0.913721 | 0.130532 |
| tossup_correctness | category | Religion | 361 | 0.681833 | 0.533101 | 0.0240443 | 0.177507 | 0.742382 | 0.742382 | 0 | 0.142022 | 0.529689 | 0.755443 | 0.887801 | 0.175623 |
| tossup_correctness | category | Science | 1445 | 0.723388 | 0.507899 | 0.0299594 | 0.167894 | 0.755709 | 0.746021 | 0.00968858 | 0.13821 | 0.573764 | 0.798063 | 0.906358 | 0.160937 |
| tossup_correctness | category | Social Science | 327 | 0.734297 | 0.528659 | 0.0364147 | 0.176704 | 0.740061 | 0.718654 | 0.0214067 | 0.176425 | 0.467099 | 0.780039 | 0.912677 | 0.165584 |
| tossup_correctness | category | Unknown | 2039 | 0.708555 | 0.496536 | 0.00967863 | 0.161912 | 0.773418 | 0.762138 | 0.01128 | 0.133905 | 0.57792 | 0.801314 | 0.914085 | 0.158995 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.661295 | 0.538297 | 0.0500867 | 0.180857 | 0.73224 | 0.743169 | -0.010929 | 0.143921 | 0.51123 | 0.765612 | 0.900366 | 0.173661 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.722346 | 0.522045 | 0.0235699 | 0.1729 | 0.746597 | 0.728796 | 0.017801 | 0.14529 | 0.537771 | 0.785176 | 0.905232 | 0.165602 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.732388 | 0.49309 | 0.02055 | 0.16093 | 0.770433 | 0.752568 | 0.0178651 | 0.143738 | 0.576176 | 0.807005 | 0.912404 | 0.156378 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.711075 | 0.470792 | 0.0131047 | 0.151647 | 0.791652 | 0.786087 | 0.00556522 | 0.127569 | 0.616614 | 0.822996 | 0.919925 | 0.14901 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.704554 | 0.496055 | 0.0181258 | 0.161112 | 0.775042 | 0.764393 | 0.0106489 | 0.147149 | 0.557567 | 0.801919 | 0.918134 | 0.158221 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.63259 | 0.739861 | 0.539124 | 1.43895 | 2.14695 | 2.6138 | 3.13321 | 3.88617 | 4.55178 |
| player | theta_1 | 1197 | -1.19556 | 0.860253 | -3.52699 | -2.53125 | -1.7701 | -1.23938 | -0.697853 | 0.320651 | 1.89122 |
| player | theta_2 | 1197 | -0.992832 | 0.622739 | -3.23566 | -2.01932 | -1.3892 | -0.978037 | -0.581589 | 0.0168858 | 1.37077 |
| player | theta_3 | 1197 | -1.07654 | 0.756054 | -3.07317 | -2.1977 | -1.57073 | -1.15598 | -0.640805 | 0.271966 | 2.05983 |
| player | theta_norm | 1197 | 2.2097 | 0.624205 | 0.388319 | 1.2702 | 1.75352 | 2.1773 | 2.62765 | 3.26543 | 4.29863 |
| tossup | start_difficulty_d1 | 1240 | -1.76988 | 0.54234 | -3.47182 | -2.53499 | -2.12505 | -1.84018 | -1.46968 | -0.805299 | 1.086 |
| tossup | start_difficulty_d2 | 1240 | -1.76453 | 0.501236 | -3.28845 | -2.522 | -2.10636 | -1.79819 | -1.44339 | -0.881039 | 0.397993 |
| tossup | start_difficulty_d3 | 1240 | -1.76454 | 0.505895 | -3.50605 | -2.5446 | -2.11166 | -1.79572 | -1.44201 | -0.903833 | 0.0855034 |
| tossup | end_difficulty_d1 | 1240 | -2.75595 | 0.632406 | -4.57319 | -3.64337 | -3.16933 | -2.83162 | -2.40695 | -1.63344 | 0.374775 |
| tossup | end_difficulty_d2 | 1240 | -2.74949 | 0.587043 | -4.59154 | -3.65554 | -3.14021 | -2.7861 | -2.3714 | -1.74578 | -0.285045 |
| tossup | end_difficulty_d3 | 1240 | -2.74714 | 0.589124 | -4.79787 | -3.65968 | -3.15492 | -2.78323 | -2.37157 | -1.77121 | -0.634879 |
| tossup | total_drop_d1 | 1240 | 0.98607 | 0.111533 | 0.599237 | 0.796954 | 0.911438 | 0.989209 | 1.06451 | 1.14829 | 1.59902 |
| tossup | total_drop_d2 | 1240 | 0.984958 | 0.10259 | 0.656829 | 0.821763 | 0.914227 | 0.985149 | 1.05386 | 1.16172 | 1.34171 |
| tossup | total_drop_d3 | 1240 | 0.982596 | 0.101399 | 0.648052 | 0.816339 | 0.908264 | 0.983573 | 1.04865 | 1.15604 | 1.29182 |
| tossup | drop_share_1_d1 | 1240 | 0.248757 | 0.0313891 | 0.100589 | 0.19982 | 0.230185 | 0.248485 | 0.268906 | 0.299111 | 0.375514 |
| tossup | drop_share_2_d1 | 1240 | 0.372263 | 0.0223649 | 0.271915 | 0.333749 | 0.359378 | 0.373282 | 0.386995 | 0.405893 | 0.475127 |
| tossup | drop_share_3_d1 | 1240 | 0.37898 | 0.040228 | 0.25728 | 0.320715 | 0.35142 | 0.378503 | 0.401703 | 0.44514 | 0.613287 |
| tossup | drop_share_1_d2 | 1240 | 0.248104 | 0.0286797 | 0.141742 | 0.202078 | 0.230078 | 0.247189 | 0.26666 | 0.294384 | 0.365508 |
| tossup | drop_share_2_d2 | 1240 | 0.371993 | 0.0204496 | 0.293528 | 0.339098 | 0.358642 | 0.371934 | 0.38563 | 0.405309 | 0.440827 |
| tossup | drop_share_3_d2 | 1240 | 0.379903 | 0.0360812 | 0.271075 | 0.323547 | 0.355151 | 0.379907 | 0.401495 | 0.439148 | 0.524967 |
| tossup | drop_share_1_d3 | 1240 | 0.248052 | 0.0296985 | 0.141117 | 0.198939 | 0.229835 | 0.248317 | 0.267767 | 0.295467 | 0.405441 |
| tossup | drop_share_2_d3 | 1240 | 0.372421 | 0.0204882 | 0.294511 | 0.339915 | 0.358892 | 0.37274 | 0.385957 | 0.405623 | 0.452753 |
| tossup | drop_share_3_d3 | 1240 | 0.379526 | 0.0364331 | 0.264074 | 0.323659 | 0.355134 | 0.376875 | 0.402248 | 0.441703 | 0.54115 |
| tossup | r_1 | 1240 | 0.322252 | 0.147821 | 0.0685756 | 0.130794 | 0.209387 | 0.290103 | 0.410537 | 0.621635 | 0.862181 |
| tossup | r_2 | 1240 | 0.333904 | 0.111699 | 0.0688092 | 0.165516 | 0.260099 | 0.327093 | 0.39641 | 0.542578 | 0.718075 |
| tossup | r_3 | 1240 | 0.343843 | 0.121077 | 0.0690094 | 0.161333 | 0.257458 | 0.336967 | 0.41393 | 0.552598 | 0.804938 |
| tossup | r_norm | 1240 | 0.617025 | 0.0423788 | 0.577363 | 0.579638 | 0.587896 | 0.603047 | 0.630308 | 0.707737 | 0.867671 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.42374 | 0.476451 | 1.98782 | 3.71337 | 4.14682 | 4.39098 | 4.65068 | 5.23145 | 6.12259 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.4096 | 0.421914 | 2.29483 | 3.7464 | 4.17944 | 4.38889 | 4.61294 | 5.08155 | 6.74731 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.40947 | 0.419642 | 2.55506 | 3.75012 | 4.17699 | 4.3953 | 4.63074 | 5.14248 | 6.20887 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.64816 | 2.40741 | -11.8297 | -3.55409 | 0.486901 | 2.84536 | 3.26106 | 3.58834 | 4.17146 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.20784 | 2.10282 | -9.76727 | -2.5788 | 2.27841 | 3.06294 | 3.35243 | 3.65643 | 4.20684 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.10645 | 2.27838 | -11.4949 | -2.93176 | 2.16712 | 3.0596 | 3.35258 | 3.67143 | 4.09302 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.77558 | 2.5458 | 0.906599 | 0.986099 | 1.06026 | 1.35954 | 4.1145 | 8.2018 | 16.2718 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.20177 | 2.24961 | 0.874834 | 0.962941 | 1.02504 | 1.16692 | 1.87363 | 7.18818 | 14.935 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.30301 | 2.39857 | 0.861741 | 0.969466 | 1.02957 | 1.18071 | 2.06227 | 7.58802 | 16.0963 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.157365 | 0.0815151 | 0.0162931 | 0.0317389 | 0.0873221 | 0.171444 | 0.214305 | 0.269744 | 0.654752 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.330038 | 0.125033 | 0.0258972 | 0.0898935 | 0.28605 | 0.343699 | 0.379216 | 0.511009 | 0.844604 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.512597 | 0.173705 | 0.0429044 | 0.286587 | 0.402503 | 0.470538 | 0.590074 | 0.872491 | 0.957157 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.173602 | 0.0757816 | 0.0101359 | 0.0377343 | 0.128795 | 0.188381 | 0.222087 | 0.268835 | 0.716217 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.337201 | 0.104974 | 0.0234756 | 0.109591 | 0.310818 | 0.344642 | 0.377739 | 0.472982 | 0.845143 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.489197 | 0.148342 | 0.0518256 | 0.312887 | 0.406355 | 0.453676 | 0.530179 | 0.84619 | 0.960667 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.170243 | 0.0724568 | 0.0139726 | 0.0353875 | 0.124675 | 0.184537 | 0.219655 | 0.262537 | 0.577033 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.337585 | 0.101556 | 0.0349955 | 0.110975 | 0.310255 | 0.343961 | 0.376814 | 0.482994 | 0.852801 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.492173 | 0.146585 | 0.0259279 | 0.317886 | 0.40947 | 0.463324 | 0.535776 | 0.843964 | 0.949295 |
| tossup_hazard | hazard_r_1 | 1240 | 0.387092 | 0.274837 | 0.0287791 | 0.0630594 | 0.135718 | 0.31057 | 0.621168 | 0.862998 | 0.947738 |
| tossup_hazard | hazard_r_2 | 1240 | 0.296181 | 0.203423 | 0.0232671 | 0.0576695 | 0.124857 | 0.240011 | 0.441348 | 0.691303 | 0.832508 |
| tossup_hazard | hazard_r_3 | 1240 | 0.316727 | 0.230446 | 0.0229132 | 0.0547201 | 0.130409 | 0.240226 | 0.469986 | 0.773174 | 0.920267 |
