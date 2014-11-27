"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-26
@summary: Problems 7-10
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/final2iejhd.pdf
"""

import numpy as np

def get(fname):
    """ return x, y """
    raw_data = np.loadtxt("data/{0}".format(fname))
    y = np.empty((raw_data.shape[0]), dtype=int)
    np.around(raw_data[:, 0], out=y)
    return raw_data[:, 1:], y

def add_const(x):
    features = np.ones((x.shape[0], x.shape[1] + 1), dtype=np.float64)
    features[:, 1:] = x
    return features

def get_err(features, labels, weights):
    predicted = np.sign(features.dot(weights))
    return float(np.count_nonzero(predicted != labels)) / len(labels)

def one_vs_all(x, y, digit):
    """
    returns new features and labels where the given
    digit has label 1 and all other digits have label -1
    The constant feature is also appended to x as first column
    """
    labels = np.ones(y.shape)
    labels[y != digit] = -1
    return x, labels

def one_vs_one(x, y, digit1, digit2):
    """
    returns new features and labels where any
    row not corresponding to digit1 or digit2 is removed
    and where digit1 gets label 1, digit2 label -1
    """
    mask = ((y == digit1) + (y == digit2))
    labels = y[mask]
    labels[labels == digit2] = -1
    labels[labels == digit1] = 1
    return x[mask, :], labels

def get_weights(features, labels, lamb=0):
    n_cols = features.shape[1]
    return np.linalg.pinv(features.transpose().dot(features) + lamb * np.identity(n_cols))\
            .dot(features.transpose()).dot(labels)

def prob7(begin=5, end=10):
    """ Output: (8, 0.07433822520916199) """
    lamb = 1.0
    lowestein = 1.0
    bestdigit = begin - 1
    xtrain, ytrain = get('features.train')
    xtrain = add_const(xtrain)
    for digit in range(begin, end):
        trainfeat, trainlab = one_vs_all(xtrain, ytrain, digit)
        wts = get_weights(trainfeat, trainlab, lamb)
        ein = get_err(trainfeat, trainlab, wts)
        print("Ein for digit {0}: {1}".format(digit, ein))
        if ein < lowestein:
            lowestein = ein
            bestdigit = digit
    return bestdigit, lowestein

def _transform8(features):
    """ nonlinear transform of features
    the features passed in should NOT include a constant feature
    """
    xform = np.ones((features.shape[0], 6))
    xform[:, 1:3] = features[:, :]
    xform[:, 3] = features[:, 0] * features[:, 1]
    xform[:, 4] = features[:, 0] * features[:, 0]
    xform[:, 5] = features[:, 1] * features[:, 1]
    return xform

def prob8(begin=0, end=5):
    """ Output: (1, 0.02192326856003986) """
    lamb = 1.0
    lowesteout = 1.0
    bestdigit = begin - 1
    xtrain, ytrain = get('features.train')
    xtrain = _transform8(xtrain)
    xtst, ytst = get('features.test')
    xtst = _transform8(xtst)
    for digit in range(begin, end):
        trainfeat, trainlab = one_vs_all(xtrain, ytrain, digit)
        tstfeat, tstlab = one_vs_all(xtst, ytst, digit)
        wts = get_weights(trainfeat, trainlab, lamb)
        eout = get_err(tstfeat, tstlab, wts)
        print("Eout for digit {0}: {1}".format(digit, eout))
        if eout < lowesteout:
            lowesteout = eout
            bestdigit = digit
    return bestdigit, lowesteout

def prob9():
    """
    Output:
    digit, eout, eoutxform, ratio:
    0, 0.227703039362, 0.106626806178, 0.468271334792
    1, 0.131041355257, 0.02192326856, 0.167300380228
    2, 0.0986547085202, 0.0986547085202, 1.0
    3, 0.0827105132038, 0.0827105132038, 1.0
    4, 0.0996512207275, 0.0996512207275, 1.0
    5, 0.079720976582, 0.0792227204783, 0.99375
    6, 0.0847035376183, 0.0847035376183, 1.0
    7, 0.0732436472347, 0.0732436472347, 1.0
    8, 0.0827105132038, 0.0827105132038, 1.0
    9, 0.0881913303438, 0.0881913303438, 1.0
    """
    lamb = 1.0
    xtrain, ytrain = get('features.train')
    xtrainxform = _transform8(xtrain)
    xtst, ytst = get('features.test')
    xtstxform = _transform8(xtst)
    print("digit, eout, eoutxform, ratio:")
    for digit in range(10):
        trainfeat, trainlab = one_vs_all(xtrain, ytrain, digit)
        trainfeatxform, trainlabxform = one_vs_all(xtrainxform, ytrain, digit)
        tstfeat, tstlab = one_vs_all(xtst, ytst, digit)
        tstfeatxform, tstlabxform = one_vs_all(xtstxform, ytst, digit)
        wts = get_weights(trainfeat, trainlab, lamb)
        wtsxform = get_weights(trainfeatxform, trainlabxform, lamb)
        eout = get_err(tstfeat, tstlab, wts)
        eoutxform = get_err(tstfeatxform, tstlabxform, wtsxform)
        print("{0}, {1}, {2}, {3}".format(digit, eout, eoutxform, eoutxform / eout))

def prob10(digit1=1, digit2=5):
    """
    Output:
    lambda, ein, out
    0.01, 0.00448430493274, 0.0283018867925
    1, 0.00512491992313, 0.0259433962264
    """
    xtrain, ytrain = get('features.train')
    xtrainxform = _transform8(xtrain)
    xtst, ytst = get('features.test')
    xtstxform = _transform8(xtst)
    trainfeat, trainlab = one_vs_one(xtrainxform, ytrain, digit1, digit2)
    tstfeat, tstlab = one_vs_one(xtstxform, ytst, digit1, digit2)
    print("lambda, ein, out")
    for i in range(-2, 1, 2):
        lamb = 10**i
        wts = get_weights(trainfeat, trainlab, lamb)
        ein = get_err(trainfeat, trainlab, wts)
        eout = get_err(tstfeat, tstlab, wts)
        print("{0}, {1}, {2}".format(lamb, ein, eout))

