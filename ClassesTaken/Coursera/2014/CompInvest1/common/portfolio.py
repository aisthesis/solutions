'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-14
@summary: Portfolio class
'''

class Portfolio(object):
    def __init__(self, cash=0.0, equities={}):
        self.cash = cash
        self.equities = dict(equities)

    def buy(equity, n_shares, total_price):
        if not equity in self.equities:
            self.equities[equity] = n_shares
        else:
            self.equities[equity] += n_shares
        self.cash -= total_price

    def sell(equity, n_shares, total_price):
        self.buy(equity, -n_shares, -total_price)

    def value(prices):
        ret = self.cash
        for equity, n_shares in self.equities.iteritems():
            ret += prices[equity] * n_shares
        return ret
