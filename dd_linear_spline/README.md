# Double-Difficulty Linear Spline

This Stage-1 variant replaces a fixed-form difficulty curve with a piecewise
linear curve whose knots follow tossup clues. A protected sentence heuristic
finds clue ends without splitting common abbreviations, acronyms, or name
initials. Each tossup has a learned value at `x = 0` and after every clue.

Correctness and buzz timing are fitted separately:

```text
d_branch_jk(x) = linear interpolation of clue landmarks
correctness = sum_k r_correct_jk * (theta_ik - d_correct_jk(x))
hazard      = sum_k r_hazard_jk  * (theta_ik - d_hazard_jk(x)) - c_i
```

The landmark values have independent `Normal(0, 1)` priors, so either curve may
rise or fall. Player skill `theta` and confidence `c` remain shared.

## Monotone-decreasing variant

`dd_linear_spline.train_monotone_pyramidal` uses the same interpolation and
saved artifact schema, but writes each landmark as the first value minus a
cumulative sum of nonnegative within-clue drops. Consequently every
correctness and hazard difficulty curve is decreasing or flat in every
dimension. First landmarks use `Normal(0, 1)` priors and successive drops use
`HalfNormal(0.5)` priors.

In-sample:

```bash
.venv/bin/python -m dd_linear_spline.train_monotone_pyramidal \
  --split year_2024 --dimensions 5 --steps 3000 --lr 0.01 --device cuda \
  --posterior-draws 0 \
  --output-dir results/compirt/in_sample/double-difficulty/dd-monotone-linear-spline/pyramidal
```

Five-fold frozen matrix-infill holdout (train on four whole-game folds, replay
frozen parameters on the fifth, then evaluate it):

```bash
.venv/bin/python -m run_scripts.linear_spline.run_monotone_holdout \
  --base-split year_2024 --dimensions 5 --steps 3000 --lr 0.01 \
  --device cuda --posterior-draws 0
```

Run from the repository root:

```bash
.venv/bin/python -m dd_linear_spline.train_pyramidal \
  --split year_2024 \
  --dimensions 5 \
  --steps 3000 \
  --lr 0.01 \
  --device cuda \
  --output-dir results/compirt/in_sample/double-difficulty/dd-linear-spline/pyramidal
```

The trainer writes the standard Stage-1 artifacts. In `tossups.csv`,
`spline_knot_x_*` stores fixed relative clue positions, `spline_y_*_d*` stores
correctness landmarks, and `hazard_spline_y_*_d*` stores hazard landmarks.
