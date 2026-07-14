# 2024 ACF Nationals Model Ranking Summary

Tournament: `2024-acf-nationals`

## How Correlations Are Calculated

The real-world rank is built from tournament individual scoring. The public [2024 ACF Nationals player standings](https://quizbowlstats.com/tournaments/2045) are ordered by PPG and do not state a minimum-games or minimum-TUH eligibility floor, so this batch defaults to `min_games=1` and `min_tuh=1`. It includes only games with at least `20` tossups as a source-data integrity rule, not a player eligibility threshold.

This aggregate uses `actual_ppg`, which is `actual_points / games`, with total points and `player_id` used as tie-breakers.

`tournament_rank_correlation` is the Pearson correlation between `actual_rank` and `tournament_model_rank` for players present in both rankings. `tournament_model_rank` is recalculated from this tournament's `BUZZ` rows only, sorting by average fitted `predicted_correct`, then model buzz count, then `player_id`.

Because both inputs are ranks, this Pearson calculation is equivalent to a Spearman rank correlation over the matched players. The global and tournament rank correlations are identical for these runs because the models were fit on this one tournament, so this summary reports only the tournament-filtered correlation.

Higher positive values mean the model ordering is more aligned with the real PPG ordering. `1.0` would be perfect agreement, `0` means little linear rank alignment, and negative values mean the ordering is moving in the opposite direction.

## Top-N Overlap Columns

`actual_top_20_in_tournament_model_rank_top_20` counts how many of the real top 20 players also appear in the model's top 20. `actual_top_50_in_tournament_model_rank_top_50` does the same check for the real top 50 against the model's top 50. A value like `17/20` means 17 of the real top 20 were captured by the model top 20; a value like `38/50` means 38 of the real top 50 were captured by the model top 50.

| run_name | calibration | tournament_rank_correlation | actual_top_20_in_tournament_model_rank_top_20 | actual_top_50_in_tournament_model_rank_top_50 |
| --- | --- | --- | --- | --- |
| baseline | no_cal | 0.454867 | 4/20 | 18/50 |
| baseline-cal | cal | 0.546334 | 5/20 | 25/50 |
| plda | no_cal | 0.830674 | 12/20 | 32/50 |
| plda-cal | cal | 0.166165 | 5/20 | 14/50 |
| lda | no_cal | 0.805231 | 10/20 | 31/50 |
| lda-cal | cal | 0.0955036 | 2/20 | 12/50 |
| category | no_cal | 0.602579 | 7/20 | 26/50 |
| category-cal | cal | -0.100421 | 1/20 | 9/50 |
| learned-topic | no_cal | 0.793767 | 10/20 | 32/50 |
| learned-topic-cal | cal | 0.0678988 | 2/20 | 14/50 |
| multidim | no_cal | 0.803039 | 9/20 | 32/50 |
| multidim-cal | cal | 0.760299 | 11/20 | 32/50 |
| embedding | no_cal | 0.853546 | 14/20 | 32/50 |
| embedding-cal | cal | 0.219517 | 5/20 | 19/50 |
| tfidf-cumulative-difficulty | no_cal | 0.674354 | 5/20 | 25/50 |
| tfidf-cumulative-difficulty-cal | cal | 0.593457 | 7/20 | 28/50 |
| tfidf-multidim-cumulative-difficulty | no_cal | 0.808229 | 10/20 | 32/50 |
| tfidf-multidim-cumulative-difficulty-cal | cal | 0.716793 | 11/20 | 32/50 |
