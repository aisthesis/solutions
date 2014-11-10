"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-07
@summary: Problems 2-6
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/hw63esjeh.pdf
2.  ein = 0.02857142857142857
    eout = 0.084
Something is wrong with the regularization implementation.
"""

import numpy as np

def get_data(fname):
    """ return features, labels """
    raw_data = np.loadtxt(fname)
    features = np.ones((raw_data.shape[0], 8))
    features[:, 1:3] = raw_data[:, 0:2]
    features[:, 3:5] = raw_data[:, 0:2] * raw_data[:, 0:2]
    features[:, 5] = raw_data[:, 0] * raw_data[:, 1]
    features[:, 6] = np.absolute(raw_data[:, 0] - raw_data[:, 1])
    features[:, 7] = np.absolute(raw_data[:, 0] + raw_data[:, 1])
    return features, raw_data[:, -1]

def get_wlin(features, labels):
    return np.linalg.pinv(features).dot(labels)

def get_wreg(features, labels, lambda_val):
    m = features.shape[1]
    return np.linalg.inv(features.transpose().dot(features) + (lambda_val * np.ones((m, m))))\
            .dot(features.transpose()).dot(labels)

def get_predictions(features, wts):
    return np.sign(features.dot(wts))

def error(predicted, actual):
    diff = np.absolute(predicted - actual)
    return float(np.sum(diff > 0.5, axis=0)) / predicted.shape[0]

def _solve_reg(fname, **kwargs):
    features, labels = get_data(fname)
    wts = kwargs.get('weights', get_wreg(features, labels, kwargs.get('lambda_val', 0)))
    print wts
    predicted = get_predictions(features, wts)
    return error(predicted, labels), wts

def prob2():
    """ (0.02857142857142857, 0.084) """
    ein, wts = _solve_reg('in.data')
    eout = _solve_reg('out.data', weights=wts)[0]
    return ein, eout

def prob3():
    """ (0.02857142857142857, 0.084) """
    ein, wts = _solve_reg('in.data', lambda_val=10**-3)
    eout = _solve_reg('out.data', weights=wts)[0]
    return ein, eout

def prob4():
    print 'ein'
    ein, wts = _solve_reg('in.data', lambda_val=10**3)
    print 'eout'
    eout = _solve_reg('out.data', weights=wts)[0]
    return ein, eout

def prob5():
    """ (0, 0.064, 0.02857142857142857) """
    ein_best = eout_best = -1.0
    best_i = -2
    for i in range(-10, 10):
        ein, wts = _solve_reg('in.data', lambda_val=10**i)
        eout = _solve_reg('out.data', weights=wts)[0]
        print "k: {0}, ein: {1}, eout: {2}".format(i, ein, eout)
        if eout < eout_best or eout_best < 0.:
            ein_best = ein
            eout_best = eout
            best_i = i
    return best_i, eout_best, ein_best

