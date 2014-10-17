'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-16
@summary: Functions for getting performance data
'''

import math

import numpy as np

def get_daily_returns(prices):
    """
    @param prices: 2D numpy array whose columns represent a sequence of prices
    @return: an array of the same size representing the price gain relative
    to previous entry. 0 for the first row.
    """
    n_rows, n_cols = np.shape(prices)
    return np.vstack((np.zeros((1, n_cols)), prices[1:, :] / prices[:-1, :] - 1))

def get_performance(prices):
    """
    Return volatility, average daily return, Sharpe ratio and cumulative return
    for each column in the prices array.
    @param prices: 2D numpy array
    """
    daily_returns = get_daily_returns(prices)
    volatility = np.std(daily_returns, axis=0)
    ave_return = np.average(daily_returns, axis=0)
    sharpe = math.sqrt(252) * ave_return / volatility
    cumulative = prices[-1, :] / prices[0, :]

    return volatility, ave_return, sharpe, cumulative
