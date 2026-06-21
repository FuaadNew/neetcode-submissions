class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisDict = {'(':')', '{': '}', '[':']'}
        stack = []
        for char in s:
            if char in parenthesisDict:
                stack.append(char)
            else:
                if not stack or parenthesisDict[stack.pop()] != char:
                    return False
        return not stack