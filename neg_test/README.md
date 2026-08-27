# Neg + buzz-timing model comparison

Which Stage-1 difficulty-curve / calibration variant best predicts whether a buzz
is a neg, and when the buzz happens?

`run_neg_test.py` runs a 5-fold game holdout over `year_2024`. For each fold it
fits Stage 1 on the train games, then runs the held-out pass on the test games
with those player priors (question params co-estimated transductively on the
test split — the player posterior is the only cross-fold information). No
Stage-2 / bonus step is needed: every metric here comes from the held-out
Stage-1 tossup predictions.

```bash
.venv/bin/python -m neg_test.run_neg_test          # train + held-out + aggregate
STAGE=aggregate .venv/bin/python -m neg_test.run_neg_test   # re-collect only
```

Outputs land in
`results/compirt/holdout/common/neg-test/{config}/fold{k}/{train,holdout}/pyramidal/`,
with `summary.csv` (5-fold mean/std) and `summary_by_fold.csv` at the root.
Env knobs: `DEVICE GPU DIMENSIONS PYR_STEPS LR SEED N_FOLDS CONFIGS FOLDS RERUN
STAGE`. All configs below are 5 dimensions, 3000 steps, lr 0.01, seed 42.

Config names are a difficulty-curve family (`multidim`, `ta-*` from
`test_additions`, `bernstein-drop2` from `polynomial_compirt`) plus a
correctness-calibration suffix: no suffix is uncalibrated, `-cal` adds the
constant Platt scale+bias, and `-cal-noscale` keeps only the additive bias.
`CONFIGS` in `run_neg_test.py` holds the exact flags.

## Headline: 5-fold mean (std)

`neg_gap` = |observed neg rate − predicted neg rate| over held-out first buzzes.
`log_loss` / `ece` / `auc` are on the binary correct-vs-neg outcome of those
buzzes. `pos_mae` is mean absolute error of predicted relative buzz position.

| config | neg_gap ↓ | log_loss ↓ | ece ↓ | auc ↑ | pos_mae ↓ |
|---|---|---|---|---|---|
| multidim | .1453 (.0064) | .5686 (.0109) | .1453 (.0064) | .7164 (.0061) | .1345 (.0012) |
| multidim-cal | **.0112** (.0013) | .5241 (.0085) | **.0189** (.0029) | .6331 (.0143) | .1250 (.0014) |
| multidim-cal-noscale | .0484 (.0014) | .4787 (.0107) | .0565 (.0032) | .7576 (.0078) | .1286 (.0014) |
| per-position-cal | .0201 (.0026) | .5217 (.0076) | .0257 (.0020) | .6455 (.0117) | .1276 (.0011) |
| ta-timing | .1569 (.0063) | .5690 (.0105) | .1569 (.0063) | .7224 (.0072) | .1368 (.0012) |
| ta-timing-cal | .0206 (.0025) | .5227 (.0070) | .0302 (.0009) | .6459 (.0096) | .1237 (.0014) |
| ta-timing-cal-noscale | .0733 (.0011) | .4803 (.0102) | .0736 (.0015) | **.7651** (.0078) | .1257 (.0014) |
| ta-both | .0251 (.0019) | .5216 (.0077) | .0254 (.0017) | .6466 (.0110) | .1245 (.0012) |
| bernstein-drop2 | .1024 (.0071) | .5578 (.0139) | .1236 (.0062) | .7234 (.0093) | **.1194** (.0010) |
| bernstein-drop2-cal-noscale | .0135 (.0006) | **.4654** (.0103) | .0216 (.0034) | .7571 (.0081) | .1290 (.0017) |

## Predicting negs

The uncalibrated models miss the held-out neg rate by 10–16 points (`multidim`,
`ta-timing`, `bernstein-drop2`, `neg_gap` .1024–.1569), and their ECE equals that
gap almost exactly, so the error is a uniform level shift rather than a shape
problem. Any Platt correction removes it.

Full calibration (`--calibrate-correctness`) fits a scale around 0.23, which
squashes the correctness-logit spread toward a constant. That buys the best raw
calibration (`multidim-cal` neg_gap .0112, ece .0189) at the cost of
discrimination: AUC falls from .7164 to .6331. `ta-timing-cal` (.7224 → .6459)
and `ta-both` (.6466) behave the same way. These configs predict the *average*
neg rate well and individual negs poorly.

Bias-only calibration (`--calibration-no-scale`) removes the level shift while
leaving the logit spread intact, so calibration and discrimination improve
together:

| | neg_gap | log_loss | auc |
|---|---|---|---|
| multidim → cal-noscale | .1453 → .0484 | .5686 → .4787 | .7164 → **.7576** |
| ta-timing → cal-noscale | .1569 → .0733 | .5690 → .4803 | .7224 → **.7651** |
| bernstein-drop2 → cal-noscale | .1024 → **.0135** | .5578 → **.4654** | .7234 → **.7571** |

