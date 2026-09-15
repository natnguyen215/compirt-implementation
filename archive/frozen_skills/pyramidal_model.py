"""The existing frozen-skills equations with Gaussian priors and Pyro SVI.

Timing is fitted independently. Given M detached timing-posterior draws, M
independent correctness posteriors are fitted in parallel as one batched model.
This approximates p(phi | timing) p(beta | correctness, phi), a modular/cut
posterior. Correctness never updates or reweights the timing posterior.
"""

import numpy as np
import pyro
import pyro.distributions as dist
import torch
from torch.nn import functional as F


TIMING_SITES = ('theta', 'speed', 'relevance', 'start', 'slope', 'end')


def normal_site(name, shape, reference, mean=0., sd=1.):
    location = reference.new_full(shape, mean)
    return pyro.sample(name, dist.Normal(location, sd).to_event(len(shape)))


def timing_parameters(data, dimensions=3):
    ref = data['mask']
    players, items = data['n_players'], data['n_items']
    return {
        'theta': normal_site('theta', (players, dimensions), ref),
        'speed': normal_site('speed', (players,), ref),
        'relevance': normal_site('relevance', (items, dimensions), ref),
        'start': normal_site('start', (items,), ref, -2., 2.),
        'slope': normal_site('slope', (items,), ref, 2., 2.),
        'end': normal_site('end', (), ref, -2.3, 2.),
    }


def race_rates(data, parameters):
    """Base player rates and slope, with optional leading posterior-draw axis."""
    players, item = data['players'], data['item']
    theta = parameters['theta'][..., players, :]
    weights = parameters['relevance'][..., item, :].softmax(-1)
    projection = (theta * weights.unsqueeze(-2)).sum(-1)
    log_base = (projection + parameters['speed'][..., players]
                + parameters['start'][..., item].unsqueeze(-1))
    base = log_base.clamp(-15, 12).exp() * data['mask']
    slope = F.softplus(parameters['slope'][..., item]).clamp(max=15)
    return base, slope


def event_log_probability(data, parameters):
    """Log P(first winner/token or dead), exactly matching the original model."""
    base, slope = race_rates(data, parameters)
    field = base.sum(-1)
    step = slope / data['total']
    previous = torch.minimum(data['token'] - 1, data['total'] - 1)
    before = (step.exp() * torch.expm1(previous * step)
              / torch.expm1(step).clamp_min(1e-8) / data['total'])
    end = parameters['end']
    if end.ndim:
        end = end.unsqueeze(-1)
    duration = torch.where(data['token'] == data['total'], end.exp(), 1 / data['total'])
    current = field * (slope * data['token'] / data['total']).exp() * duration
    winner_index = data['winner'].clamp_min(0)
    index = winner_index.expand(base.shape[:-1]).unsqueeze(-1)
    winner_base = base.gather(-1, index).squeeze(-1)
    attribution = (winner_base / field.clamp_min(1e-15)).clamp_min(1e-15).log()
    log_any = (-torch.expm1(-current)).clamp_min(1e-15).log()
    return -field * before + torch.where(data['winner'] < 0, -current, log_any + attribution)


def timing_model(data, dimensions=3):
    parameters = timing_parameters(data, dimensions)
    pyro.factor('timing_likelihood', event_log_probability(data, parameters).sum())
    return parameters


def correctness_parameters(data, intercept_sd=10.):
    m = data['skills'].shape[0]
    ref = data['basis']
    b = ref.shape[1]
    return {
        'intercept': normal_site('intercept', (m,), ref, sd=intercept_sd),
        'global_curve': normal_site('global_curve', (m, b), ref),
        'global_terminal': normal_site('global_terminal', (m,), ref),
        'player_effect': normal_site('player_effect', (m, data['n_players']), ref),
        'item_effect': normal_site('item_effect', (m, data['n_items']), ref),
        'item_curve': normal_site('item_curve', (m, data['n_items'], b), ref),
        'item_terminal': normal_site('item_terminal', (m, data['n_items']), ref),
        'skill_weight': normal_site('skill_weight', (m, data['n_items'], data['skills'].shape[-1]), ref),
    }


def correctness_linear(data, coefficients, config, squared=False):
    """Linear predictor, or its variance when supplied diagonal variances."""
    power = 2 if squared else 1
    b = data['basis'].pow(power)
    terminal = data['terminal'].pow(power)
    player, item = data['player'], data['item']
    valid = (player >= 0).to(b.dtype)
    out = coefficients['intercept'][:, None] + coefficients['global_curve'] @ b.T
    out = out + coefficients['global_terminal'][:, None] * terminal
    out = out + coefficients['player_effect'][:, player.clamp_min(0)] * valid * config['player'] ** power
    out = out + coefficients['item_effect'][:, item] * config['item'] ** power
    out = out + (coefficients['item_curve'][:, item] * b[None]).sum(-1) * config['local'] ** power
    out = out + coefficients['item_terminal'][:, item] * terminal * config['local'] ** power
    out = out + (coefficients['skill_weight'][:, item] * data['skills'].pow(power)).sum(-1) * config['skill'] ** power
    return out


def correctness_model(data, config, intercept_sd=10.):
    # Each leading index has its OWN coefficients and its OWN fixed skill draw.
    # Summing their likelihoods fits independent conditional posteriors, rather
    # than one common coefficient posterior against uncertain covariates.
    if data['skills'].requires_grad:
        raise ValueError('Timing features must be detached before correctness fitting')
    coefficients = correctness_parameters(data, intercept_sd)
    logits = correctness_linear(data, coefficients, config)
    pyro.factor('correctness_likelihood', dist.Bernoulli(logits=logits).log_prob(data['neg']).sum())
    return coefficients


def correctness_predictive(data, locations, scales, config, quadrature=24):
    """Integrate sigmoid against the diagonal-normal coefficient posterior."""
    mean = correctness_linear(data, locations, config)
    variance = correctness_linear(data, {k: v.square() for k, v in scales.items()}, config, squared=True)
    nodes, weights = np.polynomial.hermite.hermgauss(quadrature)
    result = torch.zeros_like(mean)
    sd = variance.clamp_min(0).sqrt()
    for node, weight in zip(nodes, weights):
        result += (mean + sd * float(node * np.sqrt(2))).sigmoid() * float(weight / np.sqrt(np.pi))
    return result
