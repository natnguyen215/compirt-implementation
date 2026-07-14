# Synergy-Model Bonus Metrics - Run Comparison

**Scope.** These runs evaluate the *synergy* variant of the CompIRT bonus model on
the 2024 in-sample split and the 2024 -> 2025 temporal holdout split. They differ
by the source of structured tossup/bonus information and whether the
correctness-calibration flag (`cal`) is enabled.

The values below are recomputed from the saved prediction CSVs so that legacy
artifacts with older metric headers are comparable to the current evaluator.
Lower is better for `log_loss`, `ECE`, `PPB MAE`, `buzz MAE`, and `buzz MedAE`;
higher is better for `AUC`, `part_acc`, `exact_acc`, and `acc`. Bold marks the
best value in each metric column.

## In-Sample Bonus Stage Metrics (Stage 2)

| Run | Bonus model | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | part_acc ↑ | exact_acc ↑ | PPB MAE ↓ |
|---|---|---|:--:|--:|--:|--:|--:|--:|--:|
| `all-2024` | synergy | none | ✗ | **0.9392** | **0.3278** | 0.0436 | **0.8590** | **0.6270** | 1.7408 |
| `baseline-all2024-cal` | synergy | none | ✓ | 0.9332 | 0.3377 | 0.0363 | 0.8519 | 0.6100 | 1.7655 |
| `plda-all2024` | synergy | PLDA 5d | ✗ | 0.9135 | 0.3937 | 0.0647 | 0.8340 | 0.5681 | 1.8853 |
| `plda-all2024-cal` | synergy | PLDA 5d | ✓ | 0.9182 | 0.3645 | 0.0178 | 0.8381 | 0.5767 | 1.7387 |
| `lda-all2024` | synergy | LDA 5d | ✗ | 0.9154 | 0.3865 | 0.0589 | 0.8361 | 0.5739 | 1.8686 |
| `lda-all2024-cal` | synergy | LDA 5d | ✓ | 0.9194 | 0.3618 | 0.0174 | 0.8390 | 0.5783 | 1.7401 |
| `category-all2024` | synergy | one-hot category 13d | ✗ | 0.9181 | 0.3712 | 0.0367 | 0.8373 | 0.5767 | 1.8409 |
| `category-all2024-cal` | synergy | one-hot category 13d | ✓ | 0.9196 | 0.3605 | 0.0112 | 0.8386 | 0.5795 | 1.7532 |
| `learned-topic-all2024` | synergy | learned topic 5d | ✗ | 0.9161 | 0.3818 | 0.0526 | 0.8360 | 0.5731 | 1.8602 |
| `learned-topic-all2024-cal` | synergy | learned topic 5d | ✓ | 0.9218 | 0.3558 | 0.0134 | 0.8410 | 0.5828 | 1.7138 |
| `learned-topic-tfidf-all2024` | synergy | learned topic + TF-IDF 5d | ✗ | 0.9193 | 0.3774 | 0.0566 | 0.8397 | 0.5808 | 1.7593 |
| `learned-topic-tfidf-all2024-cal` | synergy | learned topic + TF-IDF 5d | ✓ | 0.9216 | 0.3564 | 0.0138 | 0.8412 | 0.5829 | 1.7238 |
| `embedding-all2024-projection` | synergy | embedding relevance 5d | ✗ | 0.9132 | 0.3808 | 0.0356 | 0.8305 | 0.5608 | 1.9067 |
| `embedding-all2024-cal-projection` | synergy | embedding relevance 5d | ✓ | 0.9171 | 0.3652 | **0.0112** | 0.8345 | 0.5697 | 1.7317 |
| `multidim-all2024` | synergy | multidim MIRT 5d | ✗ | 0.9361 | 0.3351 | 0.0434 | 0.8546 | 0.6154 | 1.7864 |
| `multidim-all2024-cal` | synergy | multidim MIRT 5d | ✓ | 0.9370 | 0.3289 | 0.0372 | 0.8568 | 0.6226 | 1.7463 |
| `tfidf-cumulative-difficulty-all2024` | synergy | TF-IDF cumulative difficulty 5d | ✗ | 0.9326 | 0.3395 | 0.0355 | 0.8520 | 0.6095 | 1.6889 |
| `tfidf-cumulative-difficulty-all2024-cal` | synergy | TF-IDF cumulative difficulty 5d | ✓ | 0.9278 | 0.3471 | 0.0297 | 0.8483 | 0.6022 | 1.7254 |
| `tfidf-multidim-cumulative-difficulty-all2024` | synergy | TF-IDF multidim cumulative difficulty 5d | ✗ | 0.9251 | 0.3576 | 0.0386 | 0.8433 | 0.5912 | 1.9072 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | synergy | TF-IDF multidim cumulative difficulty 5d | ✓ | 0.9345 | 0.3306 | 0.0230 | 0.8545 | 0.6149 | **1.6610** |

