'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-02
@summary: Utility functions for getting market data
'''

import datetime as dt
import math

import numpy as np

import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu

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

def get_market_data(startdate, enddate, equities):
    timestamps = du.getNYSEdays(startdate, enddate, dt.timedelta(hours=16))
    data_acc_obj = da.DataAccess('Yahoo')
    keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    raw_market_data = data_acc_obj.get_data(timestamps, equities, keys)
    market_data = dict(zip(keys, raw_market_data))
    for key in keys:
        market_data[key] = market_data[key].fillna(method='ffill')
        market_data[key] = market_data[key].fillna(method='bfill')
        market_data[key] = market_data[key].fillna(1.0)
    return market_data


def get_normalized_prices(dt_start, dt_end, equities):
    d_data = get_market_data(dt_start, dt_end, equities)
    na_price = d_data['close'].values
    return na_price / na_price[0, :]

def get_daily_returns(normalized_eq_prices, allocation):
    daily_values = normalized_eq_prices.dot(allocation)
    return np.append([0], daily_values[1:] / daily_values[:-1] - 1), daily_values
