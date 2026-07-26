# Documentation

This directory contains the public reading path for the CompIRT implementation.
The repository root keeps the executable baseline model visible; these guides
explain how its data, equations, experiments, and evaluation fit together.

## Recommended reading order

1. [`../README.md`](../README.md) — setup, repository map, and the shortest
   route through the two-stage implementation.
2. [`compirt_deep_dive.md`](compirt_deep_dive.md) — root CompIRT data flow and
   equation-to-code map.
3. [`dataset-schema.md`](dataset-schema.md) and
   [`lineup-inference.md`](lineup-inference.md) — generated table contracts and
   the inferred game-lineup rules used by both model stages.
4. [`compirt-experiments.md`](compirt-experiments.md) — reproducible training,
   holdout, ablation, and evaluation commands.
5. [`../compirt_eval/METRICS.md`](../compirt_eval/METRICS.md) — the canonical
   metric equations, scored populations, aggregation order, and interpretation
   limits.
6. [`posterior-uncertainty.md`](posterior-uncertainty.md) — saved SVI parameter
   quantiles, aligned posterior draws, controls, and interpretation limits.

Model-family READMEs under `tfidf/`, `topic/`, `multidimensional/`, and
[`polynomial_compirt/`](../polynomial_compirt/README.md) document only the
terms that differ from the root model. The root mathematical model is kept as
the common reference rather than hidden behind a shared base class.

Maintainers can consult [`code-clarity-audit.md`](code-clarity-audit.md) for the
per-folder classification, resolved cleanup, deferred publication decisions,
and later path-move recommendations.

The source-paper PDFs are intentionally local and ignored by Git. Public paper
and citation links should be added once the final paper metadata is known.
