"""Refit/export selected fold predictors and verify saved predictions exactly."""
import json
import joblib
import numpy as np
import pandas as pd
import torch

from compirt_data import load_hf_tables
from analysis.correctness.paper_readiness.first_buzz_features import load_first_buzzes
from analysis.correctness.tossup_accuracy_study.run import OUTPUT
from analysis.correctness.tossup_accuracy_study.predictor import CorrectnessPredictor


def main():
    first = load_first_buzzes(load_hf_tables(split='year_2024'))
    checks = []
    for fold in range(5):
        directory = OUTPUT/f'fold_{fold}'
        partitions = pd.read_csv(directory/'inner_split.csv')
        train = first[first.game_id.isin(partitions.game_id)]
        prediction = pd.read_csv(directory/'predictions.csv')
        test = first.loc[prediction.event_id]
        selections = json.loads((directory/'selection.json').read_text())
        timing = torch.load(directory/'timing_skills.pt', map_location='cpu', weights_only=False)
        skills = torch.cat([timing['outer']['theta'], timing['outer']['speed'][:, None]], 1).numpy()
        skill_map = {p:skills[i] for p, i in timing['player_map'].items()}
        for family in ['regularized', 'frozen_skills']:
            predictor = CorrectnessPredictor(selections[family]['config'],
                                             skill_map if family == 'frozen_skills' else None).fit(train)
            path = directory/(family+'.joblib')
            joblib.dump(dict(predictor=predictor, thresholds=selections[family]['thresholds'],
                             label='all incorrect first buzzes', fold=fold), path, compress=3)
            loaded = joblib.load(path)['predictor']
            error = float(np.max(np.abs(loaded.predict_proba(test)[:, 1]-prediction[family])))
            assert error < 1e-9, (fold, family, error)
            checks.append(dict(fold=fold, family=family, maximum_probability_error=error))
    (OUTPUT/'export_checks.json').write_text(json.dumps(checks, indent=2))
    print('Exported 10 fold predictors; saved predictions reproduced within 1e-9.')


if __name__ == '__main__':
    main()
