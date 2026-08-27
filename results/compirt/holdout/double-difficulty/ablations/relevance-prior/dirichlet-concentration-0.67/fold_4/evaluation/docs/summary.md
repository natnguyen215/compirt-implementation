# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283111 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.726087 |
| log_loss | 0.474514 |
| ece | 0.0141577 |
| brier | 0.153163 |
| accuracy | 0.78932 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0159655 |
| probability_std | 0.140561 |
| probability_p10 | 0.578359 |
| probability_p50 | 0.808084 |
| probability_p90 | 0.915969 |
| mean_predictive_variance | 0.15586 |
| integrated_brier_score | 0.100821 |
| joint_tossup_event_log_loss | 6.60942 |
| buzz_position_mae | 0.148556 |
| buzz_position_median_absolute_error | 0.130829 |
| buzz_position_bias | -0.0366861 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.34822 |
| first_buzzer_mean_reciprocal_rank | 0.560576 |
| first_buzzer_log_loss | 1.68958 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.726087 |
| neg_average_precision | 0.458566 |
| neg_precision | 0.642857 |
| neg_recall | 0.158496 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.194576 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0139921 |
| no_buzz_calibration_error | 0.00226502 |
| no_buzz_brier | 0.0111463 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.726087 | 0.474514 | 0.0141577 | 0.153163 | 0.78932 | 0.773355 | 0.0159655 | 0.140561 | 0.578359 | 0.808084 | 0.915969 | 0.15586 |
| tossup_correctness | tier | fall | 2876 | 0.729175 | 0.451514 | 0.0152334 | 0.144006 | 0.805981 | 0.793115 | 0.0128651 | 0.138669 | 0.584544 | 0.819587 | 0.924614 | 0.150287 |
| tossup_correctness | tier | nationals | 1579 | 0.72069 | 0.522718 | 0.0363304 | 0.172954 | 0.746675 | 0.729576 | 0.0170994 | 0.14951 | 0.556995 | 0.797839 | 0.909765 | 0.160028 |
| tossup_correctness | tier | regionals | 1990 | 0.732378 | 0.479816 | 0.0271046 | 0.155696 | 0.78593 | 0.765829 | 0.0201005 | 0.139374 | 0.571016 | 0.796807 | 0.908437 | 0.161299 |
| tossup_correctness | tier | winter | 2825 | 0.718572 | 0.467252 | 0.0190732 | 0.149639 | 0.798584 | 0.783009 | 0.0155752 | 0.137095 | 0.589365 | 0.809491 | 0.915093 | 0.155371 |
| tossup_correctness | category | Current Events | 123 | 0.760088 | 0.46694 | 0.0503409 | 0.151918 | 0.772358 | 0.764228 | 0.00813008 | 0.135332 | 0.559561 | 0.749614 | 0.912022 | 0.17381 |
| tossup_correctness | category | Fine Arts | 1093 | 0.73911 | 0.468601 | 0.0185504 | 0.150375 | 0.795059 | 0.769442 | 0.0256176 | 0.143054 | 0.584865 | 0.82014 | 0.918829 | 0.151939 |
| tossup_correctness | category | Geography | 191 | 0.794299 | 0.490889 | 0.0720128 | 0.159661 | 0.769634 | 0.691099 | 0.078534 | 0.200719 | 0.444271 | 0.770379 | 0.895143 | 0.169325 |
| tossup_correctness | category | History | 1469 | 0.720856 | 0.497028 | 0.0287406 | 0.163322 | 0.769912 | 0.758339 | 0.0115725 | 0.142755 | 0.567835 | 0.807898 | 0.919481 | 0.155774 |
| tossup_correctness | category | Literature | 1436 | 0.713407 | 0.433129 | 0.0180985 | 0.135883 | 0.816852 | 0.81546 | 0.00139276 | 0.118578 | 0.65202 | 0.842604 | 0.926471 | 0.139956 |
| tossup_correctness | category | Mythology | 325 | 0.688421 | 0.4128 | 0.065642 | 0.127328 | 0.836923 | 0.843077 | -0.00615385 | 0.102039 | 0.663929 | 0.819959 | 0.912877 | 0.14824 |
| tossup_correctness | category | Other Academic | 67 | 0.668464 | 0.488804 | 0.0612636 | 0.158029 | 0.80597 | 0.791045 | 0.0149254 | 0.134888 | 0.582084 | 0.772014 | 0.889066 | 0.17246 |
| tossup_correctness | category | Philosophy | 322 | 0.681961 | 0.488146 | 0.0377043 | 0.159325 | 0.770186 | 0.785714 | -0.015528 | 0.12606 | 0.609175 | 0.810676 | 0.931228 | 0.151619 |
| tossup_correctness | category | Popular Culture | 100 | 0.52094 | 0.365973 | 0.0638447 | 0.105497 | 0.89 | 0.89 | 0 | 0.0658301 | 0.760045 | 0.851784 | 0.919225 | 0.12814 |
| tossup_correctness | category | Religion | 365 | 0.669217 | 0.555925 | 0.0518825 | 0.185879 | 0.745205 | 0.723288 | 0.0219178 | 0.143651 | 0.548947 | 0.784886 | 0.9121 | 0.164044 |
| tossup_correctness | category | Science | 1456 | 0.726802 | 0.480679 | 0.0220482 | 0.155381 | 0.785027 | 0.76717 | 0.0178571 | 0.144966 | 0.559608 | 0.793835 | 0.905355 | 0.162529 |
| tossup_correctness | category | Social Science | 333 | 0.746456 | 0.495374 | 0.0376868 | 0.16065 | 0.780781 | 0.72973 | 0.0510511 | 0.161063 | 0.484737 | 0.780394 | 0.909074 | 0.169218 |
| tossup_correctness | category | Unknown | 1990 | 0.732378 | 0.479816 | 0.0271046 | 0.155696 | 0.78593 | 0.765829 | 0.0201005 | 0.139374 | 0.571016 | 0.796807 | 0.908437 | 0.161299 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.762521 | 0.48563 | 0.0619365 | 0.158861 | 0.759777 | 0.748603 | 0.0111732 | 0.149604 | 0.516922 | 0.769606 | 0.875713 | 0.176272 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.702004 | 0.502867 | 0.0248916 | 0.164085 | 0.777429 | 0.754441 | 0.0229885 | 0.141217 | 0.547301 | 0.780252 | 0.900739 | 0.166839 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.724822 | 0.483077 | 0.0283452 | 0.156891 | 0.783931 | 0.766682 | 0.0172492 | 0.139135 | 0.582501 | 0.805215 | 0.913808 | 0.157522 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.715663 | 0.46232 | 0.0172404 | 0.147799 | 0.803224 | 0.787441 | 0.0157824 | 0.130737 | 0.615237 | 0.819044 | 0.918735 | 0.15034 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.740116 | 0.470562 | 0.0174515 | 0.151907 | 0.784964 | 0.771758 | 0.0132069 | 0.148383 | 0.549917 | 0.809945 | 0.91973 | 0.155391 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.65729 | 0.73633 | 0.390381 | 1.43614 | 2.16201 | 2.65497 | 3.13784 | 3.93169 | 4.63132 |
| player | theta_1 | 1196 | -1.20168 | 0.858003 | -3.60958 | -2.51945 | -1.77481 | -1.28648 | -0.712048 | 0.35044 | 2.06411 |
| player | theta_2 | 1196 | -0.980415 | 0.634831 | -3.28226 | -2.05952 | -1.3576 | -0.982708 | -0.570673 | 0.0364605 | 1.33213 |
| player | theta_3 | 1196 | -1.10155 | 0.76102 | -3.23112 | -2.30784 | -1.57766 | -1.15757 | -0.653976 | 0.28138 | 2.05248 |
| player | theta_norm | 1196 | 2.22676 | 0.614356 | 0.577204 | 1.30192 | 1.7958 | 2.17138 | 2.61867 | 3.29309 | 4.21807 |
| tossup | start_difficulty_d1 | 1240 | -1.76166 | 0.543794 | -3.41843 | -2.52658 | -2.13109 | -1.80878 | -1.46062 | -0.774148 | 1.43298 |
| tossup | start_difficulty_d2 | 1240 | -1.7522 | 0.500644 | -3.32853 | -2.50141 | -2.11304 | -1.77854 | -1.44165 | -0.832969 | -0.146926 |
| tossup | start_difficulty_d3 | 1240 | -1.75147 | 0.508094 | -3.55648 | -2.52441 | -2.11666 | -1.78384 | -1.42446 | -0.868488 | 0.670871 |
| tossup | end_difficulty_d1 | 1240 | -2.74857 | 0.632712 | -4.6054 | -3.64197 | -3.19394 | -2.81401 | -2.39539 | -1.64207 | 0.73975 |
| tossup | end_difficulty_d2 | 1240 | -2.73724 | 0.586787 | -4.59537 | -3.62285 | -3.14994 | -2.75187 | -2.36937 | -1.69791 | -0.853128 |
| tossup | end_difficulty_d3 | 1240 | -2.73555 | 0.591449 | -4.85457 | -3.64864 | -3.15769 | -2.77118 | -2.34834 | -1.70423 | 0.00247008 |
| tossup | total_drop_d1 | 1240 | 0.986906 | 0.110586 | 0.588106 | 0.798103 | 0.912112 | 0.991871 | 1.06216 | 1.16414 | 1.37342 |
| tossup | total_drop_d2 | 1240 | 0.985048 | 0.103492 | 0.640766 | 0.816463 | 0.916994 | 0.984354 | 1.05166 | 1.15763 | 1.35558 |
| tossup | total_drop_d3 | 1240 | 0.984081 | 0.10367 | 0.668401 | 0.819116 | 0.912361 | 0.984303 | 1.05385 | 1.15873 | 1.46629 |
| tossup | drop_share_1_d1 | 1240 | 0.248975 | 0.0317604 | 0.100513 | 0.195397 | 0.230275 | 0.249816 | 0.268216 | 0.297847 | 0.375634 |
| tossup | drop_share_2_d1 | 1240 | 0.372554 | 0.022108 | 0.293046 | 0.33626 | 0.358986 | 0.373734 | 0.387195 | 0.405688 | 0.480046 |
| tossup | drop_share_3_d1 | 1240 | 0.378471 | 0.040352 | 0.251096 | 0.316217 | 0.350745 | 0.376295 | 0.401233 | 0.447256 | 0.606441 |
| tossup | drop_share_1_d2 | 1240 | 0.248049 | 0.0291967 | 0.129183 | 0.198903 | 0.230446 | 0.247828 | 0.268103 | 0.295815 | 0.356227 |
| tossup | drop_share_2_d2 | 1240 | 0.371886 | 0.0205785 | 0.299657 | 0.338981 | 0.35877 | 0.372574 | 0.385533 | 0.40393 | 0.447052 |
| tossup | drop_share_3_d2 | 1240 | 0.380065 | 0.0368457 | 0.26083 | 0.323228 | 0.355806 | 0.380428 | 0.401105 | 0.444769 | 0.535193 |
| tossup | drop_share_1_d3 | 1240 | 0.247813 | 0.0305312 | 0.124842 | 0.197521 | 0.229155 | 0.247562 | 0.267713 | 0.295431 | 0.413566 |
| tossup | drop_share_2_d3 | 1240 | 0.372252 | 0.021013 | 0.267399 | 0.33743 | 0.359044 | 0.372421 | 0.385891 | 0.404904 | 0.470501 |
| tossup | drop_share_3_d3 | 1240 | 0.379935 | 0.038196 | 0.258761 | 0.323496 | 0.35368 | 0.377594 | 0.401705 | 0.445447 | 0.591001 |
| tossup | r_1 | 1240 | 0.321649 | 0.145844 | 0.0578984 | 0.127443 | 0.212658 | 0.295069 | 0.410913 | 0.605742 | 0.858879 |
| tossup | r_2 | 1240 | 0.335802 | 0.112833 | 0.0573212 | 0.163467 | 0.258734 | 0.330857 | 0.402506 | 0.533279 | 0.829888 |
| tossup | r_3 | 1240 | 0.342549 | 0.124132 | 0.0741661 | 0.160133 | 0.25436 | 0.331541 | 0.412577 | 0.561919 | 0.845881 |
| tossup | r_norm | 1240 | 0.617335 | 0.0427902 | 0.577361 | 0.579411 | 0.588059 | 0.603962 | 0.630896 | 0.704963 | 0.864672 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.4244 | 0.480875 | 2.08276 | 3.70215 | 4.15989 | 4.38793 | 4.64406 | 5.34365 | 6.29403 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.40834 | 0.423328 | 2.22289 | 3.74995 | 4.17967 | 4.38869 | 4.59926 | 5.11118 | 6.67459 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.41263 | 0.424148 | 2.50284 | 3.74471 | 4.17824 | 4.38907 | 4.63767 | 5.10446 | 6.36415 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.66653 | 2.44778 | -12.0413 | -3.52292 | 0.534773 | 2.88373 | 3.28617 | 3.61167 | 4.19281 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.18024 | 2.19433 | -10.2408 | -2.89103 | 2.3728 | 3.10482 | 3.35564 | 3.65177 | 4.25188 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.07771 | 2.19682 | -11.6481 | -2.65128 | 1.83651 | 3.04126 | 3.33747 | 3.67513 | 4.16564 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.75787 | 2.59217 | 0.875491 | 0.980316 | 1.05304 | 1.28892 | 4.12416 | 8.09306 | 16.7641 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.22809 | 2.34799 | 0.890682 | 0.962464 | 1.02256 | 1.14905 | 1.83125 | 7.55374 | 15.0015 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.33493 | 2.31301 | 0.846539 | 0.96949 | 1.02539 | 1.18426 | 2.46237 | 7.21017 | 15.9934 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.159283 | 0.082165 | 0.0126956 | 0.0312124 | 0.0872605 | 0.176011 | 0.214299 | 0.270997 | 0.631542 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.328874 | 0.125833 | 0.0184367 | 0.0801183 | 0.291827 | 0.344754 | 0.378038 | 0.523243 | 0.830877 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.511844 | 0.175656 | 0.056703 | 0.27482 | 0.401422 | 0.469646 | 0.580438 | 0.885431 | 0.96749 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.174664 | 0.0757246 | 0.0112121 | 0.0358253 | 0.131256 | 0.189487 | 0.223405 | 0.271447 | 0.766726 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.336558 | 0.103291 | 0.0215558 | 0.123851 | 0.309088 | 0.343733 | 0.377804 | 0.479752 | 0.847812 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.488778 | 0.147635 | 0.0458097 | 0.315608 | 0.404396 | 0.454236 | 0.534238 | 0.830894 | 0.963658 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.168792 | 0.0739191 | 0.013158 | 0.0351578 | 0.116949 | 0.183962 | 0.220254 | 0.261509 | 0.608557 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.338085 | 0.108238 | 0.0318501 | 0.11417 | 0.304928 | 0.342733 | 0.377154 | 0.526733 | 0.857103 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.493123 | 0.151007 | 0.0321317 | 0.30851 | 0.406736 | 0.4582 | 0.541598 | 0.839928 | 0.954887 |
| tossup_hazard | hazard_r_1 | 1240 | 0.382253 | 0.27668 | 0.0306852 | 0.0627037 | 0.139014 | 0.288292 | 0.611968 | 0.872318 | 0.950027 |
| tossup_hazard | hazard_r_2 | 1240 | 0.289447 | 0.207439 | 0.0220435 | 0.0542182 | 0.121352 | 0.225228 | 0.434899 | 0.701685 | 0.867909 |
| tossup_hazard | hazard_r_3 | 1240 | 0.3283 | 0.24299 | 0.0234608 | 0.0498748 | 0.122627 | 0.245031 | 0.528877 | 0.775691 | 0.925815 |
