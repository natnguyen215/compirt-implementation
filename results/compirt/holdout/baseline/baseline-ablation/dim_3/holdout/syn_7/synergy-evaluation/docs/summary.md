# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_3/holdout/syn_7/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_3/holdout/syn_7`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 90065.1 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 7 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.181633 |
| mean_synergy_contribution | -0.158724 |
| median_synergy_contribution | -0.0656813 |
| negative_synergy_fraction | 0.560955 |
| positive_synergy_fraction | 0.414662 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.93145 |
| log_loss | 0.338577 |
| ece | 0.028464 |
| part_accuracy | 0.851739 |
| part_accuracy_macro_team | 0.853805 |
| part_accuracy_macro_game | 0.852231 |
| part_accuracy_macro_bonus | 0.859786 |
| exact_acc | 0.607503 |
| ppb_mae | 0.601591 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.66348 |
| log_loss | 0.604299 |
| ece | 0.147822 |
| accuracy | 0.693679 |
| buzz_position_mae | 0.14778 |
| buzz_position_median_absolute_error | 0.1283 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.09231 | 0.868292 | 1.59381 | 3.30136 | 4.6782 | 5.24364 | 5.67418 | 6.22639 | 7.03604 |
| player | theta_1 | 1755 | 0.134341 | 0.778263 | -2.30045 | -1.32459 | -0.325984 | 0.195555 | 0.693329 | 1.3021 | 2.29455 |
| player | theta_2 | 1755 | 0.174061 | 0.88649 | -3.18845 | -1.49703 | -0.26134 | 0.256759 | 0.720381 | 1.46403 | 2.90464 |
| player | theta_3 | 1755 | -0.0298343 | 0.631899 | -2.51016 | -1.07803 | -0.422462 | -0.00142341 | 0.369138 | 0.996696 | 2.06543 |
| player | theta_norm | 1755 | 1.22884 | 0.573773 | 0.09246 | 0.448706 | 0.808957 | 1.1339 | 1.557 | 2.25197 | 3.60474 |
| tossup | beta | 1350 | 3.33298 | 0.809543 | 0.0772755 | 1.80502 | 2.91951 | 3.42372 | 3.84664 | 4.49555 | 5.53021 |
| tossup | gamma | 1350 | 55.2634 | 175.791 | 3.18663 | 5.51951 | 8.36402 | 12.4341 | 25.1619 | 218.626 | 2412.5 |
| tossup | mu | 1350 | 0.594036 | 0.13866 | 0.111297 | 0.358042 | 0.505362 | 0.595705 | 0.68514 | 0.81502 | 0.987363 |
| tossup | alpha_1 | 1350 | 0.709808 | 0.747059 | -1.51042 | -0.404247 | 0.180824 | 0.645446 | 1.18783 | 2.05167 | 3.20922 |
| tossup | alpha_2 | 1350 | 1.0608 | 0.753448 | -1.06778 | -0.153734 | 0.528174 | 1.0363 | 1.56022 | 2.27646 | 3.82384 |
| tossup | alpha_3 | 1350 | -0.0403423 | 0.712204 | -2.04208 | -1.30722 | -0.455217 | 0.000537075 | 0.436644 | 1.06955 | 1.68828 |
| tossup | alpha_norm | 1350 | 1.6998 | 0.611155 | 0.120216 | 0.797771 | 1.29554 | 1.63992 | 2.05828 | 2.8118 | 4.14704 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.363971 | 1.47832 | -3.16671 | -2.0867 | -0.873435 | 0.458926 | 1.57195 | 2.61431 | 4.03448 |
| bonus_part | alpha_1 | 4716 | 0.0771838 | 0.598756 | -2.25818 | -0.815199 | -0.293594 | 0.0119463 | 0.404903 | 1.16333 | 2.81542 |
| bonus_part | alpha_2 | 4716 | 0.184771 | 0.700119 | -2.10884 | -0.887076 | -0.289971 | 0.10664 | 0.640123 | 1.41328 | 2.7233 |
| bonus_part | alpha_3 | 4716 | 0.00754847 | 0.502861 | -2.62722 | -0.914997 | -0.21281 | 0.0257606 | 0.27397 | 0.809903 | 2.02112 |
| bonus_part | alpha_norm | 4716 | 0.919555 | 0.544009 | 0.0384421 | 0.198378 | 0.463105 | 0.859266 | 1.29843 | 1.90587 | 2.99012 |
