"""
Solution to Freedman, Statistical Models, lab 2, pp. 296f.

Copyright (c) 2014 Marshall Farrier

Distribution and use of this software without prior written permission
of the authors is strictly prohibitied and will be prosecuted to
the full extent of the law.

by

Marshall Farrier, marshalldfarrier@gmail.com
"""

import numpy as np

def get_matrices():
    x = np.arange(-2, 10).reshape((4, 3))
    x[0, 0] = 1
    x[0, 2] = 1
    return x, np.arange(1, 5).reshape((4, 1))

def prob02():
    """
    X'X
    [[ 67  77  91]
     [ 77  94 107]
     [ 91 107 127]]
    X'Y
    [[43]
     [50]
     [61]]
    det(X'X)
    864.0
    rank X
    3
    rank X'X
    3
    """
    x, y = get_matrices()
    print("X'X")
    print(x.transpose().dot(x))
    print("X'Y")
    print(x.transpose().dot(y))
    print("det(X'X)")
    print(np.linalg.det(x.transpose().dot(x)))
    print("rank X")
    print(np.linalg.matrix_rank(x))
    print("rank X'X")
    print(np.linalg.matrix_rank(x.transpose().dot(x)))

def prob03():
    """
    [[ 0.56597222 -0.04861111 -0.36458333]
     [-0.04861111  0.26388889 -0.1875    ]
     [-0.36458333 -0.1875      0.42708333]]
    """
    x = get_matrices()[0]
    print(np.linalg.inv(x.transpose().dot(x)))

def prob04():
    """
    [[-0.33333333]
     [-0.33333333]
     [ 1.        ]]
    """
    x, y = get_matrices()
    print(np.linalg.inv(x.transpose().dot(x)).dot(x.transpose()).dot(y))

def prob05():
    """
    trace AX: 411
    trace XA: 411
    """
    x = get_matrices()[0]
    a = np.array([
        [1, 3, 5, 7],
        [-1, 2, 9, -3],
        [6, 3, 0, 33]])
    print("trace AX: {0}".format(a.dot(x).trace()))
    print("trace XA: {0}".format(x.dot(a).trace()))
