# Scenario C Implementation

This repository implements the paper's Scenario C as an opt-in extension to
the temporal holdout pipeline. It measures bonus prediction performance after
grouping each test lineup by how observable its members and exact composition
were during training.

Scenario C is disabled by default. It does not replace or modify the existing
Scenario A/B fits or evaluation artifacts.

## Running it

From the repository root:

```bash
RUN_C1_C4=1 MODEL=baseline DEVICE=cuda \
  .venv/bin/python -m run_scripts.common.run_compirt_holdout
```

The shared implementation supports `baseline`, `multidim`, `tfidf`, and
`tfidf_multidim`. The relevant optional settings are:

- `C1_C4_ITEM_STEPS`: test bonus-item fitting steps; defaults to
  `BONUS_STEPS`.
- `C1_C4_SEED`: seed used before each test-item fit; defaults to `42`.
- `C1_C4_MIN_CROSS_TEAM_GAMES`: minimum number of cross-team C2 games before
  the report treats the central recombination comparison as adequately
  represented; defaults to `10`.

All new artifacts are written beneath the holdout runner's resolved result
root:

```text
train/compositional/             historical no-synergy Stage 2
train/synergy/                   historical synergy Stage 2
holdout/c1-c4/compositional/     no-synergy test-item fit and predictions
holdout/c1-c4/synergy/           synergy test-item fit and predictions
holdout/c1-c4/evaluation/        classifications, metrics, diagnostics, report
```

## Evaluation flow

The holdout runner performs these additional steps only when `RUN_C1_C4=1`:

1. Fit no-synergy and synergy bonus models on the historical training split.
2. Recover the exact historical observations used by both Stage-2 fits from
   their saved `bonus_part_predictions.csv` files.
3. Reject the run if the two historical branches do not contain identical
   `(observation_id, response_id)` pairs.
4. Construct the historical roster, teammate-pair, team-label, and
   composition-graph context from those audited observations.
5. Classify each test bonus response as C1, C2, C3, or C4 using its inferred
   lineup segment.
6. Fit new test bonus-item parameters separately for the no-synergy and
   synergy branches while freezing transferred player and team parameters.
7. Write point metrics, diagnostic slices, C4 base-rate comparisons, and a
   Markdown report.

The orchestration lives in
[`run_scripts/common/run_scenario_c.py`](../run_scripts/common/run_scenario_c.py). Shared
classification and metric logic lives in
[`scenario_c_rosters/classification.py`](scenario_c_rosters/classification.py), and
the restricted Pyro model lives in
[`scenario_c_model.py`](../scenario_c_model.py).

## Lineups and the classification unit

Classification is based on **player lineups**, not tournament-scoped team IDs.
The unit is one bonus response and its covering lineup segment. A game-team can
therefore be in different scenarios in the first and second halves if lineup
inference detects a substitution.

Scenario C calls `LineupIndex.record_for(...)`, the same authoritative lookup
used by the rest of the repository. It does not reproduce the half-boundary
logic or depend on the optional `bonus_team_lineup.csv` debug output.

A lineup is canonicalized as a sorted, duplicate-free player set. Its size can
be any positive value; four-player lineups are not hard-coded. This matters
because the implemented Equation 8 aggregation is an unnormalized
log-sum-exp, so predictions can depend on lineup size.

Each response records:

- lineup segment and canonical roster;
- registered-roster and inferred-lineup sizes;
- distinct players with buzz evidence in the game;
- lineup confidence and resolution rule;
- whether any game buzz evidence exists;
- whether the large-roster `whole_game_no_evidence` fallback was used.

Primary tables are produced for both `all_lineups` and
`game_buzz_evidence_only`. Zero-evidence responses remain visible in the count
and classification artifacts even though the second scope excludes them.

## C1-C4 definitions

Two kinds of historical coverage are kept separate:

- **Theta-known:** the player is present in the historical pyramidal fit.
- **Psi-informed:** the player occurs in an eligible historical bonus lineup.

Classification uses theta coverage and applies this precedence:

1. **C1 — familiar:** the exact canonical roster occurs in eligible historical
   bonus data and every member is theta-known.
2. **C2 — recombined:** every member is theta-known, but the exact roster is
   not an eligible historical roster.
3. **C3 — partially new:** at least one, but not every, member is theta-known.
4. **C4 — fully new:** no member is theta-known.

C1 requires both the exact-roster match and complete theta coverage. If an
exact historical roster somehow lacks complete theta coverage, it falls
through to C3 rather than overriding the coverage rule.

For C3, outputs include roster size, unknown-member count, and unknown-member
fraction. This supports arbitrary roster sizes while still exposing the
paper's `1-of-4` and `3-of-4` cases when they occur.

## C2 provenance diagnostics

