# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-10000-steps/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-10000-steps/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 304232 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.629115 |
| log_loss | 0.63125 |
| ece | 0.192637 |
| brier | 0.218613 |
| accuracy | 0.66638 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0988704 |
| probability_std | 0.170399 |
| probability_p10 | 0.329714 |
| probability_p50 | 0.596104 |
| probability_p90 | 0.7744 |
| mean_predictive_variance | 0.215689 |
| integrated_brier_score | 0.098032 |
| joint_tossup_event_log_loss | 6.8354 |
| buzz_position_mae | 0.142068 |
| buzz_position_median_absolute_error | 0.116013 |
| buzz_position_bias | -0.00234295 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.368908 |
| first_buzzer_mean_reciprocal_rank | 0.579109 |
| first_buzzer_log_loss | 1.68521 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.629115 |
| neg_average_precision | 0.324649 |
| neg_precision | 0.33723 |
| neg_recall | 0.436297 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.143843 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0490115 |
| no_buzz_calibration_error | 0.0357418 |
| no_buzz_brier | 0.0185262 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.629115 | 0.63125 | 0.192637 | 0.218613 | 0.66638 | 0.76525 | -0.0988704 | 0.170399 | 0.329714 | 0.596104 | 0.7744 | 0.215689 |
| tossup_correctness | tier | fall | 2933 | 0.629788 | 0.628551 | 0.217319 | 0.21682 | 0.673713 | 0.791681 | -0.117968 | 0.175344 | 0.315382 | 0.603492 | 0.777675 | 0.213725 |
| tossup_correctness | tier | nationals | 1584 | 0.622818 | 0.612601 | 0.124993 | 0.211455 | 0.670455 | 0.724747 | -0.0542929 | 0.153316 | 0.385188 | 0.62186 | 0.782948 | 0.215955 |
| tossup_correctness | tier | regionals | 1886 | 0.647748 | 0.631175 | 0.183125 | 0.219893 | 0.653765 | 0.746023 | -0.0922587 | 0.177874 | 0.314572 | 0.579907 | 0.789076 | 0.214405 |
| tossup_correctness | tier | winter | 2892 | 0.628027 | 0.644249 | 0.212395 | 0.223518 | 0.664938 | 0.773167 | -0.10823 | 0.167134 | 0.3263 | 0.584934 | 0.75891 | 0.218373 |
| tossup_correctness | category | Current Events | 124 | 0.594173 | 0.69291 | 0.231798 | 0.243464 | 0.612903 | 0.75 | -0.137097 | 0.17617 | 0.305239 | 0.545331 | 0.732496 | 0.217672 |
| tossup_correctness | category | Fine Arts | 1103 | 0.618409 | 0.631545 | 0.183334 | 0.218187 | 0.672711 | 0.759746 | -0.0870354 | 0.170631 | 0.334742 | 0.598304 | 0.773917 | 0.214842 |
| tossup_correctness | category | Geography | 197 | 0.635315 | 0.684776 | 0.172065 | 0.244832 | 0.598985 | 0.670051 | -0.071066 | 0.179648 | 0.256642 | 0.507307 | 0.736498 | 0.217723 |
| tossup_correctness | category | History | 1491 | 0.659653 | 0.589749 | 0.192038 | 0.200049 | 0.709591 | 0.787391 | -0.0778001 | 0.165329 | 0.364333 | 0.624742 | 0.785748 | 0.213574 |
| tossup_correctness | category | Literature | 1472 | 0.579192 | 0.605686 | 0.192671 | 0.206232 | 0.70856 | 0.804348 | -0.095788 | 0.155629 | 0.400205 | 0.639984 | 0.779993 | 0.213128 |
| tossup_correctness | category | Mythology | 332 | 0.589307 | 0.627724 | 0.223579 | 0.21572 | 0.680723 | 0.813253 | -0.13253 | 0.166778 | 0.350296 | 0.623223 | 0.770674 | 0.214144 |
| tossup_correctness | category | Other Academic | 69 | 0.570136 | 0.640456 | 0.196135 | 0.224053 | 0.666667 | 0.753623 | -0.0869565 | 0.161622 | 0.322535 | 0.60955 | 0.741288 | 0.218377 |
| tossup_correctness | category | Philosophy | 324 | 0.604633 | 0.587647 | 0.176629 | 0.19895 | 0.716049 | 0.799383 | -0.0833333 | 0.158135 | 0.407663 | 0.649154 | 0.800105 | 0.209925 |
| tossup_correctness | category | Popular Culture | 102 | 0.524567 | 0.815367 | 0.35902 | 0.297646 | 0.5 | 0.833333 | -0.333333 | 0.184705 | 0.222997 | 0.482652 | 0.703935 | 0.215224 |
| tossup_correctness | category | Religion | 372 | 0.641309 | 0.644345 | 0.131963 | 0.224002 | 0.663978 | 0.709677 | -0.0456989 | 0.166791 | 0.329788 | 0.602365 | 0.783052 | 0.216141 |
| tossup_correctness | category | Science | 1487 | 0.611323 | 0.677079 | 0.223215 | 0.239464 | 0.605918 | 0.752522 | -0.146604 | 0.160746 | 0.307683 | 0.547419 | 0.725216 | 0.223302 |
| tossup_correctness | category | Social Science | 336 | 0.667881 | 0.643144 | 0.159562 | 0.223383 | 0.657738 | 0.702381 | -0.0446429 | 0.176973 | 0.274079 | 0.563239 | 0.755348 | 0.216847 |
| tossup_correctness | category | Unknown | 1886 | 0.647748 | 0.631175 | 0.183125 | 0.219893 | 0.653765 | 0.746023 | -0.0922587 | 0.177874 | 0.314572 | 0.579907 | 0.789076 | 0.214405 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.659814 | 0.714617 | 0.264338 | 0.255374 | 0.568528 | 0.736041 | -0.167513 | 0.165068 | 0.220959 | 0.490031 | 0.667395 | 0.221952 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.616565 | 0.700236 | 0.231629 | 0.249841 | 0.592893 | 0.735025 | -0.142132 | 0.165169 | 0.268092 | 0.523301 | 0.706862 | 0.222708 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.62092 | 0.652514 | 0.216922 | 0.227846 | 0.642825 | 0.769436 | -0.12661 | 0.167722 | 0.319605 | 0.575137 | 0.752135 | 0.219112 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.638098 | 0.618836 | 0.203587 | 0.212908 | 0.681438 | 0.78402 | -0.102582 | 0.170062 | 0.334291 | 0.60971 | 0.779365 | 0.214609 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.6319 | 0.598986 | 0.146886 | 0.204451 | 0.700267 | 0.756008 | -0.055741 | 0.16291 | 0.37457 | 0.641603 | 0.796229 | 0.211431 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | 0.0608615 | 0.84795 | -3.03757 | -1.22975 | -0.324288 | -0.0492818 | 0.334736 | 1.79803 | 3.91436 |
| player | theta_2 | 1186 | -0.0640081 | 1.03184 | -3.30133 | -1.65833 | -0.609992 | -0.141573 | 0.389716 | 1.8605 | 4.75098 |
| player | theta_3 | 1186 | 1.09863 | 1.3667 | -3.54063 | -1.27993 | 0.066256 | 1.33764 | 2.1769 | 2.9631 | 3.85315 |
| player | theta_norm | 1186 | 1.97499 | 0.981604 | 0.130858 | 0.47582 | 1.20642 | 1.92836 | 2.64913 | 3.68175 | 5.33453 |
| tossup | start_difficulty_d1 | 1240 | 1.26557 | 0.746859 | -0.911389 | -0.273379 | 0.815178 | 1.43295 | 1.79137 | 2.2656 | 2.70634 |
| tossup | start_difficulty_d2 | 1240 | 0.409429 | 0.527755 | -1.55338 | -0.444413 | 0.119087 | 0.366203 | 0.691785 | 1.34219 | 3.32155 |
| tossup | start_difficulty_d3 | 1240 | 1.5509 | 1.13401 | -1.06683 | 0.0168337 | 0.517578 | 1.26742 | 2.64798 | 3.12185 | 3.84632 |
| tossup | end_difficulty_d1 | 1240 | 0.138462 | 0.600179 | -1.95885 | -1.18496 | -0.12652 | 0.334486 | 0.534187 | 0.810469 | 1.32254 |
| tossup | end_difficulty_d2 | 1240 | -0.533509 | 0.620071 | -4.3957 | -1.50352 | -0.861585 | -0.56983 | -0.210148 | 0.50834 | 2.65357 |
| tossup | end_difficulty_d3 | 1240 | 0.286284 | 0.807542 | -2.69269 | -0.964098 | -0.398562 | 0.303895 | 1.02199 | 1.40582 | 2.3391 |
| tossup | total_drop_d1 | 1240 | 1.12711 | 0.343293 | 0.446161 | 0.764558 | 0.876957 | 1.01033 | 1.32933 | 1.77357 | 3.20342 |
| tossup | total_drop_d2 | 1240 | 0.942938 | 0.180251 | 0.65119 | 0.783885 | 0.88597 | 0.933356 | 0.982957 | 1.07372 | 4.45553 |
| tossup | total_drop_d3 | 1240 | 1.26461 | 0.52027 | 0.637099 | 0.765629 | 0.876676 | 0.990332 | 1.60663 | 2.25454 | 3.42401 |
| tossup | drop_share_1_d1 | 1240 | 0.20402 | 0.0821176 | 0.0451038 | 0.0882996 | 0.124891 | 0.204647 | 0.280333 | 0.306174 | 0.528568 |
| tossup | drop_share_2_d1 | 1240 | 0.268788 | 0.096901 | 0.0667073 | 0.114883 | 0.176688 | 0.314606 | 0.343595 | 0.367484 | 0.684911 |
| tossup | drop_share_3_d1 | 1240 | 0.527192 | 0.165667 | 0.147135 | 0.349198 | 0.376422 | 0.470372 | 0.689528 | 0.787769 | 0.875833 |
| tossup | drop_share_1_d2 | 1240 | 0.288392 | 0.0240191 | 0.10598 | 0.241322 | 0.28114 | 0.293038 | 0.302181 | 0.31548 | 0.330802 |
| tossup | drop_share_2_d2 | 1240 | 0.34303 | 0.0148516 | 0.220848 | 0.321447 | 0.336261 | 0.344557 | 0.351875 | 0.362637 | 0.379718 |
| tossup | drop_share_3_d2 | 1240 | 0.368578 | 0.0321978 | 0.317017 | 0.339464 | 0.351842 | 0.36147 | 0.374897 | 0.426449 | 0.673171 |
| tossup | drop_share_1_d3 | 1240 | 0.23453 | 0.0939563 | 0.0352986 | 0.0777918 | 0.147409 | 0.274383 | 0.294799 | 0.322172 | 0.679467 |
| tossup | drop_share_2_d3 | 1240 | 0.298315 | 0.102216 | 0.044778 | 0.106762 | 0.232153 | 0.33426 | 0.348613 | 0.439689 | 0.772533 |
| tossup | drop_share_3_d3 | 1240 | 0.467155 | 0.165815 | 0.0821319 | 0.318601 | 0.359716 | 0.382156 | 0.577234 | 0.802231 | 0.919544 |
| tossup | r_1 | 1240 | 0.377505 | 0.308528 | 0.0140524 | 0.0237605 | 0.0521228 | 0.448132 | 0.644177 | 0.85934 | 0.934505 |
| tossup | r_2 | 1240 | 0.138989 | 0.129845 | 0.0149296 | 0.0228853 | 0.0457376 | 0.0858743 | 0.179247 | 0.443937 | 0.568815 |
| tossup | r_3 | 1240 | 0.483506 | 0.354244 | 0.0270071 | 0.0495388 | 0.122215 | 0.38899 | 0.871698 | 0.937534 | 0.965722 |
| tossup | r_norm | 1240 | 0.78847 | 0.106194 | 0.58848 | 0.632791 | 0.683934 | 0.791805 | 0.890234 | 0.93873 | 0.966026 |
