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
        
    def __lt__(self, other):
        # sort on start ascending and end descending
        if self.start < other.start:
            return True
        if other.start < self.start:
            return False
        if other.end < self.end:
            return True
        return False

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
        parts.append(', '.join([repr(event) for event in events]))
        parts.append(']}')
        return ''.join(parts)

    def append(self, event):
        assert event.start < self.end
        assert self.start < event.end
        self.events.append(event)

def find_conflicts(events):
    events.sort()
    # needs to stay sorted by ascending end time
    conflicts = []
    # endtimes will be maintained as a heap
    endtimes = []
    event_stack = deque()
    n_events = len(events)
    i = 0
    while i < n_events - 1:
        # load event stack
        curr_start = events[i].start
        heappush(endtimes, events[i].end)
        j = i + 1
        event_stack.append(events[i])
        while j < n_events and events[j].start < endtimes[0]:
            event_stack.append(events[j])
            heappush(endtimes, events[j].end)
            if events[j].start > curr_start:
                curr_start = events[j].start
            j += 1
        if len(event_stack) > 1:
            # create a new conflict
            conflicts.append(Conflict(curr_start, _popincreasing(endtimes)))
            while len(event_stack) > 0:
                k = 0
                event = event_stack.pop()
                while k < len(conflicts) and event.start < conflicts[-1 - k].end:
                    conflicts[-1 -k].append(event)
                    k -= 1
            # TODO unload event stack
        else:
            k = 0
            event = event_stack.pop()
            while k < len(conflicts) and event.start < conflicts[-1 - k].end:
                conflicts[-1 -k].append(event)
                k -= 1
        i = j
    return conflicts

def _popincreasing(heap):
    item = heap[0]
    while len(heap) > 0 and heap[0] == item:
        heappop(heap)
    return item

if __name__ == '__main__':
    events = [Event('A', 1, 9), Event('B', 3, 6), Event('C', 4, 7), Event('D', 3, 5)]
    for event in events:
        print(event)
    conflict = Conflict(3, 4)
    conflict.append(events[0])
    conflict.append(events[1])
    conflict.append(events[3])
    print(conflict)
