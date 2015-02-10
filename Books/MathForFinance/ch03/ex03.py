"""
Exercises from ch. 3
"""

import math

import numpy as np
import pynance as pn

def get_rets11():
    """
    Returns for individual equities, as specified on p. 73
    """
    return np.array([0.2, 0.13, 0.17])

def get_covs11():
    """
    Covariance matrix using values on p. 73
    """
    _sds = np.array([0.25, 0.28, 0.2])
    _corrs = np.array([0., 0.15, 0.3])
    return get_covs(_sds, _corrs)

def get_rets10():
    """
    Returns from ex. 3.10, p. 72
    """
    return np.array([0.08, 0.1, 0.06])

def get_covs10():
    """
    Covariance matrix for exercise 3.10, p. 72
    """
    _sds = np.array([0.15, 0.05, 0.12])
    _corrs = np.array([0., -0.2, 0.3])
    return get_covs(_sds, _corrs)

def get_covs(sds, corrs):
    """
    Covariance matrix derived from given values.

    Correlations must be ordered by the missing component, i.e.,
    rho12, rho02, rho01
    """
    _covs = np.zeros((3, 3))
    _other1 = _other2 = 0
    for i in range(3):
        _covs[i, i] = sds[i]**2
        _other1 = (i + 1) % 3
        _other2 = (i + 2) % 3
        _covs[_other1, _other2] = _covs[_other2, _other1] = \
                corrs[i] * sds[_other1] * sds[_other2]
    return _covs
        
def get_opt():
    """
    Return a, b, minimal risk return
    """
    _exp_rets = get_rets()
    _covs = get_covs()
    return pn.pf.optimize(_exp_rets, _covs)

def get_risk(wts, covs):
    """
    Return risk based on wts and covariance matrix
    """
    return math.sqrt(wts.dot(covs).dot(wts))

def get_mktpf(rets, covs, rate):
    """
    Weights for market portfolio (ex. 3.14)
    """
    _u = np.ones((len(rets)))
    _covinv = np.linalg.inv(covs)
    _vec = rets - rate * _u
    return (1. / _vec.dot(_covinv).dot(_u)) * _vec.dot(_covinv) 
