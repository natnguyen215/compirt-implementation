# Ablations

Runs that change configuration settings while keeping the double-difficulty
model form fixed. Structural model changes live in [`../variants/`](../variants/);
whole model families evaluated side by side live in
[`../model-comparisons/`](../model-comparisons/).

| Group | Experiments |
| --- | --- |
| [model-components/](model-components/) | `relevance-locations-terminal/`: seven relevance-prior, learned-location, and terminal-intercept configurations; details below. |
| [capacity/](capacity/) | [Degree/dimension/drop-prior grid](capacity/degree-dimensions-drop-prior/aggregate/summary.md) (100 configurations) and [degree-10 runs](capacity/high-degree/) at 3,000/10,000 steps. |
| [training/](training/) | [Optimization steps](training/optimization-steps/): 6,000/20,000 versus the 3,000-step reference. [Incorrect-response weights](training/incorrect-loss-weight/): 1.5, 2, and 3 versus 1. |

Perception-model sweeps live with their model variants under
[variants/perception/dimension-sweeps/](../variants/perception/dimension-sweeps/).
They change both the model family and its dimensionality.

## relevance-locations-terminal

Seven runs of degree-3 Bernstein at three dimensions. Folder names spell out the
configuration, so the name alone says which run it is:

`dd-bernstein-<degree><dimensions><drop-concentration>-<relevance>[-locations][-terminal]`

| Run | relevance prior | drop conc. | learned locations | terminal | Research Log row |
| --- | --- | ---: | :-: | :-: | --- |
| [`dd-bernstein-332-unconstrained/`](model-components/relevance-locations-terminal/dd-bernstein-332-unconstrained/) | unconstrained | 2.0 | no | no | `DD-Bernstein 3/3/2, no terminal` |
| [`dd-bernstein-332-unconstrained-terminal/`](model-components/relevance-locations-terminal/dd-bernstein-332-unconstrained-terminal/) | unconstrained | 2.0 | no | **yes** | `DD-Bernstein 3/3/2, terminal` |
| [`dd-bernstein-332-simplex/`](model-components/relevance-locations-terminal/dd-bernstein-332-simplex/) | **simplex** | 2.0 | no | no | `Simplex relevance, no terminal` |
| [`dd-bernstein-332-simplex-terminal/`](model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/) | **simplex** | 2.0 | no | **yes** | `Simplex relevance, terminal` |
| [`dd-bernstein-332-simplex-locations-terminal/`](model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/) | **simplex** | 2.0 | **yes** | **yes** | `Simplex relevance, locations + terminal` |
| [`dd-bernstein-330p67-simplex-locations-terminal/`](model-components/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/) | **simplex** | **0.67** | **yes** | **yes** | `Simplex relevance 3/3/0.67, locations + terminal` |
| [`dd-bernstein-332-gamma-locations-terminal/`](model-components/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/) | **Gamma(2,2)** | 2.0 | **yes** | **yes** | not in the main table |

`dd-bernstein-332-simplex-locations-terminal/` is the reference configuration
for the other ablation folders.

The progression down the table adds one setting at a time, so adjacent rows are
the comparable pairs. `unconstrained` means a free per-dimension relevance
(`effective_item_parameters = 2*dimensions + curve_parameters`, 30 here);
`simplex` means `Dirichlet(ones(k))` (28 here). Both are degree-3 Bernstein —
the parameterization, not the curve family, is what the names distinguish.

Two layout quirks, both inherited from the runner that produced the run:

- `dd-bernstein-332-simplex/` and `dd-bernstein-332-simplex-terminal/` keep a
  `degree_3/curves_3/dirichlet_2/` directory above their folds. The other five
  hold `fold_{0..4}/` directly.
- `dirichlet_N` in those paths, and in `capacity/degree-dimensions-drop-prior/`, is the
  **drop**-concentration, not the relevance Dirichlet, which stays at `ones(k)`.

`dd-bernstein-332-unconstrained/` is also an arm of two other comparisons: it
is the `degree_3/curves_3/dirichlet_2` cell of `capacity/degree-dimensions-drop-prior/` and the
Bernstein arm of
[`../model-comparisons/curve-family/`](../model-comparisons/curve-family/)
(its fold metrics match that comparison's Bernstein column).
