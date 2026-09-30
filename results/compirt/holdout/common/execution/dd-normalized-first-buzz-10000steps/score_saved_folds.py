import json
from pathlib import Path
import sys
import numpy as np
import pandas as pd
from analysis.correctness.tossup_accuracy_study.evaluate_timing import score
from compirt_eval.scenario_a_tossups.reconstruction import _load_timing_evaluation_inputs, event_first_buzz_components

fold = int(sys.argv[1])
metadata = {'roots': {'dd-root': '/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps', 'root': '/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/execution/dd-normalized-first-buzz-10000steps'}}
new_root = Path(metadata['roots']['dd-root'])
old_root = Path('results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal')
output = Path(metadata['roots']['root']) / 'dd_full_comparison'
output.mkdir(exist_ok=True)
inputs = _load_timing_evaluation_inputs(new_root / f'fold_{fold}/holdout/pyramidal')
old_predictions = pd.read_csv(old_root / f'fold_{fold}/holdout/pyramidal/tossup_predictions.csv')
columns = ['event_id', 'game_id', 'team_id', 'player_id', 'tossup_id', 't_star', 'T_j', 'y', 'z']
order = ['event_id', 'player_id']
pd.testing.assert_frame_equal(inputs.predictions[columns].sort_values(order).reset_index(drop=True),
                              old_predictions[columns].sort_values(order).reset_index(drop=True), check_dtype=False)
reference = pd.read_csv(f'results/compirt/holdout/common/tossup-accuracy-study/timing_comparison/fold_{fold}_events.csv')
reference = reference[reference.family.eq('saved_compirt')].set_index('event_id')
buzz = inputs.predictions[inputs.predictions.z.eq('BUZZ')].set_index('event_id')
correctness = pd.DataFrame({'neg': 1 - buzz.y, 'new_compirt': 1 - buzz.predicted_correct})
assert correctness.index.is_unique
old_inputs = _load_timing_evaluation_inputs(old_root / f'fold_{fold}/holdout/pyramidal')
old_buzz = old_predictions[old_predictions.z.eq('BUZZ')].set_index('event_id')
old_correctness = pd.DataFrame({'neg': 1 - old_buzz.y, 'saved_compirt': 1 - old_buzz.predicted_correct})
rows, cache, old_cache = [], {}, {}
for index, (event_id, event) in enumerate(inputs.predictions.groupby('event_id', sort=False)):
    components = event_first_buzz_components(event, inputs.players, inputs.tossups, inputs.adjustments,
        inputs.link, inputs.buzz_parameter_prefix, inputs.difficulty_scale, inputs.terminal_intercepts,
        reconstruction_cache=cache)
    rows.append(score(event_id, event, components, correctness, 'new_compirt', fold))
    if index < 10:
        old_components = event_first_buzz_components(event, old_inputs.players, old_inputs.tossups,
            old_inputs.adjustments, old_inputs.link, old_inputs.buzz_parameter_prefix,
            old_inputs.difficulty_scale, old_inputs.terminal_intercepts, reconstruction_cache=old_cache)
        check = score(event_id, event, old_components, old_correctness, 'saved_compirt', fold)
        for key in ('predicted_dead', 'integrated_brier', 'timing_nll', 'race_nll', 'joint_nll'):
            np.testing.assert_allclose(check[key], reference.loc[event_id, key], rtol=1e-6, atol=1e-6)
    if (index + 1) % 3000 == 0:
        print(f'fold {fold}: {index + 1} events scored', flush=True)
frame = pd.DataFrame(rows)
assert frame.event_id.is_unique
assert set(frame.event_id) == set(reference.index)
frame.to_csv(output / f'fold_{fold}_events.csv', index=False)
print(f'fold {fold}: complete, {len(frame)} matched events', flush=True)
