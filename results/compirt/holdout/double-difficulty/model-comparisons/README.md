# Model comparisons

Each subdirectory compares model structures under a common protocol. The
reference configuration is [`dd-bernstein-332-simplex-locations-terminal`](../ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/).

| Folder | Comparison | Result |
| --- | --- | --- |
| [`double-vs-single-difficulty/`](double-vs-single-difficulty/) | Separate versus shared correctness and hazard curves | Double Bernstein improves correctness and neg prediction; double sigmoid has better survival calibration. All four models overpredict no-buzz. See [`aggregate/comparison.md`](double-vs-single-difficulty/aggregate/comparison.md). §3.1 |
| [`curve-family/`](curve-family/) | Bernstein, sigmoid, linear spline, and monotone linear spline | Bernstein 3/3/2 has the best correctness and calibration results in all five folds; the unconstrained linear spline has the best timing results. §3.4 |

`double-vs-single-difficulty/` holds four arms: `full-double-bernstein/`,
`monotone-double-sigmoid/`, `single-curve-bernstein-baseline/`,
`single-curve-sigmoid-baseline/`. The two single-curve arms replay saved fits
rather than retraining under current conventions; this is a descriptive, not
controlled, comparison.
