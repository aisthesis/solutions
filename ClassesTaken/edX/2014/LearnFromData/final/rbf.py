"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-12-01
@summary: RBF algorithm
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/final2iejhd.pdf
"""

import numpy as np
import scipy.spatial
from scipy.spatial.distance import cdist

class Rbf:
    def __init__(self, mu, gamma):
        self.mu = mu
        self.gamma = gamma

    def getwts(self, x, y):
        phi = self._kernel(x)
        return np.linalg.pinv(phi).dot(y)

    def predict(self, x, wts):
        return self._kernel(x).dot(wts)

    def _kernel(self, x):
        kern = np.empty((x.shape[0], self.mu.shape[0] + 1), dtype=np.float64)
        kern[:, 0] = 1.
        kern[:, 1:] = np.exp(-self.gamma * cdist(x, self.mu, 'sqeuclidean'))
        return kern
