# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/tfidf-cumulative-difficulty-all2024/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/tfidf-cumulative-difficulty-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 462911 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 87666.3 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.385976 |
| mean_synergy_contribution | -0.526247 |
| median_synergy_contribution | -0.426816 |
| negative_synergy_fraction | 0.682155 |
| positive_synergy_fraction | 0.293463 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930739 |
| log_loss | 0.339997 |
| ece | 0.0277283 |
| part_accuracy | 0.850272 |
| exact_score_accuracy | 0.605502 |
| rounded_score_accuracy | 0.606114 |
| per_bonus_points_mae | 4.74821 |
| ppb_mae | 1.66905 |
| accuracy | 0.850272 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.667898 |
| log_loss | 0.585101 |
| ece | 0.129408 |
| accuracy | 0.709396 |
| buzz_position_mae | 0.138498 |
| buzz_position_median_absolute_error | 0.11929 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.911241 | 0.930739 | 0.0194986 | synergy |
| log_loss | 0.378279 | 0.339997 | -0.0382825 | synergy |
| ece | 0.0186362 | 0.0277283 | 0.00909204 | no-synergy |
| accuracy | 0.827687 | 0.850272 | 0.0225847 | synergy |
| part_accuracy | 0.827687 | 0.850272 | 0.0225847 | synergy |
| exact_score_accuracy | 0.554124 | 0.605502 | 0.0513779 | synergy |
| per_bonus_points_mae | 5.37066 | 4.74821 | -0.622441 | synergy |
| ppb_mae | 2.81649 | 1.66905 | -1.14744 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.16266 | 0.737349 | 2.20303 | 3.88593 | 4.69884 | 5.22139 | 5.67249 | 6.26469 | 7.39136 |
| player | theta_1 | 1755 | 0.393512 | 0.540433 | -1.43915 | -0.449431 | 0.0450705 | 0.351092 | 0.710087 | 1.34944 | 2.76624 |
| player | theta_2 | 1755 | 0.533488 | 0.741183 | -1.31797 | -0.55278 | -0.0183447 | 0.458422 | 0.994303 | 1.91302 | 2.80139 |
| player | theta_3 | 1755 | 0.10754 | 0.876602 | -2.4488 | -1.1715 | -0.483739 | 0.00893796 | 0.572588 | 1.88079 | 2.97027 |
| player | theta_4 | 1755 | -0.66124 | 0.813881 | -3.13942 | -2.02365 | -1.23999 | -0.642699 | -0.107929 | 0.681438 | 1.42528 |
| player | theta_5 | 1755 | -0.239915 | 0.652739 | -2.14925 | -1.2622 | -0.690713 | -0.262095 | 0.205229 | 0.85859 | 1.98561 |
| player | theta_norm | 1755 | 1.77455 | 0.702758 | 0.292478 | 0.866697 | 1.26097 | 1.63215 | 2.16437 | 3.18561 | 4.13741 |
| tossup | beta | 1350 | 2.50253 | 0.667823 | -0.48391 | 1.28473 | 2.08394 | 2.54729 | 2.96377 | 3.52919 | 4.37688 |
| tossup | gamma | 1350 | 86.0147 | 231.202 | 0.17371 | 3.55068 | 7.04579 | 13.3047 | 47.7819 | 478.827 | 2154.21 |
| tossup | mu | 1350 | 0.703411 | 0.168462 | 0.127033 | 0.412395 | 0.589528 | 0.712941 | 0.836363 | 0.954383 | 0.993853 |
| tossup | alpha_1 | 1350 | -0.517772 | 0.643023 | -2.51737 | -1.58513 | -0.982485 | -0.487872 | -0.0462116 | 0.486706 | 1.52386 |
| tossup | alpha_2 | 1350 | -0.57828 | 0.640479 | -2.52261 | -1.68279 | -0.971187 | -0.525747 | -0.142968 | 0.384497 | 1.25402 |
| tossup | alpha_3 | 1350 | 0.0937087 | 0.831292 | -2.32035 | -1.32503 | -0.470618 | 0.107662 | 0.659243 | 1.44337 | 2.5683 |
| tossup | alpha_4 | 1350 | 0.717631 | 0.802945 | -1.54798 | -0.579365 | 0.207096 | 0.671381 | 1.20302 | 2.11564 | 3.3382 |
| tossup | alpha_5 | 1350 | 0.341316 | 0.707806 | -1.39915 | -0.689526 | -0.193223 | 0.294515 | 0.788658 | 1.65806 | 2.40236 |
| tossup | alpha_norm | 1350 | 1.91628 | 0.478851 | 0.542408 | 1.12563 | 1.57837 | 1.91507 | 2.24221 | 2.69389 | 3.58761 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.286356 | 1.47593 | -2.7273 | -1.95914 | -0.979944 | 0.312894 | 1.48471 | 2.59417 | 3.99838 |
| bonus_part | alpha_1 | 4716 | 0.781436 | 0.359082 | 0.207232 | 0.378228 | 0.524928 | 0.682878 | 0.958949 | 1.50932 | 2.86814 |
| bonus_part | alpha_2 | 4716 | 0.767621 | 0.368332 | 0.161379 | 0.34533 | 0.507839 | 0.665981 | 0.954791 | 1.56172 | 2.70212 |
| bonus_part | alpha_3 | 4716 | 0.763846 | 0.312932 | 0.128684 | 0.359831 | 0.554041 | 0.706596 | 0.917274 | 1.34891 | 2.65699 |
| bonus_part | alpha_4 | 4716 | 0.937881 | 0.507075 | 0.226594 | 0.416145 | 0.577684 | 0.798562 | 1.17609 | 1.8496 | 4.46865 |
| bonus_part | alpha_5 | 4716 | 0.791791 | 0.325671 | 0.182866 | 0.421355 | 0.604737 | 0.731064 | 0.878155 | 1.41209 | 3.28915 |
| bonus_part | alpha_norm | 4716 | 1.9471 | 0.473632 | 0.896505 | 1.32074 | 1.59129 | 1.87673 | 2.24276 | 2.77672 | 4.81797 |
| synergy_player | psi_1 | 1755 | -0.0041465 | 0.439491 | -2.1783 | -0.704489 | -0.078081 | 0.000797352 | 0.0743995 | 0.748468 | 2.00008 |
| synergy_player | psi_2 | 1755 | 0.00129721 | 0.434424 | -2.12711 | -0.753345 | -0.0796791 | 0.00280732 | 0.0789107 | 0.758957 | 1.7717 |
| synergy_player | psi_3 | 1755 | 0.0106408 | 0.383084 | -1.88039 | -0.600631 | -0.0621295 | -0.000129208 | 0.0713415 | 0.647701 | 2.11766 |
| synergy_player | psi_norm | 1755 | 0.582105 | 0.435572 | 0.00969092 | 0.081287 | 0.239008 | 0.472046 | 0.808819 | 1.47979 | 2.24126 |
| synergy | synergy_score | 3042 | -0.127228 | 0.515881 | -3.2702 | -1.14342 | -0.283044 | 0.00260521 | 0.127892 | 0.450375 | 2.96249 |
| synergy | synergy_contribution | 60454 | -0.526247 | 0.998152 | -4.92323 | -2.35844 | -1.14825 | -0.426816 | 0.0352244 | 1.03641 | 3.31756 |
