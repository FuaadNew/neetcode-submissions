class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the internvals
        intervals.sort(key=lambda i:i[0])
        output = []
        #populate the output with first element
        output.append(intervals[0])
        
        #for every start, end in intervals
        for start,end in intervals:
        
            #grab the last element addded to the output
            lastEnd = output[-1][1]
            
            #is the current start less than or equal to the last end
            if start <= lastEnd:
                output[-1][1] = max(end,lastEnd)
                #make the last intervals new end the latest end 
               
            #add interval if they are not overlapping
            else:
                output.append([start,end])
        return output
            
               
       



        