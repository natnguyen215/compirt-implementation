# Synergy-Model Bonus Metrics - Run Comparison

**Scope.** These runs evaluate the *synergy* variant of the CompIRT bonus model on
the 2024 in-sample split and the 2024 -> 2025 temporal holdout split. They differ
by the source of structured tossup/bonus information and whether the
correctness-calibration flag (`cal`) is enabled.

The values below come from the evaluation CSVs regenerated on 2026-07-16.
PPB MAE uses one pooled PPB value per team across the evaluated run; no
game-level PPB metric is included.

Lower is better for `log_loss`, `ECE`, `PPB MAE`, `buzz MAE`, and `buzz MedAE`;
higher is better for `AUC`, every accuracy column, and `acc`. Bold marks the
best value in each metric column.

## In-Sample Bonus Stage Metrics (Stage 2)

| Run | Bonus model | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | part micro ↑ | team macro ↑ | game macro ↑ | bonus macro ↑ | exact ↑ | PPB MAE ↓ |
|---|---|---|:--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `all-2024` | synergy | none | ✗ | **0.9392** | **0.3278** | 0.0436 | **0.8590** | **0.8617** | **0.8594** | **0.8629** | **0.6270** | 0.8787 |
| `baseline-all2024-cal` | synergy | none | ✓ | 0.9332 | 0.3377 | 0.0363 | 0.8519 | 0.8538 | 0.8520 | 0.8537 | 0.6100 | 0.8544 |
| `plda-all2024` | synergy | PLDA 5d | ✗ | 0.9135 | 0.3937 | 0.0647 | 0.8340 | 0.8360 | 0.8343 | 0.8302 | 0.5681 | 0.7400 |
| `plda-all2024-cal` | synergy | PLDA 5d | ✓ | 0.9182 | 0.3645 | 0.0178 | 0.8381 | 0.8403 | 0.8385 | 0.8406 | 0.5767 | 0.5336 |
| `lda-all2024` | synergy | LDA 5d | ✗ | 0.9154 | 0.3865 | 0.0589 | 0.8361 | 0.8381 | 0.8364 | 0.8323 | 0.5739 | 0.7188 |
| `lda-all2024-cal` | synergy | LDA 5d | ✓ | 0.9194 | 0.3618 | 0.0174 | 0.8390 | 0.8415 | 0.8392 | 0.8400 | 0.5783 | 0.5409 |
| `category-all2024` | synergy | one-hot category 13d | ✗ | 0.9181 | 0.3712 | 0.0367 | 0.8373 | 0.8390 | 0.8373 | 0.8350 | 0.5767 | 0.7410 |
| `category-all2024-cal` | synergy | one-hot category 13d | ✓ | 0.9196 | 0.3605 | 0.0112 | 0.8386 | 0.8410 | 0.8388 | 0.8414 | 0.5795 | 0.5832 |
| `learned-topic-all2024` | synergy | learned topic 5d | ✗ | 0.9161 | 0.3818 | 0.0526 | 0.8360 | 0.8384 | 0.8362 | 0.8318 | 0.5731 | 0.7454 |
| `learned-topic-all2024-cal` | synergy | learned topic 5d | ✓ | 0.9218 | 0.3558 | 0.0134 | 0.8410 | 0.8428 | 0.8411 | 0.8434 | 0.5828 | 0.5382 |
| `learned-topic-tfidf-all2024` | synergy | learned topic + TF-IDF 5d | ✗ | 0.9193 | 0.3774 | 0.0566 | 0.8397 | 0.8419 | 0.8400 | 0.8362 | 0.5808 | 0.6434 |
| `learned-topic-tfidf-all2024-cal` | synergy | learned topic + TF-IDF 5d | ✓ | 0.9216 | 0.3564 | 0.0138 | 0.8412 | 0.8433 | 0.8413 | 0.8424 | 0.5829 | 0.5401 |
| `embedding-all2024` | synergy | embedding relevance 5d | ✗ | 0.9180 | 0.3732 | 0.0410 | 0.8378 | 0.8397 | 0.8380 | 0.8360 | 0.5762 | 0.7169 |
| `embedding-all2024-projection` | synergy | embedding relevance 5d (projection) | ✗ | 0.9132 | 0.3808 | 0.0356 | 0.8305 | 0.8329 | 0.8306 | 0.8305 | 0.5608 | 0.7575 |
| `embedding-all2024-cal` | synergy | embedding relevance 5d | ✓ | 0.9197 | 0.3601 | 0.0134 | 0.8383 | 0.8407 | 0.8385 | 0.8423 | 0.5764 | 0.5271 |
| `embedding-all2024-cal-projection` | synergy | embedding relevance 5d (projection) | ✓ | 0.9171 | 0.3652 | **0.0112** | 0.8345 | 0.8364 | 0.8348 | 0.8380 | 0.5697 | **0.5267** |
| `multidim-all2024` | synergy | multidim MIRT 5d | ✗ | 0.9361 | 0.3351 | 0.0434 | 0.8546 | 0.8580 | 0.8550 | 0.8579 | 0.6154 | 0.9344 |
| `multidim-all2024-cal` | synergy | multidim MIRT 5d | ✓ | 0.9370 | 0.3289 | 0.0372 | 0.8568 | 0.8595 | 0.8571 | 0.8597 | 0.6226 | 0.8561 |
| `multidim-tanh-all2024` | synergy | multidim MIRT tanh 5d | ✗ | 0.9382 | 0.3285 | 0.0410 | 0.8583 | 0.8608 | 0.8586 | 0.8608 | 0.6257 | 0.7835 |
| `multidim-tanh-all2024-cal` | synergy | multidim MIRT tanh 5d | ✓ | 0.9303 | 0.3421 | 0.0309 | 0.8497 | 0.8511 | 0.8499 | 0.8517 | 0.6054 | 0.7884 |
| `tfidf-cumulative-difficulty-all2024` | synergy | TF-IDF cumulative difficulty 5d | ✗ | 0.9326 | 0.3395 | 0.0355 | 0.8520 | 0.8535 | 0.8520 | 0.8550 | 0.6095 | 0.6496 |
| `tfidf-cumulative-difficulty-all2024-cal` | synergy | TF-IDF cumulative difficulty 5d | ✓ | 0.9278 | 0.3471 | 0.0297 | 0.8483 | 0.8510 | 0.8489 | 0.8488 | 0.6022 | 0.6131 |
| `tfidf-multidim-cumulative-difficulty-all2024` | synergy | TF-IDF multidim cumulative difficulty 5d | ✗ | 0.9251 | 0.3576 | 0.0386 | 0.8433 | 0.8469 | 0.8436 | 0.8430 | 0.5912 | 1.0146 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | synergy | TF-IDF multidim cumulative difficulty 5d | ✓ | 0.9345 | 0.3306 | 0.0230 | 0.8545 | 0.8563 | 0.8546 | 0.8574 | 0.6149 | 0.5922 |

