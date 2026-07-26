"""Scenario-agnostic building blocks shared by every evaluation scenario.

* 'metrics' -- scenario-agnostic probability and classification math, no I/O.
* 'ranking_metrics' -- ranking agreement math (Kendall/Spearman/Jaccard
  primitives), shared by the 'drop_robustness' and 'noise_floor' studies. No I/O.
* 'player_scoring' -- rotation-invariant PPG replay from saved Stage-1 fits.
* 'figures' -- shared plotting primitives (reliability curves, density panels).
* 'report_paths' -- output-path helpers ('graphs/' and 'csvs/' subdirectories).
* 'reports' -- generated Markdown ('experiment_report.md', 'docs/summary.md')
  and result-layout discovery.
"""
