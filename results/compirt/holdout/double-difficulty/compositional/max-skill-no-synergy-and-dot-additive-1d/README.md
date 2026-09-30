# Highest teammate skill per dimension

The two arms replace LSE with `m_k(R) = max_{i in R} theta_ik` and use
`sigmoid(alpha_b dot m(R) - beta_b + s(R))`. Synergy is either zero or the
existing additive dot 1D term over all active teammate pairs. There is no
temperature parameter. All other settings and Stage-1 source hashes match
`../no-synergy-and-dot-additive-1d/configuration.json`: five `year_2024` folds,
seed 42, frozen 3D DD-Bernstein skills, Gamma(2,2) loadings, scalar Normal
difficulty, and 3,000 AutoNormal SVI steps at learning rate 0.01.

- [Configuration and source hashes](configuration.json), with per-fold commands,
  fits, frozen predictions, and coverage audits in `fold_N/`.
- [Full compositional-population scores](aggregate/report.md).
- [Matched scores](aggregate/matched/metrics.csv), [minority-class scores](aggregate/matched/minority_metrics.csv),
  [roster scores](aggregate/matched/roster_metrics.csv), and [training diagnostics](aggregate/matched/in_sample_metrics.csv).
  Matched holdout rows use the existing comparison's `scored_game_ids`: 127,986
  parts, 42,662 bonuses, and 2,330 games. The same observation IDs and outcomes
  were checked against the LSE reference. [Extraction source hashes](aggregate/matched/sources.json)
  identify those inputs. Training diagnostics retain all training observations,
  distinguishing response and team IDs by fold.
- Findings and comparison tables: [bonus research log](../../../../../../RESEARCH_LOG_2.md).

Reproduce with the existing fold runner's `--bonus-aggregation max --steps 3000
--lr 0.01 --seed 42 --alpha-prior gamma`, both default arms, the Stage-1 root
from the configuration, and a fresh output root. See the
[runner guide](../../../../../../run_scripts/README.md#bonus-stage-from-saved-folds).
