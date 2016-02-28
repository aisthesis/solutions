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
    # sort events by start time
    events.sort(key=lambda event: event.start)
    # maintains sort by end, then start
    conflict_candidates = []
    for event in events:
        insert_for_event(conflict_candidates, event)
        i = len(conflict_candidates) - 1
        while i >= 0 and event.start < conflict_candidates[i].end:
            conflict_candidates[i].append(event)
            i -= 1
    conflicts = []
    for cand in conflict_candidates:
        if len(cand.events) > 1:
            conflicts.append(cand)
    return conflicts

def insert_for_event(conflicts, event):
    conflict_stack = deque()
    conflict_stack.append(Conflict(event.start, event.end))
    i = len(conflicts) - 1
    while i >= 0 and event.start < conflicts[i].end:
        conflict_stack.append(Conflict(event.start, conflicts[i].end))
        i -= 1
    while len(conflict_stack) > 0:
        insert_conflict(conflicts, conflict_stack.pop())

def insert_conflict(conflicts, conflict):
    # if conflict already present, do nothing
    if find(conflicts, conflict) >= 0:
        return False
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
    return True

def find(conflicts, conflict):
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
