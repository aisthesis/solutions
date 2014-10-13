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
    diff = labels - predictions
    return np.sum(diff * diff) / points.shape[0]

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
