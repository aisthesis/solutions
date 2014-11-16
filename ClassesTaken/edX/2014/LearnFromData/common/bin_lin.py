'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-02
@summary: Generic linear function
'''

import random

import numpy as np

class BinaryLinear:
    def __init__(self, *args):
        if args:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]
            self.side = args[4]
        else:
            self.x1 = random.uniform(-1, 1)
            self.y1 = random.uniform(-1, 1)
            self.x2 = random.uniform(-1, 1)
            self.y2 = random.uniform(-1, 1)
            self.side = random.randint(0, 1)
        slope = (self.y1 - self.y2) / (self.x1 - self.x2)
        intercept = self.y1 - slope * self.x1
        self.wts = np.array((intercept, slope, -1.0)).reshape((3, 1))
        if self.side:
            self.wts = -1.0 * self.wts

    def labels(self, features):
        return np.sign(features.dot(self.wts))

def get_random_points(n):
    """ return a feature set of size n """
    features = np.ones((n, 3))
    features[:, 1:] = np.random.rand(n, 2) * 2.0 - 1.0
    return features
