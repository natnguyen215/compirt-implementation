# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 302266 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.605149 |
| log_loss | 0.794659 |
| ece | 0.355254 |
| brier | 0.297911 |
| accuracy | 0.365696 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.407659 |
| probability_std | 0.0960255 |
| probability_p10 | 0.292812 |
| probability_p50 | 0.418688 |
| probability_p90 | 0.541562 |
| mean_predictive_variance | 0.234072 |
| integrated_brier_score | 0.0937598 |
| joint_tossup_event_log_loss | 6.79526 |
| buzz_position_mae | 0.137279 |
| buzz_position_median_absolute_error | 0.114722 |
| buzz_position_bias | -0.00343356 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.38986 |
| first_buzzer_mean_reciprocal_rank | 0.59549 |
| first_buzzer_log_loss | 1.62179 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.605149 |
| neg_average_precision | 0.310607 |
| neg_precision | 0.247629 |
| neg_recall | 0.882437 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.127087 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0492566 |
| no_buzz_calibration_error | 0.0375295 |
| no_buzz_brier | 0.0180395 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.605149 | 0.794659 | 0.355254 | 0.297911 | 0.365696 | 0.773355 | -0.407659 | 0.0960255 | 0.292812 | 0.418688 | 0.541562 | 0.234072 |
| tossup_correctness | tier | fall | 2876 | 0.616419 | 0.793521 | 0.37131 | 0.297783 | 0.354312 | 0.793115 | -0.438804 | 0.0913423 | 0.30474 | 0.419837 | 0.541245 | 0.235542 |
| tossup_correctness | tier | nationals | 1579 | 0.593644 | 0.775068 | 0.306021 | 0.287867 | 0.424953 | 0.729576 | -0.304623 | 0.106271 | 0.279864 | 0.424673 | 0.562006 | 0.232863 |
| tossup_correctness | tier | regionals | 1990 | 0.609794 | 0.786235 | 0.343994 | 0.293659 | 0.394975 | 0.765829 | -0.370854 | 0.103917 | 0.282505 | 0.421961 | 0.554608 | 0.233091 |
| tossup_correctness | tier | winter | 2825 | 0.604256 | 0.812702 | 0.37436 | 0.306652 | 0.32354 | 0.783009 | -0.459469 | 0.0878319 | 0.293671 | 0.411028 | 0.521266 | 0.233941 |
| tossup_correctness | category | Current Events | 123 | 0.66471 | 0.780916 | 0.351467 | 0.291686 | 0.373984 | 0.764228 | -0.390244 | 0.0947479 | 0.279629 | 0.415948 | 0.514424 | 0.233412 |
| tossup_correctness | category | Fine Arts | 1093 | 0.605463 | 0.80532 | 0.35984 | 0.302865 | 0.358646 | 0.769442 | -0.410796 | 0.0969747 | 0.281163 | 0.408388 | 0.537788 | 0.232424 |
| tossup_correctness | category | Geography | 191 | 0.537108 | 0.794817 | 0.289663 | 0.297992 | 0.403141 | 0.691099 | -0.287958 | 0.085168 | 0.293976 | 0.401346 | 0.509947 | 0.233032 |
| tossup_correctness | category | History | 1469 | 0.633087 | 0.773254 | 0.33554 | 0.28803 | 0.385296 | 0.758339 | -0.373043 | 0.0901199 | 0.309253 | 0.421646 | 0.539417 | 0.235918 |
| tossup_correctness | category | Literature | 1436 | 0.57542 | 0.806617 | 0.388465 | 0.303064 | 0.351671 | 0.81546 | -0.463788 | 0.101735 | 0.289131 | 0.431897 | 0.552294 | 0.23432 |
| tossup_correctness | category | Mythology | 325 | 0.492772 | 0.867287 | 0.439954 | 0.33323 | 0.236923 | 0.843077 | -0.606154 | 0.0820642 | 0.296884 | 0.39999 | 0.504362 | 0.23388 |
| tossup_correctness | category | Other Academic | 67 | 0.591644 | 0.859658 | 0.406673 | 0.328079 | 0.268657 | 0.791045 | -0.522388 | 0.0908058 | 0.250285 | 0.393089 | 0.485484 | 0.228384 |
| tossup_correctness | category | Philosophy | 322 | 0.66048 | 0.783272 | 0.366508 | 0.292677 | 0.385093 | 0.785714 | -0.400621 | 0.096614 | 0.292989 | 0.422774 | 0.541438 | 0.234138 |
| tossup_correctness | category | Popular Culture | 100 | 0.529111 | 0.891595 | 0.487237 | 0.343191 | 0.19 | 0.89 | -0.7 | 0.0883172 | 0.290381 | 0.401503 | 0.502204 | 0.232745 |
| tossup_correctness | category | Religion | 365 | 0.662091 | 0.765546 | 0.310335 | 0.284543 | 0.408219 | 0.723288 | -0.315068 | 0.0925914 | 0.293354 | 0.412293 | 0.537704 | 0.23385 |
| tossup_correctness | category | Science | 1456 | 0.583128 | 0.79778 | 0.349677 | 0.299691 | 0.339286 | 0.76717 | -0.427885 | 0.0875122 | 0.306574 | 0.418245 | 0.524407 | 0.235534 |
| tossup_correctness | category | Social Science | 333 | 0.646776 | 0.774059 | 0.320366 | 0.288473 | 0.411411 | 0.72973 | -0.318318 | 0.0965163 | 0.287082 | 0.403242 | 0.532382 | 0.23247 |
| tossup_correctness | category | Unknown | 1990 | 0.609794 | 0.786235 | 0.343994 | 0.293659 | 0.394975 | 0.765829 | -0.370854 | 0.103917 | 0.282505 | 0.421961 | 0.554608 | 0.233091 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.602322 | 0.98917 | 0.448458 | 0.383889 | 0.251397 | 0.748603 | -0.497207 | 0.0830485 | 0.193544 | 0.303033 | 0.40828 | 0.203279 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.629003 | 0.896977 | 0.408464 | 0.344462 | 0.280042 | 0.754441 | -0.474399 | 0.0887548 | 0.230866 | 0.344627 | 0.460992 | 0.2184 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.628718 | 0.843575 | 0.384336 | 0.320697 | 0.30867 | 0.766682 | -0.458012 | 0.0893386 | 0.268533 | 0.378096 | 0.497849 | 0.228176 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.625229 | 0.789041 | 0.366093 | 0.296039 | 0.34587 | 0.787441 | -0.441572 | 0.0847548 | 0.312536 | 0.42008 | 0.528771 | 0.236631 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.598104 | 0.718883 | 0.299753 | 0.262502 | 0.462919 | 0.771758 | -0.308838 | 0.0798859 | 0.373512 | 0.469084 | 0.577279 | 0.242834 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | 5.1702 | 1.5877 | 1.85409 | 3.54915 | 4.24 | 4.78346 | 5.61944 | 7.9489 | 13.558 |
| player | beta | 1196 | -2.85979 | 0.826865 | -6.49415 | -4.29637 | -3.38084 | -2.74755 | -2.27836 | -1.66429 | -0.894728 |
| player | theta_1 | 1196 | -1.63747 | 0.586359 | -3.71532 | -2.65352 | -1.99565 | -1.61328 | -1.25095 | -0.728083 | 0.672257 |
| player | theta_2 | 1196 | -1.59949 | 0.635292 | -3.44539 | -2.56452 | -2.0254 | -1.65377 | -1.2222 | -0.449176 | 0.710167 |
| player | theta_3 | 1196 | -1.48335 | 0.563072 | -3.7926 | -2.38747 | -1.86247 | -1.48277 | -1.1117 | -0.561925 | 0.167482 |
| player | theta_norm | 1196 | 2.87041 | 0.514316 | 1.01733 | 2.03126 | 2.52916 | 2.90282 | 3.22126 | 3.68969 | 4.31553 |
| tossup | start_difficulty_d1 | 1240 | 0.140998 | 0.314908 | -0.976725 | -0.391091 | -0.0647116 | 0.145201 | 0.342577 | 0.655358 | 1.09316 |
| tossup | start_difficulty_d2 | 1240 | 0.165295 | 0.302581 | -0.92381 | -0.343111 | -0.0429878 | 0.181037 | 0.364435 | 0.649855 | 1.07325 |
| tossup | start_difficulty_d3 | 1240 | 0.166575 | 0.307308 | -0.862602 | -0.346601 | -0.043601 | 0.180762 | 0.375497 | 0.67108 | 1.04509 |
| tossup | end_difficulty_d1 | 1240 | -1.38532 | 0.543213 | -3.94474 | -2.1512 | -1.70973 | -1.46059 | -1.03675 | -0.416041 | -0.0227511 |
| tossup | end_difficulty_d2 | 1240 | -1.25255 | 0.507286 | -3.57882 | -2.02102 | -1.58732 | -1.29519 | -0.894591 | -0.419483 | 0.0865764 |
| tossup | end_difficulty_d3 | 1240 | -1.16731 | 0.519786 | -3.57593 | -2.0123 | -1.47738 | -1.18737 | -0.785016 | -0.344568 | 0.137751 |
| tossup | total_drop_d1 | 1240 | 1.52632 | 0.530158 | 0.60838 | 0.873315 | 1.0565 | 1.49514 | 1.85512 | 2.45922 | 4.98314 |
| tossup | total_drop_d2 | 1240 | 1.41784 | 0.478182 | 0.66728 | 0.877496 | 0.976592 | 1.34873 | 1.72887 | 2.29787 | 3.87673 |
| tossup | total_drop_d3 | 1240 | 1.33389 | 0.447209 | 0.549424 | 0.871036 | 0.968056 | 1.21825 | 1.58187 | 2.19858 | 3.48805 |
| tossup | drop_share_1_d1 | 1240 | 0.255123 | 0.0952005 | 0.0482025 | 0.133096 | 0.189472 | 0.250323 | 0.294512 | 0.462655 | 0.73777 |
| tossup | drop_share_2_d1 | 1240 | 0.270187 | 0.0646819 | 0.0845169 | 0.153899 | 0.22325 | 0.277817 | 0.323108 | 0.353222 | 0.519652 |
| tossup | drop_share_3_d1 | 1240 | 0.47469 | 0.127367 | 0.0778836 | 0.294689 | 0.380185 | 0.454994 | 0.564933 | 0.690216 | 0.859928 |
| tossup | drop_share_1_d2 | 1240 | 0.251586 | 0.0766468 | 0.0842802 | 0.137068 | 0.200948 | 0.252874 | 0.290971 | 0.370221 | 0.688857 |
| tossup | drop_share_2_d2 | 1240 | 0.277824 | 0.0657284 | 0.0601234 | 0.151737 | 0.234181 | 0.291554 | 0.330462 | 0.355246 | 0.486212 |
| tossup | drop_share_3_d2 | 1240 | 0.47059 | 0.116549 | 0.0795023 | 0.329633 | 0.380872 | 0.450669 | 0.549154 | 0.694916 | 0.855596 |
| tossup | drop_share_1_d3 | 1240 | 0.260455 | 0.069203 | 0.0868662 | 0.153304 | 0.219734 | 0.261531 | 0.292705 | 0.359707 | 0.646917 |
| tossup | drop_share_2_d3 | 1240 | 0.291062 | 0.054372 | 0.0841633 | 0.183806 | 0.25904 | 0.302569 | 0.330516 | 0.352888 | 0.472781 |
| tossup | drop_share_3_d3 | 1240 | 0.448482 | 0.0998757 | 0.133327 | 0.324931 | 0.377596 | 0.428548 | 0.503999 | 0.642932 | 0.826531 |
| tossup | r_1 | 1240 | 0.378408 | 0.177686 | 0.0297261 | 0.0873176 | 0.240246 | 0.393887 | 0.508037 | 0.662735 | 0.812744 |
| tossup | r_2 | 1240 | 0.334871 | 0.17112 | 0.0266778 | 0.0787555 | 0.194883 | 0.337303 | 0.455668 | 0.621318 | 0.881368 |
| tossup | r_3 | 1240 | 0.286721 | 0.152759 | 0.0226059 | 0.0649141 | 0.166173 | 0.278374 | 0.38539 | 0.558773 | 0.786458 |
| tossup | r_norm | 1240 | 0.647366 | 0.0508003 | 0.577382 | 0.582861 | 0.608126 | 0.640251 | 0.673715 | 0.749159 | 0.886818 |
