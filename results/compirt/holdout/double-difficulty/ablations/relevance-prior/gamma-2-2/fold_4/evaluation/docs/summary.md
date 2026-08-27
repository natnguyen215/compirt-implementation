# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/gamma-2-2/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/gamma-2-2/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 282654 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.723938 |
| log_loss | 0.484883 |
| ece | 0.0453392 |
| brier | 0.156078 |
| accuracy | 0.785653 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0122977 |
| probability_std | 0.185852 |
| probability_p10 | 0.478411 |
| probability_p50 | 0.77664 |
| probability_p90 | 0.948091 |
| mean_predictive_variance | 0.158067 |
| integrated_brier_score | 0.0941973 |
| joint_tossup_event_log_loss | 6.41887 |
| buzz_position_mae | 0.136297 |
| buzz_position_median_absolute_error | 0.110658 |
| buzz_position_bias | 0.00998309 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.383279 |
| first_buzzer_mean_reciprocal_rank | 0.591031 |
| first_buzzer_log_loss | 1.61217 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.723938 |
| neg_average_precision | 0.45866 |
| neg_precision | 0.552583 |
| neg_recall | 0.285102 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.189335 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0092181 |
| no_buzz_calibration_error | -0.00250898 |
| no_buzz_brier | 0.0103669 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.723938 | 0.484883 | 0.0453392 | 0.156078 | 0.785653 | 0.773355 | 0.0122977 | 0.185852 | 0.478411 | 0.77664 | 0.948091 | 0.158067 |
| tossup_correctness | tier | fall | 2876 | 0.727405 | 0.458935 | 0.0403213 | 0.147022 | 0.801113 | 0.793115 | 0.00799722 | 0.177665 | 0.500479 | 0.796396 | 0.95162 | 0.152297 |
| tossup_correctness | tier | nationals | 1579 | 0.712649 | 0.540464 | 0.0386498 | 0.176187 | 0.746042 | 0.729576 | 0.0164661 | 0.200722 | 0.440274 | 0.747213 | 0.955198 | 0.162948 |
| tossup_correctness | tier | regionals | 1990 | 0.740724 | 0.482303 | 0.0504936 | 0.156384 | 0.786935 | 0.765829 | 0.0211055 | 0.189563 | 0.459714 | 0.757062 | 0.94365 | 0.164865 |
| tossup_correctness | tier | winter | 2825 | 0.710193 | 0.482051 | 0.0534032 | 0.153844 | 0.79115 | 0.783009 | 0.00814159 | 0.180213 | 0.497928 | 0.785319 | 0.942859 | 0.156425 |
| tossup_correctness | category | Current Events | 123 | 0.738078 | 0.477473 | 0.120704 | 0.15792 | 0.788618 | 0.764228 | 0.0243902 | 0.189737 | 0.4748 | 0.699692 | 0.960871 | 0.174786 |
| tossup_correctness | category | Fine Arts | 1093 | 0.718462 | 0.492669 | 0.0450959 | 0.156025 | 0.78957 | 0.769442 | 0.0201281 | 0.185959 | 0.47895 | 0.796589 | 0.955797 | 0.15376 |
| tossup_correctness | category | Geography | 191 | 0.773369 | 0.518484 | 0.121554 | 0.165844 | 0.753927 | 0.691099 | 0.0628272 | 0.222575 | 0.387294 | 0.704193 | 0.917446 | 0.173373 |
| tossup_correctness | category | History | 1469 | 0.71523 | 0.507519 | 0.0398413 | 0.166904 | 0.760381 | 0.758339 | 0.00204221 | 0.192873 | 0.479773 | 0.782151 | 0.952019 | 0.154806 |
| tossup_correctness | category | Literature | 1436 | 0.719085 | 0.441341 | 0.0381853 | 0.138152 | 0.814067 | 0.81546 | -0.00139276 | 0.162716 | 0.541461 | 0.820463 | 0.954311 | 0.144251 |
| tossup_correctness | category | Mythology | 325 | 0.686847 | 0.431918 | 0.0798736 | 0.133478 | 0.824615 | 0.843077 | -0.0184615 | 0.152658 | 0.558134 | 0.799633 | 0.941883 | 0.151776 |
| tossup_correctness | category | Other Academic | 67 | 0.652291 | 0.535695 | 0.138221 | 0.171492 | 0.746269 | 0.791045 | -0.0447761 | 0.164544 | 0.498537 | 0.698714 | 0.927747 | 0.180157 |
| tossup_correctness | category | Philosophy | 322 | 0.695137 | 0.485672 | 0.0593977 | 0.158473 | 0.78882 | 0.785714 | 0.00310559 | 0.175799 | 0.524328 | 0.781775 | 0.982054 | 0.149575 |
| tossup_correctness | category | Popular Culture | 100 | 0.596527 | 0.375882 | 0.0708119 | 0.111811 | 0.88 | 0.89 | -0.01 | 0.113804 | 0.663839 | 0.865328 | 0.944892 | 0.12741 |
| tossup_correctness | category | Religion | 365 | 0.660779 | 0.569298 | 0.0618751 | 0.190408 | 0.726027 | 0.723288 | 0.00273973 | 0.185428 | 0.477621 | 0.733379 | 0.933313 | 0.170873 |
| tossup_correctness | category | Science | 1456 | 0.724 | 0.491518 | 0.0589262 | 0.158163 | 0.783654 | 0.76717 | 0.0164835 | 0.187748 | 0.469411 | 0.762856 | 0.935749 | 0.164247 |
| tossup_correctness | category | Social Science | 333 | 0.758528 | 0.498021 | 0.0638961 | 0.160888 | 0.783784 | 0.72973 | 0.0540541 | 0.196451 | 0.405097 | 0.750667 | 0.936703 | 0.168651 |
| tossup_correctness | category | Unknown | 1990 | 0.740724 | 0.482303 | 0.0504936 | 0.156384 | 0.786935 | 0.765829 | 0.0211055 | 0.189563 | 0.459714 | 0.757062 | 0.94365 | 0.164865 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.742123 | 0.521131 | 0.115138 | 0.175327 | 0.743017 | 0.748603 | -0.00558659 | 0.219631 | 0.321998 | 0.678677 | 0.897648 | 0.183571 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.714611 | 0.515159 | 0.0769473 | 0.169219 | 0.760711 | 0.754441 | 0.00626959 | 0.201118 | 0.397044 | 0.717563 | 0.923167 | 0.174802 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.723428 | 0.495801 | 0.0453487 | 0.160381 | 0.77576 | 0.766682 | 0.00907853 | 0.188016 | 0.469201 | 0.766043 | 0.944312 | 0.161549 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.711606 | 0.472966 | 0.0432882 | 0.150322 | 0.797515 | 0.787441 | 0.0100739 | 0.171454 | 0.522653 | 0.797692 | 0.951438 | 0.152206 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.737625 | 0.476747 | 0.0355031 | 0.153249 | 0.791737 | 0.771758 | 0.0199797 | 0.184889 | 0.479181 | 0.784841 | 0.954421 | 0.154412 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 1.76878 | 0.650434 | -0.655465 | 0.716367 | 1.38243 | 1.78227 | 2.15654 | 2.85083 | 4.30684 |
| player | theta_1 | 1196 | -1.54415 | 0.633044 | -2.99483 | -2.49053 | -2.02659 | -1.57996 | -1.14012 | -0.400222 | 0.478966 |
| player | theta_2 | 1196 | -1.50395 | 0.652063 | -3.31233 | -2.505 | -1.97703 | -1.52583 | -1.07416 | -0.366212 | 0.649005 |
| player | theta_3 | 1196 | -1.5523 | 0.654742 | -4.03613 | -2.58894 | -2.01547 | -1.56851 | -1.08643 | -0.457925 | 0.152998 |
| player | theta_norm | 1196 | 2.82884 | 0.554433 | 1.03925 | 1.9135 | 2.44121 | 2.85493 | 3.20761 | 3.72713 | 4.21358 |
| tossup | start_difficulty_d1 | 1240 | -1.26072 | 0.39278 | -2.47565 | -1.86356 | -1.51908 | -1.28121 | -1.01578 | -0.573353 | 0.467539 |
| tossup | start_difficulty_d2 | 1240 | -1.25349 | 0.402259 | -2.53281 | -1.87347 | -1.52419 | -1.2776 | -1.0066 | -0.532799 | 0.464173 |
| tossup | start_difficulty_d3 | 1240 | -1.27398 | 0.400735 | -2.485 | -1.91618 | -1.53618 | -1.29889 | -1.0157 | -0.587432 | 0.287913 |
| tossup | end_difficulty_d1 | 1240 | -2.25463 | 0.453688 | -3.59818 | -2.94673 | -2.55326 | -2.28132 | -1.98419 | -1.43362 | -0.288364 |
| tossup | end_difficulty_d2 | 1240 | -2.2435 | 0.467404 | -3.46603 | -2.96296 | -2.56255 | -2.27236 | -1.96549 | -1.38845 | -0.182807 |
| tossup | end_difficulty_d3 | 1240 | -2.272 | 0.458443 | -3.67708 | -2.97352 | -2.59117 | -2.2888 | -2.00712 | -1.45337 | -0.517069 |
| tossup | total_drop_d1 | 1240 | 0.993915 | 0.121955 | 0.614332 | 0.806826 | 0.918124 | 0.984908 | 1.06521 | 1.17561 | 1.7564 |
| tossup | total_drop_d2 | 1240 | 0.990013 | 0.125478 | 0.62382 | 0.798594 | 0.911864 | 0.98577 | 1.0569 | 1.18517 | 2.0047 |
| tossup | total_drop_d3 | 1240 | 0.998025 | 0.128633 | 0.629682 | 0.819646 | 0.915478 | 0.984963 | 1.06443 | 1.20563 | 2.00205 |
| tossup | drop_share_1_d1 | 1240 | 0.304637 | 0.0198251 | 0.165242 | 0.272291 | 0.294185 | 0.305184 | 0.317103 | 0.334942 | 0.375899 |
| tossup | drop_share_2_d1 | 1240 | 0.346956 | 0.0131577 | 0.264515 | 0.32635 | 0.338569 | 0.346627 | 0.355161 | 0.367975 | 0.423695 |
| tossup | drop_share_3_d1 | 1240 | 0.348407 | 0.0214119 | 0.286952 | 0.31716 | 0.335463 | 0.347371 | 0.35965 | 0.381936 | 0.570244 |
| tossup | drop_share_1_d2 | 1240 | 0.304189 | 0.0193174 | 0.182133 | 0.273697 | 0.294258 | 0.304963 | 0.315609 | 0.332857 | 0.374626 |
| tossup | drop_share_2_d2 | 1240 | 0.347045 | 0.0130926 | 0.294755 | 0.327246 | 0.338377 | 0.34672 | 0.355125 | 0.368479 | 0.416325 |
| tossup | drop_share_3_d2 | 1240 | 0.348765 | 0.0201491 | 0.283231 | 0.319162 | 0.336588 | 0.348218 | 0.359223 | 0.380075 | 0.493067 |
| tossup | drop_share_1_d3 | 1240 | 0.303731 | 0.0202106 | 0.204297 | 0.270068 | 0.293156 | 0.305323 | 0.317001 | 0.333919 | 0.365184 |
| tossup | drop_share_2_d3 | 1240 | 0.34727 | 0.0134806 | 0.300843 | 0.326483 | 0.33907 | 0.34683 | 0.355433 | 0.368502 | 0.453174 |
| tossup | drop_share_3_d3 | 1240 | 0.348999 | 0.02104 | 0.291011 | 0.318949 | 0.335554 | 0.348109 | 0.359193 | 0.384607 | 0.482651 |
| tossup | r_1 | 1240 | 0.648894 | 0.289204 | 0.15898 | 0.309285 | 0.43596 | 0.585256 | 0.794324 | 1.19657 | 2.06168 |
| tossup | r_2 | 1240 | 0.670346 | 0.298767 | 0.152664 | 0.307243 | 0.449909 | 0.612765 | 0.821883 | 1.23605 | 2.29868 |
| tossup | r_3 | 1240 | 0.674487 | 0.317865 | 0.185018 | 0.320758 | 0.44307 | 0.60108 | 0.823314 | 1.29407 | 2.68217 |
| tossup | r_norm | 1240 | 1.21868 | 0.337639 | 0.431125 | 0.734569 | 0.969381 | 1.18739 | 1.42404 | 1.82465 | 2.74943 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 0.631388 | 0.281286 | -0.14017 | 0.172397 | 0.441468 | 0.636098 | 0.826774 | 1.0958 | 1.41799 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 0.643315 | 0.270522 | -0.303502 | 0.188951 | 0.456871 | 0.649742 | 0.848806 | 1.06527 | 1.45943 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 0.63663 | 0.28212 | -0.448346 | 0.181112 | 0.435501 | 0.626468 | 0.83248 | 1.09518 | 1.68178 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.758712 | 0.521955 | -3.21543 | -1.64604 | -1.0783 | -0.750457 | -0.393663 | 0.0527727 | 0.497285 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.747068 | 0.512923 | -3.24704 | -1.60669 | -1.08086 | -0.70964 | -0.386695 | 0.0409862 | 0.430121 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.817058 | 0.598078 | -3.60122 | -1.75033 | -1.21495 | -0.805791 | -0.383974 | 0.118553 | 0.982753 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 1.3901 | 0.407194 | 0.681585 | 0.910305 | 1.07833 | 1.30132 | 1.61367 | 2.13066 | 3.79897 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.39038 | 0.443558 | 0.658133 | 0.908206 | 1.05715 | 1.28254 | 1.6134 | 2.28391 | 3.98291 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.45369 | 0.493197 | 0.671355 | 0.906081 | 1.05241 | 1.33999 | 1.75675 | 2.33719 | 4.11469 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.245671 | 0.0643896 | 0.0775866 | 0.149118 | 0.20581 | 0.244831 | 0.278447 | 0.341011 | 0.664283 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.305737 | 0.0586868 | 0.0960004 | 0.196473 | 0.274199 | 0.315318 | 0.341868 | 0.381446 | 0.542629 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.448592 | 0.104717 | 0.122311 | 0.306226 | 0.381559 | 0.432054 | 0.510151 | 0.637849 | 0.820186 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.245992 | 0.0673982 | 0.0757863 | 0.138237 | 0.206475 | 0.250121 | 0.28012 | 0.336785 | 0.747486 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.304651 | 0.0596826 | 0.0697899 | 0.181907 | 0.275278 | 0.315307 | 0.341493 | 0.381452 | 0.556461 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.449357 | 0.106971 | 0.0987638 | 0.300504 | 0.3825 | 0.429563 | 0.50444 | 0.658686 | 0.854424 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.247544 | 0.0732663 | 0.0533388 | 0.136574 | 0.201455 | 0.250081 | 0.282333 | 0.36439 | 0.644991 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.303534 | 0.0598007 | 0.110536 | 0.191521 | 0.268967 | 0.315963 | 0.340557 | 0.387944 | 0.534078 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.448923 | 0.11297 | 0.0736319 | 0.291066 | 0.374834 | 0.426593 | 0.512431 | 0.662857 | 0.809668 |
| tossup_hazard | hazard_r_1 | 1240 | 1.43287 | 0.773951 | 0.225532 | 0.53322 | 0.872116 | 1.20699 | 1.81575 | 2.96881 | 5.24142 |
| tossup_hazard | hazard_r_2 | 1240 | 1.38243 | 0.747211 | 0.255001 | 0.524551 | 0.849874 | 1.18841 | 1.73249 | 2.9943 | 4.9268 |
| tossup_hazard | hazard_r_3 | 1240 | 1.40156 | 0.696675 | 0.1888 | 0.465806 | 0.870117 | 1.28333 | 1.82189 | 2.75183 | 4.77067 |