Data-derived leaders: AUC `all-2024` (0.9392); log loss `all-2024` (0.3278); ECE `embedding-all2024-cal-projection` (0.0112); part accuracy `all-2024` (0.8590); team-macro accuracy `all-2024` (0.8617); game-macro accuracy `all-2024` (0.8594); bonus-question-macro accuracy `all-2024` (0.8629); exact accuracy `all-2024` (0.6270); and pooled-team PPB MAE `embedding-all2024-cal-projection` (0.5267).

## In-Sample Tossup Stage Metrics (Stage 1)

| Run | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | acc ↑ | buzz MAE ↓ | buzz MedAE ↓ |
|---|---|:--:|--:|--:|--:|--:|--:|--:|
| `all-2024` | none | ✗ | 0.7014 | 0.5796 | 0.1491 | 0.7060 | 0.1390 | 0.1214 |
| `baseline-all2024-cal` | none | ✓ | 0.6699 | **0.5089** | 0.0066 | **0.7723** | 0.1328 | 0.1159 |
| `plda-all2024` | PLDA 5d | ✗ | 0.6631 | 0.6118 | 0.1817 | 0.6762 | 0.1609 | 0.1455 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 0.6315 | 0.5229 | 0.0116 | 0.7679 | 0.1555 | 0.1407 |
| `lda-all2024` | LDA 5d | ✗ | 0.6657 | 0.6083 | 0.1768 | 0.6806 | 0.1577 | 0.1419 |
| `lda-all2024-cal` | LDA 5d | ✓ | 0.6321 | 0.5225 | 0.0126 | 0.7678 | 0.1524 | 0.1376 |
| `category-all2024` | one-hot category 13d | ✗ | 0.6754 | 0.6216 | 0.1907 | 0.6806 | 0.1477 | 0.1306 |
| `category-all2024-cal` | one-hot category 13d | ✓ | 0.6139 | 0.5275 | 0.0054 | 0.7675 | 0.1416 | 0.1257 |
| `learned-topic-all2024` | learned topic 5d | ✗ | 0.6734 | 0.6085 | 0.1771 | 0.6817 | 0.1519 | 0.1350 |
| `learned-topic-all2024-cal` | learned topic 5d | ✓ | 0.6306 | 0.5229 | 0.0104 | 0.7680 | 0.1447 | 0.1288 |
| `learned-topic-tfidf-all2024` | learned topic + TF-IDF 5d | ✗ | 0.6723 | 0.5549 | 0.1056 | 0.7258 | 0.1443 | 0.1278 |
| `learned-topic-tfidf-all2024-cal` | learned topic + TF-IDF 5d | ✓ | 0.6223 | 0.5252 | 0.0041 | 0.7675 | 0.1437 | 0.1271 |
| `embedding-all2024` | embedding relevance 5d | ✗ | 0.6722 | 0.6074 | 0.1724 | 0.6833 | 0.1514 | 0.1350 |
| `embedding-all2024-projection` | embedding relevance 5d (projection) | ✗ | 0.6534 | 0.6188 | 0.1620 | 0.6800 | 0.1558 | 0.1386 |
| `embedding-all2024-cal` | embedding relevance 5d | ✓ | 0.6188 | 0.5260 | **0.0033** | 0.7673 | 0.1456 | 0.1289 |
| `embedding-all2024-cal-projection` | embedding relevance 5d (projection) | ✓ | 0.6519 | 0.5152 | 0.0117 | 0.7713 | 0.1486 | 0.1320 |
| `multidim-all2024` | multidim MIRT 5d | ✗ | **0.7025** | 0.5754 | 0.1282 | 0.7171 | 0.1288 | 0.1078 |
| `multidim-all2024-cal` | multidim MIRT 5d | ✓ | 0.6572 | 0.5134 | 0.0080 | 0.7714 | 0.1248 | 0.1026 |
| `multidim-tanh-all2024` | multidim MIRT tanh 5d | ✗ | 0.6990 | 0.5723 | 0.1199 | 0.7212 | 0.1276 | 0.1063 |
| `multidim-tanh-all2024-cal` | multidim MIRT tanh 5d | ✓ | 0.6597 | 0.5144 | 0.0145 | 0.7705 | **0.1234** | **0.1002** |
| `tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | 0.6972 | 0.5563 | 0.1108 | 0.7258 | 0.1318 | 0.1141 |
| `tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | 0.6484 | 0.5169 | 0.0092 | 0.7697 | 0.1301 | 0.1120 |
| `tfidf-multidim-cumulative-difficulty-all2024` | TF-IDF multidim cumulative difficulty 5d | ✗ | 0.7006 | 0.5742 | 0.1280 | 0.7169 | 0.1290 | 0.1084 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | TF-IDF multidim cumulative difficulty 5d | ✓ | 0.6611 | 0.5125 | 0.0115 | 0.7710 | 0.1244 | 0.1024 |

