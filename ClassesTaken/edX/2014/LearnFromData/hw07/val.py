"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-15
@summary: Problems 1-5
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/hw7ckmewj.pdf
"""

import numpy as np

def get_nonlin(fname):
    """ return features, labels """
    raw_data = np.loadtxt(fname)
    features = np.ones((raw_data.shape[0], 8))
    features[:, 1:3] = raw_data[:, 0:2]
    features[:, 3:5] = raw_data[:, 0:2] * raw_data[:, 0:2]
    features[:, 5] = raw_data[:, 0] * raw_data[:, 1]
    features[:, 6] = np.absolute(raw_data[:, 0] - raw_data[:, 1])
    features[:, 7] = np.absolute(raw_data[:, 0] + raw_data[:, 1])
    return features, raw_data[:, -1]

def get(fname):
    """ return x, y """
    raw_data = np.loadtxt(fname)
    return raw_data[:, :2], raw_data[:, 2]

def _phi0(x):
    return np.ones((x.shape[0], 1))

def _phi1(x):
    return x[:, 0]

def _phi2(x):
    return x[:, 1]

def _phi3(x):
    return x[:, 0] * x[:, 0]
    
def _phi4(x):
    return x[:, 1] * x[:, 1]

def _phi5(x):
    return x[:, 0] * x[:, 1]

def _phi6(x):
    return np.absolute(x[:, 0] - x[:, 1])

def _phi7(x):
    return np.absolute(x[:, 0] + x[:, 1])

phi = [_phi0, _phi1, _phi2, _phi3, _phi4, _phi5, _phi6, _phi7]

def linreg_wts(features, labels):
    return np.linalg.pinv(features).dot(labels)

def linreg_predictions(features, wts):
    return np.sign(features.dot(wts))

def class_err(predicted, actual):
    diff = np.absolute(predicted - actual)
    return float(np.sum(diff > 0.5, axis=0)) / predicted.shape[0]

def prob1():
    """ (6, 0.0) """
    features, labels = get_nonlin('in.data')
    xtrain_all = features[:25, :]
    ytrain = labels[:25]
    xval_all = features[25:, :]
    yval = labels[25:]
    bestk = 3
    best_err = 1.0
    xtrain = xtrain_all
    xval = xval_all
    for k in range(3, 8):
        xtrain = xtrain_all[:, :(k + 1)]
        wts = linreg_wts(xtrain, ytrain)
        xval = xval_all[:, :(k + 1)]
        predval = linreg_predictions(xval, wts)
        err = class_err(predval, yval)
        print k, err
        if err < best_err:
            bestk = k
            best_err = err
    return bestk, best_err

def prob2():
    """ (7, 0.072) """
    features, labels = get_nonlin('in.data')
    xtest_all, ytest = get_nonlin('out.data')
    xtrain_all = features[:25, :]
    ytrain = labels[:25]
    bestk = 3
    best_err = 1.0
    xtrain = xtrain_all
    xtest = xtest_all
    for k in range(3, 8):
        xtrain = xtrain_all[:, :(k + 1)]
        wts = linreg_wts(xtrain, ytrain)
        xtest = xtest_all[:, :(k + 1)]
        predtest = linreg_predictions(xtest, wts)
        err = class_err(predtest, ytest)
        print k, err
        if err < best_err:
            bestk = k
            best_err = err
    return bestk, best_err

def prob3():
    """ (6, 0.08) """
    features, labels = get_nonlin('in.data')
    xval_all = features[:25, :]
    yval = labels[:25]
    xtrain_all = features[25:, :]
    ytrain = labels[25:]
    bestk = 3
    best_err = 1.0
    xtrain = xtrain_all
    xval = xval_all
    for k in range(3, 8):
        xtrain = xtrain_all[:, :(k + 1)]
        wts = linreg_wts(xtrain, ytrain)
        xval = xval_all[:, :(k + 1)]
        predval = linreg_predictions(xval, wts)
        err = class_err(predval, yval)
        print k, err
        if err < best_err:
            bestk = k
            best_err = err
    return bestk, best_err

def prob4():
    """ (6, 0.192) """
    features, labels = get_nonlin('in.data')
    xtest_all, ytest = get_nonlin('out.data')
    xtrain_all = features[25:, :]
    ytrain = labels[25:]
    bestk = 3
    best_err = 1.0
    xtrain = xtrain_all
    xtest = xtest_all
    for k in range(3, 8):
        xtrain = xtrain_all[:, :(k + 1)]
        wts = linreg_wts(xtrain, ytrain)
        xtest = xtest_all[:, :(k + 1)]
        predtest = linreg_predictions(xtest, wts)
        err = class_err(predtest, ytest)
        print k, err
        if err < best_err:
            bestk = k
            best_err = err
    return bestk, best_err
