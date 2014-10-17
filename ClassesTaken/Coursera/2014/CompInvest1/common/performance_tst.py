'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-16
@summary: Test performance functions
'''

import numpy as np
import unittest

import performance as perf

class TestPerfFunctions(unittest.TestCase):

    def setUp(self):
        pricesarr = [[1.0, 1.0],
                [2.0, 0.5],
                [4.0, 0.25],
                [8.0, 0.125]]
        self.npprices = np.array(pricesarr)

    def test_get_daily_returns(self):
        daily_returns = perf.get_daily_returns(self.npprices)
        self.assertAlmostEqual(daily_returns[0, 0], 0.0)
        self.assertAlmostEqual(daily_returns[0, 1], 0.0)
        for i in range(1, 4):
            self.assertAlmostEqual(daily_returns[i, 0], 1.0)
            self.assertAlmostEqual(daily_returns[i, 1], -0.5)

    def test_get_performance(self):
        vol, ave, sharpe, cumulative = perf.get_performance(self.npprices)
        self.assertAlmostEqual(vol[0], 0.4330, places=4)
        self.assertAlmostEqual(vol[1], 0.2165, places=4)
        self.assertAlmostEqual(ave[0], 0.75)
        self.assertAlmostEqual(ave[1], -0.375)
        self.assertAlmostEqual(sharpe[0], 27.495, places=3)
        self.assertAlmostEqual(sharpe[1], -27.495, places=3)
        self.assertAlmostEqual(cumulative[0], 8.0)
        self.assertAlmostEqual(cumulative[1], 0.125)

if __name__ == '__main__':
    unittest.main()
