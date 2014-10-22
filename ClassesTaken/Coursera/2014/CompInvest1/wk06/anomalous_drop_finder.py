'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-22
@summary: Event class for finding anomalous drops
'''

import sys

sys.path.append('../common')
from event_finder import EventFinder
from order import Order

class AnomalousDropFinder(EventFinder):
    def find(self):
        super(AnomalousDropEvent, self).find()
        ref_data = self.data['SPY']
        data_dates = self.data.index
        eq_price_today = eq_price_yest = mkt_price_today = mkt_price_yest = 0.0
        eq_ret = mkt_ret = 0.0

        for equity in self.equities:
            for i in range(1, len(data_dates)):
                eq_price_today = self.data[equity].ix[data_dates[i]]
                eq_price_yest = self.data[equity].ix[data_dates[i - 1]]
                mkt_price_today = ref_data.ix[data_dates[i]]
                mkt_price_yest = ref_data.ix[data_dates[i - 1]]
                eq_ret = (eq_price_today / eq_price_yest) - 1.0
                mkt_ret = (mkt_price_today / mkt_price_yest) - 1.0
                if eq_ret <= -0.03 and mkt_ret >= 0.02:
                    self.update_event_tbl(equity, i)
                    self.add_orders(equity, i)

    def add_orders(self, equity, event_ix):
        data_dates = self.data.index
        # do nothing if event is on last day of data
        if event_ix < len(data_dates) - 1: return
        self.orders.append(Order(data_dates[event_ix], equity, "BUY", 100))
        sell_ix = event_ix + 5
        if sell_ix >= len(data_dates): sell_ix = len(data_dates) - 1
        self.orders.append(Order(data_dates[sell_ix], equity, "SELL", 100))
