# Synergy-Model Bonus Metrics - Run Comparison

**Scope.** These runs evaluate the *synergy* variant of the CompIRT bonus model on
the 2024 in-sample split and the 2024 -> 2025 temporal holdout split. They differ
by the source of structured tossup/bonus information and whether the
correctness-calibration flag (`cal`) is enabled.

The values below are recomputed from the saved prediction CSVs so that legacy
artifacts with older metric headers are comparable to the current evaluator.
Lower is better for `log_loss`, `ECE`, `PPB MAE`, `buzz MAE`, and `buzz MedAE`;
higher is better for `AUC`, `part_acc`, `exact_acc`,
`score_acc`, and `acc`. Bold marks the best value in each metric
column.

## In-Sample Bonus Stage Metrics (Stage 2)

| Run | Bonus model | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | part_acc ↑ | exact_acc ↑ | score_acc ↑ | PPB MAE ↓ |
|---|---|---|:--:|--:|--:|--:|--:|--:|--:|--:|
| `all-2024` | synergy | none | ✗ | **0.9391** | **0.3285** | 0.0448 | **0.8587** | **0.6265** | **0.6238** | 1.7620 |
| `baseline-all2024-cal` | synergy | none | ✓ | 0.9327 | 0.3380 | 0.0341 | 0.8513 | 0.6089 | 0.6115 | 1.7583 |
| `plda-all2024` | synergy | PLDA 5d | ✗ | 0.9135 | 0.3937 | 0.0647 | 0.8340 | 0.5681 | 0.5725 | 1.8853 |
| `plda-all2024-cal` | synergy | PLDA 5d | ✓ | 0.9182 | 0.3645 | 0.0178 | 0.8381 | 0.5767 | 0.5895 | 1.7387 |
| `lda-all2024` | synergy | LDA 5d | ✗ | 0.9154 | 0.3865 | 0.0589 | 0.8361 | 0.5739 | 0.5770 | 1.8686 |
| `lda-all2024-cal` | synergy | LDA 5d | ✓ | 0.9194 | 0.3618 | 0.0174 | 0.8390 | 0.5783 | 0.5907 | 1.7401 |
| `category-all2024` | synergy | one-hot category 13d | ✗ | 0.9181 | 0.3712 | 0.0367 | 0.8373 | 0.5767 | 0.5813 | 1.8409 |
| `category-all2024-cal` | synergy | one-hot category 13d | ✓ | 0.9196 | 0.3605 | 0.0112 | 0.8386 | 0.5795 | 0.5908 | 1.7532 |
| `learned-topic-all2024` | synergy | learned topic 5d | ✗ | 0.9161 | 0.3818 | 0.0526 | 0.8360 | 0.5731 | 0.5801 | 1.8602 |
| `learned-topic-all2024-cal` | synergy | learned topic 5d | ✓ | 0.9218 | 0.3558 | 0.0134 | 0.8410 | 0.5828 | 0.5956 | **1.7138** |
| `embedding-all2024` | synergy | embedding relevance 5d | ✗ | 0.9132 | 0.3808 | 0.0356 | 0.8305 | 0.5608 | 0.5667 | 1.9067 |
| `embedding-all2024-cal` | synergy | embedding relevance 5d | ✓ | 0.9171 | 0.3652 | **0.0112** | 0.8345 | 0.5697 | 0.5800 | 1.7317 |
| `multidim-all2024` | synergy | multidim MIRT 5d | ✗ | 0.9361 | 0.3351 | 0.0434 | 0.8546 | 0.6154 | 0.6151 | 1.7864 |
| `multidim-all2024-cal` | synergy | multidim MIRT 5d | ✓ | 0.9370 | 0.3289 | 0.0372 | 0.8568 | 0.6226 | 0.6197 | 1.7463 |

The uncalibrated no-topic baseline is strongest on in-sample bonus
classification metrics: AUC, log loss, part accuracy, strict exact accuracy,
and score accuracy. Calibrated learned-topic has the best PPB MAE, and
calibrated embedding-relevance has the best ECE by a very small margin over
calibrated category at full precision.

