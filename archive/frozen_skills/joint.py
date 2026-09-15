"""Matched MAP joint fine-tuning versus blocked correctness-to-trait gradients.

Both arms start from the original fitted timing and spline correctness models.
They use identical summed likelihoods, original L2 penalties, and Adam settings.
The control updates timing from timing observations only, while its correctness
head follows the changing detached traits. It is not a static frozen checkpoint.
"""
import argparse
import json
from pathlib import Path
import sys
import time

import joblib
import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.nn import functional as F

from analysis.correctness.tossup_accuracy_study import predictor as predictor_module
from analysis.correctness.tossup_accuracy_study.models import TimingModel
from frozen_skills.data import races, first_buzzes, tensor
from frozen_skills.evaluation import predict_events, summarize, correctness_scores
from frozen_skills.pyramidal_model import correctness_linear
from frozen_skills.train_holdout import ROOT, MAP_ROOT, detached_cpu

OUTPUT = Path('results/compirt/holdout/frozen-skills/joint-map-spline')


def load_original(path):
    # Historical joblib files predate the analysis/correctness directory move.
    name = 'analysis.tossup_accuracy_study.predictor'
    old = sys.modules.get(name)
    sys.modules[name] = predictor_module
    try:
        return joblib.load(path)['predictor']
    finally:
        if old is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = old


def unpack_coefficients(predictor, item_map):
    coef = predictor.model.coef_[0]
    b = predictor.spline.n_features_out_
    p, j = len(predictor.player.categories_[0]), len(predictor.item.categories_[0])
    offset = 0
    def take(n):
        nonlocal offset
        out = coef[offset:offset+n].copy()
        offset += n
        return torch.tensor(out, dtype=torch.float32)
    out = dict(intercept=torch.tensor(predictor.model.intercept_, dtype=torch.float32),
               global_curve=take(b)[None], global_terminal=take(1), player_effect=take(p)[None])
    item_effect = take(j)
    local = take(j*(b+1)).reshape(b+1, j).T
    weight = take(j*4).reshape(4, j).T
    assert offset == len(coef)
    order = torch.tensor([item_map[x] for x in predictor.item.categories_[0]])
    for name, values in [('item_effect', item_effect), ('item_curve', local[:, :b]),
                         ('item_terminal', local[:, b]), ('skill_weight', weight)]:
        expanded = torch.zeros((len(item_map),)+values.shape[1:])
        expanded[order] = values
        out[name] = expanded[None]
    return out


def design(frame, transforms, device):
    return dict(basis=tensor(transforms['spline'].transform(frame[['relative_position']]), device),
                terminal=tensor(frame.terminal, device),
                player=tensor([transforms['correctness_players'].get(p,-1) for p in frame.player_id], device, True),
                item=tensor([transforms['item_map'][j] for j in frame.tossup_id], device, True),
                trait_index=tensor([transforms['player_map'][p] for p in frame.player_id], device, True))


def standardized_traits(timing, train_ids, row_ids, feedback=True):
    raw = timing.skills()
    if not feedback:
        raw = raw.detach()
    train = raw[train_ids]
    mean = train.mean(0)
    sd = train.std(0, correction=0).clamp_min(.1)
    return ((raw[row_ids]-mean)/sd)[None], mean, sd


def mark_logits(timing, coefficients, data, train_ids, config, feedback):
    skills, _, _ = standardized_traits(timing, train_ids, data['trait_index'], feedback)
    return correctness_linear(dict(data, skills=skills), coefficients, config)[0]


def race_tuple(data):
    return tuple(data[k] for k in ['players','mask','item','token','total','winner'])


def predict_saved(frame, artifact, device='cpu'):
    data = design(frame, artifact['transforms'], device)
    raw = torch.cat([artifact['timing']['theta'], artifact['timing']['speed'][:,None]], 1).to(device)
    data['skills'] = ((raw[data['trait_index']]-artifact['mean'].to(device))/artifact['sd'].to(device))[None]
    with torch.no_grad():
        return correctness_linear(data, {k:v.to(device) for k,v in artifact['coefficients'].items()}, artifact['config'])[0].sigmoid().cpu().numpy()


