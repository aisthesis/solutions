'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-02
@summary: Generic linear function
'''

import random

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
        self.slope = (self.y1 - self.y2) / (self.x1 - self.x2)
        self.intercept = self.y1 - self.slope * self.x1

    def label(self, x, y, valiftrue=1, valiffalse=-1):
        if self.side:
            return valiftrue if y > self.slope * x + self.intercept else valiffalse 
        return valiftrue if y < self.slope * x + self.intercept else valiffalse

def get_random_points(n):
    points = [(0., 0.)] * n
    for i in range(n):
        points[i] = (random.uniform(-1, 1), random.uniform(-1, 1))
    return points
