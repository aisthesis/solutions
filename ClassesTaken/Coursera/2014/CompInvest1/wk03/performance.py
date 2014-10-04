'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-02
@summary: Homework 1 (simulate function)
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import numpy as np
import math

def simulate(dt_start, dt_end, equities, allocation):
    normalized_prices = get_normalized_prices(dt_start, dt_end, equities)
    return get_performance(normalized_prices, allocation)

def get_performance(normalized_prices, allocation):
    daily_returns, daily_values = get_daily_returns(normalized_prices, allocation)

    volatility = np.std(daily_returns)
    ave_daily_return = np.average(daily_returns)
    sharpe = math.sqrt(252) * ave_daily_return / volatility
    cumulative_return = daily_values[-1]

    return volatility, ave_daily_return, sharpe, cumulative_return

def optimize_benchmark(startdate, enddate, equities):
    t0 = dt.datetime.now()
    allocation, sharpe = optimize(startdate, enddate, equities)
    t1 = dt.datetime.now()
    return (t1 - t0).total_seconds(), allocation, sharpe

def optimize(startdate, enddate, equities):
    normalized_prices = get_normalized_prices(startdate, enddate, equities)
    n_equities = len(equities)
    best_alloc = np.zeros(n_equities)
    partial_alloc = np.zeros(n_equities)
    best_sharpe = 0.0
    best_sharpe = optimize_rec(normalized_prices, partial_alloc, 0, n_equities, 0, best_alloc, best_sharpe)
    return best_alloc, best_sharpe

def optimize_rec(normalized_prices, partial_alloc, ix, n_equities, allocated, best_alloc, best_sharpe):
    # The value for allocated ranges from 0 to 10 as integer to avoid various complications
    # base cases: last index and full allocation
    if ix == n_equities - 1:
        partial_alloc[ix] = 1.0 - allocated / 10.0
        allocated = 10
    if allocated == 10:
        possible_sharpe = get_performance(normalized_prices, partial_alloc)[2]
        if possible_sharpe > best_sharpe:
            best_sharpe = possible_sharpe
            best_alloc[:] = partial_alloc
        return best_sharpe

    to_allocate = 10 - allocated
    for i in range(to_allocate + 1):
        partial_alloc[(ix + 1):] = 0.0
        partial_alloc[ix] = i / 10.0
        best_sharpe = optimize_rec(normalized_prices, partial_alloc, ix + 1, 
                n_equities, allocated + i, best_alloc, best_sharpe)
    return best_sharpe

def get_normalized_prices(dt_start, dt_end, equities):
    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
                    
    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, equities, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Filling the data for NAN
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)

    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values
    return na_price / na_price[0, :]

def get_daily_returns(normalized_eq_prices, allocation):
    daily_values = normalized_eq_prices.dot(allocation)
    return np.append([0], daily_values[1:] / daily_values[:-1] - 1), daily_values
