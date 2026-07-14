# Confidence Threshold And Parameter Comparison

**Scope.** These rows use the same 2024 in-sample run set as
`synergy_bonus_model_comparison.md`. Values are recomputed from saved artifacts
under `results/compirt/in_sample`: Stage 1 player/tossup CSVs and Stage 2
synergy summaries. Blank `scale`/`bias` cells mean the run is uncalibrated or the
saved pyramidal summary does not expose those fields.

The tables keep like quantities together. Multidimensional/topic/embedding
difficulty is scalarized into the same effective difficulty curve as the
single-difficulty runs; raw scalar `beta`/`gamma`/`mu` and raw vector-coordinate
`beta_k`/`gamma_k`/`mu_k` are reported in separate tables.

## Calibration And Player Parameters

| Run | Topic/source | cal | theta dims | scale | bias | Median c | Mean c | Median theta_norm | Mean theta_norm |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `all-2024` | none | ✗ | 5 |  |  | 4.99 | 4.74 | 1.66 | 1.71 |
| `baseline-all2024-cal` | none | ✓ | 5 | 0.395 | 2.513 | 1.57 | 1.58 | 2.12 | 2.14 |
| `plda-all2024` | PLDA 5d | ✗ | 5 |  |  | 5.21 | 5.15 | 2.06 | 2.21 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 5 | 0.396 | 1.921 | 3.61 | 3.64 | 2.38 | 2.46 |
| `lda-all2024` | LDA 5d | ✗ | 5 |  |  | 5.18 | 5.11 | 2.11 | 2.26 |
| `lda-all2024-cal` | LDA 5d | ✓ | 5 | 0.390 | 1.923 | 3.50 | 3.53 | 2.44 | 2.49 |
| `category-all2024` | one-hot category 13d | ✗ | 13 |  |  | 5.14 | 5.06 | 2.27 | 2.41 |
| `category-all2024-cal` | one-hot category 13d | ✓ | 13 | 0.288 | 1.836 | 3.07 | 3.07 | 2.29 | 2.30 |
| `learned-topic-all2024` | learned topic 5d | ✗ | 5 |  |  | 5.18 | 5.11 | 2.11 | 2.27 |
| `learned-topic-all2024-cal` | learned topic 5d | ✓ | 5 |  |  | 3.49 | 3.51 | 2.33 | 2.37 |
| `learned-topic-tfidf-all2024` | learned topic + TF-IDF 5d | ✗ | 5 |  |  | 5.67 | 5.64 | 2.37 | 2.38 |
| `learned-topic-tfidf-all2024-cal` | learned topic + TF-IDF 5d | ✓ | 5 | 0.330 | 1.718 | 3.78 | 3.79 | 2.46 | 2.48 |
| `embedding-all2024` | embedding relevance 5d | ✗ | 5 |  |  | 5.14 | 5.06 | 1.98 | 2.13 |
| `embedding-all2024-cal` | embedding relevance 5d | ✓ | 5 | 0.319 | 1.975 | 3.03 | 3.05 | 2.06 | 2.04 |
| `multidim-all2024` | multidim MIRT 5d | ✗ | 5 |  |  | 4.89 | 4.51 | 1.49 | 1.57 |
| `multidim-all2024-cal` | multidim MIRT 5d | ✓ | 5 | 0.303 | 2.297 | 1.01 | 1.06 | 1.78 | 1.78 |
| `tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | 5 |  |  | 5.11 | 4.90 | 1.74 | 1.87 |
| `tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | 5 | 0.307 | 2.141 | 1.54 | 1.61 | 2.27 | 2.30 |
| `tfidf-multidim-cumulative-difficulty-all2024` | TF-IDF multidim cumulative difficulty 5d | ✗ | 5 |  |  | 4.86 | 4.52 | 1.34 | 1.46 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | TF-IDF multidim cumulative difficulty 5d | ✓ | 5 | 0.310 | 2.382 | 0.99 | 1.01 | 1.77 | 1.80 |

## Tossup Weight Vectors

`alpha` is learned tossup discrimination in the scalar baseline/TF-IDF runs,
`r` is the multidim or embedding relevance vector, and `topic_weight` is the
topic mixture used in the fixed/learned-topic variants.
`max share` and `effective dims` are computed after normalizing absolute weights
within each tossup, so they describe how concentrated the vector is.

