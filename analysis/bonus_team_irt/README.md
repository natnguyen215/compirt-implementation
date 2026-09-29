# Bonus models: team IRT and shared comparison

Learn a tournament-team skill vector directly from bonus part outcomes. The
1D arm uses `P(correct) = sigmoid(alpha_part * theta_team - beta_part)` with a
Gamma(2, 2) shape/rate loading prior. Multidimensional arms use
`P(correct) = sigmoid(sum_k r_part,k * (theta_team,k - beta_part,k))`, with
simplex relevance `r_part ~ Dirichlet(1)` and one difficulty per axis. Only
`r dot beta` is identified, not each `beta_k`. Team skills and difficulties have
independent standard normal priors. The default
arms have one and three dimensions, trained with AutoNormal SVI for 3,000 steps
at learning rate 0.01, seed 42. Frozen predictions use training posterior medians.
No tossup skills, lineup aggregation, or synergy enter these team models.

The [shared bonus comparison](../../results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md)
is the current results entry point for DD-Bernstein, multidimensional player
models, and Team IRT 1D and 3D. All models use the same scored games; DD uses
the normalized first-buzz skill source. Findings are summarized once in
[`RESEARCH_LOG_2.md`](../../RESEARCH_LOG_2.md).

To fit a new team model, run from the repository root:

```bash
.venv/bin/python -B -m analysis.bonus_team_irt.run \
  --output-dir results/compirt/holdout/common/bonus-team-irt/<new-run> \
  --steps 3000
```

The configurable runner supports `--help`, `--stage fit`, and `--stage evaluate`.
An identical configuration resumes completed fits through summary markers.
Changed configuration, source code, data, or reference artifacts require a
fresh output root. Parameters, entity IDs, marginal posterior quantiles, loss
traces, and held-out and training prediction tables are saved for every fit. Evaluation reuses those
fits without training. Tests live in `tests/test_bonus_team_irt.py`.

## Evaluation protocol

Use the existing five `year_2024` whole-game folds, split seed 42. The default
references are the saved DD-Bernstein and multidimensional compositional and
synergy arms from the bonus research log. Reference training splits,
observation IDs, labels, and identities are checked before comparison.

Training uses all bonus observations in each training fold. Scoring excludes
whole test games requiring a team or part absent from training, or missing any
reference prediction. Every arm scores identical complete games and parts.
Zero-bonus teams and games remain in game-level denominators. Exclusions and
train/test game IDs are saved per fold.

Shared scoring functions implement `compirt_eval/METRICS.md`: part log loss,
Brier, AUC, accuracy, exact-bonus accuracy, team PPB, tournament bonus-only PPG,
and bonus-only signed game margin MAE. Pool folds before calculating team
metrics. Margins use expected points conditional on recorded opportunities;
they do not predict bonus ownership or include tossup points.

Subject category, declared difficulty, and category x difficulty tables include
counts, observed conversion rates, and binary probability scores. Missing or
unmapped categories remain Unknown. Difficulty comes from metadata, not part
order. Each part receives one vote within a stratum. Sparse or single-class
strata are retained with undefined AUC as appropriate.

The report uses the existing compositional metric columns and difficulty/PPG/
margin layout. The folds are reused development folds with familiar entities; team vectors ignore lineup changes
and do not establish interpretable subject axes or new-team transfer.

Refresh report formatting from saved metric CSVs without fitting or rescoring:

```bash
.venv/bin/python -B -m analysis.bonus_team_irt.report \
  --output-dir results/compirt/holdout/common/bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold
```

Reports, metric CSVs, reference hashes, and configuration live under the chosen
output root. Findings belong in
`RESEARCH_LOG_2.md`.