Data-derived leaders: AUC `multidim-all2024` (0.7025); log loss `baseline-all2024-cal` (0.5089); ECE `embedding-all2024-cal` (0.0033); accuracy `baseline-all2024-cal` (0.7723); buzz MAE `multidim-tanh-all2024-cal` (0.1234); and buzz median absolute error `multidim-tanh-all2024-cal` (0.1002).

## Holdout Results (2024 -> 2025)

**Scope.** These rows use the temporal holdout pipeline:
`TRAIN_SPLIT=year_2024`, `TEST_SPLIT=year_2025`, and
`NEW_PLAYER_PRIOR=tier`. Returning players receive their 2024 posterior as the
2025 prior; new players receive a tier-conditioned population prior. Question
and bonus-part parameters are co-estimated transductively on the 2025 split,
matching the psychometric holdout setup used by the runners.

### Holdout Bonus Stage Metrics (Stage 2)

| Run | Bonus model | Topic/source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | part micro ↑ | team macro ↑ | game macro ↑ | bonus macro ↑ | exact ↑ | PPB MAE ↓ |
|---|---|---|:--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `holdout-all-2024` | synergy | none | ✗ | **0.9384** | 0.3256 | 0.0358 | 0.8587 | **0.8607** | 0.8592 | 0.8681 | 0.6241 | 0.6560 |
| `holdout-all2024-cal` | synergy | none | ✓ | 0.9326 | 0.3359 | 0.0286 | 0.8529 | 0.8543 | 0.8532 | 0.8629 | 0.6113 | 0.6978 |
| `holdout-plda-all2024` | synergy | PLDA 5d | ✗ | 0.9129 | 0.3907 | 0.0610 | 0.8338 | 0.8360 | 0.8343 | 0.8284 | 0.5663 | 0.6037 |
| `holdout-plda-all2024-cal` | synergy | PLDA 5d | ✓ | 0.9188 | 0.3622 | 0.0158 | 0.8378 | 0.8395 | 0.8383 | 0.8457 | 0.5741 | 0.4312 |
| `holdout-lda-all2024` | synergy | LDA 5d | ✗ | 0.9174 | 0.3791 | 0.0556 | 0.8380 | 0.8399 | 0.8383 | 0.8316 | 0.5754 | 0.6036 |
| `holdout-lda-all2024-cal` | synergy | LDA 5d | ✓ | 0.9221 | 0.3550 | 0.0146 | 0.8420 | 0.8433 | 0.8424 | 0.8483 | 0.5842 | 0.4343 |
| `holdout-category-all2024` | synergy | one-hot category 13d | ✗ | 0.9218 | 0.3626 | 0.0385 | 0.8412 | 0.8430 | 0.8416 | 0.8394 | 0.5816 | 0.5434 |
| `holdout-category-all2024-cal` | synergy | one-hot category 13d | ✓ | 0.9238 | 0.3505 | 0.0116 | 0.8430 | 0.8444 | 0.8434 | 0.8521 | 0.5863 | 0.4174 |
| `holdout-learned-topic-all2024` | synergy | learned topic 5d | ✗ | 0.9179 | 0.3769 | 0.0527 | 0.8385 | 0.8401 | 0.8389 | 0.8308 | 0.5762 | 0.6072 |
| `holdout-learned-topic-all2024-cal` | synergy | learned topic 5d | ✓ | 0.9244 | 0.3493 | 0.0134 | 0.8447 | 0.8459 | 0.8451 | 0.8505 | 0.5892 | 0.4568 |
| `holdout-learned-topic-tfidf-all2024` | synergy | learned topic + TF-IDF 5d | ✗ | 0.9206 | 0.3726 | 0.0560 | 0.8420 | 0.8436 | 0.8424 | 0.8374 | 0.5837 | 0.4922 |
| `holdout-learned-topic-tfidf-all2024-cal` | synergy | learned topic + TF-IDF 5d | ✓ | 0.9245 | 0.3490 | 0.0138 | 0.8440 | 0.8453 | 0.8445 | 0.8479 | 0.5881 | 0.4452 |
| `holdout-multidim-all2024` | synergy | multidim MIRT 5d | ✗ | 0.9358 | 0.3338 | 0.0400 | 0.8561 | 0.8582 | 0.8566 | 0.8646 | 0.6178 | 0.7791 |
| `holdout-multidim-all2024-cal` | synergy | multidim MIRT 5d | ✓ | 0.9361 | 0.3290 | 0.0315 | 0.8574 | 0.8588 | 0.8578 | 0.8672 | 0.6218 | 0.7215 |
| `holdout-multidim-tanh-all2024` | synergy | multidim MIRT tanh 5d | ✗ | 0.9371 | 0.3286 | 0.0350 | **0.8589** | 0.8604 | **0.8593** | 0.8695 | **0.6256** | 0.6909 |
| `holdout-multidim-tanh-all2024-cal` | synergy | multidim MIRT tanh 5d | ✓ | 0.9301 | 0.3408 | 0.0273 | 0.8509 | 0.8521 | 0.8513 | 0.8602 | 0.6065 | 0.6496 |
| `holdout-multidim-tanhbias-all2024` | synergy | multidim MIRT tanh+bias 5d | ✗ | 0.9381 | **0.3141** | **0.0038** | 0.8573 | 0.8577 | 0.8576 | **0.8713** | 0.6206 | **0.4130** |
| `holdout-tfidf-cumulative-difficulty-all2024` | synergy | TF-IDF cumulative difficulty 5d | ✗ | 0.9307 | 0.3400 | 0.0277 | 0.8503 | 0.8515 | 0.8507 | 0.8616 | 0.6055 | 0.5522 |
| `holdout-tfidf-cumulative-difficulty-all2024-cal` | synergy | TF-IDF cumulative difficulty 5d | ✓ | 0.9274 | 0.3458 | 0.0245 | 0.8472 | 0.8485 | 0.8475 | 0.8576 | 0.5972 | 0.5342 |
| `holdout-tfidf-multidim-cumulative-difficulty-all2024` | synergy | TF-IDF multidim cumulative difficulty 5d | ✗ | 0.9268 | 0.3513 | 0.0335 | 0.8460 | 0.8486 | 0.8465 | 0.8539 | 0.5954 | 0.8462 |
| `holdout-tfidf-multidim-cumulative-difficulty-all2024-cal` | synergy | TF-IDF multidim cumulative difficulty 5d | ✓ | 0.9328 | 0.3330 | 0.0212 | 0.8528 | 0.8541 | 0.8531 | 0.8591 | 0.6095 | 0.5363 |

