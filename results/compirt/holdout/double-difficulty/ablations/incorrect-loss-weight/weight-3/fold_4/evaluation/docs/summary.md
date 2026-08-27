# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-3/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-3/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 297330 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.717269 |
| log_loss | 0.582109 |
| ece | 0.194087 |
| brier | 0.199117 |
| accuracy | 0.690076 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0832794 |
| probability_std | 0.211419 |
| probability_p10 | 0.279362 |
| probability_p50 | 0.597435 |
| probability_p90 | 0.848632 |
| mean_predictive_variance | 0.199019 |
| integrated_brier_score | 0.101197 |
| joint_tossup_event_log_loss | 6.71082 |
| buzz_position_mae | 0.150703 |
| buzz_position_median_absolute_error | 0.133894 |
| buzz_position_bias | -0.0432805 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.349407 |
| first_buzzer_mean_reciprocal_rank | 0.561083 |
| first_buzzer_log_loss | 1.68765 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.717269 |
| neg_average_precision | 0.446719 |
| neg_precision | 0.381011 |
| neg_recall | 0.588291 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.184969 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0133692 |
| no_buzz_calibration_error | 0.00164207 |
| no_buzz_brier | 0.0110196 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.717269 | 0.582109 | 0.194087 | 0.199117 | 0.690076 | 0.773355 | -0.0832794 | 0.211419 | 0.279362 | 0.597435 | 0.848632 | 0.199019 |
| tossup_correctness | tier | fall | 2876 | 0.718371 | 0.557727 | 0.188212 | 0.189009 | 0.713839 | 0.793115 | -0.0792768 | 0.212023 | 0.292896 | 0.629171 | 0.868788 | 0.194041 |
| tossup_correctness | tier | nationals | 1579 | 0.709667 | 0.610131 | 0.176808 | 0.210686 | 0.661811 | 0.729576 | -0.0677644 | 0.218004 | 0.24082 | 0.568393 | 0.835276 | 0.199631 |
| tossup_correctness | tier | regionals | 1990 | 0.73377 | 0.590629 | 0.206582 | 0.202653 | 0.672864 | 0.765829 | -0.0929648 | 0.206631 | 0.268543 | 0.56574 | 0.828315 | 0.203793 |
| tossup_correctness | tier | winter | 2825 | 0.704694 | 0.585266 | 0.201233 | 0.200451 | 0.693805 | 0.783009 | -0.0892035 | 0.207203 | 0.288074 | 0.598649 | 0.84687 | 0.20038 |
| tossup_correctness | category | Current Events | 123 | 0.746882 | 0.598577 | 0.220351 | 0.210595 | 0.601626 | 0.764228 | -0.162602 | 0.220656 | 0.270518 | 0.503409 | 0.85818 | 0.199386 |
| tossup_correctness | category | Fine Arts | 1093 | 0.732367 | 0.5588 | 0.177709 | 0.188971 | 0.716377 | 0.769442 | -0.053065 | 0.211941 | 0.291065 | 0.608143 | 0.859247 | 0.196666 |
| tossup_correctness | category | Geography | 191 | 0.784284 | 0.607198 | 0.20322 | 0.208829 | 0.680628 | 0.691099 | -0.0104712 | 0.232149 | 0.190455 | 0.504329 | 0.778772 | 0.195986 |
| tossup_correctness | category | History | 1469 | 0.706827 | 0.592857 | 0.178294 | 0.203844 | 0.679374 | 0.758339 | -0.0789653 | 0.217585 | 0.272224 | 0.602007 | 0.858519 | 0.196249 |
| tossup_correctness | category | Literature | 1436 | 0.691037 | 0.540084 | 0.181835 | 0.18046 | 0.74234 | 0.81546 | -0.0731198 | 0.197698 | 0.347366 | 0.668533 | 0.866326 | 0.19306 |
| tossup_correctness | category | Mythology | 325 | 0.689709 | 0.544639 | 0.22086 | 0.182947 | 0.729231 | 0.843077 | -0.113846 | 0.184998 | 0.368538 | 0.645685 | 0.852712 | 0.200839 |
| tossup_correctness | category | Other Academic | 67 | 0.714286 | 0.653677 | 0.269325 | 0.229649 | 0.61194 | 0.791045 | -0.179104 | 0.198176 | 0.268608 | 0.489313 | 0.797294 | 0.210255 |
| tossup_correctness | category | Philosophy | 322 | 0.660938 | 0.599012 | 0.186243 | 0.208138 | 0.664596 | 0.785714 | -0.121118 | 0.21378 | 0.296276 | 0.606056 | 0.889413 | 0.194404 |
| tossup_correctness | category | Popular Culture | 100 | 0.558733 | 0.492003 | 0.213673 | 0.158817 | 0.78 | 0.89 | -0.11 | 0.13297 | 0.499112 | 0.680462 | 0.839811 | 0.201228 |
| tossup_correctness | category | Religion | 365 | 0.652978 | 0.645851 | 0.169552 | 0.227014 | 0.624658 | 0.723288 | -0.0986301 | 0.213545 | 0.262912 | 0.570738 | 0.831039 | 0.201444 |
| tossup_correctness | category | Science | 1456 | 0.722056 | 0.598439 | 0.209 | 0.205913 | 0.679258 | 0.76717 | -0.0879121 | 0.209601 | 0.25656 | 0.578245 | 0.829863 | 0.202684 |
| tossup_correctness | category | Social Science | 333 | 0.73626 | 0.612649 | 0.204187 | 0.213815 | 0.660661 | 0.72973 | -0.0690691 | 0.224836 | 0.208227 | 0.549123 | 0.822632 | 0.198796 |
| tossup_correctness | category | Unknown | 1990 | 0.73377 | 0.590629 | 0.206582 | 0.202653 | 0.672864 | 0.765829 | -0.0929648 | 0.206631 | 0.268543 | 0.56574 | 0.828315 | 0.203793 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.733499 | 0.631186 | 0.23313 | 0.220708 | 0.648045 | 0.748603 | -0.100559 | 0.210452 | 0.237251 | 0.529286 | 0.782978 | 0.20547 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.697024 | 0.60771 | 0.193475 | 0.210754 | 0.661442 | 0.754441 | -0.092999 | 0.208416 | 0.263046 | 0.570851 | 0.836689 | 0.202846 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.720752 | 0.577826 | 0.18356 | 0.197306 | 0.694961 | 0.766682 | -0.0717204 | 0.21116 | 0.281941 | 0.602814 | 0.847159 | 0.198502 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.705001 | 0.568602 | 0.191373 | 0.193409 | 0.699127 | 0.787441 | -0.0883143 | 0.203285 | 0.313722 | 0.615618 | 0.852822 | 0.199446 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.729867 | 0.587654 | 0.202509 | 0.201145 | 0.68913 | 0.771758 | -0.0826278 | 0.218777 | 0.252566 | 0.585387 | 0.849258 | 0.197341 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.68877 | 0.786498 | 0.382082 | 1.39826 | 2.15274 | 2.67731 | 3.21933 | 4.06067 | 4.72008 |
| player | theta_1 | 1196 | -1.23324 | 0.956015 | -3.77067 | -2.70313 | -1.86721 | -1.26863 | -0.696232 | 0.44453 | 2.37024 |
| player | theta_2 | 1196 | -1.05097 | 0.806193 | -3.63686 | -2.43322 | -1.5554 | -1.02969 | -0.550744 | 0.263765 | 1.68462 |
| player | theta_3 | 1196 | -1.13045 | 0.842032 | -4.07273 | -2.47297 | -1.66086 | -1.18605 | -0.63015 | 0.401462 | 2.18969 |
| player | theta_norm | 1196 | 2.36971 | 0.747854 | 0.262785 | 1.22232 | 1.83352 | 2.31266 | 2.86675 | 3.63545 | 4.7538 |
| tossup | start_difficulty_d1 | 1240 | -0.73626 | 0.666202 | -3.27974 | -1.75731 | -1.12349 | -0.755335 | -0.371688 | 0.355158 | 2.61293 |
| tossup | start_difficulty_d2 | 1240 | -0.714424 | 0.615957 | -3.10805 | -1.68141 | -1.0956 | -0.727386 | -0.344348 | 0.33233 | 1.51649 |
| tossup | start_difficulty_d3 | 1240 | -0.711285 | 0.602477 | -3.40442 | -1.68323 | -1.09876 | -0.734821 | -0.341116 | 0.352244 | 1.8777 |
| tossup | end_difficulty_d1 | 1240 | -1.741 | 0.775275 | -4.624 | -2.9524 | -2.20754 | -1.75843 | -1.30373 | -0.524773 | 1.94285 |
| tossup | end_difficulty_d2 | 1240 | -1.70946 | 0.73172 | -4.7748 | -2.89259 | -2.13353 | -1.72438 | -1.28199 | -0.519888 | 0.907145 |
| tossup | end_difficulty_d3 | 1240 | -1.70285 | 0.707236 | -4.95062 | -2.83573 | -2.13459 | -1.71276 | -1.2764 | -0.521559 | 1.23005 |
| tossup | total_drop_d1 | 1240 | 1.00474 | 0.214538 | 0.576087 | 0.745537 | 0.892909 | 0.982372 | 1.07096 | 1.27785 | 4.59212 |
| tossup | total_drop_d2 | 1240 | 0.995035 | 0.184716 | 0.538159 | 0.763419 | 0.90395 | 0.982505 | 1.06439 | 1.25243 | 3.77412 |
| tossup | total_drop_d3 | 1240 | 0.991562 | 0.150166 | 0.640797 | 0.776411 | 0.901104 | 0.977078 | 1.061 | 1.24934 | 2.27182 |
| tossup | drop_share_1_d1 | 1240 | 0.30118 | 0.0239444 | 0.115392 | 0.263567 | 0.290686 | 0.302905 | 0.315375 | 0.334615 | 0.39537 |
| tossup | drop_share_2_d1 | 1240 | 0.347369 | 0.0157009 | 0.26208 | 0.325571 | 0.338672 | 0.347015 | 0.355607 | 0.369215 | 0.60536 |
| tossup | drop_share_3_d1 | 1240 | 0.351451 | 0.0255889 | 0.279248 | 0.315531 | 0.337048 | 0.349374 | 0.363124 | 0.390933 | 0.58975 |
| tossup | drop_share_1_d2 | 1240 | 0.301452 | 0.0204328 | 0.110818 | 0.271433 | 0.291253 | 0.302442 | 0.313773 | 0.330222 | 0.381754 |
| tossup | drop_share_2_d2 | 1240 | 0.347013 | 0.0134681 | 0.302724 | 0.326565 | 0.338327 | 0.346745 | 0.35502 | 0.367905 | 0.482707 |
| tossup | drop_share_3_d2 | 1240 | 0.351535 | 0.0218764 | 0.283504 | 0.319354 | 0.33782 | 0.350989 | 0.362033 | 0.38667 | 0.583976 |
| tossup | drop_share_1_d3 | 1240 | 0.301232 | 0.0206106 | 0.167021 | 0.266787 | 0.290954 | 0.302128 | 0.313854 | 0.331635 | 0.393572 |
| tossup | drop_share_2_d3 | 1240 | 0.346964 | 0.0124777 | 0.266493 | 0.326893 | 0.339246 | 0.346827 | 0.354793 | 0.367752 | 0.39293 |
| tossup | drop_share_3_d3 | 1240 | 0.351804 | 0.0224255 | 0.280645 | 0.320991 | 0.338065 | 0.351161 | 0.362592 | 0.387979 | 0.56444 |
| tossup | r_1 | 1240 | 0.344487 | 0.224016 | 0.0364348 | 0.0724427 | 0.150073 | 0.285472 | 0.513814 | 0.757178 | 0.882257 |
| tossup | r_2 | 1240 | 0.329929 | 0.211966 | 0.031405 | 0.0812459 | 0.162683 | 0.269958 | 0.457191 | 0.761445 | 0.897877 |
| tossup | r_3 | 1240 | 0.325584 | 0.207158 | 0.051601 | 0.0820769 | 0.150191 | 0.276898 | 0.448906 | 0.744734 | 0.929003 |
| tossup | r_norm | 1240 | 0.682263 | 0.0772528 | 0.57739 | 0.585782 | 0.618391 | 0.665106 | 0.735602 | 0.829699 | 0.930376 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47055 | 0.496419 | 1.7269 | 3.74769 | 4.20268 | 4.42294 | 4.68878 | 5.39999 | 6.4061 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45734 | 0.439887 | 2.00457 | 3.81067 | 4.21737 | 4.42121 | 4.67566 | 5.20927 | 6.68011 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.44657 | 0.430953 | 2.53096 | 3.73864 | 4.22056 | 4.415 | 4.67301 | 5.19077 | 6.18711 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.78701 | 2.32256 | -12.0994 | -2.94248 | 0.691975 | 2.94353 | 3.31183 | 3.6588 | 4.40682 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.24257 | 2.0891 | -9.4004 | -2.87349 | 2.35045 | 3.11609 | 3.36953 | 3.7058 | 4.29624 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.12933 | 2.15157 | -9.55258 | -2.5401 | 1.84806 | 3.11653 | 3.36448 | 3.73742 | 4.28162 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.68353 | 2.49443 | 0.860002 | 0.97927 | 1.04961 | 1.26339 | 3.94177 | 7.78004 | 16.8683 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.21476 | 2.26661 | 0.901834 | 0.958907 | 1.02131 | 1.14285 | 1.97659 | 7.53927 | 14.232 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.31724 | 2.27394 | 0.847338 | 0.966332 | 1.02352 | 1.14895 | 2.49808 | 7.31277 | 14.2363 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.238526 | 0.0807384 | 0.0358271 | 0.0814669 | 0.181561 | 0.273648 | 0.293856 | 0.316992 | 0.526961 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.341989 | 0.0764504 | 0.0541555 | 0.176253 | 0.336223 | 0.350796 | 0.36478 | 0.452215 | 0.681518 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.419485 | 0.131179 | 0.119296 | 0.301759 | 0.348935 | 0.368318 | 0.433535 | 0.738929 | 0.903431 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.251601 | 0.0723822 | 0.0304901 | 0.0889192 | 0.235561 | 0.281062 | 0.297195 | 0.315514 | 0.675081 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.346221 | 0.0622015 | 0.0600597 | 0.213144 | 0.339969 | 0.350484 | 0.36185 | 0.415536 | 0.67729 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.402178 | 0.109106 | 0.0912988 | 0.320702 | 0.34898 | 0.365334 | 0.399102 | 0.683067 | 0.897017 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.2506 | 0.0718575 | 0.038544 | 0.0922084 | 0.225923 | 0.279878 | 0.296862 | 0.31537 | 0.568117 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348974 | 0.0616373 | 0.0826538 | 0.231865 | 0.338072 | 0.35048 | 0.363588 | 0.435808 | 0.715256 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.400426 | 0.10762 | 0.075219 | 0.31633 | 0.348711 | 0.36534 | 0.401308 | 0.663453 | 0.877514 |
| tossup_hazard | hazard_r_1 | 1240 | 0.378798 | 0.281304 | 0.0309643 | 0.0598623 | 0.132121 | 0.272249 | 0.622004 | 0.877891 | 0.946631 |
| tossup_hazard | hazard_r_2 | 1240 | 0.298302 | 0.226028 | 0.0225636 | 0.0555306 | 0.117361 | 0.211879 | 0.462496 | 0.732915 | 0.890815 |
| tossup_hazard | hazard_r_3 | 1240 | 0.3229 | 0.245363 | 0.0295753 | 0.0512374 | 0.112629 | 0.227004 | 0.521485 | 0.765632 | 0.921629 |
