"""Summarize fixed predictions; diagnostic frontiers never select fit parameters."""
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_curve

from analysis.correctness.paper_readiness.first_buzz_features import metrics
from analysis.correctness.tossup_accuracy_study.run import OUTPUT

FAMILIES = ['saved_compirt', 'regularized', 'frozen_skills', 'boosting', 'boosting_ensemble']
POLICIES = ['default', 'accuracy', 'precision60', 'f1_accuracy77',
            'f1_accuracy78', 'f1_accuracy80p6']


def frontier(y, probability):
    p, r, t = precision_recall_curve(y, probability)
    p, r = p[:-1], r[:-1]
    tp = r*np.sum(y)
    fp = tp/np.maximum(p, 1e-15)-tp
    a = 1-(fp+np.sum(y)-tp)/len(y)
    f = 2*p*r/np.maximum(p+r, 1e-15)
    return p, r, t, a, f


def cluster_difference(data, model, cluster, repetitions=2000):
    """Paired cluster bootstrap conditional on fitted models and fixed thresholds."""
    y = data.neg.to_numpy().astype(bool)
    rows = []
    for name in ['saved_compirt', model]:
        pred = data[name].to_numpy() >= .5
        rows.append(np.column_stack([pred == y, pred & y, pred & ~y, ~pred & y,
                                     np.ones(len(y))]))
    codes, _ = pd.factorize(data[cluster])
    totals = np.zeros((2, codes.max()+1, 5))
    for k in range(2):
        np.add.at(totals[k], codes, rows[k])
    rng = np.random.default_rng(20260908)
    diffs = []
    for _ in range(repetitions):
        sampled = rng.integers(totals.shape[1], size=totals.shape[1])
        s = totals[:, sampled].sum(1)
        accuracy = s[:, 0]/s[:, 4]
        f1 = 2*s[:, 1]/(2*s[:, 1]+s[:, 2]+s[:, 3])
        diffs.append([accuracy[1]-accuracy[0], f1[1]-f1[0]])
    return dict(zip(['accuracy_difference_95_interval', 'f1_difference_95_interval'],
                    np.quantile(diffs, [.025, .975], axis=0).T.tolist()))


def main():
    frames = []
    all_boosting = all((OUTPUT/f'fold_{k}/boosting/complete.json').exists() for k in range(5))
    for fold in range(5):
        directory = OUTPUT/f'fold_{fold}'
        assert (directory/'complete.json').exists()
        if all_boosting:
            directory /= 'boosting'
        frame = pd.read_csv(directory/'predictions.csv')
        frame['fold'] = fold
        frames.append(frame)
    data = pd.concat(frames, ignore_index=True)
    assert not data.event_id.duplicated().any()
    families = [f for f in FAMILIES if f in data]
    rows, fold_rows, diagnostics, feasibility = [], [], {}, []
    for name in families:
        p, r, t, a, f = frontier(data.neg, data[name])
        diagnostics[name] = {'retrospective_max_accuracy':float(a.max())}
        for floor in [.77, .78, .806]:
            ix = np.flatnonzero(a >= floor)
            best = int(ix[np.argmax(f[ix])]) if len(ix) else None
            diagnostics[name][f'max_f1_at_accuracy_{floor}'] = (
                dict(accuracy=float(a[best]), f1=float(f[best]), precision=float(p[best]),
                     recall=float(r[best]), threshold=float(t[best])) if best is not None else None)
        for policy in POLICIES:
            column = name+'__'+policy
            pred = data[name] >= .5 if policy == 'default' else data.get(column)
            complete = pred is not None and pred.notna().all()
            feasibility.append(dict(family=name, policy=policy, all_folds_available=complete))
            if not complete:
                continue
            pred = pred.astype(bool)
            rows.append(dict(family=name, policy=policy, **metrics(data.neg, data[name], pred)))
            for fold in range(5):
                mask = data.fold.eq(fold)
                fold_rows.append(dict(family=name, policy=policy, fold=fold,
                                      **metrics(data.loc[mask, 'neg'], data.loc[mask, name], pred[mask])))
    pd.DataFrame(rows).to_csv(OUTPUT/'summary.csv', index=False)
    pd.DataFrame(fold_rows).to_csv(OUTPUT/'fold_metrics.csv', index=False)
    pd.DataFrame(feasibility).to_csv(OUTPUT/'policy_feasibility.csv', index=False)
    (OUTPUT/'retrospective_frontiers.json').write_text(json.dumps(diagnostics, indent=2))
    data.to_csv(OUTPUT/'predictions.csv', index=False)
    sensitivity = []
    for label, mask in [('nonterminal', data.terminal.eq(0)), ('terminal', data.terminal.eq(1)),
                        ('exclude_zero_point_errors', ~(data.neg.eq(1) & data.value.eq(0)))]:
        for name in families:
            part = data[mask]
            sensitivity.append(dict(subset=label, family=name,
                                    **metrics(part.neg, part[name], part[name] >= .5)))
    pd.DataFrame(sensitivity).to_csv(OUTPUT/'sensitivity.csv', index=False)
    intervals = {name:{cluster:cluster_difference(data, name, cluster)
                       for cluster in ['game_id', 'tossup_id']}
                 for name in ['regularized', 'frozen_skills', 'boosting_ensemble'] if name in data}
    (OUTPUT/'conditional_bootstrap.json').write_text(json.dumps(intervals, indent=2))
    plt.rcParams.update({'font.size':11, 'axes.spines.top':False, 'axes.spines.right':False})
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
    for name in ['saved_compirt', 'regularized', 'frozen_skills', 'boosting', 'boosting_ensemble']:
        if name not in data:
            continue
        p, r, _, a, f = frontier(data.neg, data[name])
        axes[0].plot(r, p, label=name.replace('_', ' '), lw=1.5)
        # Upper envelope: maximum attainable F1 subject to each accuracy floor.
        floors = np.linspace(.74, .815, 250)
        envelope = [np.max(f[a >= floor]) if np.any(a >= floor) else np.nan for floor in floors]
        axes[1].plot(floors, envelope, lw=1.5)
    axes[0].scatter([.5], [.6], color='black', marker='*', s=120, label='Desired target')
    axes[0].axhline(data.neg.mean(), ls=':', color='gray')
    axes[0].set(xlabel='Incorrect-buzz recall', ylabel='Incorrect-buzz precision', ylim=(.2, .9), xlim=(0, 1))
    axes[1].scatter([.806], [6/11], color='black', marker='*', s=120)
    axes[1].set(xlabel='Minimum accuracy', ylabel='Maximum incorrect-buzz F1', ylim=(0, .65))
    axes[0].legend(fontsize=8)
    fig.suptitle('Pooled development folds: retrospective threshold diagnostics')
    fig.tight_layout()
    fig.savefig(OUTPUT/'frontiers.png', dpi=180)
    fig.savefig(OUTPUT/'frontiers.pdf')
    hashes = json.loads((OUTPUT/'existing_code_hashes.json').read_text())
    changed = [p for p, h in hashes.items() if not Path(p).exists() or hashlib.sha256(Path(p).read_bytes()).hexdigest() != h]
    (OUTPUT/'integrity.json').write_text(json.dumps(dict(existing_python_files_checked=len(hashes),
                                                       changed_files=changed), indent=2))
    print(pd.DataFrame(rows).query("policy == 'default'")[['family','accuracy','neg_f1','neg_ap']].to_string(index=False))
    print('Changed existing Python files:', changed)


if __name__ == '__main__':
    main()
