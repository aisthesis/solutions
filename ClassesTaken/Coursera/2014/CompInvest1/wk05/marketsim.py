'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-14
@summary: hw03 for computational investing, market simulator
'''

import datetime as dt
import sys

import numpy as np
import pandas as pd

import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu

sys.path.append("../common")
import market
import order
from portfolio import Portfolio

def get_daily_values(starting_cash, infile, outfile):
    orders = order.get(infile)
    list.sort(orders, key=lambda order: order.date)
    startdate, enddate = get_date_range(orders)
    equities = get_equities(orders)
    market_data = market.get_market_data(startdate, enddate, equities)
    closes = market_data['close']
    timestamps = closes.index

    # set up pandas DataFrame with all values equal to starting_cash
    n_rows = len(timestamps)
    initial_values = np.empty((n_rows, 1))
    initial_values.fill(starting_cash)
    daily_values = pd.DataFrame(initial_values, index=timestamps, columns=['val'])
    
    # initialize portfolio
    portfolio = Portfolio(starting_cash)
    print daily_values
    return daily_values

def get_date_range(orders):
    """ return startdate and enddate given sorted orders """
    return orders[0].date, orders[-1].date

def get_equities(orders):
    """ return a list of all equities for which orders are to be placed """
    return unique([order.equity for order in orders])

def unique(items):
    """
    return a list with no duplicates
    Cf. http://stackoverflow.com/questions/89178
    """
    seen = set()
    seen_add = seen.add
    return [item for item in items if item not in seen and not seen_add(item)]

if __name__ == '__main__':
    get_daily_values(*sys.argv[1:])
