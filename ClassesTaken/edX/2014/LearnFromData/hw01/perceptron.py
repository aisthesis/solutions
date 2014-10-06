'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-02
@summary: Homework 1: Perceptron algorithm
'''

import random

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class RandomPoint(Point):
    def __init__(self):
        random.seed()
        super(RandomPoint, self).__init__(random.uniform(-1, 1), random.uniform(-1, 1))

class PerceptronTester:
    def __init__(self):
        self.p1 = RandomPoint()
        self.p2 = RandomPoint()
        self.side = random.randint(0, 1)
        self.slope = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        self.intercept = self.p1.y - self.slope * self.p1.x

    def label(self, point):
        if self.side:
            return 1 if point.y > self.slope * point.x + self.intercept else -1 
        return 1 if point.y < self.slope * point.x + self.intercept else -1

    def learn(self, points, max_iter=64):
        iterations = 0;
        i = 0;
        weights = [0.0, 0.0, 0.0]
        tmp = 0
        while i < len(points) and iterations < max_iter:
            tmp = self.label(points[i])
            if get_label(weights, points[i]) == tmp:
                # correctly classified, move on
                i += 1
            else:
                # incorrect, so adjust weights and try again
                iterations += 1
                weights[0] += tmp
                weights[1] += tmp * points[i].x
                weights[2] += tmp * points[i].y
                i = 0
        return iterations, weights

def get_label(weights, point):
    return 1 if weights[0] + weights[1] * point.x + weights[2] * point.y > 0 else -1

def get_points(n):
    points = [Point()] * n
    for i in range(n):
        points[i] = RandomPoint()
    return points

def test_convergence(n_points, n_trials, test_set_size=64, max_iter=256):
    """
    Returns average iterations and estimate of average error pct
    """
    tot_iterations = 0.0
    tot_errors = 0.0
    iterations = 0
    weights = [0.0] * 3
    points = [Point()] * n_points
    test_points = [Point()] * test_set_size
    for i in range(n_trials):
        tester = PerceptronTester()
        points = get_points(n_points)
        iterations, weights = tester.learn(points, max_iter)
        test_points = get_points(test_set_size)
        for point in test_points:
            if get_label(weights, point) != tester.label(point):
                tot_errors += 1
        tot_iterations += iterations
    average_iterations = tot_iterations / n_trials
    ave_errors = tot_errors / (n_trials * test_set_size)
    return average_iterations, ave_errors

