'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-16
@summary: hw03 for computational investing, analysis tool
http://wiki.quantsoftware.org/index.php?title=CompInvesti_Homework_3
'''

import datetime as dt
import sys

import numpy as np
import pandas as pd

sys.path.append("../common")
#import market

def get_price_history(infile):
    price_history = pd.read_csv("output/{0}".format(infile), header=None, index_col=0, names=['Value'],
            parse_dates=True, date_parser=get_dt)
    print price_history.to_csv(date_format='%Y%m%d')
    return price_history

def get_dt(date_string):
    return dt.datetime.strptime(date_string, '%Y-%m-%d')

def write_daily_values(starting_cash, infile, outfile):
    daily_values = get_daily_values(starting_cash, infile)
    daily_values.to_csv(header=False, float_format='%0.2f', date_format='%Y-%m-%d',
            path_or_buf="output/{0}".format(outfile))


def get_date_range(orders):
    """ return startdate and enddate given sorted orders """
    return orders[0].date, orders[-1].date + dt.timedelta(days=1)

def get_equities(orders):
    """ return a list of all equities for which orders are to be placed """
    return unique([order.equity for order in orders])

def unique(items):
    """
    return a list with no duplicates
    Cf. http://stackoverflow.com/questions/89178
    """
    seen = set()
    seen_add = seen.add
    return [item for item in items if item not in seen and not seen_add(item)]

if __name__ == '__main__':
    get_price_history(*sys.argv[1:])
