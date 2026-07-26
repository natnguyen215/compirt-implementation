# SVI posterior uncertainty artifacts

Every active CompIRT trainer saves uncertainty from its fitted Pyro
`AutoNormal` guide before that in-memory guide is discarded. These files are
additional training artifacts; the established median parameter and prediction
CSVs remain unchanged.

## Files

Each Stage 1 or Stage 2 result directory contains:

- `posterior_quantiles.csv`: one readable row per scalar latent coordinate,
  with constrained 2.5%, 50%, and 97.5% quantiles;
- `posterior_quantiles.npz`: the same quantiles with each site's original tensor
  shape preserved;
- `posterior_manifest.json`: site shapes, dtypes, filenames, draw count, seed,
  approximate storage size, and interpretation notes; and
- `posterior_draws/<site>.npy`: optional arrays with shape
  `(draws, *site_shape)`.

The leading draw index is aligned across every site file. For example, row 17
of `theta.npy`, `beta.npy`, and `gamma.npy` belongs to one coherent variational
posterior draw. The `.npy` files can be opened with `numpy.load(...,
mmap_mode="r")` without loading every draw into memory.

## Controls

Training CLIs accept:

```text
--posterior-draws N
```

The default is 100 aligned parameter draws. Use `--posterior-draws 0` to save
parameter quantiles without raw draws. Drawing parameters does not construct
every possible player-question pair and does not refit the model.

## Interpretation

These are approximate SVI credible intervals conditional on the fitted model
and data. They are not bootstrap intervals over questions or games. `AutoNormal`
is mean-field and can underestimate uncertainty or omit important posterior
correlations.

Stage 2 treats the Stage 1 `theta` input as fixed, so Stage 2 intervals are
conditional on that fixed skill matrix. They do not propagate Stage 1 skill
uncertainty through bonus fitting.

The saved files contain parameter draws rather than row- or token-level
predictive intervals. Nonlinear predictive intervals should be constructed by
replaying selected predictions for aligned draw indexes; parameter endpoint
combinations are not valid predictive credible intervals.

The embedding-relevance projection is optimized as a deterministic Pyro
parameter rather than an `AutoNormal` latent site. Its weights therefore do not
appear in these guide uncertainty artifacts.
