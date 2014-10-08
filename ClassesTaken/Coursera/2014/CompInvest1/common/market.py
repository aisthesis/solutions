'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-02
@summary: Utility functions for getting market data
'''

import datetime as dt

import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu

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

def get_values(startdate, enddate, equities, key):
    market_data = get_market_data(startdate, enddate, equities)
    return market_data[key].values

def get_normalized_values(startdate, enddate, equities, key):
    values = get_values(startdate, enddate, equities, key)
    return values / values[0, :]
