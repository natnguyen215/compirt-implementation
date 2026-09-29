# Game-winner ablations at observed buzz positions

Frozen saved fits; five whole-game folds, split seed 42. All models use
2,331 complete games and the same literal recorded tossup scores. Excluding
66 recorded tossup ties leaves 2,265 decisive games. Accuracy pools these
games equally. Predicted ties are incorrect. No training is performed.

| Saved fit | Skills-only LSE | Correctness-only, observed buzz position | Full token-threshold replay |
| --- | ---: | ---: | ---: |
| DD-Bernstein, unconstrained terminal | 70.68% | 72.98% | 69.27% |
| DD-Bernstein, 3,000 steps | 67.06% | 67.33% | 65.56% |
| Multidimensional, 3,000 steps | 68.26% | 74.48% | 15.94% |

The CSVs also retain the historical DD bonus-reference fit from the earlier
comparison: 67.06% skills-only, 67.42% correctness-only, and 64.72% full replay.
The unconstrained-terminal and bonus-reference fits are historical; the two
3,000-step rows use the normalized-likelihood refits. Exact source paths and
input hashes are preserved below. These are reused development folds.

Skills-only takes each player's mean skill across dimensions, applies
unnormalized LSE across active teammates with temperature 1, and averages team
scores across the game's questions. Correctness-only instead takes each
player's correctness logit at the observed first-buzz cell, applies LSE across
teammates and then sigmoid, and averages these team-question scores across the
game. Both teams use the same observed position. No-buzz events use the final
cell. All phase-0 active players enter, with no repeated bounceback rows.

Correctness logits retain saved question relevance, difficulty, player
correctness intercepts if present, and terminal-cell intercepts. The four
studied arms have identity correctness calibration, which the code verifies.
No observed correctness labels or buzzer identity enter this score.
**Observed timing does enter: this is a conditional diagnostic, not an
end-to-end game forecast.** The team score is a heuristic, not a calibrated
probability of winning a race or a points prediction.

Full replay uses the saved schema-3 token-threshold results, with 0.5 buzz and
correctness thresholds, negs, team lockout, opponent continuation, and seed 42
for same-token ties. The normalized multidimensional fit predicts ties in
1,802 decisive games; this explains much of its low replay winner accuracy.

## Reproduce

From the repository root:

```bash
.venv/bin/python -B results/compirt/holdout/common/game-winner-ablations/skills-lse-observed-position-correctness-and-token-replay-5fold/code/compare.py
```

The source fit and replay paths are listed in `CONFIGS` in
[`code/compare.py`](code/compare.py). The script also retains two alternative
skills-only definitions for the earlier aggregation-order sensitivity check;
these do not select the displayed baseline based on outcomes.

- [`summary.csv`](summary.csv): accuracies, exact correct-game counts,
  decisive-game denominators, and correctness/replay tie counts.
- [`game_predictions.csv`](game_predictions.csv): matched game IDs, observed
  winners, all team scores, and predictions for each method.
- [`validation.json`](validation.json): input SHA-256 hashes, fold event
  counts, and no-buzz event counts.

The run checks frozen training/holdout skill agreement, agreement of
reconstructed correctness with saved row probabilities, common stopping cells
within events, full lineup coverage for both teams, unique held-out games,
and identical game populations and targets across all four fits. Synthetic
checks also cover stable LSE and the player/terminal correctness intercepts.
