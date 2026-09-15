"""Synthetic probability, design-equivalence, and cut-posterior checks."""

import numpy as np
import pandas as pd
import pyro
import torch

from analysis.correctness.tossup_accuracy_study.models import TimingModel
from analysis.correctness.tossup_accuracy_study.predictor import CorrectnessPredictor
from frozen_skills.data import races, first_buzzes, correctness_design
from frozen_skills.evaluation import predict_events
from frozen_skills.pyramidal_model import (
    event_log_probability, timing_model, correctness_model,
    correctness_linear, correctness_predictive,
)
from utils.training import fit_svi


CONFIG = dict(player=1., item=1., local=3., skill=.25, curve='spline')


def frame(winner=0, token=2, total=4, event='e', item='q'):
    return pd.DataFrame([dict(event_id=event, game_id='g', tossup_id=item,
                              player_id=f'p{i}', t_star=token, T_j=total,
                              relative_position=token / total, y=(1 if i == winner else np.nan),
                              z=('NO-BUZZ' if winner is None else 'BUZZ' if i == winner else 'CENSORED'))
                         for i in range(2)])


def parameters():
    torch.manual_seed(8)
    return {k: v.detach().double() for k, v in TimingModel(2, 1).state_dict().items()}


def data_for(rows):
    data, meta = races(rows, {'p0': 0, 'p1': 1}, {'q': 0}, 'cpu')
    return {k: v.double() if torch.is_tensor(v) and v.is_floating_point() else v for k, v in data.items()}, meta


def test_timing_matches_original_and_enumerates_to_one():
    values = parameters()
    model = TimingModel(2, 1).double()
    model.load_state_dict(values)
    total_probability = 0.
    for token in range(1, 5):
        for winner in range(2):
            data, _ = data_for(frame(winner, token))
            expected = -model.event_loss([data[k] for k in ['players','mask','item','token','total','winner']])
            actual = event_log_probability(data, values).sum()
            torch.testing.assert_close(actual, expected)
            traced = pyro.poutine.trace(pyro.poutine.condition(timing_model, data=values)).get_trace(data)
            traced.compute_log_prob()
            torch.testing.assert_close(traced.nodes['timing_likelihood']['log_prob'], actual)
            total_probability += actual.exp().item()
    data, _ = data_for(frame(None, 4))
    total_probability += event_log_probability(data, values).exp().item()
    assert abs(total_probability - 1) < 1e-12


def test_replay_matches_likelihood_and_preserves_joint_mark_mass():
    rows = pd.concat([frame(event='e0'), frame(None, 4, event='e1')])
    data, meta = data_for(rows)
    p = parameters()
    draws = {k: torch.stack([v, v + .1]) for k, v in p.items()}
    marks = torch.tensor([[.2], [.8]], dtype=torch.float64)
    output, checks = predict_events(data, meta, draws, marks, ['e0'], batch_size=1)
    expected = event_log_probability(data, draws).exp().mean(0)
    np.testing.assert_allclose(np.exp(-output.race_nll), expected, atol=1e-12)
    assert abs(output.neg_joint.iloc[0] + output.correct_joint.iloc[0] - expected[0]) < 1e-12
    assert checks['maximum_pmf_error'] < 1e-12
    assert 0 <= output.predicted_neg.iloc[0] <= 1


def design_fixture():
    rows = pd.concat([frame(winner=n%2, token=n%4+1, event=f'e{n}', item=f'q{n%2}') for n in range(12)])
    buzz = first_buzzes(rows)
    buzz['neg'] = np.arange(len(buzz)) % 2
    maps = {'p0': 0, 'p1': 1}, {'q0': 0, 'q1': 1}
    theta = torch.tensor([[[.1,.2,.3],[.4,.1,-.1]], [[.3,.1,.2],[-.2,.1,.4]]])
    draws = dict(theta=theta, speed=torch.tensor([[.1,.3],[-.2,.1]]))
    train, evaluation, transforms = correctness_design(buzz, buzz, draws, *maps, 'cpu')
    return buzz, draws, train, evaluation, transforms


def test_correctness_design_matches_original_sparse_predictor():
    buzz, draws, data, _, _ = design_fixture()
    sample = pyro.poutine.trace(correctness_model).get_trace(data, CONFIG)
    coeff = {name: node['value'] for name, node in sample.nodes.items()
             if node['type']=='sample' and name != 'correctness_likelihood'}
    logits = correctness_linear(data, coeff, CONFIG).detach().numpy()
    for d in range(2):
        skills = torch.cat([draws['theta'][d],draws['speed'][d,:,None]],-1).numpy()
        old = CorrectnessPredictor(CONFIG,{f'p{i}':skills[i] for i in range(2)}).fit(buzz)
        c = {k:v[d].detach().numpy() for k,v in coeff.items()}
        vector = np.r_[c['global_curve'], c['global_terminal'], c['player_effect'],c['item_effect'],
                       c['item_curve'].T.ravel(),c['item_terminal'],c['skill_weight'].T.ravel()]
        expected = old.transform(buzz) @ vector + c['intercept']
        np.testing.assert_allclose(logits[d], expected, atol=2e-6)


def test_svi_correctness_leaves_timing_frozen_and_saves_positive_uncertainty():
    _, draws, data, _, _ = design_fixture()
    before = {k:v.clone() for k,v in draws.items()}
    pyro.set_rng_seed(5)
    _, guide, losses = fit_svi(correctness_model, model_kwargs=dict(data=data,config=CONFIG),n_steps=3,lr=.01)
    assert np.isfinite(losses).all()
    for k in draws:
        torch.testing.assert_close(draws[k],before[k],rtol=0,atol=0)
    quantiles = guide.quantiles([.5,.8413447460685429],data,CONFIG)
    loc = {k:v[0] for k,v in quantiles.items()}
    sd = {k:v[1]-v[0] for k,v in quantiles.items()}
    assert all((v>0).all() for v in sd.values())
    p24 = correctness_predictive(data,loc,sd,CONFIG)
    p48 = correctness_predictive(data,loc,sd,CONFIG,quadrature=48)
    torch.testing.assert_close(p24,p48,atol=2e-6,rtol=1e-5)
    # Conditional components have distinct coefficients, not a shared head.
    assert loc['skill_weight'].shape == (2,2,4)


def test_zero_coefficient_uncertainty_reduces_to_point_prediction():
    _,_,data,_,_ = design_fixture()
    trace=pyro.poutine.trace(correctness_model).get_trace(data,CONFIG)
    loc={k:n['value'] for k,n in trace.nodes.items() if n['type']=='sample' and k!='correctness_likelihood'}
    actual=correctness_predictive(data,loc,{k:torch.zeros_like(v) for k,v in loc.items()},CONFIG)
    torch.testing.assert_close(actual,correctness_linear(data,loc,CONFIG).sigmoid())
