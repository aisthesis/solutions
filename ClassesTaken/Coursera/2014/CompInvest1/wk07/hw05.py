'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-28
@summary: Event class for finding anomalous drops
'''

import datetime as dt
import sys

import matplotlib.pyplot as plt
import pandas as pd

sys.path.append('../common')
import market as mkt

def show_bollinger(equity):
    startdate = dt.datetime(2010, 1, 1)
    enddate = dt.datetime(2010, 12, 31)
    closes = mkt.get_market_data(startdate, enddate, [equity])['close']
    plot_bollinger(closes, equity)

def plot_bollinger(price_history, equity):
    plt.figure(figsize=(16.0, 12.0))
    plt.clf()
    plt.subplots_adjust(bottom=0.2)
    plt.plot(price_history.index, price_history.values)
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')
    plt.legend([equity])
    plt.xticks(rotation=45)
    plt.show()

if __name__ == '__main__':
    show_bollinger(*sys.argv[1:])
