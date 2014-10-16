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

    def buy(self, equity, n_shares, total_price):
        if not equity in self.equities:
            self.equities[equity] = n_shares
        else:
            self.equities[equity] += n_shares
        self.cash -= total_price

    def sell(self, equity, n_shares, total_price):
        self.buy(equity, -n_shares, -total_price)

    def execute(self, order, prices):
        total_price = prices[order.equity] * order.n_shares
        if order.order_type.upper() == 'BUY':
            self.buy(order.equity, order.n_shares, total_price)
        elif order.order_type.upper() == 'SELL':
            self.sell(order.equity, order.n_shares, total_price)
        else:
            raise ValueError("invalid order type: '{0}'".format(order.order_type)) 

    def value(self, prices):
        ret = self.cash
        for equity, n_shares in self.equities.iteritems():
            ret += prices[equity] * n_shares
        return ret
