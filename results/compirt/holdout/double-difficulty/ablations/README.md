# Ablations

Runs that change configuration settings while keeping the double-difficulty
model form fixed. Structural model changes live in [`../variants/`](../variants/);
whole model families evaluated side by side live in
[`../model-comparisons/`](../model-comparisons/).

The reference configuration is Bernstein degree 3, 3 relevance curves, simplex
relevance prior, drop-concentration 2.0, learned curve locations, terminal
intercepts, 3,000 steps. It is **not** a separate top-level folder: it is
[`simplex-locations-terminal/reference/`](simplex-locations-terminal/reference/),
one cell of the group whose factors it fixes.

| Folder | Factor | Reference value | Result |
| --- | --- | --- | --- |
| [`simplex-locations-terminal/`](simplex-locations-terminal/) | relevance prior, learned curve locations, terminal intercepts — one group, because the three are read together | simplex + locations + terminal | Simplex improves accuracy and correctness LL; Gamma improves timing. Terminal intercepts improve joint LL, no-buzz calibration, final-decile mass, and position MAE. §3.2, §3.5–3.6 |
| [`optimization-steps/`](optimization-steps/) | SVI steps: `steps-6000/`, `steps-20000/` | 3,000 | Joint event LL continues to improve at 20,000 steps; the 3,000-step fits have not converged. |
| [`incorrect-loss-weight/`](incorrect-loss-weight/) | likelihood weight on incorrect responses: `weight-1.5`, `weight-2`, `weight-3` | 1x | Upweighting incorrect responses monotonically degrades correctness LL, ECE and accuracy while leaving position MAE flat. §3.11 |
| [`hyperparameter-grid/`](hyperparameter-grid/) | degree 3–6 x dimensions 1–5 x drop-concentration 0.67–2.0; 100 points | — | See [`aggregate/summary.md`](hyperparameter-grid/aggregate/summary.md). §3.7 |

## simplex-locations-terminal

These five runs vary settings that cannot be read one at a time: the relevance
prior, whether curve locations are learned, and whether the terminal cell gets
its own intercepts.

| Run | relevance prior | drop concentration | learned locations | terminal intercepts | Research Log main-table row |
| --- | --- | ---: | --- | --- | --- |
| [`reference/`](simplex-locations-terminal/reference/) | simplex | 2.0 | yes | on | `Simplex relevance, locations + terminal` |
| [`gamma-relevance/`](simplex-locations-terminal/gamma-relevance/) | Gamma(2,2) | 2.0 | yes | on | not in the main table |
| [`drop-concentration-0.67/`](simplex-locations-terminal/drop-concentration-0.67/) | simplex | 0.67 | yes | on | `Simplex relevance 3/3/0.67, locations + terminal` |
| [`terminal-on/`](simplex-locations-terminal/terminal-on/) | simplex | 2.0 | **no** | on | `Simplex relevance, terminal` |
| [`terminal-off/`](simplex-locations-terminal/terminal-off/) | simplex | 2.0 | **no** | **off** | `Simplex relevance, no terminal` |

`terminal-on/` and `terminal-off/` differ from `reference/` on two factors, not
one: both were run without `--learn-curve-locations`. Compare them with each
other for the terminal-intercept effect, not against `reference/`.

The two `DD-Bernstein 3/3/2` rows of that table are **not** in this group: they
use the older unconstrained relevance rather than a simplex prior, and live at
[`hyperparameter-grid/degree_3/curves_3/dirichlet_2/`](hyperparameter-grid/degree_3/curves_3/dirichlet_2/)
(no terminal) and
[`../model-comparisons/curve-family/bernstein-332/seed_42/`](../model-comparisons/curve-family/bernstein-332/seed_42/)
(terminal).

## Caveat on the hyperparameter grid

The grid predates both the simplex prior and the terminal-intercept option. Its
fits report `effective_item_parameters = 2*dimensions + curve_parameters` (the
unconstrained relevance branch) and carry no `terminal_intercepts` key, so its
points are not directly comparable with anything else in this directory. Only
the `degree_3/curves_3/dirichlet_2` point is tracked in git — the other 99 are
ignored as regenerable. `dirichlet_N` in the grid's paths is the
**drop**-concentration, not the relevance Dirichlet, which stays at `ones(k)`.