`bernstein-drop2-cal-noscale` predicts negs best overall: the best log loss
(.4654) of any config, a neg gap (.0135) within noise of the scale-calibrated
best (.0112), an ECE (.0216) essentially tied with it, and AUC held at .7571
instead of falling to .6331. It is the only config in the top three on all four
correctness metrics. The monotone Bernstein curve also responds better to
bias-only calibration than the sigmoid families do — its residual miscalibration
after the shift is .0135, against .0484 and .0733.

`per-position-cal` (position-varying calibration, no timing change) behaves like
the scale-calibrated configs: good gap (.0201), poor AUC (.6455). Letting
calibration vary with position does not recover the discrimination the scale
costs.

## Predicting buzz position

`buzz_event_predictions.csv` stores `predicted_relative_position` =
E[t | a buzz occurs] per event. Pooled over all 5 held-out folds: 45,995
first-buzz events.

Observed buzzes are heavily back-loaded — d1 has 101 events, d10 has 8,145:

| decile | d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 | d9 | d10 |
|---|---|---|---|---|---|---|---|---|---|---|
| n | 101 | 817 | 1666 | 3032 | 4921 | 6097 | 7083 | 7349 | 6784 | 8145 |
| observed mean pos | .079 | .155 | .256 | .353 | .455 | .552 | .652 | .749 | .850 | .967 |

### MAE by observed decile

| config | d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 | d9 | d10 | ALL |
|---|---|---|---|---|---|---|---|---|---|---|---|
| multidim | .323 | .293 | .201 | .146 | .093 | **.070** | .076 | .105 | .155 | .231 | .134 |
| multidim-cal | .352 | .327 | .237 | .175 | .112 | .080 | .069 | .083 | .123 | .190 | .125 |
| multidim-cal-noscale | .341 | .312 | .221 | .163 | .107 | .080 | .074 | .092 | .133 | .202 | .129 |
| per-position-cal | .318 | .298 | .210 | .152 | .098 | .075 | .077 | .097 | .138 | .203 | .128 |
| ta-timing | **.290** | **.267** | **.178** | **.125** | **.087** | .074 | .088 | .121 | .168 | .226 | .137 |
| ta-timing-cal | .322 | .296 | .205 | .151 | .101 | .080 | .082 | .100 | .133 | .173 | .124 |
| ta-timing-cal-noscale | .318 | .291 | .202 | .147 | .103 | .083 | .084 | .102 | .137 | .177 | .126 |
| ta-both | .321 | .296 | .202 | .151 | .102 | .082 | .082 | .101 | .134 | .175 | .124 |
| bernstein-drop2 | .355 | .334 | .249 | .198 | .144 | .111 | .087 | **.076** | **.083** | **.128** | **.119** |
| bernstein-drop2-cal-noscale | .368 | .343 | .252 | .195 | .135 | .096 | **.073** | **.076** | .113 | .187 | .129 |

`bernstein-drop2` has the best overall MAE (.119) by trading the ends: it is the
worst config in d1–d6 and the best in d8–d10. Because 64% of real buzzes land in
d7–d10, that trade nets out positive. On d10 it cuts MAE ~45% against `multidim`
(.128 vs .231) and ~26% against the best test_additions variant (.173).

`ta-timing` is the mirror image — best in d1–d5, worst in d9–d10, and worst
overall (.137).

### Mean predicted position within each observed decile

| config | d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 | d9 | d10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **OBSERVED** | **.079** | **.155** | **.256** | **.353** | **.455** | **.552** | **.652** | **.749** | **.850** | **.967** |
| multidim | .396 | .448 | .455 | .489 | .522 | .567 | .609 | .652 | .696 | .735 |
| multidim-cal | .423 | .481 | .492 | .521 | .550 | .592 | .636 | .682 | .729 | .776 |
| multidim-cal-noscale | .413 | .467 | .475 | .508 | .538 | .582 | .627 | .672 | .718 | .764 |
| per-position-cal | .389 | .453 | .463 | .494 | .523 | .567 | .614 | .663 | .713 | .764 |
| ta-timing | .363 | .422 | .430 | .463 | .501 | .547 | .592 | .636 | .682 | .740 |
| ta-timing-cal | .393 | .451 | .457 | .491 | .524 | .571 | .617 | .665 | .719 | .794 |
| ta-timing-cal-noscale | .391 | .446 | .453 | .485 | .521 | .571 | .617 | .663 | .715 | .790 |
| ta-both | .392 | .451 | .455 | .489 | .521 | .570 | .616 | .663 | .718 | .792 |
| bernstein-drop2 | .428 | .488 | .502 | .541 | .578 | .630 | .680 | .731 | **.787** | **.840** |
| bernstein-drop2-cal-noscale | .441 | .497 | .507 | .541 | .574 | .617 | .661 | .702 | .744 | .780 |

