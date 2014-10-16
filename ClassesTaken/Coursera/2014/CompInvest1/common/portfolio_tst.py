'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-15
@summary: Portfolio unit tests
Cf. https://docs.python.org/2/library/unittest.html
'''

import datetime as dt
import unittest

from order import Order
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

    def test_execute(self):
        p2 = Portfolio(self.initial_cash, {'foo': 10})
        order_date = dt.datetime(2000, 1, 1)
        expected_cash = self.initial_cash
        o1 = Order(order_date, 'bar', 'BUY', 2)
        o2 = Order(order_date, 'foo', 'SELL', 5)
        o3 = Order(order_date, 'foo', 'BLAH', 6)
        # execute buy order
        p2.execute(o1, self.prices)
        expected_cash -= 7.0
        self.assertEqual(p2.equities['bar'], 2)
        self.assertAlmostEqual(p2.cash, expected_cash)
        # execute sell order
        p2.execute(o2, self.prices)
        expected_cash += 25.0
        self.assertEqual(p2.equities['foo'], 5)
        self.assertAlmostEqual(p2.cash, expected_cash)
        # try to execute invalid order type
        with self.assertRaises(ValueError):
            p2.execute(o3, self.prices)
        

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
