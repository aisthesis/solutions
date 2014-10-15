'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-14
@summary: hw03 for computational investing, market simulator
'''

import datetime as dt
import sys

#import QSTK.qstkutil.DataAccess as da
#import QSTK.qstkutil.qsdateutil as du
#import QSTK.qstkutil.tsutil as tsu

sys.path.append("../common")
import order

def get_daily_values(starting_cash, infile, outfile):
    orders = order.get(infile)
    list.sort(orders, key=lambda order: order.date)
    return orders