Observed spans .079 → .967 (range .89). `multidim` spans only .396 → .735
(range .34); `bernstein-drop2` spans .428 → .840 (range .41). Every model is
compressed toward the middle of the question. Bernstein is compressed less and
centered later, which is where its late-decile advantage comes from.

Bias (predicted − observed) shows the same thing as a zero-crossing: bernstein's
sits at d8, everything else at d6–d7.

| config | d5 | d6 | d7 | d8 | d9 | d10 | ALL |
|---|---|---|---|---|---|---|---|
| multidim | +.067 | +.014 | −.042 | −.097 | −.154 | −.231 | −.054 |
| ta-both | +.066 | +.018 | −.035 | −.086 | −.132 | −.175 | −.038 |
| bernstein-drop2 | +.123 | +.078 | +.029 | −.018 | −.063 | −.126 | **+.022** |

### Distribution of predicted positions

| config | mean | sd | p05 | median | p95 |
|---|---|---|---|---|---|
| **OBSERVED** | **.674** | **.218** | **.287** | **.690** | **.993** |
| multidim | .619 | .128 | .397 | .627 | .817 |
| multidim-cal | .651 | .128 | .424 | .662 | .839 |
| multidim-cal-noscale | .640 | .131 | .408 | .651 | .833 |
| per-position-cal | .630 | .134 | .396 | .640 | .831 |
| ta-timing | .605 | .137 | .369 | .610 | .820 |
| ta-timing-cal | .638 | .143 | .389 | .645 | .854 |
| ta-timing-cal-noscale | .635 | .145 | .381 | .645 | .853 |
| ta-both | .636 | .144 | .384 | .645 | .854 |
| bernstein-drop2 | **.695** | **.152** | .420 | **.712** | **.918** |
| bernstein-drop2-cal-noscale | .669 | .129 | .438 | .682 | .866 |

Share of buzzes predicted into each decile vs observed (%):

| | d4 | d5 | d6 | d7 | d8 | d9 | d10 |
|---|---|---|---|---|---|---|---|
| **OBSERVED** | 6.6 | 10.7 | 13.3 | 15.4 | 16.0 | 14.7 | **17.7** |
| multidim | 4.2 | 12.6 | 24.4 | 29.5 | 21.1 | 6.7 | 0.4 |
| ta-both | 4.7 | 12.3 | 20.6 | 25.0 | 22.3 | 13.0 | 0.8 |
| bernstein-drop2 | 3.0 | 7.3 | 14.3 | 21.6 | 25.7 | 19.7 | **7.5** |

`bernstein-drop2` is the only config putting non-trivial mass in the last decile
(7.5% vs ≤0.9%), which is where the observed mode is. Total variation from the
observed histogram: bernstein-drop2 43.8 pp (best), ta-timing-cal-noscale 49.0,
multidim 64.6 (worst).

## Takeaways

- For neg probability, use `bernstein-drop2-cal-noscale`: best log loss (.4654),
  neg gap .0135, AUC .7571. Prefer bias-only to the multiplicative scale, which
  costs most of the discrimination for a calibration gain the bias alone
  already delivers.
- For buzz timing, use `bernstein-drop2` uncalibrated: best MAE (.119), best
  late-decile accuracy, least compressed predicted distribution.
- Those are two different fits. Adding bias-only calibration to bernstein
  recompresses timing (d10 predicted mass 7.5% → 2.6%, MAE .119 → .129), so pick
  per use case or fit both.
- Every config under-disperses buzz position (observed sd .218, best model .152).
  That is partly structural — `predicted_relative_position` is a per-event
  conditional mean and cannot reproduce within-event spread — so the decile
  histogram comparison partly measures which model shrinks least, not only which
  is best calibrated.

## On `--drop-concentration`

The bernstein configs use `--degree 5 --drop-concentration 2.0`. That flag is the
symmetric Dirichlet concentration on `drop_proportions` in
[`polynomial_compirt/pyramidal_model.py`](../polynomial_compirt/pyramidal_model.py) —
it sets *where along the question* the difficulty drop happens, not how large the
drop is (`total_drop` is a separate LogNormal). Small α concentrates the drop
into one segment (a difficulty cliff); large α spreads it evenly (a ramp).

In-sample `year_2024` fits at degree 5 / dim 5 (`results/compirt/in_sample/polynomial/`)
show α trades the same axis as everything else here — later predictions vs.
better calibration, with AUC untouched:

| α | tossup log loss | ece | auc | pos MAE | pos bias | share of drop in final segment |
|---|---|---|---|---|---|---|
| 0.1 | .6015 | .1515 | .6912 | .1289 | +.0385 | .541 |
| 0.5 | .5786 | .1310 | .6916 | .1275 | +.0298 | .433 |
| 2.0 | .5594 | .1120 | .6947 | .1270 | +.0070 | .278 |

α = 2.0 is the right default: strictly better calibration at equal
discrimination and equal timing MAE. (Caveat: the α = 0.1 run used 2000 steps vs
3000 for the other two, so part of its correctness deficit is under-training.)
