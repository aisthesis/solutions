'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-22
@summary: Event class for finding anomalous drops
'''

import datetime as dt
import sys

import QSTK.qstkstudy.EventProfiler as ep
import QSTK.qstkutil.DataAccess as da

sys.path.append('../common')
import market as mkt
import order

from anomalous_drop_finder import AnomalousDropFinder

def create_study(dt_start, dt_end, event_finder, symbols_code):
    """
    Outputs a pdf charting average behavior surrounding the given event.
    
    Usage:
    events.create_study(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31),
        events.find_abnormal_drops, 'sp5002012', 'MyEventStudy')

    @type   dt_start:       datetime.datetime
    @param  dt_start:       start date
    @type   dt_end:         datetime.datetime
    @param  dt_end:         end date
    @type   event_finder:   function
    @param  event_finder:   takes a list of equities and a dictionary of market data
                            and outputs a pandas data frame in which events are marked
                            1 and non-events marked as NANs
    @type   symbols_code    string
    @param  symbols_code    code for file containing list of symbols to use
    """
    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list(symbols_code)
    ls_symbols.append('SPY')
    print "Getting market data for {0} equities".format(len(ls_symbols))
    d_data = mkt.get_market_data(dt_start, dt_end, ls_symbols)
    print "Market data retrieved"
    event_finder.data = d_data['actual_close']
    event_finder.equities = ls_symbols
    event_finder.find()
    """
    print "Creating Study"
    ep.eventprofiler(event_finder.events, d_data, i_lookback=20, i_lookforward=20,
                s_filename="study.pdf", b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')
    """
    daily_values = order.get_daily_values(50000, event_finder.orders)
    print daily_values

if __name__ == '__main__':
    create_study(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31), 
            AnomalousDropFinder(), 'sp5002012')
