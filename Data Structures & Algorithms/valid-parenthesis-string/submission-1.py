class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin + 1, leftMax - 1
            if leftMin < 0:
                return False
            if leftMax < 0:
                leftMax = 0
        return leftMax == 0
