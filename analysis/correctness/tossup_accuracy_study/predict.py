"""Load the tested tree/spline ensemble without refitting either component."""
import json
import sys

import joblib
import numpy as np
import pandas as pd

from analysis.correctness.tossup_accuracy_study.run import OUTPUT

CATEGORICAL = ['player_id', 'tossup_id', 'category', 'player_category', 'item_clue']
NUMERIC = ['relative_position', 'terminal', 'margin', 'late_margin',
           'question_fraction', 'log_length', 'clue_phase', 'boundary']


class EnsemblePredictor:
    def __init__(self, fold=0):
        sys.path.insert(0, str(OUTPUT/'deps'))
        from catboost import CatBoostClassifier
        directory = OUTPUT/f'fold_{fold}'
        self.linear = joblib.load(directory/'regularized.joblib')['predictor']
        self.trees = CatBoostClassifier()
        self.trees.load_model(str(directory/'boosting/model.cbm'))
        selection = json.loads((directory/'boosting/selection.json').read_text())
        self.thresholds = selection['boosting_ensemble']['thresholds']

    def predict_proba(self, frame):
        return .5*self.linear.predict_proba(frame)+.5*self.trees.predict_proba(frame[CATEGORICAL+NUMERIC])

    def predict(self, frame, policy='f1_accuracy78'):
        threshold = self.thresholds[policy]
        if threshold is None:
            raise ValueError(f'Policy {policy} was infeasible in this fold validation set')
        return self.predict_proba(frame)[:, 1] >= threshold


def verify():
    from analysis.correctness.paper_readiness.first_buzz_features import load_first_buzzes
    from compirt_data import load_hf_tables
    tables = load_hf_tables(split='year_2024')
    first = load_first_buzzes(tables)
    bounds = tables['tossups'].set_index('tossup_id').sentence_boundaries.to_dict()
    first['item_clue'] = [f'{j}::clue-{np.searchsorted(bounds[j], t)}'
                          for j, t in zip(first.tossup_id, first.t_star)]
    checks = []
    for fold in range(5):
        saved = pd.read_csv(OUTPUT/f'fold_{fold}/boosting/predictions.csv')
        frame = first.loc[saved.event_id]
        model = EnsemblePredictor(fold)
        probability = model.predict_proba(frame)[:, 1]
        error = float(np.max(np.abs(probability-saved.boosting_ensemble)))
        assert error < 1e-9, (fold, error)
        for policy, threshold in model.thresholds.items():
            if threshold is not None:
                assert np.array_equal(probability >= threshold, saved['boosting_ensemble__'+policy])
        checks.append(dict(fold=fold, maximum_probability_error=error))
    (OUTPUT/'ensemble_load_checks.json').write_text(json.dumps(checks, indent=2))
    print('All five saved ensembles reproduce probabilities and policy decisions.')


if __name__ == '__main__':
    verify()
