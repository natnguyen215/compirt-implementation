"""Independent categorical boosting comparison on the study's exact splits."""
import json
import sys
import time

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score

from analysis.correctness.tossup_accuracy_study.run import OUTPUT, thresholds
from analysis.correctness.tossup_accuracy_study.models import fit_linear
from analysis.correctness.paper_readiness.first_buzz_features import load_first_buzzes
from compirt_data import load_hf_tables

sys.path.insert(0, str(OUTPUT / 'deps'))
from catboost import CatBoostClassifier  # noqa: E402


def main():
    tables = load_hf_tables(split='year_2024')
    first = load_first_buzzes(tables)
    bounds = tables['tossups'].set_index('tossup_id').sentence_boundaries.to_dict()
    first['item_clue'] = [f'{j}::clue-{np.searchsorted(bounds[j], t)}'
                          for j, t in zip(first.tossup_id, first.t_star)]
    categorical = ['player_id', 'tossup_id', 'category', 'player_category', 'item_clue']
    numeric = ['relative_position', 'terminal', 'margin', 'late_margin',
               'question_fraction', 'log_length', 'clue_phase', 'boundary']
    columns = categorical + numeric
    for fold in range(5):
        directory = OUTPUT / f'fold_{fold}' / 'boosting'
        directory.mkdir(exist_ok=True)
        if (directory / 'complete.json').exists():
            continue
        start = time.time()
        partitions = pd.read_csv(directory.parent / 'inner_split.csv')
        train = first[first.game_id.isin(partitions.game_id)]
        fit = train[train.game_id.isin(partitions.loc[partitions.inner_partition.eq('fit'), 'game_id'])]
        val = train[train.game_id.isin(partitions.loc[partitions.inner_partition.eq('validation'), 'game_id'])]
        predictions = pd.read_csv(directory.parent / 'predictions.csv')
        test = first.loc[predictions.event_id]
        assert not set(train.game_id) & set(test.game_id)
        best = (-1, None, None, None)
        candidates = []
        for depth, penalty in [(4, 5), (4, 20), (6, 5), (6, 20), (8, 5), (8, 20)]:
            config = dict(depth=depth, l2_leaf_reg=penalty, learning_rate=.05,
                          iterations=1000, loss_function='Logloss', eval_metric='AUC',
                          random_seed=42+fold, thread_count=4, allow_writing_files=False,
                          verbose=False, cat_features=categorical)
            model = CatBoostClassifier(**config)
            model.fit(fit[columns], fit.neg, eval_set=(val[columns], val.neg),
                      early_stopping_rounds=100, use_best_model=True)
            probability = model.predict_proba(val[columns])[:, 1]
            score = float(average_precision_score(val.neg, probability))
            iterations = model.tree_count_
            candidates.append(dict(config=config, validation_neg_ap=score, iterations=iterations))
            (directory/'candidates.json').write_text(json.dumps(candidates, indent=2))
            print('boost', fold, depth, penalty, iterations, score, flush=True)
            if score > best[0]:
                best = score, config, probability, iterations
        score, config, validation_probability, iterations = best
        config = {**config, 'iterations':iterations}
        model = CatBoostClassifier(**config)
        model.fit(train[columns], train.neg)
        model.save_model(str(directory/'model.cbm'))
        probability = model.predict_proba(test[columns])[:, 1]
        selection = {}
        linear_config = json.loads((directory.parent/'selection.json').read_text())['regularized']['config']
        linear_validation = fit_linear(fit, val, linear_config)
        for name, vp, tp in [
            ('boosting', validation_probability, probability),
            ('boosting_ensemble', .5*validation_probability+.5*linear_validation,
             .5*probability+.5*predictions.regularized.to_numpy()),
        ]:
            selected = thresholds(val.neg.to_numpy(), vp)
            selection[name] = dict(config=config, thresholds=selected,
                                   validation_neg_ap=float(average_precision_score(val.neg, vp)))
            predictions[name] = tp
            for policy, cut in selected.items():
                if cut is not None:
                    predictions[name+'__'+policy] = tp >= cut
        predictions.to_csv(directory/'predictions.csv', index=False)
        (directory/'selection.json').write_text(json.dumps(selection, indent=2))
        (directory/'complete.json').write_text(json.dumps(dict(seconds=time.time()-start)))
        print('BOOST FOLD COMPLETE', fold, time.time()-start, flush=True)


if __name__ == '__main__':
    main()