| Run | Weight vector | dims | Median norm | Mean norm | Median max share | Median effective dims |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `all-2024` | alpha | 5 | 1.78 | 1.80 | 0.417 | 3.35 |
| `baseline-all2024-cal` | alpha | 5 | 2.34 | 2.32 | 0.380 | 3.61 |
| `plda-all2024` | topic_weight | 5 | 0.67 | 0.69 | 0.610 | 2.21 |
| `plda-all2024-cal` | topic_weight | 5 | 0.67 | 0.69 | 0.610 | 2.21 |
| `lda-all2024` | topic_weight | 5 | 0.73 | 0.74 | 0.700 | 1.87 |
| `lda-all2024-cal` | topic_weight | 5 | 0.73 | 0.74 | 0.700 | 1.87 |
| `category-all2024` | topic_weight | 13 | 1.00 | 1.00 | 1.000 | 1.00 |
| `category-all2024-cal` | topic_weight | 13 | 1.00 | 1.00 | 1.000 | 1.00 |
| `learned-topic-all2024` | topic_weight | 5 | 0.84 | 0.81 | 0.832 | 1.42 |
| `learned-topic-all2024-cal` | topic_weight | 5 | 0.87 | 0.84 | 0.865 | 1.32 |
| `learned-topic-tfidf-all2024` | topic_weight | 5 | 0.80 | 0.79 | 0.793 | 1.55 |
| `learned-topic-tfidf-all2024-cal` | topic_weight | 5 | 0.86 | 0.83 | 0.852 | 1.36 |
| `embedding-all2024` | r | 5 | 1.00 | 0.93 | 0.999 | 1.00 |
| `embedding-all2024-cal` | r | 5 | 1.00 | 0.99 | 1.000 | 1.00 |
| `multidim-all2024` | r | 5 | 3.04 | 3.15 | 0.419 | 3.43 |
| `multidim-all2024-cal` | r | 5 | 3.27 | 3.31 | 0.373 | 3.87 |
| `tfidf-cumulative-difficulty-all2024` | alpha | 5 | 2.04 | 2.04 | 0.398 | 3.44 |
| `tfidf-cumulative-difficulty-all2024-cal` | alpha | 5 | 2.56 | 2.57 | 0.379 | 3.62 |
| `tfidf-multidim-cumulative-difficulty-all2024` | r | 5 | 3.15 | 3.26 | 0.457 | 3.27 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | r | 5 | 3.29 | 3.33 | 0.380 | 3.85 |

## Effective Difficulty Curves

For scalar-difficulty runs, `d(r) = beta * sigmoid(gamma * (mu - r))`. For
vector-difficulty runs, `d_eff(r) = sum_k w_k * beta_k * sigmoid(gamma_k *
(mu_k - r))`, where `w` is `alpha`, `r`, or `topic_weight`. TF-IDF runs include
their saved TF-IDF difficulty delta. This is the cross-run table to
use when comparing multidimensional difficulty against single-difficulty runs.

| Run | Difficulty form | Median d(10%) | Median d(50%) | Median d(90%) | Mean d(50%) | Median effective mu |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `all-2024` | scalar | 3.34 | 2.61 | 0.09 | 2.40 | 0.610 |
| `baseline-all2024-cal` | scalar | 3.79 | 3.20 | 0.21 | 2.95 | 0.656 |
| `plda-all2024` | vector/topic_weight | 2.65 | 2.03 | 0.04 | 1.84 | 0.580 |
| `plda-all2024-cal` | vector/topic_weight | 3.16 | 2.71 | 0.19 | 2.54 | 0.644 |
| `lda-all2024` | vector/topic_weight | 2.77 | 2.13 | 0.05 | 1.94 | 0.583 |
| `lda-all2024-cal` | vector/topic_weight | 3.33 | 2.87 | 0.25 | 2.70 | 0.648 |
| `category-all2024` | vector/topic_weight | 3.19 | 2.37 | 0.08 | 2.20 | 0.598 |
| `category-all2024-cal` | vector/topic_weight | 4.25 | 3.50 | 0.65 | 3.47 | 0.708 |
| `learned-topic-all2024` | vector/topic_weight | 2.95 | 2.26 | 0.05 | 2.08 | 0.590 |
| `learned-topic-all2024-cal` | vector/topic_weight | 3.70 | 3.16 | 0.36 | 2.98 | 0.666 |
| `learned-topic-tfidf-all2024` | vector/topic_weight+topic_tfidf_delta | 2.11 | 0.83 | -1.75 | 0.74 | 0.693 |
| `learned-topic-tfidf-all2024-cal` | vector/topic_weight+topic_tfidf_delta | 3.42 | 2.64 | -0.10 | 2.54 | 0.692 |
| `embedding-all2024` | vector/r | 3.18 | 2.38 | 0.09 | 2.22 | 0.599 |
| `embedding-all2024-cal` | vector/r | 4.17 | 3.56 | 0.70 | 3.43 | 0.712 |
| `multidim-all2024` | vector/r | 5.56 | 3.65 | 0.83 | 3.65 | 0.557 |
| `multidim-all2024-cal` | vector/r | 6.11 | 4.15 | 1.02 | 4.15 | 0.571 |
| `tfidf-cumulative-difficulty-all2024` | scalar+tfidf_delta | 2.21 | 0.71 | -2.16 | 0.60 | 0.722 |
| `tfidf-cumulative-difficulty-all2024-cal` | scalar+tfidf_delta | 3.04 | 1.94 | -1.22 | 1.82 | 0.707 |
| `tfidf-multidim-cumulative-difficulty-all2024` | vector/r+tfidf_delta | 5.15 | 3.16 | 0.35 | 3.19 | 0.556 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | vector/r+tfidf_delta | 6.04 | 3.98 | 0.90 | 4.06 | 0.573 |

