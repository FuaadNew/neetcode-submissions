class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2:
            return False
        closed_to_open = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in closed_to_open:
                if not stack or stack[-1] != closed_to_open[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack
            