"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i:i.start)
       

        prevInterval = intervals[0]
        for i in range(1,len(intervals)):
            
            if prevInterval.end <= intervals[i].start:
                prevInterval = intervals[i]
            else:
                return False

        return True