## Scalar Difficulty Parameters

Only runs that truly save scalar `beta`, `gamma`, and `mu` appear here.

| Run | Median beta | Mean beta | Median gamma | Mean gamma | Median mu | Mean mu |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `all-2024` | 3.40 | 3.36 | 12.84 | 51.33 | 0.610 | 0.604 |
| `baseline-all2024-cal` | 3.84 | 3.80 | 12.44 | 41.07 | 0.656 | 0.649 |
| `tfidf-cumulative-difficulty-all2024` | 2.56 | 2.53 | 12.14 | 59.33 | 0.722 | 0.705 |
| `tfidf-cumulative-difficulty-all2024-cal` | 3.24 | 3.26 | 13.47 | 58.79 | 0.707 | 0.700 |

## Vector Difficulty Coordinate Parameters

These are raw per-coordinate difficulty parameters for vector-difficulty runs.
They are useful for within-family diagnostics, but the effective-difficulty
table above is the comparable scalar view across all runs.

| Run | Weight vector | dims | Median beta_k | Mean beta_k | Median gamma_k | Mean gamma_k | Median mu_k | Mean mu_k |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `plda-all2024` | topic_weight | 5 | 0.32 | 1.08 | 5.44 | 21.14 | 0.504 | 0.529 |
| `plda-all2024-cal` | topic_weight | 5 | 0.48 | 1.33 | 5.50 | 16.73 | 0.511 | 0.556 |
| `lda-all2024` | topic_weight | 5 | 0.22 | 0.99 | 5.32 | 20.30 | 0.503 | 0.527 |
| `lda-all2024-cal` | topic_weight | 5 | 0.32 | 1.23 | 5.33 | 15.62 | 0.508 | 0.549 |
| `category-all2024` | topic_weight | 13 | 0.01 | 0.25 | 5.04 | 8.61 | 0.501 | 0.507 |
| `category-all2024-cal` | topic_weight | 13 | 0.00 | 0.33 | 5.03 | 6.65 | 0.501 | 0.516 |
| `learned-topic-all2024` | topic_weight | 5 | 0.18 | 0.91 | 5.19 | 18.59 | 0.502 | 0.523 |
| `learned-topic-all2024-cal` | topic_weight | 5 | 0.20 | 1.09 | 5.19 | 13.62 | 0.505 | 0.542 |
| `learned-topic-tfidf-all2024` | topic_weight | 5 | 0.19 | 0.78 | 5.12 | 16.27 | 0.503 | 0.547 |
| `learned-topic-tfidf-all2024-cal` | topic_weight | 5 | 0.20 | 1.04 | 5.17 | 14.03 | 0.505 | 0.548 |
| `embedding-all2024` | r | 5 | 0.02 | 0.74 | 5.12 | 15.22 | 0.502 | 0.523 |
| `embedding-all2024-cal` | r | 5 | 0.02 | 0.86 | 5.09 | 9.81 | 0.503 | 0.541 |
| `multidim-all2024` | r | 5 | 0.61 | 0.79 | 5.09 | 14.47 | 0.482 | 0.512 |
| `multidim-all2024-cal` | r | 5 | 0.75 | 0.87 | 5.17 | 11.58 | 0.509 | 0.538 |
| `tfidf-multidim-cumulative-difficulty-all2024` | r | 5 | 0.56 | 0.71 | 5.07 | 13.21 | 0.475 | 0.505 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | r | 5 | 0.74 | 0.85 | 5.20 | 10.38 | 0.506 | 0.536 |

## Bonus Synergy Scalars

These values come from each run's Stage 2 synergy summary.

