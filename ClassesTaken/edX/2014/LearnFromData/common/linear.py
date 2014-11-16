'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-12
@summary: Perceptron learning algorithm
'''

import random

import numpy as np

def perceptron(features, labels, **kwargs):
    """
    @return numpy vector of weights and iterations required
    """
    wt_row = kwargs.get('initial_wts', np.zeros((1, features.shape[1])))
    max_iter = kwargs.get('maxiter', 256)
    n_iter = 0
    predictions = predict(features, wt_row.transpose())
    while not np.array_equal(predictions, labels):
        if n_iter == max_iter:
            raise RuntimeError("data not separated after maximum iterations")
        # get misclassified elements
        diff = np.flatnonzero(predictions != labels)
        # choose random misclassified element
        ix = diff[random.randrange(len(diff))]
        wt_row += labels[ix] * features[ix, :]
        predictions = predict(features, wt_row.transpose())
        n_iter += 1
    return wt_row.transpose(), n_iter

def predict(features, wts):
    """
    @param features:   must already have constant feature appended
    @return numpy column vector of predictions
    """
    return np.sign(features.dot(wts))

def class_err(predicted, actual):
    """ fraction of incorrect labels """
    diff = np.absolute(predicted - actual)
    return float(np.sum(diff > 0.5, axis=0)) / predicted.shape[0]
