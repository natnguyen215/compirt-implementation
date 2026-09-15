# Compositional bonuses from frozen Stage-1 folds

Source: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal`.

2000 SVI steps, learning rate 0.01, seed 42; bonus discrimination prior `gamma`. Skills are fixed at the saved Stage-1 medians. Synergy uses one latent coordinate per player.

All bonus parameters are fit on training games and frozen for held-out replay. The source Stage-1 fits are reused without refitting. Coverage requires familiar players and parts; lineups are inferred from the observed game buzzes. These are matrix-infill results, not cold-start or recombined-team validation.

Pooled PPB MAE averages each team's observed and predicted points across all its held-out bonuses, then averages absolute errors equally across teams. Exact accuracy requires all three part labels to match.

| Model | Part AUC | Part log loss | Part accuracy | Brier | ECE | Exact accuracy | PPB MAE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| compositional | 0.8903 | 0.4186 | 0.8079 | 0.1338 | 0.0207 | 0.5104 | 1.9897 |
| synergy | 0.8983 | 0.4044 | 0.8172 | 0.1284 | 0.0184 | 0.5306 | 0.9040 |

Scored 128,100 parts / 42,700 bonuses / 2,332 games / 450 teams in 5 folds.

See `per_fold.csv` and `fold_mean_std.csv` for fold variation; one optimization seed was used. All folds passed checks for disjoint training/test games, unique complete bonus responses, finite losses and probabilities, and zero uncovered roster rows.
