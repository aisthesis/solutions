"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-03
@summary: create Bollinger band event studies
http://wiki.quantsoftware.org/index.php?title=CompInvesti_Homework_6
"""

import copy
import datetime as dt
import sys

import numpy as np
import pandas as pd

import QSTK.qstkutil.DataAccess as da

sys.path.append('../common')
import events
import market as mkt

def find_bollinger_breakdowns(equities, mkt_data):
    closes = mkt_data['close']
    eq_cols = [col for col in closes.columns if col != 'SPY']
    sigmas = pd.rolling_std(closes, window=20)
    mus = pd.rolling_mean(closes, window=20)
    boll_vals = (closes - mus) / sigmas
    events = copy.deepcopy(boll_vals)
    events *= np.NAN
    eventdates = events.index
    for equity in eq_cols:
        for i in range(1, len(eventdates)):
            if boll_vals.loc[eventdates[i], equity] < -2.0 and \
                    boll_vals.loc[eventdates[i - 1], equity] >= -2.0 and \
                    boll_vals.loc[eventdates[i], 'SPY'] >= 1.4:
                events.loc[eventdates[i], equity] = 1
    return events

if __name__ == '__main__':
    symbols_code = 'sp5002012'
    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list(symbols_code)
    ls_symbols.append('SPY')
    events.create_study(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31), 
            find_bollinger_breakdowns, ls_symbols, 'BollingerQuizStudy')
    """
    equities = ['AAPL', 'GOOG', 'IBM', 'MSFT', 'SPY']
    startdate = dt.datetime(2010, 11, 20)
    enddate = dt.datetime(2010, 12, 31)
    data = mkt.get_market_data(startdate, enddate, equities)
    find_bollinger_breakdowns(equities, data)
    """
