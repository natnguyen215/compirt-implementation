# Direct team-skill IRT for bonus questions

Saved Team IRT fits on the five `year_2024` whole-game folds (split and fit
seed 42, 3,000 AutoNormal SVI steps, learning rate 0.01):

- **1D:** `P = sigmoid(alpha_b * theta_t - beta_b)`, `alpha_b ~ Gamma(2, 2)`.
- **3D:** `P = sigmoid(sum_k r_bk * (theta_tk - beta_bk))`, `r_b ~ Dirichlet(1, 1, 1)`,
  so the relevance weights of each part sum to one.

Both arms use `theta_tk, beta_bk ~ Normal(0, 1)`. This run replaced the earlier
`sigmoid(theta_t dot alpha_b - beta_b)` 3D arm on 2026-09-25. Its 1D predictions
match the earlier 1D run exactly, and the earlier fitted parameters remain in
git commit `f0206078` under `bonus-team-irt/2026-09-17/`.

Current scores are in the [shared bonus comparison](../../../../comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md)
and the [bonus research log](../../../../../../RESEARCH_LOG_2.md). The
[identifiability study](identifiability/README.md) shows which 3D parameters
the data determine and what the axes track.

```bash
.venv/bin/python -B -u -m analysis.bonus_team_irt.run \
  --output-dir results/compirt/holdout/common/bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold \
  --steps 3000
```

## Artifacts

- [configuration.json](configuration.json): data, code, and reference hashes; [run.log](run.log).
- `fold_N/team_irt_{1d,3d}/`: medians (`parameters.npz`, `bonus_parts.csv`,
  `team_skills.csv`), IDs, marginal posterior quantiles, loss traces, summaries,
  held-out `bonus_part_predictions.csv`, and `train_bonus_part_predictions.csv`.
- `fold_N/split.json` and `excluded_games.csv`: training, test, and scored games.
- [aggregate/report.md](aggregate/report.md): the runner's own comparison with
  the older DD and multidimensional references. Use the shared comparison for
  current matched results.