The uncalibrated no-topic baseline is strongest on in-sample bonus
classification metrics: AUC, log loss, part accuracy, and strict exact accuracy.
Calibrated multidim TF-IDF cumulative difficulty has the best PPB MAE, and
calibrated embedding-relevance has the best ECE by a very small margin over
calibrated category at full precision. The learned-topic TF-IDF rows are broadly
comparable to their learned-topic counterparts: the uncalibrated version
improves several classification metrics but not ECE, while calibration preserves
similar classification quality. The scalar TF-IDF cumulative rows improve on
many structured-topic rows, but neither TF-IDF family displaces baseline or
calibrated multidim on the classification metrics.

## In-Sample Tossup Stage Metrics (Stage 1)

| Run | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | acc ↑ | buzz MAE ↓ |
|---|---|:--:|--:|--:|--:|--:|--:|
| `all-2024` | none | ✗ | 0.7014 | 0.5796 | 0.1491 | 0.7060 | 0.1390 |
| `baseline-all2024-cal` | none | ✓ | 0.6699 | **0.5089** | 0.0066 | **0.7723** | 0.1328 |
| `plda-all2024` | PLDA 5d | ✗ | 0.6631 | 0.6118 | 0.1817 | 0.6762 | 0.1609 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 0.6315 | 0.5229 | 0.0116 | 0.7679 | 0.1555 |
| `lda-all2024` | LDA 5d | ✗ | 0.6657 | 0.6083 | 0.1768 | 0.6806 | 0.1577 |
| `lda-all2024-cal` | LDA 5d | ✓ | 0.6321 | 0.5225 | 0.0126 | 0.7678 | 0.1524 |
| `category-all2024` | one-hot category 13d | ✗ | 0.6754 | 0.6216 | 0.1907 | 0.6806 | 0.1477 |
| `category-all2024-cal` | one-hot category 13d | ✓ | 0.6139 | 0.5275 | **0.0054** | 0.7675 | 0.1416 |
| `learned-topic-all2024` | learned topic 5d | ✗ | 0.6734 | 0.6085 | 0.1771 | 0.6817 | 0.1519 |
| `learned-topic-all2024-cal` | learned topic 5d | ✓ | 0.6306 | 0.5229 | 0.0104 | 0.7680 | 0.1447 |
| `learned-topic-tfidf-all2024` | learned topic + TF-IDF 5d | ✗ | 0.6723 | 0.5549 | 0.1056 | 0.7258 | 0.1443 |
| `learned-topic-tfidf-all2024-cal` | learned topic + TF-IDF 5d | ✓ | 0.6223 | 0.5252 | 0.0041 | 0.7675 | 0.1437 |
| `embedding-all2024-projection` | embedding relevance 5d | ✗ | 0.6534 | 0.6188 | 0.1620 | 0.6800 | 0.1514 |
| `embedding-all2024-cal-projection` | embedding relevance 5d | ✓ | 0.6519 | 0.5152 | 0.0117 | 0.7713 | 0.1456 |
| `multidim-all2024` | multidim MIRT 5d | ✗ | **0.7025** | 0.5754 | 0.1282 | 0.7171 | 0.1288 |
| `multidim-all2024-cal` | multidim MIRT 5d | ✓ | 0.6572 | 0.5134 | 0.0080 | 0.7714 | 0.1248 |
| `tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | 0.6972 | 0.5563 | 0.1108 | 0.7258 | 0.1318 |
| `tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | 0.6484 | 0.5169 | 0.0092 | 0.7697 | 0.1301 |
| `tfidf-multidim-cumulative-difficulty-all2024` | TF-IDF multidim cumulative difficulty 5d | ✗ | 0.7006 | 0.5742 | 0.1280 | 0.7169 | 0.1290 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | TF-IDF multidim cumulative difficulty 5d | ✓ | 0.6611 | 0.5125 | 0.0115 | 0.7710 | **0.1244** |

