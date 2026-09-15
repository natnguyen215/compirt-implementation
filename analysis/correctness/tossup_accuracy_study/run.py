"""Run isolated, validation-selected tossup correctness experiments."""

import argparse
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, precision_recall_curve
from sklearn.model_selection import GroupShuffleSplit
import torch

from analysis.correctness.paper_readiness.first_buzz_features import ROOT, load_first_buzzes, metrics
from analysis.correctness.tossup_accuracy_study.models import fit_linear, fit_timing
from compirt_data import load_hf_tables, build_tossup_observations
from holdout.game_splits import GameHoldoutSpec, game_holdout_masks


OUTPUT = Path('results/compirt/holdout/common/tossup-accuracy-study')


def configs():
    base = dict(player=1., item=1., local=1., curve='linear')
    result = [base]
    for field in ['player', 'item', 'local']:
        for value in [.3, 3.]:
            result.append({**base, field: value})
    for value in [.3, 3.]:
        result.append({**base, 'player': value, 'item': value, 'local': value})
    for value in [.3, 1., 3.]:
        result.append({**base, 'curve': 'spline', 'local': value})
    for value in [.3, 1.]:
        result.append({**base, 'clue': value})
    return result


def thresholds(y, p):
    precision, recall, cut = precision_recall_curve(y, p)
    precision, recall = precision[:-1], recall[:-1]
    tp = recall*np.sum(y)
    fp = tp/np.maximum(precision, 1e-15)-tp
    fn = np.sum(y)-tp
    accuracy = 1-(fp+fn)/len(y)
    f1 = 2*precision*recall/np.maximum(precision+recall, 1e-15)
    result = {'default': .5, 'accuracy': float(cut[np.argmax(accuracy)])}
    for name, eligible, criterion in [
        ('precision60', (precision >= .6) & (tp+fp >= 50), recall),
        ('f1_accuracy77', accuracy >= .77, f1),
        ('f1_accuracy78', accuracy >= .78, f1),
        ('f1_accuracy80p6', accuracy >= .806, f1),
    ]:
        indexes = np.flatnonzero(eligible)
        result[name] = float(cut[indexes[np.argmax(criterion[indexes])]]) if len(indexes) else None
    return result


def races(observations, player_map, item_map):
    events = observations.groupby('event_id', sort=False)
    n, width = len(events), int(events.size().max())
    roster = np.zeros((n, width), dtype=np.int64)
    mask = np.zeros((n, width), dtype=np.float32)
    item, token, total, winner, games = [], [], [], [], []
    for index, (_, event) in enumerate(events):
        ids = [player_map[p] for p in event.player_id]
        roster[index, :len(ids)] = ids
        mask[index, :len(ids)] = 1
        first = event.iloc[0]
        item.append(item_map[first.tossup_id])
        token.append(first.t_star)
        total.append(first.T_j)
        buzz = np.flatnonzero(event.z.to_numpy() == 'BUZZ')
        winner.append(int(buzz[0]) if len(buzz) else -1)
        games.append(first.game_id)
    arrays = [roster, mask, np.asarray(item), np.asarray(token, dtype=np.float32),
              np.asarray(total, dtype=np.float32), np.asarray(winner)]
    return [torch.as_tensor(a, device='cuda') for a in arrays], np.asarray(games)


