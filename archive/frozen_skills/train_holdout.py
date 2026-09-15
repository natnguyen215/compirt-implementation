"""Run five-fold Pyro frozen-skills SVI using the saved reference game partitions.

The old fold-specific correctness feature settings are held fixed, not searched
again. Results remain a development-fold comparison. Outputs go to a new run
folder and never overwrite original MAP or DD-Bernstein fits.
"""

import argparse
import hashlib
import json
from pathlib import Path
import time

import joblib
import numpy as np
import pandas as pd
import pyro
import torch

from analysis.correctness.paper_readiness.first_buzz_features import ROOT
from frozen_skills.data import races, first_buzzes, correctness_design
from frozen_skills.evaluation import predict_events, summarize, correctness_scores
from frozen_skills.pyramidal_model import timing_model, correctness_model, correctness_predictive
from utils.training import fit_svi, convergence_summary, require_device


MAP_ROOT = Path('results/compirt/holdout/common/tossup-accuracy-study')
DEFAULT_OUTPUT = Path('results/compirt/holdout/frozen-skills/pyro-cut-vi')


def detached_cpu(values):
    return {k: v.detach().cpu().clone() for k, v in values.items()}


def fingerprint(values):
    digest = hashlib.sha256()
    for key, value in sorted(values.items()):
        digest.update(key.encode()); digest.update(value.detach().cpu().numpy().tobytes())
    return digest.hexdigest()


def fit_timing(data, args, directory, seed):
    pyro.set_rng_seed(seed)
    kwargs = dict(data=data, dimensions=3)
    medians, guide, losses = fit_svi(
        timing_model, model_kwargs=kwargs, n_steps=args.timing_steps, lr=args.lr,
        posterior_output_dir=directory, posterior_draws=args.timing_draws, posterior_seed=seed + 1000)
    # Use the EXACT saved aligned draws, avoiding changes in RNG after export.
    draws = {site: torch.as_tensor(np.load(directory / f'posterior_draws/{site}.npy'), device=args.device)
             for site in medians}
    torch.save(dict(median=detached_cpu(medians), param_store=pyro.get_param_store().get_state()),
               directory / 'guide.pt')
    pd.DataFrame({'negative_elbo': losses}).to_csv(directory / 'losses.csv', index=False)
    return draws, convergence_summary(losses)


def fit_correctness(data, config, args, directory, seed):
    pyro.set_rng_seed(seed)
    kwargs = dict(data=data, config=config, intercept_sd=args.intercept_sd)
    _, guide, losses = fit_svi(correctness_model, model_kwargs=kwargs,
                               n_steps=args.correctness_steps, lr=args.lr)
    with torch.no_grad():
        quantiles = guide.quantiles([.5, .8413447460685429], **kwargs)
        locations = {k: v[0].detach().clone() for k, v in quantiles.items()}
        scales = {k: (v[1] - v[0]).detach().clone() for k, v in quantiles.items()}
    assert all(torch.isfinite(v).all() and (v > 0).all() for v in scales.values())
    torch.save(dict(locations=detached_cpu(locations), scales=detached_cpu(scales),
                    param_store=pyro.get_param_store().get_state()), directory / 'guide.pt')
    pd.DataFrame({'negative_elbo': losses}).to_csv(directory / 'losses.csv', index=False)
    return locations, scales, convergence_summary(losses)


