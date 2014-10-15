'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-14
@summary: Order class
'''

import datetime as dt

class Order(object):
    def __init__(self, order_date, equity, order_type, n_shares):
        self.date = order_date
        self.equity = equity
        self.order_type = order_type
        self.n_shares = n_shares
