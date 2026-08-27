# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283576 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.71054 |
| log_loss | 0.486601 |
| ece | 0.0133902 |
| brier | 0.157025 |
| accuracy | 0.781167 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0111233 |
| probability_std | 0.144454 |
| probability_p10 | 0.577565 |
| probability_p50 | 0.817032 |
| probability_p90 | 0.924654 |
| mean_predictive_variance | 0.151096 |
| integrated_brier_score | 0.1001 |
| joint_tossup_event_log_loss | 6.52985 |
| buzz_position_mae | 0.15055 |
| buzz_position_median_absolute_error | 0.133204 |
| buzz_position_bias | -0.049908 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.380837 |
| first_buzzer_mean_reciprocal_rank | 0.587207 |
| first_buzzer_log_loss | 1.63214 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.71054 |
| neg_average_precision | 0.44744 |
| neg_precision | 0.6 |
| neg_recall | 0.145115 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.180798 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.014322 |
| no_buzz_calibration_error | -0.000862424 |
| no_buzz_brier | 0.0133439 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.71054 | 0.486601 | 0.0133902 | 0.157025 | 0.781167 | 0.770044 | 0.0111233 | 0.144454 | 0.577565 | 0.817032 | 0.924654 | 0.151096 |
| tossup_correctness | tier | fall | 2817 | 0.704172 | 0.476939 | 0.0219641 | 0.15256 | 0.788427 | 0.781683 | 0.00674476 | 0.142713 | 0.576087 | 0.825506 | 0.928237 | 0.147721 |
| tossup_correctness | tier | nationals | 1542 | 0.72901 | 0.514858 | 0.0304481 | 0.170367 | 0.751621 | 0.73476 | 0.0168612 | 0.14782 | 0.562967 | 0.796837 | 0.917328 | 0.159713 |
| tossup_correctness | tier | regionals | 1934 | 0.711427 | 0.501557 | 0.0233463 | 0.163726 | 0.766805 | 0.75698 | 0.0098242 | 0.141315 | 0.58901 | 0.811023 | 0.920266 | 0.153386 |
| tossup_correctness | tier | winter | 2787 | 0.700007 | 0.470354 | 0.0181315 | 0.149507 | 0.800144 | 0.786868 | 0.0132759 | 0.145611 | 0.589167 | 0.823952 | 0.925924 | 0.148151 |
| tossup_correctness | category | Current Events | 125 | 0.754607 | 0.528886 | 0.0716732 | 0.179001 | 0.704 | 0.704 | 0 | 0.146268 | 0.531314 | 0.766365 | 0.894906 | 0.168983 |
| tossup_correctness | category | Fine Arts | 1072 | 0.725447 | 0.474651 | 0.0315582 | 0.15213 | 0.791978 | 0.770522 | 0.0214552 | 0.149714 | 0.564482 | 0.823753 | 0.926529 | 0.150071 |
| tossup_correctness | category | Geography | 185 | 0.780559 | 0.494847 | 0.0631664 | 0.162044 | 0.745946 | 0.702703 | 0.0432432 | 0.204617 | 0.383365 | 0.755982 | 0.890503 | 0.172156 |
| tossup_correctness | category | History | 1443 | 0.731414 | 0.484279 | 0.0254187 | 0.15762 | 0.774082 | 0.765073 | 0.00900901 | 0.147123 | 0.559607 | 0.800795 | 0.918273 | 0.157948 |
| tossup_correctness | category | Literature | 1411 | 0.674563 | 0.453153 | 0.02635 | 0.142077 | 0.81219 | 0.81219 | 0 | 0.123399 | 0.64773 | 0.855285 | 0.937603 | 0.132797 |
| tossup_correctness | category | Mythology | 320 | 0.661954 | 0.482838 | 0.0411155 | 0.152241 | 0.8 | 0.79375 | 0.00625 | 0.114733 | 0.649278 | 0.829588 | 0.930854 | 0.141498 |
| tossup_correctness | category | Other Academic | 64 | 0.688802 | 0.536067 | 0.0964512 | 0.18016 | 0.71875 | 0.75 | -0.03125 | 0.113463 | 0.640068 | 0.822048 | 0.908948 | 0.150874 |
| tossup_correctness | category | Philosophy | 312 | 0.669935 | 0.466794 | 0.0244473 | 0.148421 | 0.807692 | 0.801282 | 0.00641026 | 0.119272 | 0.634213 | 0.821741 | 0.919563 | 0.149835 |
| tossup_correctness | category | Popular Culture | 104 | 0.633523 | 0.418058 | 0.0366774 | 0.125052 | 0.846154 | 0.846154 | 0 | 0.07933 | 0.714657 | 0.870401 | 0.926664 | 0.122751 |
| tossup_correctness | category | Religion | 358 | 0.716091 | 0.533518 | 0.0341098 | 0.178483 | 0.731844 | 0.726257 | 0.00558659 | 0.145453 | 0.54033 | 0.775057 | 0.899328 | 0.16857 |
| tossup_correctness | category | Science | 1431 | 0.686016 | 0.500416 | 0.0283771 | 0.161501 | 0.780573 | 0.765199 | 0.0153739 | 0.14645 | 0.573694 | 0.806231 | 0.923399 | 0.153863 |
| tossup_correctness | category | Social Science | 321 | 0.739259 | 0.494081 | 0.047991 | 0.159581 | 0.781931 | 0.744548 | 0.0373832 | 0.171669 | 0.511335 | 0.792165 | 0.921336 | 0.159451 |
| tossup_correctness | category | Unknown | 1934 | 0.711427 | 0.501557 | 0.0233463 | 0.163726 | 0.766805 | 0.75698 | 0.0098242 | 0.141315 | 0.58901 | 0.811023 | 0.920266 | 0.153386 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.71912 | 0.555161 | 0.0539229 | 0.188703 | 0.713542 | 0.697917 | 0.015625 | 0.158373 | 0.485109 | 0.74846 | 0.884912 | 0.175248 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.740422 | 0.505202 | 0.02883 | 0.166226 | 0.754781 | 0.733408 | 0.0213723 | 0.152964 | 0.540152 | 0.79807 | 0.914725 | 0.158345 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.692157 | 0.510895 | 0.0288086 | 0.166192 | 0.766968 | 0.759276 | 0.00769231 | 0.144828 | 0.579956 | 0.819249 | 0.923759 | 0.149627 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.693383 | 0.471772 | 0.0173171 | 0.150361 | 0.797839 | 0.789125 | 0.00871384 | 0.127062 | 0.622191 | 0.828602 | 0.927269 | 0.144589 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.727005 | 0.472612 | 0.0159289 | 0.151751 | 0.788014 | 0.775342 | 0.0126712 | 0.153478 | 0.553342 | 0.808716 | 0.925171 | 0.154806 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.67944 | 0.699676 | 0.9115 | 1.57356 | 2.19826 | 2.65644 | 3.12444 | 3.9395 | 4.65864 |
| player | theta_1 | 1133 | -1.22946 | 0.752908 | -3.39858 | -2.38421 | -1.72064 | -1.32072 | -0.743972 | 0.13226 | 1.3627 |
| player | theta_2 | 1133 | -1.09706 | 0.789176 | -3.126 | -2.26845 | -1.59736 | -1.22703 | -0.689192 | 0.49269 | 1.99845 |
| player | theta_3 | 1133 | -0.923675 | 0.713021 | -2.81257 | -2.04231 | -1.38116 | -0.974232 | -0.527365 | 0.337654 | 2.58621 |
| player | theta_norm | 1133 | 2.23283 | 0.528762 | 0.597541 | 1.39442 | 1.88304 | 2.21278 | 2.59177 | 3.12957 | 4.08551 |
| tossup | start_difficulty_d1 | 1240 | -1.77372 | 0.552448 | -3.3568 | -2.55644 | -2.14905 | -1.82793 | -1.45778 | -0.808944 | 1.39858 |
| tossup | start_difficulty_d2 | 1240 | -1.76208 | 0.512908 | -3.68716 | -2.57153 | -2.1105 | -1.80647 | -1.42664 | -0.891008 | 0.244667 |
| tossup | start_difficulty_d3 | 1240 | -1.76673 | 0.505863 | -3.66902 | -2.5648 | -2.11655 | -1.79521 | -1.45277 | -0.902062 | 0.450179 |
| tossup | end_difficulty_d1 | 1240 | -2.76577 | 0.643068 | -4.64612 | -3.68622 | -3.21566 | -2.8291 | -2.37475 | -1.6271 | 0.685089 |
| tossup | end_difficulty_d2 | 1240 | -2.75088 | 0.604281 | -5.32983 | -3.6891 | -3.16114 | -2.79002 | -2.35539 | -1.73796 | -0.389335 |
| tossup | end_difficulty_d3 | 1240 | -2.75693 | 0.593143 | -4.95526 | -3.69529 | -3.17162 | -2.78371 | -2.379 | -1.74299 | -0.371248 |
| tossup | total_drop_d1 | 1240 | 0.992053 | 0.113752 | 0.635421 | 0.810701 | 0.916913 | 0.990908 | 1.06711 | 1.17019 | 1.84163 |
| tossup | total_drop_d2 | 1240 | 0.988804 | 0.109823 | 0.634002 | 0.812446 | 0.914551 | 0.990495 | 1.05976 | 1.16358 | 1.64267 |
| tossup | total_drop_d3 | 1240 | 0.990206 | 0.103931 | 0.696291 | 0.821419 | 0.915108 | 0.988366 | 1.06073 | 1.1658 | 1.33501 |
| tossup | drop_share_1_d1 | 1240 | 0.303952 | 0.0156697 | 0.178396 | 0.277889 | 0.294945 | 0.304486 | 0.313978 | 0.32796 | 0.360927 |
| tossup | drop_share_2_d1 | 1240 | 0.347116 | 0.0118751 | 0.308986 | 0.328473 | 0.339457 | 0.346904 | 0.354795 | 0.367266 | 0.427289 |
| tossup | drop_share_3_d1 | 1240 | 0.348932 | 0.0163764 | 0.297954 | 0.324177 | 0.337456 | 0.348365 | 0.359084 | 0.375917 | 0.43033 |
| tossup | drop_share_1_d2 | 1240 | 0.304269 | 0.0145712 | 0.234509 | 0.280014 | 0.294926 | 0.30475 | 0.314041 | 0.327893 | 0.346912 |
| tossup | drop_share_2_d2 | 1240 | 0.34706 | 0.0112938 | 0.310305 | 0.328837 | 0.33945 | 0.347233 | 0.354393 | 0.365358 | 0.380569 |
| tossup | drop_share_3_d2 | 1240 | 0.348671 | 0.0154881 | 0.303359 | 0.324754 | 0.337891 | 0.348339 | 0.358063 | 0.374382 | 0.437624 |
| tossup | drop_share_1_d3 | 1240 | 0.304124 | 0.0143518 | 0.252089 | 0.281637 | 0.294849 | 0.304653 | 0.313031 | 0.326865 | 0.363863 |
| tossup | drop_share_2_d3 | 1240 | 0.347262 | 0.0112394 | 0.305393 | 0.328941 | 0.339602 | 0.347326 | 0.354921 | 0.365413 | 0.385655 |
| tossup | drop_share_3_d3 | 1240 | 0.348615 | 0.0153116 | 0.295847 | 0.324877 | 0.338366 | 0.347387 | 0.358671 | 0.374048 | 0.40518 |
| tossup | r_1 | 1240 | 0.315586 | 0.144897 | 0.07905 | 0.134291 | 0.207242 | 0.279319 | 0.397417 | 0.595237 | 0.836822 |
| tossup | r_2 | 1240 | 0.348865 | 0.132627 | 0.0796043 | 0.153986 | 0.256008 | 0.330466 | 0.428299 | 0.602897 | 0.824015 |
| tossup | r_3 | 1240 | 0.335549 | 0.116789 | 0.0708027 | 0.16394 | 0.2522 | 0.32847 | 0.405444 | 0.541899 | 0.79462 |
| tossup | r_norm | 1240 | 0.619832 | 0.0434467 | 0.577364 | 0.579589 | 0.588778 | 0.605471 | 0.633767 | 0.711676 | 0.844877 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.50188 | 0.522513 | 1.98676 | 3.71365 | 4.2104 | 4.45231 | 4.76183 | 5.44147 | 6.48731 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.51787 | 0.426059 | 2.93207 | 3.87886 | 4.26284 | 4.48293 | 4.74078 | 5.29718 | 6.2616 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.45853 | 0.390689 | 2.4183 | 3.81246 | 4.25591 | 4.45625 | 4.64464 | 5.13059 | 6.29572 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.47889 | 2.38753 | -10.8471 | -3.27697 | -0.00469875 | 2.63567 | 3.27326 | 3.61761 | 4.22066 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.27143 | 2.21432 | -12.2901 | -2.76558 | 2.27289 | 3.16598 | 3.43934 | 3.75872 | 4.35657 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.4992 | 1.84524 | -11.3421 | -2.04055 | 2.54363 | 3.21204 | 3.45466 | 3.71515 | 4.31208 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.02299 | 2.59858 | 0.914892 | 0.990853 | 1.07749 | 1.4884 | 4.90806 | 8.12667 | 16.2505 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.24644 | 2.33099 | 0.87662 | 0.970613 | 1.02552 | 1.15413 | 2.22185 | 7.7047 | 17.2778 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.95933 | 1.96312 | 0.872374 | 0.96614 | 1.01741 | 1.1159 | 1.68107 | 6.85628 | 16.043 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.230708 | 0.0848974 | 0.0400627 | 0.0776153 | 0.157181 | 0.266823 | 0.293789 | 0.317688 | 0.595558 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.343878 | 0.0822629 | 0.0538839 | 0.167028 | 0.334024 | 0.350905 | 0.367751 | 0.478821 | 0.713704 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.425415 | 0.137303 | 0.0707679 | 0.295126 | 0.347606 | 0.370805 | 0.457137 | 0.746078 | 0.906053 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.248364 | 0.0705469 | 0.0304421 | 0.0933459 | 0.220163 | 0.277501 | 0.296406 | 0.314287 | 0.428472 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.346339 | 0.0593664 | 0.0810911 | 0.219642 | 0.33956 | 0.350671 | 0.360854 | 0.423725 | 0.715682 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.405298 | 0.106458 | 0.163176 | 0.319181 | 0.349339 | 0.367316 | 0.409226 | 0.667289 | 0.882349 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.258578 | 0.0642552 | 0.0383337 | 0.103202 | 0.248113 | 0.282598 | 0.296345 | 0.31407 | 0.471939 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348619 | 0.0516787 | 0.05836 | 0.270616 | 0.340211 | 0.351256 | 0.360465 | 0.407453 | 0.640355 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.392804 | 0.0931276 | 0.16072 | 0.322395 | 0.349367 | 0.364492 | 0.392418 | 0.601445 | 0.903306 |
| tossup_hazard | hazard_r_1 | 1240 | 0.40454 | 0.285081 | 0.0271665 | 0.0594435 | 0.134639 | 0.343113 | 0.664908 | 0.866043 | 0.942137 |
| tossup_hazard | hazard_r_2 | 1240 | 0.319023 | 0.254299 | 0.0275893 | 0.0550104 | 0.105946 | 0.21903 | 0.511371 | 0.812444 | 0.926453 |
| tossup_hazard | hazard_r_3 | 1240 | 0.276437 | 0.232941 | 0.0286623 | 0.0564854 | 0.0997464 | 0.175935 | 0.392097 | 0.772604 | 0.911837 |
