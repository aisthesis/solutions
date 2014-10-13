'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-12
@summary: Solve linear regression problem
'''

import numpy as np

def get_weights(features, labels):
    """
    @return numpy row vector of weights
    """
    # append constant feature
    X = np.ones((features.shape[0], features.shape[1] + 1))
    X[:, 1:] = features
    return np.dot(np.linalg.pinv(X), labels).transpose()

def get_predictions(weights, features):
    """
    @return numpy column vector of predictions
    """
    real_predictions = get_real_predictions(weights, features)
    predictions = np.ones(real_predictions.shape, dtype=np.int)
    predictions[real_predictions < 0.0] = -1
    return predictions

def get_real_predictions(weights, features):
    """
    @return numpy column vector of predictions
    """
    X = np.ones((features.shape[0], features.shape[1] + 1))
    X[:, 1:] = features
    return np.dot(X, weights.transpose())
