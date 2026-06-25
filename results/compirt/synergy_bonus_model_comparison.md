# Synergy-Model Bonus Metrics — Run Comparison

**Scope.** All six runs use the *synergy* variant of the CompIRT bonus model on the
full 2024 dataset (`baseline-all2024`). They differ along the **topic source**
fed to the model and whether the **correctness-calibration flag (`cal`)** is on.
The goal of the comparison is to separate the effect of (a) adding topic structure
and (b) calibrating the correctness head.

> **Important caveat.** Every number below is computed **in-sample**  Lower is better for `log_loss`, `ECE`, and `PPB MAE`; higher is
> better for `AUC`, `part_acc`, `exact_acc`, and `acc`.

## Bonus Stage Metrics (Stage 2)

| Run | Topic source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | part_acc ↑ | exact_acc ↑ | PPB MAE ↓ |
|---|---|:--:|--:|--:|--:|--:|--:|--:|
| `baseline-all2024` (baseline) | none | ✗ | **0.9390** | **0.3289** | 0.0449 | **0.8579** | **0.6242** | 1.8091 |
| `baseline-all2024-cal` | none | ✓ | 0.9326 | 0.3388 | 0.0358 | 0.8512 | 0.6098 | **1.7920** |
| `plda-all2024` | PLDA 5d | ✗ | 0.9129 | 0.3950 | 0.0658 | 0.8336 | 0.5717 | 1.9077 |
| `lda-all2024` | LDA 5d | ✗ | 0.9153 | 0.3866 | 0.0585 | 0.8351 | 0.5750 | 1.8934 |
| `category-all2024` | one-hot category 13d | ✗ | 0.9178 | 0.3716 | 0.0367 | 0.8365 | 0.5805 | 1.8583 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 0.9172 | 0.3673 | **0.0207** | 0.8367 | 0.5852 | 1.7977 |

Bold marks the best value in each column.

## Tossup Stage Metrics (Stage 1)

Tossup metrics come from the pyramidal model (Stage 1), which is shared across the
synergy and no-synergy evaluations. The `cal` flag applies to Stage 1 as well as
Stage 2 — it adds Platt scaling to the tossup correctness head — so calibrated runs
differ from uncalibrated ones here too.

| Run | Topic source | `cal` | AUC ↑ | log_loss ↓ | ECE ↓ | acc ↑ |
|---|---|:--:|--:|--:|--:|--:|
| `baseline-all2024` (baseline) | none | ✗ | **0.7041** | 0.5811 | 0.1463 | 0.7082 |
| `baseline-all2024-cal` | none | ✓ | 0.6650 | **0.5106** | **0.0073** | **0.7711** |
| `plda-all2024` | PLDA 5d | ✗ | 0.6644 | 0.6126 | 0.1824 | 0.6762 |
| `lda-all2024` | LDA 5d | ✗ | 0.6650 | 0.6132 | 0.1802 | 0.6768 |
| `category-all2024` | one-hot category 13d | ✗ | 0.6750 | 0.6259 | 0.1935 | 0.6774 |
| `plda-all2024-cal` | PLDA 5d | ✓ | 0.6330 | 0.5223 | 0.0098 | 0.7677 |

Bold marks the best value in each column.

Notable patterns:

- **Calibration collapses ECE and lifts accuracy.** Both calibrated runs drop ECE by
  ~0.15 and gain ~0.06–0.09 accuracy versus their uncalibrated counterparts. AUC
  falls slightly — Platt scaling cannot re-rank, so discrimination is unchanged by
  construction, and the small AUC drop reflects the rescaling interacting with the
  threshold-free ranking.
- The uncalibrated baseline's numbers are overconfident: best AUC but worst ECE (0.1463) 

## What the `cal` flag does

`cal` is the `calibrate_correctness` option. With it **off**, a team's probability of
converting a bonus part is

```
P(correct) = sigmoid( team_ability − part_difficulty + synergy )
```

With it **on**, the model learns **two extra global scalars** — a `scale` and a `bias` —
and passes the logit through them before the sigmoid:

```
P(correct) = sigmoid( scale · (team_ability − part_difficulty + synergy) + bias )
```

This is standard **Platt / temperature scaling**: a single shared stretch-and-shift
applied to *every* prediction. It rescales how confident the probabilities are so
they line up with observed conversion rates. (Priors: `scale ~ LogNormal(0, 0.5)`,
`bias ~ Normal(0, 3)`.) 

The same scaling is applied to the tossup correctness head in Stage 1.

Without calibration the bonus correctness head inherits its
scale from elsewhere in the model and comes out *over-confident*, which inflates ECE.


> **Side effect worth noting.** Calibration also significantly affects the synergy term.
> Mean per-row synergy contribution goes from **−0.70** (baseline, 81% of rows
> negative) to **+0.42** (`baseline-all2024-cal`); for PLDA it goes from **−0.84** to
> **+0.17**.  

## Metrics

**Bonus stage** — each observation is one bonus part (binary: converted or not); team/game metrics aggregate up.

| Metric | Granularity | What it measures |
|---|---|---|
| **AUC** | bonus part | Ranking/discrimination — area under the ROC curve over per-part correct-vs-incorrect predictions. |
| **log_loss** | bonus part | Binary cross-entropy.  |
| **ECE** | bonus part | Expected Calibration Error — gap between predicted probability and actual conversion rate, binned into 10 bins.|
| **part_acc** | bonus part | Accuracy after thresholding the predicted probability at 0.5. |
| **exact_acc** | team's bonus | Fraction of bonuses where the predicted total, snapped to {0,10,20,30}, exactly equals the observed total. |
| **PPB MAE** | team's game | Mean absolute error of points-per-bonus, averaged over every bonus a team heard in a game. |

**Tossup stage** — each observation is one first-buzz event (binary: correct or not).

| Metric | Granularity | What it measures |
|---|---|---|
| **AUC** | first buzz | Ranking/discrimination over tossup correctness predictions. |
| **log_loss** | first buzz | Binary cross-entropy. |
| **ECE** | first buzz | Expected Calibration Error on tossup correctness probabilities. |
| **acc** | first buzz | Accuracy after thresholding the predicted correctness probability at 0.5. |
