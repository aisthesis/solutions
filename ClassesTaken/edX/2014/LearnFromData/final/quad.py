"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-29
@summary: Problem 12
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/final2iejhd.pdf
http://courses.csail.mit.edu/6.867/wiki/images/a/a7/Qp-cvxopt.pdf
"""

from cvxopt import matrix
from cvxopt import solvers
import numpy as np

def prob12():
    """
    Output:
    array([[  4.32455505e-09],
    [  7.03703704e-01],
    [  7.03703704e-01],
    [  8.88888891e-01],
    [  2.59259260e-01],
    [  2.59259260e-01],
    [  5.27081494e-10]])
    """
    x, y = _get_data()
    n = len(y)
    P = matrix(_getP(x, y), tc='d')
    q = matrix(-np.ones((n, 1)), tc='d')
    G = matrix(-np.identity(n), tc='d')
    h = matrix(np.zeros((n, 1)), tc='d')
    A = matrix(y.reshape((1, n)), tc='d')
    b = matrix(np.zeros((1, 1)), tc='d')
    return np.array(solvers.qp(P, q, G, h, A, b)['x'])

def _get_data():
    x = np.array([
        [1., 0.],
        [0., 1.],
        [0., -1.],
        [-1., 0.],
        [0., 2.],
        [0., -2.],
        [-2., 0.]])
    y = np.array([-1.0] * 3 + [1.] * 4)
    return x, y

def _getP(x, y):
    return np.outer(y, y) * _kernel(x)

def _kernel(x):
    tmp = 1 + x.dot(x.transpose())
    return tmp * tmp
