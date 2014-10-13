'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-12
@summary: Homework 2, questions 5-10: regression
'''

import numpy as np
import random
import sys

sys.path.append("../common")
import lin_reg
import rand_linear
import perceptron

def get_sample(sample_size=100):
    random.seed()
    return np.random.uniform(-1, 1, (sample_size, 2))

def get_labels(binary_lin, points):
    labels = np.zeros((points.shape[0], 1))
    for i in range(points.shape[0]):
        labels[i] = binary_lin.label(rand_linear.Point(points[i, 0], points[i, 1]))
    return labels

def get_error_ratio(points, labels, weights):
    predictions = lin_reg.get_predictions(weights, points)
    n_errors = np.count_nonzero(predictions != labels)
    return float(n_errors) / points.shape[0]

def get_outofsample_error(binary_lin, weights):
    points = get_sample(1000)
    labels = get_labels(binary_lin, points)
    return get_error_ratio(points, labels, weights)


def simulate(binary_lin):
    """
    return error ratio and weights
    """
    points = get_sample()
    labels = get_labels(binary_lin, points)
    weights = lin_reg.get_weights(points, labels)
    return get_error_ratio(points, labels, weights), weights


def simulate_all():
    repetitions = 1000
    sum_e_in = 0.0
    sum_e_out = 0.0
    e_in = 0.0
    weights = np.zeros((1, 3))
    random.seed()
    for i in range(repetitions):
        binary_lin = rand_linear.BinaryLinear()
        e_in, weights = simulate(binary_lin)
        sum_e_in += e_in
        e_out = get_outofsample_error(binary_lin, weights)
        sum_e_out += e_out
    return sum_e_in / repetitions, sum_e_out / repetitions

def perc_simulate(binary_lin):
    """
    @return iterations required by perceptron when initialized with linear regression
    """
    points = get_sample(10)
    labels = get_labels(binary_lin, points)
    initial_wts = lin_reg.get_weights(points, labels)
    return perceptron.get_weights(points, labels, initial_wts)[1]

def perc_sim_all():
    repetitions = 1000
    sum_iterations = 0
    random.seed()
    for i in range(repetitions):
        binary_lin = rand_linear.BinaryLinear()
        sum_iterations += perc_simulate(binary_lin)
    return float(sum_iterations) / repetitions

