'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-21
@summary: abstract Event class and related methods

Event matrix has the following structure :
    |IBM |GOOG|XOM |MSFT| GS | JP |
(d1)|nan |nan | 1  |nan |nan | 1  |
(d2)|nan | 1  |nan |nan |nan |nan |
(d3)| 1  |nan | 1  |nan | 1  |nan |
(d4)|nan |  1 |nan | 1  |nan |nan |
...................................
...................................
d1 = start date
nan = no information about any event.
1 = status bit(positively confirms the event occurence)
"""
'''

from abc import ABCMeta, abstractmethod
import copy

import numpy as np

class EventFinder(object):
    __metaclass__ = ABCMeta

    def __init__(self, equities, data):
        """
        @type data: pandas dataframe containing all necessary information
        to define the event
        """
        self.equities = equities
        self.data = data
        self.events = copy.deepcopy(self.data) * np.NAN
        self.orders = []
        self._search_completed = False

    @abstractmethod
    def find(self):
        print "Finding events"

    @abstractmethod
    def add_orders(self, equity, event_ix):
        pass

    def update_event_tbl(self, equity, event_ix):
        """ add individual event to table """
        self.events[equity].ix[self.data.index[event_ix]] = 1
