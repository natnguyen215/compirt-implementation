# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating-10000-steps/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating-10000-steps/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 308497 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.626346 |
| log_loss | 0.658207 |
| ece | 0.218973 |
| brier | 0.230699 |
| accuracy | 0.632383 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.132867 |
| probability_std | 0.175539 |
| probability_p10 | 0.298277 |
| probability_p50 | 0.567258 |
| probability_p90 | 0.762426 |
| mean_predictive_variance | 0.217044 |
| integrated_brier_score | 0.0955285 |
| joint_tossup_event_log_loss | 6.77488 |
| buzz_position_mae | 0.139664 |
| buzz_position_median_absolute_error | 0.115638 |
| buzz_position_bias | 0.000369254 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.367509 |
| first_buzzer_mean_reciprocal_rank | 0.576757 |
| first_buzzer_log_loss | 1.65727 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.626346 |
| neg_average_precision | 0.324931 |
| neg_precision | 0.318756 |
| neg_recall | 0.497709 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.141272 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0509311 |
| no_buzz_calibration_error | 0.0376614 |
| no_buzz_brier | 0.0195103 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.626346 | 0.658207 | 0.218973 | 0.230699 | 0.632383 | 0.76525 | -0.132867 | 0.175539 | 0.298277 | 0.567258 | 0.762426 | 0.217044 |
| tossup_correctness | tier | fall | 2933 | 0.620791 | 0.672269 | 0.253991 | 0.236157 | 0.620525 | 0.791681 | -0.171156 | 0.179859 | 0.275835 | 0.559239 | 0.754576 | 0.21623 |
| tossup_correctness | tier | nationals | 1584 | 0.594576 | 0.693016 | 0.211501 | 0.247964 | 0.581439 | 0.724747 | -0.143308 | 0.159854 | 0.29723 | 0.526205 | 0.715141 | 0.224259 |
| tossup_correctness | tier | regionals | 1886 | 0.646163 | 0.631129 | 0.173057 | 0.217878 | 0.662248 | 0.746023 | -0.0837752 | 0.178616 | 0.31976 | 0.60085 | 0.782135 | 0.212772 |
| tossup_correctness | tier | winter | 2892 | 0.63776 | 0.642538 | 0.217747 | 0.224069 | 0.652835 | 0.773167 | -0.120332 | 0.173849 | 0.308296 | 0.577313 | 0.766781 | 0.216705 |
| tossup_correctness | category | Current Events | 124 | 0.599376 | 0.761663 | 0.290509 | 0.2767 | 0.516129 | 0.75 | -0.233871 | 0.164713 | 0.270951 | 0.466407 | 0.670387 | 0.221426 |
| tossup_correctness | category | Fine Arts | 1103 | 0.620381 | 0.654026 | 0.2027 | 0.228622 | 0.649139 | 0.759746 | -0.110607 | 0.176653 | 0.296671 | 0.579202 | 0.773437 | 0.215539 |
| tossup_correctness | category | Geography | 197 | 0.570396 | 0.763921 | 0.237653 | 0.27897 | 0.497462 | 0.670051 | -0.172589 | 0.173146 | 0.2316 | 0.453096 | 0.685827 | 0.217826 |
| tossup_correctness | category | History | 1491 | 0.644014 | 0.681035 | 0.277685 | 0.242384 | 0.603622 | 0.787391 | -0.183769 | 0.159542 | 0.300012 | 0.515173 | 0.712956 | 0.224452 |
| tossup_correctness | category | Literature | 1472 | 0.610224 | 0.614187 | 0.212742 | 0.210707 | 0.681386 | 0.804348 | -0.122962 | 0.170751 | 0.344833 | 0.616416 | 0.789836 | 0.212452 |
| tossup_correctness | category | Mythology | 332 | 0.597611 | 0.682617 | 0.275213 | 0.24127 | 0.605422 | 0.813253 | -0.207831 | 0.177105 | 0.270542 | 0.56626 | 0.755569 | 0.217187 |
| tossup_correctness | category | Other Academic | 69 | 0.514706 | 0.725476 | 0.281241 | 0.264629 | 0.521739 | 0.753623 | -0.231884 | 0.157892 | 0.251663 | 0.501569 | 0.684929 | 0.225045 |
| tossup_correctness | category | Philosophy | 324 | 0.58117 | 0.621699 | 0.205424 | 0.215404 | 0.660494 | 0.799383 | -0.138889 | 0.165558 | 0.375372 | 0.620509 | 0.786907 | 0.213696 |
| tossup_correctness | category | Popular Culture | 102 | 0.494118 | 0.877343 | 0.38537 | 0.324496 | 0.460784 | 0.833333 | -0.372549 | 0.187721 | 0.195712 | 0.472487 | 0.683304 | 0.212053 |
| tossup_correctness | category | Religion | 372 | 0.627841 | 0.682418 | 0.187343 | 0.241487 | 0.629032 | 0.709677 | -0.0806452 | 0.168008 | 0.280775 | 0.53649 | 0.736658 | 0.221275 |
| tossup_correctness | category | Science | 1487 | 0.642436 | 0.666744 | 0.221625 | 0.234075 | 0.613988 | 0.752522 | -0.138534 | 0.173488 | 0.289594 | 0.545306 | 0.747746 | 0.218947 |
| tossup_correctness | category | Social Science | 336 | 0.634576 | 0.681464 | 0.195102 | 0.241915 | 0.604167 | 0.702381 | -0.0982143 | 0.17016 | 0.265833 | 0.514889 | 0.724661 | 0.220993 |
| tossup_correctness | category | Unknown | 1886 | 0.646163 | 0.631129 | 0.173057 | 0.217878 | 0.662248 | 0.746023 | -0.0837752 | 0.178616 | 0.31976 | 0.60085 | 0.782135 | 0.212772 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.647082 | 0.75986 | 0.294563 | 0.2752 | 0.527919 | 0.736041 | -0.208122 | 0.17045 | 0.20508 | 0.450973 | 0.662611 | 0.217522 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.616318 | 0.730717 | 0.254432 | 0.262394 | 0.560406 | 0.735025 | -0.174619 | 0.171825 | 0.232083 | 0.494302 | 0.695135 | 0.2201 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.612174 | 0.679168 | 0.23765 | 0.239407 | 0.611284 | 0.769436 | -0.158152 | 0.173217 | 0.28838 | 0.553181 | 0.741334 | 0.218985 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.633303 | 0.646032 | 0.230037 | 0.225563 | 0.640963 | 0.78402 | -0.143057 | 0.175409 | 0.304627 | 0.577345 | 0.768941 | 0.216318 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.633648 | 0.623581 | 0.177729 | 0.215723 | 0.670561 | 0.756008 | -0.0854473 | 0.169194 | 0.342704 | 0.597196 | 0.78211 | 0.215246 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | 0.622788 | 1.13305 | -2.22636 | -1.13679 | -0.169243 | 0.430575 | 1.43308 | 2.59226 | 3.57858 |
| player | theta_2 | 1186 | -0.0511466 | 0.734249 | -2.7218 | -1.18838 | -0.424297 | -0.110979 | 0.274568 | 1.21742 | 3.73976 |
| player | theta_3 | 1186 | 0.552006 | 1.31736 | -3.1751 | -1.32235 | -0.477726 | 0.361249 | 1.70207 | 2.70586 | 4.15948 |
| player | theta_norm | 1186 | 1.8469 | 0.91663 | 0.0515409 | 0.488157 | 1.11167 | 1.77256 | 2.52939 | 3.40622 | 4.90403 |
| tossup | start_difficulty_d1 | 1240 | 1.78068 | 0.662414 | -0.75829 | 0.459242 | 1.52684 | 1.92872 | 2.19435 | 2.61785 | 3.4841 |
| tossup | start_difficulty_d2 | 1240 | 0.877072 | 0.789921 | -1.52226 | -0.627421 | 0.375733 | 0.964813 | 1.48197 | 1.99285 | 2.41569 |
| tossup | start_difficulty_d3 | 1240 | 1.18049 | 0.97514 | -1.7876 | -0.204517 | 0.450019 | 1.02182 | 1.89691 | 2.82094 | 3.96627 |
| tossup | end_difficulty_d1 | 1240 | 0.567151 | 0.560063 | -1.89751 | -0.548819 | 0.374367 | 0.639709 | 0.855893 | 1.3492 | 2.74106 |
| tossup | end_difficulty_d2 | 1240 | -0.254019 | 0.807381 | -3.98428 | -1.83593 | -0.714512 | -0.136975 | 0.275733 | 0.91095 | 1.65701 |
| tossup | end_difficulty_d3 | 1240 | 0.113443 | 0.832493 | -2.8273 | -1.26575 | -0.486204 | 0.12525 | 0.793857 | 1.34594 | 2.36737 |
| tossup | total_drop_d1 | 1240 | 1.21353 | 0.400683 | 0.502165 | 0.726937 | 0.864624 | 1.1526 | 1.47832 | 1.92038 | 2.80348 |
| tossup | total_drop_d2 | 1240 | 1.13109 | 0.49559 | 0.528776 | 0.731541 | 0.844342 | 0.933823 | 1.21929 | 2.20141 | 4.1868 |
| tossup | total_drop_d3 | 1240 | 1.06705 | 0.441598 | 0.617538 | 0.733409 | 0.822928 | 0.909817 | 1.04891 | 2.03245 | 3.75048 |
| tossup | drop_share_1_d1 | 1240 | 0.194104 | 0.0830412 | 0.0407013 | 0.0865188 | 0.124791 | 0.183691 | 0.262106 | 0.308367 | 0.596303 |
| tossup | drop_share_2_d1 | 1240 | 0.262232 | 0.0958353 | 0.0440288 | 0.107541 | 0.182968 | 0.276489 | 0.334236 | 0.388106 | 0.664341 |
| tossup | drop_share_3_d1 | 1240 | 0.543664 | 0.154725 | 0.116544 | 0.346567 | 0.403368 | 0.529624 | 0.680603 | 0.795239 | 0.913395 |
| tossup | drop_share_1_d2 | 1240 | 0.237802 | 0.0718957 | 0.0392781 | 0.0982248 | 0.187538 | 0.271129 | 0.289709 | 0.309428 | 0.349797 |
| tossup | drop_share_2_d2 | 1240 | 0.301074 | 0.0740456 | 0.0640787 | 0.134176 | 0.288618 | 0.334389 | 0.345764 | 0.359381 | 0.55785 |
| tossup | drop_share_3_d2 | 1240 | 0.461124 | 0.14157 | 0.23097 | 0.347121 | 0.368491 | 0.388537 | 0.519991 | 0.761026 | 0.892728 |
| tossup | drop_share_1_d3 | 1240 | 0.257576 | 0.070917 | 0.0385778 | 0.093681 | 0.252156 | 0.279528 | 0.294317 | 0.315112 | 0.6553 |
| tossup | drop_share_2_d3 | 1240 | 0.321799 | 0.0742218 | 0.0510577 | 0.143239 | 0.324376 | 0.337023 | 0.347874 | 0.372955 | 0.698641 |
| tossup | drop_share_3_d3 | 1240 | 0.420625 | 0.121004 | 0.106323 | 0.337467 | 0.362066 | 0.379743 | 0.410359 | 0.744511 | 0.896234 |
| tossup | r_1 | 1240 | 0.522244 | 0.30199 | 0.0149991 | 0.0333841 | 0.235471 | 0.606221 | 0.794949 | 0.895911 | 0.945772 |
| tossup | r_2 | 1240 | 0.196197 | 0.190068 | 0.0140648 | 0.0305745 | 0.0616769 | 0.112511 | 0.2699 | 0.609387 | 0.897981 |
| tossup | r_3 | 1240 | 0.28156 | 0.296766 | 0.0221779 | 0.0362883 | 0.0655514 | 0.138673 | 0.358633 | 0.898711 | 0.965034 |
| tossup | r_norm | 1240 | 0.77217 | 0.0974088 | 0.577398 | 0.612218 | 0.690982 | 0.775741 | 0.855949 | 0.92082 | 0.965362 |
