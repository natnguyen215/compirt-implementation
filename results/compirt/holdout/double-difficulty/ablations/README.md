# Ablations

Each experiment changes one factor relative to [`../reference-model/`](../reference-model/)
(Bernstein degree 3, 3 relevance curves, simplex prior with Dirichlet
concentration 2.0, learned curve locations, terminal intercepts, 3,000 steps).
The reference run is not duplicated in this directory.

| Folder | Factor | Reference value | Result |
| --- | --- | --- | --- |
| [`hyperparameter-grid/`](hyperparameter-grid/) | degree 3–6, dimensions 1–5, concentration 0.67–2.0; 100 points | — | See [`aggregate/summary.md`](hyperparameter-grid/aggregate/summary.md). The grid omits terminal intercepts and is not directly comparable with the reference. §3.7 |
| [`terminal-cell-intercepts/`](terminal-cell-intercepts/) | `off/` vs `on/` | on | Terminal intercepts improve joint LL, no-buzz calibration, final-decile mass, and position MAE under both priors. §3.2 |
| [`relevance-prior/`](relevance-prior/) | `gamma-2-2/`, `dirichlet-concentration-0.67/` | Dirichlet 2.0 (simplex) | Simplex improves accuracy and correctness LL; Gamma improves timing. The concentration-0.67 gain is small. §3.5–3.6 |
| [`optimization-steps/`](optimization-steps/) | `steps-6000/`, `steps-20000/` | 3,000 | Joint event LL continues to improve at 20,000 steps; the 3,000-step fits have not converged. |
| [`incorrect-loss-weight/`](incorrect-loss-weight/) | `weight-1.5`, `weight-2`, `weight-3` | 1x | Upweighting incorrect responses monotonically degrades correctness LL, ECE and accuracy while leaving position MAE flat. §3.11 |
