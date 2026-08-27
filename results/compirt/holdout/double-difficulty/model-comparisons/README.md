# Model comparisons

Arms meant to be read **side by side** — each answers "which model?", not
"which setting?". Compare within a subfolder; the reference configuration is
[`../reference-model/`](../reference-model/).

| Folder | Question | Verdict (RESEARCH_LOG) |
| --- | --- | --- |
| [`double-vs-single-difficulty/`](double-vs-single-difficulty/) | Does giving correctness and hazard separate curves beat one shared curve? | Double Bernstein wins correctness and negs; double sigmoid wins survival calibration. All four arms overpredict no-buzz. See [`aggregate/comparison.md`](double-vs-single-difficulty/aggregate/comparison.md). §3.1 |
| [`curve-family/`](curve-family/) | Bernstein, sigmoid, linear spline, or monotone linear spline? | Bernstein 3/3/2 wins correctness and calibration in all five folds; the unconstrained linear spline wins timing. §3.4 |
| [`compact-parameterization/`](compact-parameterization/) | Can a scalar skill projection with one curve per branch replace a curve per dimension? | Compact uses 11 item parameters vs 30 and stays competitive. §3.3 |

`double-vs-single-difficulty/` holds four arms: `full-double-bernstein/`,
`monotone-double-sigmoid/`, `single-curve-bernstein-baseline/`,
`single-curve-sigmoid-baseline/`. The two single-curve arms are **replayed saved
fits**, not retrained under current conventions — that comparison is descriptive,
not a controlled A/B. `compact-parameterization/` holds `compact/` and
`full-bernstein-332/`.
