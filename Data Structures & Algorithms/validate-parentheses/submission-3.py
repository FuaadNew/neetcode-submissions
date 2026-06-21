class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in closeToOpen:
                stack.append(c)
            else:
                if not stack or closeToOpen[stack.pop()] !=c:
                    return False
        return not stack