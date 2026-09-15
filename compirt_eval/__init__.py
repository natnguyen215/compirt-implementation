"""CompIRT evaluation package: metrics and figures organized by paper scenario.

* 'common' -- shared, scenario-agnostic building blocks:
    - 'common.metrics'      pure metric/curve math (no I/O).
    - 'common.categories'   canonical quizbowl categories for strata.
    - 'common.figures'      shared plotting primitives.
    - 'common.report_paths' output-path helpers ('graphs/' and 'csvs/').
    - 'common.reports'      generated Markdown summaries + layout discovery.
* 'scenario_a_tossups' -- Scenario A: tossup first-buzz evaluation (a subpackage;
  see its own docstring for the breakdown by concern).
* 'scenario_b_bonuses' -- Scenario B: bonus-part and points-per-bonus evaluation.
* 'synergy_comparison' -- no-synergy vs synergy bonus metric deltas, run by
  'run_scripts/common/run_synergy_comparison.py'.

'METRICS.md' is the human-readable metric and graph contract.
'evaluate_compirt.py' at the project root is the CLI entry point that ties
both scenarios together.
"""
