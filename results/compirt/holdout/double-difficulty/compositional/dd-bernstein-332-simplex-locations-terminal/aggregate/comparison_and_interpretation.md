# Compositional comparison and interpretation

All four rows score the same 128,100 parts from 42,700 bonuses in five 2024 whole-game folds. Observation IDs, labels, inferred lineups, frozen bonus replay, and disjoint training/test games were checked. Metrics were recomputed from saved predictions; no models were refit.

| Model | Arm | AUC | Log loss | Part accuracy | Pooled team PPB MAE |
| --- | --- | ---: | ---: | ---: | ---: |
| Multidim | compositional | 0.8881 | 0.4227 | 80.83% | 2.040 |
| Multidim | synergy | 0.8955 | 0.4112 | 81.39% | 1.172 |
| DD-Bernstein | compositional | 0.8903 | 0.4186 | 80.79% | 1.990 |
| DD-Bernstein | synergy | 0.8983 | 0.4044 | 81.72% | 0.904 |

The historical multidimensional fit has five skill dimensions, Normal bonus discrimination, and rank-three synergy. DD-Bernstein uses three skill dimensions, Gamma bonus discrimination, and rank-one synergy. Both bonus fits use 2,000 steps, learning rate 0.01, and seed 42. This compares complete fitted configurations; it does not isolate the effect of changing the tossup curve family.

Other historical baseline, topic, and TF-IDF runs use different splits and often fit their bonus stage on the evaluated bonus responses. Those bonus scores cannot establish a matched frozen-holdout ranking.

## Interpretation

Predictions decompose into a log-sum-exp aggregate of fixed player abilities, minus bonus-part difficulty, plus an optional roster synergy term. Positive bonus discrimination in the DD model makes its skill effects monotone. The learned skill dimensions have no assigned subject labels. Difficulty and aggregation temperature are conditional on the fitted ability scale; tau also introduces a roster-size contribution because the aggregation is not normalized.

For 94.96% of held-out bonus responses, the same team and exact inferred roster already appeared in training. A synergy term can therefore act as a persistent team adjustment. It can capture bonus-specific ability, communication, or model misspecification; this experiment does not distinguish these explanations. Individual scalar synergy-profile signs can all be flipped without changing any pair product, so a positive profile is not a measure of being a good teammate.

The DD synergy model has pooled team PPB MAE 0.904, meaning error in a team’s average bonus points across its held-out responses. Exact recovery of all three part labels is 53.06%. The pooled team error averages over many bonuses and does not describe the error on one bonus.

A team-intercept baseline and validation on withheld roster combinations would test whether the pairwise parameterization adds transferable information. Saved Stage-2 uncertainty is conditional on frozen Stage-1 skills, and these comparisons use one optimization seed.

Sources: `comparison_with_multidim.json`, `roster_familiarity.json`, and the original run directories recorded in the comparison JSON.
