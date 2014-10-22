'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-21
@summary: utility functions
'''

def unique(items):
    """
    return a list with no duplicates
    Cf. http://stackoverflow.com/questions/89178
    """
    seen = set()
    seen_add = seen.add
    return [item for item in items if item not in seen and not seen_add(item)]
