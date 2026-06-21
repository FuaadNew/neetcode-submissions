class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisDict = {'(':')', '{': '}', '[':']'}
        stack = []
        for c in s:
            if c in parenthesisDict:
                stack.append(c)
            else:
                if not stack or parenthesisDict[stack.pop()] !=c:
                    return False
        return not stack
         