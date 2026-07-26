# Synergy comparison

This package compares the saved bonus metrics from no-synergy and synergy
branches of the same run. It writes the comparison CSV, figure, Markdown
report, and refreshed evaluation summaries.

Run it from the repository root:

```bash
.venv/bin/python run_scripts/common/run_synergy_comparison.py --help
```

`evaluation.py` owns comparison calculations and artifacts. The runner owns
argument parsing and execution.
