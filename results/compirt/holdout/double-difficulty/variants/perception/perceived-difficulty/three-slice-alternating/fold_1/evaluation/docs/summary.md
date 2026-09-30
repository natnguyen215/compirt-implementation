# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 328342 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.587771 |
| log_loss | 0.736191 |
| ece | 0.277484 |
| brier | 0.265983 |
| accuracy | 0.552073 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.210052 |
| probability_std | 0.159887 |
| probability_p10 | 0.254427 |
| probability_p50 | 0.503028 |
| probability_p90 | 0.680026 |
| mean_predictive_variance | 0.2242 |
| integrated_brier_score | 0.0943879 |
| joint_tossup_event_log_loss | 6.88402 |
| buzz_position_mae | 0.138799 |
| buzz_position_median_absolute_error | 0.116143 |
| buzz_position_bias | -0.0055423 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.34774 |
| first_buzzer_mean_reciprocal_rank | 0.559448 |
| first_buzzer_log_loss | 1.69195 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.587771 |
| neg_average_precision | 0.299161 |
| neg_precision | 0.286258 |
| neg_recall | 0.591308 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.141334 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0497538 |
| no_buzz_calibration_error | 0.0338447 |
| no_buzz_brier | 0.0214899 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.587771 | 0.736191 | 0.277484 | 0.265983 | 0.552073 | 0.762125 | -0.210052 | 0.159887 | 0.254427 | 0.503028 | 0.680026 | 0.2242 |
| tossup_correctness | tier | fall | 2842 | 0.602403 | 0.751861 | 0.315472 | 0.273374 | 0.521464 | 0.785362 | -0.263899 | 0.156428 | 0.246938 | 0.479999 | 0.667805 | 0.224624 |
| tossup_correctness | tier | nationals | 1564 | 0.581193 | 0.675846 | 0.192488 | 0.240783 | 0.602941 | 0.718031 | -0.11509 | 0.137879 | 0.330807 | 0.54768 | 0.687419 | 0.230326 |
| tossup_correctness | tier | regionals | 1937 | 0.605355 | 0.714607 | 0.25799 | 0.2554 | 0.592153 | 0.758389 | -0.166236 | 0.163125 | 0.259255 | 0.528771 | 0.691139 | 0.22339 |
| tossup_correctness | tier | winter | 2750 | 0.584633 | 0.769518 | 0.301311 | 0.28013 | 0.526545 | 0.765818 | -0.239273 | 0.167193 | 0.222662 | 0.479804 | 0.672065 | 0.220849 |
| tossup_correctness | category | Current Events | 126 | 0.537504 | 0.832632 | 0.335042 | 0.308801 | 0.47619 | 0.769841 | -0.293651 | 0.157942 | 0.199304 | 0.44444 | 0.623015 | 0.220803 |
| tossup_correctness | category | Fine Arts | 1071 | 0.594675 | 0.752369 | 0.293291 | 0.272574 | 0.54155 | 0.766573 | -0.225023 | 0.169151 | 0.231654 | 0.495422 | 0.682102 | 0.220674 |
| tossup_correctness | category | Geography | 185 | 0.564922 | 0.789933 | 0.2715 | 0.29164 | 0.491892 | 0.697297 | -0.205405 | 0.157668 | 0.221038 | 0.432244 | 0.623912 | 0.220227 |
| tossup_correctness | category | History | 1440 | 0.579666 | 0.728704 | 0.267814 | 0.263811 | 0.536111 | 0.754167 | -0.218056 | 0.156465 | 0.264629 | 0.498445 | 0.685143 | 0.22539 |
| tossup_correctness | category | Literature | 1422 | 0.561466 | 0.726724 | 0.309416 | 0.261041 | 0.579466 | 0.814346 | -0.23488 | 0.156903 | 0.273324 | 0.526528 | 0.692282 | 0.225357 |
| tossup_correctness | category | Mythology | 318 | 0.559493 | 0.756263 | 0.307766 | 0.274765 | 0.540881 | 0.789308 | -0.248428 | 0.155729 | 0.264646 | 0.504165 | 0.663112 | 0.225408 |
| tossup_correctness | category | Other Academic | 66 | 0.707727 | 0.658547 | 0.236695 | 0.233548 | 0.606061 | 0.712121 | -0.106061 | 0.145184 | 0.296618 | 0.497169 | 0.655838 | 0.228437 |
| tossup_correctness | category | Philosophy | 311 | 0.601811 | 0.709822 | 0.246272 | 0.254763 | 0.565916 | 0.745981 | -0.180064 | 0.158363 | 0.278814 | 0.524935 | 0.694607 | 0.224921 |
| tossup_correctness | category | Popular Culture | 102 | 0.441667 | 0.960342 | 0.477167 | 0.362867 | 0.333333 | 0.882353 | -0.54902 | 0.158508 | 0.167815 | 0.418624 | 0.607158 | 0.215885 |
| tossup_correctness | category | Religion | 358 | 0.586065 | 0.722797 | 0.225037 | 0.260551 | 0.550279 | 0.712291 | -0.162011 | 0.159833 | 0.245816 | 0.50147 | 0.68877 | 0.224291 |
| tossup_correctness | category | Science | 1433 | 0.594813 | 0.749851 | 0.27556 | 0.272838 | 0.524075 | 0.738311 | -0.214236 | 0.151114 | 0.25718 | 0.473881 | 0.651037 | 0.225777 |
| tossup_correctness | category | Social Science | 324 | 0.597459 | 0.723616 | 0.250837 | 0.261439 | 0.54321 | 0.731481 | -0.188272 | 0.151324 | 0.25939 | 0.48679 | 0.667246 | 0.226726 |
| tossup_correctness | category | Unknown | 1937 | 0.605355 | 0.714607 | 0.25799 | 0.2554 | 0.592153 | 0.758389 | -0.166236 | 0.163125 | 0.259255 | 0.528771 | 0.691139 | 0.22339 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.566702 | 0.842761 | 0.32558 | 0.312115 | 0.45509 | 0.712575 | -0.257485 | 0.142565 | 0.179275 | 0.408692 | 0.560137 | 0.218952 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.576415 | 0.819166 | 0.318399 | 0.302443 | 0.447368 | 0.729167 | -0.281798 | 0.148174 | 0.206922 | 0.424232 | 0.597146 | 0.220705 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.618172 | 0.760146 | 0.301185 | 0.27593 | 0.530496 | 0.755083 | -0.224586 | 0.154182 | 0.228053 | 0.472279 | 0.641438 | 0.224172 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.575414 | 0.73862 | 0.292354 | 0.266988 | 0.554852 | 0.780942 | -0.22609 | 0.156337 | 0.257493 | 0.510175 | 0.673295 | 0.225429 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.583467 | 0.686749 | 0.234498 | 0.244755 | 0.600982 | 0.762029 | -0.161047 | 0.157594 | 0.293587 | 0.554573 | 0.715745 | 0.224406 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | 0.293381 | 0.958562 | -1.7492 | -1.24879 | -0.416949 | 0.274607 | 0.947026 | 1.94178 | 2.84205 |
| player | theta_2 | 1167 | 0.204272 | 0.85647 | -1.80019 | -1.18581 | -0.436842 | 0.216009 | 0.849946 | 1.56395 | 2.4901 |
| player | theta_3 | 1167 | 0.26639 | 0.906697 | -1.7149 | -1.1672 | -0.432357 | 0.246883 | 0.95102 | 1.78234 | 2.69269 |
| player | theta_norm | 1167 | 1.48266 | 0.687921 | 0.194351 | 0.497996 | 0.918552 | 1.42446 | 1.97197 | 2.66616 | 3.85391 |
| tossup | start_difficulty_d1 | 1220 | 1.62522 | 0.361617 | -0.0812604 | 0.994988 | 1.4417 | 1.66188 | 1.86194 | 2.14247 | 2.63294 |
| tossup | start_difficulty_d2 | 1220 | 1.57527 | 0.368031 | -0.0692525 | 0.907992 | 1.40226 | 1.61506 | 1.81101 | 2.07225 | 2.60603 |
| tossup | start_difficulty_d3 | 1220 | 1.54494 | 0.373827 | -0.188042 | 0.856375 | 1.35644 | 1.58379 | 1.79462 | 2.0764 | 2.78653 |
| tossup | end_difficulty_d1 | 1220 | 0.450946 | 0.424814 | -1.49532 | -0.247254 | 0.241554 | 0.483072 | 0.705086 | 1.05319 | 1.74986 |
| tossup | end_difficulty_d2 | 1220 | 0.274702 | 0.410476 | -1.94724 | -0.497395 | 0.0719207 | 0.316461 | 0.552711 | 0.852713 | 1.33698 |
| tossup | end_difficulty_d3 | 1220 | 0.456423 | 0.442731 | -1.97613 | -0.315624 | 0.212894 | 0.508898 | 0.749018 | 1.08109 | 1.67448 |
| tossup | total_drop_d1 | 1220 | 1.17427 | 0.397676 | 0.523133 | 0.717133 | 0.859887 | 1.07726 | 1.41299 | 1.92503 | 3.50133 |
| tossup | total_drop_d2 | 1220 | 1.30057 | 0.469808 | 0.444738 | 0.745775 | 0.93884 | 1.19538 | 1.58462 | 2.1354 | 4.13664 |
| tossup | total_drop_d3 | 1220 | 1.08852 | 0.358826 | 0.4475 | 0.707395 | 0.837422 | 0.973395 | 1.27049 | 1.80214 | 2.89012 |
| tossup | drop_share_1_d1 | 1220 | 0.201326 | 0.0616445 | 0.0601788 | 0.104064 | 0.154561 | 0.204992 | 0.245511 | 0.290953 | 0.502599 |
| tossup | drop_share_2_d1 | 1220 | 0.274301 | 0.0698389 | 0.0668113 | 0.139314 | 0.233327 | 0.287347 | 0.320672 | 0.365089 | 0.528639 |
| tossup | drop_share_3_d1 | 1220 | 0.524374 | 0.119472 | 0.205251 | 0.37297 | 0.430902 | 0.503416 | 0.604235 | 0.748246 | 0.858069 |
| tossup | drop_share_1_d2 | 1220 | 0.193837 | 0.0664155 | 0.0418878 | 0.0963509 | 0.139015 | 0.190879 | 0.246468 | 0.296238 | 0.489314 |
| tossup | drop_share_2_d2 | 1220 | 0.265332 | 0.073548 | 0.0621937 | 0.135024 | 0.206882 | 0.279188 | 0.322825 | 0.358021 | 0.561804 |
| tossup | drop_share_3_d2 | 1220 | 0.540831 | 0.130643 | 0.113404 | 0.364996 | 0.427354 | 0.528831 | 0.64942 | 0.763157 | 0.895918 |
| tossup | drop_share_1_d3 | 1220 | 0.216687 | 0.0540303 | 0.0502793 | 0.11863 | 0.183878 | 0.224965 | 0.254431 | 0.288936 | 0.443756 |
| tossup | drop_share_2_d3 | 1220 | 0.28792 | 0.0605909 | 0.0547851 | 0.161588 | 0.262484 | 0.303094 | 0.326328 | 0.355984 | 0.536386 |
| tossup | drop_share_3_d3 | 1220 | 0.495393 | 0.104578 | 0.249658 | 0.371539 | 0.421453 | 0.469774 | 0.543987 | 0.717847 | 0.894936 |
| tossup | r_1 | 1220 | 0.378538 | 0.205188 | 0.0286324 | 0.0787897 | 0.212925 | 0.351926 | 0.542497 | 0.738265 | 0.902317 |
| tossup | r_2 | 1220 | 0.337617 | 0.188587 | 0.0242794 | 0.0589914 | 0.181609 | 0.32206 | 0.487442 | 0.6625 | 0.797025 |
| tossup | r_3 | 1220 | 0.283845 | 0.158876 | 0.0318561 | 0.0708966 | 0.156457 | 0.263596 | 0.378186 | 0.591971 | 0.819584 |
| tossup | r_norm | 1220 | 0.66112 | 0.059936 | 0.577386 | 0.583819 | 0.613506 | 0.65192 | 0.697611 | 0.777664 | 0.905241 |
