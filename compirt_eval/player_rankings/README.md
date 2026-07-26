# Player ranking comparison

This package compares fitted conditional buzz-accuracy rankings with actual
tournament PPG or PP20 rankings. It reads saved predictions and tournament
records; it does not fit a model.

Run it from the repository root:

```bash
.venv/bin/python run_scripts/common/run_player_rankings.py --help
```

`evaluation.py` owns data loading, ranking calculations, and CSV/Markdown
artifacts. The runner owns argument parsing and terminal output.
