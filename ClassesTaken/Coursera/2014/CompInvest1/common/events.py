"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-03
@summary: create event studies
"""

import QSTK.qstkstudy.EventProfiler as ep

import market as mkt

"""
Accepts a list of symbols along with start and end date
Returns the Event Matrix which is a pandas Datamatrix
Event matrix has the following structure :
    |IBM |GOOG|XOM |MSFT| GS | JP |
(d1)|nan |nan | 1  |nan |nan | 1  |
(d2)|nan | 1  |nan |nan |nan |nan |
(d3)| 1  |nan | 1  |nan | 1  |nan |
(d4)|nan |  1 |nan | 1  |nan |nan |
...................................
...................................
Also, d1 = start date
nan = no information about any event.
1 = status bit(positively confirms the event occurence)
"""

def create_study(dt_start, dt_end, event_finder, ls_symbols, ofile_name):
    """
    Create a pdf charting average behavior surrounding the given event.
    
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
    @type   ofile_name           string
    @param  ofile_name           descriptor for pdf output file. For example, if
                            ofile_name is 'MyEventStudy', the results will be written to 
                            'MyEventStudy.pdf'
    @return: d_data, df_events
    d_data is a dictionary mapping strings like 'open', 'high', 'close', etc. to pandas 
    DataFrames containing the data retrieved
    df_events is a pandas DataFrame as described above containing 1s where the event occurs
    and NANs elsewhere
    """
    print "Getting market data for {0} equities".format(len(ls_symbols))
    d_data = mkt.get_market_data(dt_start, dt_end, ls_symbols)
    print "Market data retrieved"
    df_events = event_finder(ls_symbols, d_data)
    print "Creating Study '{0}.pdf'".format(ofile_name)
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename="{0}.pdf".format(ofile_name), b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')
    return d_data, df_events
