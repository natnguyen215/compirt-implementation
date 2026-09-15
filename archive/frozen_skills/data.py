"""Read exactly the saved reference rosters and training-only spline transforms."""

import numpy as np
import pandas as pd
import torch
from sklearn.preprocessing import SplineTransformer


def tensor(value, device, integer=False):
    return torch.as_tensor(np.asarray(value).copy(), device=device,
                           dtype=torch.long if integer else torch.float32)


def races(frame, player_map, item_map, device):
    events = list(frame.groupby('event_id', sort=False))
    width = max(len(event) for _, event in events)
    players = np.zeros((len(events), width), dtype=int)
    mask = np.zeros_like(players, dtype=float)
    items, total, token, winner, metadata = [], [], [], [], []
    for n, (event_id, event) in enumerate(events):
        if event.player_id.duplicated().any() or event.z.str.startswith('BOUNCE').any():
            raise ValueError('Expected unique phase-0 roster members')
        first = event.iloc[0]
        assert event[['tossup_id', 'T_j', 't_star', 'game_id']].nunique().eq(1).all()
        buzz = np.flatnonzero(event.z.eq('BUZZ'))
        assert len(buzz) <= 1
        assert 1 <= first.t_star <= first.T_j
        if not len(buzz):
            assert first.t_star == first.T_j
        ids = [player_map[p] for p in event.player_id]
        players[n, :len(ids)] = ids
        mask[n, :len(ids)] = 1
        items.append(item_map[first.tossup_id])
        total.append(first.T_j); token.append(first.t_star)
        winner.append(int(buzz[0]) if len(buzz) else -1)
        metadata.append(dict(event_id=event_id, game_id=first.game_id, tossup_id=first.tossup_id,
                             buzz=int(bool(len(buzz))), observed_position=first.t_star / first.T_j))
    data = dict(players=tensor(players, device, True), mask=tensor(mask, device),
                item=tensor(items, device, True), total=tensor(total, device),
                token=tensor(token, device), winner=tensor(winner, device, True),
                n_players=len(player_map), n_items=len(item_map))
    return data, pd.DataFrame(metadata)


def first_buzzes(frame):
    out = frame[frame.z.eq('BUZZ')].copy().set_index('event_id', drop=False)
    assert out.index.is_unique
    out['terminal'] = out.t_star.eq(out.T_j).astype(float)
    out['neg'] = 1 - out.y
    return out


def correctness_design(train, evaluation, timing_draws, player_map, item_map, device):
    """One deterministic transform and draw-specific TRAINING standardization."""
    spline = SplineTransformer(n_knots=5, degree=3, include_bias=False).fit(train[['relative_position']])
    correctness_players = {p: i for i, p in enumerate(sorted(train.player_id.unique()))}
    raw_skills = torch.cat([timing_draws['theta'], timing_draws['speed'][..., None]], -1).detach()
    train_index = tensor([player_map[p] for p in train.player_id], device, True)
    training = raw_skills[:, train_index]
    mean = training.mean(1, keepdim=True)
    sd = training.std(1, correction=0, keepdim=True).clamp_min(.1)
    datasets = []
    for frame in [train, evaluation]:
        ids = tensor([player_map[p] for p in frame.player_id], device, True)
        datasets.append(dict(
            basis=tensor(spline.transform(frame[['relative_position']]), device),
            terminal=tensor(frame.terminal, device),
            player=tensor([correctness_players.get(p, -1) for p in frame.player_id], device, True),
            item=tensor([item_map[j] for j in frame.tossup_id], device, True),
            skills=((raw_skills[:, ids] - mean) / sd).detach(),
            neg=tensor(frame.neg, device), n_players=len(correctness_players), n_items=len(item_map)))
    transforms = dict(spline=spline, correctness_players=correctness_players,
                      skill_mean=mean.cpu(), skill_sd=sd.cpu(), player_map=player_map, item_map=item_map)
    return *datasets, transforms


def evaluation_design(frame, timing_draws, transforms, device):
    """Apply saved training transforms; evaluation outcomes are not used."""
    raw = torch.cat([timing_draws['theta'], timing_draws['speed'][..., None]], -1)
    ids = tensor([transforms['player_map'][p] for p in frame.player_id], device, True)
    return dict(
        basis=tensor(transforms['spline'].transform(frame[['relative_position']]), device),
        terminal=tensor(frame.terminal, device),
        player=tensor([transforms['correctness_players'].get(p, -1) for p in frame.player_id], device, True),
        item=tensor([transforms['item_map'][j] for j in frame.tossup_id], device, True),
        skills=((raw[:, ids] - transforms['skill_mean'][:len(raw)].to(device))
                / transforms['skill_sd'][:len(raw)].to(device)).detach(),
        n_players=len(transforms['correctness_players']), n_items=len(transforms['item_map']))
