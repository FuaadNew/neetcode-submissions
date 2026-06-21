class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # map every character to last occurence
        lastIndex = {}
        for i,c in enumerate(s):
            lastIndex[c] = i
            
        #create result array
        res = []
        #maintain size and end
        size,end = 0,0
        # interate through every index and character
        for i,c in enumerate(s):
            #increment size of partition whenever we see character
            size+=1
            #update end of partition of lastindex of character is greater than current end
            end = max(end,lastIndex[c])
            #stop partiion if we reach end
            if i == end:
                #add to result the size of the partition
                res.append(size)
                size = 0
                #reset size
        return res
                
        


       
        