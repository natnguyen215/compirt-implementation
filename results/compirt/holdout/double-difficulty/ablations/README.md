# Ablations

Runs that change configuration settings while keeping the double-difficulty
model form fixed. Structural model changes live in [`../variants/`](../variants/);
whole model families evaluated side by side live in
[`../model-comparisons/`](../model-comparisons/).

| Folder | Factor | Result |
| --- | --- | --- |
| [`relevance-locations-terminal/`](relevance-locations-terminal/) | relevance parameterization x learned curve locations x terminal intercepts — one group, because the three are read together | Simplex relevance improves accuracy and correctness LL; unconstrained relevance improves timing. Terminal intercepts improve joint LL, no-buzz calibration, final-decile mass, and position MAE. §3.2, §3.5–3.6 |
| [`optimization-steps/`](optimization-steps/) | SVI steps: `steps-6000/`, `steps-20000/` (reference is 3,000) | Joint event LL continues to improve at 20,000 steps; the 3,000-step fits have not converged. |
| [`incorrect-loss-weight/`](incorrect-loss-weight/) | likelihood weight on incorrect responses: `weight-1.5`, `weight-2`, `weight-3` (reference is 1x) | Upweighting incorrect responses monotonically degrades correctness LL, ECE and accuracy while leaving position MAE flat. §3.11 |
| `hyperparameter-grid/` | degree 3–6 x dimensions 1–5 x drop-concentration 0.67–2.0; 100 points | Ignored by git as regenerable (~2.7 GB); its 3/3/2 point is tracked below as `dd-bernstein-332-unconstrained/`. §3.7 |

## relevance-locations-terminal

Seven runs of degree-3 Bernstein at three dimensions. Folder names spell out the
configuration, so the name alone says which run it is:

`dd-bernstein-<degree><dimensions><drop-concentration>-<relevance>[-locations][-terminal]`

| Run | relevance prior | drop conc. | learned locations | terminal | Research Log row |
| --- | --- | ---: | :-: | :-: | --- |
| [`dd-bernstein-332-unconstrained/`](relevance-locations-terminal/dd-bernstein-332-unconstrained/) | unconstrained | 2.0 | no | no | `DD-Bernstein 3/3/2, no terminal` |
| [`dd-bernstein-332-unconstrained-terminal/`](relevance-locations-terminal/dd-bernstein-332-unconstrained-terminal/) | unconstrained | 2.0 | no | **yes** | `DD-Bernstein 3/3/2, terminal` |
| [`dd-bernstein-332-simplex/`](relevance-locations-terminal/dd-bernstein-332-simplex/) | **simplex** | 2.0 | no | no | `Simplex relevance, no terminal` |
| [`dd-bernstein-332-simplex-terminal/`](relevance-locations-terminal/dd-bernstein-332-simplex-terminal/) | **simplex** | 2.0 | no | **yes** | `Simplex relevance, terminal` |
| [`dd-bernstein-332-simplex-locations-terminal/`](relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/) | **simplex** | 2.0 | **yes** | **yes** | `Simplex relevance, locations + terminal` |
| [`dd-bernstein-330p67-simplex-locations-terminal/`](relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/) | **simplex** | **0.67** | **yes** | **yes** | `Simplex relevance 3/3/0.67, locations + terminal` |
| [`dd-bernstein-332-gamma-locations-terminal/`](relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/) | **Gamma(2,2)** | 2.0 | **yes** | **yes** | not in the main table |

`dd-bernstein-332-simplex-locations-terminal/` is the reference configuration
for the other ablation folders. It is not a separate `reference/` directory,
because that name said nothing about what it configures.

The progression down the table adds one setting at a time, so adjacent rows are
the comparable pairs. `unconstrained` means a free per-dimension relevance
(`effective_item_parameters = 2*dimensions + curve_parameters`, 30 here);
`simplex` means `Dirichlet(ones(k))` (28 here). Both are degree-3 Bernstein —
the parameterization, not the curve family, is what the names distinguish.

Two layout quirks, both inherited from the runner that produced the run:

- `dd-bernstein-332-simplex/` and `dd-bernstein-332-simplex-terminal/` keep a
  `degree_3/curves_3/dirichlet_2/` directory above their folds. The other five
  hold `fold_{0..4}/` directly.
- `dirichlet_N` in those paths, and in `hyperparameter-grid/`, is the
  **drop**-concentration, not the relevance Dirichlet, which stays at `ones(k)`.

The two `unconstrained` runs are also arms of other comparisons:
`dd-bernstein-332-unconstrained/` is the `degree_3/curves_3/dirichlet_2` cell of
`hyperparameter-grid/`, and `dd-bernstein-332-unconstrained-terminal/` is the
Bernstein arm of
[`../model-comparisons/curve-family/`](../model-comparisons/curve-family/) and
the "full" arm of
[`../model-comparisons/compact-parameterization/`](../model-comparisons/compact-parameterization/),
which still holds a second copy of that same fit.
