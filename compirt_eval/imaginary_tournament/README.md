# Imaginary tournament

This package simulates artificial games by assigning fitted players to random
teams and sampling fitted tossups into packets. It replays completed Stage 1
and Stage 2 artifacts; it does not optimize model parameters.

Run it from the repository root:

```bash
.venv/bin/python run_scripts/common/run_imaginary_tournament.py \
  --pyramidal-results <run>/pyramidal \
  --compositional-results <run>/compositional \
  --output-dir <run>/imaginary-tournament
```

The outputs are `player_ppg.csv`, `games.csv`, and `summary.json`.
`evaluation.py` owns input loading, simulation, and writing. Argument parsing,
terminal output, and execution live in the runner above.

This is a simulation demonstration rather than an accuracy evaluation against
real outcomes. Powers, bouncebacks, overtime, substitutions, and score
corrections are not modeled.
