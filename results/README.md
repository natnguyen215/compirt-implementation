# Experiment Results

Result directories are retained in this repository because they record the
paper's experiment history. New runners resolve CompIRT outputs into one of two
regimes:

- `compirt/in_sample/<run>/`: the model is fitted and evaluated on the selected
  split. These are fit diagnostics, not generalization estimates.
- `compirt/holdout/<run>/`: temporal workflows train on an earlier split and
  evaluate a later split. Read each run's summary because the current holdout
  is player-prior transfer with test-period parameter fitting, not a strict
  unseen-question holdout.
- `ranking_comparison/<run>/`: comparisons between fitted player rankings and
  observed tournament scoring.

A normal two-stage result root contains `pyramidal/`, `compositional/`, optional
`synergy/`, their evaluation directories, and an optional `comparison/`.
Generated prediction CSVs and plots may be ignored for new runs even when older
paper artifacts remain tracked.

Existing result roots use several historical naming styles (`all-2024` and
`all2024`, for example). They are intentionally not renamed: paths are part of
the recorded experiment provenance. New work should follow the names emitted by
the current runners under `compirt/{in_sample,holdout}/`.
