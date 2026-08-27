# Ablations

One factor changed at a time, against [`../reference-model/`](../reference-model/)
(Bernstein degree 3, 3 relevance curves, simplex prior with Dirichlet
concentration 2.0, learned curve locations, terminal intercepts, 3,000 steps).
The reference itself is **not** duplicated in here — it is the missing cell in
every table below.

| Folder | Factor | Reference value | Verdict |
| --- | --- | --- | --- |
| [`hyperparameter-grid/`](hyperparameter-grid/) | degree 3-6 x dimensions 1-5 x concentration 0.67-2.0, 100 points | — | See [`aggregate/summary.md`](hyperparameter-grid/aggregate/summary.md). Run **without** terminal intercepts, so not drop-in comparable to the reference. §3.7 |
| [`terminal-cell-intercepts/`](terminal-cell-intercepts/) | `off/` vs `on/` | on | On is better on joint LL, no-buzz calibration, final-decile mass and position MAE under both priors. §3.2 |
| [`relevance-prior/`](relevance-prior/) | `gamma-2-2/`, `dirichlet-concentration-0.67/` | Dirichlet 2.0 (simplex) | Simplex beats Gamma on accuracy and correctness LL; Gamma keeps better timing. Concentration 0.67 is a small, not decisive, gain. §3.5-3.6 |
| [`optimization-steps/`](optimization-steps/) | `steps-6000/`, `steps-20000/` | 3,000 | Joint event LL is still improving at 20,000 steps — **the 3,000-step fits have not converged**. Treat every equal-budget comparison accordingly. |
| [`incorrect-loss-weight/`](incorrect-loss-weight/) | `weight-1.5`, `weight-2`, `weight-3` | 1x | Upweighting incorrect responses monotonically degrades correctness LL, ECE and accuracy while leaving position MAE flat. §3.11 |
