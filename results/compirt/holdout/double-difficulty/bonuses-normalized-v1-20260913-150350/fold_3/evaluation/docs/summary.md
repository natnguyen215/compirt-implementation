# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all tournaments |
| compositional | dimensions | 3 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.54463 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.889611 |
| log_loss | 0.42007 |
| ece | 0.0233364 |
| brier | 0.134273 |
| part_accuracy | 0.80686 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.281175 |
| part_accuracy_macro_team | 0.809365 |
| part_accuracy_macro_bonus | 0.807186 |
| probability_std | 0.34092 |
| probability_p10 | 0.0609047 |
| probability_p50 | 0.548612 |
| probability_p90 | 0.956359 |
| mean_predictive_variance | 0.132814 |
| exact_acc | 0.508338 |
| ranked_probability_score | 0.119254 |
| bonus_total_score_log_loss | 1.04185 |
| ppb_mae | 2.36139 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25365 | 0.889611 | 0.42007 | 0.0233364 | 0.134273 | 0.80686 | 0.525685 | 0.281175 | 0.34092 | 0.0609047 | 0.548612 | 0.956359 | 0.132814 |
| bonus_part_correctness | tier | fall | 8094 | 0.882958 | 0.424858 | 0.0257073 | 0.136843 | 0.80084 | 0.595132 | 0.205708 | 0.332474 | 0.0954672 | 0.649388 | 0.96474 | 0.131948 |
| bonus_part_correctness | tier | nationals | 4125 | 0.879727 | 0.434666 | 0.0357331 | 0.138093 | 0.80897 | 0.448485 | 0.360485 | 0.330659 | 0.0487216 | 0.424219 | 0.916959 | 0.139165 |
| bonus_part_correctness | tier | regionals | 5247 | 0.888803 | 0.423432 | 0.0346322 | 0.13575 | 0.803126 | 0.481609 | 0.321517 | 0.341916 | 0.0472281 | 0.501996 | 0.949575 | 0.133041 |
| bonus_part_correctness | tier | winter | 7899 | 0.897563 | 0.405307 | 0.0223344 | 0.128662 | 0.814407 | 0.524117 | 0.29029 | 0.345089 | 0.0573279 | 0.533606 | 0.958287 | 0.130233 |
| bonus_part_correctness | category | Current Events | 243 | 0.89336 | 0.419864 | 0.0605234 | 0.130413 | 0.798354 | 0.506173 | 0.292181 | 0.345531 | 0.0686525 | 0.538209 | 0.929174 | 0.13056 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.870161 | 0.453209 | 0.0312135 | 0.145998 | 0.789581 | 0.508682 | 0.280899 | 0.332495 | 0.0674622 | 0.517937 | 0.950362 | 0.139218 |
| bonus_part_correctness | category | Geography | 456 | 0.89105 | 0.4055 | 0.0418582 | 0.129958 | 0.817982 | 0.622807 | 0.195175 | 0.332956 | 0.0784959 | 0.70942 | 0.954502 | 0.130037 |
| bonus_part_correctness | category | History | 4050 | 0.894399 | 0.409703 | 0.0201205 | 0.130565 | 0.81284 | 0.565185 | 0.247654 | 0.340399 | 0.0645672 | 0.615978 | 0.959821 | 0.130331 |
| bonus_part_correctness | category | Literature | 4029 | 0.890324 | 0.417582 | 0.0211745 | 0.133187 | 0.807148 | 0.536113 | 0.271035 | 0.343197 | 0.0622183 | 0.515083 | 0.958727 | 0.131833 |
| bonus_part_correctness | category | Mythology | 936 | 0.891965 | 0.406216 | 0.0493923 | 0.131506 | 0.801282 | 0.619658 | 0.181624 | 0.305894 | 0.142553 | 0.692495 | 0.963276 | 0.139122 |
| bonus_part_correctness | category | Other Academic | 255 | 0.923344 | 0.356001 | 0.0732485 | 0.105488 | 0.866667 | 0.545098 | 0.321569 | 0.358144 | 0.0494948 | 0.642864 | 0.95829 | 0.119367 |
| bonus_part_correctness | category | Philosophy | 948 | 0.865085 | 0.454417 | 0.0368073 | 0.149721 | 0.773207 | 0.504219 | 0.268987 | 0.332949 | 0.0708789 | 0.475935 | 0.945897 | 0.139131 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.892778 | 0.41275 | 0.0724731 | 0.13531 | 0.796491 | 0.578947 | 0.217544 | 0.31908 | 0.148361 | 0.682388 | 0.97359 | 0.134386 |
| bonus_part_correctness | category | Religion | 1014 | 0.896473 | 0.409574 | 0.0339695 | 0.128341 | 0.828402 | 0.50789 | 0.320513 | 0.347424 | 0.0490979 | 0.527377 | 0.951948 | 0.129034 |
| bonus_part_correctness | category | Science | 4059 | 0.890628 | 0.418288 | 0.0220878 | 0.132827 | 0.813008 | 0.530426 | 0.282582 | 0.340631 | 0.0678325 | 0.560936 | 0.958597 | 0.132583 |
| bonus_part_correctness | category | Social Science | 906 | 0.910851 | 0.376392 | 0.0351483 | 0.119899 | 0.828918 | 0.471302 | 0.357616 | 0.355316 | 0.0376763 | 0.442718 | 0.959251 | 0.123619 |
| bonus_part_correctness | category | Unknown | 5247 | 0.888803 | 0.423432 | 0.0346322 | 0.13575 | 0.803126 | 0.481609 | 0.321517 | 0.341916 | 0.0472281 | 0.501996 | 0.949575 | 0.133041 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.208884 | 1.23584 | -2.74819 | -2.2555 | -1.25607 | -0.15305 | 0.83925 | 1.62929 | 2.10429 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/compositional |
| bonus_part | alpha_1 | 3768 | 0.775991 | 0.421104 | 0.183383 | 0.303174 | 0.420462 | 0.67224 | 1.05526 | 1.53679 | 2.94151 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/compositional |
| bonus_part | alpha_2 | 3768 | 0.727697 | 0.354095 | 0.23323 | 0.336182 | 0.4358 | 0.629514 | 0.952754 | 1.41398 | 2.78239 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/compositional |
| bonus_part | alpha_3 | 3768 | 0.783484 | 0.401554 | 0.198447 | 0.317956 | 0.448695 | 0.690801 | 1.05047 | 1.50872 | 3.15278 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/compositional |
| bonus_part | alpha_norm | 3768 | 1.37121 | 0.573806 | 0.493466 | 0.589216 | 0.837653 | 1.32152 | 1.82109 | 2.33905 | 3.30499 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_3/train/compositional |
