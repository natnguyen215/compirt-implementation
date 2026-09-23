# Bonus-only team IRT

Learn a tournament-team skill vector directly from bonus part outcomes:
`P(correct) = sigmoid(theta_team dot alpha_part - beta_part)`.
Team skills and scalar part difficulties have independent standard normal
priors; positive part loadings have Gamma(2, 2) shape/rate priors. The default
arms have one and three dimensions, trained with AutoNormal SVI for 3,000 steps
at learning rate 0.01, seed 42. Frozen predictions use training posterior medians.
No tossup skills, lineup aggregation, or synergy enter these team models.

Run from the repository root:

```bash
.venv/bin/python -B -m analysis.bonus_team_irt.run \
  --output-dir results/compirt/holdout/common/bonus-team-irt/2026-09-17 \
  --steps 3000
```

The configurable runner supports `--help`, `--stage fit`, and `--stage evaluate`.
An identical configuration resumes completed fits through summary markers.
Changed configuration, source code, data, or reference artifacts require a
fresh output root. Parameters, entity IDs, marginal posterior quantiles, loss
traces, and prediction tables are saved for every fit. Evaluation reuses those
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
  --output-dir results/compirt/holdout/common/bonus-team-irt/2026-09-17
```

Reports, metric CSVs, reference hashes, and configuration live under the chosen
output root. Findings belong in
`RESEARCH_LOG_2.md`.
