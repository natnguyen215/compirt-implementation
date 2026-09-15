"""New mark-model experiments on the existing development folds.

Uses the previous study's train-internal game splits verbatim. No outer labels
are used for feature fitting, candidate selection, or threshold selection.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, log_loss

from analysis.correctness.paper_readiness.first_buzz_features import ROOT, load_first_buzzes
from analysis.correctness.tossup_accuracy_study.run import thresholds
from analysis.correctness.bayesian_mark_study.models import features, fit_map, variational
from compirt_data import load_hf_tables
from holdout.game_splits import GameHoldoutSpec, game_holdout_masks

OUTPUT = Path('results/compirt/holdout/common/bayesian-mark-study')
PREVIOUS = Path('results/compirt/holdout/common/tossup-accuracy-study')
# Whole-prefix fits are retained only as a dependency of the predictive mixture.
FAMILIES = {
    'whole_prefix': [{'text': v, 'text_column': 'prefix_text'} for v in [1., 3.]],
    'vb_base': [{'vb': True}],
}


def load_data():
    tables = load_hf_tables(split='year_2024')
    first = load_first_buzzes(tables)
    questions = tables['tossups'].set_index('tossup_id')
    first['subcategory'] = first.category+'::'+first.tossup_id.map(questions.subcategory).fillna('Unknown')
    first['player_subcategory'] = first.player_id+'::'+first.subcategory
    tokens = questions.tokens.to_dict()
    first['window_text'] = [' '.join(tokens[j][max(0, int(t)-24):int(t)])
                            for j, t in zip(first.tossup_id, first.t_star)]
    first['prefix_text'] = [' '.join(tokens[j][:int(t)])
                            for j, t in zip(first.tossup_id, first.t_star)]
    return tables, first


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folds', nargs='+', type=int, default=list(range(5)))
    parser.add_argument('--families', nargs='+', choices=list(FAMILIES), default=list(FAMILIES))
    parser.add_argument('--device', default='cuda')
    args = parser.parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    tables, first = load_data()
    for fold in args.folds:
        directory = OUTPUT/f'fold_{fold}'; directory.mkdir(exist_ok=True)
        saved = pd.read_csv(ROOT/f'fold_{fold}/holdout/pyramidal/tossup_predictions.csv')
        saved = saved[saved.z.eq('BUZZ')]
        test = first.loc[saved.event_id].copy()
        assert np.array_equal(test.neg, 1-saved.y.to_numpy())
        assert np.allclose(test.relative_position, saved.relative_position)
        mask = game_holdout_masks(tables, GameHoldoutSpec('year_2024', 'test', 5, fold, 42))
        held_out = set(tables['games'].loc[mask, 'game_id'])
        train = first[~first.game_id.isin(held_out)].copy()
        split = pd.read_csv(PREVIOUS/f'fold_{fold}/inner_split.csv')
        fit = train[train.game_id.isin(split.loc[split.inner_partition.eq('fit'), 'game_id'])]
        val = train[train.game_id.isin(split.loc[split.inner_partition.eq('validation'), 'game_id'])]
        assert len(fit)+len(val) == len(train)
        assert not set(fit.game_id)&set(val.game_id)
        assert not set(train.game_id)&held_out
        assert set(test.game_id) <= held_out
        for family in args.families:
            path = directory/f'{family}.json'
            if path.exists():
                continue
            start = time.time(); candidates = []; best = None
            for config in FAMILIES[family]:
                x, z, groups, names = features(fit, val, config)
                if config.get('vb'):
                    p, plugin, info = variational(x, z, fit, groups, names, config, args.device)
                else:
                    p, info = fit_map(x, z, fit, config); plugin = p
                score = float(average_precision_score(val.neg, p))
                candidates.append({'config': config, 'validation_ap': score,
                                   'validation_log_loss': float(log_loss(val.neg, p)), 'fit': info})
                print('candidate', fold, family, config, round(score, 6), flush=True)
                if best is None or score > best[0]:
                    best = (score, config, p, plugin)
            _, config, val_p, val_plugin = best
            policies = thresholds(val.neg.to_numpy(), val_p)
            x, z, groups, names = features(train, test, config)
            if config.get('vb'):
                p, plugin, info = variational(x, z, train, groups, names, config, args.device)
            else:
                p, info = fit_map(x, z, train, config); plugin = p
            frame = test[['event_id', 'game_id', 'tossup_id', 'player_id', 'neg', 'value',
                          'relative_position', 'terminal', 'category', 'subcategory']].reset_index(drop=True)
            frame['fold'] = fold; frame['probability'] = p; frame['plugin_probability'] = plugin
            for policy, cut in policies.items():
                if cut is not None:
                    frame[policy] = p >= cut
            frame.to_csv(directory/f'{family}.csv', index=False)
            pd.DataFrame({'event_id': val.event_id, 'game_id': val.game_id, 'neg': val.neg,
                          'probability': val_p, 'plugin_probability': val_plugin}).to_csv(
                              directory/f'{family}_validation.csv', index=False)
            result = {'family': family, 'config': config, 'candidates': candidates,
                      'thresholds': policies, 'fit': info, 'seconds': time.time()-start,
                      'n_train': len(train), 'n_fit': len(fit), 'n_val': len(val), 'n_test': len(test),
                      'inner_split_sha256': hashlib.sha256((PREVIOUS/f'fold_{fold}/inner_split.csv').read_bytes()).hexdigest()}
            path.write_text(json.dumps(result, indent=2)+'\n')
            print('finished', fold, family, round(result['seconds'], 1), flush=True)


if __name__ == '__main__':
    main()