def fit_fold(fold, args):
    directory = args.output / f'fold_{fold}'
    directory.mkdir(parents=True, exist_ok=True)
    if all((directory/mode/'complete.json').exists() for mode in ['joint', 'blocked']):
        return
    source = MAP_ROOT / f'fold_{fold}'
    cp = torch.load(source/'timing_skills.pt', map_location='cpu', weights_only=False)
    original = load_original(source/'frozen_skills.joblib')
    assert original.config.get('curve') == 'spline' and not original.config.get('clue')
    coefficients = unpack_coefficients(original, cp['item_map'])
    transforms = dict(spline=original.spline, player_map=cp['player_map'], item_map=cp['item_map'],
                      correctness_players={p:i for i,p in enumerate(original.player.categories_[0])})
    train_rows = pd.read_csv(ROOT/f'fold_{fold}/train/pyramidal/tossup_predictions.csv')
    test_rows = pd.read_csv(ROOT/f'fold_{fold}/holdout/pyramidal/tossup_predictions.csv')
    splits = pd.read_csv(source/'inner_split.csv')
    assert set(train_rows.game_id) == set(splits.game_id)
    assert not set(train_rows.game_id) & set(test_rows.game_id)
    splits.to_csv(directory/'training_game_split.csv', index=False)
    pd.DataFrame({'game_id':sorted(test_rows.game_id.unique())}).to_csv(directory/'holdout_games.csv',index=False)
    train, test = first_buzzes(train_rows), first_buzzes(test_rows)
    saved = pd.read_csv(source/'predictions.csv').set_index('event_id')
    assert set(saved.index) == set(test.index)
    np.testing.assert_array_equal(saved.loc[test.index,'neg'], test.neg)
    fit_data, test_data = design(train, transforms, args.device), design(test, transforms, args.device)
    train_races, _ = races(train_rows, cp['player_map'], cp['item_map'], args.device)
    test_races, metadata = races(test_rows, cp['player_map'], cp['item_map'], args.device)
    train_ids = fit_data['trait_index']
    target = tensor(train.neg, args.device)
    for mode in ['blocked', 'joint']:
        out = directory/mode
        out.mkdir(exist_ok=True)
        if (out/'complete.json').exists():
            continue
        started = time.monotonic()
        timing = TimingModel(len(cp['player_map']), len(cp['item_map'])).to(args.device)
        timing.load_state_dict(cp['outer'])
        head = nn.ParameterDict({k:nn.Parameter(v.to(args.device).clone()) for k,v in coefficients.items()})
        with torch.no_grad():
            initial = mark_logits(timing, head, test_data, train_ids, original.config, False).sigmoid().cpu().numpy()
        initial_error = float(np.max(np.abs(initial-saved.loc[test.index,'frozen_skills'].to_numpy())))
        assert initial_error < 2e-5, initial_error
        optimizer = torch.optim.Adam(list(timing.parameters())+list(head.parameters()), lr=args.lr)
        rows = []
        print(f'Fold {fold}, {mode}: initial prediction error {initial_error:.2g}', flush=True)
        for step in range(args.steps):
            optimizer.zero_grad()
            timing_loss = timing.event_loss(race_tuple(train_races))
            mark = mark_logits(timing, head, fit_data, train_ids, original.config, mode=='joint')
            correct_loss = F.binary_cross_entropy_with_logits(mark, target, reduction='sum')
            penalty = timing.penalty()+.5*sum(v.square().sum() for k,v in head.items() if k!='intercept')
            loss = (timing_loss+correct_loss+penalty)/len(train_races['item'])
            if not torch.isfinite(loss):
                raise ValueError('Nonfinite objective')
            loss.backward()
            torch.nn.utils.clip_grad_norm_(list(timing.parameters())+list(head.parameters()), 10)
            optimizer.step()
            rows.append(dict(step=step, objective=float(loss.detach()), timing_nll=float(timing_loss.detach()),
                             correctness_nll=float(correct_loss.detach()), penalty=float(penalty.detach())))
            if step % 200 == 0:
                print(mode, fold, step, rows[-1]['objective'], flush=True)
        with torch.no_grad():
            pneg = mark_logits(timing, head, test_data, train_ids, original.config, False).sigmoid()[None]
            _, mean, sd = standardized_traits(timing, train_ids, train_ids, False)
            draws = {k:v.detach()[None] for k,v in timing.state_dict().items()}
            events, checks = predict_events(test_races, metadata, draws, pneg, test.index)
        artifact = dict(timing=detached_cpu(timing.state_dict()), coefficients=detached_cpu(head),
                        mean=mean.cpu(), sd=sd.cpu(), transforms=transforms, config=original.config)
        joblib.dump(artifact, out/'model.joblib', compress=3)
        replay = predict_saved(test.drop(columns=['y','neg']), joblib.load(out/'model.joblib'))
        np.testing.assert_allclose(replay, pneg[0].cpu().numpy(), atol=2e-6, rtol=2e-5)
        events['family'] = 'original_spline_'+mode
        events['fold'] = fold
        events['neg'] = events.event_id.map(test.neg)
        buzz = events.buzz.eq(1)
        events['joint_nll'] = events.race_nll
        prob = np.where(events.loc[buzz,'neg'].eq(1), events.loc[buzz,'predicted_neg'], 1-events.loc[buzz,'predicted_neg'])
        events.loc[buzz,'joint_nll'] -= np.log(np.clip(prob,1e-15,1))
        events.to_csv(out/'events.csv',index=False)
        pd.DataFrame(rows).to_csv(out/'losses.csv',index=False)
        checks.update(initial_saved_prediction_max_error=initial_error,
                      replay_max_error=float(np.max(np.abs(replay-pneg[0].cpu().numpy()))),
                      train_test_games_disjoint=True, original_training_games_match=True,
                      theta_change_norm=float((timing.theta.detach().cpu()-cp['outer']['theta']).norm()))
        (out/'checks.json').write_text(json.dumps(checks,indent=2))
        summary = dict(seconds=time.monotonic()-started, timing=summarize(events),
                       correctness=correctness_scores(events[buzz]),
                       initial_objective=rows[0]['objective'], final_objective=rows[-1]['objective'],
                       last_100_objective_slope=float(np.polyfit(np.arange(min(100,len(rows))),[r['objective'] for r in rows[-100:]],1)[0]))
        (out/'summary.json').write_text(json.dumps(summary,indent=2))
        (out/'complete.json').write_text(json.dumps({'seconds':summary['seconds']}))
        print(f'Complete {fold} {mode}: {summary}',flush=True)


