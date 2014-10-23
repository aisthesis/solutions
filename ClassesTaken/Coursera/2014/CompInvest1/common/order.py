'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-14
@summary: Order class
'''

import csv
import datetime as dt

import numpy as np
import pandas as pd

import market as mkt
from portfolio import Portfolio
import utils

class Order(object):
    def __init__(self, order_date, equity, order_type, n_shares):
        self.date = order_date
        self.equity = equity
        self.order_type = order_type
        self.n_shares = n_shares

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.date.year, self.date.month, self.date.day,
                self.equity, self.order_type, self.n_shares)

def get(infile):
    """
    Return a list of orders from a csv file like:
    2008, 12, 3, AAPL, BUY, 130
    2008, 12, 8, AAPL, SELL, 130
    2008, 12, 5, IBM, BUY, 50
    """
    orders = []
    with open(infile, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        for row in filereader:
            # TODO use date rather than datetime here
            orders.append(Order(dt.datetime(int(row[0]), int(row[1]), int(row[2])), 
                row[3].strip(), row[4].strip(), int(row[5])))
    return orders

def get_daily_values(starting_cash, orders):
    """
    return a pandas DataFrame indexed by date and with sole field 'Value', which is
    the portfolio value by day resulting from processing the given orders
    """
    # sort orders by date
    list.sort(orders, key=lambda order: order.date)
    startdate, enddate = get_date_range(orders)
    equities = get_equities(orders)
    closes = mkt.get_market_data(startdate, enddate + dt.timedelta(days=1), equities)['close']
    trading_days = closes.index

    # set up pandas DataFrame with all values equal to starting_cash
    n_rows = len(trading_days)
    initial_values = np.empty((n_rows, 1))
    initial_values.fill(starting_cash)
    daily_values = pd.DataFrame(initial_values, index=trading_days, columns=['Value'])

    # initialize portfolio and prices dictionary
    portfolio = Portfolio(float(starting_cash))
    prices = dict(zip(equities, [0.0] * len(equities)))

    # get daily values
    order_ix = 0
    for trading_day in trading_days:
        
        # update prices
        for equity in equities:
            prices[equity] = closes.loc[trading_day, equity]

        # execute orders
        while order_ix < len(orders) and trading_day.date() == orders[order_ix].date.date():
            portfolio.execute(orders[order_ix], prices)
            order_ix += 1
        daily_values.loc[trading_day, 'Value'] = portfolio.value(prices)

    return daily_values


def get_date_range(orders):
    """ return start and enddate from a sorted list of orders """
    return orders[0].date, orders[-1].date

def get_equities(orders):
    """ return a list of all equities for which there are orders """
    return utils.unique([order.equity for order in orders])