| Run | Topic/source | cal | synergy dims | tau | Mean synergy | Median synergy | Positive frac. | Negative frac. |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `all-2024` | none | ✗ | 3 | 0.539 | -0.739 | -0.727 | 0.158 | 0.811 |
| `baseline-all2024-cal` | none | ✓ | 3 | 0.591 | 0.214 | 0.079 | 0.602 | 0.367 |
| `plda-all2024` | PLDA 5d | ✗ | 3 | 0.327 | -0.848 | -0.746 | 0.082 | 0.886 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 3 | 0.563 | 0.064 | 0.007 | 0.543 | 0.426 |
| `lda-all2024` | LDA 5d | ✗ | 3 | 0.356 | -0.889 | -0.797 | 0.076 | 0.893 |
| `lda-all2024-cal` | LDA 5d | ✓ | 3 | 0.623 | 0.044 | 0.005 | 0.529 | 0.439 |
| `category-all2024` | one-hot category 13d | ✗ | 3 | 0.361 | -0.707 | -0.604 | 0.144 | 0.825 |
| `category-all2024-cal` | one-hot category 13d | ✓ | 3 | 0.706 | 0.091 | 0.010 | 0.556 | 0.413 |
| `learned-topic-all2024` | learned topic 5d | ✗ | 3 | 0.332 | -0.857 | -0.757 | 0.084 | 0.885 |
| `learned-topic-all2024-cal` | learned topic 5d | ✓ | 3 | 0.516 | 0.081 | 0.017 | 0.570 | 0.399 |
| `learned-topic-tfidf-all2024` | learned topic + TF-IDF 5d | ✗ | 3 | 0.356 | -0.204 | -0.062 | 0.366 | 0.603 |
| `learned-topic-tfidf-all2024-cal` | learned topic + TF-IDF 5d | ✓ | 3 | 0.521 | 0.060 | 0.009 | 0.566 | 0.402 |
| `embedding-all2024` | embedding relevance 5d | ✗ | 3 | 0.390 | -0.941 | -0.795 | 0.088 | 0.880 |
| `embedding-all2024-cal` | embedding relevance 5d | ✓ | 3 | 0.582 | 0.109 | 0.023 | 0.579 | 0.389 |
| `multidim-all2024` | multidim MIRT 5d | ✗ | 3 | 0.519 | -0.686 | -0.688 | 0.195 | 0.774 |
| `multidim-all2024-cal` | multidim MIRT 5d | ✓ | 3 | 0.699 | 0.104 | 0.021 | 0.544 | 0.425 |
| `tfidf-cumulative-difficulty-all2024` | TF-IDF cumulative difficulty 5d | ✗ | 3 | 0.712 | -0.514 | -0.252 | 0.321 | 0.648 |
| `tfidf-cumulative-difficulty-all2024-cal` | TF-IDF cumulative difficulty 5d | ✓ | 3 | 0.680 | -0.065 | 0.001 | 0.505 | 0.464 |
| `tfidf-multidim-cumulative-difficulty-all2024` | TF-IDF multidim cumulative difficulty 5d | ✗ | 3 | 0.254 | -0.925 | -0.782 | 0.110 | 0.858 |
| `tfidf-multidim-cumulative-difficulty-all2024-cal` | TF-IDF multidim cumulative difficulty 5d | ✓ | 3 | 0.949 | 0.207 | 0.065 | 0.602 | 0.366 |

## Interpretation

Without correctness calibration, the fitted confidence threshold `c` stays near
5 across most families. Calibration gives the model explicit `scale`/`bias`
parameters for the correctness logit, so `c` no longer has to absorb that
calibration problem. The drop is largest in the multidim and TF-IDF multidim
runs, where calibrated median `c` is about 1.

The synergy summaries move in the same direction: uncalibrated synergy
contributions are usually negative, while calibrated runs are near zero or
positive with a much larger positive fraction. The effective-difficulty table
keeps scalar and multidimensional difficulty comparable; the raw `gamma` and
`mu` tables are split by parameter form so coordinate-valued vector difficulty
is not treated as the same object as scalar difficulty.

## Column Notes

`Median max share` measures how concentrated a tossup's weight vector is in its
largest coordinate. For a weight vector `w`, the report first normalizes absolute
weights as `p_k = abs(w_k) / sum_j abs(w_j)`, then takes `max_k p_k`. A value
near 1 means one dimension dominates the tossup; lower values mean the tossup is
spread across several dimensions. The table reports the median of that quantity
across tossups.

`Median effective dims` is another concentration summary for the same normalized
weights. It uses `1 / sum_k p_k^2`, the inverse participation ratio. A one-hot
vector has effective dimension 1, while a perfectly even 5-dimensional vector
has effective dimension 5. Intermediate values mean the weight mass behaves like
that many evenly used dimensions; for example, 3.5 means the typical tossup is
using roughly three to four dimensions' worth of weight mass.

`Effective difficulty` means the single difficulty curve actually subtracted
from skill after combining any vector-valued difficulty coordinates. Scalar
runs already have one curve: `d(r) = beta * sigmoid(gamma * (mu - r))`. Vector
runs compute one curve per coordinate and combine them with the tossup weights:
`d_eff(r) = sum_k w_k * beta_k * sigmoid(gamma_k * (mu_k - r))`. TF-IDF
cumulative runs then add their saved TF-IDF difficulty adjustment. This is why
the effective-difficulty table can compare scalar, topic, embedding, multidim,
and TF-IDF variants in the same units.
