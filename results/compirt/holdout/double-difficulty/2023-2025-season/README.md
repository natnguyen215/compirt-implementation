# Data splits

The reference configuration refit on a different population. **Metrics here
cannot be compared with the `year_2024` runs elsewhere in this tree** — the
event population, its no-buzz rate and its all-correct baseline all differ.

| Folder | Split | Notes |
| --- | --- | --- |
| [`season-2023-25/`](season-2023-25/) | `base_split=all` (ACF 2023-25) | Same model as [`../reference-model/`](../reference-model/); 3x the data. Its joint event LL of 5.5353 is lower than the 2024 runs because the population changed, not because the model improved. |
