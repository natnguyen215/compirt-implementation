# Scenario C: roster generalization

Paper Scenario C groups each held-out bonus response by how observable its
lineup was during training, then compares the no-synergy and synergy bonus
models within each group. It was an opt-in step of the temporal holdout runner
(`RUN_C1_C4=1`, now removed) and never produced saved results.

| Code | Role |
| --- | --- |
| [`run_scripts/common/run_scenario_c.py`](../run_scripts/common/run_scenario_c.py) | Fits test items for both branches and writes the evaluation (`--help` lists its inputs) |
| [`scenario_c_rosters/classification.py`](scenario_c_rosters/classification.py) | Classification, provenance diagnostics, and metrics |
| [`scenario_c_model.py`](../scenario_c_model.py) | Test-item Pyro model with frozen player and team parameters |

## Classification

The unit is one bonus response and its inferred lineup segment from
`LineupIndex.record_for(...)`, so a game-team can change scenario at a
substitution. A lineup is a sorted, duplicate-free player set of any size.

A player is **theta-known** if present in the historical pyramidal fit and
**psi-informed** if they appear in an eligible historical bonus lineup. With
theta coverage:

1. **C1, familiar:** the exact roster occurred in historical bonus data and
   every member is theta-known.
2. **C2, recombined:** every member is theta-known but the exact roster is new.
3. **C3, partially new:** some but not all members are theta-known.
4. **C4, fully new:** no member is theta-known.

An exact historical roster without full theta coverage falls to C3. C3 rows
record roster size and unknown-member count. C2 rows add provenance
diagnostics: normalized cross-tournament team-name overlap, the share of
teammate pairs seen in training, shared historical team label, and shared
composition-graph component. Raw `team_id` is tournament-scoped and never
compared across tournaments. Tables are produced for all lineups and for
lineups with game buzz evidence.

The two historical bonus fits must contain identical
`(observation_id, response_id)` pairs, or the run is rejected.

## Test-item model

Test-player `theta` comes from the held-out tossup posterior. From each
historical bonus fit, `tau`, synergy profiles `psi`, and any calibration scale
and bias are frozen; players without historical bonus data get `psi = 0`. Only
the test bonus parts' `alpha` and `beta` are Pyro sample sites. Both branches
fit their own test items on the same outcomes, so the protocol is transductive
in items, and freely fitted items can absorb team effects and shrink the
measured synergy difference.

## Metrics and artifacts

For `ALL` and C1–C4: bonus-part AUC, log loss, ECE, and accuracy; exact
three-part and bonus-score accuracy; per-bonus points MAE; and game-team PPB
MAE. A game-team counts toward one scenario's PPB only if all its responses
share that scenario. Paired synergy-minus-no-synergy differences are point
estimates; there is no bootstrap. For C4, mean predicted part probability and
PPB are compared with training-only tier base rates, falling back to the
global rate when a tier is missing.

The evaluation directory holds `experiment_report.md`, `summary.json`,
`graphs/scenario_c_auc.png`, and `csvs/` with the response classification,
scenario counts and metrics, synergy comparison, diagnostic slices,
composition-graph statistics, C4 base-rate comparison, and eligible training
response IDs.

## Limitations

- Exact-slug identity can inflate C3 and C4 when one person has several IDs.
- School-team substitutions can dominate C2 when there is little ad hoc-team
  data.
- Lineup inference on zero-buzz games can create artificial roster novelty.
- Transductive item fits can attenuate synergy effects.
- The repository data does not cover the paper's nine-tournament experiment.
