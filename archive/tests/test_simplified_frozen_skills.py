"""Contracts for the single-head, fixed-trait Bernstein experiment."""
import numpy as np
import pyro
import torch

from frozen_skills.simplified import design, logits, model, predict
from tests.test_frozen_skills import frame, parameters
from utils.training import fit_svi


def checkpoint():
    return dict(outer={k: v.float() for k, v in parameters().items()},
                player_map={'p0': 0, 'p1': 1}, item_map={'q': 0})


def test_curve_monotonic_and_prediction_ignores_labels():
    rows = frame().iloc[[0]].copy()
    rows = rows.loc[rows.index.repeat(4)].reset_index(drop=True)
    rows['t_star'] = [1, 2, 3, 4]
    cp = checkpoint()
    p = dict(ability=torch.zeros(2), weight=torch.zeros(1, 4),
             start=torch.tensor([2.]), drop=torch.tensor([3.]),
             shares=torch.tensor([[.2, .3, .5]]), terminal=torch.tensor(0.))
    data = design(rows, cp)
    z = logits(data, p)
    assert (z[1:] > z[:-1]).all()
    assert torch.allclose(z[-1], torch.tensor(1.))
    artifact = dict(median=p, timing=cp)
    np.testing.assert_array_equal(predict(rows, artifact), predict(rows.drop(columns=['y']), artifact))
    p['terminal'] = torch.tensor(-2.)
    changed = logits(data, p)
    torch.testing.assert_close(changed[:-1], z[:-1])
    torch.testing.assert_close(changed[-1], z[-1]-2)


def test_svi_preserves_timing_and_fits_one_head():
    pyro.set_rng_seed(4)
    cp = checkpoint()
    before = {k: v.clone() for k, v in cp['outer'].items()}
    data = design(frame(), cp)
    median, _, losses = fit_svi(model, model_kwargs=dict(data=data, correct=torch.tensor([1., 0.])),
                               n_steps=3, lr=.005)
    assert np.isfinite(losses).all()
    assert median['weight'].shape == (1, 4)
    assert set(median) == {'ability', 'weight', 'start', 'drop', 'shares', 'terminal'}
    for key, value in before.items():
        torch.testing.assert_close(cp['outer'][key], value)