Data-derived leaders: AUC `holdout-all-2024` (0.9384); log loss `holdout-multidim-tanhbias-all2024` (0.3141); ECE `holdout-multidim-tanhbias-all2024` (0.0038); part accuracy `holdout-multidim-tanh-all2024` (0.8589); team-macro accuracy `holdout-all-2024` (0.8607); game-macro accuracy `holdout-multidim-tanh-all2024` (0.8593); bonus-question-macro accuracy `holdout-multidim-tanhbias-all2024` (0.8713); exact accuracy `holdout-multidim-tanh-all2024` (0.6256); and pooled-team PPB MAE `holdout-multidim-tanhbias-all2024` (0.4130).

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
| `holdout-multidim-all2024-cal` | multidim MIRT 5d | ✓ | 0.6245 | 0.5212 | 0.0064 | 0.7710 | 0.1309 | 0.1079 |
| `holdout-multidim-tanh-all2024` | multidim MIRT tanh 5d | ✗ | 0.6743 | 0.5953 | 0.1333 | 0.7088 | 0.1331 | 0.1105 |
| `holdout-multidim-tanh-all2024-cal` | multidim MIRT tanh 5d | ✓ | 0.6213 | 0.5237 | 0.0131 | 0.7708 | **0.1296** | **0.1054** |
| `holdout-multidim-tanhbias-all2024` | multidim MIRT tanh+bias 5d | ✗ | 0.6716 | 0.5649 | 0.1079 | 0.7304 | 0.1350 | 0.1114 |
| `holdout-tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | 0.6679 | 0.5851 | 0.1294 | 0.7094 | 0.1385 | 0.1193 |
| `holdout-tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | 0.6003 | 0.5290 | 0.0149 | 0.7704 | 0.1351 | 0.1150 |
| `holdout-tfidf-multidim-cumulative-difficulty-all2024` | TF-IDF multidim cumulative difficulty 5d | ✗ | 0.6759 | 0.5969 | 0.1377 | 0.7046 | 0.1350 | 0.1128 |
| `holdout-tfidf-multidim-cumulative-difficulty-all2024-cal` | TF-IDF multidim cumulative difficulty 5d | ✓ | 0.6245 | 0.5213 | 0.0081 | 0.7710 | 0.1307 | 0.1080 |

