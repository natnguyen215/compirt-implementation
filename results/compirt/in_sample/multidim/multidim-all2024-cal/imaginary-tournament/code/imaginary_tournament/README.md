# Imaginary tournament

This package simulates artificial games by assigning fitted players to random
teams and sampling fitted tossups into packets. It replays completed Stage 1
artifacts; it does not optimize model parameters.

Run it from the repository root:

```bash
.venv/bin/python run_scripts/common/run_imaginary_tournament.py \
  --pyramidal-results <run>/pyramidal \
  --output-dir <run>/imaginary-tournament
```

The outputs are `player_ppg.csv`, `games.csv`, and `summary.json`.
`evaluation.py` owns input loading, simulation, and writing. Argument parsing,
terminal output, and execution live in the runner above.

This is a simulation demonstration rather than an accuracy evaluation against
real outcomes. Buzzes use the first token at which a player's current-token
buzz probability reaches 0.5; calibrated correctness uses the same 0.5 threshold.
The shared game evaluator handles early -5 misses, opponent continuations, and
zero-point terminal misses. Same-token ties use seeded uniform random choice. Team scores and PPG
are tossup-only. The seed controls random rosters, packets, and same-token ties. Powers, overtime,
substitutions, and score corrections are not modeled.
