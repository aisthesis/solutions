'''
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on January, 23, 2013

@author: Sourabh Bajaj
@contact: sourabhbajaj@gatech.edu
@summary: Event Profiler Tutorial
'''


import copy
import datetime as dt
import math
import sys

import numpy as np
import pandas as pd

import QSTK.qstkstudy.EventProfiler as ep
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu

sys.path.append('../common')
import market as mkt

"""
Accepts a list of symbols along with start and end date
Returns the Event Matrix which is a pandas Datamatrix
Event matrix has the following structure :
    |IBM |GOOG|XOM |MSFT| GS | JP |
(d1)|nan |nan | 1  |nan |nan | 1  |
(d2)|nan | 1  |nan |nan |nan |nan |
(d3)| 1  |nan | 1  |nan | 1  |nan |
(d4)|nan |  1 |nan | 1  |nan |nan |
...................................
...................................
Also, d1 = start date
nan = no information about any event.
1 = status bit(positively confirms the event occurence)
"""

def find_goes_below(symbols, market_data, threshold):
    """
    Event when actual close drops below the given threshold.

    Can be called as parameter to create_study using a specific threshold:
    import functools
    event_finder = functools.partial(events.find_goes_below, threshold=5.0)
    events.create_study(startdate, enddate, event_finder, symbol_code, ofile_name)

    @return     a pandas dataframe marking each instance of the event with 1
                and non-events with NAN
    """
    actual_closes = market_data['actual_close']
    events = copy.deepcopy(actual_closes)
    events = events * np.NAN
    event_dates = actual_closes.index

    for equity in symbols:
        for i in range(1, len(event_dates)):
            if actual_closes[equity].ix[event_dates[i-1]] >= threshold and \
                    actual_closes[equity].ix[event_dates[i]] < threshold:
                events[equity].ix[event_dates[i]] = 1

    return events

def find_abnormal_drops(ls_symbols, d_data):
    ''' Finding the event dataframe '''
    df_close = d_data['close']
    ts_market = df_close['SPY']

    print "Finding Events"

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    # Time stamps for the event range
    ldt_timestamps = df_close.index

    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            # Calculating the returns for this timestamp
            f_symprice_today = df_close[s_sym].ix[ldt_timestamps[i]]
            f_symprice_yest = df_close[s_sym].ix[ldt_timestamps[i - 1]]
            f_marketprice_today = ts_market.ix[ldt_timestamps[i]]
            f_marketprice_yest = ts_market.ix[ldt_timestamps[i - 1]]
            f_symreturn_today = (f_symprice_today / f_symprice_yest) - 1
            f_marketreturn_today = (f_marketprice_today / f_marketprice_yest) - 1

            # Event is found if the symbol is down more then 3% while the
            # market is up more then 2%
            if f_symreturn_today <= -0.03 and f_marketreturn_today >= 0.02:
                df_events[s_sym].ix[ldt_timestamps[i]] = 1

    return df_events


def create_study(dt_start, dt_end, event_finder, symbols_code, ofile_name):
    """
    Outputs a pdf charting average behavior surrounding the given event.
    
    Usage:
    events.create_study(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31),
        events.find_abnormal_drops, 'sp5002012', 'MyEventStudy')

    @type   dt_start:       datetime.datetime
    @param  dt_start:       start date
    @type   dt_end:         datetime.datetime
    @param  dt_end:         end date
    @type   event_finder:   function
    @param  event_finder:   takes a list of equities and a dictionary of market data
                            and outputs a pandas data frame in which events are marked
                            1 and non-events marked as NANs
    @type   symbols_code    string
    @param  symbols_code    code for file containing list of symbols to use
    @type   ofile_name           string
    @param  ofile_name           descriptor for pdf output file. For example, if
                            ofile_name is 'MyEventStudy', the results will be written to 
                            'MyEventStudy.pdf'
    """
    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list(symbols_code)
    ls_symbols.append('SPY')
    print "Getting market data for {0} equities".format(len(ls_symbols))
    d_data = mkt.get_market_data(dt_start, dt_end, ls_symbols)
    print "Market data retrieved"
    df_events = event_finder(ls_symbols, d_data)
    print "Creating Study '{0}.pdf'".format(ofile_name)
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename="{0}.pdf".format(ofile_name), b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')

if __name__ == '__main__':
    create_study(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31), 
            find_abnormal_drops, 'sp5002012', 'MyEventStudy')