Data-derived leaders: AUC `holdout-all-2024` (0.6838); log loss `holdout-all2024-cal` (0.5200); ECE `holdout-learned-topic-all2024-cal` (0.0024); accuracy `holdout-all2024-cal` (0.7711); buzz MAE `holdout-multidim-tanh-all2024-cal` (0.1296); and buzz median absolute error `holdout-multidim-tanh-all2024-cal` (0.1054).

### Holdout Synergy Delta Versus No-Synergy Bonus Model

Each row is `synergy - no_synergy` for the same holdout run. Positive is better only for AUC; negative is better for log loss, ECE, and pooled-team PPB MAE.

| Run | Topic/source | `cal` | ΔAUC ↑ | Δlog_loss ↓ | ΔECE ↓ | Δpart ↑ | Δteam macro ↑ | Δgame macro ↑ | Δbonus macro ↑ | Δexact ↑ | ΔPPB MAE ↓ |
|---|---|:--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `holdout-all-2024` | none | ✗ | +0.0060 | -0.0144 | -0.0012 | +0.0064 | +0.0064 | +0.0064 | +0.0029 | +0.0148 | -0.7873 |
| `holdout-all2024-cal` | none | ✓ | +0.0031 | -0.0056 | +0.0018 | +0.0052 | +0.0054 | +0.0052 | +0.0045 | +0.0132 | -0.8214 |
| `holdout-plda-all2024` | PLDA 5d | ✗ | +0.0082 | -0.0189 | -0.0097 | +0.0177 | +0.0171 | +0.0179 | +0.0345 | +0.0387 | -1.3956 |
| `holdout-plda-all2024-cal` | PLDA 5d | ✓ | +0.0117 | -0.0223 | +0.0058 | +0.0143 | +0.0151 | +0.0145 | +0.0104 | +0.0309 | -1.4601 |
| `holdout-lda-all2024` | LDA 5d | ✗ | +0.0074 | -0.0175 | -0.0085 | +0.0151 | +0.0143 | +0.0152 | +0.0291 | +0.0333 | -1.2559 |
| `holdout-lda-all2024-cal` | LDA 5d | ✓ | +0.0107 | -0.0210 | +0.0052 | +0.0133 | +0.0137 | +0.0134 | +0.0095 | +0.0295 | -1.3666 |
| `holdout-category-all2024` | one-hot category 13d | ✗ | +0.0063 | -0.0150 | -0.0053 | +0.0098 | +0.0106 | +0.0101 | +0.0184 | +0.0221 | -1.1271 |
| `holdout-category-all2024-cal` | one-hot category 13d | ✓ | +0.0116 | -0.0229 | +0.0059 | +0.0147 | +0.0162 | +0.0150 | +0.0119 | +0.0340 | -1.4710 |
| `holdout-learned-topic-all2024` | learned topic 5d | ✗ | +0.0065 | -0.0148 | -0.0062 | +0.0132 | +0.0126 | +0.0133 | +0.0270 | +0.0299 | -1.1787 |
| `holdout-learned-topic-all2024-cal` | learned topic 5d | ✓ | +0.0088 | -0.0179 | +0.0047 | +0.0119 | +0.0124 | +0.0121 | +0.0085 | +0.0267 | -1.2343 |
| `holdout-learned-topic-tfidf-all2024` | learned topic + TF-IDF 5d | ✗ | +0.0049 | -0.0113 | -0.0005 | +0.0065 | +0.0070 | +0.0067 | +0.0102 | +0.0152 | -0.8947 |
| `holdout-learned-topic-tfidf-all2024-cal` | learned topic + TF-IDF 5d | ✓ | +0.0090 | -0.0180 | +0.0046 | +0.0108 | +0.0112 | +0.0110 | +0.0050 | +0.0243 | -1.2531 |
| `holdout-multidim-all2024` | multidim MIRT 5d | ✗ | +0.0090 | -0.0193 | +0.0016 | +0.0089 | +0.0090 | +0.0089 | +0.0047 | +0.0219 | -0.9481 |
| `holdout-multidim-all2024-cal` | multidim MIRT 5d | ✓ | +0.0018 | -0.0022 | +0.0028 | +0.0043 | +0.0044 | +0.0043 | +0.0011 | +0.0098 | -0.7528 |
| `holdout-multidim-tanh-all2024` | multidim MIRT tanh 5d | ✗ | +0.0038 | -0.0126 | -0.0079 | +0.0062 | +0.0059 | +0.0062 | +0.0062 | +0.0152 | -0.6412 |
| `holdout-multidim-tanh-all2024-cal` | multidim MIRT tanh 5d | ✓ | +0.0044 | -0.0095 | -0.0008 | +0.0073 | +0.0076 | +0.0074 | +0.0058 | +0.0180 | -1.1052 |
| `holdout-multidim-tanhbias-all2024` | multidim MIRT tanh+bias 5d | ✗ | +0.0107 | -0.0251 | -0.0046 | +0.0148 | +0.0154 | +0.0149 | +0.0131 | +0.0327 | -1.3608 |
| `holdout-tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | +0.0195 | -0.0383 | +0.0091 | +0.0226 | +0.0229 | +0.0225 | +0.0344 | +0.0514 | -1.7718 |
| `holdout-tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | +0.0149 | -0.0305 | +0.0034 | +0.0187 | +0.0192 | +0.0188 | +0.0211 | +0.0428 | -1.5693 |
| `holdout-tfidf-multidim-cumulative-difficulty-all2024` | TF-IDF multidim cumulative difficulty 5d | ✗ | +0.0045 | -0.0099 | -0.0020 | +0.0062 | +0.0063 | +0.0062 | +0.0220 | +0.0151 | -0.5552 |
| `holdout-tfidf-multidim-cumulative-difficulty-all2024-cal` | TF-IDF multidim cumulative difficulty 5d | ✓ | +0.0047 | -0.0094 | -0.0001 | +0.0071 | +0.0072 | +0.0070 | +0.0062 | +0.0153 | -0.8066 |

