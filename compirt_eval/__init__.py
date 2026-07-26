"""CompIRT evaluation package: metrics and figures organized by paper scenario.

Scenario-agnostic building blocks live in 'common'; each paper scenario has its
own subpackage; cross-cutting diagnostics and standalone studies sit alongside
them.

* 'common' -- shared, scenario-agnostic building blocks:
    - 'common.metrics'      pure metric/curve math (no I/O).
    - 'common.ranking_metrics' pure ranking-agreement math (no I/O).
    - 'common.player_scoring' rotation-invariant PPG replay over saved fits.
    - 'common.figures'      shared plotting primitives.
    - 'common.report_paths' output-path helpers ('graphs/' and 'csvs/').
    - 'common.reports'      generated Markdown summaries + layout discovery.
* 'scenario_a_tossups' -- Scenario A: tossup first-buzz evaluation (a subpackage;
  see its own docstring for the breakdown by concern).
* 'scenario_b_bonuses' -- Scenario B: bonus-part and points-per-bonus evaluation.
* 'scenario_c_rosters' -- Scenario C: roster-generalization study (C1-C4).
* 'diagnostics' -- cross-cutting replay diagnostics: posterior predictive
  checks and the seeded match-winner simulation.
* 'parameter_recovery' -- standalone synthetic generate/refit/recovery study.
* 'imaginary_tournament' -- standalone randomized-roster simulation over
  saved fitted players and questions.
* 'noise_floor' -- standalone identical-data seed-stability evaluation.
* 'drop_robustness' -- standalone random and targeted event-drop evaluation.
* 'player_rankings' -- standalone comparison of fitted conditional buzz
  accuracy against tournament PPG/PP20 standings.
* 'synergy_comparison' -- standalone no-synergy vs synergy bonus metric deltas.

The standalone studies expose their evaluation functions here for reuse; their
command-line runners live under 'run_scripts/'.

'METRICS.md' is the human-readable metric and graph contract.

'evaluate_compirt.py' at the project root is the CLI entry point that ties
both scenarios together.
"""
