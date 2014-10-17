'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-16
@summary: hw03 for computational investing, analysis tool
http://wiki.quantsoftware.org/index.php?title=CompInvesti_Homework_3
'''

import datetime as dt
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.append("../common")
import market as mkt
import performance as perf

def show_analysis(infile, ref_eq):
    price_history = get_price_history(infile)
    add_reference_data(price_history, ref_eq)
    print_analysis(price_history, ref_eq)
    plot_price_history(price_history, ref_eq)

def add_reference_data(price_history, ref_eq):
    startdate, enddate = get_date_range(price_history)
    ref_history = mkt.get_dataframe(startdate, enddate, [ref_eq], 'close')
    initial_pf_val = price_history.values[0, 0]
    normalization_factor = float(initial_pf_val) / ref_history.values[0, 0]
    ref_history.loc[:, ref_eq] *= normalization_factor
    price_history.loc[:, ref_eq] = ref_history.values.flatten()

def get_date_range(price_history):
    return price_history.index[0], price_history.index[-1] + dt.timedelta(days=1)

def print_analysis(price_history, ref_eq):
    price_dates = price_history.index
    prices = price_history.values
    vol, ave_ret, sharpe, cumulative = perf.get_performance(prices)
    print "\nDetails of the performance of the portfolio:"
    print "\nData range: {0} to {1}".format(price_dates[0].strftime('%Y-%m-%d'),
            price_dates[-1].strftime('%Y-%m-%d'))
    print "Initial value: {0}".format(prices[0, 0])
    print "Final value: {0}".format(prices[-1, 0])
    print "\nSharpe ratio of fund: {0}".format(sharpe[0])
    print "Sharpe ratio of {0}: {1}".format(ref_eq, sharpe[1])
    print "\nTotal return of fund: {0}".format(cumulative[0])
    print "Total return of {0}: {1}".format(ref_eq, cumulative[1])
    print "\nStandard deviation of fund: {0}".format(vol[0])
    print "Standard deviation of {0}: {1}".format(ref_eq, vol[1])
    print "\nAverage daily return of fund: {0}".format(ave_ret[0])
    print "Average daily return of {0}: {1}".format(ref_eq, ave_ret[1])

def get_price_history(infile):
    price_history = pd.read_csv("output/{0}".format(infile), header=None, index_col=0, names=['Value'],
            parse_dates=True, date_parser=get_dt)
    return price_history

def get_dt(date_string):
    return dt.datetime.strptime(date_string, '%Y-%m-%d')

def plot_price_history(price_history, ref_eq):
    plt.figure(figsize=(16.0, 12.0))
    plt.clf()
    plt.subplots_adjust(bottom=0.2)
    plt.plot(price_history.index, price_history.values)
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')
    plt.legend(['Portfolio', ref_eq])
    plt.xticks(rotation=45)
    plt.show()

if __name__ == '__main__':
    show_analysis(*sys.argv[1:])
