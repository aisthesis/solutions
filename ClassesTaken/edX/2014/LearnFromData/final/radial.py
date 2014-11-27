"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-30
@summary: Problem 13-18
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/final2iejhd.pdf
"""

from cvxopt import matrix
from cvxopt import solvers
import numpy as np
import scipy.spatial
from scipy.spatial.distance import cdist
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

import lloyd
from rbf import Rbf

def prob13(gamma=1.5, n_runs=100):
    """ Output: 0.0004 """
    n_pts = 100
    not_sep_total = 0
    np.random.seed()
    for i in range(n_runs):
        x, y = _getdata(100)
        alpha, kern = _getsvmalpha(x, y, gamma)
        predicted = _svmkernpred(kern, y, alpha)
        errors = np.count_nonzero(predicted != y)
        if errors > 0:
            not_sep_total += 1
    return float(not_sep_total) / n_runs

def _getsvmalpha(x, y, gamma):
    n_pts = len(y)
    kern = _kernel(x, x, gamma)
    P = matrix(_getP(kern, y), tc='d')
    q = matrix(-np.ones((n_pts, 1)), tc='d')
    G = matrix(-np.identity(n_pts), tc='d')
    h = matrix(np.zeros((n_pts, 1)), tc='d')
    A = matrix(y.reshape((1, n_pts)), tc='d')
    b = matrix(np.zeros((1, 1)), tc='d')
    sol = solvers.qp(P, q, G, h, A, b)
    alpha = np.array(sol['x'])
    return alpha, kern

def _getdata(n_pts=100):
    x = _getrandx(n_pts)
    return x, _gety(x)

def _getP(kern, y):
    return np.outer(y, y) * kern

def _kernel(x1, x2, gamma):
    return np.exp(-gamma * cdist(x1, x2, 'sqeuclidean'))

def _getrandx(n_pts):
    return 2. * np.random.random_sample((n_pts, 2)) - 1.

def _gety(x):
    return np.sign(x[:, 1] - x[:, 0] + 0.25 * np.sin(np.pi * x[:, 0])).reshape((x.shape[0], 1))

def _n_svm_errors(x, y, sol):
    pass

def _svmkernpred(kern, y, alpha):
    """ use for in-sample, because kernel already calculated """
    m = _getsvix(alpha)
    n_rows = len(y)
    alpha_y_t = (alpha * y).transpose()
    b = y[m] - alpha_y_t.dot(kern[:, m])
    return np.sign(alpha_y_t.dot(kern) + b).transpose()

def _svmpredict(xin, yin, gamma, alpha, xout):
    m = _getsvix(alpha)
    alpha_y_t = (alpha * yin).transpose()
    b = yin[m] - alpha_y_t.dot(_kernel(xin, xin[m:(m + 1), :], gamma))
    return np.sign(alpha_y_t.dot(_kernel(xin, xout, gamma) + b)).transpose()

def _getsvix(alpha):
    """ return the index of some support vector """
    threshold = 10**-5
    for i in range(len(alpha)):
        if alpha[i] > threshold:
            return i
    raise ValueError("no support vector found")

def prob14(k=9, gamma=1.5, n_runs=512):
    """ 
    Incorrect answer: svm should win with probability > 0.75
    Output: 
    (0.584051724137931, 0.09375, 464)
    (0.6236786469344608, 0.076171875, 473)
    """
    n_pts = 100
    kernformwins = 0
    emptyclustertotal = 0
    validruns = 0
    np.random.seed()
    for i in range(n_runs):
        xin, yin = _getdata(n_pts)
        alpha, kern = _getsvmalpha(xin, yin, gamma)
        pred_svmin = _svmkernpred(kern, yin, alpha)
        # don't count if data not linearly separable
        if np.count_nonzero(pred_svmin != yin) > 0:
            continue
        mu = _getrandx(k)
        try:
            mu = lloyd.centers(xin, init=mu)
        except ValueError:
            emptyclustertotal += 1
            continue
        rbf = Rbf(mu, gamma)
        wts = rbf.getwts(xin, yin)
        xout, yout = _getdata(n_pts)
        pred_svmout = _svmpredict(xin, yin, gamma, alpha, xout)
        pred_rbfout = np.sign(rbf.predict(xout, wts))
        n_correctsvm = np.count_nonzero(pred_svmout == yout)
        n_correctrbf = np.count_nonzero(pred_rbfout == yout)
        if n_correctsvm > n_correctrbf:
            kernformwins += 1
        validruns += 1
    kernwinratio = float(kernformwins) / validruns
    emptyratio = float(emptyclustertotal) / n_runs
    return kernwinratio, emptyratio, validruns

def prob15():
    """ 
    Incorrect: svm should win with probability between 0.6 and 0.9
    Output (various runs):
    (0.476303317535545, 0.17578125, 422)
    """
    return prob14(k=12)

def prob16(gamma=1.5, n_runs=512):
    """ Output:
    Averages for 9 clusters:
    Ein: 0.0256640625
    Eout: 0.041640625
    Averages for 12 clusters:
    Ein: 0.0174609375
    Eout: 0.03486328125
    """
    n_pts = 100
    np.random.seed()
    ein9_tot = ein12_tot = eout9_tot = eout12_tot = 0.
    empty_tot = 0
    for i in range(n_runs):
        xin, yin = _getdata(n_pts)
        mu9 = _getrandx(9)
        try:
            mu9 = lloyd.centers(xin, init=mu9)
        except ValueError:
            empty_tot += 1
            continue
        mu12 = _getrandx(12)
        try:
            mu12 = lloyd.centers(xin, init=mu12)
        except ValueError:
            empty_tot += 1
            continue
        rbf9 = Rbf(mu9, gamma)
        rbf12 = Rbf(mu12, gamma)
        wts9 = rbf9.getwts(xin, yin)
        wts12 = rbf12.getwts(xin, yin)
        pred9in = np.sign(rbf9.predict(xin, wts9))
        pred12in = np.sign(rbf12.predict(xin, wts12))
        ein9_tot += _get_error(pred9in, yin)
        ein12_tot += _get_error(pred12in, yin)
        xout, yout = _getdata(n_pts)
        pred9out = np.sign(rbf9.predict(xout, wts9))
        pred12out = np.sign(rbf12.predict(xout, wts12))
        eout9_tot += _get_error(pred9out, yout)
        eout12_tot += _get_error(pred12out, yout)
    print("Averages for 9 clusters:")
    print("Ein: {0}".format(ein9_tot / n_runs))
    print("Eout: {0}".format(eout9_tot / n_runs))
    print("Averages for 12 clusters:")
    print("Ein: {0}".format(ein12_tot / n_runs))
    print("Eout: {0}".format(eout12_tot / n_runs))

def prob17(k=9, n_runs=512):
    """ Output:
    Averages for gamma = 1.5 :
    Ein: 0.0328787878788
    Eout: 0.0571428571429
    Averages for gamma = 2.0 :
    Ein: 0.0370346320346
    Eout: 0.0614285714286
    Empty clusters: 50
    """
    n_pts = 100
    np.random.seed()
    ein15_tot = ein20_tot = eout15_tot = eout20_tot = 0.
    empty_tot = 0
    validruns = 0
    for i in range(n_runs):
        xin, yin = _getdata(n_pts)
        mu = _getrandx(k)
        try:
            mu = lloyd.centers(xin, init=mu)
        except ValueError:
            empty_tot += 1
            continue
        rbf15 = Rbf(mu, 1.5)
        rbf20 = Rbf(mu, 2.)
        wts15 = rbf15.getwts(xin, yin)
        wts20 = rbf20.getwts(xin, yin)
        pred15in = np.sign(rbf15.predict(xin, wts15))
        pred20in = np.sign(rbf20.predict(xin, wts20))
        ein15_tot += _get_error(pred15in, yin)
        ein20_tot += _get_error(pred20in, yin)
        xout, yout = _getdata(n_pts)
        pred15out = np.sign(rbf15.predict(xout, wts15))
        pred20out = np.sign(rbf20.predict(xout, wts20))
        eout15_tot += _get_error(pred15out, yout)
        eout20_tot += _get_error(pred20out, yout)
        validruns += 1

    print("Averages for gamma = 1.5 :")
    print("Ein: {0}".format(ein15_tot / validruns))
    print("Eout: {0}".format(eout15_tot / validruns))
    print("Averages for gamma = 2.0 :")
    print("Ein: {0}".format(ein20_tot / validruns))
    print("Eout: {0}".format(eout20_tot / validruns))
    print("Empty clusters: {0}".format(empty_tot))

def prob18(k=9, gamma=1.5, n_runs=512):
    """ Output:
    Fraction where Ein = 0 : 0.0231578947368
    Average Ein : 0.0350105263158
    Empty cluster runs : 37
    """
    n_pts = 100
    n_perfect_ein = empty_tot = validruns = 0
    ein_tot = 0.
    np.random.seed()
    for i in range(n_runs):
        xin, yin = _getdata(n_pts)
        mu = _getrandx(k)
        try:
            mu = lloyd.centers(xin, init=mu)
        except ValueError:
            empty_tot += 1
            continue
        rbf = Rbf(mu, gamma)
        wts = rbf.getwts(xin, yin)
        predicted = np.sign(rbf.predict(xin, wts))
        err = _get_error(predicted, yin)
        ein_tot += err
        validruns += 1
        if err < 1.0 / (n_pts * 2):
            n_perfect_ein += 1
    print("Fraction where Ein = 0 : {0}".format(float(n_perfect_ein) / validruns))
    print("Average Ein : {0}".format(ein_tot / validruns))
    print("Empty cluster runs : {0}".format(empty_tot))

def _get_error(predicted, actual):
    return float(np.count_nonzero(predicted != actual)) / len(actual)
