# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 325817 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.596692 |
| log_loss | 0.737962 |
| ece | 0.290837 |
| brier | 0.266584 |
| accuracy | 0.548759 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.224595 |
| probability_std | 0.162858 |
| probability_p10 | 0.243696 |
| probability_p50 | 0.502624 |
| probability_p90 | 0.683413 |
| mean_predictive_variance | 0.223172 |
| integrated_brier_score | 0.0950349 |
| joint_tossup_event_log_loss | 6.86197 |
| buzz_position_mae | 0.138928 |
| buzz_position_median_absolute_error | 0.116082 |
| buzz_position_bias | -0.000730965 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.364078 |
| first_buzzer_mean_reciprocal_rank | 0.573353 |
| first_buzzer_log_loss | 1.65445 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.596692 |
| neg_average_precision | 0.302474 |
| neg_precision | 0.272807 |
| neg_recall | 0.594955 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.136672 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0497325 |
| no_buzz_calibration_error | 0.0380055 |
| no_buzz_brier | 0.0180489 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.596692 | 0.737962 | 0.290837 | 0.266584 | 0.548759 | 0.773355 | -0.224595 | 0.162858 | 0.243696 | 0.502624 | 0.683413 | 0.223172 |
| tossup_correctness | tier | fall | 2876 | 0.611907 | 0.766134 | 0.330159 | 0.278377 | 0.519124 | 0.793115 | -0.273992 | 0.162341 | 0.223564 | 0.480463 | 0.664715 | 0.222273 |
| tossup_correctness | tier | nationals | 1579 | 0.599611 | 0.671959 | 0.204312 | 0.23899 | 0.59468 | 0.729576 | -0.134896 | 0.137199 | 0.335824 | 0.536241 | 0.69812 | 0.230538 |
| tossup_correctness | tier | regionals | 1990 | 0.611198 | 0.716354 | 0.270914 | 0.256627 | 0.58593 | 0.765829 | -0.179899 | 0.17002 | 0.2419 | 0.52162 | 0.696299 | 0.221067 |
| tossup_correctness | tier | winter | 2825 | 0.590431 | 0.761396 | 0.313203 | 0.277015 | 0.52708 | 0.783009 | -0.255929 | 0.166244 | 0.222331 | 0.490064 | 0.678277 | 0.221451 |
| tossup_correctness | category | Current Events | 123 | 0.66361 | 0.737751 | 0.310065 | 0.267274 | 0.544715 | 0.764228 | -0.219512 | 0.148186 | 0.247628 | 0.465546 | 0.643441 | 0.226058 |
| tossup_correctness | category | Fine Arts | 1093 | 0.59822 | 0.739956 | 0.287253 | 0.267131 | 0.550778 | 0.769442 | -0.218664 | 0.163866 | 0.240313 | 0.502567 | 0.684021 | 0.222831 |
| tossup_correctness | category | Geography | 191 | 0.515408 | 0.812265 | 0.255989 | 0.298863 | 0.486911 | 0.691099 | -0.204188 | 0.161031 | 0.191909 | 0.450703 | 0.624296 | 0.219858 |
| tossup_correctness | category | History | 1469 | 0.611007 | 0.730116 | 0.280228 | 0.263587 | 0.552076 | 0.758339 | -0.206263 | 0.153845 | 0.249872 | 0.499721 | 0.662412 | 0.225852 |
| tossup_correctness | category | Literature | 1436 | 0.59495 | 0.711371 | 0.30659 | 0.253998 | 0.578691 | 0.81546 | -0.236769 | 0.163862 | 0.268541 | 0.533772 | 0.706182 | 0.223071 |
| tossup_correctness | category | Mythology | 325 | 0.445327 | 0.811089 | 0.371423 | 0.300735 | 0.433846 | 0.843077 | -0.409231 | 0.156358 | 0.243904 | 0.481881 | 0.670296 | 0.224749 |
| tossup_correctness | category | Other Academic | 67 | 0.587601 | 0.769163 | 0.325529 | 0.281724 | 0.522388 | 0.791045 | -0.268657 | 0.159305 | 0.230679 | 0.475535 | 0.663949 | 0.223433 |
| tossup_correctness | category | Philosophy | 322 | 0.686888 | 0.665222 | 0.27815 | 0.234435 | 0.636646 | 0.785714 | -0.149068 | 0.163967 | 0.272046 | 0.535597 | 0.709382 | 0.223047 |
| tossup_correctness | category | Popular Culture | 100 | 0.547497 | 0.897748 | 0.472465 | 0.33498 | 0.41 | 0.89 | -0.48 | 0.155745 | 0.237635 | 0.432005 | 0.627287 | 0.220268 |
| tossup_correctness | category | Religion | 365 | 0.615924 | 0.730122 | 0.24977 | 0.263036 | 0.564384 | 0.723288 | -0.158904 | 0.166317 | 0.233932 | 0.490739 | 0.681796 | 0.221637 |
| tossup_correctness | category | Science | 1456 | 0.556257 | 0.783609 | 0.309121 | 0.287222 | 0.492445 | 0.76717 | -0.274725 | 0.154964 | 0.234638 | 0.479114 | 0.65522 | 0.224226 |
| tossup_correctness | category | Social Science | 333 | 0.609488 | 0.721006 | 0.254725 | 0.260835 | 0.516517 | 0.72973 | -0.213213 | 0.163137 | 0.227971 | 0.486349 | 0.674602 | 0.222783 |
| tossup_correctness | category | Unknown | 1990 | 0.611198 | 0.716354 | 0.270914 | 0.256627 | 0.58593 | 0.765829 | -0.179899 | 0.17002 | 0.2419 | 0.52162 | 0.696299 | 0.221067 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.612106 | 0.865443 | 0.371558 | 0.323971 | 0.407821 | 0.748603 | -0.340782 | 0.15027 | 0.169242 | 0.381682 | 0.564302 | 0.212301 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.593646 | 0.818671 | 0.335634 | 0.30206 | 0.454545 | 0.754441 | -0.299896 | 0.15473 | 0.197822 | 0.4328 | 0.609379 | 0.219466 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.623027 | 0.777175 | 0.32089 | 0.28285 | 0.513845 | 0.766682 | -0.252837 | 0.158256 | 0.213448 | 0.462587 | 0.641456 | 0.222017 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.594534 | 0.734055 | 0.301845 | 0.265087 | 0.551041 | 0.787441 | -0.2364 | 0.157436 | 0.255385 | 0.507417 | 0.676697 | 0.225006 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.586609 | 0.678766 | 0.237906 | 0.240983 | 0.611581 | 0.771758 | -0.160176 | 0.157515 | 0.301016 | 0.559301 | 0.718342 | 0.224043 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | 0.306838 | 0.962589 | -1.75866 | -1.23499 | -0.410486 | 0.272607 | 0.999479 | 1.966 | 2.85491 |
| player | theta_2 | 1196 | 0.172588 | 0.865981 | -1.85393 | -1.20266 | -0.521626 | 0.154214 | 0.826337 | 1.61558 | 2.54696 |
| player | theta_3 | 1196 | 0.232427 | 0.88949 | -1.82852 | -1.15795 | -0.461285 | 0.201547 | 0.893502 | 1.72718 | 2.62377 |
| player | theta_norm | 1196 | 1.47367 | 0.68722 | 0.0558597 | 0.462821 | 0.917337 | 1.40186 | 1.97482 | 2.65402 | 3.7034 |
| tossup | start_difficulty_d1 | 1240 | 1.65119 | 0.367741 | -0.0920413 | 1.00651 | 1.45217 | 1.68468 | 1.88963 | 2.16784 | 2.70355 |
| tossup | start_difficulty_d2 | 1240 | 1.56555 | 0.371839 | -0.0252753 | 0.888123 | 1.34618 | 1.59799 | 1.81539 | 2.12021 | 2.49059 |
| tossup | start_difficulty_d3 | 1240 | 1.52486 | 0.355945 | -0.0580206 | 0.834226 | 1.32372 | 1.56093 | 1.77241 | 2.04243 | 2.63315 |
| tossup | end_difficulty_d1 | 1240 | 0.47335 | 0.409862 | -1.54939 | -0.191782 | 0.248564 | 0.49307 | 0.707524 | 1.14135 | 1.87703 |
| tossup | end_difficulty_d2 | 1240 | 0.262152 | 0.434643 | -2.32005 | -0.526473 | 0.0383548 | 0.332634 | 0.556214 | 0.844299 | 1.58678 |
| tossup | end_difficulty_d3 | 1240 | 0.421382 | 0.392167 | -1.32779 | -0.30604 | 0.221084 | 0.471413 | 0.6839 | 0.958395 | 1.36626 |
| tossup | total_drop_d1 | 1240 | 1.17784 | 0.373959 | 0.504257 | 0.736393 | 0.881197 | 1.09645 | 1.41345 | 1.86669 | 3.38837 |
| tossup | total_drop_d2 | 1240 | 1.3034 | 0.480061 | 0.503299 | 0.742311 | 0.929136 | 1.20872 | 1.577 | 2.18789 | 4.4272 |
| tossup | total_drop_d3 | 1240 | 1.10348 | 0.346435 | 0.455183 | 0.72377 | 0.875125 | 1.01815 | 1.25938 | 1.75863 | 2.96139 |
| tossup | drop_share_1_d1 | 1240 | 0.198023 | 0.061074 | 0.0524172 | 0.104381 | 0.150407 | 0.197941 | 0.240117 | 0.293047 | 0.542368 |
| tossup | drop_share_2_d1 | 1240 | 0.270786 | 0.0705301 | 0.0633183 | 0.141581 | 0.226091 | 0.284796 | 0.318914 | 0.360416 | 0.562867 |
| tossup | drop_share_3_d1 | 1240 | 0.531191 | 0.120569 | 0.181015 | 0.370747 | 0.441044 | 0.512107 | 0.616407 | 0.744672 | 0.877954 |
| tossup | drop_share_1_d2 | 1240 | 0.195521 | 0.0658821 | 0.0413347 | 0.0977329 | 0.1416 | 0.191209 | 0.248282 | 0.297667 | 0.553177 |
| tossup | drop_share_2_d2 | 1240 | 0.267317 | 0.071224 | 0.0739698 | 0.136816 | 0.215891 | 0.278483 | 0.323744 | 0.359676 | 0.51622 |
| tossup | drop_share_3_d2 | 1240 | 0.537162 | 0.1285 | 0.109354 | 0.367428 | 0.424474 | 0.519066 | 0.636003 | 0.758272 | 0.876586 |
| tossup | drop_share_1_d3 | 1240 | 0.21509 | 0.0557587 | 0.0608339 | 0.119671 | 0.175797 | 0.220898 | 0.257693 | 0.293615 | 0.410647 |
| tossup | drop_share_2_d3 | 1240 | 0.287277 | 0.0597544 | 0.0712215 | 0.171289 | 0.255372 | 0.301734 | 0.328034 | 0.356863 | 0.501034 |
| tossup | drop_share_3_d3 | 1240 | 0.497633 | 0.105638 | 0.248169 | 0.368128 | 0.415811 | 0.473246 | 0.562003 | 0.703846 | 0.858678 |
| tossup | r_1 | 1240 | 0.394757 | 0.211481 | 0.0372822 | 0.0772909 | 0.215881 | 0.391397 | 0.54294 | 0.765736 | 0.930184 |
| tossup | r_2 | 1240 | 0.320517 | 0.186502 | 0.0310404 | 0.0646567 | 0.1718 | 0.302824 | 0.425796 | 0.689485 | 0.858941 |
| tossup | r_3 | 1240 | 0.284726 | 0.171801 | 0.0292926 | 0.0605449 | 0.143049 | 0.263183 | 0.393047 | 0.615389 | 0.882579 |
| tossup | r_norm | 1240 | 0.66607 | 0.0701638 | 0.577409 | 0.584236 | 0.61091 | 0.651765 | 0.700438 | 0.806131 | 0.931499 |
