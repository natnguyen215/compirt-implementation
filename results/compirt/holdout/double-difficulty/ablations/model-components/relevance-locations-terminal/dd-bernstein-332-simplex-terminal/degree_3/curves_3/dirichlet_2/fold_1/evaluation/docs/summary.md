# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 303182 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.712897 |
| log_loss | 0.506502 |
| ece | 0.0683872 |
| brier | 0.165227 |
| accuracy | 0.768393 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00626856 |
| probability_std | 0.165405 |
| probability_p10 | 0.464632 |
| probability_p50 | 0.724465 |
| probability_p90 | 0.894359 |
| mean_predictive_variance | 0.183244 |
| integrated_brier_score | 0.109369 |
| joint_tossup_event_log_loss | 6.71536 |
| buzz_position_mae | 0.166176 |
| buzz_position_median_absolute_error | 0.150058 |
| buzz_position_bias | -0.0802368 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.324865 |
| first_buzzer_mean_reciprocal_rank | 0.541873 |
| first_buzzer_log_loss | 1.72113 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.712897 |
| neg_average_precision | 0.460498 |
| neg_precision | 0.523573 |
| neg_recall | 0.292649 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.176796 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0120081 |
| no_buzz_calibration_error | -0.00390101 |
| no_buzz_brier | 0.0148396 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.712897 | 0.506502 | 0.0683872 | 0.165227 | 0.768393 | 0.762125 | 0.00626856 | 0.165405 | 0.464632 | 0.724465 | 0.894359 | 0.183244 |
| tossup_correctness | tier | fall | 2842 | 0.728216 | 0.472829 | 0.0590309 | 0.15199 | 0.787474 | 0.785362 | 0.00211119 | 0.159003 | 0.498738 | 0.758411 | 0.912726 | 0.172796 |
| tossup_correctness | tier | nationals | 1564 | 0.715552 | 0.54511 | 0.0687069 | 0.181744 | 0.741049 | 0.718031 | 0.0230179 | 0.165437 | 0.422631 | 0.673716 | 0.850387 | 0.199858 |
| tossup_correctness | tier | regionals | 1937 | 0.694469 | 0.525126 | 0.0818161 | 0.172665 | 0.756324 | 0.758389 | -0.00206505 | 0.165856 | 0.442234 | 0.705899 | 0.877401 | 0.189498 |
| tossup_correctness | tier | winter | 2750 | 0.701647 | 0.506227 | 0.07111 | 0.164276 | 0.772727 | 0.765818 | 0.00690909 | 0.164139 | 0.474181 | 0.738366 | 0.899887 | 0.180189 |
| tossup_correctness | category | Current Events | 126 | 0.727693 | 0.517963 | 0.119823 | 0.170989 | 0.753968 | 0.769841 | -0.015873 | 0.149407 | 0.436953 | 0.656046 | 0.846096 | 0.205172 |
| tossup_correctness | category | Fine Arts | 1071 | 0.738582 | 0.486659 | 0.0738882 | 0.157245 | 0.791783 | 0.766573 | 0.0252101 | 0.174251 | 0.444692 | 0.726241 | 0.899539 | 0.181045 |
| tossup_correctness | category | Geography | 185 | 0.79222 | 0.524708 | 0.118064 | 0.170127 | 0.756757 | 0.697297 | 0.0594595 | 0.213681 | 0.302073 | 0.672585 | 0.848123 | 0.191489 |
| tossup_correctness | category | History | 1440 | 0.71657 | 0.508441 | 0.0523436 | 0.166502 | 0.759028 | 0.754167 | 0.00486111 | 0.163546 | 0.472266 | 0.728745 | 0.904764 | 0.180734 |
| tossup_correctness | category | Literature | 1422 | 0.697791 | 0.462426 | 0.0797499 | 0.147072 | 0.799578 | 0.814346 | -0.0147679 | 0.149128 | 0.531567 | 0.76903 | 0.909674 | 0.170405 |
| tossup_correctness | category | Mythology | 318 | 0.704406 | 0.477015 | 0.0646192 | 0.152164 | 0.808176 | 0.789308 | 0.0188679 | 0.151296 | 0.511315 | 0.765195 | 0.902871 | 0.171852 |
| tossup_correctness | category | Other Academic | 66 | 0.802912 | 0.510113 | 0.104194 | 0.167441 | 0.757576 | 0.712121 | 0.0454545 | 0.15518 | 0.462473 | 0.691432 | 0.827593 | 0.203498 |
| tossup_correctness | category | Philosophy | 311 | 0.721519 | 0.511393 | 0.0451585 | 0.169432 | 0.755627 | 0.745981 | 0.0096463 | 0.145445 | 0.510386 | 0.721021 | 0.891097 | 0.185795 |
| tossup_correctness | category | Popular Culture | 102 | 0.426852 | 0.43626 | 0.140554 | 0.128768 | 0.872549 | 0.882353 | -0.00980392 | 0.105637 | 0.622598 | 0.787903 | 0.880342 | 0.165551 |
| tossup_correctness | category | Religion | 358 | 0.700438 | 0.555014 | 0.0741005 | 0.185481 | 0.734637 | 0.712291 | 0.0223464 | 0.163838 | 0.437671 | 0.69706 | 0.865731 | 0.195252 |
| tossup_correctness | category | Science | 1433 | 0.695841 | 0.533265 | 0.0573474 | 0.176352 | 0.7418 | 0.738311 | 0.00348918 | 0.166202 | 0.465297 | 0.716505 | 0.895169 | 0.185944 |
| tossup_correctness | category | Social Science | 324 | 0.757408 | 0.504389 | 0.0741581 | 0.164355 | 0.777778 | 0.731481 | 0.0462963 | 0.169318 | 0.414706 | 0.691218 | 0.874879 | 0.192374 |
| tossup_correctness | category | Unknown | 1937 | 0.694469 | 0.525126 | 0.0818161 | 0.172665 | 0.756324 | 0.758389 | -0.00206505 | 0.165856 | 0.442234 | 0.705899 | 0.877401 | 0.189498 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.66159 | 0.580394 | 0.0929508 | 0.198101 | 0.694611 | 0.712575 | -0.0179641 | 0.157162 | 0.429451 | 0.679547 | 0.835775 | 0.201628 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.719686 | 0.534076 | 0.0695901 | 0.177941 | 0.735746 | 0.729167 | 0.00657895 | 0.18198 | 0.394067 | 0.687651 | 0.878256 | 0.190377 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.725177 | 0.502608 | 0.0506218 | 0.163741 | 0.770213 | 0.755083 | 0.01513 | 0.161538 | 0.480583 | 0.732058 | 0.901348 | 0.180984 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.69259 | 0.498609 | 0.077217 | 0.161284 | 0.777778 | 0.780942 | -0.00316456 | 0.156809 | 0.495068 | 0.738115 | 0.898517 | 0.179823 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.719628 | 0.504276 | 0.076003 | 0.164335 | 0.772177 | 0.762029 | 0.0101473 | 0.168642 | 0.452144 | 0.715823 | 0.889736 | 0.18486 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 4.4004 | 0.546258 | 2.33904 | 3.50987 | 4.01784 | 4.43327 | 4.76795 | 5.30785 | 5.76551 |
| player | theta_1 | 1167 | -1.24738 | 0.920449 | -3.68973 | -2.51716 | -1.90454 | -1.37308 | -0.649473 | 0.424558 | 1.90595 |
| player | theta_2 | 1167 | -1.10439 | 0.716644 | -3.63139 | -2.20803 | -1.59173 | -1.15128 | -0.687928 | 0.213654 | 1.11306 |
| player | theta_3 | 1167 | -0.997536 | 0.625673 | -3.21727 | -1.97155 | -1.40054 | -1.00846 | -0.577134 | 0.0565612 | 1.07009 |
| player | theta_norm | 1167 | 2.25184 | 0.671614 | 0.289642 | 1.12838 | 1.78842 | 2.27185 | 2.73254 | 3.30719 | 4.29721 |
| tossup | start_difficulty_d1 | 1220 | -0.784414 | 0.67063 | -3.34391 | -2.09768 | -1.10677 | -0.703749 | -0.36708 | 0.176385 | 1.18937 |
| tossup | start_difficulty_d2 | 1220 | -0.642753 | 0.503095 | -3.00746 | -1.53674 | -0.857316 | -0.596423 | -0.388039 | 0.114949 | 1.33816 |
| tossup | start_difficulty_d3 | 1220 | -0.657481 | 0.540698 | -3.16426 | -1.62274 | -0.873853 | -0.609124 | -0.382302 | 0.143154 | 0.967468 |
| tossup | end_difficulty_d1 | 1220 | -1.95969 | 0.86352 | -5.61948 | -3.67972 | -2.34666 | -1.84585 | -1.432 | -0.751809 | 0.444256 |
| tossup | end_difficulty_d2 | 1220 | -1.77705 | 0.646291 | -4.69492 | -2.89653 | -2.02954 | -1.71555 | -1.44951 | -0.87033 | 0.500466 |
| tossup | end_difficulty_d3 | 1220 | -1.79523 | 0.690389 | -5.18588 | -3.08238 | -2.04581 | -1.73294 | -1.44218 | -0.819421 | 0.206915 |
| tossup | total_drop_d1 | 1220 | 1.17527 | 0.242966 | 0.719485 | 0.904043 | 1.03478 | 1.12089 | 1.24863 | 1.64886 | 3.06142 |
| tossup | total_drop_d2 | 1220 | 1.13429 | 0.184928 | 0.760788 | 0.923776 | 1.03918 | 1.11028 | 1.18866 | 1.39633 | 2.90555 |
| tossup | total_drop_d3 | 1220 | 1.13775 | 0.183649 | 0.760553 | 0.914263 | 1.03529 | 1.11244 | 1.19385 | 1.45905 | 2.64977 |
| tossup | drop_share_1_d1 | 1220 | 0.31735 | 0.0216192 | 0.248659 | 0.288221 | 0.304225 | 0.314564 | 0.327229 | 0.358176 | 0.41113 |
| tossup | drop_share_2_d1 | 1220 | 0.349589 | 0.0122139 | 0.310195 | 0.330279 | 0.342121 | 0.349292 | 0.356837 | 0.369127 | 0.414808 |
| tossup | drop_share_3_d1 | 1220 | 0.333061 | 0.0210744 | 0.247416 | 0.291854 | 0.32298 | 0.335339 | 0.347474 | 0.361578 | 0.39063 |
| tossup | drop_share_1_d2 | 1220 | 0.313926 | 0.0170165 | 0.238878 | 0.288941 | 0.303745 | 0.313185 | 0.323208 | 0.34054 | 0.409542 |
| tossup | drop_share_2_d2 | 1220 | 0.34917 | 0.0120075 | 0.305961 | 0.329484 | 0.341992 | 0.349011 | 0.356119 | 0.369386 | 0.425427 |
| tossup | drop_share_3_d2 | 1220 | 0.336904 | 0.0174616 | 0.247993 | 0.309294 | 0.327144 | 0.336869 | 0.347788 | 0.363475 | 0.411092 |
| tossup | drop_share_1_d3 | 1220 | 0.315442 | 0.0186879 | 0.264535 | 0.288486 | 0.30359 | 0.314084 | 0.324528 | 0.346379 | 0.436989 |
| tossup | drop_share_2_d3 | 1220 | 0.348421 | 0.0114862 | 0.306719 | 0.329807 | 0.340641 | 0.348459 | 0.35583 | 0.367344 | 0.392093 |
| tossup | drop_share_3_d3 | 1220 | 0.336137 | 0.0183214 | 0.231631 | 0.306368 | 0.326649 | 0.337182 | 0.347588 | 0.363036 | 0.406523 |
| tossup | r_1 | 1220 | 0.368014 | 0.195611 | 0.0428781 | 0.0963702 | 0.206194 | 0.338185 | 0.507663 | 0.738673 | 0.861502 |
| tossup | r_2 | 1220 | 0.310328 | 0.173232 | 0.0526862 | 0.0916042 | 0.177968 | 0.272743 | 0.40703 | 0.650115 | 0.875695 |
| tossup | r_3 | 1220 | 0.321657 | 0.165268 | 0.06673 | 0.109788 | 0.206676 | 0.290885 | 0.397675 | 0.660456 | 0.896712 |
| tossup | r_norm | 1220 | 0.652241 | 0.0727738 | 0.577357 | 0.581137 | 0.597642 | 0.626394 | 0.681072 | 0.81896 | 0.899686 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 1.78537 | 0.848556 | 0.19441 | 0.640822 | 1.07034 | 1.63025 | 2.45222 | 3.28539 | 4.24405 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 1.58508 | 0.778297 | 0.213507 | 0.538088 | 0.97628 | 1.46185 | 2.08625 | 3.02155 | 4.31657 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 1.54264 | 0.786658 | 0.277579 | 0.616893 | 0.933743 | 1.34704 | 2.00272 | 3.16474 | 4.68829 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | -0.360135 | 1.44854 | -8.00845 | -3.48074 | -0.455761 | 0.0364422 | 0.47384 | 1.05371 | 2.04122 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | -0.369839 | 1.25597 | -10.1236 | -2.83211 | -0.479978 | -0.0491492 | 0.280338 | 0.76833 | 1.6902 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | -0.250915 | 1.26399 | -8.68322 | -2.8456 | -0.309018 | 0.0127152 | 0.372384 | 0.851568 | 2.48966 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.14551 | 1.93341 | 0.797191 | 0.946189 | 1.00912 | 1.10429 | 2.60224 | 6.24432 | 11.2594 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 1.95492 | 1.7518 | 0.818016 | 0.951014 | 1.00443 | 1.09108 | 1.99239 | 5.78511 | 13.1766 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 1.79355 | 1.7494 | 0.750416 | 0.948725 | 0.996862 | 1.05122 | 1.35503 | 5.6756 | 11.7169 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.226955 | 0.0762602 | 0.0335097 | 0.0746238 | 0.175906 | 0.257913 | 0.284547 | 0.304042 | 0.358942 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.348184 | 0.0785122 | 0.0786093 | 0.184506 | 0.338135 | 0.350808 | 0.364912 | 0.479903 | 0.695081 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.424861 | 0.12396 | 0.0849789 | 0.322373 | 0.358901 | 0.380069 | 0.431389 | 0.733789 | 0.885811 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.234917 | 0.0740741 | 0.0283069 | 0.0799787 | 0.191275 | 0.267105 | 0.288855 | 0.307055 | 0.481007 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.345432 | 0.063898 | 0.0640862 | 0.214886 | 0.338131 | 0.350793 | 0.364007 | 0.421764 | 0.76401 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.419651 | 0.114222 | 0.123144 | 0.334937 | 0.356618 | 0.375168 | 0.433035 | 0.695416 | 0.892441 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.243942 | 0.0701578 | 0.0377281 | 0.0774777 | 0.225536 | 0.272166 | 0.290169 | 0.306795 | 0.380367 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.34549 | 0.0576507 | 0.051818 | 0.229753 | 0.34011 | 0.350006 | 0.362218 | 0.411299 | 0.664619 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.410568 | 0.106292 | 0.227461 | 0.336508 | 0.356089 | 0.373233 | 0.406829 | 0.675231 | 0.910454 |
| tossup_hazard | hazard_r_1 | 1220 | 0.378836 | 0.305006 | 0.0284669 | 0.0496122 | 0.101502 | 0.264755 | 0.680267 | 0.897166 | 0.950975 |
| tossup_hazard | hazard_r_2 | 1220 | 0.339552 | 0.286568 | 0.0105684 | 0.0324882 | 0.0871071 | 0.227703 | 0.602898 | 0.854782 | 0.918837 |
| tossup_hazard | hazard_r_3 | 1220 | 0.281612 | 0.250376 | 0.0196609 | 0.04168 | 0.0815578 | 0.168827 | 0.456231 | 0.784742 | 0.90923 |
