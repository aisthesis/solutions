'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-02
@summary: Generic random linear function
'''

import random

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class RandomPoint(Point):
    def __init__(self):
        super(RandomPoint, self).__init__(random.uniform(-1, 1), random.uniform(-1, 1))

class BinaryLinear:
    def __init__(self):
        self.p1 = RandomPoint()
        self.p2 = RandomPoint()
        self.side = random.randint(0, 1)
        self.slope = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        self.intercept = self.p1.y - self.slope * self.p1.x

    def label(self, x, y):
        if self.side:
            return 1 if y > self.slope * x + self.intercept else -1 
        return 1 if y < self.slope * x + self.intercept else -1
