'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-21
@summary: abstract Event class and related methods
'''

from abc import ABCMeta, abstractmethod
import copy

import numpy as np

class EventFinder:
    __metaclass__ = ABCMeta

    def __init__(self, equities, data):
        """
        @type data: pandas dataframe containing all necessary information
        to define the event
        """
        self.equities = equities
        self.data = data
        self.events = copy.deepcopy(self.data) * np.NAN
        self._search_completed = False

    @abstractmethod
    def get_orders(self):
        return []

    @abstractmethod
    def get_events(self):
        return self.events
