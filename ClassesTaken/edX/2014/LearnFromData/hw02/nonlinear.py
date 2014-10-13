'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-12
@summary: Homework 2, questions 8-10: non-linear target
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

def get_labels(points):
    values = points[:,0] * points[:,0] + points[:,1] * points[:,1] - 0.6
    noise = np.random.rand(values.shape[0])
    values[noise < 0.1] *= -1.0
    labels = np.ones(values.shape, dtype=np.int)
    labels[values < 0.0] = -1
    return labels

def get_error_ratio(points, labels, weights):
    predictions = lin_reg.get_predictions(weights, points)
    n_errors = np.count_nonzero(predictions != labels)
    return float(n_errors) / points.shape[0]

def sim_linear():
    points = get_sample(1000)
    labels = get_labels(points)
    weights = lin_reg.get_weights(points, labels)
    return get_error_ratio(points, labels, weights)

def sim_lin_all():
    repetitions = 1000
    sum_e_in = 0.0
    random.seed()
    for i in range(repetitions):
        binary_lin = rand_linear.BinaryLinear()
        sum_e_in += sim_linear()
    return sum_e_in / repetitions

def get_nl_weights():
    points = get_sample(1000)
    labels = get_labels(points)
    features = get_nl_features(points)
    return lin_reg.get_weights(features, labels)

def get_nl_features(points):
    features = np.zeros((points.shape[0], 5))
    features[:, 0:1] = points[:, 0:1]
    features[:, 2] = points[:, 0] * points[:, 1]
    features[:, 3] = points[:, 0] * points[:, 0]
    features[:, 4] = points[:, 1] * points[:, 1]
    return features

def simulate():
    training_pts = get_sample(1000)
    training_labels = get_labels(training_pts)
    training_features = get_nl_features(training_pts)
    weights = lin_reg.get_weights(training_features, training_labels)
    test_pts = get_sample(1000)
    test_labels = get_labels(test_pts)
    test_features = get_nl_features(test_pts)
    predictions = lin_reg.get_predictions(weights, test_features)
    n_errors = np.count_nonzero(predictions != test_labels)
    return float(n_errors) / test_labels.shape[0]

def simulate_all():
    n_reps = 1000
    sum_error_ratio = 0.0
    for i in range(n_reps):
        sum_error_ratio += simulate()
    return sum_error_ratio / n_reps