Calibration sharply reduces tossup ECE and log loss in every family, but because
the model is reoptimized with the calibration parameters, AUC can move too. The
uncalibrated multidim keeps the best in-sample tossup AUC; calibrated baseline
has the best log loss and accuracy, category-calibrated has the best ECE, and
calibrated multidim TF-IDF cumulative has the best buzz MAE. The embedding-relevance rows
follow the broader calibrated pattern: calibration substantially improves log
loss, ECE, and accuracy, while AUC is roughly flat.
The learned-topic TF-IDF run improves uncalibrated learned-topic log loss, ECE,
accuracy, and buzz timing. Its calibrated fit trades lower ECE and slightly
better buzz timing for worse AUC, log loss, and accuracy than learned-topic-cal.
The TF-IDF cumulative rows do not change the in-sample tossup-stage leaders
except on buzz-position error.

## Holdout Results (2024 -> 2025)

**Scope.** These rows use the temporal holdout pipeline:
`TRAIN_SPLIT=year_2024`, `TEST_SPLIT=year_2025`, and
`NEW_PLAYER_PRIOR=tier`. Returning players receive their 2024 posterior as the
2025 prior; new players receive a tier-conditioned population prior. Question
and bonus-part parameters are co-estimated transductively on the 2025 split,
matching the psychometric holdout setup used by the runners.

### Holdout Bonus Stage Metrics (Stage 2)

