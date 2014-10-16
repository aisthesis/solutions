'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-15
@summary: Unit tests for market.py
'''

import datetime as dt
import unittest

import market as mkt

class TestMarketFunctions(unittest.TestCase):

    def setUp(self):
        self.startdate = dt.datetime(2008, 1, 1)
        self.enddate = dt.datetime(2008, 1, 31)
        self.equities = ['AAPL', 'JNJ']

    def test_get_market_data(self):
        """
        market_data is a dictionary whose keys are 'open', 'high', 'low', 'close', 'volume'
        and 'actual_close' and whose values are a pandas DataFrame with dates as index
        and equities ('AAPL' etc.) as columns
        """
        market_data = mkt.get_market_data(self.startdate, self.enddate, self.equities)
        opens = market_data['open']
        actual_start = opens.index[0]
        self.assertEqual(actual_start.year, 2008)
        self.assertEqual(actual_start.month, 1)
        self.assertEqual(actual_start.day, 2)
        self.assertAlmostEqual(opens.loc[actual_start, 'AAPL'], 199.27)
        self.assertAlmostEqual(opens.loc[actual_start, 'JNJ'], 66.56)

    def test_get_values(self):
        """
        get_values returns a 2D array whose rows are the respective values for each
        equity on a given date
        """
        values = mkt.get_values(self.startdate, self.enddate,
                self.equities, 'actual_close')
        self.assertAlmostEqual(values[0, 0], 194.84)
        self.assertAlmostEqual(values[-1, 1], 62.18) 

    def test_get_normalized_values(self):
        values = mkt.get_normalized_values(self.startdate, self.enddate,
                self.equities, 'high')
        self.assertAlmostEqual(values[0, 0], 1.0)
        self.assertAlmostEqual(values[0, 1], 1.0)
        self.assertAlmostEqual(values[-1, 0], 0.68, places=2)
        self.assertAlmostEqual(values[-1, 1], 0.94, places=2)

if __name__ == '__main__':
    unittest.main()
