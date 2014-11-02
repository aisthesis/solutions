'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-01
@summary: logistic regression exercises

Logistic regression
Output:
...
(0.10665063862625336, 331)
'''

import math
import sys

import numpy as np

sys.path.append("../common")
import bin_linear as bl

def run_experiments(n_experiments, n_training_points):
    eout_tot, n_epochs_tot = 0.0, 0
    eout, n_epochs = 0.0, 0
    for i in range(n_experiments):
        eout, n_epochs = run_experiment(n_training_points)
        eout_tot += eout
        n_epochs_tot += n_epochs

    return eout_tot / n_experiments, n_epochs_tot / n_experiments

def run_experiment(n_training_points):
    fn, features, labels = get_training_data(n_training_points)
    wt, n_epochs = get_wts(features, labels, halt_epsilon=0.01)
    # get error on test data
    tst_feat, tst_lab = get_data(fn, 100)
    eout = get_error(wt, tst_feat, tst_lab)
    print wt, eout, n_epochs
    return eout, n_epochs

def get_training_data(n_training_pts):
    fn = bl.BinaryLinear()
    features, labels = get_data(fn, n_training_pts)
    return fn, features, labels

def get_data(fn, n_pts):
    points = bl.get_random_points(n_pts)
    labels = np.empty((n_pts, 1))
    for i in range(n_pts):
        labels[i, 0] = fn.label(points[i][0], points[i][1])
    features = np.ones((len(points), 3))
    features[:, 1:] = points
    return features, labels


def get_wts(features, labels, eta=0.01, halt_epsilon=0.01):
    wt = np.ones((1, 3))
    nxt_wt = np.zeros((1, 3))
    n_epochs = 0
    while np.linalg.norm(nxt_wt - wt) >= halt_epsilon:
        wt = nxt_wt.copy()
        permutation = np.random.permutation(len(features))
        n_epochs += 1
        for i in permutation:
            nxt_wt -= eta * get_derivative(wt, features[i, :], labels[i])
    return nxt_wt, n_epochs

def get_derivative(wt, feature, y):
    return -(feature * y) / (1 + math.exp(y * feature.dot(np.transpose(wt))))

def get_error(wt, features, labels):
    return np.average(np.log(1 + np.exp(-labels * features.dot(np.transpose(wt)))))

if __name__ == '__main__':
    print run_experiments(100, 100)
