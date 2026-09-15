"""Replay frozen timing and saved DD-Bernstein on identical held-out rosters.

Run with .venv/bin/python -m analysis.correctness.tossup_accuracy_study.evaluate_timing.
No fitting or model selection is performed. Timing point predictions condition
on a buzz occurring; distribution scores include dead events.
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.special import softmax

from analysis.correctness.paper_readiness.first_buzz_features import ROOT
from analysis.correctness.tossup_accuracy_study.models import TimingModel
from compirt_eval.scenario_a_tossups.reconstruction import (
    _load_timing_evaluation_inputs, event_first_buzz_components,
)

STUDY = Path('results/compirt/holdout/common/tossup-accuracy-study')
OUTPUT = STUDY / 'timing_comparison'
GRID = np.linspace(0, 1, 21)


def frozen_components(event, checkpoint):
    state = checkpoint['outer']
    ids = event.player_id.astype(str).to_numpy()
    players = np.array([checkpoint['player_map'][p] for p in ids])
    item = checkpoint['item_map'][event.tossup_id.iloc[0]]
    total = int(event.T_j.iloc[0])
    relative = np.arange(1, total + 1) / total
    log_base = (state['theta'][players] @ softmax(state['relevance'][item])
                + state['speed'][players] + state['start'][item])
    base = np.exp(np.clip(log_base, -15, 12))
    slope = min(np.logaddexp(0, state['slope'][item]), 15)
    duration = np.full(total, 1 / total)
    duration[-1] = np.exp(state['end'])
    exposure = base.sum() * np.exp(slope * relative) * duration
    survival = np.exp(-np.r_[0, np.cumsum(exposure)[:-1]])
    mass = survival * -np.expm1(-exposure)
    return dict(relative_position=relative, first_buzz_mass=mass,
                dead_mass=np.exp(-exposure.sum()), player_ids=ids,
                player_first_buzz_mass=base[:, None] / base.sum() * mass)


def score(event_id, event, components, correctness, family, fold):
    relative = components['relative_position']
    mass = components['first_buzz_mass']
    player_mass = components['player_first_buzz_mass']
    dead = float(components['dead_mass'])
    assert np.isfinite(mass).all() and (mass >= 0).all()
    assert abs(mass.sum() + dead - 1) < 1e-8
    assert np.allclose(player_mass.sum(0), mass, atol=1e-10)
    buzz = event[event.z.eq('BUZZ')]
    is_buzz = not buzz.empty
    observed = float(buzz.relative_position.iloc[0]) if is_buzz else np.inf
    idx = np.searchsorted(relative, GRID, side='right')
    cdf = np.r_[0, np.cumsum(mass)][idx]
    squared = (cdf - (GRID >= observed)) ** 2
    row = dict(event_id=event_id, game_id=event.game_id.iloc[0],
               tossup_id=event.tossup_id.iloc[0], family=family, fold=fold,
               buzz=int(is_buzz), predicted_dead=dead, observed_dead=int(not is_buzz),
               dead_brier=(dead - int(not is_buzz)) ** 2,
               integrated_brier=np.trapezoid(squared, GRID))
    if is_buzz:
        actual = buzz.iloc[0]
        token = int(actual.t_star) - 1
        winner = int(np.flatnonzero(components['player_ids'] == str(actual.player_id))[0])
        expected = float(relative @ mass / mass.sum()) if mass.sum() > 1e-12 else 1.
        error = expected - observed
        identity = player_mass.sum(1) / mass.sum()
        row.update(observed_position=observed, predicted_position=expected,
                   absolute_error=abs(error), squared_error=error ** 2, signed_error=error,
                   first_buzzer_top1=float(np.argmax(identity) == winner),
                   first_buzzer_nll=-np.log(max(identity[winner], 1e-300)))
        timing_probability = mass[token]
        race_probability = player_mass[winner, token]
        p_neg = float(correctness.loc[event_id, family])
        assert int(correctness.loc[event_id, 'neg']) == 1 - int(actual.y)
        mark_probability = p_neg if int(actual.y) == 0 else 1 - p_neg
    else:
        timing_probability = race_probability = dead
        mark_probability = 1.
    row.update(timing_nll=-np.log(max(timing_probability, 1e-300)),
               race_nll=-np.log(max(race_probability, 1e-300)),
               joint_nll=-np.log(max(race_probability, 1e-300))
                         - np.log(max(mark_probability, 1e-300)))
    return row


def summarize(frame):
    buzz = frame[frame.buzz.eq(1)]
    return dict(events=len(frame), buzz_events=len(buzz),
                timing_mae=buzz.absolute_error.mean(),
                timing_rmse=np.sqrt(buzz.squared_error.mean()),
                timing_bias=buzz.signed_error.mean(),
                integrated_brier=frame.integrated_brier.mean(),
                timing_nll=frame.timing_nll.mean(), race_nll=frame.race_nll.mean(),
                joint_nll=frame.joint_nll.mean(),
                first_buzzer_accuracy=buzz.first_buzzer_top1.mean(),
                first_buzzer_nll=buzz.first_buzzer_nll.mean(),
                dead_brier=frame.dead_brier.mean(),
                predicted_dead_rate=frame.predicted_dead.mean(),
                observed_dead_rate=frame.observed_dead.mean())


def main():
    OUTPUT.mkdir(exist_ok=True)
    torch.set_num_threads(1)
    rows, checks = [], []
    for fold in range(5):
        checkpoint = torch.load(STUDY / f'fold_{fold}/timing_skills.pt',
                                map_location='cpu', weights_only=False)
        model = TimingModel(len(checkpoint['player_map']), len(checkpoint['item_map']))
        model.load_state_dict(checkpoint['outer'])
        checkpoint['outer'] = {k: v.numpy().astype(float) for k, v in checkpoint['outer'].items()}
        inputs = _load_timing_evaluation_inputs(ROOT / f'fold_{fold}/holdout/pyramidal')
        correctness = pd.read_csv(STUDY / f'fold_{fold}/predictions.csv').set_index('event_id')
        assert correctness.index.is_unique
        cache, fold_rows, seen_buzz = {}, [], set()
        for index, (event_id, event) in enumerate(inputs.predictions.groupby('event_id', sort=False)):
            assert not event.z.astype(str).str.startswith('BOUNCE').any()
            frozen = frozen_components(event, checkpoint)
            bernstein = event_first_buzz_components(
                event, inputs.players, inputs.tossups, inputs.adjustments, inputs.link,
                inputs.buzz_parameter_prefix, inputs.difficulty_scale,
                inputs.terminal_intercepts, reconstruction_cache=cache)
            for family, components in [('saved_compirt', bernstein), ('frozen_skills', frozen)]:
                fold_rows.append(score(event_id, event, components, correctness, family, fold))
            buzz = event[event.z.eq('BUZZ')]
            if not buzz.empty:
                seen_buzz.add(event_id)
            # Independent check against the actual fitted model's likelihood,
            # for initial examples plus every dead/terminal event.
            if index < 10 or buzz.empty or int(event.t_star.iloc[0]) == int(event.T_j.iloc[0]):
                ids = [checkpoint['player_map'][p] for p in event.player_id]
                winner = -1 if buzz.empty else ids.index(checkpoint['player_map'][buzz.player_id.iloc[0]])
                race = [torch.tensor([ids]), torch.ones(1, len(ids)),
                        torch.tensor([checkpoint['item_map'][event.tossup_id.iloc[0]]]),
                        torch.tensor([float(event.t_star.iloc[0])]),
                        torch.tensor([float(event.T_j.iloc[0])]), torch.tensor([winner])]
                with torch.no_grad():
                    reference = model.event_loss(race).item()
                difference = abs(reference - fold_rows[-1]['race_nll'])
                assert difference < 2e-4, (fold, event_id, difference)
                checks.append(difference)
            if (index + 1) % 2000 == 0:
                print(f'fold {fold}: {index + 1} events', flush=True)
        assert seen_buzz == set(correctness.index)
        frame = pd.DataFrame(fold_rows)
        frame.to_csv(OUTPUT / f'fold_{fold}_events.csv', index=False)
        rows.extend(fold_rows)
        print(f'completed fold {fold}', flush=True)
    frame = pd.DataFrame(rows)
    pooled = pd.DataFrame([dict(family=family, **summarize(group))
                           for family, group in frame.groupby('family')])
    folds = pd.DataFrame([dict(fold=fold, family=family, **summarize(group))
                          for (fold, family), group in frame.groupby(['fold', 'family'])])
    pooled.to_csv(OUTPUT / 'summary.csv', index=False)
    folds.to_csv(OUTPUT / 'fold_metrics.csv', index=False)
    (OUTPUT / 'checks.json').write_text(json.dumps(dict(
        likelihood_checks=len(checks), maximum_likelihood_difference=max(checks),
        normalized_pmf_checks=len(frame), correctness_event_sets_match=True,
        brier_grid=GRID.tolist()), indent=2))
    print(pooled.to_string(index=False), flush=True)


if __name__ == '__main__':
    main()
