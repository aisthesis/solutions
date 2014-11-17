"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-16
@summary: Problems 8-10
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/hw7ckmewj.pdf
http://courses.csail.mit.edu/6.867/wiki/images/a/a7/Qp-cvxopt.pdf
"""

import random
import sys

from cvxopt import matrix
from cvxopt import solvers
import numpy as np

sys.path.append("../common")
import linear as lin
import bin_lin as blin

def prob8():
    """
    Sample output:
    (0.5781, 0.10930148999999985, 0.09463880000000033)
    Return
    ---
    1. fraction of cases where svm is better than pla
    2. average pla error
    3. average svm error
    """
    n_runs = 10000
    n_pts = 10
    n_tstpts = 10000
    tot_pla_err = 0.0
    tot_svm_err = 0.0
    n_svm_wins = 0
    trainfeat = np.empty((n_pts, 3))
    trainlab = np.empty((n_pts, 1))
    testfeat = np.empty((n_tstpts, 3))
    testlab = np.empty((n_tstpts, 1))
    P = matrix(np.diag((0., 1., 1.)), tc='d')
    q = matrix(np.zeros((3, 1)), tc='d')
    random.seed()
    solvers.options['show_progress'] = False
    for i in range(n_runs):
        classifier = blin.BinaryLinear()
        trainfeat = blin.get_random_points(n_pts)
        trainlab = classifier.labels(trainfeat)
        testfeat = blin.get_random_points(n_tstpts)
        testlab = classifier.labels(testfeat)
        pla_err = _pla_eout(trainfeat, trainlab, testfeat, testlab)
        svm_err = _svm_eout(trainfeat, trainlab, testfeat, testlab, P, q)
        if svm_err < pla_err:
            n_svm_wins += 1
        tot_pla_err += pla_err
        tot_svm_err += svm_err
    return float(n_svm_wins) / n_runs, tot_pla_err / n_runs, tot_svm_err / n_runs

def prob9():
    """
    Sample output:
    (0.6364, 0.013328370000000032, 0.010662909999999965)
    Return
    ---
    1. fraction of cases where svm is better than pla
    2. average pla error
    3. average svm error
    """
    n_runs = 10000
    n_pts = 100
    n_tstpts = 10000
    tot_pla_err = 0.0
    tot_svm_err = 0.0
    n_svm_wins = 0
    trainfeat = np.empty((n_pts, 3))
    trainlab = np.empty((n_pts, 1))
    testfeat = np.empty((n_tstpts, 3))
    testlab = np.empty((n_tstpts, 1))
    P = matrix(np.diag((0., 1., 1.)), tc='d')
    q = matrix(np.zeros((3, 1)), tc='d')
    random.seed()
    solvers.options['show_progress'] = False
    for i in range(n_runs):
        classifier = blin.BinaryLinear()
        trainfeat = blin.get_random_points(n_pts)
        trainlab = classifier.labels(trainfeat)
        testfeat = blin.get_random_points(n_tstpts)
        testlab = classifier.labels(testfeat)
        pla_err = _pla_eout(trainfeat, trainlab, testfeat, testlab, maxiter=16384)
        svm_err = _svm_eout(trainfeat, trainlab, testfeat, testlab, P, q)
        if svm_err < pla_err:
            n_svm_wins += 1
        tot_pla_err += pla_err
        tot_svm_err += svm_err
    return float(n_svm_wins) / n_runs, tot_pla_err / n_runs, tot_svm_err / n_runs

def prob10():
    """
    Sample output:
    (2.987963891675025, 3)

    Return
    ---
    ave. number of support vectors within epsilon = 10**-6
    """
    n_runs = 1000
    n_invalid = 0
    n_pts = 100
    epsilon = 10**-6
    svconst = 1.0 + epsilon
    svtot = 0
    trainfeat = np.empty((n_pts, 3))
    trainlab = np.empty((n_pts, 1))
    P = matrix(np.diag((0., 1., 1.)), tc='d')
    q = matrix(np.zeros((3, 1)), tc='d')
    random.seed()
    solvers.options['show_progress'] = False
    for i in range(n_runs):
        classifier = blin.BinaryLinear()
        trainfeat = blin.get_random_points(n_pts)
        trainlab = classifier.labels(trainfeat)
        G = matrix(-1.0 * trainlab * trainfeat, tc='d')
        h = matrix(-1.0 * np.ones((len(trainlab), 1)), tc='d')
        wts = solvers.qp(P, q, G, h)['x']
        n_svs = np.count_nonzero(np.absolute(trainfeat.dot(wts)) <= svconst)
        if n_svs < 2:
            n_invalid += 1
        else:
            svtot += n_svs
    return float(svtot) / (n_runs - n_invalid), n_invalid

def _pla_eout(trainfeat, trainlab, testfeat, testlab, **kwargs):
    """ error on test data after training on training data """
    maxiter = kwargs.get('maxiter', 2048)
    wts, n_iter = lin.perceptron(trainfeat, trainlab, maxiter=maxiter)
    return lin.class_err(lin.predict(testfeat, wts), testlab)

def _svm_eout(trainfeat, trainlab, testfeat, testlab, P, q):
    """ error on test data after training on training data """
    G = matrix(-1.0 * trainlab * trainfeat, tc='d')
    h = matrix(-1.0 * np.ones((len(trainlab), 1)), tc='d')
    wts = solvers.qp(P, q, G, h)['x']
    return lin.class_err(lin.predict(testfeat, wts), testlab)
