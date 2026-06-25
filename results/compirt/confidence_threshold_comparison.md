# Confidence Threshold `c` — Platt Scaling vs. Uncalibrated

The buzz-reluctance parameter `c` inflates significantly without Platt scaling
because the model compensates for an overconfident correctness logit by raising
the threshold needed to trigger a buzz.

## Median and Mean `c` by Run

| Run | Topic source | Platt scaling | Median `c` | Mean `c` |
|---|---|:---:|---:|---:|
| `baseline-all2024-cal` | none | ✓ | 1.55 | 1.57 |
| `category-all2024-cal` | one-hot category 13d | ✓ | 3.12 | 3.18 |
| `lda-all2024-cal` | LDA 5d | ✓ | 3.61 | 3.67 |
| `learned-all2024-cal` | learned ProdLDA 5d | ✓ | 3.73 | 3.79 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 3.74 | 3.81 |
| `baseline-all2024-ard` | none (ARD) | ✗ | 5.01 | 4.76 |
| `lda-all2024` | LDA 5d | ✗ | 5.30 | 5.28 |
| `learned-all2024` | learned ProdLDA 5d | ✗ | 5.33 | 5.31 |
| `plda-all2024` | PLDA 5d | ✗ | 5.35 | 5.32 |
| `category-all2024` | one-hot category 13d | ✗ | 5.29 | 5.24 |

## Interpretation

Without Platt scaling the model has no dedicated knob to adjust the scale of the
correctness logit, so it pushes `c` to ~5 across all topic variants to suppress
buzzing until the logit is very large. Platt scaling adds a global `scale` and
`bias` that fix the overconfidence directly, allowing `c` to reflect actual
  buzz reluctance. 
 