def race_subset(race, games, keep):
    index = torch.as_tensor(np.isin(games, list(keep)), device='cuda')
    return [x[index] for x in race]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folds', type=int, nargs='+', default=list(range(5)))
    args = parser.parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(1)
    tables = load_hf_tables(split='year_2024')
    first = load_first_buzzes(tables)
    obs = build_tossup_observations(tables)
    player_map = {p:i for i,p in enumerate(sorted(set(obs.player_id) | set(first.player_id)))}
    item_map = {p:i for i,p in enumerate(sorted(set(obs.tossup_id) | set(first.tossup_id)))}
    first['player_index'] = first.player_id.map(player_map)
    first['item_index'] = first.tossup_id.map(item_map)
    bounds = tables['tossups'].set_index('tossup_id').sentence_boundaries.to_dict()
    first['item_clue'] = [f'{j}::clue-{np.searchsorted(bounds[j], t)}'
                          for j,t in zip(first.tossup_id, first.t_star)]
    race, race_games = races(obs, player_map, item_map)
    for fold in args.folds:
        directory = OUTPUT/f'fold_{fold}'
        directory.mkdir(exist_ok=True)
        if (directory/'complete.json').exists():
            print('Skipping completed fold', fold, flush=True)
            continue
        start = time.time()
        saved = pd.read_csv(ROOT/f'fold_{fold}/holdout/pyramidal/tossup_predictions.csv')
        saved = saved[saved.z.eq('BUZZ')]
        test = first.loc[saved.event_id].copy()
        assert np.array_equal(test.neg.to_numpy(), 1-saved.y.to_numpy())
        assert np.allclose(test.relative_position, saved.relative_position)
        held_out = game_holdout_masks(tables, GameHoldoutSpec('year_2024','test',5,fold,42))
        held_out_games = set(tables['games'].loc[held_out,'game_id'])
        train = first[~first.game_id.isin(held_out_games)].copy()
        train_games = set(tables['games'].game_id)-held_out_games
        # Split all eligible training games, including games with dead events.
        group_list = np.asarray(sorted(train_games))
        splitter = GroupShuffleSplit(n_splits=1, test_size=.2, random_state=20260908+fold)
        fit_idx, val_idx = next(splitter.split(group_list, groups=group_list))
        fit_games, val_games = set(group_list[fit_idx]), set(group_list[val_idx])
        fit = train[train.game_id.isin(fit_games)]
        val = train[train.game_id.isin(val_games)]
        assert not fit_games & val_games and not train_games & held_out_games
        pd.DataFrame({'game_id':group_list, 'inner_partition':[
            'fit' if g in fit_games else 'validation' for g in group_list
        ]}).to_csv(directory/'inner_split.csv', index=False)
        predictions = test[['event_id','game_id','tossup_id','neg','value','terminal']].reset_index(drop=True)
        predictions['saved_compirt'] = 1-saved.predicted_correct.to_numpy()
        selections, candidate_rows = {}, []

        def save_candidate(family, config, probability, steps=None):
            score = float(average_precision_score(val.neg, probability))
            row = {'family':family,'config':config,'validation_neg_ap':score,'steps':steps}
            candidate_rows.append(row)
            (directory/'candidates.json').write_text(json.dumps(candidate_rows,indent=2))
            print('candidate', fold, family, config, round(score,5), steps, flush=True)
            return score

        def save_family(name, config, validation_probability, probability, steps=None):
            selected = thresholds(val.neg.to_numpy(), validation_probability)
            selections[name] = {'config':config,'steps':steps,'thresholds':selected,
                                'validation_neg_ap':float(average_precision_score(val.neg, validation_probability))}
            predictions[name] = probability
            for policy, threshold in selected.items():
                if threshold is not None:
                    predictions[name+'__'+policy] = probability >= threshold
            predictions.to_csv(directory/'predictions.csv',index=False)
            (directory/'selection.json').write_text(json.dumps(selections,indent=2))
            print('finished',fold,name,'outer diagnostic',metrics(test.neg.to_numpy(),probability,probability>=.5),flush=True)

        best = (-1,None,None)
        for config in configs():
            probability = fit_linear(fit,val,config)
            score = save_candidate('regularized',config,probability)
            if score > best[0]:
                best = score, config, probability
        _, linear_config, linear_val = best
        linear_test = fit_linear(train,test,linear_config)
        save_family('regularized',linear_config,linear_val,linear_test)

        fit_race = race_subset(race,race_games,fit_games)
        train_race = race_subset(race,race_games,train_games)
        print('training timing-only skills',fold,flush=True)
        inner_timing = fit_timing(fit_race,len(player_map),len(item_map),42+fold)
        outer_timing = fit_timing(train_race,len(player_map),len(item_map),42+fold)
        torch.save({'inner':inner_timing.state_dict(),'outer':outer_timing.state_dict(),
                    'player_map':player_map,'item_map':item_map},directory/'timing_skills.pt')
        inner_skills = inner_timing.skills().detach().cpu().numpy()
        outer_skills = outer_timing.skills().detach().cpu().numpy()
        best = (-1,None,None)
        for scale in [.25,.5,1.]:
            config = {**linear_config,'skill':scale}
            probability = fit_linear(fit,val,config,inner_skills)
            score = save_candidate('frozen_skills',config,probability)
            if score > best[0]:
                best = score, config, probability
        _,config,val_probability = best
        probability = fit_linear(train,test,config,outer_skills)
        save_family('frozen_skills',config,val_probability,probability)

        (directory/'complete.json').write_text(json.dumps({'seconds':time.time()-start,
                                                         'n_train':len(train),'n_test':len(test)},indent=2))
        print('FOLD COMPLETE',fold,round(time.time()-start,1),flush=True)


if __name__ == '__main__':
    main()
