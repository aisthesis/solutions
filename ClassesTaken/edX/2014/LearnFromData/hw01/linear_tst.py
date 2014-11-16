"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-15
@summary: test perceptron implementation in common/linear.py
"""

import random
import sys

import numpy as np

sys.path.append("../common")
import linear
import bin_lin
from bin_lin import BinaryLinear

def prob7():
    n_runs = 1000
    n_pts = 10
    total_iterations = 0
    trainfeat = np.ones((n_pts, 3))
    labels = np.empty((n_pts, 1))
    random.seed()
    for i in range(n_runs):
        classifier = BinaryLinear()
        trainfeat = bin_lin.get_random_points(n_pts)
        labels = classifier.labels(trainfeat)
        #print trainfeat
        #print labels
        wts, n_iter = linear.perceptron(trainfeat, labels, maxiter=2048)
        total_iterations += n_iter
    return float(total_iterations) / n_runs

def prob8():
    n_runs = 1000
    n_pts = 10
    total_err = 0.0
    trainfeat = np.ones((n_pts, 3))
    testfeat = np.ones((100, 3))
    labels = np.empty((n_pts, 1))
    random.seed()
    for i in range(n_runs):
        classifier = BinaryLinear()
        trainfeat = bin_lin.get_random_points(n_pts)
        labels = classifier.labels(trainfeat)
        wts, n_iter = linear.perceptron(trainfeat, labels, maxiter=2048)
        testfeat = bin_lin.get_random_points(100)
        testlab = classifier.labels(testfeat)
        total_err += linear.class_err(linear.predict(testfeat, wts), testlab)
    return total_err / n_runs

def prob9():
    n_runs = 1000
    n_pts = 100
    total_iterations = 0
    trainfeat = np.ones((n_pts, 3))
    labels = np.empty((n_pts, 1))
    random.seed()
    for i in range(n_runs):
        classifier = BinaryLinear()
        trainfeat = bin_lin.get_random_points(n_pts)
        labels = classifier.labels(trainfeat)
        #print trainfeat
        #print labels
        wts, n_iter = linear.perceptron(trainfeat, labels, maxiter=8192)
        total_iterations += n_iter
    return float(total_iterations) / n_runs

def prob10():
    n_runs = 1000
    n_pts = 100
    total_err = 0.0
    trainfeat = np.ones((n_pts, 3))
    testfeat = np.ones((100, 3))
    labels = np.empty((n_pts, 1))
    random.seed()
    for i in range(n_runs):
        classifier = BinaryLinear()
        trainfeat = bin_lin.get_random_points(n_pts)
        labels = classifier.labels(trainfeat)
        wts, n_iter = linear.perceptron(trainfeat, labels, maxiter=16384)
        testfeat = bin_lin.get_random_points(100)
        testlab = classifier.labels(testfeat)
        total_err += linear.class_err(linear.predict(testfeat, wts), testlab)
    return total_err / n_runs
