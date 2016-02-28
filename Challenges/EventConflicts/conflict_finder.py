# Find conflicting events
from collections import deque
from heapq import heappop, heappush

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

    def append(self, event):
        assert event.start < self.end
        assert self.start < event.end
        self.events.append(event)

def get_conflicts(events):
    events.sort(key=lambda event: (event.start, event.end))
    conflict_candidates = _get_conflict_candidates(events)
    _insert_events(conflict_candidates, events)
    return _filter_true_conflicts(conflict_candidates)

def _filter_true_conflicts(conflict_candidates):
    conflicts = []
    for candidate in conflict_candidates:
        if len(candidate.events) > 1:
            conflicts.append(candidate)
    return conflicts

def _insert_events(conflicts, events):
    i = 0
    for event in events:
        # add event to each overlapping conflict
        while i < len(conflicts) and conflicts[i].start < event.start:
            i += 1
        j = i
        while j < len(conflicts) and conflicts[j].end <= event.end:
            conflicts[j].append(event)
            j += 1

def _get_conflict_candidates(events):
    divisions = _get_divisions(events)
    conflict_candidates = []
    for i in range(len(divisions) - 1):
        conflict_candidates.append(Conflict(divisions[i], divisions[i + 1]))
    return conflict_candidates

def _get_divisions(events):
    divisions = []
    for event in events:
        heappush(divisions, event.start)
        heappush(divisions, event.end)
    div_deduped = []
    while len(divisions):
        division = heappop(divisions)
        if not len(div_deduped) or division > div_deduped[-1]:
            div_deduped.append(division)
    return div_deduped

if __name__ == '__main__':
    events = [Event('A', 1, 9), Event('B', 3, 6), Event('C', 4, 7), Event('D', 3, 5)]
    conflicts = get_conflicts(events)
    for conflict in conflicts:
        print(conflict)
