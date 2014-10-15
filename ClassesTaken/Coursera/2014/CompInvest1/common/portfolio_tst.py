'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-15
@summary: Portfolio unit tests
Cf. https://docs.python.org/2/library/unittest.html
'''

import unittest

from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):
    
    def setUp(self):
        self.initial_cash = 1000.0
        self.prices = {'foo': 5.0, 'bar': 3.5}
        self.p0 = Portfolio(self.initial_cash)

    def test_ctor(self):
        p0 = Portfolio()
        p1 = Portfolio(self.initial_cash)
        p2 = Portfolio(self.initial_cash, {'foo': 10})
        self.assertAlmostEqual(p0.value(self.prices), 0.0)
        self.assertAlmostEqual(p1.value(self.prices), self.initial_cash)
        self.assertAlmostEqual(p2.value(self.prices), self.initial_cash + 50.0)

    def test_buy(self):
        p1 = Portfolio(self.initial_cash)
        p1.buy('foo', 10, 10.0)
        self.assertEqual(p1.equities['foo'], 10)
        self.assertAlmostEqual(p1.cash, self.initial_cash - 10.0)

    def test_sell(self):
        p2 = Portfolio(self.initial_cash, {'foo': 10})
        p2.sell('foo', 5, 10.0)
        self.assertEqual(p2.equities['foo'], 5)
        self.assertAlmostEqual(p2.cash, self.initial_cash + 10.0)

    def test_value(self):
        p1 = Portfolio(self.initial_cash)
        # prices values 5 shares of foo at 25.0
        p1.buy('foo', 5, 20.0)
        # fair price for bar
        p1.buy('bar', 2, 7.0)
        # net result: profit of 5.0
        self.assertAlmostEqual(p1.value(self.prices), self.initial_cash + 5.0)

if __name__ == '__main__':
    unittest.main()