def fit_fold(fold, args):
    directory = args.output / f'fold_{fold}'
    complete = directory / 'complete.json'
    if complete.exists():
        print(f'Skipping completed fold {fold}', flush=True)
        return
    directory.mkdir(parents=True, exist_ok=True)
    timing_dir, correctness_dir = directory / 'timing', directory / 'correctness'
    timing_dir.mkdir(exist_ok=True); correctness_dir.mkdir(exist_ok=True)
    started = time.monotonic()
    reference = ROOT / f'fold_{fold}'
    train_rows = pd.read_csv(reference / 'train/pyramidal/tossup_predictions.csv')
    test_rows = pd.read_csv(reference / 'holdout/pyramidal/tossup_predictions.csv')
    original = MAP_ROOT / f'fold_{fold}'
    partitions = pd.read_csv(original / 'inner_split.csv')
    assert set(train_rows.game_id) == set(partitions.game_id)
    assert not set(train_rows.game_id) & set(test_rows.game_id)
    checkpoint = torch.load(original / 'timing_skills.pt', map_location='cpu', weights_only=False)
    player_map, item_map = checkpoint['player_map'], checkpoint['item_map']
    config = json.loads((original / 'selection.json').read_text())['frozen_skills']['config']
    if config.get('curve') != 'spline' or config.get('clue'):
        raise ValueError('This matched implementation requires the selected spline/no-clue design')
    partitions.to_csv(directory / 'original_inner_split.csv', index=False)
    pd.DataFrame({'game_id': sorted(test_rows.game_id.unique())}).to_csv(directory / 'holdout_games.csv', index=False)
    (directory / 'feature_config.json').write_text(json.dumps(config, indent=2))
    train, _ = races(train_rows, player_map, item_map, args.device)
    test, metadata = races(test_rows, player_map, item_map, args.device)
    print(f'FOLD {fold}: timing fit, {len(train["item"])} races', flush=True)
    draws, timing_info = fit_timing(train, args, timing_dir, args.seed + fold)
    frozen_hash = fingerprint(draws)
    train_buzz, test_buzz = first_buzzes(train_rows), first_buzzes(test_rows)
    saved = pd.read_csv(original / 'predictions.csv').set_index('event_id')
    assert set(saved.index) == set(test_buzz.index)
    np.testing.assert_array_equal(saved.loc[test_buzz.index, 'neg'], test_buzz.neg)
    fit_design, test_design, transforms = correctness_design(
        train_buzz, test_buzz, draws, player_map, item_map, args.device)
    joblib.dump(transforms, correctness_dir / 'transforms.joblib', compress=3)
    print(f'FOLD {fold}: {args.timing_draws} conditional correctness posteriors', flush=True)
    locations, scales, correctness_info = fit_correctness(
        fit_design, config, args, correctness_dir, args.seed + 100 + fold)
    assert fingerprint(draws) == frozen_hash
    with torch.no_grad():
        mark = correctness_predictive(test_design, locations, scales, config)
        mark48 = correctness_predictive(test_design, locations, scales, config, quadrature=48)
        quadrature_error = float((mark - mark48).abs().max())
    # Use the more accurate calculation; this is numerical integration, not tuning.
    mark = mark48
    np.save(correctness_dir / 'conditional_mark_probabilities.npy', mark.cpu().numpy())
    events, checks = predict_events(test, metadata, draws, mark, test_buzz.index)
    events['family'] = 'pyro_frozen_skills'; events['fold'] = fold
    events['neg'] = events.event_id.map(test_buzz.neg)
    events['joint_nll'] = events.race_nll
    buzz_mask = events.buzz.eq(1)
    probability = np.where(events.loc[buzz_mask, 'neg'].eq(1),
                            events.loc[buzz_mask, 'neg_joint'], events.loc[buzz_mask, 'correct_joint'])
    events.loc[buzz_mask, 'joint_nll'] = -np.log(np.clip(probability, 1e-300, 1))
    events.to_csv(directory / 'events.csv', index=False)
    predictions = events[buzz_mask][['event_id', 'game_id', 'tossup_id', 'neg', 'predicted_neg', 'mark_only_neg']]
    predictions.to_csv(directory / 'predictions.csv', index=False)
    scores = dict(timing=summarize(events), correctness=correctness_scores(predictions),
                  mark_only_correctness=correctness_scores(predictions, 'mark_only_neg'))
    (directory / 'metrics.json').write_text(json.dumps(scores, indent=2))
    checks.update(frozen_timing_sha256=frozen_hash, timing_unchanged_after_correctness=True,
                  train_test_games_disjoint=True, original_training_games_match=True,
                  correctness_events_match=True, quadrature_24_vs_48_max_error=quadrature_error)
    (directory / 'checks.json').write_text(json.dumps(checks, indent=2))
    summary = dict(model='pyro-frozen-skills', inference='AutoNormal SVI; finite-mixture cut posterior',
                   timing=timing_info, correctness=correctness_info, seconds=time.monotonic() - started,
                   split=f'game-holdout:year_2024:test:5:{fold}:42', frozen_predict=True,
                   seed=args.seed + fold, timing_draws=args.timing_draws,
                   intercept_prior_sd=args.intercept_sd, timing_steps=args.timing_steps,
                   correctness_steps=args.correctness_steps, lr=args.lr,
                   threshold=.5, hyperparameter_selection='reuse original inner-selected feature settings',
                   training_races=len(train['item']), heldout_races=len(test['item']),
                   players=len(player_map), items=len(item_map), feature_config=config)
    (directory / 'summary.json').write_text(json.dumps(summary, indent=2))
    complete.write_text(json.dumps(dict(seconds=summary['seconds']), indent=2))
    print(f'FOLD {fold} COMPLETE: {scores}', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--folds', nargs='+', type=int, default=list(range(5)))
    parser.add_argument('--timing-steps', type=int, default=3000)
    parser.add_argument('--correctness-steps', type=int, default=3000)
    parser.add_argument('--timing-draws', type=int, default=16)
    parser.add_argument('--lr', type=float, default=.005)
    parser.add_argument('--intercept-sd', type=float, default=10.)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--device', default='cuda')
    args = parser.parse_args()
    if min(args.timing_steps, args.correctness_steps, args.timing_draws) < 1:
        parser.error('steps and timing draws must be positive')
    if not set(args.folds) <= set(range(5)) or len(set(args.folds)) != len(args.folds):
        parser.error('folds must be unique values from 0 through 4')
    require_device(args.device)
    torch.set_num_threads(1)
    args.output.mkdir(parents=True, exist_ok=True)
    configuration = {k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items() if k != 'folds'}
    path = args.output / 'configuration.json'
    if path.exists() and json.loads(path.read_text()) != configuration:
        raise ValueError('Output directory has a different configuration; use a fresh directory')
    path.write_text(json.dumps(configuration, indent=2))
    for fold in args.folds:
        fit_fold(fold, args)


if __name__ == '__main__':
    main()
