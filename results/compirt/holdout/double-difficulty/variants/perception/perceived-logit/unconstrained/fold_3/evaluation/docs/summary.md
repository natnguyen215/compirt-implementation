# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/unconstrained/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/unconstrained/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 336427 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.546423 |
| log_loss | 0.603306 |
| ece | 0.103786 |
| brier | 0.188603 |
| accuracy | 0.769163 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000881057 |
| probability_std | 0.0972724 |
| probability_p10 | 0.722096 |
| probability_p50 | 0.893828 |
| probability_p90 | 0.953147 |
| mean_predictive_variance | 0.108212 |
| integrated_brier_score | 0.176747 |
| joint_tossup_event_log_loss | 7.77171 |
| buzz_position_mae | 0.342914 |
| buzz_position_median_absolute_error | 0.344309 |
| buzz_position_bias | -0.330095 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.347907 |
| first_buzzer_mean_reciprocal_rank | 0.562802 |
| first_buzzer_log_loss | 1.6774 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.546423 |
| neg_average_precision | 0.271995 |
| neg_precision | 0.425926 |
| neg_recall | 0.0110153 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0284681 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.230545 |
| no_buzz_calibration_error | 0.21536 |
| no_buzz_brier | 0.0703191 |
| full_pmf_max_mass_error | 1.11022e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.546423 | 0.603306 | 0.103786 | 0.188603 | 0.769163 | 0.770044 | -0.000881057 | 0.0972724 | 0.722096 | 0.893828 | 0.953147 | 0.108212 |
| tossup_correctness | tier | fall | 2817 | 0.549521 | 0.571625 | 0.0950134 | 0.180301 | 0.779198 | 0.781683 | -0.00248491 | 0.0893954 | 0.735824 | 0.888743 | 0.943283 | 0.112214 |
| tossup_correctness | tier | nationals | 1542 | 0.600013 | 0.622359 | 0.102047 | 0.201693 | 0.734112 | 0.73476 | -0.000648508 | 0.119953 | 0.644188 | 0.864635 | 0.953381 | 0.12735 |
| tossup_correctness | tier | regionals | 1934 | 0.531553 | 0.647321 | 0.126248 | 0.200985 | 0.756463 | 0.75698 | -0.000517063 | 0.107222 | 0.689243 | 0.899312 | 0.959395 | 0.107174 |
| tossup_correctness | tier | winter | 2787 | 0.510514 | 0.594243 | 0.106435 | 0.181161 | 0.787226 | 0.786868 | 0.000358809 | 0.0746132 | 0.792962 | 0.907729 | 0.955817 | 0.0942983 |
| tossup_correctness | category | Current Events | 125 | 0.616093 | 0.653665 | 0.141257 | 0.220517 | 0.712 | 0.704 | 0.008 | 0.0981359 | 0.663902 | 0.868541 | 0.917823 | 0.13013 |
| tossup_correctness | category | Fine Arts | 1072 | 0.557459 | 0.610037 | 0.12537 | 0.191116 | 0.770522 | 0.770522 | 0 | 0.085677 | 0.752815 | 0.90862 | 0.955025 | 0.0994799 |
| tossup_correctness | category | Geography | 185 | 0.601259 | 0.675963 | 0.151941 | 0.220703 | 0.713514 | 0.702703 | 0.0108108 | 0.0965209 | 0.741912 | 0.879883 | 0.938652 | 0.114912 |
| tossup_correctness | category | History | 1443 | 0.557306 | 0.592842 | 0.0857753 | 0.187979 | 0.763687 | 0.765073 | -0.001386 | 0.0998976 | 0.694492 | 0.873555 | 0.945159 | 0.120171 |
| tossup_correctness | category | Literature | 1411 | 0.511067 | 0.541007 | 0.0828903 | 0.161926 | 0.810773 | 0.81219 | -0.00141743 | 0.0874451 | 0.767191 | 0.904797 | 0.957316 | 0.0991627 |
| tossup_correctness | category | Mythology | 320 | 0.52917 | 0.557734 | 0.090219 | 0.171806 | 0.790625 | 0.79375 | -0.003125 | 0.0926057 | 0.732024 | 0.903269 | 0.946346 | 0.10394 |
| tossup_correctness | category | Other Academic | 64 | 0.589844 | 0.62879 | 0.17918 | 0.207091 | 0.75 | 0.75 | 0 | 0.105221 | 0.696609 | 0.875283 | 0.950348 | 0.11927 |
| tossup_correctness | category | Philosophy | 312 | 0.522258 | 0.556271 | 0.111716 | 0.168296 | 0.801282 | 0.801282 | 0 | 0.0834866 | 0.773225 | 0.906791 | 0.957822 | 0.0969362 |
| tossup_correctness | category | Popular Culture | 104 | 0.536222 | 0.455017 | 0.0639107 | 0.137973 | 0.836538 | 0.846154 | -0.00961538 | 0.0868142 | 0.763101 | 0.894525 | 0.94117 | 0.106804 |
| tossup_correctness | category | Religion | 358 | 0.540424 | 0.701235 | 0.165729 | 0.222271 | 0.72067 | 0.726257 | -0.00558659 | 0.102285 | 0.722674 | 0.906663 | 0.953482 | 0.104659 |
| tossup_correctness | category | Science | 1431 | 0.575212 | 0.587004 | 0.0919131 | 0.186823 | 0.765898 | 0.765199 | 0.000698812 | 0.0973378 | 0.724705 | 0.883514 | 0.944724 | 0.114657 |
| tossup_correctness | category | Social Science | 321 | 0.508368 | 0.672618 | 0.147338 | 0.214347 | 0.735202 | 0.744548 | -0.00934579 | 0.0897124 | 0.75216 | 0.893744 | 0.94527 | 0.105947 |
| tossup_correctness | category | Unknown | 1934 | 0.531553 | 0.647321 | 0.126248 | 0.200985 | 0.756463 | 0.75698 | -0.000517063 | 0.107222 | 0.689243 | 0.899312 | 0.959395 | 0.107174 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.501287 | 0.709805 | 0.178072 | 0.233505 | 0.697917 | 0.697917 | 0 | 0.0906086 | 0.687388 | 0.856233 | 0.926777 | 0.132918 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.537603 | 0.644684 | 0.105149 | 0.209025 | 0.728909 | 0.733408 | -0.00449944 | 0.102168 | 0.687235 | 0.860288 | 0.934515 | 0.128696 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.502793 | 0.628736 | 0.107697 | 0.198275 | 0.757466 | 0.759276 | -0.00180995 | 0.0955916 | 0.721152 | 0.879577 | 0.942637 | 0.117026 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.557785 | 0.56039 | 0.0920796 | 0.174136 | 0.788777 | 0.789125 | -0.000348554 | 0.0949992 | 0.725625 | 0.894353 | 0.951661 | 0.107207 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.565002 | 0.606626 | 0.1136 | 0.186329 | 0.775685 | 0.775342 | 0.000342466 | 0.0953943 | 0.749076 | 0.915343 | 0.961314 | 0.0946674 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | -1.39651 | 0.692611 | -3.00883 | -2.31229 | -1.82034 | -1.47083 | -1.10725 | -0.262374 | 2.20011 |
| player | beta | 1133 | -3.25389 | 1.0957 | -6.88806 | -5.60183 | -3.77128 | -3.02964 | -2.42683 | -1.9548 | -1.5723 |
| player | theta_1 | 1133 | 0.890766 | 0.866508 | -2.29056 | -0.735689 | 0.406785 | 0.985914 | 1.5099 | 2.11383 | 2.79312 |
| player | theta_2 | 1133 | 0.887136 | 0.970514 | -2.71094 | -0.773726 | 0.255395 | 1.02015 | 1.56903 | 2.3147 | 3.98212 |
| player | theta_3 | 1133 | 0.872316 | 0.844522 | -2.19117 | -0.734294 | 0.333935 | 0.967989 | 1.46795 | 2.06722 | 3.14027 |
| player | theta_norm | 1133 | 2.08044 | 0.646055 | 0.327411 | 0.968743 | 1.62326 | 2.14023 | 2.5535 | 3.03911 | 4.5512 |
| tossup | start_difficulty_d1 | 1240 | -1.01061 | 0.459117 | -2.2304 | -1.78711 | -1.3681 | -0.989845 | -0.604474 | -0.342268 | -0.101589 |
| tossup | start_difficulty_d2 | 1240 | -0.993052 | 0.435939 | -2.06766 | -1.6815 | -1.33559 | -1.00804 | -0.611758 | -0.315966 | -0.119861 |
| tossup | start_difficulty_d3 | 1240 | -0.954703 | 0.396389 | -2.04908 | -1.65046 | -1.24284 | -0.928851 | -0.642792 | -0.363682 | -0.174204 |
| tossup | end_difficulty_d1 | 1240 | -1.67969 | 0.392866 | -3.05212 | -2.35243 | -1.97805 | -1.62663 | -1.35072 | -1.12758 | -0.969359 |
| tossup | end_difficulty_d2 | 1240 | -1.66628 | 0.376636 | -2.80238 | -2.30205 | -1.94282 | -1.65817 | -1.34605 | -1.1167 | -0.932005 |
| tossup | end_difficulty_d3 | 1240 | -1.64117 | 0.34761 | -2.78451 | -2.28065 | -1.85818 | -1.60953 | -1.38317 | -1.14132 | -0.93441 |
| tossup | total_drop_d1 | 1240 | 0.669082 | 0.190849 | 0.228216 | 0.321634 | 0.530088 | 0.704828 | 0.810348 | 0.928807 | 1.24619 |
| tossup | total_drop_d2 | 1240 | 0.673228 | 0.180882 | 0.23965 | 0.336127 | 0.549839 | 0.700346 | 0.807969 | 0.91602 | 1.2125 |
| tossup | total_drop_d3 | 1240 | 0.686467 | 0.182916 | 0.245975 | 0.341865 | 0.564118 | 0.720612 | 0.823254 | 0.946263 | 1.1698 |
| tossup | drop_share_1_d1 | 1240 | 0.326039 | 0.0281965 | 0.189733 | 0.284666 | 0.309644 | 0.323035 | 0.339526 | 0.374868 | 0.454855 |
| tossup | drop_share_2_d1 | 1240 | 0.322796 | 0.0174307 | 0.257643 | 0.290535 | 0.312191 | 0.325626 | 0.33505 | 0.346086 | 0.367992 |
| tossup | drop_share_3_d1 | 1240 | 0.351165 | 0.0299998 | 0.246772 | 0.307999 | 0.333623 | 0.348313 | 0.365532 | 0.402199 | 0.5495 |
| tossup | drop_share_1_d2 | 1240 | 0.321536 | 0.0246082 | 0.222076 | 0.280098 | 0.309028 | 0.322292 | 0.334795 | 0.361312 | 0.420423 |
| tossup | drop_share_2_d2 | 1240 | 0.322879 | 0.0185036 | 0.252207 | 0.287408 | 0.313462 | 0.326668 | 0.33555 | 0.346724 | 0.368759 |
| tossup | drop_share_3_d2 | 1240 | 0.355586 | 0.0318615 | 0.264271 | 0.31667 | 0.33553 | 0.349333 | 0.369473 | 0.423517 | 0.508946 |
| tossup | drop_share_1_d3 | 1240 | 0.322626 | 0.0261548 | 0.199504 | 0.280498 | 0.309584 | 0.322387 | 0.336548 | 0.364867 | 0.435567 |
| tossup | drop_share_2_d3 | 1240 | 0.323754 | 0.018156 | 0.258584 | 0.288415 | 0.313438 | 0.327462 | 0.336684 | 0.347865 | 0.368069 |
| tossup | drop_share_3_d3 | 1240 | 0.35362 | 0.0328894 | 0.262863 | 0.312388 | 0.333771 | 0.347923 | 0.365375 | 0.419273 | 0.513975 |
| tossup | r_1 | 1240 | 0.334352 | 0.23124 | 0.0308594 | 0.0711537 | 0.137006 | 0.264484 | 0.493534 | 0.811347 | 0.918736 |
| tossup | r_2 | 1240 | 0.354528 | 0.251339 | 0.0331916 | 0.0667246 | 0.139194 | 0.281951 | 0.571262 | 0.81948 | 0.924765 |
| tossup | r_3 | 1240 | 0.31112 | 0.21454 | 0.0335985 | 0.0658215 | 0.140409 | 0.246189 | 0.443362 | 0.74406 | 0.884206 |
| tossup | r_norm | 1240 | 0.699295 | 0.0883683 | 0.577395 | 0.584937 | 0.626324 | 0.680072 | 0.763655 | 0.864891 | 0.926343 |
