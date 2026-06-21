"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #make array for start
        start = sorted([i.start for i in intervals])
        #make array for end
        end = sorted([i.end for i in intervals])
        # make res and count var
        res,count = 0,0
        # intialize both indexes
        s,e = 0,0
        while s<len(intervals):
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(res,count)
        return res

        