def report(output):
    frames=[]
    for fold in range(5):
        for mode in ['blocked','joint']:
            frames.append(pd.read_csv(output/f'fold_{fold}/{mode}/events.csv'))
    pooled=[]
    folds=[]
    events=pd.concat(frames,ignore_index=True)
    assert not events.duplicated(['family','event_id']).any()
    for family,g in events.groupby('family'):
        pooled.append(dict(family=family,**summarize(g),**{'correctness_'+k:v for k,v in correctness_scores(g[g.buzz.eq(1)]).items()}))
        for fold,f in g.groupby('fold'):
            folds.append(dict(family=family,fold=fold,**summarize(f),**{'correctness_'+k:v for k,v in correctness_scores(f[f.buzz.eq(1)]).items()}))
    baseline=pd.read_csv('results/compirt/holdout/frozen-skills/pyro-cut-vi/comparison.csv')
    comparison=pd.concat([baseline,pd.DataFrame(pooled)],ignore_index=True)
    comparison.to_csv(output/'comparison.csv',index=False)
    pd.DataFrame(folds).to_csv(output/'fold_metrics.csv',index=False)
    left=events[events.family.eq('original_spline_joint')].set_index('event_id')
    intervals=[]
    refs=pd.concat([pd.read_csv(MAP_ROOT/f'timing_comparison/fold_{f}_events.csv') for f in range(5)])
    for family in ['original_spline_blocked','frozen_skills','saved_compirt']:
        right=(events if family=='original_spline_blocked' else refs)
        right=right[right.family.eq(family)].set_index('event_id')
        for metric in ['absolute_error','integrated_brier','joint_nll']:
            delta=pd.DataFrame({'game':left.game_id,'delta':left[metric]-right[metric]}).dropna()
            groups=delta.groupby('game').delta.agg(['sum','count'])
            sums,counts=groups['sum'].to_numpy(),groups['count'].to_numpy()
            rng=np.random.default_rng(42); samples=[]
            for _ in range(2000):
                ix=rng.integers(0,len(groups),len(groups)); samples.append(sums[ix].sum()/counts[ix].sum())
            lo,hi=np.quantile(samples,[.025,.975])
            intervals.append(dict(reference=family,metric=metric,delta=delta.delta.mean(),low=lo,high=hi))
    pd.DataFrame(intervals).to_csv(output/'game_bootstrap.csv',index=False)
    config=json.loads((output/'configuration.json').read_text())
    lines=['# Joint training of the original frozen spline model','',
           'Five existing whole-game holdouts: 46,640 race events and 45,995 first buzzes.',
           'Both new arms start from the saved original timing and correctness coefficients, verified against saved held-out probabilities before fitting.',
           f"Each arm gets {config['steps']} additional full-batch Adam steps at lr {config['lr']}. This is warm-started MAP fine-tuning, not Pyro VI or training from scratch.",
           'The joint arm lets correctness update theta and speed. The blocked arm detaches those traits from correctness, while timing continues to learn from timing observations. Correctness follows the moving detached traits; this is a matched no-feedback control, not a permanently frozen checkpoint.',
           'The original timing penalty and all correctness L2 penalties are retained; the global correctness intercept stays unpenalized. The objective sums race and correctness log likelihoods with coefficient one, then adds penalties. Dividing the entire objective by training race count only rescales optimization.',
           'Training-buzz-row mean and standard deviation (floor 0.1) are recomputed from current traits at each step; the joint arm differentiates through this training-only standardization. Final transforms are saved for replay.', '',
           '| Model | Timing MAE | Correctness loss | Correctness accuracy | Joint loss |',
           '| --- | ---: | ---: | ---: | ---: |']
    for r in comparison.itertuples():
        lines.append(f'| {r.family} | {r.timing_mae:.5f} | {r.correctness_log_loss:.5f} | {r.correctness_accuracy:.2%} | {r.joint_nll:.5f} |')
    lines += ['', 'Lower losses are better. Accuracy uses threshold 0.5. No held-out outcomes select settings or stopping.',
              'Use joint versus blocked to assess correctness feedback under this initialization and budget. Comparison with the original saved fit also changes optimization budget. These reused development folds do not establish future-season or unseen-item performance.',
              'Game-bootstrap intervals (2,000 resamples) condition on fixed fits and exclude refit uncertainty and cross-game question dependence. Saved DD predates the likelihood repair; replay is normalized but it is not a repaired refit.',
              'Every correctness prediction replays from a saved artifact on CPU with outcomes erased. The full timing PMFs are checked for normalization.', '',
              'Reproduce: `.venv/bin/python -m frozen_skills.joint`.', '']
    (output/'REPORT.md').write_text('\n'.join(lines))
    print(comparison[['family','timing_mae','correctness_log_loss','correctness_accuracy','joint_nll']].to_string(index=False))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=OUTPUT)
    parser.add_argument('--folds',type=int,nargs='+',default=list(range(5)))
    parser.add_argument('--steps',type=int,default=1000)
    parser.add_argument('--lr',type=float,default=.005)
    parser.add_argument('--device',default='cuda')
    args=parser.parse_args()
    if args.steps<2 or args.lr<=0 or not set(args.folds)<=set(range(5)):
        parser.error('Require steps >= 2, positive lr, folds 0..4')
    torch.set_num_threads(1)
    args.output.mkdir(parents=True,exist_ok=True)
    config=dict(steps=args.steps,lr=args.lr,initialization='original saved MAP',gradient_control='detach theta and speed from correctness')
    path=args.output/'configuration.json'
    if path.exists() and json.loads(path.read_text())!=config:
        raise ValueError('Different configuration; use a fresh output directory')
    path.write_text(json.dumps(config,indent=2))
    for fold in args.folds:
        fit_fold(fold,args)
    if all((args.output/f'fold_{f}/{m}/complete.json').exists() for f in range(5) for m in ['joint','blocked']):
        report(args.output)


if __name__=='__main__':
    main()
