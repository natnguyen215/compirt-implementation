# Complete five-fold normalized retraining comparison

All 95 queue tasks finished without failures at 2026-09-13 17:25:51 America/Los_Angeles.

Tossup probability scores pool 46,640 race events; correctness and position scores use 45,995 observed buzzes. Both historical and retrained parameters are scored with normalized full-grid replay. This differs from historical unnormalized/older-convention event losses. All bonus models have matched observations, labels and lineups: 128,100 parts / 42,700 bonuses / 450 teams. Game replay uses fold means, schema 3 and seed 42. Game predictions are tossup-only, not combined tossup-plus-bonus match predictions.

## Tossups

| model | version | correctness_accuracy | correctness_log_loss | correctness_auc | timing_mae | joint_nll | first_buzzer_accuracy | predicted_dead_rate | dead_brier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD | historical | 0.77949777 | 0.48777248 | 0.71543873 | 0.15186356 | 6.61552614 | 0.35164692 | 0.01476979 | 0.01323399 |
| DD | retrained | 0.77934558 | 0.48778630 | 0.71536705 | 0.15442760 | 6.60427191 | 0.35332101 | 0.03121129 | 0.01524258 |
| Multidim | historical | 0.62752473 | 0.81103993 | 0.63197485 | 0.14542476 | 6.80241316 | 0.39584737 | 0.05868040 | 0.02117952 |
| Multidim | retrained | 0.62789434 | 0.80877752 | 0.63232367 | 0.14547064 | 6.79522563 | 0.39652136 | 0.06166073 | 0.02185833 |

## Bonuses

| model | version | arm | auc | log_loss | accuracy | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DD | historical | compositional | 0.89031550 | 0.41856976 | 0.80791569 | 0.51044496 | 1.98969009 |
| DD | historical | synergy | 0.89825503 | 0.40443578 | 0.81716628 | 0.53060890 | 0.90395824 |
| DD | retrained | compositional | 0.89034417 | 0.41848123 | 0.80790788 | 0.51044496 | 1.98380193 |
| DD | retrained | synergy | 0.89822236 | 0.40451103 | 0.81722092 | 0.53096019 | 0.91055047 |
| Multidim | historical | compositional | 0.88811991 | 0.42270494 | 0.80828259 | 0.51224824 | 2.04029526 |
| Multidim | historical | synergy | 0.89548749 | 0.41124874 | 0.81391881 | 0.52440281 | 1.17173862 |
| Multidim | retrained | compositional | 0.88825968 | 0.42259512 | 0.80847775 | 0.51285714 | 2.03511538 |
| Multidim | retrained | synergy | 0.89549244 | 0.41133401 | 0.81380952 | 0.52421546 | 1.17768861 |

## Game replay

| model | version | tossup_game_winner_accuracy | tossup_model_official_winner_accuracy | tossup_game_margin_mae | first_buzzer_team_replay_accuracy | tossup_scorer_team_replay_accuracy |
| --- | --- | --- | --- | --- | --- | --- |
| DD | historical | 0.64725823 | 0.65963594 | 49.62218253 | 0.47533324 | 0.42844967 |
| DD | retrained | 0.65569536 | 0.66955423 | 48.38269949 | 0.41016007 | 0.39035875 |
| Multidim | retrained | 0.15933620 | 0.15986479 | 55.82491188 | 0.01201640 | 0.09430392 |

Historical DD game replay is the updated token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42 reference, not obsolete game metrics stored beside older fits. Historical multidimensional game replay has not been refreshed here and is not compared. Frozen-skills fits remain unchanged. These are reused development folds and one optimization seed. Research logs and existing frozen-skills comparison tables remain historical; this report records the new comparison separately.
