"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-03
@summary: create event studies
"""

import copy
import datetime as dt
import sys

import numpy as np

import QSTK.qstkutil.DataAccess as da

sys.path.append('../common')
import events

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

def find_big_diff_from_sp(equities, market_data, threshold):
    """
    Event if equity move exceeds threshold. If threshold is positive,
    equity must go up more than S&P by that amount. If it is negative,
    equity must go down more than S&P by that amount.
    Can be called as parameter to create_study using a specific threshold:
    import functools
    event_finder = functools.partial(events.find_big_diff_from_sp, threshold=-0.05)
    events.create_study(startdate, enddate, event_finder, symbol_code, ofile_name)
    """
    closes = market_data['close']
    sp500 = closes['SPY']
    events = copy.deepcopy(closes)
    events = events * np.NAN
    close_dates = closes.index
    if threshold > 0:
        fill_above_sp(events, equities, close_dates, closes, sp500, threshold)
    else:
        fill_below_sp(events, equities, close_dates, closes, sp500, threshold)
    return events

def fill_above_sp(events, equities, dates, values, sp500, threshold):
    sp_gain = 0.0
    eq_gain = 0.0
    for equity in equities:
        for i in range(1, len(dates)):
            sp_gain = sp500.ix[dates[i]] / sp500.ix[dates[i-1]]
            eq_gain = values[equity].ix[dates[i]] / values[equity].ix[dates[i-1]]
            if eq_gain - sp_gain >= threshold:
                events[equity].ix[dates[i]] = 1

def fill_below_sp(events, equities, dates, values, sp500, threshold):
    sp_gain = 0.0
    eq_gain = 0.0
    for equity in equities:
        for i in range(1, len(dates)):
            sp_gain = sp500.ix[dates[i]] / sp500.ix[dates[i-1]]
            eq_gain = values[equity].ix[dates[i]] / values[equity].ix[dates[i-1]]
            if eq_gain - sp_gain <= threshold:
                events[equity].ix[dates[i]] = 1

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

if __name__ == '__main__':
    symbols_code = 'sp5002012'
    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list(symbols_code)
    ls_symbols.append('SPY')
    events.create_study(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31), 
            find_abnormal_drops, ls_symbols, 'MyEventStudy')