| Run | Bonus model | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | part_acc ↑ | exact_acc ↑ | PPB MAE ↓ |
|---|---|---|:--:|--:|--:|--:|--:|--:|--:|
| `holdout-all-2024` | synergy | none | ✗ | **0.9384** | **0.3256** | 0.0358 | **0.8587** | **0.6241** | **1.6573** |
| `holdout-all2024-cal` | synergy | none | ✓ | 0.9326 | 0.3359 | 0.0286 | 0.8529 | 0.6113 | 1.7030 |
| `holdout-plda-all2024` | synergy | PLDA 5d | ✗ | 0.9129 | 0.3907 | 0.0610 | 0.8338 | 0.5663 | 1.8153 |
| `holdout-plda-all2024-cal` | synergy | PLDA 5d | ✓ | 0.9188 | 0.3622 | 0.0158 | 0.8378 | 0.5741 | 1.6959 |
| `holdout-lda-all2024` | synergy | LDA 5d | ✗ | 0.9174 | 0.3791 | 0.0556 | 0.8380 | 0.5754 | 1.7856 |
| `holdout-lda-all2024-cal` | synergy | LDA 5d | ✓ | 0.9221 | 0.3550 | 0.0146 | 0.8420 | 0.5842 | 1.6757 |
| `holdout-category-all2024` | synergy | one-hot category 13d | ✗ | 0.9218 | 0.3626 | 0.0385 | 0.8412 | 0.5816 | 1.7288 |
| `holdout-category-all2024-cal` | synergy | one-hot category 13d | ✓ | 0.9238 | 0.3505 | **0.0116** | 0.8430 | 0.5863 | 1.6719 |
| `holdout-learned-topic-all2024` | synergy | learned topic 5d | ✗ | 0.9179 | 0.3769 | 0.0527 | 0.8385 | 0.5762 | 1.7833 |
| `holdout-learned-topic-all2024-cal` | synergy | learned topic 5d | ✓ | 0.9244 | 0.3493 | 0.0134 | 0.8447 | 0.5892 | 1.6658 |
| `holdout-learned-topic-tfidf-all2024` | synergy | learned topic + TF-IDF 5d | ✗ | 0.9206 | 0.3726 | 0.0560 | 0.8420 | 0.5837 | 1.6915 |
| `holdout-learned-topic-tfidf-all2024-cal` | synergy | learned topic + TF-IDF 5d | ✓ | 0.9245 | 0.3490 | 0.0138 | 0.8440 | 0.5881 | **1.6549** |
| `holdout-multidim-all2024` | synergy | multidim MIRT 5d | ✗ | 0.9358 | 0.3338 | 0.0400 | 0.8561 | 0.6178 | 1.7291 |
| `holdout-multidim-all2024-cal` | synergy | multidim MIRT 5d | ✓ | 0.9361 | 0.3290 | 0.0315 | 0.8574 | 0.6218 | 1.7182 |
| `holdout-tfidf-cumulative-difficulty-all2024` | synergy | TF-IDF cumulative difficulty 5d | ✗ | 0.9307 | 0.3400 | 0.0277 | 0.8503 | 0.6055 | 1.6691 |
| `holdout-tfidf-cumulative-difficulty-all2024-cal` | synergy | TF-IDF cumulative difficulty 5d | ✓ | 0.9274 | 0.3458 | 0.0245 | 0.8472 | 0.5972 | 1.6833 |

The calibrated baseline holdout row is now a synergy run, not a no-synergy
baseline. The uncalibrated baseline synergy run remains strongest on holdout
bonus AUC, log loss, part accuracy, and exact accuracy. The calibrated
learned-topic TF-IDF run has the best PPB MAE. Among the other structured rows,
calibrated multidim is closest to baseline on the classification metrics and
calibrated category has the best ECE. The scalar TF-IDF cumulative holdout rows
are competitive with the stronger structured variants: the uncalibrated row is
close to learned-topic-cal on PPB MAE, while the calibrated row improves ECE
but gives back a little discrimination and PPB accuracy.

### Holdout Tossup Stage Metrics (Stage 1)

