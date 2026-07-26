# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/learned-topic-all2024/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/learned-topic-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 703579 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 226566 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.331503 |
| mean_synergy_contribution | -0.856635 |
| median_synergy_contribution | -0.757369 |
| negative_synergy_fraction | 0.884888 |
| positive_synergy_fraction | 0.0837098 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.916082 |
| log_loss | 0.381829 |
| ece | 0.0525872 |
| part_accuracy | 0.835952 |
| part_accuracy_macro_team | 0.838422 |
| part_accuracy_macro_game | 0.836172 |
| part_accuracy_macro_bonus | 0.831819 |
| exact_acc | 0.573089 |
| ppb_mae | 0.745437 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.673358 |
| log_loss | 0.608489 |
| ece | 0.177094 |
| accuracy | 0.68168 |
| buzz_position_mae | 0.151874 |
| buzz_position_median_absolute_error | 0.134984 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.908621 | 0.916082 | 0.0074612 | synergy |
| log_loss | 0.400035 | 0.381829 | -0.018206 | synergy |
| ece | 0.0643658 | 0.0525872 | -0.0117786 | synergy |
| part_accuracy | 0.821933 | 0.835952 | 0.0140191 | synergy |
| part_accuracy_macro_team | 0.82478 | 0.838422 | 0.0136422 | synergy |
| part_accuracy_macro_game | 0.821776 | 0.836172 | 0.0143968 | synergy |
| part_accuracy_macro_bonus | 0.806527 | 0.831819 | 0.025292 | synergy |
| exact_acc | 0.544294 | 0.573089 | 0.0287949 | synergy |
| ppb_mae | 1.94098 | 0.745437 | -1.19554 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 5.1062 | 0.601931 | 2.61471 | 3.87155 | 4.83406 | 5.17655 | 5.49409 | 5.94718 | 6.75994 |
| player | theta_1 | 1455 | 0.0899177 | 1.0391 | -1.68527 | -1.23816 | -0.747564 | -0.0800082 | 0.731531 | 2.04773 | 3.97693 |
| player | theta_2 | 1455 | 0.108775 | 1.16972 | -2.25316 | -1.48046 | -0.853773 | -0.0484497 | 0.954748 | 2.20175 | 3.5063 |
| player | theta_3 | 1455 | 0.0960713 | 0.932001 | -1.6064 | -1.0146 | -0.637916 | -0.131859 | 0.679267 | 1.96801 | 3.37413 |
| player | theta_4 | 1455 | 0.0410647 | 1.23887 | -2.30318 | -1.58555 | -0.990243 | -0.148279 | 0.826117 | 2.39965 | 3.86191 |
| player | theta_5 | 1455 | 0.0868155 | 0.988044 | -1.81714 | -1.26562 | -0.729907 | -0.00439473 | 0.754078 | 1.87105 | 3.24597 |
| player | theta_norm | 1455 | 2.2672 | 0.849873 | 0.416174 | 1.11258 | 1.71983 | 2.11272 | 2.66234 | 3.93312 | 6.29445 |
| tossup | beta_1 | 1260 | 0.744684 | 1.29441 | -2.79657 | -0.0203094 | 0.0766811 | 0.159709 | 0.404631 | 3.90107 | 4.58284 |
| tossup | beta_2 | 1260 | 1.17824 | 1.52248 | -1.64063 | -0.00989085 | 0.100003 | 0.243758 | 2.7023 | 4.06719 | 4.89504 |
| tossup | beta_3 | 1260 | 0.544018 | 1.06997 | -3.29919 | -0.0151928 | 0.0695402 | 0.142407 | 0.288717 | 3.53593 | 4.60841 |
| tossup | beta_4 | 1260 | 1.22654 | 1.62904 | -2.94818 | -0.0149956 | 0.089078 | 0.213901 | 2.97022 | 4.29071 | 5.2455 |
| tossup | beta_5 | 1260 | 0.840941 | 1.32415 | -0.609209 | -0.0233377 | 0.09157 | 0.1904 | 0.638875 | 3.87524 | 5.57385 |
| tossup | gamma_1 | 1260 | 11.1814 | 30.083 | 4.16105 | 4.59538 | 4.91406 | 5.15981 | 5.58068 | 30.9888 | 614.541 |
| tossup | gamma_2 | 1260 | 25.5266 | 114.836 | 3.65316 | 4.62417 | 4.96893 | 5.30057 | 10.6189 | 66.5456 | 1819.49 |
| tossup | gamma_3 | 1260 | 11.5477 | 53.3174 | 4.27843 | 4.59624 | 4.88944 | 5.09699 | 5.41559 | 21.9933 | 1411.18 |
| tossup | gamma_4 | 1260 | 21.7603 | 90.9545 | 3.67192 | 4.62271 | 4.97125 | 5.27577 | 8.9193 | 53.8741 | 1674.28 |
| tossup | gamma_5 | 1260 | 22.9321 | 130.604 | 2.84001 | 4.64147 | 4.93933 | 5.17886 | 5.84915 | 39.6134 | 1993.89 |
| tossup | mu_1 | 1260 | 0.517012 | 0.0776412 | 0.226728 | 0.466146 | 0.489985 | 0.501239 | 0.512031 | 0.698459 | 0.953501 |
| tossup | mu_2 | 1260 | 0.527088 | 0.090332 | 0.208334 | 0.43287 | 0.489706 | 0.502433 | 0.522694 | 0.731034 | 0.921024 |
| tossup | mu_3 | 1260 | 0.510578 | 0.0661684 | 0.259342 | 0.466663 | 0.489026 | 0.500228 | 0.511263 | 0.638182 | 0.934483 |
| tossup | mu_4 | 1260 | 0.543005 | 0.104952 | 0.158137 | 0.46237 | 0.491416 | 0.504869 | 0.543395 | 0.788904 | 0.956757 |
| tossup | mu_5 | 1260 | 0.518124 | 0.0794437 | 0.194503 | 0.454858 | 0.488835 | 0.501142 | 0.515124 | 0.710484 | 0.890126 |
| tossup | topic_weight_1 | 1260 | 0.157694 | 0.28112 | 0.00670502 | 0.0106737 | 0.0152441 | 0.0246534 | 0.0798363 | 0.894345 | 0.961788 |
| tossup | topic_weight_2 | 1260 | 0.259143 | 0.337261 | 0.00572232 | 0.0101357 | 0.0175934 | 0.0502593 | 0.592171 | 0.897467 | 0.956044 |
| tossup | topic_weight_3 | 1260 | 0.122003 | 0.236807 | 0.00710067 | 0.0115098 | 0.0168748 | 0.0258672 | 0.0615908 | 0.850796 | 0.951016 |
| tossup | topic_weight_4 | 1260 | 0.27688 | 0.355304 | 0.0078241 | 0.0142794 | 0.0237554 | 0.0508697 | 0.649572 | 0.922788 | 0.963855 |
| tossup | topic_weight_5 | 1260 | 0.18428 | 0.281333 | 0.00936585 | 0.0147131 | 0.0232287 | 0.0401023 | 0.150171 | 0.857495 | 0.954512 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 3768 | 0.0964202 | 0.780111 | -3.15203 | -0.894246 | -0.0999023 | 0.0367766 | 0.167689 | 1.63748 | 4.51326 |
| bonus_part | beta_2 | 3768 | 0.120708 | 0.983669 | -3.16132 | -1.75355 | -0.135439 | 0.0452376 | 0.251432 | 2.14255 | 4.19044 |
| bonus_part | beta_3 | 3768 | 0.0679131 | 0.698859 | -3.09369 | -0.702316 | -0.106995 | 0.034998 | 0.169444 | 1.16644 | 4.25786 |
| bonus_part | beta_4 | 3768 | 0.176745 | 1.03153 | -3.13429 | -1.61186 | -0.12095 | 0.0491922 | 0.244842 | 2.49115 | 4.50393 |
| bonus_part | beta_5 | 3768 | 0.0759591 | 0.829147 | -3.12771 | -1.36288 | -0.120159 | 0.043371 | 0.208435 | 1.65506 | 4.28408 |
| synergy_player | psi_1 | 1455 | -0.00377934 | 0.347275 | -1.44306 | -0.598206 | -0.0580589 | -0.000907697 | 0.0502518 | 0.552571 | 1.6315 |
| synergy_player | psi_2 | 1455 | 0.00200565 | 0.392252 | -1.48262 | -0.689082 | -0.0761579 | -0.00394403 | 0.0735547 | 0.687819 | 1.5868 |
| synergy_player | psi_3 | 1455 | 0.00280746 | 0.408687 | -1.66352 | -0.732926 | -0.0728737 | -0.000632932 | 0.0749513 | 0.774011 | 1.6728 |
| synergy_player | psi_norm | 1455 | 0.530036 | 0.400477 | 0.0118441 | 0.0547555 | 0.189062 | 0.438669 | 0.796682 | 1.29462 | 2.00085 |
| synergy | synergy_score | 2521 | -0.130968 | 0.413638 | -2.07687 | -0.952753 | -0.299289 | -0.00485699 | 0.0736803 | 0.384947 | 1.82089 |
| synergy | synergy_contribution | 44487 | -0.856635 | 0.727611 | -2.64162 | -2.14085 | -1.42161 | -0.757369 | -0.253831 | 0.0559362 | 2.58022 |
