# Clue-aligned linear-spline double difficulty

A Stage-1 double-difficulty model whose curves are piecewise linear with knots
at clue ends. `clues.py` finds sentence boundaries without splitting common
abbreviations, acronyms, or initials. Each tossup learns a value at `x = 0` and
after every clue, separately for correctness and hazard:

```text
d_branch_jk(x) = linear interpolation of the clue landmarks
correctness = sum_k r_correct_jk * (theta_ik - d_correct_jk(x))
hazard      = sum_k r_hazard_jk  * (theta_ik - d_hazard_jk(x)) - c_i
```

Landmarks have independent `Normal(0, 1)` priors, so a curve may rise or fall.
`theta` and `c` are shared by both branches.

The monotone variant (`train_monotone_pyramidal.py`) writes each landmark as the
first value minus a cumulative sum of `HalfNormal(0.5)` drops, so every curve
is flat or decreasing. It saves the same schema.

## Commands

```bash
.venv/bin/python -m dd_linear_spline.train_pyramidal \
  --split year_2024 --dimensions 5 --steps 3000 --lr 0.01 --device cuda \
  --output-dir results/compirt/in_sample/double-difficulty/dd-linear-spline/pyramidal
.venv/bin/python -m dd_linear_spline.train_monotone_pyramidal \
  --split year_2024 --dimensions 5 --steps 3000 --lr 0.01 --device cuda --posterior-draws 0 \
  --output-dir results/compirt/in_sample/double-difficulty/dd-monotone-linear-spline/pyramidal
# Five-fold frozen matrix infill for the monotone variant
.venv/bin/python -m run_scripts.linear_spline.run_monotone_holdout \
  --base-split year_2024 --dimensions 5 --steps 3000 --lr 0.01 --device cuda --posterior-draws 0
```

In `tossups.csv`, `spline_knot_x_*` holds relative clue positions,
`spline_y_*_d*` the correctness landmarks, and `hazard_spline_y_*_d*` the hazard
landmarks.

## Saved runs

[`dd-linear-spline/`](../../results/compirt/in_sample/double-difficulty/dd-linear-spline/)
and
[`dd-monotone-linear-spline/`](../../results/compirt/in_sample/double-difficulty/dd-monotone-linear-spline/)
under `results/compirt/in_sample/double-difficulty/`. The live
`holdout/frozen_predict.py` no longer replays this schema.
