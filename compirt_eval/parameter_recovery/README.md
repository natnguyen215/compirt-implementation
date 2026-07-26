# Synthetic parameter recovery

This package owns the bounded two-dimensional parameter-recovery study. Unlike
the standard evaluator, it deliberately generates synthetic data and refits the
multidimensional Stage 1 model because recovery after fitting is the quantity
being studied.

Run it from the repository root:

```bash
.venv/bin/python \
  run_scripts/multidimensional/multidim/run_parameter_recovery.py \
  --output-dir <result-root>/compirt_eval/parameter-recovery
```

`evaluation.py` contains generation, fitting, alignment, scoring, and output
logic. Argument parsing and execution live in the runner above, matching every
other standalone evaluation study.

The default one-seed run is a smoke test. It does not establish general
identifiability across dataset sizes, roster-overlap patterns, or seeds.
