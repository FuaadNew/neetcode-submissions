"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)
        if not intervals:
            return True
        lastEnd = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < lastEnd:
                return False
            lastEnd = interval.end
        return True

