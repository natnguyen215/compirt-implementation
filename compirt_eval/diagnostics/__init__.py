"""Cross-cutting diagnostics that draw on both fitted stages.

* 'posterior_predictive' -- bounded PPCs: trainer-side draw saving plus the
  evaluator-side summary and figure.
* 'match_simulation' -- seeded match-winner simulation, its CSV, and figures.

The standalone synthetic refitting study lives in 'parameter_recovery'.
"""