## In-Sample Tossup Stage Metrics (Stage 1)

| Run | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | acc ↑ |
|---|---|:--:|--:|--:|--:|--:|
| `all-2024` | none | ✗ | **0.7037** | 0.5804 | 0.1515 | 0.7059 |
| `baseline-all2024-cal` | none | ✓ | 0.6698 | **0.5092** | 0.0101 | **0.7714** |
| `plda-all2024` | PLDA 5d | ✗ | 0.6631 | 0.6118 | 0.1817 | 0.6762 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 0.6315 | 0.5229 | 0.0116 | 0.7679 |
| `lda-all2024` | LDA 5d | ✗ | 0.6657 | 0.6083 | 0.1768 | 0.6806 |
| `lda-all2024-cal` | LDA 5d | ✓ | 0.6321 | 0.5225 | 0.0126 | 0.7678 |
| `category-all2024` | one-hot category 13d | ✗ | 0.6754 | 0.6216 | 0.1907 | 0.6806 |
| `category-all2024-cal` | one-hot category 13d | ✓ | 0.6139 | 0.5275 | **0.0054** | 0.7675 |
| `learned-topic-all2024` | learned topic 5d | ✗ | 0.6734 | 0.6085 | 0.1771 | 0.6817 |
| `learned-topic-all2024-cal` | learned topic 5d | ✓ | 0.6306 | 0.5229 | 0.0104 | 0.7680 |
| `embedding-all2024` | embedding relevance 5d | ✗ | 0.6534 | 0.6188 | 0.1620 | 0.6800 |
| `embedding-all2024-cal` | embedding relevance 5d | ✓ | 0.6519 | 0.5152 | 0.0117 | 0.7713 |
| `multidim-all2024` | multidim MIRT 5d | ✗ | 0.7025 | 0.5754 | 0.1282 | 0.7171 |
| `multidim-all2024-cal` | multidim MIRT 5d | ✓ | 0.6572 | 0.5134 | 0.0080 | **0.7714** |

Calibration sharply reduces tossup ECE and log loss in every family, but because
the model is reoptimized with the calibration parameters, AUC can move too. The
uncalibrated baseline keeps the best in-sample tossup AUC; calibrated baseline
has the best log loss, category-calibrated has the best ECE, and calibrated
multidim ties the top accuracy after rounding to four decimals. The
embedding-relevance rows follow the broader calibrated pattern: calibration
substantially improves log loss, ECE, and accuracy, while AUC is roughly flat.

## Holdout Results (2024 -> 2025)

**Scope.** These rows use the temporal holdout pipeline:
`TRAIN_SPLIT=year_2024`, `TEST_SPLIT=year_2025`, and
`NEW_PLAYER_PRIOR=tier`. Returning players receive their 2024 posterior as the
2025 prior; new players receive a tier-conditioned population prior. Question
and bonus-part parameters are co-estimated transductively on the 2025 split,
matching the psychometric holdout setup used by the runners.

### Holdout Bonus Stage Metrics (Stage 2)

