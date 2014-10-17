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
#import market

def show_analysis(infile):
    price_history = get_price_history(infile)
    plot_price_history(price_history)

def get_price_history(infile):
    price_history = pd.read_csv("output/{0}".format(infile), header=None, index_col=0, names=['Value'],
            parse_dates=True, date_parser=get_dt)
    return price_history

def get_dt(date_string):
    return dt.datetime.strptime(date_string, '%Y-%m-%d')

def plot_price_history(price_history):
    plt.figure(figsize=(10.0, 8.0))
    plt.clf()
    plt.subplots_adjust(bottom=0.2)
    plt.plot(price_history.index, price_history.values)
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')
    plt.legend(['Portfolio'])
    plt.xticks(rotation=45)
    plt.show()

if __name__ == '__main__':
    show_analysis(*sys.argv[1:])
