import bisect
from sortedcontainers import SortedDict

class MyCalendar:
    def __init__(self):
        self.treeMap = SortedDict()

    def book(self, start: int, end: int) -> bool:
        index = self.treeMap.bisect_left(start)
        if index > 0 and self.treeMap.values()[index-1] > start:
            return False
        if index < len(self.treeMap) and self.treeMap.keys()[index] < end:
            return False
        self.treeMap[start] = end
        return True


