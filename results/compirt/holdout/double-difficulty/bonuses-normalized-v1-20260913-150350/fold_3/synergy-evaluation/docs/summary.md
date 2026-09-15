# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/synergy-evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.53922 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.897054 |
| log_loss | 0.407488 |
| ece | 0.0216992 |
| brier | 0.129202 |
| part_accuracy | 0.816677 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.290992 |
| part_accuracy_macro_team | 0.819098 |
| part_accuracy_macro_bonus | 0.817182 |
| probability_std | 0.348319 |
| probability_p10 | 0.0567198 |
| probability_p50 | 0.557923 |
| probability_p90 | 0.965891 |
| mean_predictive_variance | 0.127482 |
| exact_acc | 0.529154 |
| ranked_probability_score | 0.113688 |
| bonus_total_score_log_loss | 1.00741 |
| ppb_mae | 1.72069 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25365 | 0.897054 | 0.407488 | 0.0216992 | 0.129202 | 0.816677 | 0.525685 | 0.290992 | 0.348319 | 0.0567198 | 0.557923 | 0.965891 | 0.127482 |
| bonus_part_correctness | tier | fall | 8094 | 0.884716 | 0.426342 | 0.0278915 | 0.135999 | 0.807018 | 0.595132 | 0.211885 | 0.345844 | 0.0744541 | 0.674975 | 0.977844 | 0.121512 |
| bonus_part_correctness | tier | nationals | 4125 | 0.894105 | 0.409815 | 0.023533 | 0.129445 | 0.818909 | 0.448485 | 0.370424 | 0.333576 | 0.0568145 | 0.424732 | 0.922256 | 0.137402 |
| bonus_part_correctness | tier | regionals | 5247 | 0.899465 | 0.402875 | 0.026903 | 0.127256 | 0.821041 | 0.481609 | 0.339432 | 0.3448 | 0.0398091 | 0.482373 | 0.946115 | 0.131067 |
| bonus_part_correctness | tier | winter | 7899 | 0.906207 | 0.390016 | 0.0238958 | 0.123402 | 0.822509 | 0.524117 | 0.298392 | 0.350045 | 0.0559963 | 0.553373 | 0.968005 | 0.126036 |
| bonus_part_correctness | category | Current Events | 243 | 0.88374 | 0.437587 | 0.059747 | 0.140006 | 0.798354 | 0.506173 | 0.292181 | 0.357162 | 0.0530086 | 0.551886 | 0.950415 | 0.122364 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.881357 | 0.437038 | 0.0396276 | 0.139331 | 0.805924 | 0.508682 | 0.297242 | 0.341906 | 0.0604841 | 0.541029 | 0.963854 | 0.13244 |
| bonus_part_correctness | category | Geography | 456 | 0.892114 | 0.402087 | 0.0371733 | 0.129598 | 0.815789 | 0.622807 | 0.192982 | 0.342652 | 0.076192 | 0.712988 | 0.969182 | 0.123342 |
| bonus_part_correctness | category | History | 4050 | 0.900296 | 0.3982 | 0.020787 | 0.126609 | 0.816543 | 0.565185 | 0.251358 | 0.348556 | 0.0628043 | 0.634842 | 0.970981 | 0.123625 |
| bonus_part_correctness | category | Literature | 4029 | 0.901937 | 0.398297 | 0.0196316 | 0.12502 | 0.824274 | 0.536113 | 0.288161 | 0.35044 | 0.0572895 | 0.523474 | 0.970278 | 0.126479 |
| bonus_part_correctness | category | Mythology | 936 | 0.892827 | 0.406358 | 0.0461641 | 0.130548 | 0.803419 | 0.619658 | 0.183761 | 0.315236 | 0.13167 | 0.714758 | 0.973914 | 0.132158 |
| bonus_part_correctness | category | Other Academic | 255 | 0.92843 | 0.342759 | 0.0389135 | 0.104734 | 0.843137 | 0.545098 | 0.298039 | 0.36418 | 0.0618026 | 0.657198 | 0.97187 | 0.113734 |
| bonus_part_correctness | category | Philosophy | 948 | 0.888191 | 0.418786 | 0.0217788 | 0.135868 | 0.804852 | 0.504219 | 0.300633 | 0.339233 | 0.0692536 | 0.487886 | 0.963249 | 0.134756 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.877121 | 0.449223 | 0.0694766 | 0.147971 | 0.775439 | 0.578947 | 0.196491 | 0.330646 | 0.113836 | 0.707231 | 0.980087 | 0.124864 |
| bonus_part_correctness | category | Religion | 1014 | 0.901531 | 0.401606 | 0.0383174 | 0.124802 | 0.835306 | 0.50789 | 0.327416 | 0.354181 | 0.0511196 | 0.546093 | 0.964986 | 0.123904 |
| bonus_part_correctness | category | Science | 4059 | 0.891455 | 0.419319 | 0.0237137 | 0.133118 | 0.810544 | 0.530426 | 0.280118 | 0.349541 | 0.0628204 | 0.574116 | 0.969247 | 0.125774 |
| bonus_part_correctness | category | Social Science | 906 | 0.918556 | 0.363454 | 0.0363826 | 0.114718 | 0.836645 | 0.471302 | 0.365342 | 0.360971 | 0.0367401 | 0.451524 | 0.970172 | 0.1197 |
| bonus_part_correctness | category | Unknown | 5247 | 0.899465 | 0.402875 | 0.026903 | 0.127256 | 0.821041 | 0.481609 | 0.339432 | 0.3448 | 0.0398091 | 0.482373 | 0.946115 | 0.131067 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.195889 | 1.21047 | -2.74608 | -2.18381 | -1.24504 | -0.122566 | 0.827651 | 1.58519 | 2.24455 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| bonus_part | alpha_1 | 3768 | 0.818863 | 0.441683 | 0.189329 | 0.31487 | 0.439707 | 0.714599 | 1.11429 | 1.61708 | 2.97558 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| bonus_part | alpha_2 | 3768 | 0.798709 | 0.392323 | 0.260469 | 0.355135 | 0.475663 | 0.701527 | 1.04662 | 1.51883 | 3.13938 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| bonus_part | alpha_3 | 3768 | 0.815443 | 0.411657 | 0.210591 | 0.329895 | 0.465653 | 0.725877 | 1.09641 | 1.53744 | 3.33278 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| bonus_part | alpha_norm | 3768 | 1.45551 | 0.611023 | 0.509102 | 0.61265 | 0.890232 | 1.41521 | 1.93395 | 2.45388 | 3.54937 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| synergy_player | psi_1 | 1455 | -0.00142492 | 0.447325 | -2.27401 | -0.760402 | -0.271242 | 0.00066819 | 0.279812 | 0.737103 | 1.50482 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| synergy_player | psi_norm | 1455 | 0.332584 | 0.299021 | 0.000103037 | 0.012849 | 0.0769649 | 0.275765 | 0.482859 | 0.92803 | 2.27401 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| synergy | synergy_score | 2512 | 0.0278189 | 0.250769 | -1.19422 | -0.399841 | -0.0135762 | 0.00885964 | 0.123512 | 0.385176 | 2.1493 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
| synergy | synergy_contribution | 36032 | 0.256622 | 0.684556 | -1.61207 | -0.840062 | -0.0902977 | 0.0504856 | 0.713531 | 1.45279 | 3.09312 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/synergy |
