"""Audit saved split, label, decision, and optimization contracts."""
import hashlib
import json
import numpy as np
import pandas as pd
from analysis.correctness.bayesian_mark_study.run import OUTPUT, PREVIOUS, FAMILIES


def main():
    count = 0; candidate_fits = 0; max_gradient = 0.; all_events = []
    for fold in range(5):
        split = pd.read_csv(PREVIOUS/f'fold_{fold}/inner_split.csv')
        old = pd.read_csv(PREVIOUS/f'fold_{fold}/predictions.csv')
        all_events.extend(old.event_id)
        for name in list(FAMILIES)+['predictive_mixture']:
            frame = pd.read_csv(OUTPUT/f'fold_{fold}/{name}.csv')
            val = pd.read_csv(OUTPUT/f'fold_{fold}/{name}_validation.csv')
            info = json.loads((OUTPUT/f'fold_{fold}/{name}.json').read_text())
            assert np.array_equal(frame.event_id, old.event_id)
            assert np.array_equal(frame.neg, old.neg)
            assert not set(frame.game_id)&set(split.game_id)
            assert set(val.game_id) <= set(split.loc[split.inner_partition.eq('validation'), 'game_id'])
            assert frame.probability.between(0, 1).all()
            assert val.probability.between(0, 1).all()
            assert not frame.event_id.duplicated().any()
            for policy, cut in info['thresholds'].items():
                if cut is None:
                    assert policy not in frame
                else:
                    assert np.array_equal(frame[policy], frame.probability >= cut)
            if name in FAMILIES:
                assert info['inner_split_sha256'] == hashlib.sha256((PREVIOUS/f'fold_{fold}/inner_split.csv').read_bytes()).hexdigest()
                candidate_fits += len(info['candidates'])+1
            if name.startswith('vb_'):
                for fit in [info['fit']]+[c['fit'] for c in info['candidates']]:
                    max_gradient = max(max_gradient, fit['max_abs_gradient'])
                    assert fit['max_abs_gradient'] < 1e-5
            count += 1
    assert len(all_events) == len(set(all_events)) == 45995
    earlier = json.loads((OUTPUT/'existing_code_hashes.json').read_text())
    dependencies = ['compirt_data.py', 'holdout/game_splits.py',
                    'analysis/correctness/paper_readiness/first_buzz_features.py',
                    'analysis/correctness/tossup_accuracy_study/run.py',
                    'analysis/season_2024_25_eda/analyze.py']
    # The correctness studies were grouped under analysis/correctness/ after
    # these fits ran, so the saved hashes are keyed by their original paths.
    # Content is unchanged by the move; only the key needs translating.
    original_path = {
        'analysis/correctness/paper_readiness/first_buzz_features.py':
            'analysis/paper_readiness/neg_target_experiments.py',
        'analysis/correctness/tossup_accuracy_study/run.py':
            'analysis/tossup_accuracy_study/run.py',
    }
    from pathlib import Path
    changed_sources = [p for p in dependencies
                       if hashlib.sha256(Path(p).read_bytes()).hexdigest()
                       != earlier[original_path.get(p, p)]]
    result = {'status': 'passed', 'family_fold_artifacts': count, 'fits': candidate_fits,
              'unique_scored_events': len(all_events), 'largest_variational_objective_gradient': max_gradient,
              'source_files_changed_since_original_fits': changed_sources,
              'note': 'Validates saved artifacts, not source equivalence or fresh refits. Retired experiments were removed after the original fits.'}
    (OUTPUT/'validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
