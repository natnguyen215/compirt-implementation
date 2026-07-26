# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/lda/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/lda`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 63455.8 |
| pyramidal | calibrate_correctness | False |
| pyramidal | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 11229.9 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.378922 |
| mean_synergy_contribution | -1.47251 |
| median_synergy_contribution | -1.42694 |
| negative_synergy_fraction | 0.999145 |
| positive_synergy_fraction | 0 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921167 |
| log_loss | 0.397935 |
| ece | 0.0990388 |
| part_accuracy | 0.846516 |
| part_accuracy_macro_team | 0.842284 |
| part_accuracy_macro_game | 0.846657 |
| part_accuracy_macro_bonus | 0.838401 |
| exact_acc | 0.594699 |
| ppb_mae | 0.581447 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.65652 |
| log_loss | 0.625836 |
| ece | 0.1527 |
| accuracy | 0.658816 |
| buzz_position_mae | 0.163773 |
| buzz_position_median_absolute_error | 0.157697 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 5.52095 | 0.369611 | 3.90006 | 4.97521 | 5.25453 | 5.53608 | 5.77116 | 6.08939 | 6.29199 |
| player | theta_1 | 189 | 0.205644 | 1.06638 | -2.05478 | -1.43131 | -0.697574 | 0.210691 | 0.901808 | 2.03999 | 3.25855 |
| player | theta_2 | 189 | 0.178664 | 0.986848 | -1.96842 | -1.44865 | -0.524942 | 0.188905 | 0.963623 | 1.7939 | 2.60717 |
| player | theta_3 | 189 | 0.140415 | 1.2499 | -2.45194 | -1.71093 | -0.922942 | 0.0471239 | 1.09888 | 2.2295 | 3.1709 |
| player | theta_4 | 189 | 0.0844263 | 1.11579 | -1.51109 | -1.09642 | -0.762456 | -0.218911 | 0.6997 | 2.37072 | 3.47037 |
| player | theta_5 | 189 | 0.0355382 | 1.25679 | -2.07608 | -1.69514 | -1.04471 | -0.116249 | 0.999384 | 2.28953 | 2.91017 |
| player | theta_norm | 189 | 2.46128 | 0.714515 | 0.464099 | 1.39764 | 2.00817 | 2.4442 | 2.87759 | 3.72521 | 5.20261 |
| tossup | beta_1 | 360 | 0.885164 | 1.33709 | -0.107036 | -0.0507982 | 0.0131654 | 0.114175 | 1.17143 | 3.54117 | 3.98719 |
| tossup | beta_2 | 360 | 1.21245 | 1.3469 | -0.137259 | -0.00218215 | 0.172899 | 0.534762 | 2.07808 | 3.85628 | 4.37173 |
| tossup | beta_3 | 360 | 1.16215 | 1.39318 | -0.100882 | -0.0161351 | 0.102551 | 0.449552 | 2.41126 | 3.79185 | 4.40763 |
| tossup | beta_4 | 360 | 0.318426 | 0.90423 | -0.0916241 | -0.067933 | -0.0154598 | 0.0262079 | 0.105534 | 3.0708 | 4.39277 |
| tossup | beta_5 | 360 | 1.10266 | 1.4098 | -0.117083 | -0.026211 | 0.0883128 | 0.327751 | 1.80013 | 3.91716 | 4.41317 |
| tossup | gamma_1 | 360 | 11.9984 | 25.2166 | 4.36967 | 4.63198 | 4.93102 | 5.27069 | 8.45171 | 36.7313 | 361.428 |
| tossup | gamma_2 | 360 | 19.4036 | 50.0008 | 4.41104 | 4.7042 | 5.19569 | 5.79619 | 13.4814 | 67.399 | 592.314 |
| tossup | gamma_3 | 360 | 17.4214 | 41.4877 | 4.39762 | 4.71554 | 5.0882 | 5.61112 | 12.2207 | 65.1998 | 452.289 |
| tossup | gamma_4 | 360 | 11.4807 | 49.318 | 4.32429 | 4.55505 | 4.84673 | 5.09019 | 5.34235 | 15.2421 | 783.666 |
| tossup | gamma_5 | 360 | 14.9415 | 27.1561 | 4.34755 | 4.64791 | 5.01045 | 5.51387 | 12.1857 | 57.5995 | 218.64 |
| tossup | mu_1 | 360 | 0.542894 | 0.0914939 | 0.440309 | 0.478394 | 0.494378 | 0.504709 | 0.532098 | 0.75228 | 0.928442 |
| tossup | mu_2 | 360 | 0.549781 | 0.0938449 | 0.398441 | 0.471658 | 0.492497 | 0.508243 | 0.584062 | 0.754952 | 0.8697 |
| tossup | mu_3 | 360 | 0.548337 | 0.0949059 | 0.401556 | 0.4726 | 0.493732 | 0.507737 | 0.559698 | 0.753723 | 0.900276 |
| tossup | mu_4 | 360 | 0.515009 | 0.063366 | 0.470527 | 0.479859 | 0.490536 | 0.500556 | 0.510907 | 0.655442 | 0.911648 |
| tossup | mu_5 | 360 | 0.551769 | 0.0965288 | 0.456621 | 0.479888 | 0.495581 | 0.505948 | 0.570841 | 0.783805 | 0.903755 |
| tossup | topic_weight_1 | 360 | 0.223952 | 0.333494 | 0.00281902 | 0.00313496 | 0.00370607 | 0.0345403 | 0.26672 | 0.923587 | 0.983542 |
| tossup | topic_weight_2 | 360 | 0.240054 | 0.21258 | 0.00533466 | 0.00609217 | 0.0703108 | 0.164108 | 0.385038 | 0.658598 | 0.843227 |
| tossup | topic_weight_3 | 360 | 0.239308 | 0.25606 | 0.00486135 | 0.00553053 | 0.0397695 | 0.131536 | 0.403593 | 0.756245 | 0.92202 |
| tossup | topic_weight_4 | 360 | 0.0751751 | 0.202531 | 0.00109164 | 0.00121315 | 0.00134598 | 0.0014843 | 0.0297544 | 0.689082 | 0.948814 |
| tossup | topic_weight_5 | 360 | 0.221512 | 0.246693 | 0.00418633 | 0.00495095 | 0.0344891 | 0.113857 | 0.341132 | 0.743912 | 0.933887 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 1071 | 0.0282471 | 0.792306 | -2.75487 | -1.62586 | -0.0894655 | 0.0125173 | 0.115932 | 1.69687 | 2.519 |
| bonus_part | beta_2 | 1071 | 0.0439428 | 0.842696 | -2.70767 | -1.64496 | -0.258068 | 0.0382703 | 0.406782 | 1.64312 | 2.44663 |
| bonus_part | beta_3 | 1071 | 0.0668902 | 0.894427 | -2.67114 | -1.63677 | -0.218207 | 0.0304823 | 0.342485 | 1.83312 | 2.69514 |
| bonus_part | beta_4 | 1071 | 0.0237118 | 0.398613 | -2.49242 | -0.243017 | -0.041991 | 0.00454829 | 0.0584053 | 0.343218 | 2.35668 |
| bonus_part | beta_5 | 1071 | 0.0303326 | 0.733767 | -2.76773 | -1.43596 | -0.104121 | 0.0134615 | 0.18936 | 1.4074 | 2.49256 |
| synergy_player | psi_1 | 189 | 0.0149646 | 0.524648 | -1.46456 | -1.15326 | -0.0576867 | 0.011348 | 0.221275 | 0.912174 | 1.41098 |
| synergy_player | psi_2 | 189 | -0.00406034 | 0.486084 | -1.51603 | -0.781627 | -0.107522 | -0.00194248 | 0.0951102 | 0.90345 | 1.54125 |
| synergy_player | psi_3 | 189 | 0.00276817 | 0.526536 | -1.51274 | -1.07552 | -0.0769227 | -0.000131001 | 0.120346 | 0.853387 | 1.45207 |
| synergy_player | psi_norm | 189 | 0.80527 | 0.37029 | 0.0657898 | 0.298082 | 0.545171 | 0.675544 | 1.1324 | 1.44806 | 1.54234 |
| synergy | synergy_score | 274 | -0.259646 | 0.580703 | -1.99397 | -1.10137 | -0.760785 | -0.294308 | 0.292692 | 0.427007 | 1.01878 |
| synergy | synergy_contribution | 7017 | -1.47251 | 0.240031 | -2.11643 | -1.7737 | -1.62255 | -1.42694 | -1.29169 | -1.13418 | 0 |