| Run | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | acc ↑ | buzz MAE ↓ | buzz MedAE ↓ |
|---|---|:--:|--:|--:|--:|--:|--:|--:|
| `holdout-all-2024` | none | ✗ | **0.6838** | 0.5913 | 0.1493 | 0.7011 | 0.1432 | 0.1236 |
| `holdout-all2024-cal` | none | ✓ | 0.6306 | **0.5200** | 0.0119 | **0.7711** | 0.1373 | 0.1181 |
| `holdout-plda-all2024` | PLDA 5d | ✗ | 0.6445 | 0.6291 | 0.1911 | 0.6641 | 0.1623 | 0.1446 |
| `holdout-plda-all2024-cal` | PLDA 5d | ✓ | 0.5899 | 0.5296 | 0.0041 | 0.7703 | 0.1568 | 0.1403 |
| `holdout-lda-all2024` | LDA 5d | ✗ | 0.6501 | 0.6208 | 0.1816 | 0.6729 | 0.1581 | 0.1403 |
| `holdout-lda-all2024-cal` | LDA 5d | ✓ | 0.5970 | 0.5279 | 0.0037 | 0.7703 | 0.1525 | 0.1356 |
| `holdout-category-all2024` | one-hot category 13d | ✗ | 0.6534 | 0.6386 | 0.2006 | 0.6684 | 0.1503 | 0.1313 |
| `holdout-category-all2024-cal` | one-hot category 13d | ✓ | 0.5801 | 0.5312 | 0.0084 | 0.7704 | 0.1449 | 0.1276 |
| `holdout-learned-topic-all2024` | learned topic 5d | ✗ | 0.6558 | 0.6212 | 0.1824 | 0.6732 | 0.1540 | 0.1358 |
| `holdout-learned-topic-all2024-cal` | learned topic 5d | ✓ | 0.5973 | 0.5277 | **0.0024** | 0.7704 | 0.1470 | 0.1293 |
| `holdout-learned-topic-tfidf-all2024` | learned topic + TF-IDF 5d | ✗ | 0.6449 | 0.5756 | 0.1164 | 0.7128 | 0.1466 | 0.1287 |
| `holdout-learned-topic-tfidf-all2024-cal` | learned topic + TF-IDF 5d | ✓ | 0.5833 | 0.5307 | 0.0103 | 0.7704 | 0.1460 | 0.1282 |
| `holdout-multidim-all2024` | multidim MIRT 5d | ✗ | 0.6742 | 0.5989 | 0.1401 | 0.7037 | 0.1345 | 0.1121 |
| `holdout-multidim-all2024-cal` | multidim MIRT 5d | ✓ | 0.6245 | 0.5212 | 0.0064 | 0.7710 | **0.1309** | **0.1079** |
| `holdout-tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | 0.6679 | 0.5851 | 0.1294 | 0.7094 | 0.1385 | 0.1193 |
| `holdout-tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | 0.6003 | 0.5290 | 0.0149 | 0.7704 | 0.1351 | 0.1150 |

Calibration again reduces holdout tossup ECE and log loss. The uncalibrated
baseline keeps the best tossup AUC, while calibrated baseline has the best
log loss and accuracy. Calibrated learned-topic has the best tossup ECE, and
calibrated multidim has the best buzz-position errors. Scalar TF-IDF cumulative
improves over most fixed/learned topic variants on uncalibrated tossup AUC and
buzz timing, but it does not overtake baseline or multidim on the holdout
tossup-stage leaders.

### Holdout Synergy Delta Versus No-Synergy Bonus Model

Each row is `synergy - no_synergy` for the same holdout run. Positive is better
only for AUC; negative is better for log loss, ECE, and PPB MAE.

| Run | Topic/source | `cal` | ΔAUC ↑ | Δlog_loss ↓ | ΔECE ↓ | ΔPPB MAE ↓ |
|---|---|:--:|--:|--:|--:|--:|
| `holdout-all-2024` | none | ✗ | +0.0060 | -0.0144 | -0.0012 | -0.4656 |
| `holdout-all2024-cal` | none | ✓ | +0.0031 | -0.0056 | +0.0018 | -0.4848 |
| `holdout-plda-all2024` | PLDA 5d | ✗ | +0.0082 | -0.0189 | -0.0097 | -0.8635 |
| `holdout-plda-all2024-cal` | PLDA 5d | ✓ | +0.0117 | -0.0223 | +0.0058 | -0.8303 |
| `holdout-lda-all2024` | LDA 5d | ✗ | +0.0074 | -0.0175 | -0.0085 | -0.7770 |
| `holdout-lda-all2024-cal` | LDA 5d | ✓ | +0.0107 | -0.0210 | +0.0052 | -0.7640 |
| `holdout-category-all2024` | one-hot category 13d | ✗ | +0.0063 | -0.0150 | -0.0053 | -0.6081 |
| `holdout-category-all2024-cal` | one-hot category 13d | ✓ | +0.0116 | -0.0229 | +0.0059 | -0.8127 |
| `holdout-learned-topic-all2024` | learned topic 5d | ✗ | +0.0065 | -0.0148 | -0.0062 | -0.7143 |
| `holdout-learned-topic-all2024-cal` | learned topic 5d | ✓ | +0.0088 | -0.0179 | +0.0047 | -0.6905 |
| `holdout-learned-topic-tfidf-all2024` | learned topic + TF-IDF 5d | ✗ | +0.0049 | -0.0113 | -0.0005 | -0.4552 |
| `holdout-learned-topic-tfidf-all2024-cal` | learned topic + TF-IDF 5d | ✓ | +0.0090 | -0.0180 | +0.0046 | -0.6986 |
| `holdout-multidim-all2024` | multidim MIRT 5d | ✗ | +0.0090 | -0.0193 | +0.0016 | -0.6056 |
| `holdout-multidim-all2024-cal` | multidim MIRT 5d | ✓ | +0.0018 | -0.0022 | +0.0028 | -0.4177 |
| `holdout-tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | +0.0195 | -0.0383 | +0.0091 | -1.1474 |
| `holdout-tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | +0.0149 | -0.0305 | +0.0034 | -0.9564 |

