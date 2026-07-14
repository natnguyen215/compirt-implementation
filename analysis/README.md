# analysis/ — tools for slicing the baseline dimensionality sweep

This package answers one research question — **where do the multidimensional
CompIRT gains come from?** — by re-scoring the saved predictions of the
`results/compirt/holdout/baseline-ablation` sweep (the same baseline family at
skill dimensions m = 1…7). Nothing here retrains anything.

**Division of labor:** the code computes numbers, tables, CSVs and graphs; the
*human* reads them and writes the findings. The written analysis lives at
`results/analysis/FINDINGS.md` and is authored by hand — these modules exist so
every number in it can be regenerated and re-checked, not to generate prose.

## One module per question

Run each as a module from the repo root; each prints its key tables and writes
CSVs to `results/analysis/csvs/` (gitignored) and figures to
`results/analysis/graphs/` (committed).

| Module | Question |
| --- | --- |
| `python -m analysis.overall` | Headline metric series by dimension, plus the **reconciliation guardrail**: recomputed totals must match the sweep's own committed `tossup_metrics.csv` / `bonus_metrics.csv` (~1e-16), so every slice provably decomposes the same numbers the committed reports headline. |
| `python -m analysis.difficulty` | Do harder questions gain more? Three model-free difficulty definitions; the split-half one is leak-free and adjudicates. `--seed 42 7 123` re-checks the gradient across fold draws. |
| `python -m analysis.categories` | Do the dimensions capture topic specialization? Tossup-side category slice (via the HF `tossups` table) plus the within-player on-specialty concentration test with exogenous 2024 strength. |
| `python -m analysis.players` | Who gains — strong players or specialized profiles? Joint OLS of per-player gain on exogenous 2024 general skill vs multidim norm. |
| `python -m analysis.buzz_position` | Early vs late buzzes, with the Murphy decomposition separating calibration from discrimination. |

Shared plumbing: `data.py` (loaders, caching, category canonicalization, the
shared-observed-columns assertion), `metrics.py` (slice scoring via
`compirt_eval.metrics` — metrics are never reimplemented — plus the Murphy
decomposition), `figures.py` (plot styling and builders).

## Ground rules every module obeys

These are the traps this analysis has already fallen into once; the code is
structured so they are hard to re-commit.

1. **Rotation invariance.** The baseline model's latent axes are identified
   only up to rotation (`theta ~ N(0,I)`, `alpha ~ N(0,I)`, likelihood sees
   only `theta · alpha`). Any per-player statistic built from raw `theta_k`
   coordinates measures the arbitrary basis SVI landed in, not the player.
   Only norms, inner products, and the scalar dim-1 fit are allowed.
2. **Stage-2 loadings must be rotation-covariant for the baseline.** The
   baseline's bonus stage originally drew `alpha_b ~ Gamma(2,2)` — loadings
   confined to the positive orthant of Stage-1's rotation-arbitrary basis —
   which made every bonus number a basis lottery (rotating theta, which leaves
   Stage-1 predictions bit-identical, moved PPB MAE by more than the sweep's
   whole dim-1→7 spread; evidence under
   `results/compirt/holdout/baseline-ablation-{seedcheck,rotcheck,s1seed}/`).
   The fix: baseline Stage-2 now uses `alpha_b ~ Normal(0, I)`, matching its
   tossup stage, and the bonus series became monotone. If bonus metrics ever
   turn erratic across dimensions again, suspect reintroduced basis-dependence
   before believing them. (The `multidim_mirt` family keeps its Gamma `r` on
   purpose — positivity is what pins *its* basis and makes its dimensions
   interpretable.)
3. **Exogeneity.** Covariates read off the evaluated model or the scored
   labels can explain a gain because of the fit, not the player. Prefer the
   sweep's 2024 training leg (`dim_N/train/`) as the covariate source, or
   split-half estimates scored on the held-out fold.
4. **No confidence intervals, by design** (`compirt_eval/SCENARIO_C.md`). Every
   table carries sample sizes; monotonicity across the sweep is a *weak* noise
   filter (~1/64 false-positive rate per slice under pure noise), not a test.
   The real noise floors are the seed/rotation replicate runs above.
5. **Transductivity.** The "holdout" leg refits question parameters on 2025
   data and Stage 2 fits entirely on the 2025 labels it is scored on; only the
   player prior carries across years. Between-dimension comparisons are fair
   (every dimension is treated identically), but no number is pure
   generalization error.

## Gotchas

- Run as modules from the repo root (`python -m analysis.overall`), never from
  inside `analysis/`.
- `players.csv` has a `theta_norm` column matching the `theta_` prefix that is
  **not** a coordinate; `data.numbered_columns` filters on a digit suffix for
  this reason.
- `results/**/*.csv` is gitignored, so the CSV outputs will not show in
  `git status`. Intended — they regenerate from the commands above.
- The category vocabulary in the source data is dirty (`Pop Culture` vs
  `Popular Culture`, `Any History`, `Painting &amp; Sculpture`);
  `data.CATEGORY_CANON` canonicalizes it in every loader.
