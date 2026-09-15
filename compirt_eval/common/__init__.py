"""Scenario-agnostic building blocks shared by every evaluation scenario.

* 'metrics' -- scenario-agnostic probability and classification math, no I/O.
* 'categories' -- canonical top-level quizbowl categories for strata.
* 'figures' -- shared plotting primitives (reliability curves, density panels).
* 'report_paths' -- output-path helpers ('graphs/' and 'csvs/' subdirectories).
* 'reports' -- generated Markdown ('experiment_report.md', 'docs/summary.md')
  and result-layout discovery.
"""
