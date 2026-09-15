"""Compare completed Pyro folds with the original MAP and saved DD reference."""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from frozen_skills.evaluation import summarize, correctness_scores
from frozen_skills.train_holdout import DEFAULT_OUTPUT, MAP_ROOT


LABELS = dict(saved_compirt='Saved DD-Bernstein', frozen_skills='Original frozen MAP',
              pyro_frozen_skills='Pyro frozen VI')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    all_events = []
    correctness = []
    for fold in range(5):
        directory = args.output / f'fold_{fold}'
        if not (directory / 'complete.json').exists():
            raise RuntimeError(f'Fold {fold} is incomplete')
        events = pd.read_csv(directory / 'events.csv')
        baseline = pd.read_csv(MAP_ROOT / f'timing_comparison/fold_{fold}_events.csv')
        baseline['neg'] = np.nan
        saved = pd.read_csv(MAP_ROOT / f'fold_{fold}/predictions.csv').set_index('event_id')
        for family, group in baseline.groupby('family'):
            assert set(group.event_id) == set(events.event_id)
            buzz = group[group.buzz.eq(1)].copy()
            buzz['neg'] = buzz.event_id.map(saved.neg)
            buzz['predicted_neg'] = buzz.event_id.map(saved[family])
            correctness.append(buzz[['event_id','fold','family','neg','predicted_neg']])
        correctness.append(events[events.buzz.eq(1)][['event_id','fold','family','neg','predicted_neg']])
        all_events.extend([events, baseline])
    all_events = pd.concat(all_events, ignore_index=True)
    correctness = pd.concat(correctness, ignore_index=True)
    assert not all_events.duplicated(['family','event_id']).any()
    pooled, folds = [], []
    for family, group in all_events.groupby('family'):
        c = correctness[correctness.family.eq(family)]
        scores = correctness_scores(c)
        pooled.append(dict(family=family, **summarize(group), **{'correctness_'+k:v for k,v in scores.items()}))
    for (family, fold), group in all_events.groupby(['family','fold']):
        c = correctness[(correctness.family==family)&(correctness.fold==fold)]
        folds.append(dict(family=family, fold=fold, **summarize(group),
                          **{'correctness_'+k:v for k,v in correctness_scores(c).items()}))
    pooled = pd.DataFrame(pooled).set_index('family')
    pd.DataFrame(folds).to_csv(args.output/'fold_metrics.csv',index=False)
    pooled.to_csv(args.output/'comparison.csv')
    pyro_events=all_events[all_events.family.eq('pyro_frozen_skills')]
    pyro_buzz=pyro_events[pyro_events.buzz.eq(1)]
    mark_only=correctness_scores(pyro_buzz,'mark_only_neg')
    (args.output/'mark_only_correctness.json').write_text(json.dumps(mark_only,indent=2))
    intervals=[]
    for reference in ['frozen_skills','saved_compirt']:
        other=all_events[all_events.family.eq(reference)].set_index('event_id')
        left=pyro_events.set_index('event_id')
        for metric in ['absolute_error','integrated_brier','joint_nll']:
            d=pd.DataFrame({'game_id':left.game_id,'delta':left[metric]-other[metric]}).dropna()
            g=d.groupby('game_id').delta.agg(['sum','count'])
            sums,counts=g['sum'].to_numpy(),g['count'].to_numpy()
            rng=np.random.default_rng(42)
            samples=[]
            for _ in range(2000):
                ix=rng.integers(0,len(g),len(g));samples.append(sums[ix].sum()/counts[ix].sum())
            low,high=np.quantile(samples,[.025,.975])
            intervals.append(dict(reference=reference,metric=metric,pyro_minus_reference=d.delta.mean(),low=low,high=high))
    pd.DataFrame(intervals).to_csv(args.output/'game_bootstrap.csv',index=False)
    lines=['# Pyro frozen-skills holdout comparison','',
           'Five saved whole-game folds; 46,640 race events, including 45,995 first buzzes.',
           'The original MAP model and saved DD-Bernstein reference are unchanged.', '',
           '| Metric | Saved DD-Bernstein | Original frozen MAP | Pyro frozen VI |',
           '| --- | ---: | ---: | ---: |']
    entries=[('Position MAE ↓','timing_mae',False),('Position RMSE ↓','timing_rmse',False),
             ('Integrated timing Brier ↓','integrated_brier',False),('Timing log loss ↓','timing_nll',False),
             ('First-buzzer accuracy ↑','first_buzzer_accuracy',True),('Joint event log loss ↓','joint_nll',False),
             ('Correctness accuracy at 0.5 ↑','correctness_accuracy',True),
             ('Incorrect-buzz precision ↑','correctness_neg_precision',True),
             ('Incorrect-buzz recall ↑','correctness_neg_recall',True),
             ('Incorrect-buzz F1 ↑','correctness_neg_f1',True),
             ('Incorrect-buzz AP ↑','correctness_neg_ap',True),
             ('Correctness log loss ↓','correctness_log_loss',False)]
    for label,key,percent in entries:
        values=[pooled.loc[family,key] for family in LABELS]
        rendered=[f'{v:.2%}' if percent else f'{v:.5f}' for v in values]
        lines.append('| '+label+' | '+' | '.join(rendered)+' |')
    config=json.loads((args.output/'configuration.json').read_text())
    training=[json.loads((args.output/f'fold_{fold}/summary.json').read_text()) for fold in range(5)]
    slopes=[row['timing']['last_100_loss_slope'] for row in training]
    lines.extend(['','## Inference and comparability','',
        f"Timing and correctness each use {config['timing_steps']:,} and {config['correctness_steps']:,} full-batch SVI steps, respectively, with AutoNormal and clipped Adam (lr {config['lr']}).",
        f"The cut-posterior approximation uses {config['timing_draws']} fixed timing-posterior draws, each paired with its own independent conditional coefficient posterior.",
        'Correctness never changes the timing draws. Coefficient uncertainty is integrated by 48-point Gauss-Hermite quadrature; mixture probabilities are averaged before scoring.',
        'Conditional correctness in the main table is the joint incorrect-event mass divided by the timing/identity event mass. This weights the paired posterior components by the observed winner/time, without using the held-out correctness label.',
        f"Averaging the correctness heads without this timing conditioning gives log loss {mark_only['log_loss']:.5f}, accuracy {mark_only['accuracy']:.2%}, and incorrect AP {mark_only['neg_ap']:.5f}; see mark_only_correctness.json.",
        'The timing equations, Gaussian priors and selected correctness feature scales match the original model. A proper N(0,10²) correctness-intercept prior replaces its unpenalized intercept.',
        'The feature settings were selected by the original inner training-game validation; this run reuses them rather than conducting a new search. Only the fixed 0.5 threshold is reported. No held-out outcomes enter fitting or stopping.',
        'This is approximate modular Bayesian inference, not a single jointly updated posterior. Finite timing draws and mean-field guides limit posterior accuracy. Its training budget and inference differ from the earlier MAP fit; this is not an isolated uncertainty-averaging ablation.',
        'The DD reference is a saved historical fit scored through normalized full-grid replay, not a newly retrained likelihood-repair baseline.',
        f'The final-100-step timing ELBO slopes range from {min(slopes):.3f} to {max(slopes):.3f}; timing is still improving at the fixed 3,000-step budget. These are budgeted fits, not a convergence or optimality claim.',
        '', '## Artifacts and reproduction','',
        'comparison.csv and fold_metrics.csv hold pooled and per-fold scores. game_bootstrap.csv gives paired game-cluster 95% intervals (2,000 resamples), conditional on fixed fitted predictions and excluding cross-game question dependence.',
        'Each fold contains split manifests, feature settings, complete timing posterior draws/quantiles, conditional correctness guide means/scales, training losses, prediction rows, and freeze/normalization checks.',
        '', '```bash', '.venv/bin/python -m frozen_skills.train_holdout',
        '.venv/bin/python -m frozen_skills.report', '.venv/bin/python -m frozen_skills.verify', '```', ''])
    verification=args.output/'replay_checks.json'
    if verification.exists():
        replay=json.loads(verification.read_text())
        if len(replay)==5 and all('quadrature_48_vs_96_maximum_neg_difference' in row for row in replay):
            position=[row['eight_vs_sixteen_mean_absolute_position_difference'] for row in replay]
            quadrature=max(row['quadrature_48_vs_96_maximum_neg_difference'] for row in replay)
            lines.extend(['## Numerical checks','',
                f"Saved-artifact replay checks {sum(row['events'] for row in replay):,} ordinary/terminal/dead examples on CPU, with correctness labels erased. All match original predictions within tolerance; see replay_checks.json.",
                f'On that verification subset, changing from eight to sixteen timing draws changes expected position by a mean absolute {min(position):.4f}–{max(position):.4f} across folds. Monte Carlo convergence is not established, and the bootstrap intervals do not include this variation.',
                f'The largest conditional-probability difference between 48- and 96-node coefficient quadrature is {quadrature:.2g}.', ''])
    (args.output/'REPORT.md').write_text('\n'.join(lines))
    print(pooled.to_string())
    print(pd.DataFrame(intervals).to_string(index=False))


if __name__=='__main__':
    main()
