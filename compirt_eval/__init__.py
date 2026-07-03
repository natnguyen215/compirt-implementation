"""CompIRT evaluation package: metrics and figures split by paper scenario.

* 'metrics' -- pure metric/curve math shared by both scenarios.
* 'figures' -- shared plotting primitives (reliability curves, density panels).
* 'outputs' -- output-path helpers ('graphs/' and 'csvs/' subdirectories).
* 'tossups' -- Scenario A: tossup first-buzz evaluation (a subpackage; see
  its own docstring for the breakdown by concern).
* 'bonuses' -- Scenario B: bonus-part and points-per-bonus evaluation.

'evaluate_compirt.py' at the project root is the CLI entry point that ties
both scenarios together.
"""