| Run | Bonus model | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | part_acc ↑ | exact_acc ↑ | score_acc ↑ | PPB MAE ↓ |
|---|---|---|:--:|--:|--:|--:|--:|--:|--:|--:|
| `holdout-all-2024` | synergy | none | ✗ | **0.9388** | **0.3251** | 0.0366 | **0.8596** | **0.6274** | **0.6250** | 1.6846 |
| `holdout-all2024-cal` | synergy | none | ✓ | 0.9333 | 0.3334 | 0.0270 | 0.8544 | 0.6144 | 0.6142 | 1.6703 |
| `holdout-plda-all2024` | synergy | PLDA 5d | ✗ | 0.9129 | 0.3907 | 0.0610 | 0.8338 | 0.5663 | 0.5695 | 1.8153 |
| `holdout-plda-all2024-cal` | synergy | PLDA 5d | ✓ | 0.9188 | 0.3622 | 0.0158 | 0.8378 | 0.5741 | 0.5846 | 1.6959 |
| `holdout-lda-all2024` | synergy | LDA 5d | ✗ | 0.9174 | 0.3791 | 0.0556 | 0.8380 | 0.5754 | 0.5815 | 1.7856 |
| `holdout-lda-all2024-cal` | synergy | LDA 5d | ✓ | 0.9221 | 0.3550 | 0.0146 | 0.8420 | 0.5842 | 0.5968 | 1.6757 |
| `holdout-category-all2024` | synergy | one-hot category 13d | ✗ | 0.9218 | 0.3626 | 0.0385 | 0.8412 | 0.5816 | 0.5889 | 1.7288 |
| `holdout-category-all2024-cal` | synergy | one-hot category 13d | ✓ | 0.9238 | 0.3505 | **0.0116** | 0.8430 | 0.5863 | 0.5980 | 1.6719 |
| `holdout-learned-topic-all2024` | synergy | learned topic 5d | ✗ | 0.9179 | 0.3769 | 0.0527 | 0.8385 | 0.5762 | 0.5813 | 1.7833 |
| `holdout-learned-topic-all2024-cal` | synergy | learned topic 5d | ✓ | 0.9244 | 0.3493 | 0.0134 | 0.8447 | 0.5892 | 0.5997 | **1.6658** |
| `holdout-multidim-all2024` | synergy | multidim MIRT 5d | ✗ | 0.9358 | 0.3338 | 0.0400 | 0.8561 | 0.6178 | 0.6130 | 1.7291 |
| `holdout-multidim-all2024-cal` | synergy | multidim MIRT 5d | ✓ | 0.9361 | 0.3290 | 0.0315 | 0.8574 | 0.6218 | 0.6215 | 1.7182 |

The calibrated baseline holdout row is now a synergy run, not a no-synergy
baseline. The uncalibrated baseline synergy run remains strongest on holdout
bonus AUC, log loss, part accuracy, exact accuracy, and score accuracy.
Among structured rows, calibrated multidim is closest to baseline on the
classification metrics, calibrated learned-topic has the best PPB MAE, and
calibrated category has the best ECE.

### Holdout Tossup Stage Metrics (Stage 1)

| Run | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | acc ↑ | buzz MAE ↓ | buzz MedAE ↓ |
|---|---|:--:|--:|--:|--:|--:|--:|--:|
| `holdout-all-2024` | none | ✗ | **0.6840** | 0.5938 | 0.1526 | 0.6985 | 0.1433 | 0.1238 |
| `holdout-all2024-cal` | none | ✓ | 0.6351 | **0.5187** | 0.0099 | **0.7715** | 0.1368 | 0.1176 |
| `holdout-plda-all2024` | PLDA 5d | ✗ | 0.6445 | 0.6291 | 0.1911 | 0.6641 | 0.1623 | 0.1446 |
| `holdout-plda-all2024-cal` | PLDA 5d | ✓ | 0.5899 | 0.5296 | 0.0041 | 0.7703 | 0.1568 | 0.1403 |
| `holdout-lda-all2024` | LDA 5d | ✗ | 0.6501 | 0.6208 | 0.1816 | 0.6729 | 0.1581 | 0.1403 |
| `holdout-lda-all2024-cal` | LDA 5d | ✓ | 0.5970 | 0.5279 | 0.0037 | 0.7703 | 0.1525 | 0.1356 |
| `holdout-category-all2024` | one-hot category 13d | ✗ | 0.6534 | 0.6386 | 0.2006 | 0.6684 | 0.1503 | 0.1313 |
| `holdout-category-all2024-cal` | one-hot category 13d | ✓ | 0.5801 | 0.5312 | 0.0084 | 0.7704 | 0.1449 | 0.1276 |
| `holdout-learned-topic-all2024` | learned topic 5d | ✗ | 0.6558 | 0.6212 | 0.1824 | 0.6732 | 0.1540 | 0.1358 |
| `holdout-learned-topic-all2024-cal` | learned topic 5d | ✓ | 0.5973 | 0.5277 | **0.0024** | 0.7704 | 0.1470 | 0.1293 |
| `holdout-multidim-all2024` | multidim MIRT 5d | ✗ | 0.6742 | 0.5989 | 0.1401 | 0.7037 | 0.1345 | 0.1121 |
| `holdout-multidim-all2024-cal` | multidim MIRT 5d | ✓ | 0.6245 | 0.5212 | 0.0064 | 0.7710 | **0.1309** | **0.1079** |

