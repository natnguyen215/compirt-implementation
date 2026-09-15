"""One Bayesian Bernstein correctness model conditional on frozen MAP traits.

Run the matched five-game-fold experiment with ``python -m frozen_skills.simplified``.
Timing predictions are reused exactly; this tests correctness simplification,
not a new timing fit. Predictions use posterior medians, without a mixture.
"""
import argparse
import json
from pathlib import Path
import time

import numpy as np
import pandas as pd
import pyro
import pyro.distributions as dist
import torch

from analysis.correctness.paper_readiness.first_buzz_features import ROOT
from frozen_skills.data import first_buzzes, tensor
from frozen_skills.evaluation import summarize, correctness_scores
from frozen_skills.train_holdout import MAP_ROOT, fingerprint, detached_cpu
from hazard_double_difficulty.bernstein.pyramidal_model import bernstein_basis, control_values
from utils.training import fit_svi, convergence_summary, require_device

OUTPUT = Path('results/compirt/holdout/frozen-skills/simplified-bernstein-map-timing')
FAMILY = 'simplified_frozen_skills'


def design(frame, checkpoint, device='cpu'):
    """Only identities and positions enter prediction; outcomes are not read."""
    state = checkpoint['outer']
    traits = torch.cat([state['theta'], state['speed'][:, None]], -1).to(device).detach()
    player = tensor([checkpoint['player_map'][p] for p in frame.player_id], device, True)
    return dict(player=player,
                item=tensor([checkpoint['item_map'][j] for j in frame.tossup_id], device, True),
                skills=traits[player],
                basis=bernstein_basis(tensor(frame.t_star / frame.T_j, device), 3),
                terminal=tensor(frame.t_star.eq(frame.T_j), device),
                n_players=len(checkpoint['player_map']), n_items=len(checkpoint['item_map']))


def logits(data, parameters):
    curve = control_values(parameters['start'], parameters['drop'], parameters['shares'])
    return (parameters['ability'][data['player']]
            + (parameters['weight'][data['item']] * data['skills']).sum(-1)
            - (curve[data['item']] * data['basis']).sum(-1)
            + parameters['terminal'] * data['terminal'])


def model(data, correct):
    if data['skills'].requires_grad:
        raise ValueError('Timing traits must be detached')
    ref = data['skills']
    def normal(name, shape, sd=1.):
        return pyro.sample(name, dist.Normal(ref.new_zeros(shape), sd).to_event(len(shape)))
    j = data['n_items']
    parameters = dict(ability=normal('ability', (data['n_players'],)),
                      weight=normal('weight', (j, 4)), start=normal('start', (j,)),
                      drop=pyro.sample('drop', dist.LogNormal(ref.new_zeros(j), .5).to_event(1)),
                      shares=pyro.sample('shares', dist.Dirichlet(ref.new_full((j, 3), 2.)).to_event(1)),
                      terminal=normal('terminal', (), 2.))
    pyro.sample('correct', dist.Bernoulli(logits=logits(data, parameters)).to_event(1), obs=correct)


def predict(frame, artifact, device='cpu'):
    parameters = {k: v.to(device) for k, v in artifact['median'].items()}
    with torch.no_grad():
        return (-logits(design(frame, artifact['timing'], device), parameters)).sigmoid().cpu().numpy()


