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
        intervalsList = []
        for interval in intervals:
            intervalsList.append((interval.start, interval.end))
        
     
        intervalsList.sort()

        prevInterval = intervalsList[0]
        for i in range(1,len(intervalsList)):
            
            if prevInterval[1] <= intervalsList[i][0]:
                prevInterval = intervalsList[i]
            else:
                return False

        return True
