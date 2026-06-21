class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        res = []
        while i < len(intervals):
            start,end = intervals[i]
            j = i + 1
            while j < len(intervals) and end >= intervals[j][0]:
                new_start,new_end = intervals[j]
                end = max(end,new_end)
                j+=1
            res.append([start,end])
            i = j
        return res

        