# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 309820 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.607158 |
| log_loss | 0.673627 |
| ece | 0.222216 |
| brier | 0.237924 |
| accuracy | 0.616078 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.146046 |
| probability_std | 0.176575 |
| probability_p10 | 0.293515 |
| probability_p50 | 0.557117 |
| probability_p90 | 0.762137 |
| mean_predictive_variance | 0.217226 |
| integrated_brier_score | 0.0938343 |
| joint_tossup_event_log_loss | 6.7758 |
| buzz_position_mae | 0.137838 |
| buzz_position_median_absolute_error | 0.113972 |
| buzz_position_bias | -0.00358214 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.362037 |
| first_buzzer_mean_reciprocal_rank | 0.574517 |
| first_buzzer_log_loss | 1.65341 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.607158 |
| neg_average_precision | 0.314098 |
| neg_precision | 0.310394 |
| neg_recall | 0.502543 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.144306 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0519004 |
| no_buzz_calibration_error | 0.0359913 |
| no_buzz_brier | 0.0213995 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.607158 | 0.673627 | 0.222216 | 0.237924 | 0.616078 | 0.762125 | -0.146046 | 0.176575 | 0.293515 | 0.557117 | 0.762137 | 0.217226 |
| tossup_correctness | tier | fall | 2842 | 0.613259 | 0.667177 | 0.244623 | 0.235053 | 0.62069 | 0.785362 | -0.164673 | 0.174403 | 0.302266 | 0.554789 | 0.765637 | 0.2179 |
| tossup_correctness | tier | nationals | 1564 | 0.604713 | 0.666209 | 0.185682 | 0.23608 | 0.608056 | 0.718031 | -0.109974 | 0.162153 | 0.316392 | 0.552915 | 0.740766 | 0.222381 |
| tossup_correctness | tier | regionals | 1937 | 0.608295 | 0.668265 | 0.205605 | 0.234972 | 0.63397 | 0.758389 | -0.124419 | 0.183806 | 0.291426 | 0.572049 | 0.781552 | 0.213386 |
| tossup_correctness | tier | winter | 2750 | 0.603461 | 0.688289 | 0.234314 | 0.244019 | 0.603273 | 0.765818 | -0.162545 | 0.18085 | 0.273034 | 0.551848 | 0.757206 | 0.216301 |
| tossup_correctness | category | Current Events | 126 | 0.576964 | 0.764139 | 0.300503 | 0.279206 | 0.52381 | 0.769841 | -0.246032 | 0.16387 | 0.240244 | 0.499775 | 0.677795 | 0.222206 |
| tossup_correctness | category | Fine Arts | 1071 | 0.617082 | 0.678382 | 0.232727 | 0.239739 | 0.594771 | 0.766573 | -0.171802 | 0.185705 | 0.277392 | 0.552554 | 0.760051 | 0.214368 |
| tossup_correctness | category | Geography | 185 | 0.546512 | 0.761559 | 0.243024 | 0.280023 | 0.459459 | 0.697297 | -0.237838 | 0.155485 | 0.252114 | 0.459575 | 0.653387 | 0.223734 |
| tossup_correctness | category | History | 1440 | 0.597739 | 0.684601 | 0.232197 | 0.244006 | 0.586111 | 0.754167 | -0.168056 | 0.1646 | 0.300396 | 0.532997 | 0.734764 | 0.222335 |
| tossup_correctness | category | Literature | 1422 | 0.576706 | 0.632811 | 0.225765 | 0.218602 | 0.675809 | 0.814346 | -0.138537 | 0.175309 | 0.345156 | 0.612358 | 0.797981 | 0.21142 |
| tossup_correctness | category | Mythology | 318 | 0.562229 | 0.688767 | 0.244639 | 0.244209 | 0.613208 | 0.789308 | -0.176101 | 0.17739 | 0.293137 | 0.57138 | 0.76688 | 0.216538 |
| tossup_correctness | category | Other Academic | 66 | 0.697648 | 0.664339 | 0.239002 | 0.236028 | 0.651515 | 0.712121 | -0.0606061 | 0.163365 | 0.247289 | 0.512894 | 0.651052 | 0.22273 |
| tossup_correctness | category | Philosophy | 311 | 0.622818 | 0.649363 | 0.189474 | 0.22818 | 0.630225 | 0.745981 | -0.115756 | 0.18066 | 0.295455 | 0.567936 | 0.782342 | 0.214169 |
| tossup_correctness | category | Popular Culture | 102 | 0.503704 | 0.841645 | 0.428744 | 0.306813 | 0.5 | 0.882353 | -0.382353 | 0.175841 | 0.205197 | 0.49176 | 0.68072 | 0.218145 |
| tossup_correctness | category | Religion | 358 | 0.603807 | 0.684364 | 0.179087 | 0.242423 | 0.620112 | 0.712291 | -0.0921788 | 0.175115 | 0.318199 | 0.545235 | 0.754765 | 0.218232 |
| tossup_correctness | category | Science | 1433 | 0.630803 | 0.673739 | 0.217265 | 0.23839 | 0.61619 | 0.738311 | -0.122121 | 0.163694 | 0.291121 | 0.534466 | 0.722249 | 0.222761 |
| tossup_correctness | category | Social Science | 324 | 0.607546 | 0.680001 | 0.21568 | 0.242106 | 0.589506 | 0.731481 | -0.141975 | 0.161935 | 0.285603 | 0.546891 | 0.726037 | 0.223343 |
| tossup_correctness | category | Unknown | 1937 | 0.608295 | 0.668265 | 0.205605 | 0.234972 | 0.63397 | 0.758389 | -0.124419 | 0.183806 | 0.291426 | 0.572049 | 0.781552 | 0.213386 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.550595 | 0.784431 | 0.265256 | 0.287925 | 0.467066 | 0.712575 | -0.245509 | 0.163533 | 0.204354 | 0.468658 | 0.653293 | 0.220482 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.608249 | 0.746524 | 0.259549 | 0.269301 | 0.524123 | 0.729167 | -0.205044 | 0.173866 | 0.226751 | 0.475256 | 0.683315 | 0.218848 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.621608 | 0.695745 | 0.243495 | 0.247005 | 0.595745 | 0.755083 | -0.159338 | 0.173624 | 0.266161 | 0.529121 | 0.726571 | 0.219706 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.603129 | 0.670346 | 0.236576 | 0.23619 | 0.627286 | 0.780942 | -0.153657 | 0.174242 | 0.30312 | 0.562248 | 0.761217 | 0.217643 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.603353 | 0.633552 | 0.181229 | 0.221152 | 0.655319 | 0.762029 | -0.10671 | 0.170335 | 0.343019 | 0.597871 | 0.792592 | 0.214457 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | 0.580361 | 1.16835 | -3.31595 | -1.16853 | -0.193904 | 0.370815 | 1.3931 | 2.63749 | 3.99706 |
| player | theta_2 | 1167 | 0.0607813 | 0.959602 | -3.07188 | -1.33232 | -0.457607 | -0.0655575 | 0.539262 | 1.76912 | 3.67586 |
| player | theta_3 | 1167 | 0.594863 | 1.28417 | -3.06407 | -1.2865 | -0.378436 | 0.407503 | 1.62225 | 2.76359 | 3.943 |
| player | theta_norm | 1167 | 1.92339 | 0.962971 | 0.089533 | 0.522237 | 1.13911 | 1.86762 | 2.609 | 3.57681 | 4.88832 |
| tossup | start_difficulty_d1 | 1220 | 1.64903 | 0.906358 | -0.972926 | 0.0876553 | 0.884644 | 1.93402 | 2.30529 | 2.91999 | 4.01934 |
| tossup | start_difficulty_d2 | 1220 | 0.971303 | 0.685677 | -1.19761 | -0.134775 | 0.493828 | 0.990618 | 1.43137 | 2.07343 | 2.84519 |
| tossup | start_difficulty_d3 | 1220 | 1.09816 | 1.03967 | -1.09121 | -0.45826 | 0.351951 | 0.866441 | 1.92866 | 2.86107 | 3.98594 |
| tossup | end_difficulty_d1 | 1220 | 0.432912 | 0.762054 | -2.48926 | -1.03031 | -0.0367832 | 0.619681 | 0.911762 | 1.47899 | 2.57282 |
| tossup | end_difficulty_d2 | 1220 | -0.111489 | 0.657002 | -2.82367 | -1.23112 | -0.534148 | -0.045936 | 0.296122 | 0.923412 | 2.16422 |
| tossup | end_difficulty_d3 | 1220 | -0.00187764 | 0.92013 | -3.84164 | -1.5117 | -0.616893 | -0.0476661 | 0.717877 | 1.40273 | 2.89684 |
| tossup | total_drop_d1 | 1220 | 1.21612 | 0.444056 | 0.586158 | 0.714907 | 0.850172 | 1.10402 | 1.51671 | 2.01643 | 4.32029 |
| tossup | total_drop_d2 | 1220 | 1.08279 | 0.38391 | 0.509286 | 0.739952 | 0.857669 | 0.958682 | 1.19034 | 1.80391 | 3.79459 |
| tossup | total_drop_d3 | 1220 | 1.10004 | 0.449806 | 0.594487 | 0.74067 | 0.846262 | 0.931295 | 1.12136 | 2.0853 | 3.90079 |
| tossup | drop_share_1_d1 | 1220 | 0.205077 | 0.0859162 | 0.0395923 | 0.0805517 | 0.124168 | 0.21926 | 0.276155 | 0.306145 | 0.685631 |
| tossup | drop_share_2_d1 | 1220 | 0.274309 | 0.0957316 | 0.0491275 | 0.107603 | 0.192168 | 0.311407 | 0.338698 | 0.37235 | 0.640027 |
| tossup | drop_share_3_d1 | 1220 | 0.520614 | 0.160231 | 0.145274 | 0.350259 | 0.385061 | 0.461315 | 0.668896 | 0.806134 | 0.907222 |
| tossup | drop_share_1_d2 | 1220 | 0.230139 | 0.0736875 | 0.0468499 | 0.0995595 | 0.161457 | 0.261404 | 0.287615 | 0.308729 | 0.497949 |
| tossup | drop_share_2_d2 | 1220 | 0.292977 | 0.0813129 | 0.0577335 | 0.130482 | 0.241283 | 0.332244 | 0.34653 | 0.36392 | 0.545094 |
| tossup | drop_share_3_d2 | 1220 | 0.476884 | 0.146294 | 0.159113 | 0.34604 | 0.36872 | 0.398698 | 0.590049 | 0.761493 | 0.889193 |
| tossup | drop_share_1_d3 | 1220 | 0.256771 | 0.0735392 | 0.0489988 | 0.0949931 | 0.238771 | 0.284017 | 0.297256 | 0.314981 | 0.593828 |
| tossup | drop_share_2_d3 | 1220 | 0.320001 | 0.0734306 | 0.0505033 | 0.146072 | 0.322198 | 0.338688 | 0.348927 | 0.373349 | 0.725736 |
| tossup | drop_share_3_d3 | 1220 | 0.423227 | 0.124589 | 0.0880455 | 0.337851 | 0.358027 | 0.373957 | 0.421638 | 0.756933 | 0.895882 |
| tossup | r_1 | 1220 | 0.471299 | 0.312165 | 0.017202 | 0.0348952 | 0.14112 | 0.506461 | 0.765323 | 0.917474 | 0.960031 |
| tossup | r_2 | 1220 | 0.247213 | 0.230623 | 0.0115906 | 0.0244316 | 0.0586815 | 0.152751 | 0.407286 | 0.723707 | 0.898658 |
| tossup | r_3 | 1220 | 0.281488 | 0.290903 | 0.0192846 | 0.0355403 | 0.0682109 | 0.138588 | 0.418323 | 0.887785 | 0.950023 |
| tossup | r_norm | 1220 | 0.766799 | 0.0978053 | 0.578987 | 0.617186 | 0.684124 | 0.756964 | 0.852306 | 0.924428 | 0.960453 |
