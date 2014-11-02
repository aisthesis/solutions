'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-01
@summary: logistic regression exercises

Logistic regression
Output:
'''

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
    fn, points, labels = get_training_data(n_training_points)
    print labels

    eout = 0.1
    n_epochs = 550
    return eout, n_epochs

def get_training_data(n_training_pts):
    fn = bl.BinaryLinear()
    points = bl.get_random_points(n_training_pts)
    labels = [0] * n_training_pts
    for i in range(n_training_pts):
        labels[i] = fn.label(points[i][0], points[i][1])
    return fn, points, labels

#def get_wts(points, labels):

if __name__ == '__main__':
    print run_experiments(3, 4)
