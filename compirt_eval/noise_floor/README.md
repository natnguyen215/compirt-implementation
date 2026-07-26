# Seed noise floor

This evaluation family reads identical-data Stage-1 fits trained under
different SVI seeds and measures movement in their model-predicted expected-PPG
rankings. Evaluation code in this package never launches retraining.

Like the drop-robustness studies, the executable runner lives under
`run_scripts/`; it schedules the fits and then calls this package to analyze
their saved artifacts. The default invocation reproduces the retained
multidimensional tanh 2024 study:

```bash
.venv/bin/python \
  run_scripts/multidimensional/multidim/run_multidim_noise_floor.py
```

Pass `--collect-only` to rebuild `predicted_ppg_by_seed.csv` from existing fits
without training. Use `--help` to select another seed root while retaining the
same calculations and artifact layout. Exact scoring equations and denominators
are documented in [`../METRICS.md`](../METRICS.md); the evaluation-family
summary is in [`../EVALUATION_TLDR.md`](../EVALUATION_TLDR.md).
