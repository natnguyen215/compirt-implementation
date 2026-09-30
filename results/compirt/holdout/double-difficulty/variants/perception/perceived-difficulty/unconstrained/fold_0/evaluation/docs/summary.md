# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/unconstrained/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/unconstrained/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 338771 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.668761 |
| log_loss | 0.514791 |
| ece | 0.0301573 |
| brier | 0.16863 |
| accuracy | 0.767509 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00225928 |
| probability_std | 0.132465 |
| probability_p10 | 0.551232 |
| probability_p50 | 0.763973 |
| probability_p90 | 0.888255 |
| mean_predictive_variance | 0.17581 |
| integrated_brier_score | 0.171009 |
| joint_tossup_event_log_loss | 7.68831 |
| buzz_position_mae | 0.329093 |
| buzz_position_median_absolute_error | 0.331221 |
| buzz_position_bias | -0.314085 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.347283 |
| first_buzzer_mean_reciprocal_rank | 0.562402 |
| first_buzzer_log_loss | 1.69637 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.668761 |
| neg_average_precision | 0.385086 |
| neg_precision | 0.519196 |
| neg_recall | 0.130156 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0315866 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.222867 |
| no_buzz_calibration_error | 0.209597 |
| no_buzz_brier | 0.0674402 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.668761 | 0.514791 | 0.0301573 | 0.16863 | 0.767509 | 0.76525 | 0.00225928 | 0.132465 | 0.551232 | 0.763973 | 0.888255 | 0.17581 |
| tossup_correctness | tier | fall | 2933 | 0.669619 | 0.481379 | 0.00944489 | 0.154399 | 0.793727 | 0.791681 | 0.00204569 | 0.1094 | 0.637435 | 0.807068 | 0.905199 | 0.156511 |
| tossup_correctness | tier | nationals | 1584 | 0.682909 | 0.576175 | 0.11636 | 0.195093 | 0.718434 | 0.724747 | -0.00631313 | 0.14287 | 0.413394 | 0.622188 | 0.796089 | 0.216666 |
| tossup_correctness | tier | regionals | 1886 | 0.651772 | 0.541113 | 0.0381255 | 0.179743 | 0.752386 | 0.746023 | 0.00636267 | 0.112147 | 0.551875 | 0.721462 | 0.842345 | 0.193945 |
| tossup_correctness | tier | winter | 2892 | 0.681907 | 0.497891 | 0.0183689 | 0.161322 | 0.777663 | 0.773167 | 0.00449516 | 0.109651 | 0.628524 | 0.799687 | 0.897327 | 0.161178 |
| tossup_correctness | category | Current Events | 124 | 0.637183 | 0.547681 | 0.0972273 | 0.182286 | 0.741935 | 0.75 | -0.00806452 | 0.12395 | 0.532869 | 0.703624 | 0.847554 | 0.196683 |
| tossup_correctness | category | Fine Arts | 1103 | 0.632238 | 0.534189 | 0.0328162 | 0.17556 | 0.757933 | 0.759746 | -0.00181324 | 0.127386 | 0.56294 | 0.772663 | 0.884443 | 0.174037 |
| tossup_correctness | category | Geography | 197 | 0.707459 | 0.579119 | 0.05753 | 0.198851 | 0.680203 | 0.670051 | 0.0101523 | 0.147102 | 0.500659 | 0.729651 | 0.877269 | 0.188489 |
| tossup_correctness | category | History | 1491 | 0.678333 | 0.489404 | 0.0342713 | 0.158369 | 0.783367 | 0.787391 | -0.00402414 | 0.134836 | 0.557924 | 0.78216 | 0.909295 | 0.16711 |
| tossup_correctness | category | Literature | 1472 | 0.666953 | 0.465839 | 0.0260689 | 0.147466 | 0.80231 | 0.804348 | -0.00203804 | 0.116851 | 0.616521 | 0.813671 | 0.900577 | 0.156133 |
| tossup_correctness | category | Mythology | 332 | 0.703286 | 0.458942 | 0.0703713 | 0.146048 | 0.813253 | 0.813253 | 0 | 0.118552 | 0.571545 | 0.773564 | 0.886013 | 0.174571 |
| tossup_correctness | category | Other Academic | 69 | 0.433258 | 0.638971 | 0.174656 | 0.221972 | 0.710145 | 0.753623 | -0.0434783 | 0.123537 | 0.493955 | 0.662764 | 0.812662 | 0.211921 |
| tossup_correctness | category | Philosophy | 324 | 0.679299 | 0.475361 | 0.0551047 | 0.151787 | 0.799383 | 0.799383 | 0 | 0.127322 | 0.584762 | 0.765815 | 0.889126 | 0.172738 |
| tossup_correctness | category | Popular Culture | 102 | 0.52526 | 0.497586 | 0.0924084 | 0.160223 | 0.803922 | 0.833333 | -0.0294118 | 0.11178 | 0.636748 | 0.746867 | 0.870813 | 0.17738 |
| tossup_correctness | category | Religion | 372 | 0.657934 | 0.573634 | 0.0596876 | 0.195747 | 0.715054 | 0.709677 | 0.00537634 | 0.143478 | 0.502983 | 0.741915 | 0.86782 | 0.184639 |
| tossup_correctness | category | Science | 1487 | 0.687233 | 0.516936 | 0.0318459 | 0.169526 | 0.763954 | 0.752522 | 0.0114324 | 0.153905 | 0.498527 | 0.765949 | 0.896828 | 0.173623 |
| tossup_correctness | category | Social Science | 336 | 0.655127 | 0.578915 | 0.0204954 | 0.19517 | 0.720238 | 0.702381 | 0.0178571 | 0.136071 | 0.514507 | 0.732074 | 0.872584 | 0.185697 |
| tossup_correctness | category | Unknown | 1886 | 0.651772 | 0.541113 | 0.0381255 | 0.179743 | 0.752386 | 0.746023 | 0.00636267 | 0.112147 | 0.551875 | 0.721462 | 0.842345 | 0.193945 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.629045 | 0.572469 | 0.083614 | 0.189963 | 0.730964 | 0.736041 | -0.00507614 | 0.130374 | 0.542767 | 0.73061 | 0.868959 | 0.188818 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.656929 | 0.550996 | 0.0230875 | 0.18413 | 0.73198 | 0.735025 | -0.00304569 | 0.133398 | 0.532768 | 0.750821 | 0.874216 | 0.181526 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.668022 | 0.510393 | 0.0261981 | 0.166841 | 0.768992 | 0.769436 | -0.000444247 | 0.125347 | 0.567322 | 0.770698 | 0.883176 | 0.173927 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.672388 | 0.494584 | 0.0414886 | 0.160406 | 0.784717 | 0.78402 | 0.000697837 | 0.130761 | 0.561334 | 0.768528 | 0.889901 | 0.173611 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.671849 | 0.52173 | 0.0290707 | 0.171344 | 0.764019 | 0.756008 | 0.00801068 | 0.138226 | 0.536412 | 0.758764 | 0.893137 | 0.176593 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -1.87694 | 0.739783 | -4.30223 | -3.04771 | -2.41593 | -1.93272 | -1.3389 | -0.617358 | -0.141932 |
| player | theta_2 | 1186 | -1.48559 | 0.740474 | -4.04809 | -2.76618 | -2.0321 | -1.41541 | -0.884604 | -0.367309 | 0.032637 |
| player | theta_3 | 1186 | -1.11007 | 0.918082 | -3.52949 | -2.88068 | -1.82554 | -0.734872 | -0.361936 | -0.118634 | 0.261246 |
| player | alpha_1 | 1186 | -0.770906 | 0.72927 | -2.88416 | -2.0976 | -1.2105 | -0.749041 | -0.252473 | 0.365486 | 1.31167 |
| player | alpha_2 | 1186 | -0.350704 | 0.901171 | -2.7722 | -1.66219 | -0.9441 | -0.439668 | 0.164917 | 1.31648 | 2.80374 |
| player | alpha_3 | 1186 | 0.142069 | 1.04242 | -3.00475 | -1.76269 | -0.562883 | 0.225831 | 0.898415 | 1.67038 | 3.08244 |
| player | beta_1 | 1186 | -2.11386 | 1.05431 | -5.40472 | -4.07996 | -2.75443 | -1.99752 | -1.3559 | -0.547258 | -0.171165 |
| player | beta_2 | 1186 | -1.61811 | 0.851785 | -4.57233 | -3.08891 | -2.21112 | -1.57122 | -0.920615 | -0.389241 | -0.127316 |
| player | beta_3 | 1186 | -1.3493 | 1.30537 | -5.55721 | -4.20219 | -1.97035 | -0.783067 | -0.357018 | -0.136245 | 0.184479 |
| player | theta_norm | 1186 | 2.84922 | 0.884076 | 0.905666 | 1.40571 | 2.18809 | 2.80798 | 3.46583 | 4.35453 | 5.23576 |
| tossup | start_difficulty_d1 | 1240 | -2.24095 | 1.02499 | -4.83097 | -3.84994 | -2.98152 | -2.29276 | -1.56641 | -0.366252 | 0.489695 |
| tossup | start_difficulty_d2 | 1240 | -1.06266 | 1.35286 | -4.6861 | -3.80968 | -1.76116 | -0.494306 | -0.0674713 | 0.274276 | 0.989519 |
| tossup | start_difficulty_d3 | 1240 | -0.988168 | 1.12615 | -4.02069 | -2.78357 | -1.98038 | -0.92214 | 0.0609303 | 0.482536 | 1.07684 |
| tossup | end_difficulty_d1 | 1240 | -3.12931 | 1.00079 | -6.43529 | -4.5646 | -3.86727 | -3.25793 | -2.52153 | -1.21924 | -0.332649 |
| tossup | end_difficulty_d2 | 1240 | -2.10454 | 1.33579 | -7.21141 | -4.52706 | -3.24859 | -1.55323 | -1.03668 | -0.631399 | 0.272081 |
| tossup | end_difficulty_d3 | 1240 | -2.11281 | 1.258 | -8.1657 | -4.16615 | -3.09044 | -2.00688 | -1.01723 | -0.470493 | 0.118293 |
| tossup | total_drop_d1 | 1240 | 0.888361 | 0.367358 | 0.304637 | 0.427545 | 0.663005 | 0.85315 | 1.0232 | 1.51609 | 4.41562 |
| tossup | total_drop_d2 | 1240 | 1.04188 | 0.561956 | 0.3179 | 0.44969 | 0.879608 | 0.967137 | 1.0941 | 1.88868 | 6.94039 |
| tossup | total_drop_d3 | 1240 | 1.12464 | 0.536924 | 0.580989 | 0.767339 | 0.901232 | 0.997612 | 1.14655 | 1.90105 | 6.76006 |
| tossup | drop_share_1_d1 | 1240 | 0.339956 | 0.0290506 | 0.232613 | 0.298341 | 0.320161 | 0.335903 | 0.357335 | 0.390593 | 0.460061 |
| tossup | drop_share_2_d1 | 1240 | 0.32826 | 0.0186781 | 0.270042 | 0.294801 | 0.316238 | 0.330505 | 0.341129 | 0.354395 | 0.401528 |
| tossup | drop_share_3_d1 | 1240 | 0.331784 | 0.0275951 | 0.237934 | 0.287792 | 0.314396 | 0.33095 | 0.348635 | 0.377694 | 0.461106 |
| tossup | drop_share_1_d2 | 1240 | 0.3139 | 0.0298509 | 0.13237 | 0.276569 | 0.301355 | 0.310302 | 0.321701 | 0.375422 | 0.462522 |
| tossup | drop_share_2_d2 | 1240 | 0.339484 | 0.0223105 | 0.262808 | 0.29365 | 0.331786 | 0.343598 | 0.352614 | 0.369325 | 0.430576 |
| tossup | drop_share_3_d2 | 1240 | 0.346615 | 0.0287265 | 0.237434 | 0.302881 | 0.334047 | 0.345814 | 0.355973 | 0.400504 | 0.593529 |
| tossup | drop_share_1_d3 | 1240 | 0.321147 | 0.0297859 | 0.158095 | 0.282953 | 0.301594 | 0.317232 | 0.339551 | 0.370589 | 0.435685 |
| tossup | drop_share_2_d3 | 1240 | 0.344396 | 0.016904 | 0.303381 | 0.320259 | 0.33399 | 0.343401 | 0.352295 | 0.368691 | 0.500693 |
| tossup | drop_share_3_d3 | 1240 | 0.334457 | 0.0243435 | 0.224134 | 0.291683 | 0.319627 | 0.338928 | 0.350924 | 0.364368 | 0.512282 |
| tossup | r_1 | 1240 | 0.507969 | 0.277028 | 0.0354707 | 0.0730474 | 0.216433 | 0.557692 | 0.763177 | 0.85862 | 0.943664 |
| tossup | r_2 | 1240 | 0.253262 | 0.282688 | 0.029935 | 0.0489128 | 0.0711913 | 0.11182 | 0.238946 | 0.836 | 0.934385 |
| tossup | r_3 | 1240 | 0.238769 | 0.200936 | 0.0172719 | 0.036165 | 0.0716333 | 0.158445 | 0.365349 | 0.648354 | 0.825015 |
| tossup | r_norm | 1240 | 0.754725 | 0.0803306 | 0.581557 | 0.62595 | 0.684064 | 0.759487 | 0.817694 | 0.879708 | 0.944515 |
