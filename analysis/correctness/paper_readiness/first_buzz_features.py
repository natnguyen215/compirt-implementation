"""Shared first-buzz features and metrics; preliminary experiment sweep retired."""

from pathlib import Path

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    f1_score,
    log_loss,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
)

from analysis.season_2024_25_eda.analyze import clue_phase


ROOT = Path(
    'results/compirt/holdout/double-difficulty/ablations/model-components/'
    'relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal'
)
def load_first_buzzes(tables):
    """Construct features without using outcomes of other held-out events."""
    data = tables['tossup_buzzes'].copy()
    data['_order'] = data.buzz_id.str.rsplit('-', n=1).str[-1].astype(int)
    data = data.sort_values(['game_id', 'tossup_id', 'token_position', '_order'])
    data = data.drop_duplicates(['game_id', 'tossup_id']).copy()
    data['event_id'] = data.game_id + '::' + data.tossup_id
    data['T_j'] = data.num_tokens_total.clip(lower=1)
    data['t_star'] = np.minimum(data.token_position.clip(lower=1), data.T_j)
    data['relative_position'] = data.t_star / data.T_j
    data['terminal'] = (data.t_star == data.T_j).astype(int)
    data['neg'] = 1 - data.correct.astype(int)
    questions = tables['tossups'].set_index('tossup_id')
    data['category'] = data.tossup_id.map(questions.category).fillna('Unknown')
    data['category'] = data.category.replace('', 'Unknown')
    data['player_category'] = data.player_id + '::' + data.category
    # Source builder saves these scores before adding the observed buzz value.
    data['margin'] = ((data.team_score - data.opponent_score) / 100).clip(-5, 5)
    data['question_fraction'] = data.question_number_in_game / 20
    data['late_margin'] = data.margin * data.question_fraction
    data['log_length'] = np.log(data.T_j / 100)
    phase = [
        clue_phase(int(t), questions.at[j, 'sentence_boundaries'], int(total))
        for t, j, total in zip(data.t_star, data.tossup_id, data.T_j)
    ]
    data['clue_phase'] = [v[0] for v in phase]
    data['boundary'] = [int(v[1]) for v in phase]
    return data.set_index('event_id', drop=False)


def metrics(y, p, prediction):
    precision, recall, thresholds = precision_recall_curve(y, p)
    eligible = np.flatnonzero(precision[:-1] >= .6)
    diagnostic_recall = float(recall[eligible].max()) if len(eligible) else 0.0
    target_recall = np.flatnonzero(recall[:-1] >= .5)
    diagnostic_precision = float(precision[target_recall].max())
    return {
        'n': len(y),
        'log_loss': float(log_loss(y, p)),
        'neg_ap': float(average_precision_score(y, p)),
        'auc': float(roc_auc_score(y, p)),
        'accuracy': float(accuracy_score(y, prediction)),
        'neg_precision': float(precision_score(y, prediction, zero_division=0)),
        'neg_recall': float(recall_score(y, prediction)),
        'neg_f1': float(f1_score(y, prediction)),
        'retrospective_recall_at_precision_60': diagnostic_recall,
        'retrospective_precision_at_recall_50': diagnostic_precision,
    }
