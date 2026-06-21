class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # if newinterval end is less than interval i's start
                #append to res and everything after
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if nre intervals start is is greater than intervals i's end
            #append to result
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                # else there is a conflict and we merge the intervals
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        
                
        res.append(newInterval)
        return res
        #insert just in case 
        