def fit_fold(fold, args):
    directory = args.output / f'fold_{fold}'
    if (directory / 'complete.json').exists():
        return
    directory.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    train = pd.read_csv(ROOT / f'fold_{fold}/train/pyramidal/tossup_predictions.csv')
    test = pd.read_csv(ROOT / f'fold_{fold}/holdout/pyramidal/tossup_predictions.csv')
    source = MAP_ROOT / f'fold_{fold}'
    splits = pd.read_csv(source / 'inner_split.csv')
    assert set(train.game_id) == set(splits.game_id)
    assert not set(train.game_id) & set(test.game_id)
    checkpoint = torch.load(source / 'timing_skills.pt', map_location='cpu', weights_only=False)
    frozen_hash = fingerprint(checkpoint['outer'])
    train_buzz, test_buzz = first_buzzes(train), first_buzzes(test)
    saved = pd.read_csv(source / 'predictions.csv').set_index('event_id')
    assert set(saved.index) == set(test_buzz.index)
    np.testing.assert_array_equal(saved.loc[test_buzz.index, 'neg'], test_buzz.neg)
    data = design(train_buzz, checkpoint, args.device)
    pyro.set_rng_seed(args.seed + fold)
    print(f'Fold {fold}: fitting one correctness posterior on {len(train_buzz)} buzzes', flush=True)
    median, _, losses = fit_svi(model, model_kwargs=dict(data=data, correct=tensor(train_buzz.y, args.device)),
                               n_steps=args.steps, lr=args.lr, posterior_output_dir=directory)
    artifact = dict(median=detached_cpu(median), timing=checkpoint,
                    param_store=pyro.get_param_store().get_state())
    torch.save(artifact, directory / 'model.pt')
    pd.DataFrame({'negative_elbo': losses}).to_csv(directory / 'losses.csv', index=False)
    pneg = predict(test_buzz, artifact, args.device)
    # Independently reload on CPU with outcomes erased to verify usable saved prediction.
    reloaded = torch.load(directory / 'model.pt', map_location='cpu', weights_only=False)
    replay = predict(test_buzz.drop(columns=['y', 'neg']), reloaded)
    np.testing.assert_allclose(replay, pneg, atol=2e-6, rtol=2e-5)
    assert fingerprint(checkpoint['outer']) == frozen_hash
    baseline = pd.read_csv(MAP_ROOT / f'timing_comparison/fold_{fold}_events.csv')
    events = baseline[baseline.family.eq('frozen_skills')].copy()
    assert set(events.event_id) == set(test.event_id)
    events['family'] = FAMILY
    events['neg'] = events.event_id.map(test_buzz.neg)
    events['predicted_neg'] = events.event_id.map(pd.Series(pneg, index=test_buzz.index))
    events['joint_nll'] = events.race_nll
    buzz = events.buzz.eq(1)
    probability = np.where(events.loc[buzz, 'neg'].eq(1), events.loc[buzz, 'predicted_neg'],
                           1-events.loc[buzz, 'predicted_neg'])
    events.loc[buzz, 'joint_nll'] -= np.log(np.clip(probability, 1e-15, 1))
    events.to_csv(directory / 'events.csv', index=False)
    checks = dict(train_test_games_disjoint=True, original_training_games_match=True,
                  correctness_events_match=True, timing_unchanged=True, timing_sha256=frozen_hash,
                  cpu_replay_max_error=float(np.max(np.abs(replay-pneg))), replay_events=len(pneg))
    (directory / 'checks.json').write_text(json.dumps(checks, indent=2))
    splits.to_csv(directory / 'training_game_split.csv', index=False)
    pd.DataFrame({'game_id': sorted(test.game_id.unique())}).to_csv(directory / 'holdout_games.csv', index=False)
    summary = dict(correctness=correctness_scores(events[buzz]), timing=summarize(events),
                   convergence=convergence_summary(losses), seconds=time.monotonic()-started)
    (directory / 'summary.json').write_text(json.dumps(summary, indent=2))
    (directory / 'complete.json').write_text(json.dumps({'seconds': summary['seconds']}))
    print(f'Fold {fold} complete: {summary}', flush=True)