Calibration again reduces holdout tossup ECE and log loss. The uncalibrated
baseline keeps the best tossup AUC, while calibrated baseline has the best
log loss and accuracy. Calibrated learned-topic has the best tossup ECE, and
calibrated multidim has the best buzz-position errors.

### Holdout Synergy Delta Versus No-Synergy Bonus Model

Each row is `synergy - no_synergy` for the same holdout run. Positive is better
only for AUC; negative is better for log loss, ECE, and PPB MAE.

| Run | Topic/source | `cal` | ΔAUC ↑ | Δlog_loss ↓ | ΔECE ↓ | ΔPPB MAE ↓ |
|---|---|:--:|--:|--:|--:|--:|
| `holdout-all-2024` | none | ✗ | +0.0053 | -0.0125 | -0.0004 | -0.3948 |
| `holdout-all2024-cal` | none | ✓ | +0.0024 | -0.0045 | +0.0016 | -0.5000 |
| `holdout-plda-all2024` | PLDA 5d | ✗ | +0.0082 | -0.0189 | -0.0097 | -0.8635 |
| `holdout-plda-all2024-cal` | PLDA 5d | ✓ | +0.0117 | -0.0223 | +0.0058 | -0.8303 |
| `holdout-lda-all2024` | LDA 5d | ✗ | +0.0074 | -0.0175 | -0.0085 | -0.7770 |
| `holdout-lda-all2024-cal` | LDA 5d | ✓ | +0.0107 | -0.0210 | +0.0052 | -0.7640 |
| `holdout-category-all2024` | one-hot category 13d | ✗ | +0.0063 | -0.0150 | -0.0053 | -0.6081 |
| `holdout-category-all2024-cal` | one-hot category 13d | ✓ | +0.0116 | -0.0229 | +0.0059 | -0.8127 |
| `holdout-learned-topic-all2024` | learned topic 5d | ✗ | +0.0065 | -0.0148 | -0.0062 | -0.7143 |
| `holdout-learned-topic-all2024-cal` | learned topic 5d | ✓ | +0.0088 | -0.0179 | +0.0047 | -0.6905 |
| `holdout-multidim-all2024` | multidim MIRT 5d | ✗ | +0.0090 | -0.0193 | +0.0016 | -0.6056 |
| `holdout-multidim-all2024-cal` | multidim MIRT 5d | ✓ | +0.0018 | -0.0022 | +0.0028 | -0.4177 |

The synergy term improves holdout AUC, log loss, and PPB MAE for every run,
including the newly available calibrated baseline. Its effect on ECE is mixed:
uncalibrated rows usually improve ECE, while calibrated rows generally trade a
small ECE increase for better discrimination, log loss, and PPB.

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
contribution moves from **-0.7585** without calibration (83.5% of rows negative)
to **+0.2200** with calibration (38.2% negative, 58.7% positive). PLDA moves from
**-0.8482** to **+0.0640**. Embedding-relevance moves from **-1.0022** to
**+0.2070**. On the holdout baseline, the calibrated synergy run has mean
contribution **+0.4065**.

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
| **score_acc** | team's bonus | Fraction of bonuses where the expected-point total, snapped to {0,10,20,30}, exactly equals the observed total. |
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