Synergy improves AUC in 21/21 runs, log loss in 21/21, ECE in 11/21, micro part accuracy in 21/21, team-macro accuracy in 21/21, game-macro accuracy in 21/21, bonus-question-macro accuracy in 21/21, exact accuracy in 21/21, and pooled-team PPB MAE in 21/21. Negative PPB deltas mean the synergy model is closer to each team's aggregate PPB.

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

**Bonus stage** - each observation is one bonus part (binary: converted or not).
The macro metrics first average those part-level correctness indicators within
each named group, then give every observed group one equal vote.

| Metric | Granularity | What it measures |
|---|---|---|
| **AUC** | bonus part | Ranking/discrimination - area under the ROC curve over per-part correct-vs-incorrect predictions. |
| **log_loss** | bonus part | Binary cross-entropy. |
| **ECE** | bonus part | Expected Calibration Error - gap between predicted probability and actual conversion rate, binned into 10 bins. |
| **part micro** | bonus part | Accuracy after thresholding at 0.5, with every response-part row receiving one vote. |
| **team macro** | team across evaluated run | Mean part accuracy within each team, averaged equally across observed teams. |
| **game macro** | game | Mean part accuracy within each game, averaged equally across observed games. |
| **bonus macro** | bonus question | Mean part accuracy across responses to each bonus question, averaged equally across observed questions. |
| **exact_acc** | team's bonus | Fraction of bonuses where all three thresholded part predictions exactly match the observed part outcomes. |
| **PPB MAE** | team across evaluated run | Pool all bonuses heard by each team, calculate observed and predicted PPB, then average absolute error across teams. |

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
