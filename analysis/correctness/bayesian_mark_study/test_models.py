"""Numerical checks for the new inference code; synthetic data only."""
import numpy as np
import pandas as pd
from scipy import sparse
from scipy.integrate import quad
from scipy.special import expit

from analysis.correctness.bayesian_mark_study.models import variational


def test_variational_intercept_matches_numerically_integrated_posterior():
    # A one-parameter posterior can be integrated directly, independently of VI.
    n, successes = 100, 80
    x = sparse.csr_matrix(np.ones((n, 1)))
    y = pd.DataFrame({'neg': np.r_[np.ones(successes), np.zeros(n-successes)]})
    p, plugin, info = variational(x, x[:1], y, np.array([0]), ['global'], {},
                                  device='cpu', max_steps=500)
    def density(beta):
        return np.exp(successes*beta-n*np.logaddexp(0, beta)-beta**2/18+51)
    normalizer = quad(density, -20, 20, epsabs=1e-10)[0]
    exact = quad(lambda b: expit(b)*density(b), -20, 20, epsabs=1e-10)[0]/normalizer
    assert abs(p[0]-exact) < .002
    assert info['max_abs_gradient'] < 1e-5
    assert .5 < p[0] < plugin[0] < 1


def test_quadrature_against_high_order_rule():
    # Covers the predictor uncertainty range observed in the fitted models.
    def integrate(n, mean, sd):
        nodes, weights = np.polynomial.hermite.hermgauss(n)
        return np.dot(weights, expit(mean+np.sqrt(2)*sd*nodes))/np.sqrt(np.pi)
    for mean in [-4., -1., 0., 2.]:
        for sd in [.1, .7, 1.5]:
            assert abs(integrate(16, mean, sd)-integrate(100, mean, sd)) < 2e-5
