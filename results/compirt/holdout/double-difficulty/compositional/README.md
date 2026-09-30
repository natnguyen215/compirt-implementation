# Compositional bonus fits

For current results, use the [shared bonus comparison](../../../comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md).
It scores **DD-Bernstein**, **DD-Bernstein + synergy**, the multidimensional
bonus-difficulty variant, multidimensional references, and **Team IRT 1D/3D**
on identical games. The [bonus research log](../../../../../RESEARCH_LOG_2.md)
is the single summary of findings.

Every run uses frozen 3D player skills from the
[normalized-first-buzz Stage-1 run](../likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps/),
3,000 bonus steps, and five folds, so names carry only the bonus
configuration. Run-local reports retain the full compositional population; use
the shared comparison for comparisons with team IRT. Synergy dimensions
describe the player synergy profiles, not the Stage-1 skills.

| Run | Bonus difficulty | Synergy |
| --- | --- | --- |
| [no-synergy-and-dot-additive-1d](no-synergy-and-dot-additive-1d/aggregate/report.md) | Scalar | None, and additive dot 1D (DD-Bernstein; DD-Bernstein + synergy) |
| [max-skill-no-synergy-and-dot-additive-1d](max-skill-no-synergy-and-dot-additive-1d/aggregate/report.md) | Scalar; highest teammate skill per dimension | None, and additive dot 1D |
| [noisy-or](noisy-or/aggregate/report.md) | Scalar inside each member sigmoid; Eq. 9 Noisy-OR | None; no temperature |
| [phi-psi-additive-1d](phi-psi-additive-1d/aggregate/report.md) | Scalar | Additive phi-psi 1D |
| [phi-psi-additive-3d](phi-psi-additive-3d/aggregate/report.md) | Scalar | Additive phi-psi 3D |
| [dot-multiplicative-1d](dot-multiplicative-1d/aggregate/report.md) | Scalar | Multiplicative dot 1D |
| [dot-multiplicative-3d](dot-multiplicative-3d/aggregate/report.md) | Scalar | Multiplicative dot 3D |
| [phi-psi-multiplicative-1d](phi-psi-multiplicative-1d/aggregate/report.md) | Scalar | Multiplicative phi-psi 1D |
| [phi-psi-multiplicative-3d](phi-psi-multiplicative-3d/aggregate/report.md) | Scalar | Multiplicative phi-psi 3D |
| [multidim-difficulty-dot-additive-1d](multidim-difficulty-dot-additive-1d/aggregate/report.md) | Dimensionwise pooling, vector | Additive dot 1D |
| [multidim-difficulty-dot-additive-3d](multidim-difficulty-dot-additive-3d/aggregate/report.md) | Dimensionwise pooling, vector | Additive dot 3D |

Familiar/new-roster metrics, team PPG, and margins for all runs are in
[`no-synergy-and-dot-additive-1d/aggregate/bonus_metrics_report.md`](no-synergy-and-dot-additive-1d/aggregate/bonus_metrics_report.md),
written by [`analysis/compositional/novel_roster_metrics.py`](../../../../../analysis/compositional/novel_roster_metrics.py).

## Saved layout and reproduction

Each run has `configuration.json`, per-fold `train/` and `holdout/` branches,
per-fold evaluation reports, and `aggregate/` pooled metrics. Fit and replay
provenance, source hashes, and resume markers remain with their runs.

See the [runner guide](../../../../../run_scripts/README.md#bonus-stage-from-saved-folds)
for training and saved-prediction evaluation.