Formal C2 membership depends only on roster novelty and theta coverage. The
implementation then adds diagnostics to distinguish plausible recombination
from substitution artifacts:

- normalized cross-tournament `team_name` overlap;
- the fraction of teammate pairs observed during training;
- whether all members share a historical team label;
- whether all members lie in the same training composition-graph component;
- `same_team_label_variant` versus
  `cross_team_recombination_candidate` provenance.

Raw `team_id` is never compared across tournaments because it is
tournament-scoped. Normalized team names are only diagnostic proxies. If too
few cross-team C2 games are available, the generated report says prominently
that aggregate C2 mainly measures substitution robustness and cannot strongly
support the paper's central compositional-generalization claim.

## Frozen-parameter test-item model

Scenario C uses the existing held-out tossup posterior for test-player
`theta`. That posterior is initialized from historical returning-player or
tier priors by the normal temporal holdout pipeline.

For each historical bonus branch, the implementation transfers and freezes:

- the aggregation temperature `tau`;
- synergy profiles `psi`, for the synergy branch;
- optional correctness-calibration scale and bias.

Players without informative historical bonus observations receive `psi = 0`,
the point prediction under the zero-centered prior. A theta-known but
psi-uninformed player therefore retains their test `theta` while contributing
no transferred synergy profile.

The model in [`scenario_c_model.py`](../scenario_c_model.py) exposes only test
bonus-part `alpha` and `beta` as latent Pyro sample sites. `theta`, `psi`,
`tau`, and calibration values are ordinary fixed tensors and cannot be added
to the `AutoNormal` guide or optimizer parameter store. The no-synergy and
synergy branches fit their own test item parameters on the same test outcomes,
with `pyro.set_rng_seed(C1_C4_SEED)` called before each fit.

This is a transductive item-estimation protocol: prediction outcomes are used
to estimate new test-item parameters. Freely fitted test items can absorb some
team-level variation, so the measured synergy-minus-no-synergy difference may
be attenuated.

## Metrics

Point estimates are reported for `ALL` and C1-C4:

- bonus-part AUC, log loss, ECE, and accuracy;
- exact three-part outcome accuracy;
- exact bonus-score accuracy from the three thresholded part decisions;
- per-bonus predicted-points MAE;
- game/team PPB MAE.

For a scenario-specific PPB metric, a game-team is included only if all of its
included bonus responses have the same scenario. Mixed-scenario game-teams
remain in part- and bonus-level metrics and are excluded only from that
scenario's PPB. `ALL` always includes every game-team.

The implementation intentionally does **not** perform bootstrap resampling or
produce confidence intervals. `synergy_comparison.csv` contains paired point
differences computed on identical saved observations.

## C4 graceful-degradation check

The paper treats C4 as a graceful-degradation test rather than an ordinary
accuracy contest. `c4_tier_base_rate_comparison.csv` compares each model's C4
mean predicted part probability and PPB with training-only tier base rates.
When a C4 tier is absent from the corresponding training scope, the code uses
the global training rate and records that fallback explicitly.

The intended interpretation is whether finite C4 predictions move toward
tier-level rates without collapsing to extreme values.

## Evaluation artifacts

The `holdout/c1-c4/evaluation/` directory contains:

- `experiment_report.md`: sample-size table, primary metrics, point
  differences, diagnostics, graph statistics, C4 comparison, and caveats.
- `csvs/eligible_training_response_ids.csv`: audited historical response IDs.
- `csvs/response_classification.csv`: response-level scenario and provenance.
- `csvs/scenario_counts.csv`: counts and roster-size distributions by scope.
- `csvs/scenario_metrics.csv`: point metrics by model, scope, and scenario.
- `csvs/synergy_comparison.csv`: synergy-minus-no-synergy point differences.
- `csvs/scenario_diagnostic_metrics.csv`: C2 provenance/pair novelty and C3
  unknown-member slices.
- `csvs/composition_graph_stats.csv`: historical co-roster graph summaries.
- `csvs/c4_tier_base_rate_comparison.csv`: C4 graceful-degradation table.
- `graphs/scenario_c_auc.png`: compact C1-C4 AUC visualization.
- `summary.json`: protocol metadata and headline diagnostic counts.

Each model branch also saves its test predictions, test item parameters, loss
curve, and parameter-source metadata beneath `holdout/c1-c4/`.

## Interpretation limitations

The generated report discloses the main limitations:

- exact-slug identity linking can inflate C3/C4 when one person has multiple
  unresolved identifiers;
- school-team substitutions can dominate C2 without enough ad hoc-team data;
- zero-buzz lineup inference can create artificial roster novelty;
- transductively fitted item parameters can attenuate synergy effects;
- current repository data does not reproduce the paper's complete
  nine-tournament experiment.

Scenario D, inductive item estimation, fuzzy identity linking, additional
paper baselines, and uncertainty resampling remain separate work.
