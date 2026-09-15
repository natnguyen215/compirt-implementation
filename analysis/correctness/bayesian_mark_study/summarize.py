"""Paired development-panel comparisons, including honest transferred policies."""
import json
import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, brier_score_loss, log_loss
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve

from analysis.correctness.bayesian_mark_study.run import OUTPUT, PREVIOUS, FAMILIES
from analysis.correctness.paper_readiness.first_buzz_features import metrics


def bootstrap_delta(y, p, ref, games, repetitions=1000):
    """Paired whole-game bootstrap; conditional on already fitted predictions.

    Sort once per model. Tied probabilities are evaluated at tie-group ends,
    matching sklearn average_precision_score with integer sample weights.
    """
    _, group = np.unique(games, return_inverse=True)
    n_groups = group.max()+1
    def prep(prob):
        order = np.argsort(-prob, kind='stable')
        ends = np.r_[np.flatnonzero(np.diff(prob[order]) != 0), len(y)-1]
        return order, ends
    def ap(weights, order, ends):
        pos = weights[order]*y[order]
        tp = np.cumsum(pos)[ends]
        count = np.cumsum(weights[order])[ends]
        return float(np.sum(np.diff(np.r_[0, tp])*tp/np.maximum(count, 1))/max(tp[-1], 1))
    a, b = prep(p), prep(ref)
    losses = -(y*np.log(p.clip(1e-12, 1))+(1-y)*np.log((1-p).clip(1e-12, 1)))
    other = -(y*np.log(ref.clip(1e-12, 1))+(1-y)*np.log((1-ref).clip(1e-12, 1)))
    rng = np.random.default_rng(20260909); values = []
    for _ in range(repetitions):
        weight = rng.multinomial(n_groups, np.full(n_groups, 1/n_groups))[group]
        values.append([ap(weight, *a)-ap(weight, *b), np.average(losses-other, weights=weight)])
    interval = np.quantile(values, [.025, .975], axis=0)
    return {'ap_delta': float(average_precision_score(y, p)-average_precision_score(y, ref)),
            'ap_lower': float(interval[0, 0]), 'ap_upper': float(interval[1, 0]),
            'log_loss_delta': float(log_loss(y, p)-log_loss(y, ref)),
            'log_loss_lower': float(interval[0, 1]), 'log_loss_upper': float(interval[1, 1])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--skip-bootstrap', action='store_true')
    args = parser.parse_args()
    families = list(FAMILIES)+['predictive_mixture']
    previous_names = ['saved_compirt', 'regularized', 'frozen_skills']
    has_boosting = all((PREVIOUS/f'fold_{k}/boosting/complete.json').exists() for k in range(5))
    if has_boosting:
        previous_names += ['boosting', 'boosting_ensemble']
    frames = {name: [] for name in families+previous_names+['selected_new', 'selected_with_previous']}
    chosen = []; fold_metrics = []
    for fold in range(5):
        directory = OUTPUT/f'fold_{fold}'
        old = pd.read_csv(PREVIOUS/f'fold_{fold}/predictions.csv')
        old_selection = json.loads((PREVIOUS/f'fold_{fold}/selection.json').read_text())
        if has_boosting:
            boost = pd.read_csv(PREVIOUS/f'fold_{fold}/boosting/predictions.csv')
            assert np.array_equal(old.event_id, boost.event_id)
            for name in ['boosting', 'boosting_ensemble']:
                old[name] = boost[name]
            old_selection.update(json.loads((PREVIOUS/f'fold_{fold}/boosting/selection.json').read_text()))
        scores = {}; current = {}
        for family in families:
            frame = pd.read_csv(directory/f'{family}.csv')
            assert np.array_equal(frame.event_id, old.event_id)
            assert np.array_equal(frame.neg, old.neg)
            selection = json.loads((directory/f'{family}.json').read_text())
            scores[family] = max(c['validation_ap'] for c in selection['candidates'])
            current[family] = frame
            frames[family].append(frame)
            fold_metrics.append({'fold': fold, 'family': family,
                                 **metrics(frame.neg.to_numpy(), frame.probability.to_numpy(), frame.probability.to_numpy() >= .5)})
        template = current[families[0]]
        for name in previous_names:
            frame = template[[c for c in template if c not in ['probability', 'plugin_probability', 'default',
                        'accuracy', 'precision60', 'f1_accuracy77', 'f1_accuracy78', 'f1_accuracy80p6']]].copy()
            frame['probability'] = old[name]
            frame['default'] = old[name] >= .5
            if name != 'saved_compirt':
                for policy, threshold in old_selection[name]['thresholds'].items():
                    if threshold is not None:
                        frame[policy] = old[name] >= threshold
                scores[name] = old_selection[name]['validation_neg_ap']
            current[name] = frame; frames[name].append(frame)
            fold_metrics.append({'fold': fold, 'family': name,
                                 **metrics(frame.neg.to_numpy(), frame.probability.to_numpy(), frame.probability.to_numpy() >= .5)})
        winner_new = max(families, key=lambda f: scores[f])
        winner_all = max(scores, key=scores.get)
        frames['selected_new'].append(current[winner_new])
        frames['selected_with_previous'].append(current[winner_all])
        chosen.append({'fold': fold, 'selected_new': winner_new, 'selected_with_previous': winner_all,
                       'validation_ap': scores})
    (OUTPUT/'family_selection.json').write_text(json.dumps(chosen, indent=2)+'\n')
    pd.DataFrame(fold_metrics).to_csv(OUTPUT/'fold_metrics.csv', index=False)
    all_frames = {k: pd.concat(v, ignore_index=True) for k, v in frames.items()}
    rows = []; sensitivity = []; calibration = []; uncertainty = []
    for family, data in all_frames.items():
        y, p = data.neg.to_numpy(), data.probability.to_numpy()
        for policy in ['default', 'accuracy', 'precision60', 'f1_accuracy77', 'f1_accuracy78', 'f1_accuracy80p6']:
            available = policy in data and data[policy].notna().all()
            row = {'family': family, 'policy': policy, 'available_all_folds': available}
            if available:
                row.update(metrics(y, p, data[policy].astype(bool).to_numpy()))
                row['brier'] = brier_score_loss(y, p)
            rows.append(row)
        for label, mask in [('all', np.ones(len(y), dtype=bool)),
                            ('nonterminal', data.terminal.eq(0).to_numpy()),
                            ('terminal', data.terminal.eq(1).to_numpy()),
                            ('nonzero_scoring', data.value.ne(0).to_numpy())]:
            sensitivity.append({'family': family, 'slice': label,
                                **metrics(y[mask], p[mask], p[mask] >= .5)})
        bins = np.minimum((p*10).astype(int), 9)
        for band in range(10):
            mask = bins == band
            if mask.any():
                calibration.append({'family': family, 'bin': band, 'n': int(mask.sum()),
                                    'predicted': float(p[mask].mean()), 'observed': float(y[mask].mean())})
        if family.startswith('vb_'):
            uncertainty.append({'family': family,
                                'posterior_predictive_log_loss': log_loss(y, p),
                                'plugin_log_loss': log_loss(y, data.plugin_probability),
                                'posterior_predictive_ap': average_precision_score(y, p),
                                'plugin_ap': average_precision_score(y, data.plugin_probability)})
    summary = pd.DataFrame(rows)
    summary.to_csv(OUTPUT/'metrics.csv', index=False)
    pd.DataFrame(sensitivity).to_csv(OUTPUT/'sensitivity.csv', index=False)
    pd.DataFrame(calibration).to_csv(OUTPUT/'calibration.csv', index=False)
    pd.DataFrame(uncertainty).to_csv(OUTPUT/'posterior_averaging.csv', index=False)
    reference = all_frames['frozen_skills']; boot = []
    for family in ([] if args.skip_bootstrap else families+['selected_new', 'selected_with_previous']):
        data = all_frames[family]
        assert np.array_equal(data.event_id, reference.event_id)
        boot.append({'family': family, **bootstrap_delta(data.neg.to_numpy(), data.probability.to_numpy(),
                    reference.probability.to_numpy(), data.game_id.to_numpy())})
        print('bootstrap', boot[-1], flush=True)
    if boot:
        pd.DataFrame(boot).to_csv(OUTPUT/'paired_game_bootstrap.csv', index=False)
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
    plot_names = ['saved_compirt', 'frozen_skills', 'vb_base', 'predictive_mixture']
    if has_boosting:
        plot_names.append('boosting_ensemble')
    labels = {'saved_compirt': 'Original DD-Bernstein', 'frozen_skills': 'Earlier frozen skills',
              'recent_prefix': 'New recent-prefix text', 'vb_base': 'New variational Bayes',
              'predictive_mixture': 'New Bayesian + prefix', 'boosting_ensemble': 'Other study: boosting ensemble'}
    for family in plot_names:
        data = all_frames[family]
        pr, re, _ = precision_recall_curve(data.neg, data.probability)
        axes[0].plot(re, pr, label=labels[family], lw=1.5)
        q = pd.DataFrame(calibration).query('family == @family')
        axes[1].plot(q.predicted, q.observed, '.-', label=family)
    axes[0].plot(.5, .6, 'k*', ms=13, label='desired target')
    axes[0].set(xlabel='Incorrect-buzz recall', ylabel='Incorrect-buzz precision',
                xlim=(0, .7), ylim=(.2, 1), title='Development PR curves (retrospective)')
    axes[0].legend(fontsize=7)
    axes[1].plot([0, 1], [0, 1], 'k--', alpha=.5)
    axes[1].set(xlabel='Mean predicted incorrect probability', ylabel='Observed incorrect fraction',
                title='Held-out calibration')
    q = summary.query("policy == 'f1_accuracy77' and available_all_folds and family in @plot_names")
    axes[2].barh(np.arange(len(q)), q.neg_f1, color='steelblue')
    for i, (_, row) in enumerate(q.iterrows()):
        axes[2].text(row.neg_f1+.005, i, f'{row.neg_f1:.1%} F1 / {row.accuracy:.1%} acc.', va='center', fontsize=8)
    axes[2].set_yticks(np.arange(len(q)), [labels[name] for name in q.family], fontsize=8)
    axes[2].set(xlabel='Held-out incorrect-buzz F1', xlim=(0, .72),
                title='Transferred policy: validation accuracy ≥77%')
    fig.tight_layout(); fig.savefig(OUTPUT/'comparison.png', dpi=180); plt.close(fig)
    print(summary.query("policy in ['default','precision60','f1_accuracy77']")[[
        'family','policy','accuracy','neg_precision','neg_recall','neg_f1','neg_ap','log_loss']].to_string(index=False))


if __name__ == '__main__':
    main()
