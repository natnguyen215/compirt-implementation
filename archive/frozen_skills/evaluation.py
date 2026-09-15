"""Posterior-predictive first-buzz distributions and like-for-like score tables."""

import numpy as np
import pandas as pd
import torch

from analysis.correctness.paper_readiness.first_buzz_features import metrics
from frozen_skills.pyramidal_model import race_rates


GRID = np.linspace(0, 1, 21)


def slice_races(data, start, stop):
    return {k: v[start:stop] if torch.is_tensor(v) else v for k, v in data.items()}


@torch.no_grad()
def predict_events(data, metadata, draws, mark_probabilities, buzz_ids, batch_size=256):
    """Integrate timing and its paired conditional correctness posterior.

    mark_probabilities[d, n] has already integrated coefficient uncertainty
    conditional on timing draw d. Mixture probabilities, not losses, are averaged.
    The returned conditional mark divides joint event mass by race event mass.
    """
    n = len(metadata)
    m = draws['theta'].shape[0]
    assert mark_probabilities.shape == (m, len(buzz_ids))
    lookup = {event_id: index for index, event_id in enumerate(buzz_ids)}
    rows = []
    checks = []
    grid = data['mask'].new_tensor(GRID)
    for start in range(0, n, batch_size):
        stop = min(start + batch_size, n)
        part = slice_races(data, start, stop)
        base, slope = race_rates(part, draws)
        field = base.sum(-1)
        positions = torch.arange(1, int(part['total'].max()) + 1, device=base.device)
        relative = positions[None, :] / part['total'][:, None]
        active = positions[None, :] <= part['total'][:, None]
        duration = torch.where(positions[None, :] == part['total'][:, None],
                               draws['end'].exp()[:, None, None], 1 / part['total'][None, :, None])
        exposure = field[:, :, None] * (slope[:, :, None] * relative).exp() * duration * active
        before = torch.cat([torch.zeros_like(exposure[:, :, :1]), exposure.cumsum(-1)[:, :, :-1]], -1)
        mass = (-before).exp() * -torch.expm1(-exposure)
        dead = (-exposure.sum(-1)).exp()
        probability = mass.mean(0)
        dead_probability = dead.mean(0)
        checks.append(float((probability.sum(-1) + dead_probability - 1).abs().max()))
        assert checks[-1] < 5e-6, checks[-1]
        total_buzz = mass.sum(-1)
        player_probability = (base / field[:, :, None] * total_buzz[:, :, None]).mean(0)
        player_probability /= probability.sum(-1)[:, None].clamp_min(1e-20)
        expected = (probability * relative).sum(-1) / probability.sum(-1).clamp_min(1e-20)
        counts = torch.floor(part['total'][:, None] * grid + 1e-6).long()
        cdf = torch.cat([torch.zeros_like(probability[:, :1]), probability.cumsum(-1)], -1).gather(1, counts)
        observed = part['token'] / part['total']
        truth = (grid >= observed[:, None]) & (part['winner'][:, None] >= 0)
        brier = torch.trapezoid((cdf - truth.float()).square(), grid, dim=-1)
        index = (part['token'].long() - 1)[None, :, None].expand(m, -1, 1)
        time_at_stop = mass.gather(-1, index).squeeze(-1)
        winner_index = part['winner'].clamp_min(0)[None, :, None].expand(m, -1, 1)
        attribution = base.gather(-1, winner_index).squeeze(-1) / field
        winner_time = time_at_stop * attribution
        for offset in range(stop - start):
            meta = metadata.iloc[start + offset]
            is_buzz = bool(meta.buzz)
            dp = float(dead_probability[offset])
            row = dict(meta, predicted_dead=dp, observed_dead=int(not is_buzz),
                       dead_brier=(dp - int(not is_buzz)) ** 2,
                       integrated_brier=float(brier[offset]))
            if is_buzz:
                mark = mark_probabilities[:, lookup[meta.event_id]].to(base.device)
                race_draw = winner_time[:, offset]
                race_probability = float(race_draw.mean())
                time_probability = float(time_at_stop[:, offset].mean())
                neg_joint = float((race_draw * mark).mean())
                correct_joint = float((race_draw * (1 - mark)).mean())
                error = float(expected[offset]) - float(observed[offset])
                row.update(predicted_position=float(expected[offset]), absolute_error=abs(error),
                           squared_error=error ** 2, signed_error=error,
                           first_buzzer_top1=float(player_probability[offset].argmax() == part['winner'][offset]),
                           first_buzzer_nll=-np.log(max(float(player_probability[offset, part['winner'][offset]]), 1e-300)),
                           predicted_neg=neg_joint / max(race_probability, 1e-300),
                           mark_only_neg=float(mark.mean()),
                           neg_joint=neg_joint, correct_joint=correct_joint)
            else:
                race_probability = time_probability = dp
            row.update(timing_nll=-np.log(max(time_probability, 1e-300)),
                       race_nll=-np.log(max(race_probability, 1e-300)))
            rows.append(row)
    return pd.DataFrame(rows), dict(maximum_pmf_error=max(checks), pmfs=n)


def summarize(events):
    buzz = events[events.buzz.eq(1)]
    return dict(events=len(events), buzz_events=len(buzz),
                timing_mae=buzz.absolute_error.mean(), timing_rmse=np.sqrt(buzz.squared_error.mean()),
                timing_bias=buzz.signed_error.mean(), integrated_brier=events.integrated_brier.mean(),
                timing_nll=events.timing_nll.mean(), race_nll=events.race_nll.mean(),
                joint_nll=events.joint_nll.mean(), first_buzzer_accuracy=buzz.first_buzzer_top1.mean(),
                first_buzzer_nll=buzz.first_buzzer_nll.mean(), dead_brier=events.dead_brier.mean(),
                predicted_dead_rate=events.predicted_dead.mean(), observed_dead_rate=events.observed_dead.mean())


def correctness_scores(frame, column='predicted_neg'):
    return metrics(frame.neg.to_numpy(), frame[column].to_numpy(), frame[column].to_numpy() >= .5)