The synergy term improves holdout AUC, log loss, and PPB MAE for every run,
including the calibrated baseline, scalar TF-IDF cumulative, and learned-topic
TF-IDF holdouts. The scalar TF-IDF cumulative runs show the largest synergy
gains in AUC, log loss, and PPB MAE among the rows shown. The effect on ECE is
mixed: uncalibrated rows often improve ECE, while calibrated rows and both
TF-IDF families can trade a small ECE increase for better discrimination, log
loss, and PPB.

## What the `cal` Flag Does

`cal` is the `calibrate_correctness` option. With it **off**, a team's
probability of converting a bonus part is

```
P(correct) = sigmoid(team_ability - part_difficulty + synergy)
```

With it **on**, the model learns two extra global scalars, a `scale` and a
`bias`, and passes the logit through them before the sigmoid:

```
P(correct) = sigmoid(scale * (team_ability - part_difficulty + synergy) + bias)
```

This is Platt / temperature scaling: a single shared stretch-and-shift applied to
every prediction. In these runs the calibration parameters are optimized with
the model, so calibration can change more than ECE; it can also move AUC,
accuracy, and the learned synergy contribution.

The effect on the synergy term is large. In-sample baseline mean synergy
contribution moves from **-0.7388** without calibration (81.1% of rows negative)
to **+0.2136** with calibration (36.7% negative, 60.2% positive). PLDA moves from
**-0.8482** to **+0.0640**. Embedding-relevance (non-projection FFN variant;
`embedding-all2024-projection` has no saved per-team synergy contributions)
moves from **-0.9413** to **+0.1089**. On the holdout baseline, the calibrated
synergy run has mean contribution **+0.3924**.

## Metrics

**Bonus stage** - each observation is one bonus part (binary: converted or not);
team/game metrics aggregate up.

| Metric | Granularity | What it measures |
|---|---|---|
| **AUC** | bonus part | Ranking/discrimination - area under the ROC curve over per-part correct-vs-incorrect predictions. |
| **log_loss** | bonus part | Binary cross-entropy. |
| **ECE** | bonus part | Expected Calibration Error - gap between predicted probability and actual conversion rate, binned into 10 bins. |
| **part_acc** | bonus part | Accuracy after thresholding the predicted probability at 0.5. |
| **exact_acc** | team's bonus | Fraction of bonuses where all three thresholded part predictions exactly match the observed part outcomes. |
| **PPB MAE** | team's game | Mean absolute error of points-per-bonus, averaged over every bonus a team heard in a game. |

**Tossup stage** - each observation is one first-buzz event (binary: correct or
not).

| Metric | Granularity | What it measures |
|---|---|---|
| **AUC** | first buzz | Ranking/discrimination over tossup correctness predictions. |
| **log_loss** | first buzz | Binary cross-entropy. |
| **ECE** | first buzz | Expected Calibration Error on tossup correctness probabilities. |
| **acc** | first buzz | Accuracy after thresholding the predicted correctness probability at 0.5. |
| **buzz MAE** | first buzz | Mean absolute error between observed and expected first-buzz position. |
| **buzz MedAE** | first buzz | Median absolute error between observed and expected first-buzz position. |
