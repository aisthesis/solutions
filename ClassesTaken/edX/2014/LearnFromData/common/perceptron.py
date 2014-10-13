'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-12
@summary: Solve linear regression problem
'''

import random

import numpy as np

def get_weights(features, labels, initial_weights, max_iter=256):
    """
    @return numpy row vector of weights and iterations required
    """
    # append constant feature
    X = np.ones((features.shape[0], features.shape[1] + 1))
    X[:, 1:] = features
    n_iter = 0
    weights = initial_weights.copy()
    predictions = get_predictions(weights, X)
    while not (np.array_equal(predictions, labels)) and n_iter < max_iter:
        diff = np.flatnonzero(predictions == labels)
        ix = diff[random.randrange(len(diff))]
        weights += X[ix, :] * labels[ix]
        n_iter += 1
    return weights, n_iter

def get_predictions(weights, X):
    """
    @param X:   must already have constant feature appended
    @return numpy column vector of predictions
    """
    real_predictions = np.dot(X, weights.transpose())
    predictions = np.ones(real_predictions.shape, dtype=np.int)
    predictions[real_predictions < 0.0] = -1
    return predictions
