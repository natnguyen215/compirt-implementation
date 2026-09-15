# terminal_cell

Why the last token position of a tossup is not just another token.

Every pyramidal family models a tossup as a discrete-time survival process over
token positions `1 .. T_j` and gives each position the same kind of cell, with a
hazard that varies only through a smooth curve in the relative position
`x = t / T_j`. This folder measures the empirical game--tossup first-buzz
hazard cell by cell and shows that assumption is violated at exactly one place:
the end. An event is one tossup read in one game, so this is the hazard that the
first buzz by anyone in the game occurs in a cell; it is not a per-team or
per-player hazard.

## Exact calculation

Let `B_e` indicate that game--tossup event `e` has a recorded first buzz. For a
buzzed event, the observation builder clamps its recorded position to the
question bounds,

\[
\tau_e=\min\!\left(\max(1,\text{raw\_token\_position}_e),T_e\right),
\]

and defines the number of tokens remaining as `R_e = T_e - \tau_e`. A dead
tossup has `B_e=0` and no `R_e`. For the cell with `r` tokens remaining,
`hazard_by_tokens_remaining` computes

\[
\widehat h(r)
=
\frac{\sum_e \mathbf 1[B_e=1\ \land\ R_e=r]}
     {\sum_e \mathbf 1[B_e=0\ \lor\ R_e\le r]}.
\]

The numerator is the number of events whose first buzz occurs in that exact
cell. The denominator is its risk set: dead events plus buzzed events whose
first buzz occurs in that cell or a later one. Events that buzzed earlier are
therefore excluded. This is the discrete-time empirical hazard conditional on
the event having remained unbuzzed upon entering the cell.

For example, at `r=0` the reported estimate is `2,065 / 2,763 = 0.7474`; at
`r=1` it is `1,119 / 3,882 = 0.2883`. These are exact-position estimates, not
fractions of all 48,612 events.

## Result (`--split year_2024`, 48,612 events, dead rate 1.44%)

| Tokens remaining | At risk | Buzzes | Event first-buzz hazard |
| ---: | ---: | ---: | ---: |
| 14 | 10,045 | 487 | 0.0485 |
| 7 | 7,071 | 441 | 0.0624 |
| 4 | 5,689 | 525 | 0.0923 |
| 2 | 4,567 | 685 | 0.1500 |
| 1 | 3,882 | 1,119 | 0.2883 |
| **0** | **2,763** | **2,065** | **0.7474** |

The hazard rises gently and smoothly through the question — about 0.05 in the
middle, roughly tripling over the last dozen tokens — and then **jumps by a
factor of 2.6 in the final cell**. Position `T_j` is where the reader stops and
the whole post-reading buzz window is recorded, so that cell covers far more
real time than any single token before it.

A degree-`p` Bernstein (or sigmoid, or spline) curve in `x` cannot produce a
jump of that size across one token, which is about 0.0075 of a 133-token
question. A model without a separate terminal term has to approximate it by
making the whole curve steeper, which spreads first-buzz mass too early and
leaves survival stranded past the end of the question — the mechanism behind the
4–7x over-prediction of dead tossups.

## It holds on every 2024 question set

Each set was measured independently. The jump is present in all four, and its
size is monotone in the difficulty of the set:

| question set | final cell | one token earlier | ratio |
| --- | ---: | ---: | ---: |
| ACF Fall (easiest) | 0.7931 | 0.2564 | 3.1x |
| ACF Winter | 0.8287 | 0.2590 | 3.2x |
| ACF Regionals | 0.6995 | 0.2727 | 2.6x |
| ACF Nationals (hardest) | 0.6357 | 0.3778 | 1.7x |

Easier sets pile more mass into the giveaway because a larger share of their
questions are still unanswered when the reader finishes. At Nationals the
stronger field buzzes earlier, so less probability survives to the final cell
and the discontinuity is correspondingly smaller. The effect is therefore a
property of the reading protocol, modulated by how hard the set is — not an
artifact of one tournament.

This is the evidence behind the double-difficulty families' terminal-cell
intercepts; see [`../../docs/double-difficulty-bernstein.md`](../../docs/double-difficulty-bernstein.md#terminal-cell-intercepts).

## Reproduce

```bash
.venv/bin/python -m analysis.terminal_cell.analyze --split year_2024
# one question set at a time
.venv/bin/python -m analysis.terminal_cell.analyze --tournament 2024-acf-regionals
```

Writes `data/hazard_by_tokens_remaining.csv` and
`data/hazard_by_relative_position.csv`.
