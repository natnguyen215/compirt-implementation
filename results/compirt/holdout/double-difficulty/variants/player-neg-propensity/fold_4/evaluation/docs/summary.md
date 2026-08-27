# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 281891 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.725361 |
| log_loss | 0.475326 |
| ece | 0.00785134 |
| brier | 0.153464 |
| accuracy | 0.788134 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0147789 |
| probability_std | 0.14347 |
| probability_p10 | 0.573311 |
| probability_p50 | 0.814524 |
| probability_p90 | 0.92135 |
| mean_predictive_variance | 0.152788 |
| integrated_brier_score | 0.100276 |
| joint_tossup_event_log_loss | 6.55952 |
| buzz_position_mae | 0.149853 |
| buzz_position_median_absolute_error | 0.132632 |
| buzz_position_bias | -0.0430568 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.365912 |
| first_buzzer_mean_reciprocal_rank | 0.575961 |
| first_buzzer_log_loss | 1.65173 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.725361 |
| neg_average_precision | 0.453999 |
| neg_precision | 0.631985 |
| neg_recall | 0.156116 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.18397 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0133675 |
| no_buzz_calibration_error | 0.00164044 |
| no_buzz_brier | 0.010975 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.725361 | 0.475326 | 0.00785134 | 0.153464 | 0.788134 | 0.773355 | 0.0147789 | 0.14347 | 0.573311 | 0.814524 | 0.92135 | 0.152788 |
| tossup_correctness | tier | fall | 2876 | 0.726162 | 0.45224 | 0.0107658 | 0.144148 | 0.804937 | 0.793115 | 0.011822 | 0.136451 | 0.59375 | 0.823938 | 0.927292 | 0.14837 |
| tossup_correctness | tier | nationals | 1579 | 0.717213 | 0.525598 | 0.0361552 | 0.173888 | 0.752375 | 0.729576 | 0.0227992 | 0.154644 | 0.545543 | 0.802856 | 0.918259 | 0.15657 |
| tossup_correctness | tier | regionals | 1990 | 0.740379 | 0.477427 | 0.0230068 | 0.154848 | 0.784422 | 0.765829 | 0.018593 | 0.143803 | 0.561263 | 0.805201 | 0.914425 | 0.157963 |
| tossup_correctness | tier | winter | 2825 | 0.716159 | 0.469249 | 0.0101481 | 0.150557 | 0.793628 | 0.783009 | 0.0106195 | 0.14267 | 0.574006 | 0.817077 | 0.920972 | 0.151525 |
| tossup_correctness | category | Current Events | 123 | 0.775495 | 0.46213 | 0.0858421 | 0.149306 | 0.788618 | 0.764228 | 0.0243902 | 0.13229 | 0.556486 | 0.7526 | 0.913293 | 0.172247 |
| tossup_correctness | category | Fine Arts | 1093 | 0.736529 | 0.468938 | 0.0229456 | 0.150119 | 0.794145 | 0.769442 | 0.0247027 | 0.143321 | 0.583385 | 0.825691 | 0.925112 | 0.148796 |
| tossup_correctness | category | Geography | 191 | 0.796867 | 0.486792 | 0.0664703 | 0.157495 | 0.78534 | 0.691099 | 0.0942408 | 0.193165 | 0.448888 | 0.764154 | 0.891593 | 0.171895 |
| tossup_correctness | category | History | 1469 | 0.713993 | 0.503582 | 0.0326786 | 0.166156 | 0.75902 | 0.758339 | 0.000680735 | 0.147068 | 0.550056 | 0.809542 | 0.921377 | 0.154778 |
| tossup_correctness | category | Literature | 1436 | 0.721045 | 0.429967 | 0.0140159 | 0.134859 | 0.817549 | 0.81546 | 0.00208914 | 0.125569 | 0.641051 | 0.849431 | 0.933924 | 0.135751 |
| tossup_correctness | category | Mythology | 325 | 0.663733 | 0.418943 | 0.0378161 | 0.128989 | 0.84 | 0.843077 | -0.00307692 | 0.104049 | 0.673047 | 0.82807 | 0.917511 | 0.144517 |
| tossup_correctness | category | Other Academic | 67 | 0.679245 | 0.487183 | 0.0909482 | 0.156324 | 0.80597 | 0.791045 | 0.0149254 | 0.135241 | 0.568803 | 0.756466 | 0.906651 | 0.170353 |
| tossup_correctness | category | Philosophy | 322 | 0.672681 | 0.493192 | 0.0325422 | 0.160796 | 0.770186 | 0.785714 | -0.015528 | 0.129523 | 0.608336 | 0.820339 | 0.934113 | 0.147377 |
| tossup_correctness | category | Popular Culture | 100 | 0.538304 | 0.367313 | 0.0538906 | 0.105612 | 0.89 | 0.89 | 0 | 0.0712574 | 0.748855 | 0.861162 | 0.924997 | 0.12513 |
| tossup_correctness | category | Religion | 365 | 0.657853 | 0.561861 | 0.0474591 | 0.187629 | 0.742466 | 0.723288 | 0.0191781 | 0.142273 | 0.56647 | 0.794939 | 0.908079 | 0.163702 |
| tossup_correctness | category | Science | 1456 | 0.72129 | 0.482706 | 0.0112624 | 0.1563 | 0.784341 | 0.76717 | 0.0171703 | 0.147114 | 0.560584 | 0.803906 | 0.913835 | 0.15726 |
| tossup_correctness | category | Social Science | 333 | 0.749977 | 0.493673 | 0.0430608 | 0.160378 | 0.792793 | 0.72973 | 0.0630631 | 0.161968 | 0.506386 | 0.780045 | 0.916946 | 0.168054 |
| tossup_correctness | category | Unknown | 1990 | 0.740379 | 0.477427 | 0.0230068 | 0.154848 | 0.784422 | 0.765829 | 0.018593 | 0.143803 | 0.561263 | 0.805201 | 0.914425 | 0.157963 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.739303 | 0.491825 | 0.048895 | 0.161228 | 0.759777 | 0.748603 | 0.0111732 | 0.156935 | 0.492413 | 0.774769 | 0.879614 | 0.171942 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.704603 | 0.50305 | 0.00957524 | 0.164758 | 0.768025 | 0.754441 | 0.0135841 | 0.142691 | 0.550731 | 0.787768 | 0.909131 | 0.163175 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.72404 | 0.484227 | 0.0254437 | 0.157382 | 0.778484 | 0.766682 | 0.0118021 | 0.1419 | 0.58179 | 0.813582 | 0.919858 | 0.153595 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.715876 | 0.463549 | 0.0097449 | 0.148129 | 0.800873 | 0.787441 | 0.0134318 | 0.132583 | 0.610177 | 0.824593 | 0.924578 | 0.147748 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.738782 | 0.470576 | 0.00966988 | 0.15179 | 0.790721 | 0.771758 | 0.0189638 | 0.152662 | 0.546983 | 0.81565 | 0.924111 | 0.15274 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.7067 | 0.70137 | 0.60125 | 1.58658 | 2.22675 | 2.69796 | 3.15278 | 3.94197 | 4.60904 |
| player | theta_1 | 1196 | -1.21361 | 0.778997 | -3.6032 | -2.37599 | -1.71348 | -1.27831 | -0.733477 | 0.196171 | 1.49218 |
| player | theta_2 | 1196 | -1.12016 | 0.786013 | -3.04982 | -2.23582 | -1.64325 | -1.22971 | -0.712925 | 0.404881 | 2.07728 |
| player | theta_3 | 1196 | -0.923005 | 0.687352 | -2.8299 | -1.96901 | -1.40162 | -0.953287 | -0.532383 | 0.302339 | 2.2802 |
| player | theta_norm | 1196 | 2.23724 | 0.519806 | 0.655133 | 1.42555 | 1.88449 | 2.21385 | 2.59236 | 3.10348 | 4.03081 |
| tossup | start_difficulty_d1 | 1240 | -1.76313 | 0.548952 | -3.20296 | -2.55423 | -2.14399 | -1.82318 | -1.46453 | -0.741833 | 1.42127 |
| tossup | start_difficulty_d2 | 1240 | -1.7565 | 0.502656 | -3.35828 | -2.55372 | -2.10503 | -1.78633 | -1.43477 | -0.891869 | 0.331213 |
| tossup | start_difficulty_d3 | 1240 | -1.75839 | 0.501289 | -3.29984 | -2.52608 | -2.11182 | -1.7843 | -1.45101 | -0.863285 | 0.954851 |
| tossup | end_difficulty_d1 | 1240 | -2.75443 | 0.638531 | -4.56432 | -3.69342 | -3.19067 | -2.80877 | -2.40115 | -1.55841 | 0.715263 |
| tossup | end_difficulty_d2 | 1240 | -2.74571 | 0.589475 | -4.55422 | -3.67176 | -3.14865 | -2.77075 | -2.37296 | -1.75464 | -0.273078 |
| tossup | end_difficulty_d3 | 1240 | -2.74799 | 0.586458 | -4.53848 | -3.64762 | -3.16213 | -2.77369 | -2.37921 | -1.71517 | 0.327062 |
| tossup | total_drop_d1 | 1240 | 0.991306 | 0.11251 | 0.632851 | 0.805498 | 0.914708 | 0.990622 | 1.0614 | 1.17932 | 1.79781 |
| tossup | total_drop_d2 | 1240 | 0.989211 | 0.106511 | 0.604291 | 0.821946 | 0.916399 | 0.988454 | 1.05782 | 1.16663 | 1.38285 |
| tossup | total_drop_d3 | 1240 | 0.989607 | 0.102796 | 0.627789 | 0.830355 | 0.917516 | 0.987778 | 1.05834 | 1.16742 | 1.40274 |
| tossup | drop_share_1_d1 | 1240 | 0.303916 | 0.0156422 | 0.184739 | 0.278228 | 0.295371 | 0.304432 | 0.31419 | 0.327782 | 0.356406 |
| tossup | drop_share_2_d1 | 1240 | 0.347109 | 0.0119421 | 0.306318 | 0.32869 | 0.339248 | 0.346841 | 0.3548 | 0.367325 | 0.438126 |
| tossup | drop_share_3_d1 | 1240 | 0.348974 | 0.0162996 | 0.305489 | 0.323833 | 0.337648 | 0.348237 | 0.358837 | 0.376059 | 0.450016 |
| tossup | drop_share_1_d2 | 1240 | 0.304197 | 0.0144713 | 0.23969 | 0.280674 | 0.294896 | 0.304588 | 0.313961 | 0.327434 | 0.34606 |
| tossup | drop_share_2_d2 | 1240 | 0.347108 | 0.0112916 | 0.30963 | 0.328915 | 0.339263 | 0.347436 | 0.354625 | 0.366056 | 0.380497 |
| tossup | drop_share_3_d2 | 1240 | 0.348696 | 0.0152448 | 0.301334 | 0.325361 | 0.338181 | 0.348398 | 0.357827 | 0.375181 | 0.408482 |
| tossup | drop_share_1_d3 | 1240 | 0.304085 | 0.0141819 | 0.235441 | 0.281168 | 0.295213 | 0.304322 | 0.313412 | 0.327371 | 0.352107 |
| tossup | drop_share_2_d3 | 1240 | 0.347251 | 0.0112479 | 0.307249 | 0.328915 | 0.339601 | 0.347339 | 0.354781 | 0.365377 | 0.38583 |
| tossup | drop_share_3_d3 | 1240 | 0.348664 | 0.0153539 | 0.309954 | 0.325158 | 0.337839 | 0.347431 | 0.35852 | 0.374576 | 0.416494 |
| tossup | r_1 | 1240 | 0.318796 | 0.150908 | 0.0816349 | 0.129725 | 0.20377 | 0.283287 | 0.405575 | 0.625179 | 0.850697 |
| tossup | r_2 | 1240 | 0.348901 | 0.134319 | 0.0740396 | 0.152019 | 0.24703 | 0.337471 | 0.435093 | 0.598661 | 0.790324 |
| tossup | r_3 | 1240 | 0.332304 | 0.120695 | 0.0571445 | 0.155875 | 0.245724 | 0.318921 | 0.407152 | 0.548773 | 0.838173 |
| tossup | r_norm | 1240 | 0.622205 | 0.044586 | 0.577361 | 0.579377 | 0.590957 | 0.607789 | 0.637983 | 0.718898 | 0.857581 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.51133 | 0.509117 | 1.81431 | 3.74079 | 4.2266 | 4.46109 | 4.78845 | 5.40752 | 6.59178 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.5243 | 0.457076 | 2.33872 | 3.84013 | 4.27109 | 4.47691 | 4.722 | 5.40401 | 6.68771 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.46169 | 0.402566 | 2.26926 | 3.83343 | 4.26743 | 4.4491 | 4.63316 | 5.13821 | 6.46855 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.60094 | 2.33357 | -10.393 | -3.01638 | 0.102384 | 2.74734 | 3.30843 | 3.67313 | 4.21822 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.23004 | 2.14756 | -10.5636 | -2.62125 | 2.02398 | 3.18043 | 3.424 | 3.73218 | 4.2694 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.43673 | 1.92893 | -11.993 | -2.13899 | 2.49665 | 3.23186 | 3.46023 | 3.70656 | 4.5427 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.91039 | 2.53011 | 0.796933 | 0.984212 | 1.0523 | 1.37712 | 4.69949 | 7.82821 | 15.4542 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.29426 | 2.29509 | 0.894509 | 0.968878 | 1.01982 | 1.15661 | 2.4904 | 7.43357 | 15.6941 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.02496 | 2.06876 | 0.88266 | 0.961497 | 1.01341 | 1.09606 | 1.66181 | 7.01817 | 16.8232 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.233813 | 0.0847503 | 0.0421974 | 0.0810922 | 0.161751 | 0.270209 | 0.294861 | 0.318293 | 0.664633 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.345075 | 0.0820396 | 0.054178 | 0.176764 | 0.335153 | 0.350325 | 0.366462 | 0.472892 | 0.736457 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.421112 | 0.135303 | 0.0742502 | 0.287158 | 0.347734 | 0.368446 | 0.455878 | 0.731978 | 0.903625 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.247084 | 0.0736371 | 0.0334979 | 0.0872486 | 0.218021 | 0.278367 | 0.296481 | 0.315136 | 0.474376 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.343292 | 0.0627513 | 0.0769744 | 0.207691 | 0.338743 | 0.349919 | 0.360378 | 0.417569 | 0.655585 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.409624 | 0.114452 | 0.123618 | 0.320535 | 0.34934 | 0.365586 | 0.414214 | 0.689734 | 0.888378 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.258233 | 0.0677479 | 0.0382111 | 0.0914979 | 0.250468 | 0.284563 | 0.29793 | 0.316319 | 0.492387 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.346285 | 0.0563886 | 0.0538847 | 0.242296 | 0.33948 | 0.349965 | 0.360532 | 0.409126 | 0.696447 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.395482 | 0.101994 | 0.156088 | 0.322113 | 0.348749 | 0.363823 | 0.387646 | 0.652221 | 0.907904 |
| tossup_hazard | hazard_r_1 | 1240 | 0.397729 | 0.291124 | 0.0245328 | 0.0571471 | 0.132897 | 0.303462 | 0.682798 | 0.874921 | 0.945498 |
| tossup_hazard | hazard_r_2 | 1240 | 0.323617 | 0.260537 | 0.0263693 | 0.0524641 | 0.103149 | 0.215847 | 0.534756 | 0.82753 | 0.932958 |
| tossup_hazard | hazard_r_3 | 1240 | 0.278654 | 0.238324 | 0.0281328 | 0.054633 | 0.100325 | 0.172283 | 0.415295 | 0.786486 | 0.902666 |
