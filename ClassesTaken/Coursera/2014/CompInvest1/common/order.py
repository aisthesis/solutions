'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-14
@summary: Order class
'''

import csv
import datetime as dt

class Order(object):
    def __init__(self, order_date, equity, order_type, n_shares):
        self.date = order_date
        self.equity = equity
        self.order_type = order_type
        self.n_shares = n_shares

def get(infile):
    """
    Return a list of orders from a csv file like:
    2008, 12, 3, AAPL, BUY, 130
    2008, 12, 8, AAPL, SELL, 130
    2008, 12, 5, IBM, BUY, 50
    """
    orders = []
    with open(infile, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        for row in filereader:
            orders.append(Order(dt.datetime(int(row[0]), int(row[1]), int(row[2])), 
                row[3].strip(), row[4].strip(), int(row[5])))
    return orders