def report(output):
    config = json.loads((output / 'configuration.json').read_text())
    training = [json.loads((output / f'fold_{f}/summary.json').read_text()) for f in range(5)]
    frames = [pd.read_csv(output / f'fold_{f}/events.csv') for f in range(5)]
    all_events = pd.concat(frames, ignore_index=True)
    assert not all_events.event_id.duplicated().any()
    scores = dict(family=FAMILY, **summarize(all_events),
                  **{'correctness_'+k:v for k,v in correctness_scores(all_events[all_events.buzz.eq(1)]).items()})
    old = pd.read_csv(Path('results/compirt/holdout/frozen-skills/pyro-cut-vi/comparison.csv'))
    comparison = pd.concat([old, pd.DataFrame([scores])], ignore_index=True)
    comparison.to_csv(output / 'comparison.csv', index=False)
    pd.DataFrame([dict(fold=f, **summarize(e), **{'correctness_'+k:v for k,v in
                 correctness_scores(e[e.buzz.eq(1)]).items()}) for f,e in enumerate(frames)]).to_csv(output / 'fold_metrics.csv', index=False)
    intervals = []
    for family in ['frozen_skills', 'saved_compirt']:
        refs = pd.concat([pd.read_csv(MAP_ROOT / f'timing_comparison/fold_{f}_events.csv') for f in range(5)])
        ref = refs[refs.family.eq(family)].set_index('event_id')
        left = all_events.set_index('event_id')
        delta = pd.DataFrame({'game': left.game_id, 'delta': left.joint_nll-ref.joint_nll})
        assert delta.delta.notna().all()
        groups = delta.groupby('game').delta.agg(['sum', 'count'])
        rng = np.random.default_rng(42)
        sums, counts = groups['sum'].to_numpy(), groups['count'].to_numpy()
        samples = []
        for _ in range(2000):
            ix = rng.integers(0, len(groups), len(groups))
            samples.append(sums[ix].sum()/counts[ix].sum())
        low, high = np.quantile(samples, [.025, .975])
        intervals.append(dict(reference=family, metric='joint_nll', delta=delta.delta.mean(), low=low, high=high))
    pd.DataFrame(intervals).to_csv(output / 'game_bootstrap.csv', index=False)
    lines = ['# Simplified frozen-skills matched holdouts', '',
             'One monotone cubic Bernstein correctness model, fitted with Pyro SVI conditional on the original MAP timing traits.',
             'The five original whole-game partitions and timing checkpoints are fixed. All 46,640 race events and 45,995 buzzes are scored.', '',
             '| Model | Timing MAE | Correctness log loss | Correctness accuracy | Joint log loss |',
             '| --- | ---: | ---: | ---: | ---: |']
    for row in comparison.itertuples():
        lines.append(f'| {row.family} | {row.timing_mae:.5f} | {row.correctness_log_loss:.5f} | {row.correctness_accuracy:.2%} | {row.joint_nll:.5f} |')
    lines += ['', 'Lower losses are better. Accuracy uses a fixed 0.5 threshold.', '',
              'Both the curve/priors and correctness fitting method differ from original frozen MAP; this does not isolate Bernstein versus spline alone.',
              f"One AutoNormal posterior is fitted for {config['steps']:,} steps at lr {config['lr']}, seed {config['seed']} + fold. Prediction uses posterior medians, without quadrature or timing uncertainty propagation.",
              'This is a fixed-budget development-fold comparison, not untouched-test evidence or a convergence claim. The saved DD fit predates the likelihood repair.',
              'Timing columns are reused exactly from the validated original MAP replay; they are not evidence for a new Pyro timing fit.',
              'Every held-out correctness prediction is reloaded and replayed on CPU with outcomes removed. Timing hashes and game-disjointness checks are saved per fold.',
              'game_bootstrap.csv gives paired game-cluster 95% intervals for joint-loss differences, conditional on fitted parameters; it excludes refit uncertainty and cross-game question dependence.', '',
              'Reproduce: `.venv/bin/python -m frozen_skills.simplified`.', '']
    lines += ['## Training diagnostics', '', '| Fold | Final-100-step ELBO-loss slope | Fit and replay seconds |',
              '| --- | ---: | ---: |']
    for fold, row in enumerate(training):
        lines.append(f"| {fold} | {row['convergence']['last_100_loss_slope']:.4f} | {row['seconds']:.1f} |")
    lines += ['', 'A negative slope means the estimated loss is still declining at the budget limit; it does not establish convergence.', '']
    (output / 'REPORT.md').write_text('\n'.join(lines))
    print(comparison[['family', 'timing_mae', 'correctness_log_loss', 'correctness_accuracy', 'joint_nll']].to_string(index=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--folds', nargs='+', type=int, default=list(range(5)))
    parser.add_argument('--steps', type=int, default=3000)
    parser.add_argument('--lr', type=float, default=.005)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--device', default='cuda')
    args = parser.parse_args()
    if args.steps < 1 or args.lr <= 0 or not set(args.folds) <= set(range(5)):
        parser.error('Require positive steps/lr and folds from 0 through 4')
    require_device(args.device)
    torch.set_num_threads(1)
    args.output.mkdir(parents=True, exist_ok=True)
    config = dict(steps=args.steps, lr=args.lr, seed=args.seed, degree=3, timing='original MAP', prediction='posterior medians')
    path = args.output / 'configuration.json'
    if path.exists() and json.loads(path.read_text()) != config:
        raise ValueError('Configuration differs; use a fresh output directory')
    path.write_text(json.dumps(config, indent=2))
    for fold in args.folds:
        fit_fold(fold, args)
    if all((args.output/f'fold_{f}/complete.json').exists() for f in range(5)):
        report(args.output)


if __name__ == '__main__':
    main()
