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

def show_bollinger(equity, k=2.0):
    startdate = dt.datetime(2010, 1, 1)
    enddate = dt.datetime(2010, 12, 31)
    data = get_data(equity, startdate, enddate, k)
    plot_bollinger(data, equity)

def get_data(equity, startdate, enddate, k):
    data = mkt.get_market_data(startdate, enddate, [equity])['close']
    sigmas = pd.rolling_std(data, window=20).values.flatten()
    data.loc[:, 'SMA'] = pd.rolling_mean(data, window=20).values.flatten()
    upper_band = data.loc[:, 'SMA'].values + k * sigmas
    lower_band = data.loc[:, 'SMA'].values - k * sigmas
    data.loc[:, 'upper'] = upper_band
    data.loc[:, 'lower'] = lower_band
    data.loc[:, 'boll_val'] = (data.loc[:, equity].values.flatten() - \
            data.loc[:, 'SMA'].values.flatten()) / sigmas
    # For purposes of quiz
    print data.ix[90:100, 'boll_val']
    return data

def plot_bollinger(price_history, equity):
    plt.figure(figsize=(16.0, 12.0))
    plt.clf()
    plt.subplots_adjust(bottom=0.2)
    # plot equity with bands
    ax1 = plt.subplot(2, 1, 1)
    lines = plt.plot(price_history.index, price_history.iloc[:, 0:2].values)
    lines[1].set_color('r')
    plt.fill_between(price_history.index, price_history.loc[:, 'upper'].values,
            price_history.loc[:, 'lower'].values, facecolor='gray', alpha=0.5)
    plt.ylabel('Adjusted Close')
    plt.legend([equity, 'SMA'])
    plt.setp(ax1.get_xticklabels(), visible=False)

    # plot Bollinger feature
    plt.subplot(2, 1, 2, sharex=ax1)
    plt.plot(price_history.index, price_history.loc[:, 'boll_val'].values)
    plt.fill_between(price_history.index, 1.0, -1.0, facecolor='gray', alpha=0.5)
    plt.ylabel('Bollinger Feature')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == '__main__':
    show_bollinger(*sys.argv[1:], k=1.0)
