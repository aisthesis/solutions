# Find conflicting events
from collections import deque

class Event(object):

    def __init__(self, name, start, end):
        assert start < end
        self.name = name
        self.start = start
        self.end = end

    def __repr__(self):
        return '({}, {}, {})'.format(self.name, self.start, self.end)

class Conflict(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.events = deque()

    def __repr__(self):
        parts = deque('{')
        parts.append('start: {}, '.format(self.start))
        parts.append('end: {}, '.format(self.end))
        parts.append('events: [')
        parts.append(', '.join([repr(event) for event in self.events]))
        parts.append(']}')
        return ''.join(parts)

    def __eq__(self, other):
        if self.start != other.start:
            return False
        if self.end != other.end:
            return False
        return True

    def append(self, event):
        assert event.start < self.end
        assert self.start < event.end
        self.events.append(event)

def get_conflicts(events):
    # maintains sort by end, then start
    conflict_candidates = _get_conflict_candidates(events)
    return conflict_candidates

def _get_conflict_candidates(events):
    # comprehensive but unpopulated list of all
    # possible conflicts
    # sorted by end time, then start time
    conflict_candidates = []
    events.sort(key=lambda event: event.end)
    # populate with all possible end times
    for event in events:
        _insert_conflict(conflict_candidates, Conflict(event.start, event.end))
    # now enrich with conflicts where start and end are derived
    # from different events
    events.sort(key=lambda event: event.start)
    first_overlap_ix = 0
    conflict_stack = deque()
    for event in events:
        # move forward to first possible overlap
        while first_overlap_ix < len(conflict_candidates) and 
                conflict_candidates[first_overlap_ix].end <= event.start:
            first_overlap_ix += 1
        runner_ix = first_overlap_ix
        while runner_ix < len(conflict_candidates):
            pass
    return conflict_candidates 

def _insert_conflict(conflicts, conflict):
    # safe insertion:
    # does nothing if conflict already present
    # otherwise inserts conflict into correct place in list
    # if conflict already present, do nothing
    if _find(conflicts, conflict) >= 0:
        return
    # conflicts are sorted by end, then start
    conflicts.append(conflict)
    i = len(conflicts) - 1
    while i > 0 and conflict.end < conflicts[i - 1].end:
        conflicts[i] = conflicts[i - 1]
        i -= 1
    while i > 0 and conflict.end == conflicts[i - 1].end and conflict.start < conflicts[i - 1].start:
        conflicts[i] = conflicts[i - 1]
        i -= 1
    conflicts[i] = conflict

def _find(conflicts, conflict):
    if len(conflicts) == 0:
        return -1
    return _find_rec(conflicts, conflict, 0, len(conflicts))

def _find_rec(conflicts, conflict, start_ix, end_ix):
    # return index if found, -1 otherwise
    if start_ix >= len(conflicts):
        return -1
    if start_ix + 1 >= end_ix:
        if conflicts[start_ix] == conflict:
            return start_ix
        return -1
    mid_ix = (start_ix + end_ix) // 2
    if conflicts[mid_ix].end < conflict.end:
        return _find_rec(conflicts, conflict, mid_ix + 1, end_ix)
    if conflict.end < conflicts[mid_ix].end:
        return _find_rec(conflicts, conflict, start_ix, mid_ix)
    if conflicts[mid_ix].start < conflict.start:
        return _find_rec(conflicts, conflict, mid_ix + 1, end_ix)
    if conflict.start < conflicts[mid_ix].start:
        return _find_rec(conflicts, conflict, start_ix, mid_ix)
    return mid_ix

if __name__ == '__main__':
    events = [Event('A', 1, 9), Event('B', 3, 6), Event('C', 4, 7), Event('D', 3, 5)]
    conflicts = get_conflicts(events)
    for conflict in conflicts:
        print(conflict)
