class Solution:
    def checkValidString(self, s: str) -> bool:
        #create leftmin and leftMax variables
        leftMax,leftMin = 0,0
        

        # go through every character in string
        for c in s:
            #if we get a left parenthesis we increment both leftmin and leftMax
            if c =='(':
                leftMax,leftMin = leftMax + 1,leftMin + 1
            
            #if we get a right parenthesis we decrement both leftmin and leftMax
            elif c ==')':
                leftMax,leftMin = leftMax - 1 ,leftMin - 1
            
                #else if we have a wildcard character
            else:
                leftMax,leftMin = leftMax + 1 ,leftMin - 1
                # we decrement leftMin and increment leftMax
                
            # if leftMax is negative return False
            if leftMax < 0:
                return False
            # if leftMin is negative we set it to zero
            if leftMin < 0:
                leftMin = 0
            
        #return leftMin equals 0
        return leftMin == 0
        



